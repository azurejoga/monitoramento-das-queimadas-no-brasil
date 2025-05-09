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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9584739a-1f95-3d21-addd-a7618743b006 | -21.17975 | -43.98202 | 2025-05-09 03:49:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 13ca6da9-0fab-384f-9c11-ef3e52c395cd | -20.06042 | -49.37046 | 2025-05-09 03:49:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 158ce1be-8a03-35e4-9545-e1c388c763e4 | -9.54707 | -36.92101 | 2025-05-09 03:49:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 75898ebf-9c3e-3c3a-a20f-da5f6967af4d | -20.76272 | -46.77086 | 2025-05-09 03:49:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d524d3c-e77f-3db8-acfb-8c2b177934ea | -14.64358 | -45.13569 | 2025-05-09 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4785375-6d02-3478-9b14-ade18a5f0938 | -17.47293 | -45.47084 | 2025-05-09 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62731c06-2ae8-3c54-ad6a-f14914ed2f11 | -14.64276 | -45.14009 | 2025-05-09 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b11bf6b-cb86-3560-a4f5-4513ce87499c | -14.21002 | -45.46055 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4edfb0a-9664-3f1c-bf5c-7ba690a1dbba | -20.06043 | -49.37051 | 2025-05-09 03:49:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6bae3d6c-dabe-350b-ad1e-dad4802bc511 | -9.56305 | -35.69137 | 2025-05-09 03:49:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 37d68df4-cfb9-3980-89b3-c7ca406352e3 | -20.06258 | -49.36048 | 2025-05-09 03:49:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2d676320-be79-3473-9127-f3da9c45f741 | -14.20461 | -45.46434 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 343db668-07eb-3b7c-9cb6-a8050a80a6ba | -14.201 | -45.45878 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4636965-9399-357d-8f41-02c6c91f7615 | -18.25994 | -53.00599 | 2025-05-09 03:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9fe57f51-43f4-31c2-a800-1dc459a54e12 | -14.22177 | -45.47258 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46dcfa27-df3d-30ac-8fbe-cc66e4f47abe | -14.1992 | -45.46817 | 2025-05-09 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e87e91b5-0b32-31e5-8227-9610b3afb28f | -17.23066 | -47.38913 | 2025-05-09 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b86e0de0-523b-3ad0-bd01-656edf62e11c | -14.64714 | -45.14096 | 2025-05-09 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98726a08-fb70-358a-ba7a-30a2bdb8e6db | -8.07 | -43.1216 | 2025-05-09 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| cc0e7b26-23e2-3078-bae2-b0b50a509cdc | -8.0889 | -43.1196 | 2025-05-09 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| de5cb722-b632-31b2-857e-1b624dfe42ec | -24.09211 | -48.97136 | 2025-05-09 03:51:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d8d3268-8cce-388f-8978-f7ea9b488bd6 | -22.69924 | -43.34774 | 2025-05-09 03:51:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc2d25d9-934f-36ef-beb7-352684e5fac0 | -22.7841 | -43.75595 | 2025-05-09 03:51:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 162aa444-b10c-33e1-8cc5-4a3ea598eeac | -22.6679 | -49.82813 | 2025-05-09 03:51:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9992d3e9-1bd9-3046-9598-b3afc4d10da7 | -23.33622 | -46.77168 | 2025-05-09 03:51:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d63854a-25ac-3941-97df-ba3c984e520d | -23.33395 | -46.9579 | 2025-05-09 03:51:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 445dcc3e-88e0-3e4d-b091-effdf85d0411 | -20.99512 | -51.79303 | 2025-05-09 03:51:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2428ce5a-4554-3345-abf3-78842b8c31d8 | -22.85441 | -42.97976 | 2025-05-09 03:51:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8689a631-0bbd-3420-a499-d21b613ab51b | -24.9348 | -51.91726 | 2025-05-09 03:51:00 | NOAA-20 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f36ec168-9435-3e0e-adee-16dd12fb7100 | -22.67297 | -49.82931 | 2025-05-09 03:51:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7badcc0d-1959-373d-bea3-b1f316eac3fc | -23.98565 | -48.91776 | 2025-05-09 03:51:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e56c5e3d-b4cd-362d-988f-17bacb9957fa | -22.69561 | -43.43067 | 2025-05-09 03:51:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1e810cd1-adb5-3214-8a9d-a862d29345ef | -22.66858 | -49.82498 | 2025-05-09 03:51:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdb86f14-23ca-36c7-92a2-e1841e4ce24f | -23.33312 | -46.96207 | 2025-05-09 03:51:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8be37df8-44ab-3bf3-8a81-ec6032f4d1de | -21.78385 | -52.75362 | 2025-05-09 03:51:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb79223c-39a3-3d55-9410-e324ab725e81 | -23.32974 | -46.95703 | 2025-05-09 03:51:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9511bc7b-6adb-340d-8d39-1d677d50ed4b | -22.67608 | -42.85395 | 2025-05-09 03:51:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7b018bc4-5327-36d9-bb97-6488c5aaa228 | -24.92844 | -51.91967 | 2025-05-09 03:51:00 | NOAA-20 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d8bdede4-3da3-335e-bde6-04535ed86a2e | -23.40494 | -46.55543 | 2025-05-09 03:51:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 20cd8f06-bdcd-3b39-b97e-c1af936be387 | -21.78512 | -52.74823 | 2025-05-09 03:51:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0442d023-08d9-381b-9382-d8f59199e90e | -24.92938 | -51.91562 | 2025-05-09 03:51:00 | NOAA-20 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 619a2189-13eb-3053-93ff-d6206b858743 | -22.54116 | -48.81118 | 2025-05-09 03:51:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb8dcb55-64b9-35af-8713-752ca50a5079 | -22.90133 | -43.75171 | 2025-05-09 03:51:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fd21a6ed-664b-3ce2-9c38-f7fb1ed595bd | -21.88927 | -47.19131 | 2025-05-09 03:51:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d81c2cd9-aba1-3776-8423-d9ee54493842 | -8.07 | -43.1216 | 2025-05-09 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| ef221ff9-f00d-351a-b453-0442a9e22153 | -8.07 | -43.1216 | 2025-05-09 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 7d07a43f-7903-3f4a-8e6e-418d11a1ae9e | -8.0889 | -43.1196 | 2025-05-09 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 10b8c56c-d1dd-3e14-a88a-b33ce8d7f57c | -8.07 | -43.1216 | 2025-05-09 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 3472fe2e-8e8d-3911-9792-2c5fa77cdba6 | -8.07 | -43.1216 | 2025-05-09 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 03abd62f-4b80-3f0e-81ea-945a7c060350 | -3.46362 | -49.17846 | 2025-05-09 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42f59b8f-9760-37ca-a522-935993dbee20 | -6.96826 | -42.78083 | 2025-05-09 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5b3ae25f-1b5a-3f85-bb92-98115cd08a4b | -5.16746 | -45.10659 | 2025-05-09 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3c8a1b13-1104-3423-a17f-1dbc7d6ba9d6 | -5.16813 | -45.102 | 2025-05-09 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c2814c44-2248-3ab2-8b49-395a010e3be8 | -6.6237 | -44.77571 | 2025-05-09 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5d2d7a6-e534-3d1e-a2e7-2a1b8023c2a4 | -5.19001 | -44.95265 | 2025-05-09 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b410dfbe-0db3-39c9-8f37-94469f9f1cac | -6.69708 | -42.14184 | 2025-05-09 04:38:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 21e8fc81-3d8e-35fb-a2b7-1c806a088610 | -5.16387 | -45.10322 | 2025-05-09 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a4f5a5df-4f02-3262-8c1a-cada5d0e6fa3 | -6.19839 | -48.0428 | 2025-05-09 04:38:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8293b210-2584-3f57-901e-ed4498bd0d96 | -7.07389 | -44.38631 | 2025-05-09 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 733aa2a8-aee3-3993-957a-bf45492c3bfe | -4.00016 | -43.24643 | 2025-05-09 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88ee2657-bbd6-33f0-9414-b30a097fec8e | -8.17107 | -46.71189 | 2025-05-09 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2ddd50d-3828-31dd-bf70-1b8fbdf8c63c | -8.17167 | -46.7077 | 2025-05-09 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8381f92-828e-3701-8ef7-838ef6e9ccc0 | -8.17885 | -46.70881 | 2025-05-09 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36503cf7-24e0-3e05-b0a9-732160cf4782 | -5.82475 | -47.62114 | 2025-05-09 04:38:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edf67f43-9484-3b5d-8d47-a982cf89194a | -8.0742 | -43.12016 | 2025-05-09 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| e72a8669-ded1-365a-b2a8-e5d3b34cdf08 | -8.07358 | -43.12466 | 2025-05-09 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.0 |
| 59b891b3-d20e-38a9-bf95-023f8748146b | -8.08256 | -43.12596 | 2025-05-09 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 5d46e3b9-7a45-3826-87fb-e2c61cda6969 | -6.69777 | -42.13686 | 2025-05-09 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| fee2fa49-5a1f-370e-b233-256b318c1bd6 | -5.16367 | -45.10604 | 2025-05-09 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6a70b4f0-4d0d-317c-a8a2-998c79d7ed2b | -6.19504 | -48.04227 | 2025-05-09 04:38:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb5369ae-ecfb-3ae3-b8c3-712269a6b283 | -8.17304 | -46.70951 | 2025-05-09 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d2f949c-c559-3e21-bf4e-e07ae25064f2 | -8.07807 | -43.12531 | 2025-05-09 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 810c408d-185b-3fdb-960c-8a16c355c071 | -7.65131 | -47.60274 | 2025-05-09 04:38:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e61005b-76a2-3781-9bd1-cfd36156f6e0 | -6.97211 | -42.78614 | 2025-05-09 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c43ce1c8-5c21-3de0-bf32-52eb11b9f58c | -6.7018 | -42.14245 | 2025-05-09 04:38:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f4e1430e-5e9d-3879-b5a7-956a40760c62 | -3.99598 | -43.24578 | 2025-05-09 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0af275f-b0f8-333e-9af7-c5061809077f | -6.61772 | -48.01134 | 2025-05-09 04:38:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e23514a9-ad2d-3331-89d1-331f58d41e4f | -8.16882 | -46.71312 | 2025-05-09 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfd8d7cc-2cb5-3a4e-bfca-7f19317dcd96 | -4.00435 | -43.24707 | 2025-05-09 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44061f73-b497-39e0-b9a6-e396b34ffa8b | -3.58666 | -48.9545 | 2025-05-09 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2066060e-6782-3b11-930d-138635e6a091 | -8.17663 | -46.71006 | 2025-05-09 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1371576c-ef74-316c-a1d1-4d6942900664 | -3.46416 | -49.17501 | 2025-05-09 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25292b9c-d64c-334a-a907-ab8c2784ad39 | -6.70249 | -42.13751 | 2025-05-09 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 13326cc1-c51f-31f3-a61e-a9d4cf9e7a38 | -5.77401 | -43.48409 | 2025-05-09 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 686ff74d-136b-341f-a1e2-5d1969254878 | -7.21628 | -43.1208 | 2025-05-09 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bd5ef5e9-2048-3d64-9c61-6af4b338f9fd | -7.84663 | -48.00097 | 2025-05-09 04:38:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5076e4a1-4c9b-3f86-82ed-3c5cb8502294 | -6.96308 | -42.78476 | 2025-05-09 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7cb5c43a-452d-3480-905b-09ccbcabce9e | -6.71643 | -47.59356 | 2025-05-09 04:38:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f89a3204-6b33-3b77-81a3-1678e40682d2 | -5.56658 | -43.48291 | 2025-05-09 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79cefe73-59a7-3f7d-9b28-9fd9de541425 | -7.08418 | -44.37273 | 2025-05-09 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 640cc70b-64d2-33ed-81ad-624ea79bcdd7 | -4.17622 | -48.14436 | 2025-05-09 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d92e4c55-350c-3f21-95f4-33fd6e300dbf | -4.00638 | -56.11121 | 2025-05-09 04:38:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5516b5f8-f2d3-3c07-bc4c-2a4fa7080217 | -6.9676 | -42.78545 | 2025-05-09 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0f7d8e5f-8d10-382c-9eb3-c7d39ad44c4d | -7.07337 | -44.38993 | 2025-05-09 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c60ec14-e2f1-39fc-be45-4472bf5f0e2a | -6.06665 | -44.63594 | 2025-05-09 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb33eb16-43c5-35ab-b399-ef1fc25c4325 | -6.6241 | -44.77212 | 2025-05-09 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1225003d-779b-3763-a063-04a7b001da4e | -3.58336 | -48.95399 | 2025-05-09 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a9b7c80-860e-3425-99e8-f095b8957017 | -3.70911 | -53.71049 | 2025-05-09 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3d75f745-4fc9-3b01-a1c2-dd3c40514804 | -8.17526 | -46.70826 | 2025-05-09 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 582341b7-e08c-3d29-ab6d-a6583a380eb7 | -7.21689 | -43.11641 | 2025-05-09 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README6.md)
