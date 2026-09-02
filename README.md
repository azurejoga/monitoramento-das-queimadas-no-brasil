# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3492aa4b-d300-3f7a-a6b0-753e0fd7f761 | -6.6949 | -58.7485 | 2026-09-02 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 73100876-49b1-3762-849d-56f3eaff6e7b | -6.6948 | -58.7678 | 2026-09-02 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 03beec0c-eb69-3270-866b-e6209891cca5 | -13.4254 | -43.8639 | 2026-09-02 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0ed83d97-98fd-3c84-87df-6b55d5385a59 | -7.2191 | -60.6699 | 2026-09-02 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| be7f0c3a-9a55-3d97-848e-55d392080b3c | -17.0878 | -56.8534 | 2026-09-02 00:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| f04cb815-48a8-39b1-90ac-156f019c4a98 | -13.4059 | -43.8673 | 2026-09-02 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6ebf0926-8232-3f68-9b7c-46c1f9f202dd | -7.7344 | -60.974 | 2026-09-02 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 8ed4222f-29f4-3b37-96db-5646b0047d1e | -8.511 | -50.2969 | 2026-09-02 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 39fea34f-ceca-34bd-b67b-ae54ee9e6aa2 | -10.7165 | -46.1716 | 2026-09-02 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 0d8e2844-5ac9-3dff-8f35-9f99f0afdca7 | -7.77 | -61.2015 | 2026-09-02 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| a63d245d-3310-3e2d-801e-652c8c7b6d1b | -7.2005 | -60.6897 | 2026-09-02 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| bc4dd0fe-df49-30e4-bab0-1201750731a2 | -4.5008 | -45.9054 | 2026-09-02 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 88cc4ce1-4e14-35a4-9dd7-12fdaae64833 | -8.279 | -54.9174 | 2026-09-02 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| a4eb06d7-65bc-305d-82fe-55e0edbb81fd | -7.2006 | -60.6706 | 2026-09-02 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| c2813e3a-7dbb-3623-a9e2-8e0e0569c085 | -8.7612 | -62.6058 | 2026-09-02 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 34.1 |
| aa2cd103-ff5b-3ad5-bd20-58dfe99d95c6 | -10.8818 | -45.3534 | 2026-09-02 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 3efd2458-ef87-3bfb-9213-272b0a25d526 | -9.7267 | -47.7606 | 2026-09-02 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 57d73d59-2939-3e02-8d0b-b9866cbd4bc0 | -8.4922 | -50.2985 | 2026-09-02 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| b2401935-81a2-3ff8-9d22-237525f39ddb | -6.6764 | -58.7686 | 2026-09-02 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9281b154-706b-31d8-8b93-8fd236b66eb8 | -4.1183 | -51.0278 | 2026-09-02 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 09393a48-0917-3bf8-b6aa-d178fbae0112 | -10.0291 | -46.4364 | 2026-09-02 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 0334691d-38c6-3d6b-a36b-4c06a3f57839 | -11.6815 | -50.1932 | 2026-09-02 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9b00665d-5092-3192-81b7-21132e08c27c | -11.112 | -51.5536 | 2026-09-02 00:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| e810ac45-117d-323f-becf-d0af878440f7 | -5.8537 | -57.5576 | 2026-09-02 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 82739c44-5e63-38be-b152-0bf3498a09b7 | -8.1298 | -54.9471 | 2026-09-02 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 6e0aa055-bc8b-3499-b976-d54769b383b0 | -10.7161 | -46.1942 | 2026-09-02 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 8590fd61-bc27-3bce-9845-f46415a3f54f | -11.3328 | -50.6607 | 2026-09-02 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 1881f168-7f2c-3c17-b207-6ade6661bfd2 | -3.8604 | -44.0585 | 2026-09-02 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 245f1a3e-a528-36f7-ae8c-f6ad2c9cb0d6 | -7.219 | -60.689 | 2026-09-02 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 7ff07767-d61b-3d67-ab69-a3c2fe905c47 | -3.8417 | -44.0594 | 2026-09-02 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 04584ad2-fc36-312a-948a-6ea15b624ce1 | -8.2791 | -54.8973 | 2026-09-02 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| ba508e5a-cbe4-3eaf-ab5d-f56ca5bf12fa | -11.6624 | -50.1954 | 2026-09-02 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| c915390a-8dad-35a0-8ead-4711a304b75d | -8.7613 | -62.5869 | 2026-09-02 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.6 |
| f2ba4b31-11b3-3cce-8fba-0457c7a6161e | -8.1112 | -54.9483 | 2026-09-02 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 967da02e-02c5-36eb-b913-b1689c79178c | -8.7428 | -62.5876 | 2026-09-02 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 2d353f29-4a6b-32e4-a9f1-520fdbecc4aa | -9.8806 | -64.9764 | 2026-09-02 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 110.4 |
| e8e41aa9-7dc9-39a6-9b10-634700c4376e | -9.862 | -64.9771 | 2026-09-02 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 2888dbb2-2641-3222-b3bc-186335439af9 | -10.9009 | -45.3509 | 2026-09-02 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 86798308-c2be-38f2-a508-067eb1af9681 | -8.911 | -62.372 | 2026-09-02 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 4b49225a-84ca-3a91-8d1d-c0b995fc40a8 | -11.3331 | -50.6394 | 2026-09-02 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a6a5ea56-820b-3fa4-a7b3-9bafdd4748eb | -11.7903 | -50.545 | 2026-09-02 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 320.8 |
| 2312b89d-c81a-3533-9a53-0963b9880e08 | -8.7613 | -62.5869 | 2026-09-02 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4841bdb8-c2be-3be4-b19e-099d9c001b1b | -4.5008 | -45.9054 | 2026-09-02 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ae728e82-3341-3cb7-84dd-66228c766068 | -7.77 | -61.2015 | 2026-09-02 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 752cda42-c7fb-3b25-beaf-fe9760165e22 | -6.1844 | -57.7395 | 2026-09-02 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| bc6884f4-082a-36d5-a679-254fc11933b6 | -8.1298 | -54.9471 | 2026-09-02 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 7271ad92-b91b-3815-8e8b-af63bc056539 | -8.911 | -62.372 | 2026-09-02 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 2e09bb5b-5730-3208-a0a4-b909e730fc50 | -10.9009 | -45.3509 | 2026-09-02 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| bd2ff9fa-f43a-33e6-bc40-cd4c5eb49e1e | -3.1083 | -61.238 | 2026-09-02 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8d67d63a-bfb1-318e-895c-5b48f576152f | -11.6624 | -50.1954 | 2026-09-02 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| fca91df7-24c2-3a81-839a-124d43a3d9b1 | -8.511 | -50.2969 | 2026-09-02 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7e873a35-58de-3b0b-9d99-8d7c458fb589 | -8.2236 | -62.7405 | 2026-09-02 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bd6a364b-d09e-385f-b44e-d368fc16f83d | -11.7713 | -50.5472 | 2026-09-02 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 272.7 |
| 184428c6-12f1-300a-acd6-27e0794b7981 | -9.862 | -64.9771 | 2026-09-02 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 15bba419-ce10-35ca-b69a-c5effb8ae58c | -3.8604 | -44.0585 | 2026-09-02 00:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c034fd22-d072-3c40-82d0-45d099666e74 | -8.4922 | -50.2985 | 2026-09-02 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 60e76466-db48-3645-9fb1-abb71265e2b8 | -10.6841 | -54.0451 | 2026-09-02 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 33ca740e-93ec-3313-a6fb-62b047aa97b7 | -17.0878 | -56.8534 | 2026-09-02 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| ffcec5cc-14ad-3101-92b3-8e201cf71963 | -11.79 | -50.5664 | 2026-09-02 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1086b24d-7df0-3dd9-89c3-a67ae77eda85 | -7.7344 | -60.974 | 2026-09-02 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f5631573-aa1a-3788-997e-28e27ade5109 | -5.8537 | -57.5576 | 2026-09-02 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 348f8435-5905-34de-90f3-372a7ba7d1e7 | -7.2191 | -60.6699 | 2026-09-02 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 4611a17c-a9cb-3638-8422-b761854d2af1 | -13.4059 | -43.8673 | 2026-09-02 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a783a43b-b130-345b-876f-0c5e41a6d32d | -6.6948 | -58.7678 | 2026-09-02 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 4d060d6f-19f7-3281-b369-d59c9bf78e57 | -7.2005 | -60.6897 | 2026-09-02 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| e5f48318-1629-3cfa-bf97-18bbefe07bbe | -16.2123 | -47.4874 | 2026-09-02 00:10:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| bcf822ad-55f8-3a6a-9149-bff4f204ad4d | -11.7716 | -50.5258 | 2026-09-02 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 187.4 |
| ffa06675-ecfb-32b0-9ed8-d64e81712218 | -9.7267 | -47.7606 | 2026-09-02 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 8f6e9ca9-b073-361a-aee9-0d715eac8df5 | -4.1183 | -51.0278 | 2026-09-02 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d690b25d-02f1-3336-9fc0-59fdf13c197b | -8.2235 | -62.7594 | 2026-09-02 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 65cf4881-4693-32a5-a6f9-9c480b294794 | -9.8806 | -64.9764 | 2026-09-02 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.1 |
| cc1b9d84-ce32-30f5-a688-6286f3b6eb31 | -11.7906 | -50.5236 | 2026-09-02 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 62fc027b-a89a-356b-9043-89c135d20594 | -6.6764 | -58.7686 | 2026-09-02 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 40562dff-06e4-3e75-a95d-01961d8df54b | -7.2006 | -60.6706 | 2026-09-02 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| ad199dd1-73ad-35e8-aaa2-4642f87a5a77 | -6.6949 | -58.7485 | 2026-09-02 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 56b5baa9-5922-3a72-8c9b-66ab95a189aa | -8.42 | -54.68 | 2026-09-02 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27296ed0-b962-31f7-9e82-f4709386b2dc | -8.46 | -54.76 | 2026-09-02 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98df536a-518c-3810-91ee-3d557a3cfed9 | -8.43 | -54.75 | 2026-09-02 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1efb5b98-760a-3c97-a521-45f371b5b521 | -11.76 | -50.55 | 2026-09-02 00:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15d2bb18-bb9f-3a7e-b7c7-3432119e71ce | -12.14 | -47.09 | 2026-09-02 00:15:00 | MSG-03 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cab780e3-c082-3c47-84d3-f99e39551747 | -12.14 | -47.14 | 2026-09-02 00:15:00 | MSG-03 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 552ce78b-25fe-3260-b242-a96a824bdaed | -11.76 | -50.61 | 2026-09-02 00:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d77351ec-ddc1-3442-8eb2-5f87191a55f1 | -11.79 | -50.56 | 2026-09-02 00:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 619952f2-b497-3d0f-8c3d-84e9ac45b51d | -8.45 | -54.69 | 2026-09-02 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67a690d2-9cd0-3a14-a5b9-00e1893f7c33 | -16.7339 | -47.0688 | 2026-09-02 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 174.2 |
| f9db89c5-3a00-3607-ab88-9dbe591f0435 | -10.6841 | -54.0451 | 2026-09-02 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 60a3189f-8947-3e34-8aef-ae5c4b4c4cdd | -13.4059 | -43.8673 | 2026-09-02 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| b687ae8e-9b8b-3fb7-94dc-7c0c48c9bd3c | -16.2128 | -47.4645 | 2026-09-02 00:20:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 118.1 |
| ca588c9e-d1eb-3e20-9f3b-e905e80bd114 | -16.7334 | -47.0918 | 2026-09-02 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 3ddecb94-5a07-395b-a4ae-2baae0183146 | -4.1183 | -51.0278 | 2026-09-02 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ae137e5c-917c-3823-9fea-531661aacd1c | -8.2236 | -62.7405 | 2026-09-02 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 83d50085-b337-3ac2-ba2b-509fd61a6037 | -16.1926 | -47.491 | 2026-09-02 00:20:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 14ee5969-ec69-31ec-a3ac-c77a0a96930c | -6.6948 | -58.7678 | 2026-09-02 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0a35cadc-6a42-3ec0-a3d3-9c36fcdca2b4 | -11.6624 | -50.1954 | 2026-09-02 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.6 |
| dd49083c-c0ee-36fb-9756-502bb3daf297 | -16.2123 | -47.4874 | 2026-09-02 00:20:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 2d837a34-8120-3f36-81f6-f6cc843f31aa | -5.8537 | -57.5576 | 2026-09-02 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| a76551f3-4a0e-35ff-9d29-86d0c266b695 | -7.2006 | -60.6706 | 2026-09-02 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 12d2f753-52ae-375d-a1e5-77ab33e292c3 | -16.7538 | -47.0649 | 2026-09-02 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a1aa2529-3bb0-38d9-8446-4d5b3342cd88 | -3.8604 | -44.0585 | 2026-09-02 00:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ec68f340-033d-3de0-ac14-460d05289df5 | -9.8806 | -64.9764 | 2026-09-02 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.1 |


[Clique aqui para ver as próximas entradas](README2.md)
