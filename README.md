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
| d8624510-887c-38e9-8c9e-fd2198c5cf3c | -5.7662 | -43.6245 | 2025-04-19 00:10:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91564c15-b104-3243-845b-226b4957e808 | -7.0617 | -44.376099 | 2025-04-19 00:10:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c2c13b8-5944-3561-bd8b-af36c0d10063 | -7.0634 | -44.3834 | 2025-04-19 00:10:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb6f6549-0c00-3773-b4ad-026d0135b2bc | -5.776 | -43.6222 | 2025-04-19 00:10:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7104575c-74b1-30d8-b751-70068fbe511a | -12.4237 | -39.223598 | 2025-04-19 00:10:00 | METOP-B | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d34d75df-b49c-3563-a442-87eaf2a841e6 | -5.7742 | -43.614399 | 2025-04-19 00:10:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13d02653-c358-3be8-9d93-d284c5002198 | -7.0503 | -44.370998 | 2025-04-19 00:10:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d51d9c9-92db-3c7b-b859-51f9e5c62103 | -5.9178 | -44.467098 | 2025-04-19 00:10:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 237668ac-cdf1-3544-be29-17fd6dd894cb | -5.9161 | -44.459801 | 2025-04-19 00:10:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5492e5cc-433d-3fea-ace5-afa792ee4fb2 | -5.7644 | -43.6166 | 2025-04-19 00:10:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef676be6-34ee-365e-b316-c06e0fa09122 | -11.38 | -42.300201 | 2025-04-19 00:10:00 | METOP-B | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 89bb3492-1737-3b64-83f7-2e55d1f02dd1 | -7.0519 | -44.3783 | 2025-04-19 00:10:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9de9acb-c844-32c7-b984-e3843f9a21ec | -7.0601 | -44.368801 | 2025-04-19 00:10:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08cac074-4eb2-3650-9acf-7e966545f8e6 | -5.78877 | -43.61197 | 2025-04-19 00:50:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4aea181d-dbf3-3bf3-a0fc-748298737ad6 | -5.94222 | -44.46506 | 2025-04-19 00:50:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 02133d02-b8d9-35ab-8153-fb8774fda08c | -7.07601 | -44.38261 | 2025-04-19 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 7712b448-6021-3d4f-a336-e9d192273225 | -7.07339 | -44.36559 | 2025-04-19 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d92a23e9-28b3-3c80-a14e-28e8c1a1b9a5 | -5.79186 | -43.63227 | 2025-04-19 00:50:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b6c5ed1e-c056-39c7-b7b5-c06b3e2b18f2 | -5.16286 | -45.1105 | 2025-04-19 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 61786f3c-6eed-31a9-b593-55418943849b | -7.0624 | -44.364799 | 2025-04-19 01:00:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b5e770b-81f1-3be8-800a-6260147c1125 | -6.5606 | -51.103901 | 2025-04-19 01:00:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87759f27-5886-330d-8a0a-5c3551d6c51b | -7.0674 | -44.384701 | 2025-04-19 01:00:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f1e0ddb-b463-3704-90ea-3748d483dfd3 | -5.22241 | -36.14627 | 2025-04-19 03:19:00 | NOAA-20 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1dd3024-1cee-364c-9503-9e6669837673 | -7.06924 | -44.38328 | 2025-04-19 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 740376f2-457c-3d38-b5c5-c27d1e1bcc43 | -11.91118 | -37.7178 | 2025-04-19 03:21:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 40aa12be-903c-3925-8a9c-6a85e6c75281 | -5.78449 | -43.62684 | 2025-04-19 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e214a98-1714-3895-9293-d5505f476d89 | -5.79146 | -43.6209 | 2025-04-19 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df012bec-aa46-337f-b52d-817bef2a9e15 | -7.07758 | -44.3782 | 2025-04-19 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 33e8736e-5006-3cd6-b495-394ba6d41f60 | -10.69512 | -37.05033 | 2025-04-19 03:21:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01c88c5b-acce-3ba9-87c9-65deb34684ba | -5.79263 | -43.62149 | 2025-04-19 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f13473b7-b256-318e-ae16-c601b3eadced | -7.29851 | -34.82481 | 2025-04-19 03:21:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8671bf2d-bf2b-3929-acbb-69b701ee2b9d | -10.01239 | -38.58007 | 2025-04-19 03:21:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8e41b381-dc03-3a8d-b84d-5d65c1a66a61 | -5.78327 | -43.62627 | 2025-04-19 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 412de292-e1ea-35d7-9d76-564890b1d833 | -11.07192 | -37.13198 | 2025-04-19 03:21:00 | NOAA-20 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a496589e-1d6a-35b4-8b9d-91915558ee7d | -7.07049 | -44.37674 | 2025-04-19 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9104e0e0-3e82-3c4b-b1bb-e0f22cb5e9cf | -5.7902 | -43.62097 | 2025-04-19 04:12:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3065e419-0836-38c9-a5b2-0bae18fc772c | -5.79352 | -43.62148 | 2025-04-19 04:12:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d992c18-895f-3ee2-a64b-0c39cb5349db | -5.79407 | -43.618 | 2025-04-19 04:12:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6822d9e-7796-3a77-bd49-ebb0ffb7110a | -5.22565 | -36.14696 | 2025-04-19 04:12:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a725d2ba-1a6a-3a54-b361-1c615be88d37 | -5.43825 | -46.28718 | 2025-04-19 04:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40d9ec9f-47eb-3215-9c1d-f8e3a72185bc | -5.48501 | -43.33387 | 2025-04-19 04:12:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db276900-f8d3-3082-9e8f-eacce4945cae | -5.79684 | -43.62201 | 2025-04-19 04:12:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d551be8-7681-34d4-8a57-1a53866377a2 | -5.1609 | -45.10854 | 2025-04-19 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93d4ab1e-2be8-3822-af59-5133b388ab0a | -5.16438 | -45.1091 | 2025-04-19 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96ccf334-2d53-3ebd-bee2-13b1e99bf2c7 | -5.78633 | -43.62394 | 2025-04-19 04:12:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5e12946-7df3-3a13-ace4-2445aca1ffc1 | -5.79739 | -43.61853 | 2025-04-19 04:12:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75a70e87-f829-3bb7-a453-a9c56805eb41 | -5.78965 | -43.62445 | 2025-04-19 04:12:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd3c1212-5f10-33c5-9419-e701ffaea3db | -7.08015 | -44.37123 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e90cc86a-6452-3267-8e7b-2c2adcb79790 | -7.08573 | -44.37941 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dae820e3-f37a-3475-95f8-8c01d91036d2 | -5.94183 | -44.46682 | 2025-04-19 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1ca8aca4-72f3-33a1-b6a9-98ece0fbf32a | -10.0152 | -38.58133 | 2025-04-19 04:14:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4c8f450d-e29c-3028-91cb-ada8b59ef73c | -7.08182 | -44.38241 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0c8217b-37c6-3c71-b297-8a77f995b795 | -7.07177 | -44.3808 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc3b7e30-41c3-3dd9-b6ce-08fdf783a3a8 | -7.07233 | -44.37725 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb03b1b6-ffca-3a8c-8fa4-390dc461592a | -7.07847 | -44.38187 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c52df69f-27d5-352f-9512-95d61b1c7e72 | -7.07903 | -44.37832 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d977b12-4928-339c-9f0a-988d63b4f5d8 | -7.07568 | -44.37779 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5de2be07-249e-3f66-ae7d-7182a2cac190 | -7.07624 | -44.37424 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b9f721f-4e9c-3ba6-a9ea-d8561b086de4 | -7.0768 | -44.3707 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11a4b0ae-1a8e-3638-b5ad-811eda2ec02a | -11.40544 | -42.30301 | 2025-04-19 04:14:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a8b16871-e930-3373-9c36-d3a41d263cc0 | -7.07959 | -44.37478 | 2025-04-19 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7291bd1-ab4a-3142-be81-9ee42015d787 | -5.94917 | -44.46429 | 2025-04-19 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ee0a31f-7c80-378c-a768-f253ff47e685 | -10.01572 | -38.57769 | 2025-04-19 04:14:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 51b57264-b33a-3ffd-b654-353879a8233e | -7.31225 | -45.09702 | 2025-04-19 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86ba209e-3330-33b7-a1ce-9d9c60a94075 | -23.63195 | -46.42426 | 2025-04-19 04:17:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59dd2111-05aa-3527-b6d6-262ca4660e59 | -23.63137 | -46.42804 | 2025-04-19 04:17:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 57186a15-fe3d-3e0e-bff7-77026b0f71dd | -21.4562 | -48.7041 | 2025-04-19 04:19:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c5df7cf-58a7-3043-87d4-b85c36ebd8ad | -30.13481 | -50.51273 | 2025-04-19 04:19:00 | NOAA-21 | CAPIVARI DO SUL | RIO GRANDE DO SUL | Brasil | 4304671 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 52c0038a-1b2b-3f64-bb59-6682d1e1442a | -22.5396 | -48.81181 | 2025-04-19 04:19:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30fddb52-cf8a-3c44-a50d-2369bddcf241 | -23.34026 | -46.77445 | 2025-04-19 04:19:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bc280c90-3c2c-37b3-b658-0d6e5f640724 | -23.40811 | -46.55524 | 2025-04-19 04:19:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2e828e4c-39bc-33e9-843b-05d5f7cf3725 | -29.92802 | -50.21712 | 2025-04-19 04:19:00 | NOAA-21 | OSÓRIO | RIO GRANDE DO SUL | Brasil | 4313508 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| fb911b30-d0b4-3ea2-847b-888c39c05312 | -5.161 | -45.10839 | 2025-04-19 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5787737a-68be-3bd2-9bb0-60588d4ff414 | -5.48362 | -43.33261 | 2025-04-19 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8978e94-81ef-3840-b0be-aec9c0ef5995 | 1.98967 | -60.87383 | 2025-04-19 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea303df0-b30a-310b-9048-ff4b85b77858 | -5.16427 | -45.10686 | 2025-04-19 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| facf965e-bbc2-329b-996b-26a98c96fa94 | -5.16046 | -45.10629 | 2025-04-19 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 065b0393-fceb-34fc-8ec7-06c472d605f4 | 1.99664 | -60.87259 | 2025-04-19 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 127a3e11-ae99-3221-82e4-6228a633f2ea | -3.43743 | -51.24395 | 2025-04-19 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ec013d5-3480-395c-8f5d-80b7f96b0b01 | -5.16481 | -45.10893 | 2025-04-19 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74239c63-e340-320d-9ac0-56f2bd1210d4 | -5.94037 | -44.46927 | 2025-04-19 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f660d6a-9792-3ac8-b039-021fa763ff27 | -5.78918 | -43.62107 | 2025-04-19 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d596f8fc-08ba-31e8-9404-2330b8e653ea | -7.0838 | -44.37976 | 2025-04-19 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d6f6180-91e5-3fd8-941c-b8690ddc23b4 | -7.0756 | -44.37864 | 2025-04-19 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68e5ddd7-5337-3198-b417-9dc435dd4cbe | -7.0797 | -44.37921 | 2025-04-19 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57fa0cfd-6754-33c9-9b02-02c91446f852 | -7.07095 | -44.38177 | 2025-04-19 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7fdd086-f31f-3d3e-b846-111532959e94 | -7.07615 | -44.37492 | 2025-04-19 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 948544e8-685f-3689-813b-492dfa6640ec | -7.0715 | -44.37806 | 2025-04-19 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5586e4c2-a67a-3b24-89b9-f4726d0910cd | -5.94114 | -44.464 | 2025-04-19 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b119bfc6-8d69-3835-930b-1c8b6d54265e | -5.794 | -43.61775 | 2025-04-19 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f49ab7d-c706-385a-92ac-a5b0dc1b5645 | -5.7886 | -43.62496 | 2025-04-19 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e2d7c7d-36aa-340f-bc34-5a2706472e78 | -5.79764 | -43.62232 | 2025-04-19 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87c7158c-a510-3f9e-99fd-dec03c1b554f | -5.79341 | -43.62171 | 2025-04-19 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e134dce0-1032-33aa-9671-a0896e27f28e | -6.21543 | -55.642 | 2025-04-19 04:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce8b2c37-8b99-3c67-ac90-9b3cf16dda82 | -7.08025 | -44.3755 | 2025-04-19 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77b54573-6cc7-3abc-a1ba-c9b18b4a8dae | -7.0767 | -44.3712 | 2025-04-19 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1af0e7f9-b870-3c38-8f04-8bd5befac2a6 | -5.79823 | -43.61836 | 2025-04-19 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a7df1e5-10c7-3e86-b072-6f6f68205190 | -17.51988 | -54.29148 | 2025-04-19 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 58e79a93-a8e8-3a74-8c12-0216a3c0f0a0 | -17.52401 | -54.28822 | 2025-04-19 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| e542c8ee-732c-3b09-84c1-86feb84b0cd5 | -23.59281 | -47.44057 | 2025-04-19 04:44:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README2.md)
