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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8da44647-31e5-35ab-bc03-539e39003abd | -9.53685 | -46.93674 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e302f8d-75ca-3e14-9bfa-e2f0948b1c26 | -13.944 | -43.80526 | 2025-10-28 04:44:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f81c5565-f47c-333a-9bcc-529f149cfd6f | -13.55137 | -49.58508 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ddad3dd-8eb0-3446-aa57-6d40b4220cee | -12.61858 | -45.0857 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e6a7bc0-d667-3e18-bfbd-4b1138b048a7 | -10.93165 | -50.25574 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8f94c97-0a4b-3996-9e8d-0060aaba63ef | -9.5533 | -46.92628 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18872ac2-6310-3b17-8a2f-777a63ae50bc | -9.79463 | -48.3864 | 2025-10-28 04:44:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f734248-94e2-354e-9c24-77433f5a545a | -8.34294 | -46.88876 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b958b703-6313-383f-a676-65666f7f9880 | -10.2261 | -47.55824 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81eb0a1f-c840-393b-9b1b-8b545236947e | -15.15446 | -46.59924 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 046a8830-d4be-34d8-97e0-249bf42615bc | -10.83431 | -44.95498 | 2025-10-28 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a1316cd-c96c-3ccf-8122-209834590214 | -8.32026 | -46.83596 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dea77449-8a01-3d04-90d4-1f2430f07f0c | -13.18341 | -48.44849 | 2025-10-28 04:44:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89d84f69-9bf5-32b5-ad6c-c56f1714fa6a | -12.05133 | -46.39366 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06f4eada-2c5e-3780-a91a-9bc2907daafd | -12.69551 | -46.32045 | 2025-10-28 04:44:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 661a6f33-35c8-3539-b0f4-6f515def80b0 | -13.26141 | -47.96003 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 092cde5a-888f-3ffa-a374-7eec313f479e | -13.55192 | -49.58142 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 917715fb-75e8-3143-a558-065c17ec78e6 | -10.56623 | -49.76011 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74e1f693-9f8e-38db-8605-38b37b60e00c | -13.66237 | -47.62739 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 343b80aa-8cef-3447-9519-755be0496b1d | -10.94497 | -50.27952 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa110659-1829-3f31-91a2-e68f5384af52 | -13.4289 | -47.38083 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80009f82-27d6-3b74-a9b1-7702ee8000e2 | -13.55641 | -49.57476 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 913c593c-94c1-3566-91be-f7ce1e08ad4e | -14.5622 | -47.98302 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9de8be7-51ee-3a8d-bb7e-0c5c5e18445a | -10.31604 | -48.78406 | 2025-10-28 04:44:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a66e4fa2-73ce-3ec1-ac91-63cd226a5af0 | -9.45828 | -46.86614 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 211a3aee-3441-3324-a70d-5cd69e7cbc19 | -11.77249 | -44.63543 | 2025-10-28 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1639408f-2aa7-3b00-bb35-ff85c5a6f308 | -13.87565 | -48.48631 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0021f52b-e40e-3de0-b4c7-13c9a424c0ce | -11.27686 | -45.50658 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d303a25c-10c8-31e0-b51d-d7b804607e73 | -10.61992 | -49.01104 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f2467e6-0d42-3b28-92a8-82988b790530 | -12.07945 | -45.64552 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbb71b5e-c169-3c66-9a8a-1453837f608f | -9.82879 | -47.7349 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7acc4925-10da-39d4-9a41-2f2925703370 | -11.31499 | -51.43552 | 2025-10-28 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82d47a4e-66bc-38bd-b104-a585519521fc | -12.08708 | -45.65034 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| daf29456-fc6d-3d5f-8308-d028480a8a60 | -15.7304 | -46.29515 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fd4a4ce-65d4-3068-b2c4-38ca740935a9 | -10.33117 | -47.2262 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1e3787d-7bc1-38b6-a164-36d8eacac7cb | -11.05808 | -49.67713 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70cadf0e-acf3-3c7c-90ae-ad8feedd9ad9 | -11.30658 | -45.35402 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac95fc0b-dd2d-396d-8bd7-bbdf613a4255 | -13.24346 | -47.05858 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ff854e6-cd05-3747-bf1f-44ddcbf5771e | -15.22836 | -47.9451 | 2025-10-28 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70240ed1-285a-3764-8c4c-bff1aa8c5b87 | -15.57939 | -43.20619 | 2025-10-28 04:44:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| de6dde2c-cbc1-3d3b-bc88-afbe964d3d92 | -9.1849 | -44.61597 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7852bf11-457f-3d6d-a059-5d48b63ec41b | -14.82283 | -47.41758 | 2025-10-28 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71f1ebf5-e595-3962-be8b-3533cae3f04a | -9.05974 | -46.94334 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63a19cf5-ec40-3518-bea0-212cef702f5f | -10.48991 | -51.86598 | 2025-10-28 04:44:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f20d46f7-a203-3d0a-aa41-4505e18bf8c2 | -8.53623 | -47.35607 | 2025-10-28 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c501b1e-78b0-3777-ac27-4e98820acd49 | -14.24903 | -48.12123 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0467845-7536-3d25-8dba-3244c15be224 | -9.05911 | -46.94754 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af3c0c98-3a13-324d-98e0-43cb891af0b1 | -8.11602 | -48.82054 | 2025-10-28 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4e5f3c5-e58c-3935-980d-d4784b3cf221 | -12.82338 | -47.72648 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ade3e8a7-611d-30cb-ae97-61e71f38bb82 | -14.61608 | -48.41294 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77cc2d38-ae43-37ea-902d-cdc853dc14b9 | -15.19773 | -43.78286 | 2025-10-28 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9145cc4e-a882-3bc5-b87a-d86971a80599 | -8.30468 | -46.81682 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c96805f-f7ea-3f10-a153-75a828e6c964 | -12.84606 | -47.23214 | 2025-10-28 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a3ec526-4db9-37ec-b989-f8e4c166aa7c | -10.35117 | -47.70883 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab006e44-d274-31c4-8115-ae7711d742b9 | -13.32122 | -48.34341 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c76312c-49de-33f9-a139-d3800ea7a007 | -9.5367 | -46.96309 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd534087-cba3-3cfa-b2f0-6a7883e8701e | -9.13377 | -51.30395 | 2025-10-28 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d5ed7565-546c-3464-8366-48c2f3f005fe | -9.5695 | -47.9017 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee7f803c-766a-3660-9d0c-e577cd2293a9 | -15.19554 | -47.21462 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8087b099-2af8-3608-a9ea-5cb450a22ae2 | -14.55115 | -47.98194 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a76043fa-bf7d-34dc-89d5-c9db1d414340 | -13.74074 | -48.42437 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8720093-c1b9-30c2-b65d-8fe48ec6f258 | -13.55476 | -49.58567 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0f91f35-4221-3713-8bb2-9656ec65a3ec | -13.62035 | -47.02581 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6aedca8d-6810-369c-953f-da6f26823707 | -12.08867 | -45.66897 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c30e025-ed6d-3db2-8cca-b67b92a1238b | -9.30727 | -45.84893 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55034de0-4f68-3386-b1ea-05714b24b3ee | -10.46596 | -50.86476 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d4edc45-b3ca-3c69-ba1f-1d1a09327190 | -10.99603 | -50.35949 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f838116c-2b8c-3121-b46c-4214a5bae65d | -11.15675 | -47.78039 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2f8c7c6-94d6-39f3-aa05-0835e90779d9 | -10.07042 | -48.20401 | 2025-10-28 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 315a44b8-a470-304b-9a74-6525ed1be0bc | -13.79564 | -48.66329 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9f36dcd3-ec4c-3cf0-896d-0e913157b0bd | -9.5912 | -47.85334 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7257c34-e7c4-35c4-b0b6-782d6a7d4f3c | -13.66592 | -46.5301 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a2dfd62-e11b-357b-8964-191e95139aac | -10.64558 | -47.90584 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b593d15f-2e8d-33a4-858e-a8327652b99d | -13.94338 | -48.41429 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dd1ca35-4c5e-399d-907b-43ba93b708a9 | -12.53096 | -47.5643 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bdbd4a8-c8fa-3f76-80dd-b3e80a70d8a6 | -9.22418 | -46.36119 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97a31860-2211-3763-a320-8b7f04e26d36 | -11.56514 | -44.9774 | 2025-10-28 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67e427c6-1bad-398f-b543-06d8ca91390c | -8.4746 | -48.21492 | 2025-10-28 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c43d9bb9-a721-3229-8b5a-ddfa7dbcd5e3 | -10.96772 | -50.25755 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae3371ad-1b1e-38c1-8e19-8576136e7afa | -13.10292 | -47.10154 | 2025-10-28 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc343e09-b152-3478-bfd6-1262607688e6 | -10.87276 | -50.10919 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e8a5ff7-39d3-3276-a0bc-431c38befc03 | -9.25585 | -50.02314 | 2025-10-28 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5704e82-7dee-338e-aa05-c59fe6f583e6 | -9.55363 | -46.9744 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 027c2de1-fdaf-3495-8e21-61a6946b8587 | -8.56702 | -47.03034 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb2ac483-80ae-3652-92ab-80e8dd39bac1 | -14.7828 | -44.98523 | 2025-10-28 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdd7606c-6859-3d82-98cc-76fec5e3067d | -13.88149 | -48.49584 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cda8e672-6121-3f2c-90b3-d0b80754ade2 | -11.04097 | -47.8595 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 025d63a1-4556-3ce5-bf96-93c17d16826e | -10.31548 | -48.78776 | 2025-10-28 04:44:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 276c586b-6bee-34a8-9ff8-5ecf682042dc | -11.28446 | -45.51134 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| abb07c3e-405c-330b-90b0-9b5645dbf27f | -9.33961 | -50.35181 | 2025-10-28 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f317d99a-8be8-39d4-9d76-987f4606d574 | -10.88708 | -48.37817 | 2025-10-28 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 839d8e1b-5aa9-391a-aa0c-bad71c77a4c2 | -8.11817 | -55.29159 | 2025-10-28 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e04b50fd-e097-3dfe-a875-d824a22183c4 | -13.43265 | -47.38114 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a842388f-b8ad-380e-a05e-3fb81479d103 | -14.53107 | -47.9971 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56c32a1c-1bfb-3b26-9bba-d0177a74fc67 | -13.88505 | -48.4963 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25c1aeba-e9d2-39a9-84e3-9ff61c29eb52 | -14.73685 | -48.16497 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69b875a5-d934-3b8f-b4b4-e959cafd52af | -10.9433 | -50.26843 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9390e27c-297e-3b74-a503-af7154fbd04d | -13.57867 | -48.52706 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d35a53b-0dd1-3d1a-96e0-d6a15c48627f | -10.91946 | -50.2682 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0535a11-3694-3c65-962c-83472aec96cc | -11.14094 | -44.94104 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README65.md)
