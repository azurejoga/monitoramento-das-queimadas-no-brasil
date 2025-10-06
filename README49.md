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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ef35606-7921-3258-8154-c702e25afdb5 | -9.96438 | -43.77691 | 2025-10-06 04:27:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44b12800-ce71-328f-bc71-0d71a7e3cf55 | -14.90334 | -51.504 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| db4653d9-f3fe-3579-8082-dbd36a6c0ef2 | -11.44011 | -43.48126 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7a390bb-56af-3f03-9439-593e5ab4bb6e | -13.10454 | -48.00365 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e8cf368-f878-3d76-8b43-c96bb0485cea | -12.57511 | -48.14393 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf4562df-b1b0-37a9-983a-046822205dba | -13.6825 | -47.34901 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69cb076d-adaf-3f7e-bf3e-070276059374 | -10.32152 | -50.26939 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56f0ae77-33b2-34f6-99d4-d0a2a223fe4d | -9.02217 | -50.68674 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b05f5e9f-9e2a-3597-a43e-7b4fc142a014 | -13.08759 | -47.83143 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3880977-894d-3687-9531-77ecee01556f | -9.23163 | -51.82081 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c893c16-374c-3e7a-bcc2-f642e131eaa9 | -15.87816 | -46.25277 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f61ee0c2-2720-3117-86c3-182b222c152b | -12.45583 | -45.53973 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0519192a-765c-31b6-95d4-e519e355320d | -11.85174 | -45.05884 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c71cd749-fea8-36e1-8b67-054af9f0f414 | -17.07324 | -43.38042 | 2025-10-06 04:27:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b1824d8-39b8-3339-a319-456e2439cc8d | -16.10327 | -43.63247 | 2025-10-06 04:27:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a19e76f-4d44-3f28-908d-fdb1b08ade6e | -11.25511 | -47.7763 | 2025-10-06 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77ba93c8-f950-35c2-b174-fc9dcd2d155e | -15.72976 | -46.28521 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd87409a-520f-330c-b633-bae89b14577f | -13.33494 | -48.05249 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60d08f6f-0da8-3166-911b-be47afe4e16a | -14.88323 | -50.12027 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c18a416-bf3a-3390-8a2a-ecb348884c6a | -11.0349 | -47.79123 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e5f4bfa-4b62-3d15-9ae1-2083e1a0cc9d | -15.65349 | -49.10226 | 2025-10-06 04:27:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bffe1c7-72c4-30c8-87f1-6b5dd6e4e9fe | -11.04756 | -47.77537 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fea23004-a820-3058-b121-c017df643bd6 | -13.33778 | -47.18068 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8530f349-1ea9-349b-a714-32844a1eae78 | -13.36572 | -47.57391 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 456103b2-7626-3b62-b1f1-2c3798987282 | -12.24927 | -49.20022 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39a9d7ad-fe95-3175-bfae-8c07041a1a03 | -14.68257 | -48.39834 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71e40701-f782-3f45-aaf4-a857f1249598 | -14.32763 | -52.98478 | 2025-10-06 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8594cfae-bc0b-3e77-a70f-1f4e9cb874f5 | -12.32125 | -45.36222 | 2025-10-06 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 882fb1bb-b5c7-3869-85f5-58d0b8af1bd7 | -11.51179 | -54.45499 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e574690e-cbac-36c3-a02d-8b272dfb8da3 | -11.87941 | -56.86502 | 2025-10-06 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7092614-1449-3ac6-b571-d9afcb1da855 | -11.88006 | -56.86163 | 2025-10-06 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70d312de-7093-3cd9-a54f-72d3cd3ceefd | -12.70587 | -48.56466 | 2025-10-06 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dadfb9dc-75d7-35ec-8489-db992065dcad | -13.10784 | -48.0042 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0432441a-8762-3d88-a9f0-950f3460fd65 | -11.8407 | -44.9161 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42538f8c-00aa-3ae4-ad19-5192acb9fecd | -10.43983 | -50.4123 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fa68e64-9a67-3e19-9a6c-e87376693589 | -14.485 | -47.54804 | 2025-10-06 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac6e2ed7-9f10-3ede-b874-852bcb8dd42b | -11.84883 | -44.93393 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b128ae10-70bf-3b40-82d8-7c0675ed3723 | -9.33415 | -54.52256 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13a42e47-ac54-3326-9475-6bb66c2919bb | -13.08596 | -47.82036 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6aeb4041-c391-3740-b161-abe0effe3cd4 | -11.51228 | -54.45851 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1924ca05-b566-3159-aed4-f55281ecb363 | -11.79998 | -45.1199 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e12ae92-be7f-3a21-b417-c1867f921bb4 | -15.80584 | -43.67483 | 2025-10-06 04:27:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68147a49-4965-3bf1-a53e-eb26a772540d | -14.99943 | -49.96985 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03679177-e44c-3b9a-9987-2509fc7d5034 | -11.05142 | -47.7724 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcb6ef3f-053f-3f14-9e3e-4e3973f0a9bc | -11.52185 | -47.68024 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89f77720-19f8-3f19-ae5e-9a718baf52c3 | -14.49107 | -47.55268 | 2025-10-06 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 42bd9094-a13e-399c-883d-c71f972c1f88 | -11.84941 | -45.05048 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39052eb4-91f1-3d1e-9385-b152f36f4cf1 | -14.56182 | -46.66616 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ccf0870-9f46-3583-88ad-7cf5be256c3c | -11.81622 | -44.88728 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88c6c2b5-3ee8-381e-b3bd-b1b75c201571 | -13.26237 | -46.4726 | 2025-10-06 04:27:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4697ca37-97e0-3968-99a7-41c85389d4c3 | -15.21243 | -46.39734 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5282dad-9c70-3a2d-b6ea-645d26c1f966 | -15.24319 | -49.28374 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 302acb8d-50df-3247-a4e9-6e79fe374d0d | -12.91502 | -46.81038 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e06b6b5d-c17a-306f-b8d7-2485eb6b4a95 | -15.25548 | -47.15059 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95a92878-67b0-3f59-a7b9-6fa1fcf72214 | -10.79136 | -48.59021 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a5bbb6a-8506-3164-998f-ed7021a7e75f | -10.67745 | -48.47622 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9112ad42-61a8-3f04-bc9e-3791252d2673 | -8.95752 | -50.69595 | 2025-10-06 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fedc878d-662b-3015-ab2f-fce0142f6eab | -16.0003 | -50.85027 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f345b0d-1b74-3ad8-a710-2b34dc275a7a | -15.67842 | -46.27828 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad00ad2c-80cb-3ef2-8d28-5fa0a9ed6882 | -12.70531 | -48.56819 | 2025-10-06 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 632aab8e-19af-36eb-a92c-687e7ec2b5a1 | -9.39448 | -45.86858 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae416c98-10e5-30ef-b52a-7f83ca7d409e | -11.17705 | -47.73143 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c90556e-becc-3b84-b645-4a2c51fc372b | -9.53051 | -45.5771 | 2025-10-06 04:27:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9a0d30a-7a74-3484-bd66-4e34dcfdcdbb | -12.91665 | -46.79963 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f466e3e-c81a-32af-80ff-3c62d4b3e6f8 | -13.07933 | -47.949 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2083cbb8-d298-33af-bc0e-f77234c30c19 | -15.61987 | -52.53328 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9c110086-1772-3af2-bbf3-08194f55cfb5 | -9.96962 | -48.75053 | 2025-10-06 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b2026d9-345e-3c1e-9fdd-60f9ca1672c1 | -13.25574 | -47.62416 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bfed389f-b456-3299-9fb1-353b150ed413 | -14.71344 | -48.35256 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 374387b7-1098-32de-addf-7f376300dd79 | -8.74491 | -50.66417 | 2025-10-06 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 57c7c4cd-592e-328c-9de9-f9a13443e742 | -14.84345 | -54.78749 | 2025-10-06 04:27:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e5685a2-431f-39bd-b9e8-fc74c3d83f41 | -11.54924 | -47.04647 | 2025-10-06 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f239c876-c9b2-3349-abaa-3b5079d336ae | -11.15042 | -47.92122 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51ba06f0-bcef-3c1e-9634-ecfbdbcd69fb | -15.20934 | -56.80615 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a90b1137-9fde-3fd5-95cc-8b4e153724de | -14.70899 | -48.3809 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27d89b9c-4001-37b0-a749-b45975992520 | -16.01639 | -50.96649 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9db19cb-a079-3bc0-97cb-d5cb034bde6b | -13.2712 | -47.82876 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86c9d055-ccdc-3c37-9488-a49e10aaf075 | -11.71084 | -45.41373 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f81122a-ee01-36b2-bfef-f4f7c205f59e | -13.05934 | -47.92058 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b8450f4-e1a8-332e-8723-c679bdd00d9f | -14.7534 | -54.68105 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1cd1c6a0-899d-3444-a08b-067418c915b8 | -14.67765 | -48.38661 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e084f3c-147f-3ecc-b269-9747b4b0d185 | -13.51744 | -48.21241 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26c6f0ef-4781-377c-930a-6af4d5370dc2 | -16.35334 | -47.05103 | 2025-10-06 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b62b525c-8303-3382-b689-40c376352967 | -12.91611 | -46.8032 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db7e45c6-49b8-3221-b2ee-b2efb737f18f | -14.7057 | -50.02785 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09e4f8d4-59be-393c-b885-e97ae12ee2b4 | -13.63509 | -48.71548 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05113775-d696-3665-b201-30ad34be32da | -13.26405 | -47.80964 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0692a48c-5a50-3eaa-a629-e65e8509fe0e | -16.00667 | -50.96058 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5ffc781-0b9d-394a-95ff-0b01e1a561be | -12.45048 | -45.5083 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ce6a114-5756-3de6-80af-fe74ded1f3af | -15.99893 | -50.943 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adee14b7-0d66-3060-a69a-ed5d4d64cf73 | -14.94461 | -46.82826 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 341b6812-0c18-3454-96ef-7d17548f4b13 | -11.46938 | -43.49708 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f37db7d-9b4d-3296-8b58-7ebef5b88583 | -11.8815 | -44.95503 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5866865c-40e3-3c0b-95d3-cb7ce8cb59bd | -14.4043 | -45.93909 | 2025-10-06 04:27:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 259259d8-eee9-3eff-8743-35f73edfc8d2 | -13.08097 | -47.87361 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f24fdab9-9e65-39aa-aeb8-7b547158e7a3 | -11.87487 | -56.88868 | 2025-10-06 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 942c5ef1-a04c-33bc-8a07-09065ba8ead9 | -9.33035 | -54.51666 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edca8b69-a571-3176-b525-9e37ff756430 | -12.07142 | -47.99282 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35dc8511-912a-3d57-83ee-7fcb80904bda | -11.57623 | -46.76253 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ceae28e-f820-3f42-8d20-ee45b50f718e | -13.83665 | -47.91416 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README50.md)
