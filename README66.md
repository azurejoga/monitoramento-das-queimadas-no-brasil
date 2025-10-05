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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5bd31de-7069-3003-9c86-8ab386d2f84d | -13.74044 | -48.07148 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efb17c83-8872-331d-91fc-414a1c9cdf74 | -12.10969 | -50.90008 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1b81a11-2126-3ea6-a827-de6eb9e2cff8 | -11.89257 | -44.98686 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe4f7264-1207-30d5-914e-37e5ecc4a8bc | -14.39644 | -45.94334 | 2025-10-05 03:55:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5b9d8c9-786c-39d2-bf36-465870b3af5c | -14.94821 | -46.85111 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| acaeb078-6f97-3789-90fe-897ca362810f | -15.61393 | -52.49864 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a3e7bbe-33ed-3f87-b39c-32e7df14086d | -13.72154 | -51.46314 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4f4ce23-c1ff-34e0-b1f8-3a9eebeecc31 | -15.87525 | -46.2598 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 446c4dde-224a-3a26-9774-6a35c496cc44 | -13.27803 | -47.61568 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d521ae3b-54d3-35d9-8cdc-23d4cbe61c73 | -14.92312 | -46.84357 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 49571f9f-12c7-3e57-94c1-8ceeb2c67557 | -11.59495 | -46.71042 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 017f0c10-7bf9-3b04-8faf-c229e1e386f0 | -15.38509 | -47.9403 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f771185-ba3b-3a0c-a0f3-b7737236bb53 | -11.63488 | -46.87416 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70d44be3-9dd7-36f6-a5f0-4f9f7c76795e | -16.03238 | -50.95229 | 2025-10-05 03:55:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b6d77a5-13c2-3212-b17b-5f33f0aac194 | -14.65661 | -48.34655 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a324834-26f1-31cb-8f96-5699207683b3 | -13.4836 | -47.28612 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1dabf54c-3ae7-3197-a85d-55e9f0b26ac4 | -14.01248 | -44.92531 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a923e95-30cf-3199-b67f-26eeeefc1cca | -11.0414 | -47.79379 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71097bff-d915-305b-9a3d-4241a48fc3a0 | -13.32851 | -47.18637 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 575eca33-c40d-371b-a158-0a9194eba001 | -15.70665 | -46.27736 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13df2398-f045-33f1-8e47-0f5569b30635 | -14.67443 | -48.35942 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a93fcb1b-931f-3238-82d8-f3f55120d07c | -11.49468 | -46.78387 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc704802-edf3-3780-a642-c2c099524996 | -11.54104 | -47.68586 | 2025-10-05 03:55:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 862664dc-e990-37ba-9215-88f4cbac7b89 | -16.29148 | -45.24085 | 2025-10-05 03:55:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43deea2f-7863-3aea-a676-1edcb6a9a782 | -10.82577 | -47.98899 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1b0ff2a-51ac-3dab-823e-351881f624a1 | -14.68144 | -48.34969 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 98174ed9-39a0-3a6f-9795-1b52eb07b3bf | -11.87056 | -44.96694 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 255ffa2f-f20b-37f6-9651-30f09492d0f2 | -11.48284 | -44.97601 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2d37b88-207d-3b0b-a06c-682388cbd5df | -15.97313 | -50.91429 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f6a19ca-da3b-3a5a-aa34-f437873d6cfb | -15.93538 | -48.99796 | 2025-10-05 03:55:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 161270c4-c662-3210-b275-59dfb18ab986 | -13.26951 | -47.60812 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b09ac4e7-206e-317c-8659-e267e4ab67c3 | -13.24941 | -47.23653 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53d33537-5e4b-3b64-9009-c7e41dc9c722 | -13.46163 | -47.26277 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3042dc30-1c41-3c7b-9afd-3c8809865a7d | -18.54869 | -41.57999 | 2025-10-05 03:55:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e7505c13-42b6-3de1-be8f-51ea528eff32 | -11.80805 | -46.85012 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9ca90ccb-6dd2-35b5-97c9-7a9e821b190d | -15.39153 | -47.95726 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee088fe5-a828-3774-be61-efab030478b6 | -10.75667 | -46.61306 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7f1dad3f-36b3-3003-a639-bda5bdaecd13 | -13.08904 | -47.8854 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa54e554-2e75-3e41-be71-c739f97637e9 | -12.90497 | -47.31279 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| decf8dbd-2cd0-33e1-960b-e7415b9374f4 | -10.84048 | -47.97889 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3aad227d-0b6d-30db-b437-89724ce48d63 | -10.80252 | -51.00619 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bfcc22c-0625-3206-957c-1e29433312ef | -11.91261 | -46.23932 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 073f95d8-031c-3b11-82c8-a705f1deae90 | -14.09469 | -46.34989 | 2025-10-05 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6c23d91-cb11-324b-ad44-d1be83b4d534 | -13.8561 | -43.99333 | 2025-10-05 03:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 59635380-46b8-371d-8bb4-194342b71f7c | -11.63391 | -46.87946 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f33f6e4-330c-34f5-8e1a-9a552cd30cf9 | -11.10265 | -47.87807 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52d3ca7a-07d7-32e9-a256-57feb915dc9a | -14.33789 | -45.85867 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d693f97-a18c-32d4-a635-71b7a1645d42 | -13.0269 | -42.45002 | 2025-10-05 03:55:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91a4b70c-5038-3604-ae14-f82762a5681b | -15.74347 | -46.26658 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d877f42-dba3-368f-babb-fb551ae89328 | -13.74084 | -47.96195 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd59c845-addf-3000-b3af-cefceb3dfbbe | -11.0419 | -47.79108 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28ba06a7-d137-38f1-afc7-8650b8e94966 | -11.63416 | -45.07415 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c824bdc-3678-3749-b358-969b2aa73603 | -17.55998 | -46.78168 | 2025-10-05 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3960502d-70e9-3516-ab0b-13dede1e6944 | -14.91763 | -46.84851 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40442e82-2aef-3d7b-9fb4-ea5d4376a16c | -15.38785 | -47.9511 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a009a41-aaa5-3eac-9fd8-3a4b95f6eda0 | -14.69621 | -48.3522 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d2a2138-d643-3798-a0ac-e43ef513723e | -10.82268 | -47.98866 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16057d28-3fad-3106-aafc-8ac052344513 | -14.68645 | -48.29842 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17a92444-2dbf-32f5-88c4-827d152188f4 | -14.24832 | -46.10919 | 2025-10-05 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7923fec-4400-3a2b-9bad-71c900c0175b | -14.92115 | -46.85424 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5a2e2da6-9ded-3a04-8fd1-c35e4c41676f | -14.97897 | -49.99996 | 2025-10-05 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3051b17b-6802-323d-b60f-0747f9df6545 | -12.92239 | -45.07251 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8845e973-b14e-310e-b89a-f9ee67bc4bcc | -13.32665 | -47.56624 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db00c437-aa1e-32e4-8274-a04e25e8ecfa | -14.66953 | -48.35843 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 895e56b3-da53-3688-b88c-2a1075f806e2 | -13.37334 | -47.5544 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a09e676-7d2d-3a23-bbed-3ce7fa0d8da8 | -15.22527 | -49.2972 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f9b2aac2-c7b6-3c81-8529-28104c95fb25 | -11.48635 | -44.98034 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fccfdff4-40fc-3c35-909c-8dcbde22d0c1 | -12.98233 | -51.01114 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab813945-427c-3320-a532-6748fe225f3c | -10.83951 | -47.97186 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 15ca41e7-ad3e-3de2-a5d5-85d22b925387 | -16.07385 | -50.9226 | 2025-10-05 03:55:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6235e735-79a0-3966-84b4-010bc1df9881 | -12.89265 | -47.32653 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 817be985-cb8d-339d-83ad-6dbfc4018d25 | -14.6708 | -48.36898 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 82ff465c-0342-3de7-91aa-83050f1d48b1 | -13.28799 | -47.58865 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b117dbd-bfd2-3826-aa6a-377247ba048f | -15.54171 | -46.80807 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e617066-b21b-3361-8efc-b6e38bea08c3 | -10.84169 | -47.97253 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| ea095678-a5c4-3570-9bb4-92542e42f1b9 | -11.45068 | -44.95526 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4ae3ad25-5f0a-30f3-a991-714218e1ab4a | -13.26395 | -47.19629 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b334cff3-19af-3bd1-bcc0-d4ba82b0672f | -13.43585 | -47.79875 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4aa11c60-6b59-34ad-8681-f75de8163ba1 | -14.33051 | -47.68703 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0e6b819f-4164-331e-84c3-30c1043952c4 | -15.53782 | -46.82867 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfca7786-7f5a-3ad5-a9ff-8c580992fd96 | -11.81761 | -45.04846 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d627b93-c7b1-3560-a73c-874e2a57ae2b | -13.12907 | -50.88282 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f1ddbde1-98ef-3eb7-8eb0-527a51c955d1 | -13.15769 | -50.89368 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b4b2991-827d-39f3-af40-4385d6feb6a9 | -13.30929 | -47.63129 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1df4bd9-aec5-3e83-b17a-15be86ec1c39 | -11.24979 | -47.78204 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e13e8e99-cd5d-3368-b240-f2f0d28cd07c | -11.71082 | -45.35212 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef661412-38ed-35da-b287-01818de9b070 | -17.07656 | -43.34858 | 2025-10-05 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 988bbb88-0444-35f9-ba5c-504acf2c3834 | -11.9146 | -46.24239 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6d4fecf6-b417-349b-a40e-a4451a60c798 | -10.99911 | -46.51244 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eab846ff-c45e-3a9d-866d-a467fcddc811 | -13.3167 | -47.17221 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83c5c862-5226-3ec8-9ae0-ebe8ecacecd3 | -11.7972 | -47.91949 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a444a2d8-113a-3a9b-95e6-63160bfadd33 | -10.57152 | -48.69185 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| caee5fbb-5d22-3cc5-8ac0-14e590f55ca3 | -10.82791 | -47.98911 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f3f3992-1a48-398e-90f3-41e9c0a6056b | -11.87465 | -44.96787 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1288da79-fff2-3bc8-8e9c-6519f7c021c9 | -11.63343 | -45.0783 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0a7dd9c-44c5-3e73-ab4d-a85cda3b049b | -17.55038 | -42.38637 | 2025-10-05 03:55:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c73e975-98c4-3ac3-a95c-e466b479fd0d | -12.09791 | -45.17731 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b1e7b8a-53e7-3dbd-8d61-9de169873620 | -13.52094 | -47.29338 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb59b1a3-e188-36c3-94bb-21c0f1d03096 | -14.64842 | -48.32634 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5e52219-0a75-3186-a47c-36bc0e592ab7 | -11.80076 | -46.85214 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README67.md)
