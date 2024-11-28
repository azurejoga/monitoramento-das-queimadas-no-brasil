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
| 1402d0bb-8e22-30a1-8a24-e27d185cf87e | -2.89545 | -51.37373 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51939dc4-0481-3327-b3b2-1e32eff0de0c | -2.05503 | -51.18785 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e379fc7e-e767-3418-a5e0-c3788fee525a | -4.12256 | -48.82201 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cae7ae97-a9f5-338a-9ecf-b0ffb41aebfa | -3.95044 | -46.69028 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3c816b2-ae4a-3b94-ac69-3e67a4e11494 | -4.52032 | -45.72912 | 2024-11-28 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 70a7d29b-d0ae-3b6b-8dc5-c1afe076827e | -3.67126 | -45.79328 | 2024-11-28 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c30f2de-d8fd-3767-a548-ec8c0be4471b | -2.24296 | -53.46559 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe24b993-3e1b-3946-910f-05148f3cc06b | -3.3626 | -50.18793 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cebb8f2-9cb9-31d2-8bd6-062ad181b9ce | -3.29257 | -45.52253 | 2024-11-28 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 30.6 |
| ed4e36d1-5153-34cf-8aeb-1e0f62cb3347 | -3.32369 | -53.70062 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 493f3ec1-5eb2-3a18-80fc-ff6d6ea3b063 | -4.18198 | -44.26833 | 2024-11-28 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dedf79ad-fde7-38d2-8b2a-34b6880305b5 | -3.70643 | -43.42764 | 2024-11-28 04:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7cd2aaa7-1203-38a9-93fc-d1cd8877b06d | -1.66022 | -55.23507 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc906d70-d4bd-3c8b-864b-5dbba51b6d6d | -3.28775 | -50.27484 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2427bec7-9a44-3a46-bed4-809399217885 | -3.56722 | -46.34361 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1520d8b7-2119-37df-8360-d9423b4d378a | -2.84183 | -46.86641 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7512038b-bda4-3fb8-a662-39a9df82e855 | -2.85875 | -46.84697 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 435a8164-d73c-3df5-be79-3d7b8a7fa6dc | -3.08237 | -50.25373 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5aecd75b-fe7d-3f35-bcc2-9619e7162c8b | -9.62345 | -51.49684 | 2024-11-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f32e6666-fb92-32e1-bfe8-9477dd0fa5b8 | -3.69896 | -43.43031 | 2024-11-28 04:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7f373c4-d6cd-3764-b962-36da298798ef | -2.87446 | -46.8568 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4daf49ad-ad32-336e-b302-8ede48b269c3 | -2.80137 | -53.04849 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4def719d-ce9d-3281-a875-979e229ef0d3 | -3.08365 | -49.21232 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 68da0e49-048b-34aa-a241-0839eefa29b3 | -2.91196 | -51.71312 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6b830719-e96a-3291-af69-cc727b28bf54 | -3.10825 | -53.26913 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30aba2ad-dfa1-3acf-bf7d-a0060124e5ad | -3.49744 | -50.49558 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4c0d52d-c4c6-3fc7-b511-225f5829e9dd | -3.0969 | -50.36636 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b42d3e00-3d4f-38bb-acc0-ed50ca7fef38 | -3.26401 | -46.4358 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f89521db-8faf-3f2f-bfa5-513dc6491cc0 | -2.86829 | -46.85213 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f97dd223-c8b6-3605-b093-d1d067385bff | -3.13204 | -51.04261 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 421d3598-9a7f-39df-a97e-4b6835fb19c6 | -3.24062 | -50.76874 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3fc966c-054a-33a3-bba6-f355a5435d04 | -3.26191 | -44.93932 | 2024-11-28 04:25:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 893a2b5c-e3be-3d51-8b9f-b4ff8e42a48a | -2.36519 | -50.43288 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fead1cb6-7413-32ed-9bc4-4d872fa11efb | -2.5991 | -54.21577 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83061dc5-5b31-3e8f-a465-33bc28c60f63 | -3.81515 | -47.46827 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 478fb002-9723-37d1-bef2-32020251ce5f | -4.38679 | -47.77685 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ae593d8-0e37-3b80-bad8-ac0159651087 | -3.14721 | -51.29257 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca4073c6-8748-33b8-8c33-ca439c587a79 | -3.69753 | -50.22791 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad509fd4-f615-3688-a705-cdb9619d7181 | -4.05375 | -50.86983 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efe3b827-4f81-3b58-ab48-cd5dc97f63e5 | -3.09455 | -53.26132 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37e44e36-5221-3097-af0e-b6dc12d80f43 | -2.7536 | -54.12934 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f5800779-f001-3d34-9a6d-2d274fa994ce | -2.87052 | -46.85987 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b5f76990-57cb-3506-8e4a-608425b0e7bb | -3.80287 | -46.68122 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90e25e84-a35b-3b89-a722-32e7f3af7f03 | -3.07756 | -50.25823 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84a90041-1cc3-33fb-98f2-07814285f303 | -4.14235 | -48.22321 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64684fc5-83cf-3fae-9489-3e790f727908 | -3.83278 | -46.53501 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a5f9433-344f-3124-a239-4503f572a35c | -2.92147 | -48.33352 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a9aafa4-ba35-3700-a42a-86511dc2e4b7 | -4.04858 | -46.84329 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e0c6bd5-9613-316c-8a94-2bb8b303d39c | -4.20415 | -45.29848 | 2024-11-28 04:25:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a24ef316-fd13-3572-bc51-4adec1d0544a | -2.93186 | -49.4361 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4121d210-6d81-3c8d-b53d-16bdd3e5162a | -3.78449 | -50.13663 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da14c1f6-3fa3-36c0-bc71-f72fcf3fc98e | -3.11412 | -53.75909 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 796d6f0e-8f52-3707-9a5b-b2190a2b7b2e | -4.0147 | -46.99097 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2669b9d3-e888-3216-a911-b2f742dfba6f | -3.60634 | -51.16037 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aef29c74-36ac-3b54-9777-569823e805d8 | -2.84355 | -46.85563 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c336318-3f7f-3b6b-8b18-23232efc1f9e | -1.86754 | -53.94999 | 2024-11-28 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ae688a52-b2bf-3707-98ae-2b769d1cbeb8 | -3.91448 | -46.53381 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efb5e62b-10a3-31e1-90a5-948de639a5a9 | -3.31505 | -53.75352 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ea9a39d-06aa-32be-845a-a411aeaeef92 | -3.27152 | -50.62896 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5e41e1b-edb6-3fa3-a929-a1f5ccc6bd53 | -4.10728 | -50.97902 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 795b9bd3-a3dc-3721-b2ca-00b19d9c1583 | -3.29365 | -45.51565 | 2024-11-28 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c29b354d-14b8-3b70-8c32-0e8562eb64f2 | -3.12143 | -53.10179 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4f1a0f3-e919-3725-a8d1-b77382291114 | -5.40126 | -43.60581 | 2024-11-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3534ec5c-6fbf-3de2-858a-39a569c2d228 | -4.1326 | -46.11985 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a91b160-908d-3d87-937f-8ad45c535a72 | -3.36899 | -50.82701 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3256db69-befd-3f07-86fa-ddfe89c4fc40 | -3.17823 | -50.28064 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3efd3440-2234-3338-89b0-2b900be97bfc | -4.04967 | -46.85801 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d019b8d-1ddb-3498-aedc-5a6d07794e3f | -4.05474 | -46.82617 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b98ba070-7d3c-3b12-bd10-7a0b0adfbf6b | -2.84578 | -46.86335 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c48d711-e526-390b-8a36-c3c40f77f02a | -4.08743 | -46.1482 | 2024-11-28 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a7385b1a-e73e-31e5-917c-46da24fb4cff | -2.43878 | -50.41539 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b305968-b0ec-3840-bf9b-3ddd4b6cd329 | -3.57697 | -50.33084 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b47e0c4b-1acf-3f3d-a14b-03098c9bb62b | -5.21592 | -41.2856 | 2024-11-28 04:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3c5ccba9-afe9-3195-b68a-ad111e1f363e | -2.98044 | -53.88809 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c7f8e38-0356-3415-b0a9-3a12fff33f36 | -3.79228 | -50.13795 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27ccc7e3-ffc4-3690-aa96-25c85843c68b | -3.36609 | -50.76631 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eed43325-166f-3ab3-a814-bf88bd626ca5 | -3.193 | -46.56466 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f9a7479-c9db-37f7-b26a-35c2e8da1557 | -4.87038 | -47.7562 | 2024-11-28 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d2a3781-63d7-3ebd-8cfc-6a06d795c629 | -2.01659 | -51.19168 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e6bb020a-1a03-32ff-8693-b9de7632fe79 | -2.87174 | -46.80868 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63a89a7c-cacf-37dc-be80-ef1de8bb2970 | -1.71291 | -53.2543 | 2024-11-28 04:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 683b33a3-447f-3fe0-8f00-3686e36b6360 | -4.6575 | -46.92823 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9371dab-8003-329d-83cc-82f38932c4a1 | -3.70517 | -53.7542 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c586fd1d-a7dc-3cb2-8c3e-632269e709c5 | -2.85532 | -46.86853 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0d918b6-dea8-3798-882e-667789410b09 | -3.94053 | -47.98402 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 146d0929-7d17-32ac-8b20-d69ddebb8ef5 | -2.6514 | -49.51555 | 2024-11-28 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3696afd3-0520-338f-aa19-0a5bc79a723e | -3.10639 | -53.10888 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1325492e-b32b-334a-ae72-c8a257952632 | -3.83223 | -46.53849 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 316d3d8d-c11e-38fb-91d4-0092bb08a809 | -5.30267 | -44.4353 | 2024-11-28 04:25:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a742335e-131d-36f4-9609-993ce2a6b587 | -3.78172 | -46.68512 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 327941d2-57e7-39a4-9276-26fa7d2f4df1 | -4.2986 | -48.19586 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66db4a6a-a71e-3632-88f8-80530501810d | -2.5793 | -51.92614 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2446dd7-eece-3010-bf45-45e75e3c1a27 | -4.45082 | -45.89104 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c2b1c6d-4ebb-3dc7-be0c-75601ed60474 | -3.81458 | -47.47194 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3322397e-bbf6-3765-acf7-a2a6233f5d44 | -4.10964 | -50.75763 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38be9887-333e-36f8-bf61-557e4bf4c66c | -4.57067 | -45.40876 | 2024-11-28 04:25:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 402ff9b1-c9bd-3cc9-a234-b0c0a0d3f92b | -3.58015 | -50.33646 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9d18f3c-f53c-3222-b194-c4e94c3119d6 | -2.57894 | -48.07728 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b316264-ed7c-3891-85fa-c97697a288b9 | -2.82939 | -54.12261 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 310166ac-c711-3936-b72a-a776dfd1af4a | -4.11417 | -48.48621 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README65.md)
