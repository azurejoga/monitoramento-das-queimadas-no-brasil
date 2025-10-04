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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4de7dfcd-94c4-32b4-9ce4-96908538a406 | -14.91595 | -46.88464 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f71bc645-8b12-3a7d-bc05-49167eca8fee | -13.40984 | -43.68879 | 2025-10-04 03:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a595dd2-b057-386a-ae96-fac24fee5881 | -12.59475 | -49.88917 | 2025-10-04 03:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4089f33-3689-387d-917d-94b2bb6ecfd2 | -11.88654 | -44.99201 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f8ec3da-8d43-3c7d-a559-979ec19098b3 | -13.67628 | -47.30465 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c13e2770-9705-385c-9a61-551018ed42e5 | -14.39004 | -45.949 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1627b236-cfbc-303a-8ec3-1d5930f6575c | -13.26577 | -46.47515 | 2025-10-04 03:53:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4a9e20f-5e18-3420-b4a8-876adc6844ec | -13.20806 | -47.81018 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4cfbce9-e0a5-35ab-8be0-c25e201dfc18 | -13.9955 | -48.18762 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74a05e7c-117c-3378-bf68-a8ac3f57f7b1 | -13.40918 | -43.69249 | 2025-10-04 03:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eab6bb5-1f40-3d7b-a6f5-9a15dbd9bdf8 | -12.59383 | -49.88441 | 2025-10-04 03:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85260ec7-61ac-34d1-a387-2559c219ce6c | -13.75534 | -48.05494 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 78d96b4f-3725-37f1-a21e-6145f8b582ee | -12.52537 | -45.97957 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3043b12c-72b8-3d17-a5f2-a361cfec51e6 | -12.29232 | -45.36528 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca061c54-6312-387f-bab8-eff9b5ec59d2 | -14.91977 | -46.89123 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eaa319df-d58c-35fe-92a2-bacf5b32799d | -11.79239 | -46.82899 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| acb08658-5aa3-3028-ae83-8e1c37cfbec7 | -14.84689 | -48.28352 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9340e13-ed04-3bd6-b1f3-c4499ab6a3f8 | -14.16362 | -49.21151 | 2025-10-04 03:53:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cecb46f9-5f09-349a-be11-3d54fc84a43e | -13.11587 | -47.84436 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d93caa9c-e3cd-3d2a-a63c-88e0741feb84 | -11.59438 | -47.04618 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7207eea1-4fda-3df3-8238-3a4a70f47f62 | -13.10214 | -47.88519 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a7656ba-9202-351a-be58-8d62a6ca8fbe | -12.59461 | -47.00158 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ecfdad7-a33d-33cc-b41a-e573bd086265 | -14.75333 | -48.14383 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4effc72-b659-38d8-a2a7-ab5e8ded05b8 | -13.13239 | -47.81732 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52fe1abd-6819-36fa-8d2b-72ff9e55bcf2 | -13.21655 | -47.82338 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84ac501b-5d74-3b9c-a31c-172ffb69f5d4 | -13.98169 | -48.20072 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6f1f0b5-10f0-356a-95fc-be2e1db52837 | -14.65831 | -48.3129 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8e40f9af-f4ef-3ab4-b294-dae4dfcd7674 | -14.68223 | -48.07042 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9884bfc5-fbf4-34b7-a6ae-c13b722cf1ca | -13.31571 | -47.24305 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9136618-a5a1-3841-9c25-3cc4f524a0ac | -16.01204 | -50.93505 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a4152abe-00cf-3964-8841-94f68871b918 | -13.20741 | -47.8036 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feb8ab62-5d93-30a4-b55d-91163380a49c | -11.28021 | -47.79649 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77a3101c-1b15-3033-bc47-248d832e3d1b | -13.66652 | -47.87286 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3879846-139e-394e-9fec-b89f06ce8182 | -16.08706 | -51.06618 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43042025-d7a6-34c9-bb69-3c33ba0034ff | -11.90884 | -46.24936 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 261b4171-b233-312e-b3e6-c353685d4cd1 | -11.10111 | -49.85426 | 2025-10-04 03:53:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc5ac4b8-19f6-3887-b104-9e7f589ce5d4 | -14.93613 | -49.9729 | 2025-10-04 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f477c3da-c667-30a5-a72e-d56ce251ec9b | -17.0881 | -46.24747 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ec1e7f90-6566-36b8-95c4-97f20410e7be | -13.30749 | -48.13629 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee90389e-d147-3749-a1fa-b6d9fb83a32c | -13.31947 | -47.60944 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5c9a6d5-e920-3507-b966-d456e59e5288 | -11.84223 | -45.02829 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3a4e441-4235-3116-a0aa-9f4233e1fada | -14.46478 | -48.39867 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34c5d9ea-e4c9-35bd-b93d-0eaf0950728c | -17.61445 | -44.46293 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dec73642-2d3f-37e2-ba91-67503da50599 | -12.64195 | -46.98603 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 888b3b26-9495-3134-bd31-692f93c57f55 | -15.32486 | -46.30689 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 120d6293-c2d2-3079-a2ef-7d9d216d3eeb | -12.65017 | -46.97108 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 083fe213-b490-3f0d-96de-a5c26edcc99b | -13.21032 | -47.81729 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35392465-bec1-362b-8d0a-c7deb0c74ce0 | -12.19706 | -47.77827 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7db0ffb2-a4a4-3e96-a634-259a392f1547 | -13.28846 | -47.18642 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b350883-1eff-3b96-b3b7-595d02646973 | -13.73843 | -47.93046 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ecf9f1c-b0d4-33cf-8dcf-9428b2a64e3f | -14.63265 | -48.24659 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86747ad4-6cba-3912-9941-7b549d268d2f | -13.39349 | -47.28312 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8752112-2ddb-3523-bfd0-cd909d440b6f | -13.26204 | -47.24013 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 349e47cf-74bf-31b1-b6dd-aa629c9d4968 | -14.63601 | -48.25748 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1980c20b-2dba-31e6-aa63-f65e599cf872 | -14.16452 | -49.20715 | 2025-10-04 03:53:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 076c7e4c-2510-3a32-80ff-3401231b6377 | -13.31824 | -47.25731 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a78a6192-5cd8-3364-926b-f2d816cdb44b | -15.19561 | -46.39318 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69699507-2318-3125-8a70-3e94250734d7 | -12.92882 | -46.37388 | 2025-10-04 03:53:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4de76b3e-f977-3243-ab61-3f0c6efcb8b4 | -13.20414 | -47.80198 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d40489d-8feb-3be0-b87f-a0190433465e | -11.92628 | -46.3747 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 33620ecf-89e3-3d8b-8262-55cf82f5e317 | -14.65141 | -48.2367 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e5a9b1c-091d-3dc6-8fc6-029fa522ba30 | -13.10794 | -47.84641 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5910abe-deb6-31e7-8bce-63f940e26dff | -15.60169 | -52.46852 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31c2d9ac-48d3-3ddc-98d7-bb84c92a2c2a | -14.44055 | -46.38184 | 2025-10-04 03:53:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e145145f-902e-317c-8c7d-ad4c6386278a | -13.33056 | -47.58046 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f73e72a3-f89c-346c-85ca-5cc5fb6edfd1 | -13.51279 | -47.28116 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8ab1ff0-f1c5-3cda-a3b0-716fd82ad7df | -16.36367 | -51.4729 | 2025-10-04 03:53:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78d2338b-2587-37fc-953c-db3786e4bcd6 | -15.59601 | -52.49444 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec34b784-7a9d-33e2-a440-5ae632caf517 | -12.08879 | -45.17313 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 569ef3ae-adac-32bd-8871-3c80238faec5 | -13.16262 | -44.63902 | 2025-10-04 03:53:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ba5eb5f-97db-3219-b9ec-f9a666dcd3ab | -17.57644 | -44.48993 | 2025-10-04 03:53:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bbc0d7f-07d2-3236-b722-bc3fe2bdb195 | -11.92555 | -46.35118 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cca64281-344d-3542-94a0-05b7ac1456dc | -15.7309 | -46.27307 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d898013-9c36-3e7f-9221-04afd06d5915 | -13.99335 | -48.20253 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c472cc0d-a2ab-3991-8267-a39812f056f6 | -11.86282 | -44.96722 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b86e5fa-dc2b-35a4-9ae8-3dda5d002549 | -11.78344 | -46.82008 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ee460d6-9e44-31a9-8a32-04c35f6e7e3c | -14.65752 | -48.3168 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 91e0b0e0-b258-3d48-bfb1-73e3293a5127 | -17.08243 | -46.23395 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c300ce0b-640d-3579-b28e-76a81401d6fa | -13.51792 | -47.28223 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ec975a2-b1bb-3cb5-ae48-719772560779 | -12.08165 | -45.1864 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65577cd3-586f-3039-8f05-b98f12600d1f | -13.20352 | -47.80507 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29c55b11-8432-30c1-bbde-45d05ba89651 | -13.27649 | -47.22075 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c9b16a6-0e15-3506-b5e7-5cf3bdb24f7b | -12.09335 | -45.17418 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83aec836-b49c-36e8-be91-82ff77c96b62 | -11.49931 | -46.75122 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47b2f88c-457f-365f-8c0f-1de6a48e9ea8 | -15.35267 | -46.299 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1e94ec91-5504-355c-b318-b9428dd4d1b8 | -12.91216 | -46.92511 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f33d8e4-5c36-3218-9d39-d675ade5dc27 | -16.75902 | -43.96816 | 2025-10-04 03:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3439d42-246b-3adc-ab58-60d5802eaf26 | -17.0796 | -43.36569 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e190107d-1f3f-32ba-b0eb-7f4d6f266b33 | -13.31498 | -47.24285 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa76edbb-bd1b-3753-af6e-fab619a06242 | -14.84617 | -48.28703 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46d9d14c-fe1e-3bd7-a2ba-a20c9689f8f8 | -15.36878 | -47.95459 | 2025-10-04 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cae936be-c4cf-3237-8c65-ff8f95ea458d | -12.60029 | -46.99972 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79dee5e0-8fb7-343d-a6d6-98385b745533 | -11.54203 | -47.67603 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57ba7fbe-ff2c-3e61-bbfe-8b87ad37b4b9 | -14.21972 | -44.78333 | 2025-10-04 03:53:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de0eed6f-402e-3ecf-8c00-c75f32661d99 | -11.90815 | -46.38857 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46fc3b7e-d035-3126-b290-24f875ce503e | -13.23686 | -47.83319 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c54a0dec-b378-3c6d-8748-f9a82d443b89 | -15.78527 | -42.04958 | 2025-10-04 03:53:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5dc4852b-ebb2-3559-8ca9-6eebb02768d4 | -12.8926 | -47.1672 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4abd0161-6e29-3236-b01c-52fc64abbc28 | -12.71811 | -48.56774 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77eb839d-f6c5-3874-837f-8cfdaf42342e | -14.88147 | -48.27784 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README41.md)
