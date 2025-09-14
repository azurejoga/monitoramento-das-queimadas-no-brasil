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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02b16664-55e6-3b0f-abfb-66e1f1b5e70a | -13.30838 | -44.67127 | 2025-09-14 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bab87125-53a9-307b-8b73-59b3089dc0bb | -6.43716 | -44.08245 | 2025-09-14 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6135f8ee-6789-3e44-93ac-fcf00db56891 | -16.83993 | -40.85042 | 2025-09-14 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dbc860f1-dd2f-3eb9-9037-57133af4a01e | -12.57812 | -45.6668 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c5afbc2-a76e-39e3-97b2-69f32cd263d2 | -16.28377 | -45.67997 | 2025-09-14 03:49:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6381e00-75d5-30d3-9f29-8f116ea45fdd | -17.69368 | -42.55924 | 2025-09-14 03:49:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 6eb8f8eb-a9d6-38d9-98ca-f636a54adbc0 | -6.10217 | -45.94476 | 2025-09-14 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2a7f281-92af-3b99-aba7-bca491447274 | -6.18051 | -41.17015 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4d054409-8feb-33d1-9b35-d851afc7abd3 | -10.90779 | -47.20443 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54af4479-03f6-355b-ba0d-269eb2bf1ed6 | -13.93431 | -44.83976 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 650bfed3-540f-3b64-9a18-086f38a6be4e | -5.95495 | -44.11692 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc3dd245-ef26-3b68-ad63-c2f49e1d5fdc | -11.46964 | -50.76202 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81727521-1596-3d05-89cf-32209bdc68b9 | -10.88116 | -48.18952 | 2025-09-14 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15d3cb2d-5c4c-32a8-b6ce-0f2193ef234a | -12.07796 | -47.56979 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bd14978-cedd-3d1a-8066-b86d5f2cc633 | -12.81212 | -47.15295 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f320edc0-c4a9-3b39-a330-abbc964f0a19 | -11.38038 | -43.50386 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dba06e89-7b34-3c3d-bf90-929ad04d5f0c | -12.56598 | -45.65392 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f84329e-58bc-3954-a53d-2b4a8cf2ae62 | -12.81346 | -47.95264 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d6f3502-6943-3a67-a0aa-a97427e1ab01 | -12.24244 | -46.78384 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 091d62ba-a038-3e80-bf50-f4b8558d3434 | -11.23611 | -47.63024 | 2025-09-14 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| adbd4516-98d8-3ede-9722-496ae36607b8 | -6.27361 | -42.39816 | 2025-09-14 03:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 69754a5b-07e1-3dd8-98fa-43a765166372 | -14.62567 | -52.04361 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d715f82b-9008-32e0-9cd6-836bda26fea4 | -11.44114 | -45.13646 | 2025-09-14 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c828d56-7cfd-3595-8347-b219e8ce7fbe | -18.00955 | -46.95856 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dc24542e-e525-3ea9-b8a2-9d85e9830770 | -13.28802 | -43.78136 | 2025-09-14 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41436f6d-86f6-388b-8809-339752a05ea3 | -16.27851 | -45.68358 | 2025-09-14 03:49:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbd66908-ed99-3cfb-a6c7-63bc4f35f85c | -12.96713 | -48.04177 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1778b0b-bcf8-3b34-b460-1b57e4609d54 | -12.0872 | -44.73141 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a199cd1-7784-3fd2-ae76-798fc6e4a2c3 | -11.2476 | -44.77251 | 2025-09-14 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 3b822e61-638b-3a28-829b-72588d825837 | -12.78241 | -48.02364 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bfa1551e-673b-3f7e-a460-ce0971520564 | -15.52342 | -48.5243 | 2025-09-14 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea6e9d02-25fe-31be-8bae-b2d20ada9e44 | -12.09012 | -44.86555 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6a708a2-4483-3a87-8593-fe58b5248839 | -5.73121 | -43.20295 | 2025-09-14 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 33dac688-1db3-36c4-9451-38942a404633 | -6.33632 | -43.87062 | 2025-09-14 03:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ebdd0381-e20c-37f0-b223-c6fb6d8f1a71 | -13.93108 | -44.85709 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1b79b13c-3a65-3838-91a3-e1f05ad428bc | -13.93783 | -44.84498 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4083913d-598d-30ab-83fa-512af9afbc31 | -18.01202 | -46.97038 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2b6ba630-ddca-311d-afc1-e1a92c7e14e0 | -14.62334 | -52.04365 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e156c52-f131-379c-b0c6-8b17759affe2 | -11.24163 | -47.63108 | 2025-09-14 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08b5629d-ee8d-3ca4-806a-65d80ed8997c | -13.89602 | -48.30245 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8da82789-4dcb-3902-bbcb-01ebc9b0f28a | -6.17626 | -41.16739 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ecdff258-75db-3678-8360-fdb7f5918289 | -14.6301 | -52.11021 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6143dbc3-ecfa-33f0-8e38-8c0dfaf3b337 | -11.45952 | -43.57303 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55cc96da-3cce-309a-a168-335490dc9ef2 | -13.88571 | -48.29339 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fde19a9d-c6ed-3620-9247-5c05504a91a3 | -12.24694 | -46.78795 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c4e307b2-c10c-3ddd-b784-4d5806f69e0f | -11.35951 | -47.3379 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b869d13-e2bd-3f8c-bb4f-fda91f4c4475 | -14.36 | -52.94281 | 2025-09-14 03:49:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8b2e5b4-45e2-3af8-92a1-e948dd4c6cca | -12.80818 | -47.14555 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 07e71d62-8d17-38f9-9830-b27fcd83def9 | -12.77222 | -48.01782 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 57079119-6589-3adb-a9e1-fed4b41833f7 | -11.29877 | -50.7822 | 2025-09-14 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 11fb228d-598c-3495-8bc0-ae8f3e1ce835 | -12.03805 | -46.55035 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13d911bc-0f11-3e27-a0f7-ccb4d14a7cfd | -11.78123 | -46.62415 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6a99a116-b9f8-363d-a533-9d6115f86eec | -12.78153 | -47.99955 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9ec53d8a-0937-329d-afc2-4e19901a8278 | -15.77663 | -52.22315 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fe87206-a06f-3892-82e2-2b77f080f28c | -13.90536 | -48.30869 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32b0ebea-fdec-34a8-a183-d0dfd2a33860 | -17.31667 | -46.09281 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 569e4eca-03ce-3166-99cc-a11a6e19585f | -6.2636 | -44.09703 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9646e288-1b7d-3c5e-a342-9af5e7c5e045 | -17.35661 | -42.62476 | 2025-09-14 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a4dba0f-8b00-3162-a60c-10558596f65d | -18.01615 | -46.94956 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8f8ac59-ebb0-3928-a6b7-97c453fab65b | -14.17432 | -46.15293 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4852f721-651c-3269-bb97-2a8a5f8906e8 | -13.88089 | -48.28913 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b2e6658-79f4-34af-8cb1-3e0913dfe2a5 | -11.77554 | -46.6264 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4ee1493-f8f9-344d-82f4-02cb68b38c1e | -12.97123 | -48.04681 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93692dc6-6fbd-390f-8290-7da2267ebc4e | -14.19672 | -46.16884 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9a7da3bd-0e3f-3099-be5c-c9bfc215944e | -7.10937 | -36.48779 | 2025-09-14 03:49:00 | NOAA-20 | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9b35060c-1f0e-3512-8416-cbc8d3b3abac | -14.19941 | -46.18016 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 50f9fa1e-3c18-3997-9ae0-47a0ab2adb3c | -14.2828 | -46.12732 | 2025-09-14 03:49:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a0cddcd-8dcc-3035-8564-d2917749b1c5 | -10.89351 | -48.17894 | 2025-09-14 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 012a0900-9424-3e4a-b3ce-48b4e22735a9 | -12.5791 | -45.66164 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d081a75-c7be-32ed-bd1d-9743152aef83 | -14.19862 | -46.17976 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1e873520-082c-3625-960c-430b26e6e4ba | -10.76981 | -44.7784 | 2025-09-14 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 852a74d2-bf67-32ef-9490-5bf20f0841b7 | -11.37562 | -47.34084 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 014b3190-cf22-33cb-9d31-389386a1c419 | -14.1939 | -46.17879 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f7c860da-412a-3ea9-ae73-f345458b559b | -15.04453 | -50.15658 | 2025-09-14 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ea55990-882a-3949-97d9-f7c380a541c4 | -7.06634 | -38.54691 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 9f002bc2-d99e-3afc-8941-d9c364abe3bd | -17.29875 | -46.11401 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ecf3b8b-99fe-382d-b8ed-7e280e1d7828 | -13.43786 | -49.12674 | 2025-09-14 03:49:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b5ab935-5728-3209-836a-d92709592d63 | -13.93946 | -44.83626 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d35c49c1-2df6-3821-8d61-1aaac4ecf455 | -15.79948 | -52.21426 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6201e469-70d1-33b6-876c-a81be54fda72 | -5.7915 | -43.89281 | 2025-09-14 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e8363c9-e997-3239-869d-1dcd841472d7 | -12.78022 | -48.03465 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 95aa4191-7f32-3e14-8dfd-516e8b13474d | -18.29289 | -45.10575 | 2025-09-14 03:49:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34108686-f83f-339d-aeff-1226ee102e30 | -10.93457 | -47.35798 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7755b1e5-c4d1-3966-8c14-267c70178597 | -17.31858 | -46.08291 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f18a4f18-3529-3826-a58f-0640a0ac12d7 | -12.10002 | -44.86226 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70d64d45-0cdc-3323-83d7-0f67d263803a | -14.48481 | -47.33715 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e6ec45d-71cd-34f8-8f38-8f43139db5e6 | -5.72924 | -43.19962 | 2025-09-14 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fd58950d-a586-388f-b3ef-abe379987983 | -12.7675 | -48.0013 | 2025-09-14 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 1493203f-41bb-3dc1-a4f1-9a0ba2a050fe | -11.4643 | -50.7528 | 2025-09-14 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 58ed675f-f518-3a00-9719-7ee48acf0d10 | -14.2107 | -46.1749 | 2025-09-14 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 990dd395-22b8-3174-bf9e-a5d0eec73054 | -11.2885 | -51.1122 | 2025-09-14 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 9be19675-0947-3e92-bc21-032c3f4b0917 | -12.8019 | -47.1474 | 2025-09-14 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b096effc-e440-309f-a938-6cc6f34ae625 | -12.7867 | -47.9986 | 2025-09-14 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 1006e412-6c1c-3b4a-8326-a0c91e1cabe2 | -12.7863 | -48.0209 | 2025-09-14 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 6e61e2ff-cd8a-3be0-959b-588a8d535a1b | -12.7671 | -48.0236 | 2025-09-14 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 43de2f0f-d69e-30ec-a75b-93bcd63f901d | -23.74997 | -51.76734 | 2025-09-14 03:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 4cfccd20-f866-3cc4-85ea-4504889c7843 | -19.1791 | -42.65841 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 737a1f64-7590-32b7-af55-ee4878d411fc | -20.12658 | -46.87244 | 2025-09-14 03:51:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51dab99f-e34e-34db-92f2-ee5c1bed29ff | -18.97949 | -48.59275 | 2025-09-14 03:51:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b5e93bba-8212-334f-a041-b37b0cd23c7e | -22.65743 | -53.12007 | 2025-09-14 03:51:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
