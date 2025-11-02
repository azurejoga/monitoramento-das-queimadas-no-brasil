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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 739abf0c-3060-3cdf-a82d-3d92eb005ba9 | -4.13077 | -51.13889 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd577d5e-386a-372f-95af-63389351e97b | -4.54823 | -45.79517 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aad703b-d125-390a-b480-c7b661aa7de1 | -3.55656 | -54.57068 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cb0408a6-18c1-3309-9a0c-ef4587fe5b6a | -0.68782 | -52.37047 | 2025-11-02 04:18:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 442c4f02-1cf3-38fc-8cda-c8a2f4021467 | -3.22226 | -50.58588 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b3027e0-6830-39e0-81a4-79618e9c47dd | -3.56246 | -54.57162 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 85643982-87df-363b-a236-2c1b8ea0380f | -3.5056 | -50.47382 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 22651a08-524c-3a84-9ad7-4659a176e1e6 | -3.67158 | -50.48606 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d9ce4b1-874a-37d3-8ad7-f935c1999f0e | -3.06421 | -45.4518 | 2025-11-02 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a56b98b-f6c4-3707-a146-50e3b7c23221 | -4.5409 | -45.79768 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 330fb1fe-5923-319e-b63b-f2f2f691399f | -3.55584 | -54.57488 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1e81c04f-99cb-385a-bebf-f22bb066276d | -3.66005 | -50.70939 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bab8e70f-d638-34f5-bc9c-990f50b582f8 | -5.07473 | -43.67703 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcdfd5d1-47c3-3b2c-9c50-ed871e1bdc39 | -4.30284 | -41.44907 | 2025-11-02 04:18:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f4eb6719-c059-3918-a6c8-c61a4397f770 | -3.81957 | -50.93793 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e2b7dd7-5487-31ff-a2f2-0b947aa22e08 | -3.58951 | -47.51789 | 2025-11-02 04:18:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 868c3424-3bc8-3228-91db-f2bf4872f6bf | -3.43998 | -52.63822 | 2025-11-02 04:18:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f7da2e15-802f-3e1e-965d-239145f602ea | -4.71885 | -45.69943 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf982bff-e2dd-3676-9534-91f2e463bfae | -3.02055 | -53.96985 | 2025-11-02 04:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ec39ff4-6e9d-3c39-8f51-6336af38cd62 | -3.89555 | -52.20871 | 2025-11-02 04:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9310ff9e-e007-3ad5-99fe-1f9438bbb87d | -3.01945 | -49.44772 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 87be335e-2f3c-3be5-a9b6-6d6e8fa03287 | -4.68168 | -44.62362 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 836487b8-aab8-333d-9de4-5710d4de7e8d | -1.73795 | -54.45784 | 2025-11-02 04:18:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 17ccabc4-e9e1-3d02-8467-873556ff49dd | -3.22679 | -50.58658 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0eea881-6d4f-3cf9-98f6-443b790c14d6 | -4.65217 | -46.83814 | 2025-11-02 04:18:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97752a97-a02e-3882-8ad5-e7e282cc29a6 | -1.42523 | -55.23622 | 2025-11-02 04:18:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 784f96ed-6694-30b7-bcde-b8daf6a6a03e | -5.11844 | -43.37443 | 2025-11-02 04:18:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 930f0a59-1c91-3f71-b68f-6dcbccde030c | -2.74536 | -47.14296 | 2025-11-02 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e623e232-9626-3743-a180-59052d777327 | -4.72281 | -45.69624 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3346b80c-32d1-3f0f-936e-0f5cceb661e5 | -5.03703 | -43.6145 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98307695-a523-319e-acc6-9cc6c1a792ec | -4.85099 | -45.68328 | 2025-11-02 04:18:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f5fa25d-ee99-35eb-a387-1fdbc43e487c | -3.01588 | -49.44319 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a08a5a9f-72c1-348a-96c9-a5bd7ac90a2f | -3.80926 | -52.41233 | 2025-11-02 04:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3665d18-8fc0-3293-be4e-172f07669b36 | -3.56775 | -51.6392 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d385565-e644-3096-b15d-38b05c7438a9 | -3.01483 | -53.96896 | 2025-11-02 04:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef41c18f-8618-3162-8127-9836e9b372dd | -4.70344 | -45.88304 | 2025-11-02 04:18:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87e4f474-659c-362c-89de-4bbca125e532 | -3.43068 | -45.91238 | 2025-11-02 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29388fbf-2fb1-3abf-a67a-7ecbb7a567e3 | -0.46214 | -51.75862 | 2025-11-02 04:18:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 49e8df4e-12f1-3537-b0c0-500b22740f8c | -4.51187 | -46.00371 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00b03a0d-cb2c-32d4-b63c-7361ab6cb73d | -4.5401 | -45.67124 | 2025-11-02 04:18:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 934f6885-904f-3ea6-a217-99a77c32fbe7 | -4.5042 | -45.78828 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 582fc8bf-d9bf-37b2-a318-1df60adc6ecf | -3.06551 | -49.37609 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7ec0e1f-d6ba-3dab-8787-22874e0d6997 | -4.4803 | -46.0705 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e3febe6-1ff9-3076-a3e9-e022a49c2428 | -4.38931 | -46.41954 | 2025-11-02 04:18:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b050df92-25e9-3035-b422-f925948be10d | -4.24417 | -47.52894 | 2025-11-02 04:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8555fe18-e3ba-3396-92e1-17a19ca66644 | -3.13073 | -49.23502 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cf566d0-f842-3f78-bd1e-69459bb0dd35 | -4.37749 | -49.74575 | 2025-11-02 04:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52e0dcc7-f5b8-3638-849c-59dd0f5436be | -3.89925 | -45.7464 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5e2b0b28-7dd3-3d13-a858-4de2433f4bd5 | -3.44084 | -52.63929 | 2025-11-02 04:18:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c50b9af-a810-31b8-bf74-201e3ee3d67c | -3.60243 | -50.6271 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 424d4d0d-8924-3fd3-a9c4-418a2935093b | -3.17275 | -46.58201 | 2025-11-02 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0131d713-4153-30fa-90b3-30cac2cbd655 | -1.74145 | -54.46013 | 2025-11-02 04:18:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e919f5ec-afe6-3eb8-87d0-b143a8036ae5 | -4.58011 | -44.79199 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f462591e-6c3d-3431-9e0e-58172246c0d8 | -3.46149 | -50.22138 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f45353eb-2a2e-3159-8063-db050ebada32 | -4.60995 | -45.6339 | 2025-11-02 04:18:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e253de6a-380a-3706-9204-379f10fb4cbc | -3.3574 | -49.24452 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b564429-6499-336b-867b-9fd22c455593 | -5.07304 | -43.66615 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d08d3fe4-8e9b-3200-9d1e-ed522c32d072 | -3.09729 | -43.93973 | 2025-11-02 04:18:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b101c87-c0a2-336f-b77d-a511a9888c04 | -4.10838 | -51.10119 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ae05f95-3f14-3d5d-a5c3-af7259da8ead | -4.64257 | -38.57232 | 2025-11-02 04:18:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 1bc0d5f7-089e-34f0-bf43-a12191b40846 | -4.58066 | -44.78851 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d0fdb6b-d883-3a72-88c1-dc1e4293e456 | -4.55105 | -45.79931 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eaedf726-93d6-317c-921a-5c75935b042e | -4.30633 | -41.44971 | 2025-11-02 04:18:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 62acdb72-8e4f-3689-8baf-b6cafb78480c | -3.02545 | -51.22655 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9efd3d31-6939-30aa-aa5f-7f4218ffffaa | -2.35093 | -47.54214 | 2025-11-02 04:18:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3601ac6e-879e-3503-926d-63e7493611d1 | -3.07655 | -51.24728 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cc4f109-c3fa-3a4c-b252-83858992a6fe | -3.44139 | -52.63609 | 2025-11-02 04:18:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 821d3eca-8806-3909-95ad-8931f08a30d3 | -4.15815 | -46.79582 | 2025-11-02 04:18:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0591ef36-735f-3ec5-9933-ddb4954f4afd | -2.83472 | -49.40799 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b46095e-b58a-34f6-85e7-90fbc801d0f2 | -5.78508 | -40.80792 | 2025-11-02 04:18:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f0c47c9d-8d56-3d66-a18c-06e7d2aa2f36 | -5.00551 | -43.35656 | 2025-11-02 04:18:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c39f406c-b054-3fdd-ab14-3d2c43422d1c | -5.52427 | -41.10326 | 2025-11-02 04:18:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dfc61f97-b289-3127-a95f-6bf4a84a0f6d | -3.47437 | -49.92651 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93cd43f6-e025-371d-8267-d977b8b963ff | -2.49419 | -48.15042 | 2025-11-02 04:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe0ed99c-83e9-340a-a6a4-3e64fe77e5d1 | -0.45701 | -51.75781 | 2025-11-02 04:18:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a83721b3-80ec-3f33-8ea0-f4e9670045e2 | -4.67837 | -44.62311 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec0f41c5-3eeb-3bda-8202-35859a90b177 | -3.0774 | -51.2421 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2164a79-e848-389f-afca-4943472f8617 | -4.30094 | -48.06936 | 2025-11-02 04:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 231bc722-93a9-3976-ba7d-8cd18fc5d982 | -3.89338 | -52.09936 | 2025-11-02 04:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 084deaf5-5b8c-3cb8-a752-6bcd9193429a | -4.38584 | -46.41901 | 2025-11-02 04:18:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 159bed1e-b36b-3144-a05e-1575a0c302ef | -3.45237 | -45.57603 | 2025-11-02 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8d47982-606a-3977-ba81-857bd12eefba | -4.68123 | -45.66349 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca858bd8-6fff-324a-b529-350b1e7eac8e | -5.78574 | -40.80347 | 2025-11-02 04:18:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 79bfe885-70a5-38a9-890f-8191637d330b | -6.09834 | -35.35814 | 2025-11-02 04:18:00 | NOAA-21 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1edf467d-c8ac-31cd-b8bd-4aa9cdffdb63 | -4.61321 | -45.80894 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1364a519-692f-331e-a241-7c53c17f27de | -4.14188 | -51.14997 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cdbbb91-0284-3b65-853b-42210f2cded6 | -3.02123 | -53.96589 | 2025-11-02 04:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0d9fead-8ab7-3f4d-b8a5-984e3bc7b18c | -3.32259 | -51.57273 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 524fea8d-949e-3beb-97a3-1b10b7a33423 | -4.33376 | -40.1899 | 2025-11-02 04:18:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f919955c-087a-3b37-b5db-c2519e6b1074 | -4.01831 | -50.45974 | 2025-11-02 04:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e8a278c-1677-3a9e-a9b8-ea968afc607b | -3.79946 | -46.11105 | 2025-11-02 04:18:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01217324-64c4-3c5a-a82b-e39cfcb10b38 | -4.37392 | -49.74128 | 2025-11-02 04:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abb71803-afb4-31a0-9ca6-759a0ec4057c | -3.42713 | -50.23787 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70b556f1-beed-3a94-8442-f96d34265d3f | -3.37937 | -52.36712 | 2025-11-02 04:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3f90163-ef6d-37a8-aac7-b6209e7c9fd0 | -4.63897 | -38.56789 | 2025-11-02 04:18:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 8867e5ca-87e6-3082-a0c2-7ec08f330a18 | -3.14106 | -49.42015 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58189b41-1ff4-3e47-af73-680f9a9c28db | -3.94358 | -46.61736 | 2025-11-02 04:18:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ef90221-1f3f-3a4a-a4d0-24bf6cfb10ae | -4.0562 | -46.75214 | 2025-11-02 04:18:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e9f417d-870b-31d0-9b2e-fe4d56c3f266 | -2.63029 | -47.29959 | 2025-11-02 04:18:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8adf89f3-fefb-373f-b0ea-0ee3d4479283 | -3.55841 | -54.57013 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |


[Clique aqui para ver as próximas entradas](README10.md)
