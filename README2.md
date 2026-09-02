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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c43771e3-9b6a-362b-a318-6aab6e6ff48f | -6.6949 | -58.7485 | 2026-09-02 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 57bcd446-fb0c-35da-89ab-138f37748e94 | -8.7428 | -62.5876 | 2026-09-02 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 174b1d59-b3a4-30f7-8276-2237ef98e0f2 | -11.7906 | -50.5236 | 2026-09-02 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 174.1 |
| ac681aad-dfa8-3457-8865-4ded12b6a61e | -8.911 | -62.372 | 2026-09-02 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 22f94456-45fa-37c4-bc61-f720e5559f44 | -10.7161 | -46.1942 | 2026-09-02 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| b363b1e5-b17e-3938-ba54-b2c771a4afcf | -8.2421 | -62.7398 | 2026-09-02 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b310d9a5-a880-3dff-870f-517f56d1a1a9 | -9.862 | -64.9771 | 2026-09-02 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7802715c-918b-3e03-ab81-881ba31e9012 | -11.7716 | -50.5258 | 2026-09-02 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 0721860d-9261-3ea3-8a79-c9471bd6effa | -8.2235 | -62.7594 | 2026-09-02 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d3b22134-4ae8-307b-add3-fbb1dd97279a | -16.1931 | -47.4682 | 2026-09-02 00:20:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 8292b7a6-f8fe-30d2-9223-b5ed9c749a1c | -8.1112 | -54.9483 | 2026-09-02 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 3366ceff-0423-3b94-9690-4ce703938719 | -8.511 | -50.2969 | 2026-09-02 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1a1fe5ab-166f-39b7-9262-0ca7ee2b236f | -8.7613 | -62.5869 | 2026-09-02 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 206.9 |
| 52fbca77-05fb-394b-8eec-29744479652c | -11.7713 | -50.5472 | 2026-09-02 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 200.2 |
| cb36a7c6-9c83-3f22-b43d-f8f4ce5bd95e | -8.7612 | -62.6058 | 2026-09-02 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| cafab9ec-c232-3179-a5fb-3e54d1078758 | -11.7903 | -50.545 | 2026-09-02 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 287.5 |
| 57a90444-6877-346c-b86a-105aadc015a5 | -8.1298 | -54.9471 | 2026-09-02 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 003da0f2-ef77-375e-a715-edadb9605d60 | -9.8806 | -64.9764 | 2026-09-02 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 1e4b453a-b2c6-3d80-bcad-0c77224e3139 | -11.7906 | -50.5236 | 2026-09-02 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| e6c10dac-0ac1-37df-b21f-1a4c43a2eff8 | -16.2123 | -47.4874 | 2026-09-02 00:30:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 6a7a6670-d128-3e57-a5d0-d6743423a4c7 | -9.862 | -64.9771 | 2026-09-02 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d729beff-8bed-3e8c-9961-fd169305579d | -8.1036 | -58.2749 | 2026-09-02 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| df01a0fe-a9d9-37d6-a4d8-0e976ce90048 | -8.1298 | -54.9471 | 2026-09-02 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| de4a29b2-df99-313e-bb4b-cdfd2e1c38c8 | -16.7345 | -47.0457 | 2026-09-02 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 08d55c67-6051-3a27-99ba-2d46ed18611b | -7.2005 | -60.6897 | 2026-09-02 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| b2d49af7-83bd-352b-8de2-44e8e7aeb68a | -16.2128 | -47.4645 | 2026-09-02 00:30:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 127.6 |
| c97c2ddd-d422-35aa-ba8d-aa6de9df83f6 | -4.1183 | -51.0278 | 2026-09-02 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e01b6998-4da6-326b-a20f-15ec38d41949 | -16.1931 | -47.4682 | 2026-09-02 00:30:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 9df2d2a0-5bd6-3b96-b60d-f6e19bee3775 | -11.7903 | -50.545 | 2026-09-02 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 782c8c6d-18ce-3343-92a9-a6ea8f95eb4f | -16.1926 | -47.491 | 2026-09-02 00:30:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 42aa320a-b096-3dff-9a65-f1a212ec17d1 | -8.7612 | -62.6058 | 2026-09-02 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 29.3 |
| b78dd4a2-48a6-33ef-b5ee-f9cf7bdbe75c | -16.7334 | -47.0918 | 2026-09-02 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 0247ebeb-7861-3663-b503-379b6937efee | -11.5291 | -45.4473 | 2026-09-02 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1eaebf36-4da2-3089-a5ef-570560c244e1 | -16.7532 | -47.088 | 2026-09-02 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1950f4fd-7600-3ed0-8e01-812527ccff77 | -7.2006 | -60.6706 | 2026-09-02 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 40e3ed7d-1dd7-3d10-a1cc-67e53d077bc3 | -6.6949 | -58.7485 | 2026-09-02 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3b58e463-fc51-308e-b465-00c40439f529 | -16.7538 | -47.0649 | 2026-09-02 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 2460b121-e8f3-3c02-a522-cace0f0e16df | -8.7613 | -62.5869 | 2026-09-02 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 3d381a80-2865-324c-abad-fdc9f66e6166 | -11.6624 | -50.1954 | 2026-09-02 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 7ba98658-d287-3d18-a357-9ed3da76aaa2 | -1.4761 | -54.2365 | 2026-09-02 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 0b7a0182-c548-36fd-987a-ea9c8fc217dd | -11.5287 | -45.4703 | 2026-09-02 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5a3b45a0-1253-3589-9c72-31fd58605b45 | -5.8537 | -57.5576 | 2026-09-02 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| fcf479eb-cc98-36aa-81c2-46b40bdc383d | -16.7543 | -47.0419 | 2026-09-02 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 86.4 |
| be0e495d-ff57-3ddc-acf1-ae7505f73230 | -11.7713 | -50.5472 | 2026-09-02 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 6a2e76e7-c6cb-3884-92c0-34591c9d147c | -7.77 | -61.2015 | 2026-09-02 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 24e638cc-a649-3f66-b525-9f1670acecfe | -10.6841 | -54.0451 | 2026-09-02 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 3eb90fa9-a744-38d6-8d2e-2b9321f01839 | -7.3671 | -60.6067 | 2026-09-02 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ff92f364-b857-3e71-ad84-eb9a8769c057 | -16.7339 | -47.0688 | 2026-09-02 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 355.8 |
| b663ced2-0677-3cf0-aa9e-147f30247504 | -6.6948 | -58.7678 | 2026-09-02 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 03a6eb86-bcb4-339a-bc52-6d37e2d45004 | -7.2191 | -60.6699 | 2026-09-02 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 4c84df4c-0786-34a9-9067-90dca269cba8 | -9.8806 | -64.9764 | 2026-09-02 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 94486d1e-9240-3139-ab60-da226a17fb76 | -12.1512 | -47.0833 | 2026-09-02 00:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9073b333-6b0b-3205-aa1f-1fcb36f6c5d0 | -7.2191 | -60.6699 | 2026-09-02 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| e1020f3a-aa5d-336c-8578-91c017991bea | -8.1112 | -54.9483 | 2026-09-02 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| bb80a0be-40b7-37ac-a7e0-29217debb879 | -16.1528 | -46.6517 | 2026-09-02 00:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 103.2 |
| fb026787-47e8-306e-8cdb-f2aada897232 | -7.77 | -61.2015 | 2026-09-02 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| f702c210-52c3-398c-bfcb-7c23b8f58906 | -4.5008 | -45.9054 | 2026-09-02 00:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 40d6551c-5a23-3a48-b90b-a3d608cd87a0 | -6.6949 | -58.7485 | 2026-09-02 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a6e101d6-8ac5-313f-bd0b-4706415655bd | -16.1926 | -47.491 | 2026-09-02 00:40:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 0b4b8bcc-4307-37f2-aa9c-8012f0f29bd7 | -11.7906 | -50.5236 | 2026-09-02 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 97317f4f-2e96-3053-b690-2e428d6445b4 | -16.1931 | -47.4682 | 2026-09-02 00:40:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 4267d2f5-31ff-35de-9110-b7c71ccb1e86 | -9.862 | -64.9771 | 2026-09-02 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| a072fb80-4527-38d7-8499-dae6d82523f2 | -16.2128 | -47.4645 | 2026-09-02 00:40:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 9c1f1425-a492-360e-9067-655a72bde75c | -16.7345 | -47.0457 | 2026-09-02 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 9a77ad06-e58d-3a1a-b4fe-1ff74c73e51c | -4.1183 | -51.0278 | 2026-09-02 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 3087309f-972e-3b61-811e-67d8aa5e60fc | -8.5728 | -63.1807 | 2026-09-02 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0d3464d0-2337-333e-ae66-28674060c3a8 | -6.6948 | -58.7678 | 2026-09-02 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7d404c92-e6b0-359e-9a04-2710affcdbcd | -16.7339 | -47.0688 | 2026-09-02 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 230.1 |
| 4ee563af-85dc-3baf-af0b-07f85c3d1d6b | -14.9895 | -47.9728 | 2026-09-02 00:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 8c2f9db1-7133-3bd8-8db3-adbc4ffcdb31 | -12.1704 | -47.0806 | 2026-09-02 00:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 537e6fc9-9777-3c61-80cc-ad4cad084b02 | -7.2006 | -60.6706 | 2026-09-02 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 32740d62-3c2e-3815-8ebf-70f9751d7185 | -12.1508 | -47.1058 | 2026-09-02 00:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 22a2c489-e5c5-3516-a348-9c2a0d0ddc0d | -8.2236 | -62.7405 | 2026-09-02 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 72ff8fc3-5bb1-3c97-a80a-745e582d5cf3 | -12.1896 | -47.0779 | 2026-09-02 00:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 56fc122b-09b2-301c-abbe-02cfc627c9bf | -12.1504 | -47.1283 | 2026-09-02 00:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| d285166b-204d-3de6-a622-c82991cb1d71 | -8.7613 | -62.5869 | 2026-09-02 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 95578244-54c8-3e86-9bca-32645fb18f1e | -8.5727 | -63.1996 | 2026-09-02 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1d7bf8cc-8b03-38aa-bb96-c7112117d475 | -15.1318 | -49.5942 | 2026-09-02 00:40:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| cb3beaba-03db-375c-91b0-f295328d516d | -12.1312 | -47.1309 | 2026-09-02 00:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 476e46dc-2aac-3123-a335-77b45a833dde | -16.2123 | -47.4874 | 2026-09-02 00:40:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 8f0e07e6-61e6-3f7f-b74e-761ac267013b | -9.4421 | -67.4535 | 2026-09-02 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6f283667-90bd-383b-97f2-e3b4eb10255f | -7.2005 | -60.6897 | 2026-09-02 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 2f0f3f4e-2adf-3828-865b-d7b3502cad05 | -10.6841 | -54.0451 | 2026-09-02 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 5bf9997a-abc2-32c5-b916-b07195c7950e | -16.7334 | -47.0918 | 2026-09-02 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 122.2 |
| d1033daf-8476-358c-b273-669060d17b0f | -11.6624 | -50.1954 | 2026-09-02 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 2481fe22-d3cf-341e-82bf-0893a6d28140 | -16.1534 | -46.6286 | 2026-09-02 00:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 9e4e5cce-cdfb-3add-a7f3-83b6519aca74 | -16.1726 | -46.648 | 2026-09-02 00:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 98ed4a6a-2b0a-3771-b55c-bf1d6b3ce134 | -16.7538 | -47.0649 | 2026-09-02 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 42b3e567-6037-34bb-be23-50da84793e35 | -7.3671 | -60.6067 | 2026-09-02 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 02033c72-ab05-3a6c-a527-e852376722f5 | -11.7903 | -50.545 | 2026-09-02 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 16e9b5df-efac-300f-ab7b-18ccd1d8f896 | -12.1516 | -47.0608 | 2026-09-02 00:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ea4ed084-98b1-334c-b25c-a64fc8140b39 | -5.8537 | -57.5576 | 2026-09-02 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 9f69a537-8c01-34d9-8437-6cc479d2970c | -6.6764 | -58.7686 | 2026-09-02 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b0ede758-365f-3692-b413-1cebef6bacbd | -8.1298 | -54.9471 | 2026-09-02 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| b9511e6d-c33c-3727-8b95-c5ddd9771925 | -4.1183 | -51.0278 | 2026-09-02 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 1f36a430-c390-3cff-8e3a-a48ca74b0674 | -8.1112 | -54.9483 | 2026-09-02 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6bef00a5-8e35-3bfc-933a-24ffcd69596a | -7.2006 | -60.6706 | 2026-09-02 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 64b51ed7-3b1f-3ad8-88fb-64d460d1c0e6 | -16.1926 | -47.491 | 2026-09-02 00:50:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 6403d962-ba3f-34c8-a558-a6410eedcbea | -6.6764 | -58.7686 | 2026-09-02 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 856601fd-d596-34b8-b8a4-50241a80c9a6 | -8.1298 | -54.9471 | 2026-09-02 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |


[Clique aqui para ver as próximas entradas](README3.md)
