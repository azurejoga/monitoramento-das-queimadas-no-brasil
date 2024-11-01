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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db45d5cf-7ff0-328e-a517-d40319c1cd12 | -3.0353 | -49.4901 | 2024-11-01 03:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 2c154050-0a3f-364a-876c-030367b78bf0 | -3.2417 | -53.3562 | 2024-11-01 03:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f7d13a47-a709-363d-81a7-c1174c13862b | -3.2416 | -53.3764 | 2024-11-01 03:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e6eec9ec-8341-3119-ac2f-6afb2c7ca6a4 | -3.5631 | -47.3847 | 2024-11-01 03:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| b1cdc9e0-3c30-3dae-80c9-412e215ae163 | -3.5446 | -47.3855 | 2024-11-01 03:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5b9224fc-9078-3f44-81d3-5fafbe7e6e09 | -4.4056 | -43.4514 | 2024-11-01 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| a22cd800-fa6d-3021-825b-851e5450af5e | -4.4054 | -43.4746 | 2024-11-01 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 96cd6afb-c557-3d12-a770-8e2ce7c444e3 | -4.3869 | -43.4525 | 2024-11-01 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e06aabf9-23a3-3134-adc2-a93acd125865 | -4.3867 | -43.4757 | 2024-11-01 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 69ec1663-fd24-389d-a16a-98d62d47b150 | -4.9211 | -47.0346 | 2024-11-01 03:35:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 11cfec09-a30f-34f8-a0e0-8f64f3d4853e | -6.1229 | -43.9578 | 2024-11-01 03:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| a04e6523-6c3a-36d0-8a34-15e071415e38 | -6.1041 | -43.9593 | 2024-11-01 03:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| f42bc2ee-397e-3200-849c-54864de5a411 | -9.9187 | -64.8058 | 2024-11-01 03:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0f052267-eb85-35f0-bbc9-202ae275021d | -17.6861 | -57.5004 | 2024-11-01 03:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| ad0942d7-fe74-3ddb-b084-223ae1f137d0 | -17.6667 | -57.4822 | 2024-11-01 03:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 17bbba39-b182-3c39-b482-b0456bc6b7ff | -17.6664 | -57.5028 | 2024-11-01 03:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 192.2 |
| 3b44c937-8c82-391c-b7b9-727f75a73385 | -17.6661 | -57.5233 | 2024-11-01 03:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.5 |
| d86b31d1-7b02-3da7-b210-849aa8046636 | -17.6467 | -57.5051 | 2024-11-01 03:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| cf28dc44-a862-3c27-b664-0ef942f12222 | -17.6463 | -57.5257 | 2024-11-01 03:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 836d86e0-665e-3bbe-97fd-2b65aa67ec89 | -19.5063 | -56.7039 | 2024-11-01 03:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| a6382402-1012-3c47-ad4f-a65db84cd504 | -19.5059 | -56.7249 | 2024-11-01 03:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 0400127e-59c1-3bb7-b8f1-0b991709a02f | -19.4859 | -56.7277 | 2024-11-01 03:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| d6590172-2b15-34e6-b1a6-774fb9db6dd5 | -6.77482 | -37.5448 | 2024-11-01 03:42:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7496edc8-1c77-3c86-ba9e-d0174e4691c2 | -6.77137 | -37.54418 | 2024-11-01 03:42:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 418d41ae-00d1-31a6-838c-071ffb373018 | -6.76914 | -34.98903 | 2024-11-01 03:42:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 6d8364e8-a9e6-3d7e-be2a-89c370ff41a4 | -6.7686 | -34.99249 | 2024-11-01 03:42:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 8ca8192f-f51d-39b6-bbd1-413c210afd1d | -6.76637 | -34.98506 | 2024-11-01 03:42:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 85980511-f5cf-33fa-8dd5-97d8ab365db4 | -6.76583 | -34.98851 | 2024-11-01 03:42:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 1816bd4e-3cec-31ca-aab3-c8a52da8fa08 | -6.7653 | -34.99197 | 2024-11-01 03:42:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| f9144eaf-066f-3c81-a832-b01fe788888a | -6.76306 | -34.98455 | 2024-11-01 03:42:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dc082587-4e74-3639-99f9-38398c604d82 | -6.70715 | -37.48759 | 2024-11-01 03:42:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bbcc72ef-e779-3575-8f6f-c03db90159b5 | -6.70371 | -37.48692 | 2024-11-01 03:42:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7ebad2a9-4144-345a-a6b8-7f73bfa858f1 | -6.70309 | -37.49079 | 2024-11-01 03:42:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e0e02f00-be19-35b9-9d94-06de411756b6 | -6.50753 | -39.35519 | 2024-11-01 03:42:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7a5c1b63-ef18-3305-8341-9abc11cd328a | -6.47803 | -37.71366 | 2024-11-01 03:42:00 | NOAA-21 | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 26244d64-6c06-3daa-813b-12224391a319 | -6.39001 | -39.6738 | 2024-11-01 03:42:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85b30cff-5cfb-33f6-9dd6-3babc43f99f5 | -6.38613 | -39.6731 | 2024-11-01 03:42:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4d93495-c0d5-383f-a729-1f103c1cefc0 | -6.12289 | -41.81382 | 2024-11-01 03:42:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| eb652ee7-b2b7-3a49-82c1-892401569e0b | -6.11837 | -41.81317 | 2024-11-01 03:42:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 313b1aa6-1e38-3608-8cd0-59f8a8da33c8 | -5.95737 | -42.67693 | 2024-11-01 03:42:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e1cccd8-8f6c-3402-97fe-97d432cc743a | -5.78192 | -35.38428 | 2024-11-01 03:42:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c9b70df9-67c3-3005-a8fe-eba38418ca86 | -5.78138 | -35.38773 | 2024-11-01 03:42:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 231b2cf9-0ba1-3819-bffe-b1392898591a | -5.77129 | -35.51722 | 2024-11-01 03:42:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| edc31af7-ef99-36f0-9c74-389f680895d5 | -5.75371 | -41.77107 | 2024-11-01 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| da6832da-5226-302c-add7-3eabc3374cb3 | -5.67371 | -39.86754 | 2024-11-01 03:42:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 22dbc2e7-2659-321a-9535-c48aabdfc2ee | -5.66969 | -39.8671 | 2024-11-01 03:42:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5428bac1-abd1-348a-af01-f25b68efbfb3 | -5.62364 | -41.72422 | 2024-11-01 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 75452180-6cdd-3299-aac2-91c6399e1dcc | -5.59262 | -41.77114 | 2024-11-01 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c168d2e6-a105-3693-b8b7-11ce6d4ee30a | -5.5028 | -41.65921 | 2024-11-01 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1b423781-0f3b-34c6-8cf3-f540139dd912 | -5.46501 | -43.17396 | 2024-11-01 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d407cc5-8dbe-3a01-b2bf-ca9605af57f4 | -5.46452 | -43.17684 | 2024-11-01 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b1fc450-fbeb-3386-8eb3-c5ef1b81b714 | -5.46404 | -43.17971 | 2024-11-01 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5db62637-e4fa-353c-b7a2-62740640bd3e | -4.9777 | -39.80979 | 2024-11-01 03:42:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 829549c6-945d-3415-9bdb-0954e88eed43 | -4.94626 | -42.57783 | 2024-11-01 03:42:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d215ce55-09bf-3b64-a81c-b1b93054070b | -4.93413 | -43.63089 | 2024-11-01 03:42:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dd0c3f0-4ba4-36ee-a84c-f14ee5728be9 | -4.72027 | -42.65417 | 2024-11-01 03:42:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eca8bd4e-3635-3947-aba9-ea3df08c3b8c | -4.7169 | -42.65745 | 2024-11-01 03:42:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a03f840-a0ee-304c-a366-0ae0da585723 | -4.6301 | -42.81433 | 2024-11-01 03:42:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 12a48b06-f4ef-30c4-a35f-bde140762bef | -4.55055 | -43.10019 | 2024-11-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5908c5d8-9cce-36b3-8f06-5a7a2d9308a6 | -4.55004 | -43.10312 | 2024-11-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d81bec9a-9bf2-3d63-8a43-a644c823fbae | -4.54101 | -40.46749 | 2024-11-01 03:42:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61756e93-63ff-3c14-bb5b-811e571982b3 | -4.54082 | -40.46705 | 2024-11-01 03:42:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 941adadf-8e74-3ee9-ba8c-fdcbedc27ef0 | -4.44055 | -43.67603 | 2024-11-01 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baccd38f-1a2f-3129-b247-0fe544f9dc9d | -4.44048 | -43.67847 | 2024-11-01 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7847fc42-8f50-3c30-824f-6ba3335ea848 | -4.44 | -43.67924 | 2024-11-01 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 633cf7b7-ee30-3abe-b9ab-448f1f82e4b8 | -4.40531 | -43.47199 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d11f883-94e8-3cf0-b9a5-62f854d251e8 | -4.40477 | -43.47518 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bba5856c-b5a4-32fa-9dca-0b9ae3327acf | -4.40422 | -43.47839 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e18cea53-d486-3320-be65-c5525d257ab1 | -4.40119 | -43.46489 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0688080d-7954-3338-b370-a02ff3c84331 | -4.40066 | -43.46801 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c136f8b5-3fee-313d-a9e1-e1a71ce14efd | -4.40012 | -43.47114 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| abf60b56-0df9-3036-b182-86db749bd309 | -4.39958 | -43.47433 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fdc2ddb4-a7be-3ea4-82e9-3896bc13cef4 | -4.39903 | -43.47753 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 04f7c974-c208-3d30-a099-0b17a0209988 | -4.39849 | -43.48069 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bf855a3-235e-3a59-84b7-8ba30b19fb28 | -4.39796 | -43.48382 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9a3e264-6776-3449-9cb4-69d377a6c795 | -4.39742 | -43.48695 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7dbe454-61d1-39a9-bf57-2c451e12824b | -4.39652 | -43.46101 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d2e06c7-0bdb-3371-b5c9-55888cbd6e27 | -4.39598 | -43.46412 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a7b0dfcb-7c47-330e-9a66-35ebe88118cb | -4.39492 | -43.47033 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5e62a82b-b3c2-34d7-b24c-8f52b4efc64d | -4.39438 | -43.47349 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5281b078-22e7-3c14-a0c3-0d2ac9764c80 | -4.39384 | -43.47663 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5e877161-4e68-3bd7-b9a4-e0c6fdfff720 | -4.39331 | -43.47977 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 193ad0f6-8006-3dbd-b6dc-280b7a6887fe | -4.39278 | -43.48288 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3c54e9a-eea5-3de6-8db2-b5c37ebcdec4 | -4.39224 | -43.486 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0560024f-2eee-38cd-86a2-1e9d2594f6d3 | -4.39079 | -43.46331 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b30862e4-354a-3c55-90c8-6db662f59b1b | -4.39025 | -43.46641 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 90100e1c-abce-328d-94c8-8ef8f26beee4 | -4.38972 | -43.46951 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 65d8ea11-21fe-339d-ae74-b94ac3c34055 | -4.38919 | -43.4726 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 25710e2e-b332-3485-9f42-3c127de2091e | -4.38867 | -43.47569 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 25b085b0-93d2-3da5-a9a3-d93821c909e5 | -4.38814 | -43.47876 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e36f705-c2dc-31e7-9d0c-79ed7f20ff2a | -4.3876 | -43.48188 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e08d972-a43d-383b-a013-171f682a3496 | -4.38707 | -43.48502 | 2024-11-01 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81c382ad-275b-3aad-9dc0-b46af2451c39 | -4.27207 | -43.42435 | 2024-11-01 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a7cd8e9-5237-3f4e-89ff-5aec0b85972d | -4.26636 | -43.43397 | 2024-11-01 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c823df62-5e93-32c1-bd7b-64626021fc2d | -4.26583 | -43.43703 | 2024-11-01 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4e9e45f-f3e7-335e-8343-57d60b1d4207 | -4.26537 | -43.43272 | 2024-11-01 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 79b6bf36-dd19-352b-9551-37967c4d347d | -4.26486 | -43.43579 | 2024-11-01 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c7cfa07e-b417-323b-af8e-ab7ba1d0208b | -4.26116 | -43.43314 | 2024-11-01 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fd88c2d-f735-3f1c-b6b8-6dbecb7f2003 | -4.1898 | -38.15486 | 2024-11-01 03:42:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aa31afbf-0667-3b6a-83cf-45be64b1647a | -4.08742 | -40.87459 | 2024-11-01 03:42:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
