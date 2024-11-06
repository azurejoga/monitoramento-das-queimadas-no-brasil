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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99dce090-f01e-3feb-8748-8c2e20e1867d | -4.05717 | -46.93336 | 2024-11-06 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f5bc6fbe-6251-38cf-b058-7594bafd1949 | -3.53128 | -52.99891 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 998d8507-ae22-33f7-b8f4-fb3e324a5f51 | -3.17749 | -50.59411 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceecaf2a-5917-3f2e-a556-b9768a6abfb3 | -2.50179 | -49.11287 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 215f1420-ef7d-3f1c-b104-9eaa7ab9f24c | -3.74202 | -50.0617 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cfc2672-9191-3e04-b8f3-f52f44130112 | -4.13069 | -43.58091 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c84f7006-4c56-31d7-a182-129f7d89a042 | -2.54987 | -54.01204 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83b5228b-020f-3170-9ee3-57a1c4c3f7e3 | -3.70845 | -50.14356 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 567d6ba4-bf7e-33ce-a025-8d2ed8ee0dc5 | -3.94446 | -50.49276 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8418767-53ad-351c-bc84-8a1575f73159 | -2.73194 | -51.92185 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3155a00e-f06b-3464-919c-a8175258c219 | -3.96961 | -48.14003 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f709c6a8-2479-3022-88cb-4771d4ecbc1a | -2.83894 | -51.3497 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b84f9388-254c-3b30-91bd-437848abfbdd | -2.79592 | -51.48156 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63583979-2c04-3b5e-85a2-d887cc735f31 | -2.84454 | -48.44862 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed5dd974-2260-30db-b8d2-32d1a03d68e9 | -3.1414 | -51.19909 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65d7f3eb-76b6-3698-af3c-d25f9a76367f | -4.17737 | -46.58825 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 33eeb88e-11c8-37bf-9c0e-13adb914888d | 0.45688 | -50.27266 | 2024-11-06 04:36:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efe02385-fdd2-3ba5-a255-f1a5b625586a | -3.21703 | -53.06545 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4acbf647-f159-3fdc-902d-a123d7b3c9b3 | -3.09255 | -50.27098 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e87403a-6760-3259-9a69-b3552f2306b4 | -3.02382 | -51.00752 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d64c6fc8-81dd-300c-9e4b-83d3b78a7db1 | -2.88862 | -49.11706 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92c466b2-89ed-3b87-ac07-99fd58356c9d | -4.36515 | -45.76365 | 2024-11-06 04:36:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd928268-b54d-3c19-8379-9bddaa1e47c5 | -2.28198 | -50.6664 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02449cbc-39be-3ad6-987e-135b5da61893 | -4.02769 | -45.6666 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f60efda-c28b-3534-bf37-c470b4d13f64 | -2.93981 | -51.05443 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b5dc57c2-c818-3f34-8cef-baede71d21ab | -3.09428 | -50.26016 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12846f8a-7a7a-3960-ba9c-e16d3f870cfa | -4.13238 | -43.58723 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8fc75fe4-b5df-3ed6-9073-336da207f027 | -3.23393 | -50.54659 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24641339-cf19-34d0-8af0-6d36cd7d22ee | -2.84104 | -49.33257 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbc10fc9-4a6a-3ae5-b9a3-b3bd9e773f70 | -4.16118 | -46.57788 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95eb136b-276a-339d-a6ba-83fd7375319a | -2.44371 | -49.02965 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8de9a02-6f12-3088-ab26-8c0b9e6bdcd3 | -4.30194 | -48.62059 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4aa2864f-a4e9-3684-8658-195b0cdd0b8d | -3.97303 | -48.16168 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31bcd695-25f8-32af-94de-09bda3da621d | -3.16548 | -51.30174 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0afa578f-7f93-39f5-b052-7632a32c468d | -2.81654 | -51.48903 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f7c1d44-68cc-3e35-8b8a-c99558f98cfc | -3.03821 | -53.27452 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 300bca28-ce5e-3303-ac7e-0e3fa43e4d12 | -3.22408 | -53.3934 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88a49635-698e-311a-8354-c445e0d36d48 | -3.01478 | -53.44068 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 30c8434f-5396-36f5-814d-867b26abc9d2 | -2.78638 | -51.60824 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e1f7842-de1a-3ad9-8d85-dfc8283352ef | -4.07511 | -48.31253 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66f10b1a-760e-3f0f-91f4-735adb9d2295 | -2.80526 | -51.49129 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d0674d0b-7686-32db-9da0-6ab4a2af352f | -4.32075 | -48.65173 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6bbe916-4b1f-3bfb-805d-e51cfab2093e | -3.53256 | -49.98942 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5109cf83-5d8e-3056-ac9c-ed2465d5765a | -2.79043 | -48.57401 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b3010f3d-ad4c-3c99-8282-cfaf18fe8b89 | -2.42187 | -50.49318 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 066e9be3-8c4c-36e1-80d6-02a77231e0b9 | -3.66623 | -52.19128 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68bf09f6-0851-3359-8163-2d8fc4ab7ef9 | -2.34458 | -48.90484 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef863680-428a-36e6-bbd4-b4ccdbb90f8d | -4.2178 | -53.55987 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 10d6470e-5661-358d-a475-4ba8885bebea | -3.96481 | -49.94154 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba52e385-c3aa-3f89-9220-3a3604be6e12 | -5.25669 | -46.17607 | 2024-11-06 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c481d8be-77a0-3809-9501-92f08337549b | -2.83039 | -48.66792 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41fff2f0-2d9d-386a-a604-eb3cdc7fba63 | -1.52119 | -52.55175 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33aef4f3-2653-37af-acab-b3b678d8e308 | -2.66135 | -48.57492 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 620d7d06-e60e-3d65-9db6-42e85c5d31ef | -3.70895 | -50.18381 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e1a616a-828c-3a5f-a1d0-4945574edce1 | -2.52691 | -49.14902 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6642f3af-3201-3223-8c42-64511d6b62eb | -3.90956 | -46.45424 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c12d65f9-383c-3149-94ea-ca89a315ca1d | -2.69892 | -49.30702 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa1c8ef9-79f5-3175-a767-292333139979 | -5.55004 | -43.69894 | 2024-11-06 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb00d51f-a70c-3778-a726-6e30e92cd306 | -3.5424 | -47.3782 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 31c0ceb3-895a-37ca-911f-fa21b0a060e2 | -2.05549 | -52.66994 | 2024-11-06 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd7e1180-0c9a-3d49-b761-aa1be2bdfdd5 | -2.82221 | -52.94402 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a04b23e8-9655-3771-aa43-f6639ae0108f | -3.52535 | -50.34988 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8f708e3-7c23-341f-a2fe-1df1d3099be6 | -3.09716 | -50.24219 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35ddd6ba-96ef-3cc0-8f81-500a0bef0796 | -3.53326 | -50.34372 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2856b745-7981-3ebd-b5f4-c9085e18dfaa | -2.78031 | -52.87121 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6db6bb33-3e63-3b24-8f6c-82910499b8dc | -3.06147 | -50.50814 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c0564a0-7037-356b-98e3-4dd3ffefd73b | -2.8168 | -52.90437 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c274645a-490e-3fbd-8ea9-797c05c01d09 | -2.28766 | -50.67499 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3841812-c7e5-3a9f-a0f0-62b06ff876ea | -2.97303 | -51.02437 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b50d7b40-ffa9-337c-a637-4e8c47a07365 | -4.55711 | -48.00877 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4baeda5e-3a12-32fe-b5ae-4be47d3faca2 | -2.647 | -48.55863 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a9b306a-d7ee-388f-a9e5-56a012c6983e | -2.79752 | -51.49417 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6c4f1c69-4c97-35ec-9420-1a8a21f50f0d | -2.78337 | -52.87671 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3a0f5a7-6f53-3037-bc73-b08eb30a68a9 | -4.12405 | -46.90929 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14ba4c80-51eb-3b4e-8917-c5f8e2c0fb35 | -3.08848 | -51.12743 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba12de98-5306-3ffe-b96c-bd6f0c5109db | -2.79462 | -51.48958 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7df6dad0-7ebd-3330-92d1-0c66b615c1f5 | -2.71833 | -48.73148 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e354704-44b3-3d7a-b1fa-c994693173d5 | -3.66013 | -50.23095 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3937e978-99fb-3106-9b19-aa346057ce75 | -4.34638 | -48.62082 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b96d4493-6fdc-320c-97d9-498fd21bde69 | -2.27941 | -46.82779 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33f2d102-a6c9-30c8-9d6f-8bdc39e9474a | -4.42682 | -50.08969 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3f8c0dc-84cb-39e7-89f4-8e7d1d435568 | -3.52461 | -51.32036 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3448d32d-7046-3c81-b880-a7d704e56378 | -2.89507 | -48.60064 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91922240-cccb-3879-b599-6a36e4c73675 | -3.09114 | -54.55001 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 585bca33-b89b-3826-92d3-9038a065ef00 | 1.35293 | -50.87743 | 2024-11-06 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6209848f-9d37-3845-ae96-2c6259a50cfa | -3.92365 | -46.4085 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd4fd9d9-2cfa-394b-882f-c2136e90b747 | -2.60744 | -51.30251 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 707e225b-1a6e-3899-aaf5-513ed173f12f | -3.80378 | -52.36083 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7305adf-4a76-3603-acb1-5a6ba7d0bebd | -2.5853 | -54.00245 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0bb9a93-d2f0-33cb-a266-7fa8c3dfe5f5 | -2.91839 | -49.1217 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e6e3022-fec3-3eff-b2ee-f7031d7e6448 | -3.35034 | -50.30037 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 458c1592-866e-36f2-aa32-119419a2c22d | -2.80746 | -46.60918 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2c8ff9f-3076-35e7-a0d5-0196a894c460 | -3.3181 | -40.03603 | 2024-11-06 04:36:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b3bbcfa0-480f-3b21-b7a8-3d0164b5f034 | -2.94688 | -54.13265 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bcb9003-b8d3-3afc-b697-cf3455a07b3c | -2.824 | -48.55796 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a7ee64f-a3ed-3363-ab16-06f5f1e11291 | -2.47564 | -49.02051 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af306c08-0d83-362c-a4d0-7ca5b8dcced8 | -3.09593 | -50.27152 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7793dd8a-1a87-3521-8ad7-0f04977b2b60 | -2.78703 | -51.60419 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b5607c1-d4a7-3251-a3f8-f60635669121 | -3.07998 | -54.5119 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0dd88ef-7d24-36b6-8a05-8d7096753420 | -3.08186 | -47.57961 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README39.md)
