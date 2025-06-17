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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fd0f9ca-94c9-365e-9af3-90977b65110f | -21.42545 | -48.64599 | 2025-06-17 04:38:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99a17b79-059b-37ee-b16e-99298b1ee8ea | -18.06155 | -48.89768 | 2025-06-17 04:38:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ef1fb9c0-1277-318a-a1d4-62695b3ad97d | -20.09627 | -51.23401 | 2025-06-17 04:38:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 12607f3e-34d9-339a-ae71-307482c1a459 | -19.71906 | -45.89096 | 2025-06-17 04:38:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 833421a1-64ce-34b5-a191-de71a950b55a | -16.7614 | -49.2496 | 2025-06-17 04:38:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b3ce3cc-458a-3980-a9d7-a155e6db0bc2 | -20.92172 | -49.09766 | 2025-06-17 04:38:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fa5e1b15-09cc-32db-8e10-e9f74d369b1b | -15.62643 | -57.30968 | 2025-06-17 04:38:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e7a9540-579a-39e9-ae66-d7e2d1cae5a9 | -18.13487 | -43.96152 | 2025-06-17 04:38:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29360e20-a43c-39a1-b9e1-62d6d39796bd | -15.62276 | -57.3038 | 2025-06-17 04:38:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86ccee8e-0e0a-31bf-b379-d01473bcc424 | -20.5774 | -44.57622 | 2025-06-17 04:38:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9bffa1be-e265-3f32-baa4-875da734169f | -18.64436 | -53.31761 | 2025-06-17 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da38a84b-4dd3-3052-8793-b23356546465 | -22.69868 | -43.34915 | 2025-06-17 04:38:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c365275a-2bda-3232-85b6-a7a40950acea | -20.55272 | -54.12561 | 2025-06-17 04:38:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 091e2380-bc32-3283-a195-f041858c760d | -19.54377 | -49.67743 | 2025-06-17 04:38:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 18a13e35-835e-3295-bdff-eac3a7244761 | -19.02245 | -57.62168 | 2025-06-17 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 62b7714a-e29d-3426-8bad-36e38fe9ab02 | -19.9319 | -44.13519 | 2025-06-17 04:38:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40a2c74c-2b56-3d59-8eab-1e4470de332e | -20.15325 | -45.20383 | 2025-06-17 04:38:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1d5dfcf2-572c-3723-a14a-0ad31b6c7a7e | -15.56935 | -55.65314 | 2025-06-17 04:38:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d1feb80-2f04-33a1-8027-31f03f914013 | -18.10173 | -42.35711 | 2025-06-17 04:38:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c1030df6-c51b-361f-a3d3-02c4a3d147ed | -15.57349 | -55.65398 | 2025-06-17 04:38:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42eea6fa-5dc7-3abe-ba7d-aae33c71bdb0 | -18.32259 | -49.88704 | 2025-06-17 04:38:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7386b1b3-2239-39ea-ac0d-2bfeb63f2a17 | -20.55346 | -54.12135 | 2025-06-17 04:38:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6be9bebf-fc49-3f07-a61d-a793f02babcc | -20.92519 | -49.0982 | 2025-06-17 04:38:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b6b6fb6b-7324-3963-9573-f41aa8d09eec | -19.00393 | -52.0852 | 2025-06-17 04:38:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16ebf30e-6528-3124-aae0-36d64e00c915 | -20.92578 | -49.09418 | 2025-06-17 04:38:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bb64c7a7-55aa-358e-92d2-6587d5e1a3e7 | -21.42605 | -48.6418 | 2025-06-17 04:38:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 104ef8b0-63a7-37c3-b316-9e20ee08bbc9 | -20.23644 | -46.73746 | 2025-06-17 04:38:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5e2d9b7-d2bb-3743-b1b7-12663989e2ff | -20.15272 | -45.20799 | 2025-06-17 04:38:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3ec48732-3ed8-3c0f-a5b3-d74cbdac3956 | -17.9142 | -45.5403 | 2025-06-17 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 777da85a-c201-3016-ba0c-d9ccdad82a31 | -23.34036 | -46.77198 | 2025-06-17 04:38:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 08b5fe35-0bf3-31de-abe6-1ae05e5ba261 | -21.97825 | -42.80302 | 2025-06-17 04:38:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 973830b9-6019-3b9d-8312-0673475f9d7d | -16.29882 | -52.93323 | 2025-06-17 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fd4324b-a527-3697-b6ad-430cff18b496 | -16.29813 | -52.93728 | 2025-06-17 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b225d4c8-e622-38ca-949f-4ffb78a1217f | -21.61845 | -57.56853 | 2025-06-17 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc8464b9-82b7-3e29-84ba-8bf3e3b04817 | -15.5742 | -55.65013 | 2025-06-17 04:38:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a779ff9e-11b4-33b1-8069-3f9c230ea35b | -21.12979 | -47.79091 | 2025-06-17 04:38:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35df1d20-f24f-3dbd-82b7-c393236963f9 | -16.29104 | -52.93605 | 2025-06-17 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9afb306-e0ae-3ff7-aeda-badfe4c6f4e7 | -17.59807 | -48.42626 | 2025-06-17 04:38:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35643064-6845-36ae-94e5-5148d90a133f | -22.77078 | -49.3116 | 2025-06-17 04:38:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| abf0cdcf-8e76-3c2c-8d48-11a518019a6e | -22.53923 | -48.81146 | 2025-06-17 04:38:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b2242d7-09aa-37ca-aeb2-eeac18bf261e | -21.33226 | -48.59326 | 2025-06-17 04:38:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4849674f-ac08-394a-a01e-d07db1eb53a5 | -19.00455 | -52.08143 | 2025-06-17 04:38:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 208377b2-32b8-31f8-9998-035111c16a05 | -19.70031 | -47.02034 | 2025-06-17 04:38:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad62d11d-526f-3548-86c6-70264de3f5ee | -18.32372 | -49.87969 | 2025-06-17 04:38:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18929487-ebc2-3c8c-9181-0502048e73bd | -20.0107 | -44.18007 | 2025-06-17 04:38:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| ad574870-b56b-32de-accd-a10f4c69e918 | -22.76669 | -49.31521 | 2025-06-17 04:38:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5a4b653-2fca-3934-b304-873c8510dd4c | -15.6274 | -57.30452 | 2025-06-17 04:38:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb86f384-51f1-3eab-870c-8acb7698d797 | -18.88594 | -50.99849 | 2025-06-17 04:38:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c7cadfb-9fe8-3e9f-8208-c1d3ced616ba | -16.30167 | -52.93787 | 2025-06-17 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ccfcd48-e9a2-3535-a126-18f92ad5d0f7 | -20.92231 | -49.09364 | 2025-06-17 04:38:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5392b425-496d-3327-ba6b-ce5ee1b0b7f9 | -17.4908 | -47.37872 | 2025-06-17 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfda8360-4aa6-375c-87d0-0b4e41532df4 | -19.00118 | -52.08082 | 2025-06-17 04:38:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b528c613-efb5-38e6-a17c-402bedcd3f81 | -20.557 | -54.12208 | 2025-06-17 04:38:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b27102e-afcc-3467-a8b1-8745c03b5f87 | -22.77019 | -49.31578 | 2025-06-17 04:38:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5dca64e3-6bc4-3175-8167-700e9889898c | -21.13229 | -47.78874 | 2025-06-17 04:38:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1a36022-0734-31f1-89cc-219be11deb99 | -21.13169 | -47.79329 | 2025-06-17 04:38:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fd122c0-4b94-3912-ae12-f8e2a4833fdd | -21.61764 | -57.57265 | 2025-06-17 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb04fb63-06c7-3c56-a40b-c3fc98b79b26 | -21.13047 | -47.80236 | 2025-06-17 04:38:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ecde7b0-b703-37be-b318-d6dec89b8c74 | -16.29458 | -52.93668 | 2025-06-17 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 376cc6e1-f2ed-3106-9600-c931071eb223 | -22.90043 | -43.75433 | 2025-06-17 04:38:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 84db9e64-c56e-3dea-b937-c66a4a417303 | -18.31924 | -49.88648 | 2025-06-17 04:38:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3b94f7c-75fa-33e9-9173-c59f38af5f52 | -8.07 | -43.1216 | 2025-06-17 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| a8c63fe4-0093-3c21-8443-ae1a8ebbf995 | -7.44715 | -44.89141 | 2025-06-17 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83dc49b9-faf2-3c9a-9a06-6cabf573ad75 | -8.33567 | -48.44976 | 2025-06-17 04:55:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 930d7d69-3e7e-3692-80b4-e67d99549356 | -4.2465 | -47.58458 | 2025-06-17 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73ddcf90-a7dd-339a-adf9-04f972a648e8 | -7.44576 | -44.89418 | 2025-06-17 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a095b7d2-3d87-3b4f-a184-74ac8c48cb52 | -6.67768 | -43.21693 | 2025-06-17 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6a08395e-bd7b-3a6d-8910-36abeb759509 | -8.07218 | -43.11572 | 2025-06-17 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 517926f3-1e7c-3833-8558-ee42df1b157e | -7.2341 | -43.07841 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e4e25723-4163-3684-8c38-b36becacfe65 | -2.45195 | -47.50126 | 2025-06-17 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00158acc-2d40-3b1b-8bc2-ccefcfcd4523 | -6.29527 | -44.23083 | 2025-06-17 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6172dfbd-f04c-34b0-b39c-e636c471bc95 | -8.61503 | -45.02028 | 2025-06-17 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09ec1eb9-0114-360c-8358-f13cd0f7005e | -8.61396 | -45.02715 | 2025-06-17 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74c2cd9c-5ea5-3999-891b-1dc482a65b1e | -7.72385 | -55.14021 | 2025-06-17 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79079c0f-4a55-3313-b199-850e770d4253 | -7.25058 | -43.09512 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 76bde57f-147c-305b-95ac-74f7eb22b76d | -2.588 | -51.92339 | 2025-06-17 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc371aa5-8f76-3300-bac0-6260e0d8b647 | -7.26157 | -44.64319 | 2025-06-17 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 009fb26e-83b0-3d52-be5e-3332be038e5d | -7.26652 | -44.64437 | 2025-06-17 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 261f057b-d0b1-34d5-8e58-eb1e02603124 | -8.88303 | -48.52225 | 2025-06-17 04:55:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59323e49-6dbf-3bec-86be-d83e2d3f839e | -7.17824 | -43.60664 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb7687d3-e7e5-3f1b-b199-6680a25cfce2 | -8.34156 | -48.44795 | 2025-06-17 04:55:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06136ec0-d175-389e-9075-9aed308060d2 | -6.29788 | -47.00523 | 2025-06-17 04:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c814609-195b-34dd-b724-16cb09e4b727 | -7.24445 | -43.09422 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1cd76d0b-fc7b-381e-9847-4d71bae98c83 | -8.60289 | -48.05914 | 2025-06-17 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 620679fa-c760-32d0-b081-d1637dbd1090 | -4.37568 | -48.07137 | 2025-06-17 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ab69735-2336-35aa-b538-c0f87e8f7778 | -3.77639 | -41.60458 | 2025-06-17 04:55:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 21220df2-d77d-3fe7-a8e4-016af74ae1d8 | -8.60989 | -45.01525 | 2025-06-17 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf2416c9-edbd-3853-b3cd-215a04ad888a | -2.44771 | -47.50062 | 2025-06-17 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54491c7b-690f-3350-a4ac-71df6dc98461 | -9.10522 | -46.05254 | 2025-06-17 04:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50604b63-9965-301a-a0c9-d6110da84645 | -7.18529 | -43.59892 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a15d9084-fef0-3eb6-9ce2-b8f8d8489b5f | -7.45675 | -45.5012 | 2025-06-17 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5d1a2e8-4d54-3764-aa23-12ce017caf43 | -6.15651 | -48.05597 | 2025-06-17 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90ddcdef-d6f7-3c9d-ab03-d8018af2991d | -7.97438 | -45.94553 | 2025-06-17 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3924a5e-2504-3b35-832d-fe9ea31457f4 | -2.4487 | -47.49768 | 2025-06-17 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2512bcf-b18d-3aa4-98c6-0a8cef543634 | -7.44528 | -44.89762 | 2025-06-17 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d16af008-d98e-3a91-a2aa-5df5cf2b5aba | -7.45721 | -45.4979 | 2025-06-17 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dd86957-6795-3f2d-aceb-79843239cc15 | -7.24865 | -44.61403 | 2025-06-17 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ec62545-22ef-3ebf-9525-0400df4b4b16 | -6.15163 | -48.05919 | 2025-06-17 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35f1d1f4-e91e-3860-bf82-fd4323da0dca | -7.97008 | -45.93858 | 2025-06-17 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d37bbc3-16af-366e-b207-3365c3cf23aa | -8.72919 | -47.99218 | 2025-06-17 04:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
