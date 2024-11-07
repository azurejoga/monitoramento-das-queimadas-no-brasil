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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53381dea-5cb7-358d-a465-e2440a3b58e5 | -2.81774 | -52.92544 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a275e167-c784-372f-a7ef-a542b3550d78 | -4.39245 | -49.77015 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46f470ff-d503-3537-aa42-69de5f7160b6 | -3.6079 | -52.52278 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09a5e5db-94c1-3b80-8734-8ba4fbf2bad5 | -3.19659 | -53.40176 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3f4511b-a850-3f02-9200-42cd1924f7a7 | -5.0366 | -46.84832 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19d08e1b-2528-3034-ad52-ee14319d5576 | -7.90568 | -46.69417 | 2024-11-07 04:18:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f36b8a17-166b-3a05-8ba3-5d44be34e402 | -7.38457 | -42.93246 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 827c6ec9-eb81-3b6a-92ef-826870d841e1 | -3.05899 | -52.50181 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a31e6fc6-ce08-3d36-8473-57d6bd953c72 | -2.82361 | -52.92286 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac2567ba-5826-355e-804a-921dcc47f07c | -2.3126 | -48.143 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6ae8b5e-5edd-3b1d-91cd-4a5dd15acc83 | -2.83692 | -52.90807 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f643c84-fa66-3fae-8ec4-dce3e99e4e73 | -1.14886 | -53.74689 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7588ba50-0f82-3a23-886f-9d8cc2cd5a13 | -3.5127 | -50.47052 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 670e2674-7e15-39db-845f-4cfc6df28ec6 | -5.97249 | -44.00668 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61eb5938-25a0-30ce-9bef-509aff7f828e | -2.6585 | -49.87207 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 98f243a4-90c7-3ac3-a583-7718e34574c5 | -3.62034 | -50.19442 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f150bd32-b181-3648-9e9c-f11042f8e006 | -2.66146 | -49.88094 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5fdb5c0c-1cce-32f4-9512-fe10d405f718 | -2.67599 | -51.82731 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 028737cc-ac4d-3438-aca4-1efee3e68c5d | -2.89424 | -49.40538 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d002835f-9333-3f53-8634-4de33deb3d6d | -4.54327 | -45.69859 | 2024-11-07 04:18:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 202c7a63-e820-3f61-abcd-632cfee9150d | -5.82657 | -47.34422 | 2024-11-07 04:18:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6f9d8af6-c8a3-3a95-993c-d25cd0fcfd18 | -5.50182 | -43.3454 | 2024-11-07 04:18:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b04b8700-794d-3fd1-9f8a-d79cf9b52ae6 | -2.97621 | -50.30161 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6be6b54-5b3e-3ba6-a0e7-02df59ae305b | -1.33341 | -54.61227 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c1719c4e-2115-3f68-95ee-34bca2b0da20 | -4.07467 | -48.31853 | 2024-11-07 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33758aa1-a0cf-3043-b715-5369283e371b | -4.67009 | -46.33231 | 2024-11-07 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd91308a-8931-3039-9883-ce84f645131f | -5.04766 | -46.84624 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ad60374-7747-34cb-be21-f20e5c774087 | -7.37772 | -42.93143 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7d226f62-036f-339c-bcb1-90fb1b322038 | -2.92746 | -49.34521 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca2c5a6f-6339-3d0d-8838-c290ae5f12bb | -3.21752 | -53.1104 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db73d591-eae8-30b3-98fd-fb7f9447f3b0 | -2.22392 | -46.8638 | 2024-11-07 04:18:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0cc84b70-603c-3ede-a836-d6007ed617da | -3.00371 | -51.44638 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 685c2f64-6d7c-3bf2-a39b-2624a3057ffe | -3.15855 | -50.20618 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb16ad83-3698-3d7c-8d5d-f0ee28fbecba | -3.24945 | -46.4694 | 2024-11-07 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31dd2aa6-8996-3f1a-bb8c-82c7e23f0da9 | -3.45619 | -50.37218 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 078ff307-aeee-315a-a2a6-546ea9e4b53b | -8.31233 | -43.62499 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c83acb1b-fad1-30ea-9cfd-0b4ca6c5a9dc | -8.11668 | -44.41339 | 2024-11-07 04:18:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e4b0054-184f-3efa-8729-c1e865a39c99 | -5.30166 | -50.56268 | 2024-11-07 04:18:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c62ae89-6e7e-305a-bf6e-03f236af0dd1 | -1.1461 | -53.71881 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 488296a2-d431-3161-91bf-3bdae5f7c755 | -4.9964 | -46.89788 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e30293cb-0939-3ed2-9e7e-b4056d1299dc | -3.2931 | -53.11652 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85ce9b9a-7c23-35dc-932c-7433b9e075b3 | -3.03597 | -53.27383 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb3d8a68-bed1-35e3-ba5c-1ba911e04b07 | -2.88108 | -48.28712 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d57b9628-c47a-3500-943f-26cc459ff103 | -2.45463 | -45.84254 | 2024-11-07 04:18:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cccae3bb-54c8-3fac-8cc3-c73903e3f97a | -2.97759 | -50.29301 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1edb9175-a918-38fb-864f-d7af81ba1540 | -2.7197 | -54.15593 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d51a3ef3-c929-3f61-8002-1533ae0a71d0 | -5.08093 | -46.04184 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7799bbbc-a8ed-38bc-9f1c-fabd7a97423d | -2.91946 | -49.60157 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df88625d-f62a-3cbf-a770-5f996edd5b04 | -2.64238 | -46.77932 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1de6fd92-dde1-35f9-8acf-b452f9ede1b4 | -7.10903 | -41.57129 | 2024-11-07 04:18:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| df443723-b899-39fc-ba32-df63b1d68843 | -5.02738 | -46.83889 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c73941c3-abf0-3f3b-a5b5-e587c9d50bf5 | -8.49646 | -42.11151 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dbed1623-e5ed-3f2c-b9f4-5e0661d5487c | -3.04253 | -49.53764 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b5e2ffa-f59d-3ead-b70b-cd897b333126 | -3.819 | -46.46103 | 2024-11-07 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8ba493c-16df-30bd-852d-7a0815b40504 | -1.52316 | -52.15546 | 2024-11-07 04:18:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84337ef3-9842-3d56-8f23-76605a008faa | -4.21054 | -49.76548 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 982d563d-2c5a-30d5-93dd-06b68d7f6439 | -5.03025 | -46.8433 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a3708a9e-aa65-3d06-bc2f-40a32b4036f9 | -5.27232 | -45.51862 | 2024-11-07 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae1baa60-d01e-38e6-ae5b-cf7a90307e37 | -3.01601 | -53.43568 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c3d8170-d136-3ae5-9f9f-52fb829b919d | -2.97058 | -53.87169 | 2024-11-07 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 329393aa-c66f-3ac3-933e-0b2e31232e53 | -1.38885 | -52.20999 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 907bcb1c-b785-3399-8acf-0cf107682c7c | -4.42078 | -47.25565 | 2024-11-07 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ace34dc-9acb-31fa-81d5-194d5b0cb91d | -4.51575 | -42.86635 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56d9f6d2-078f-3bfd-9afa-ee39116793e3 | -2.6628 | -49.87278 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bc6421fa-352b-3def-8c9c-fc1a46995b3b | -7.67264 | -42.76225 | 2024-11-07 04:18:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 4e055f68-25ba-3be4-844c-548aa563612e | -3.24653 | -50.02001 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b836dce-fdfa-3637-8758-d71302440d2c | -6.17509 | -44.85913 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a345c13-60cb-3d26-8a76-59d7a644d239 | -4.48514 | -48.11045 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a891591d-61d8-3141-b8a1-6c1ce10eed3c | -1.15009 | -53.73944 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 460f46f5-bc65-311c-838b-0213a37bd487 | -2.61056 | -51.30195 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9482317-5094-3a3c-babe-47e0c8138612 | -2.83581 | -48.46277 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fd79c93-e52f-3912-ad9b-29ae498a7c77 | -2.88383 | -48.28497 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 278dd132-16e8-3aeb-ab54-279ef38e959b | -2.70636 | -46.67408 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c5a6dab-69fb-3006-ae86-f4df3131f58b | -6.69329 | -43.05576 | 2024-11-07 04:18:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c27e81ef-7b88-3744-b008-36116095142d | -4.71387 | -47.23267 | 2024-11-07 04:18:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c7ee956-b5fe-32b9-b536-33a0b1dbec1e | -3.11855 | -53.12345 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4cce100-02fd-3c34-afb3-d5e026573d46 | -2.42806 | -53.6642 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1aa36e04-6d2e-338d-8f29-eb983c0758ab | -5.37521 | -46.26427 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d98f928-b5b0-3d50-a398-10732362826e | -3.03318 | -53.26965 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a77381e6-49a8-350b-a9ac-9d2b6e3ab574 | -1.32066 | -54.64579 | 2024-11-07 04:18:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8dcb6f42-578a-3351-b598-047b1a139f04 | -2.45747 | -45.84681 | 2024-11-07 04:18:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0650ad9-2bd1-37ec-902b-84ee27be6941 | -4.99522 | -49.89387 | 2024-11-07 04:18:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8792c169-c70c-3501-95fb-bf2986a67069 | -3.45477 | -50.38085 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fe492f71-20c1-360d-9a59-8a1dbdf8a755 | -3.2227 | -50.44786 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4cf4b7f-9dd1-3209-9b6a-aa1563c75b4f | -2.81116 | -52.96498 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58f169f4-af0d-3cd1-9999-54c20c5e624b | -5.98614 | -45.36613 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d2777ba9-cbb5-3614-91c6-7a61e9e5353f | -2.81408 | -52.91479 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63246c37-1fc3-3e9e-a3ee-7602bdcd7126 | -2.07963 | -52.04929 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd5142b6-b833-3b64-a6df-3dab1decec2d | -4.68639 | -46.38459 | 2024-11-07 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5372d31e-8b65-3467-8885-87f1e7d17f43 | -3.94776 | -49.43528 | 2024-11-07 04:18:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f45a57b-4643-32c1-8fbe-90c83285622c | -3.118 | -53.12675 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c8a74e6-66f9-339f-8104-0c60d6c5f685 | -1.28317 | -54.56982 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d898ff9-b08e-358d-8f86-4a0cf0d0e856 | -2.6671 | -49.87347 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2965516-0fb4-3154-9b6c-b944641cb1f6 | -4.71744 | -47.23319 | 2024-11-07 04:18:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 788f6716-23f1-3315-a498-2cc0a5cda73e | -8.30386 | -43.61253 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6472ed2-6bdb-3a4c-b9c9-355f1a187fb9 | -5.98269 | -45.55929 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 828eacfe-927d-3814-93d9-09bf50efe9c9 | -8.18725 | -42.83778 | 2024-11-07 04:18:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 565d1b8b-019d-3d7e-8451-764262dd2d77 | -4.51465 | -42.87353 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a9b33f1-4bb1-3245-b6dd-b15422b6a364 | -1.35003 | -54.62454 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0a6d1bc-bb39-32f9-9b2b-81563efe1c73 | -1.33251 | -54.61023 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README33.md)
