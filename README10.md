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
| 1af5a071-0257-32ae-8365-02bc29407c2b | -10.8351 | -58.60375 | 2024-10-21 01:05:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 5af07e07-58ce-3d70-a830-f90d99633a82 | -4.50062 | -46.06598 | 2024-10-21 01:05:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9ea0c6e1-8b90-3f86-8930-4dfe0a05510d | -4.61577 | -46.07336 | 2024-10-21 01:05:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2c0a4003-7224-3a79-b4b4-44f1b5de4095 | -4.62703 | -46.07196 | 2024-10-21 01:05:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 28.6 |
| c928904a-41ad-3756-b492-f682f67b4f6e | -5.01751 | -50.84528 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 94649ead-e6a7-3118-894b-4fbfae87f1d2 | -5.00868 | -50.84653 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c0b553d-435e-3017-b93c-79ef5a15e0cb | -4.94696 | -50.46894 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 32f08cd0-6935-37b7-84bb-fba254239cea | -4.43852 | -48.88823 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32495cd9-75cc-3c9a-b9b0-2bd3328ba887 | -4.94573 | -50.46011 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 013c361c-d12b-306d-a54a-4249cdaf3c48 | -4.84233 | -50.84639 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 890366ac-7a13-3e10-a820-579d2305f242 | -4.73025 | -48.31087 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3a4ccd88-efdf-3bd9-b4ea-2d821890c004 | -4.72684 | -48.31739 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ff0da2e2-d7c8-3f2c-84de-e61abafa6aba | -4.72538 | -48.30696 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58bc514f-db6d-3830-ac32-e6be8eec81b8 | -4.67423 | -50.64002 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b7e25d0-6fd6-386b-a7f1-5e607cfeb046 | -4.67301 | -50.63121 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 24fb8c88-d049-3e43-9310-7ceef8a4e7e2 | -4.66541 | -50.64127 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cdfce0a-bc4f-366c-baca-7c107859cfbc | -4.6642 | -50.95559 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 56274cc1-9bb0-3f45-936a-35fe47690a7d | -4.66418 | -50.63246 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0829dd02-4ac2-3197-8840-1e1ebe9c8dfb | -4.66298 | -50.94678 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ccd6d29b-b0b5-3a70-959c-22ab426888c3 | -4.66175 | -50.93798 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8a9bdfdc-2a57-3cff-89b3-0c87d7ca0ff5 | -4.63396 | -50.9483 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3622e1ec-6ccb-3952-9c6f-8604e1e382ac | -4.63273 | -50.9395 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4eedbd59-eb70-3e2e-a4dc-598cf92fff1e | -4.61612 | -50.67523 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e53ac3e4-946b-3f7f-8fb2-a56183ba785e | -4.61489 | -50.66641 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| db3b3bf7-16da-3c3c-a251-89e7764f9d27 | -4.60606 | -50.66766 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f2b8588-dd8b-30cc-bb45-fe6d21dee08a | -4.58711 | -50.67667 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 70ac88f7-19f4-3fa7-a07d-f3c9cd35a84c | -4.57341 | -50.96586 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 66d3bc39-ac0d-3aa2-b6e2-32bc768eb810 | -4.57218 | -50.95706 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 7b6b6343-f30e-3a53-a137-882aeaa1d4c9 | -4.56458 | -50.96711 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 09fb623a-94a4-315c-afd4-b15b60ad57ae | -4.56336 | -50.95831 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d0f01d78-2ffe-3557-bc87-62015f5216d1 | -4.50049 | -46.07244 | 2024-10-21 01:05:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a963c9d8-0cf3-3374-8f73-58bc9701685f | -4.4831 | -50.44844 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 00774946-0cd6-3cb9-a53e-cc308acec965 | -4.45164 | -46.45153 | 2024-10-21 01:05:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 7cce6c92-6974-3303-b7d0-770962c67ccf | -4.44966 | -46.43772 | 2024-10-21 01:05:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a60af696-dcf3-381f-8e63-73b7fe63029e | -4.44068 | -46.45287 | 2024-10-21 01:05:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7130966d-62a4-31c8-8b04-63c991d8e325 | -4.42923 | -48.88963 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 37bfc106-3b9a-3f5e-9392-c76d5f6218e2 | -4.42786 | -48.87983 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 793122b7-d531-30e9-97d1-61898a4a6ea9 | -4.42103 | -50.93681 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 825ede9d-81dd-3b87-a01a-d7bd4a9ba83c | -4.42053 | -50.73948 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5ad12e4e-f753-319a-bcad-55d86751f8e8 | -4.41897 | -49.80016 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9a1e9b22-6c71-3eaf-b79a-12696332da1a | -4.41236 | -50.53656 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0c1d2db4-93c7-36f0-86e5-3383cd165c2b | -4.41112 | -50.52772 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5172e1cd-1860-319e-ab32-4626492a299b | -4.36178 | -48.47932 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3b8bd2ac-8a50-3cd0-9583-158a1a89c3e6 | -4.33707 | -48.71081 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eabb115a-64d6-3d3a-a690-2a4993b155e1 | -4.31251 | -45.81074 | 2024-10-21 01:05:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 843d5128-ca16-3e76-b42b-5f49ac9c3ba5 | -4.29079 | -51.05084 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0dd68e6c-0d41-3bf0-af57-08f74fc2cb49 | -4.27953 | -49.98941 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ac06ea63-2022-37ed-8c25-74342e1a4955 | -4.25442 | -50.9995 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2f0ed0e5-ed1f-3010-b13d-a8e0d54e3991 | -4.25319 | -50.9907 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1f36af32-9c79-363b-8b04-fef8010e8c15 | -4.24559 | -51.00074 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e424f0e-f56e-3109-9041-381d8e36dffc | -4.24537 | -53.66406 | 2024-10-21 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c86487d9-736e-3461-8d27-bcf0779afc63 | -4.24437 | -50.99195 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ed0ccd4-6206-378f-b340-94d75dc75b76 | -4.22047 | -50.09556 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c2a1c516-62df-329f-b481-eaad85576f1d | -4.21325 | -48.55962 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 1b730aec-a82a-361d-a30b-c36b47e70782 | -4.21176 | -48.54936 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 04327fab-87b6-3ac0-916c-76f2bebfe265 | -4.18821 | -48.04605 | 2024-10-21 01:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e556422f-1f45-386b-b31d-63d46d62867f | -4.18358 | -48.59058 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 408c7b02-9cf6-3ef5-9899-aaf3a6f573a7 | -4.17411 | -48.59191 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a7406a75-3cad-3ae4-9fe0-1fe95380faf4 | -4.10427 | -48.24061 | 2024-10-21 01:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d4fc006a-3c57-3dfb-9d4c-0bb51d2ae59f | -4.099 | -46.15641 | 2024-10-21 01:05:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b5721d69-3000-310a-89ed-4436ed2e98b9 | -4.09687 | -46.14185 | 2024-10-21 01:05:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 1aef16b3-c213-330a-8b8d-31189a59755e | -4.06928 | -46.65937 | 2024-10-21 01:05:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fbabab3a-aaf6-3ba5-b84a-7aa64cf15e01 | -4.04664 | -50.96045 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 05c8c3cc-811a-3115-8374-5253218fc1ba | -4.04639 | -51.02324 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f0372b26-9c5f-3eac-a947-1851dad81145 | -4.04542 | -50.95166 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a4ef7e0-7308-36ce-8c87-a32df583ccce | -4.02752 | -51.01694 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7983ec5f-241d-388e-9e1f-e3a1748a1091 | -4.0263 | -51.00815 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 7e8ed412-6a0a-365f-9922-be55ab35cedd | -4.01747 | -51.0094 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5d72a27e-40af-3c6f-a871-6293b1c0ce08 | -3.93558 | -49.97084 | 2024-10-21 01:05:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8fca3799-a26f-3e04-b98d-b6b63533a9c1 | -3.93432 | -49.96179 | 2024-10-21 01:05:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9638ac7d-6659-3936-ae89-fd0be6bd445e | -3.91531 | -48.345 | 2024-10-21 01:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| faa11aa4-914f-3c57-9a4e-ae4ee0dda571 | -3.91378 | -48.33447 | 2024-10-21 01:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 1049c55a-92ae-3816-9ecb-af8a0b502fe4 | -3.91128 | -49.9928 | 2024-10-21 01:05:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b9701e12-d725-3078-8ca9-b97ae1753c15 | -3.90417 | -52.39173 | 2024-10-21 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d05db2b1-d2ce-30d3-a3c6-f4099277ea84 | -3.90234 | -49.99406 | 2024-10-21 01:05:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c6d6d5c2-5bae-38d4-b21d-e093e2cb517d | -3.8999 | -48.33194 | 2024-10-21 01:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b5e95395-9cdc-3244-8807-bcf2e4453ddf | -3.88564 | -51.1927 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6ab3952d-5c7e-325c-9a0c-bb1cf50562a5 | -3.88317 | -49.98757 | 2024-10-21 01:05:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1a988617-3f96-3d57-bbcb-f11a009e812d | -3.87681 | -51.19395 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 1c3c5e94-231c-37d5-9dd0-a056072b63ea | -3.8683 | -52.19975 | 2024-10-21 01:05:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c2d28cf5-636f-3dc9-8345-77bbf98c3194 | -3.86312 | -51.8252 | 2024-10-21 01:05:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c735a06-4c86-3b3b-856a-f3d66b02b9d9 | -3.85251 | -48.98955 | 2024-10-21 01:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 98a1f20b-b0d9-3517-afdd-920fd0d558ba | -3.85046 | -52.1371 | 2024-10-21 01:05:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 79cb0762-ca2c-39c6-875a-29248a661a32 | -3.83695 | -51.90844 | 2024-10-21 01:05:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f4e5cf01-205e-30e6-bfa3-a7c4bed7be9b | -3.83485 | -51.29552 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 39f6d31c-9889-3290-a075-41a28354759f | -3.82627 | -48.87222 | 2024-10-21 01:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1b8611a3-fad6-317b-a94b-d44776345469 | -3.81964 | -50.65471 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ed3478e2-7bd0-3750-82a0-88f8330904c1 | -3.81691 | -48.87358 | 2024-10-21 01:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 471518e8-8c9c-3bdc-b21f-308fb30c4599 | -3.8128 | -51.13713 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 918a21df-2c11-3acc-9c51-cf0789059678 | -3.79652 | -51.81357 | 2024-10-21 01:05:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 31483139-592b-30f5-99ef-529bf42d3da2 | -3.79528 | -51.80462 | 2024-10-21 01:05:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 17fb00c5-89fa-30f2-87f3-26ef6a297076 | -3.79407 | -52.3283 | 2024-10-21 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| aee7df77-3b21-3dbb-b9f0-41895b75a13c | -3.7928 | -52.31913 | 2024-10-21 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b3113a9d-1df4-3e48-9c8d-e2bff577c759 | -3.77279 | -50.19012 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cda07745-18bc-32c3-b4fd-8f21250dcf91 | -3.76927 | -53.40843 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 27e88ec6-f545-3d77-9eeb-09194a85702a | -3.76785 | -53.39822 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 01be5e7b-47ba-3201-b1ec-fa949fba072b | -3.7591 | -52.4087 | 2024-10-21 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efb6df54-03bc-39c4-88fa-6ce554b4b171 | -3.74083 | -53.41242 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9e128948-c9c1-3b07-a978-71c85dea177b | -3.73005 | -51.33467 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0599e80-ee52-3b27-b82c-f0adb1c88258 | -3.72745 | -50.71871 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README11.md)
