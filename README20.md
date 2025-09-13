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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63177fe3-98c9-3792-98bc-36562a101eb0 | -21.60788 | -46.80708 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b5f8ded5-8e51-3dc8-ba9f-2a9d5a6694a1 | -20.44858 | -46.44304 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9f0e5e2-6c32-30bd-8843-d9016c292aa5 | -20.55199 | -45.83561 | 2025-09-13 03:21:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9d484ed0-5188-3240-8b3f-9013a1e42ba3 | -19.99368 | -46.90479 | 2025-09-13 03:21:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c5188b38-7b33-338d-a866-fce24a77061c | -19.32932 | -45.11051 | 2025-09-13 03:21:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c68cc24-e285-37e1-896b-027d9b60a3f6 | -25.51723 | -49.11182 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 818fc437-0afd-38e4-9322-a6ab6182a5c9 | -20.55751 | -41.0158 | 2025-09-13 03:21:00 | NOAA-21 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4bab9ad5-0282-3e49-9c03-d98a57b4f500 | -19.64125 | -45.08421 | 2025-09-13 03:21:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8e63a37a-8d34-3416-bf5f-73f2c77d2a28 | -19.64254 | -45.08234 | 2025-09-13 03:21:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 58d0e91b-64b4-3ba8-9f0b-8d2964577873 | -22.79542 | -47.80441 | 2025-09-13 03:21:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f69fc1fe-1251-3bcc-bb92-1f90538f4a06 | -20.08896 | -46.90977 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82c1c698-1ca4-3fcc-aac7-815e7752ded9 | -21.32134 | -44.99104 | 2025-09-13 03:21:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b08d6f51-62cf-3941-ab25-339f591d79f5 | -20.33696 | -46.66417 | 2025-09-13 03:21:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 05a1c04e-82e3-38d4-a882-f3be02869f20 | -20.10138 | -46.91963 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0768dd0d-6ca8-3a70-b4e1-b386b6fd1204 | -20.5534 | -45.82973 | 2025-09-13 03:21:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e85bc1b2-9398-36a6-b45a-aaf331521df2 | -21.61481 | -46.81374 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 8046828c-af4e-336a-9c05-52c700e51340 | -20.44835 | -46.4486 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2fd9da1c-f8ec-3de1-88db-d04cd6291f9a | -22.24768 | -46.149 | 2025-09-13 03:21:00 | NOAA-21 | BORDA DA MATA | MINAS GERAIS | Brasil | 3108305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c8536d35-947c-3879-bbb3-d18922066493 | -21.62201 | -46.81373 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 7ed2b19b-6cbb-3fb4-a0eb-4d7f070a4b1f | -20.09968 | -46.92659 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ffd20869-1c20-37b3-a47a-aa8aa2962e4f | -20.54542 | -45.83411 | 2025-09-13 03:21:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e474f8af-76e6-3151-bb00-33c652b46180 | -19.33436 | -45.11793 | 2025-09-13 03:21:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f4ef8bad-688b-36b7-89cd-1ffc060c313c | -21.61658 | -46.80096 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 96f3be8d-5e10-3039-873d-d5e4fb771b3a | -20.59967 | -44.90622 | 2025-09-13 03:21:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a97b079f-edef-3504-ae78-39c48940eaa4 | -20.55156 | -45.82963 | 2025-09-13 03:21:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 000684b1-2ccc-3141-8e30-a8317d04eae2 | -19.3357 | -45.1123 | 2025-09-13 03:21:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| da6c0d79-5bc3-3b68-a676-6c971e3ce5e8 | -19.9875 | -46.91121 | 2025-09-13 03:21:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f73aa9ba-b399-3e38-a530-4a587a2ce77a | -21.32306 | -44.99146 | 2025-09-13 03:21:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c2ee288f-39bc-337b-bdb4-98d5d3eb2c97 | -20.09588 | -46.9118 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf16f652-896b-357f-9547-fd2d3d69b843 | -19.63534 | -43.73448 | 2025-09-13 03:21:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02b0a3dd-ccee-3a94-800e-a056863711d8 | -20.09362 | -46.93997 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e5fefe4-92b0-328e-a281-712cc135d507 | -19.65294 | -45.86834 | 2025-09-13 03:21:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1da12ff0-c4c1-334b-9033-c551fcc81efa | -19.04246 | -46.66102 | 2025-09-13 03:21:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eab60d85-e2a2-350a-9363-61ed8e3bc445 | -19.97775 | -46.909 | 2025-09-13 03:21:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01500189-585f-34b5-abe6-8e9dcfd3b696 | -25.51353 | -49.11095 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d9be47a1-9565-3aab-9861-3b0629337cbf | -21.61512 | -46.80685 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ba612aff-b3ad-385d-88e7-5222fe74b34a | -20.5501 | -45.83554 | 2025-09-13 03:21:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 29537ddf-8a73-34b4-abc5-86e6265bcb93 | -19.33546 | -45.11362 | 2025-09-13 03:21:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c824ef4e-b304-3a89-ad62-4bb78b80de08 | -20.10608 | -46.91988 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2eb33e7d-31bc-3919-892c-1c254f4f1827 | -20.08637 | -46.9392 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3bdf3f0-14cb-354a-8d71-9398d3171e25 | -20.08458 | -46.94632 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96f64747-b4e7-3768-8fe8-8ce2d35cf668 | -20.09703 | -46.92636 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 97e257a2-ff4c-3209-80ae-3648af52bdba | -21.61647 | -46.80722 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a4cadaf5-e558-3b31-ab7c-ea4cf1f78c57 | -20.08905 | -46.93973 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b8d1f909-2042-37cc-96db-d5015753aa93 | -20.59877 | -44.91011 | 2025-09-13 03:21:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 07f9deb1-1706-3717-b000-a81c67d2ac8c | -20.07732 | -46.94564 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7ecfdd6-905f-3841-ac83-ee38a44e1501 | -20.44986 | -46.43771 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 96c8f1eb-f01d-3aa3-97bd-32211b8cf3c3 | -21.62 | -46.82163 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| efaa2978-be83-3031-93eb-24d7b31c8c39 | -25.52051 | -49.11306 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ce80cce2-f341-3d09-bb7d-966a1124885d | -20.45524 | -46.4452 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e344b03-9d1c-302c-a657-865adc0d472f | -11.8659 | -50.5791 | 2025-09-13 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 6e85a224-ee4a-3bb7-87dc-f6a96d8b6350 | -9.5137 | -54.6292 | 2025-09-13 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 242.8 |
| c4f4b210-a8f1-3e36-8149-bda457bb5110 | -21.5912 | -48.419 | 2025-09-13 03:30:00 | GOES-19 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b56c2f22-f1fe-32f0-baf9-0b3a56071f6a | -11.8468 | -50.5813 | 2025-09-13 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 97adf09d-2688-3a66-a2d1-7c0297c4b32b | -9.2843 | -59.418 | 2025-09-13 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 304dc7c6-b926-367f-b479-175a30f928e5 | -10.7664 | -50.5299 | 2025-09-13 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 2297582b-00d1-36eb-83a2-d3679830a010 | -16.3418 | -51.5434 | 2025-09-13 03:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 79f34529-9ab8-3632-8f90-406e69d27fce | -8.1004 | -50.1821 | 2025-09-13 03:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 31430f16-65ea-3da5-b86d-5cde195ee694 | -9.5326 | -54.6075 | 2025-09-13 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| ce4829a3-a90d-382f-8494-23402d0adc20 | -11.7384 | -46.6231 | 2025-09-13 03:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| cf2cba24-462f-3c1d-9335-d3a44711e801 | -11.7388 | -46.6005 | 2025-09-13 03:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 6be37442-d95b-33b0-95c4-1d1888b08a5e | -9.5135 | -54.6494 | 2025-09-13 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 074de1f3-888c-37da-a2c2-fb1e4b3709f2 | -21.6187 | -46.8115 | 2025-09-13 03:30:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| 5f5f9325-6db3-3cdf-bc8a-22ca896ebc9c | -12.006 | -47.7505 | 2025-09-13 03:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 494b68c2-e905-3749-a7ac-e878b955a93a | -9.5006 | -55.9588 | 2025-09-13 03:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| fa9df0d0-912e-3551-906d-a13aeefc91cc | -11.8472 | -50.5598 | 2025-09-13 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 240.1 |
| 7c44deff-acaf-3a8c-ab8a-293e960313ba | -14.2905 | -46.0693 | 2025-09-13 03:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 11ece1ec-0036-3504-b3c5-ef9f7ace399c | -9.5004 | -55.9788 | 2025-09-13 03:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| d0fa1107-05e9-3c20-b03f-5b290e080d66 | -11.8281 | -50.562 | 2025-09-13 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 180.2 |
| d3786611-ed0e-3fd7-9c3e-11a80d7b5baa | -9.5322 | -54.648 | 2025-09-13 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 8a1a2632-d90d-3c36-a0ce-0611ee5614a8 | -11.809 | -50.5642 | 2025-09-13 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 2a8bad9c-9b92-3872-9d83-9850c350e1e5 | -10.7853 | -50.5279 | 2025-09-13 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f2e87d12-d7e6-337c-b24a-5b76321977d3 | -10.785 | -50.5493 | 2025-09-13 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f5846a61-c148-355a-b092-f8cd52f671b2 | -9.2658 | -59.3997 | 2025-09-13 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 4029b933-82e1-3497-82af-1cbc44d14892 | -9.2844 | -59.3986 | 2025-09-13 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ae35c3a3-4e41-3fee-8b3a-2d402e074ed7 | -17.272 | -46.1037 | 2025-09-13 03:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 3121a6cb-ed74-334c-ac19-41f52ba9a13e | -10.7477 | -50.5106 | 2025-09-13 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 191.6 |
| f1fd1fb5-56e1-35d0-bf75-dd2b42be4522 | -10.748 | -50.4892 | 2025-09-13 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 62012fc4-b6e6-385d-ab35-f736fb9a3ad2 | -10.7667 | -50.5086 | 2025-09-13 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 5ca0a51e-8023-3c83-ad12-078d136644c1 | -12.0056 | -47.7728 | 2025-09-13 03:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| dcdb6057-6d13-310a-a146-52671da2270b | -9.5324 | -54.6277 | 2025-09-13 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 327.0 |
| 2f2f20d5-26ff-360e-8bfa-8e9989fa8fe8 | -11.9865 | -47.7754 | 2025-09-13 03:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| f1c75e55-5cb7-3867-8379-26ea6ec0d4a5 | -11.8662 | -50.5576 | 2025-09-13 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 17022969-f6f2-3c95-9e02-946eff0b8e42 | -9.5139 | -54.6089 | 2025-09-13 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 637112eb-91ba-3d21-916d-59dd319f625d | -9.2656 | -59.4191 | 2025-09-13 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 2c3f258d-3279-38c5-a67d-110d03b4c70e | -11.9869 | -47.7531 | 2025-09-13 03:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 695579ca-9b6c-3364-834c-239caa4029ef | -16.0805 | -49.9489 | 2025-09-13 03:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 05379810-0a61-3f96-ae71-72ae56d8e2f2 | -9.2472 | -59.4007 | 2025-09-13 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 08c28169-acea-3f63-b3c9-6c745e4f8a12 | -9.5324 | -54.6277 | 2025-09-13 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 305.2 |
| 1c8eae5a-d376-3888-9faa-3095f57514a8 | -9.2658 | -59.3997 | 2025-09-13 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 21c4e726-8bc4-382f-b520-66d046f6f00c | -9.2843 | -59.418 | 2025-09-13 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1f409531-3d19-387f-8732-241fdfe9ff1c | -8.1004 | -50.1821 | 2025-09-13 03:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| f07388b8-a62c-3dcd-94fb-503c6656df4d | -8.0817 | -50.1836 | 2025-09-13 03:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c8fcde94-901d-39f0-9a6e-db4ce9ddc5a8 | -21.5912 | -48.419 | 2025-09-13 03:40:00 | GOES-19 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e4f2c9eb-50ac-3a22-8608-ca2a9c79ff95 | -9.5137 | -54.6292 | 2025-09-13 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 230.7 |
| 04fb2794-4529-345b-9f5a-bd3c9c133b9c | -9.2656 | -59.4191 | 2025-09-13 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 7a982330-433a-3605-81e0-e7a47270ebb4 | -14.2905 | -46.0693 | 2025-09-13 03:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 574ba878-7c69-389f-80c2-4c3ab2d004b9 | -10.7477 | -50.5106 | 2025-09-13 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| f4681f51-a587-35bf-bfdf-8a8066ef52e1 | -21.6187 | -46.8115 | 2025-09-13 03:40:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| ded2d754-4629-3526-8a75-0549a7cbfdf5 | -9.2472 | -59.4007 | 2025-09-13 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |


[Clique aqui para ver as próximas entradas](README21.md)
