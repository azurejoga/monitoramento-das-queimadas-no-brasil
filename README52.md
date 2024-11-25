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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f917bd4-886c-3676-9b78-65a2ffbbacd8 | -4.25877 | -48.73187 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b83ad8af-1f07-3b2d-9e4d-783200127654 | -4.53796 | -47.66938 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5be7bad2-d7b7-3062-b118-c1c077b74cc1 | -2.61087 | -53.97105 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 05ddff8f-218f-3da4-a98f-bdcdd51c6036 | -2.24569 | -53.6202 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c882657-0a7c-368b-8b65-b8c50eab2844 | -2.22235 | -46.39287 | 2024-11-25 05:20:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 568b36ac-e1a6-3627-a6de-43a2bfbdafe4 | -1.04324 | -51.74036 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f206ea15-e63a-32e2-92fa-219e37b0b7a2 | -2.43805 | -54.14302 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d9df65c-bcba-3586-bd17-7549c6b157a5 | -3.10138 | -53.7366 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f6f79d8-9e02-3d0e-a269-dc9ad448b579 | -0.34395 | -51.54168 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ebbe403-4018-3cf4-a510-8ee834df7edd | -4.25317 | -48.72791 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20f0c837-d01c-38f7-92f2-bd4e4487176d | -3.23702 | -54.22993 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbe2cbb1-7e09-3ba1-8a0e-96c8e7214e9f | -1.17487 | -54.13172 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f26d1588-ac1c-331a-bbbf-2d10a4b9aa8c | -3.23285 | -54.22928 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02b829ba-b77c-38d3-b827-b03cc6424740 | -2.79199 | -53.00381 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63332b47-a3ea-3dab-96c8-4148366f1c8a | -3.87385 | -52.20948 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60883bc9-0143-3d72-bca0-89334ba30515 | -3.36784 | -51.42974 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a330042-b276-3122-922d-597791fe346e | -2.58643 | -54.36943 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b515b64-fae1-3517-a9cf-dc055eeca826 | -1.13006 | -54.17915 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 678cf270-6de0-3b6b-a864-995c4b929eda | -3.28022 | -53.83625 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aad982bb-0164-3656-8381-83485143abd1 | -1.44502 | -52.58147 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77800c79-32aa-3798-9c92-efe591adba3b | -3.04797 | -54.02567 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fa5da65-0da8-3611-b892-56a37f8a8e92 | -1.38615 | -52.32957 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ace252bd-1c36-3b65-995d-ae83d464ce76 | 1.95004 | -60.85921 | 2024-11-25 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb60e707-5f90-3645-9453-f82f2b65f577 | -1.43807 | -52.44693 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4b35ab6-ce5f-32df-9d1b-d0b65bf212f2 | -1.31142 | -51.74923 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9c025b0-9cdb-3df8-b982-eb5de398c800 | -2.79415 | -53.00244 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5032877e-184c-373f-ae46-80edcb4b8834 | -4.54605 | -48.95471 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e964c3b-041c-3c92-b166-1739e5d1aaea | -1.1301 | -53.61535 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62a79b3b-1b8b-3510-9f05-0d6faf205c56 | -2.83864 | -54.07012 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e502198d-f81c-32cf-84ee-dcc205a29e92 | -3.93754 | -47.98737 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6abbf05b-03b4-38f2-af96-5e1bfe526f68 | -1.88661 | -53.32994 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 169e3e49-45b7-36b2-a0a2-9c4b43b710ea | -2.18709 | -53.8018 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83292fd7-622f-30be-b102-cca2dcce754d | -3.67685 | -54.58711 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cd577dc-ed53-3e90-8ea9-11d71c6616a0 | -1.24399 | -51.74186 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3ddf01d-63c8-37a2-b65d-0047b8435b04 | -4.41872 | -49.70639 | 2024-11-25 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eab34b96-62f3-3f63-ab38-249dc290c286 | -1.24335 | -51.74409 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c297bb9-c31f-352e-bb37-c5118a73a372 | -1.4793 | -51.96355 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0967f5c-e365-30a1-b48b-f7585d2b3569 | -3.50799 | -53.81762 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 021d49f7-e21c-3398-9fbe-5d8a7a1d96cb | -3.24926 | -53.27291 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 129fd14b-f4f8-3718-a4a9-a6a9138da7e0 | -0.97684 | -52.79986 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b67e192-8f51-339f-be10-6d4e5e4cbd44 | -2.88977 | -51.58544 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c760048a-b54f-3b13-99ad-32ee6805fd9d | -3.37931 | -54.68294 | 2024-11-25 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fb4bbc2-1874-3019-a591-ef5ae7bddf26 | 1.36847 | -55.91964 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4179c19d-7e80-3c41-8dfd-71b61192da0e | -0.35151 | -51.97502 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02ff3d72-dd60-3eff-b59d-493f200131a7 | -2.13779 | -52.27645 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45d30032-1209-3af6-8865-9708f7454231 | -2.79508 | -53.01356 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e550c3b6-f16f-3d2f-a596-1c63eb57b1fc | -1.76868 | -52.7101 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4d802f3-d270-3dd2-bb9a-d43fedf19fe6 | -4.25794 | -48.69515 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6130353b-6a36-3a00-b9d3-98499b7f9e74 | -1.81854 | -53.72404 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fe680c5-ca8c-3598-a048-6d858fec34a9 | -2.76189 | -54.03215 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b47d349-9d28-38bd-bb44-f6c80e605ab2 | -3.64558 | -51.39119 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a286b723-0272-3226-97f8-5fed2fbaf46c | -3.06411 | -53.22089 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0620d671-dd48-3021-adba-4f382ee38ca0 | -4.24224 | -48.67324 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8dc5ce8-9a1c-3d37-a618-75e97ef1854c | 1.41076 | -55.8885 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c9c0879-06bb-3c64-a11d-547b28d1032b | -3.94469 | -47.983 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8a4013e7-e899-3ae1-9f79-50e39cbbe54d | -2.79991 | -54.12025 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e4531dd-79d3-3610-af68-6fbd84426c48 | -3.23227 | -54.23308 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c7b0913-ae98-3e03-a9bd-b253c7466c0f | -2.80113 | -53.01753 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 628f6a4d-b235-38ff-b9a2-0c31981df8e9 | -0.98338 | -51.71531 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec9714d1-ea46-36e2-9374-1696450c56f1 | -0.98259 | -51.72046 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea80497d-bbd6-34b9-b80c-183fcd5df5d2 | -2.17375 | -53.77582 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a06fe50-6648-34d2-8c2e-dbf5b767c4ba | -3.26497 | -53.82112 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57dd3279-3edf-3d64-9bdd-cbff94a7741f | -1.62587 | -52.44562 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e81e396-4fa6-3ed2-85c6-ae9a65882843 | -3.5802 | -52.18179 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4987158-3304-336c-a246-614bc1dfb0f7 | 1.51128 | -55.67498 | 2024-11-25 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91a98310-c8bd-3b1f-aba9-1fe7c91cff0a | -1.25758 | -51.74925 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 113e9645-570f-3cf3-ade6-edc6ab9cf47e | 1.41557 | -55.89593 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efc5304a-077d-32a3-8afb-3e370b2a62ce | -3.25062 | -54.23478 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c4ea7ce-a8aa-378f-9c1b-e9e5a3cd59d2 | -3.96501 | -54.07834 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aee66684-0cf5-307c-a40e-257aee93e74e | -2.8018 | -53.013 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d8105c8-fe19-3970-b46e-da46da416ded | -2.82741 | -51.28823 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c26571c-85b8-3a75-91dd-2fc07bbb72ff | -3.94271 | -47.98545 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8b199f2b-4be3-3a74-9adc-660f5ea5327b | -3.50611 | -53.80106 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a224f418-ce0e-3944-8c0d-6abe9a7004bd | -1.62279 | -55.17405 | 2024-11-25 05:20:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a1e4fba-d8bd-3594-af8a-abdb727138da | -2.35599 | -53.7121 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46f56827-fb74-3997-81e5-a95c70ac1052 | -3.2487 | -54.21885 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09cbdfa5-d00e-3984-a2cb-130dfe04843d | -3.36275 | -51.42908 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 194157c2-b18d-3d57-ac14-c61ecb46d157 | -1.99107 | -53.29299 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cf464be-56f4-3dc0-af1f-c4bbe5798d02 | -3.27961 | -53.84029 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0134cb6e-8e92-3512-91e0-59d89339c509 | -4.25247 | -48.73271 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 7b91c66a-7906-39e4-a73c-5b5cf8f0de70 | -3.71028 | -51.78249 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3fb30009-963e-387d-a1b1-b4a33b909413 | -2.64975 | -51.77562 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0356cafc-7c4d-3fc9-bc4b-1130abca46ca | -2.20767 | -53.66793 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 645bf922-feca-3499-ac9f-f44b5b530e8a | -3.49934 | -53.81651 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d172c16d-adb2-3ef2-92cf-73b0c511b6c0 | -2.8178 | -54.11514 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5a1a046-d2d5-3429-b135-95cd4b2ec15c | -4.26008 | -48.7225 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f93dcf4-f1b3-3812-944a-64052aa77260 | -3.42217 | -53.28509 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 630f2350-97c5-3f09-8635-d8804787a0e9 | -2.87916 | -51.58578 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f733807a-c3ae-3fda-baaa-b1e897925eb3 | -3.04374 | -54.02507 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0392fa9-63ba-30b1-8438-16759f3603d1 | -3.04346 | -51.44566 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8418029-7aa5-388b-a6d9-828aeec44c41 | -3.25232 | -54.22329 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11e90a55-073a-3168-a576-e647a2c6c75b | -1.77298 | -53.62596 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f566b03-1496-3a7d-bd75-ee2aa1516c80 | -2.80564 | -53.01818 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cb88817-dfca-33a1-bf51-782c7d5cd335 | -3.25593 | -54.22774 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbc028e8-9198-38f9-9946-fd95a16effc1 | -2.82154 | -51.79808 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8795b36b-6446-3369-89f5-c7871ef7c184 | -3.65069 | -51.39193 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0bf55fc-6104-3efc-8815-8d8da7a064a8 | -0.36715 | -51.55063 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23088117-558c-3987-805e-62ff09ee55ee | -3.84964 | -52.14975 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4af59ea-1806-36ea-8b2a-611f7931794b | -3.47567 | -51.98987 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b83c9a2-e7da-341c-b3a3-6ec105a0a027 | -3.54504 | -50.40491 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README53.md)
