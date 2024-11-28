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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07791996-181a-3638-9913-ee867b97977f | -4.06534 | -46.82423 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31002d12-7389-3149-bd70-cc58ce724045 | -3.38433 | -50.10125 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f702349-cfcf-3a03-addc-5aafff667fee | -3.28495 | -54.74569 | 2024-11-28 04:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a3cdf07-88f5-30e1-9753-4f42230c3067 | -4.30958 | -48.08286 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b530c91d-cbfa-3439-b9b1-17e1e4579f69 | -2.81395 | -46.83653 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e0af619-690f-3294-8b95-298d05a1e07b | -3.03777 | -48.51314 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c483a52-5d81-3947-8a45-2299ca0522c8 | -3.70432 | -47.12949 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6f6cd35-dbd5-3e57-ac97-fe09d311689b | -3.69831 | -50.22297 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6b85c3e-dce5-30e1-9adc-344b113ce1d3 | -3.78138 | -50.13105 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bd577cf-f6bc-3801-8ffb-4fb3644cd9fa | -3.39022 | -50.11545 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4263f55d-4984-3e16-ab91-e8ce76ba7115 | -1.6009 | -55.38291 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e27e96de-95ff-3ed3-bc41-e9739b4bdd6f | -3.98384 | -46.65231 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50ad810f-cec9-366f-9ba6-be55717adac9 | -3.33626 | -46.42851 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe1998ef-ad5c-3372-b17d-05ddaccefd6b | -3.54273 | -50.19062 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4842070b-e661-3f93-82b1-71fe62624d20 | -3.7044 | -51.80449 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57f6a44c-b8d9-30b8-94b8-94de3d8f454a | -4.76442 | -44.80095 | 2024-11-28 04:25:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 54b694ea-e1de-36b9-b4c2-2cebd1434824 | -3.0596 | -51.05851 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cbe809c1-1acf-3969-93bf-6b0e4b0b8c90 | -4.83784 | -44.28707 | 2024-11-28 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f3810f4-c90c-3f62-9e15-d0337bbc3867 | -5.19165 | -44.24746 | 2024-11-28 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83d01b5f-dedc-31d1-9e4b-9dd58f32c8bb | -15.89181 | -45.99809 | 2024-11-28 04:25:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7fbaf87-f2e0-32f7-8f35-b7de50165e0d | -2.8058 | -53.02217 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6248e752-d14a-3224-beeb-5a7f9d75c6c7 | -3.10182 | -53.26112 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3ec914f-0bd6-3cd1-9060-d9f8274cb9bb | -4.64262 | -45.66365 | 2024-11-28 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b289ed0-f2e5-3521-813a-33070b1b87e1 | -3.85439 | -46.50621 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad0904b2-e7d9-3c84-8582-8a1e9efe2527 | -3.93156 | -48.16 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebe5cbb2-e5ce-331c-a1fe-9b79a2d469fe | -3.95489 | -49.3485 | 2024-11-28 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aab17784-4e35-383c-8abf-b4df2f11e1bd | -3.38238 | -50.1142 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 94a7ec71-f456-3d9e-83ed-b16bdfeba6fc | -3.7389 | -51.84038 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a689279-2106-35fb-82fd-55726f2043c1 | -2.87219 | -46.87115 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 778b1abb-be5b-3c27-bc56-b96d848db3f1 | -2.86881 | -46.87062 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70085ec3-0e1e-3817-95ab-5fef711e43aa | -3.66904 | -45.78588 | 2024-11-28 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 706b1833-95bc-3823-978d-b3f89a5d1183 | -3.68133 | -50.88039 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c9876d1-5ef5-3bc5-a5d7-7e7275f555a4 | -2.00198 | -51.17265 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a6f79da-f92f-3b52-841d-587ec79639b1 | -3.2413 | -53.64069 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 839d932d-07a6-369f-b6df-f825b582a7a4 | -4.04802 | -46.84682 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2314043-885e-33ca-9174-23a007392192 | -4.09311 | -44.8583 | 2024-11-28 04:25:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b661943-574a-350c-9cc5-25c5b7891bcb | -4.31926 | -49.39333 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94271e31-c258-3c5a-9e53-a1d74214ce81 | -3.41537 | -50.15726 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 673e1c43-c3dc-38c6-bcc7-9f8ef0bef4d3 | -1.61648 | -53.87429 | 2024-11-28 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 297fad42-3c25-3f03-8ce6-382f80fe14e3 | -2.58067 | -53.66354 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2653602d-a45d-324a-bc10-efca94bc830d | -3.11838 | -53.75999 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19d1e0bf-21ec-37ab-addc-b7e63c082f3a | -4.77161 | -44.42423 | 2024-11-28 04:25:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ffd5ecf0-87c5-38f6-bea0-87bb71f8039c | -4.03212 | -46.54147 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6ac567a-83a6-3203-95bc-39ec048eabc7 | -4.20374 | -46.55096 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7727e86-658d-3a75-a214-cc72f6c286a6 | -2.52805 | -50.1108 | 2024-11-28 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22c105f4-5569-3513-bb89-f781a9458900 | -3.76612 | -46.67556 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ed3d59c-7c45-3ada-b14c-4152b3c54353 | -3.14297 | -51.29184 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5014ab1a-7977-3e47-adb1-5fd035cc1808 | -2.72621 | -51.74537 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fd90e4b-3d46-34f8-bf62-956b4fb6b971 | -3.59093 | -50.361 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f7ceb2b-16dd-3241-8e56-614d60393381 | -2.9214 | -49.1651 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a879250-a258-36f4-ae12-ab83f6f7461f | -3.78506 | -46.68564 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03a4f717-82e0-3cc7-b82b-e08fcdbd048f | -3.32539 | -50.21813 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44b6d9b5-80cf-376d-8727-88de20163fc6 | -3.52848 | -52.159 | 2024-11-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddceed86-af73-348f-829f-488eab5644a5 | -3.58697 | -50.36032 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9b9f9f3-bf7a-372a-adeb-9da8e5d8744b | -4.61845 | -45.494 | 2024-11-28 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b47f8b93-a3e2-3273-9f91-f90f2cf50e00 | -3.18534 | -48.431 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54860119-7550-339c-87d1-a55c03896356 | -3.3228 | -50.25933 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa003bb8-207d-3e6f-ae52-a0e2f721dacd | -4.30722 | -48.20916 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f64c020-72ca-3409-ab45-2763415009b3 | -3.11317 | -53.76495 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85022e57-ca25-3882-9639-88be3896f534 | -3.51126 | -50.30968 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ab77cc5-b3a1-354e-a22e-cbb077634490 | -4.53405 | -44.62136 | 2024-11-28 04:25:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39addc34-339e-3198-ad9b-3539956995f0 | -3.8289 | -46.53798 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67be3f09-2772-38db-8826-aa6a93346e63 | -3.5105 | -54.53259 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3513dc81-dbde-366d-87f6-0a23bea251d7 | -3.39627 | -54.27977 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5112f175-6086-31c1-b8de-5a1a1ea2053a | -3.68893 | -51.56104 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dc57479-24c9-35c2-a642-acda37e0c310 | -3.24122 | -50.76506 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f9bd38d-1f62-3574-8f9a-abb7b534f777 | -4.20361 | -45.30194 | 2024-11-28 04:25:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc4ef0dc-2327-3663-860a-2fcbd7cbfa51 | -4.76119 | -46.37893 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 046f8397-f39a-3e03-bbe6-994a947dedcb | -3.32775 | -50.05435 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39adce69-5aba-3b71-b2f3-30d294ca3eaf | -3.09942 | -53.2621 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9cd1ccb-5bfb-3db0-a286-5403238efab7 | -3.3863 | -50.11482 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 146fa31c-4059-3b31-b765-9f381f32364c | -4.05179 | -48.33451 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cf3c191-b046-3a7b-8b8e-1f43c5964496 | -2.87779 | -46.87938 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c43ec2dc-de5c-3dd8-bdb5-65cd8bc7f124 | -3.86688 | -46.34042 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1cf25fd1-130b-36e0-a03d-97d9d4a01738 | -4.76174 | -46.37547 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6445cabf-2cbb-3307-976c-acbb57650c98 | -3.68182 | -49.56981 | 2024-11-28 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0db80584-54ba-3803-9ce7-5fd00e1b2199 | -3.05897 | -51.06234 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7ff0be32-c91f-3a3d-b95c-deaaf927820d | -4.5346 | -44.61782 | 2024-11-28 04:25:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0210c446-e638-3703-bfbc-9a7529e3c3ce | -8.60099 | -49.85909 | 2024-11-28 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a923a98b-b774-302f-961f-690b26871cc7 | -3.10345 | -53.82513 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c104ca5a-a02e-3a6f-8ead-462531b91248 | -1.78305 | -52.73608 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71a15d2b-fbfd-3b97-a77b-b806753a4afd | -2.86099 | -46.85464 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fbedcf0-0e98-33eb-bc9f-e84ea472e874 | -2.82288 | -54.0321 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 135ff491-bf9f-3300-8c5d-76a7b918cd9a | -3.07388 | -49.20161 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91a32f44-d21f-3a38-83bf-8a0cdd4348ee | -3.79577 | -49.94364 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 497669cc-58a6-3eca-8efb-471b70be7cd7 | -4.1809 | -48.63274 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04caf95e-def4-3b95-b22f-2753264aab37 | -5.30678 | -43.08262 | 2024-11-28 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e5513e0-37df-3c98-b6d5-149b55b2dc73 | -3.22604 | -45.64231 | 2024-11-28 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75a8b3c5-2558-393a-9e80-283a695c8852 | -4.04745 | -46.85038 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e641d14-b6e4-3366-8fee-6b69824a19f9 | -4.35018 | -48.68763 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a9ea08a-320d-372f-bd4f-a5025aaae818 | -3.94939 | -46.50708 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdb18cc2-8d23-3499-8ecb-cf5af88b9b12 | -3.32852 | -50.22384 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 091c911b-debf-3a97-9d04-0867cf8127ff | -2.69545 | -51.98923 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d32e5e8d-ec34-3017-bfd2-9f9c6acf51a0 | -3.1929 | -50.82886 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b13e982d-2805-37c8-bbc6-1c562fa905e7 | -3.13086 | -51.04267 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1b4cdbb-443e-3708-bc00-6ebe528b81ea | -3.04703 | -54.04322 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f31aadd-5ee9-3262-b991-6908fa4ba5dc | -3.97772 | -46.64778 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 973aa23f-8d16-3836-befd-da43414462b0 | -4.54536 | -46.58318 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a623933c-c640-3eef-80d0-be64ff90846a | -3.50085 | -50.32365 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08b5fbd2-8b82-33e7-a975-5e997e150aed | -3.46943 | -50.54108 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README56.md)
