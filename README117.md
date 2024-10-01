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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aba701be-4fe6-39f4-a2d9-c3ae08fbbf09 | -15.91532 | -57.18311 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b7fd40b-8198-3d29-8496-ea9ab419de0c | -15.91312 | -57.17524 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c1f95a1-8b9f-3a63-b714-135d340e195f | -15.91256 | -57.17891 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8021fc62-6bfa-385e-8cff-d724b324bd81 | -15.91092 | -57.16741 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7cb7d89b-c24b-3fa8-825f-379dc90f2846 | -15.91089 | -57.21191 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45db79ca-4d07-36a6-8e8d-95618289edf6 | -15.9125 | -57.44402 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8467d26d-ac6a-368e-915f-264fb436c000 | -15.90919 | -57.44345 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 99faffbc-df62-3b59-9622-ede1b306a782 | -15.8103 | -57.3797 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7aa2070d-7ca3-38ea-88c4-f70d207822cd | -15.80258 | -57.36383 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc94757d-a0df-394d-bb83-42ba6fbda576 | -15.80134 | -57.34863 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 818d5af2-4d9d-3a62-84bf-fb77eef97dec | -15.80092 | -57.37445 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffc6ac02-54fe-3ad9-a981-61b1a1528d54 | -15.80037 | -57.37798 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43f57481-cc7a-3849-bf78-9212b3eaa775 | -15.79747 | -57.37364 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2e48f93-ee28-30d7-a75b-a2c1e6b17d3d | -15.79692 | -57.37717 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f3a68b6-dfd0-330d-81ce-5332476b3e1c | -15.74446 | -57.43094 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d47a684e-deec-3f70-b32b-a65520cf41c8 | -15.63229 | -57.45297 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5f435db-9636-3f02-bea9-f7f37a2eea49 | -15.63175 | -57.43455 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f86ba019-2bcf-3cf2-8d34-f58c2af04e27 | -15.63174 | -57.45654 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83960dd0-7ff9-3240-84b0-7c015e277f2d | -15.62899 | -57.45242 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcf20688-a8ec-3f04-bc3c-d0b5134a5b3f | -15.62843 | -57.45599 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ac8c97b-1c90-330e-9a81-67a38f058817 | -15.62788 | -57.45958 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84cbcaf6-c668-3a7e-9606-bf1c43e2a2d5 | -15.62568 | -57.45188 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5214de75-fd77-31a3-a098-9574eab7948c | -15.62512 | -57.45546 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81140a4d-5ba0-3289-8a6c-514c902b8977 | -15.62458 | -57.43703 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e73e699-5e87-3934-b611-f5a6e69d316c | -15.62292 | -57.44776 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17ef216a-7dad-3764-8990-1f9b9adf50fb | -15.62237 | -57.45133 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 010e6700-7979-39a9-b7c9-6fb84eb644ba | -15.62182 | -57.43291 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb9364a5-1cdb-3ae5-b273-4102b0e110b4 | -15.62181 | -57.45491 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db530982-b33d-3063-a6e9-94c302124e11 | -15.62126 | -57.45848 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9a76ee0-39ef-3c02-9fd6-b9989ccfb59b | -15.6185 | -57.45436 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4daf1ae-4f13-3742-92cb-55b95c34c29e | -15.6163 | -57.44667 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 026c08ac-ab47-3920-a8c1-572f753d93b3 | -15.6152 | -57.45382 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 881faa2a-940c-3379-94c1-2f0450b9a321 | -15.61299 | -57.44612 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14333e05-6512-3067-b227-be091fe35147 | -15.61024 | -57.442 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb005a61-6824-3e95-b5ea-b91862f63d0a | -15.60417 | -57.43733 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c43fe36-cc34-392b-8180-243b9072fdc4 | -15.60362 | -57.44091 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19872e13-0e04-33f3-a536-187bdb3df1ef | -15.60086 | -57.43679 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c21d913-2921-351a-9ab1-a03d6fd3eef0 | -15.60031 | -57.44036 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70884f6c-52a0-3e15-b1cd-8d6a05c3b321 | -15.597 | -57.43982 | 2024-10-01 05:08:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c4b6b26-64a5-3592-a64b-3b5c92367c8c | -15.59368 | -57.46126 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77380824-7bef-3e66-8911-c0977ed48c5d | -15.59314 | -57.44285 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4068cf0-78a1-3941-9745-7e5d3fdaeaa9 | -15.59259 | -57.44642 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07c2f7c2-a61b-324d-b389-eef1730b6f57 | -15.59148 | -57.45357 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c38877c9-63e8-3dfd-8e98-34106d860784 | -15.59093 | -57.45715 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bb0e612-8f8a-3de3-aec2-66eed767ca6d | -15.59037 | -57.46072 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8362ce3-8fe2-3d07-99b9-7000325e97f8 | -15.58928 | -57.44588 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43d81743-3a56-32ac-ad21-788b7fb93976 | -15.58873 | -57.44945 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0339d97-0410-36e4-84fd-4e28ef5690bd | -15.58817 | -57.45303 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80ffe412-7bcc-3b61-8dda-84c9567e35a3 | -15.5832 | -57.4632 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fda7af6-158e-3e5c-83d3-99fa7beac3ef | -16.61104 | -57.29934 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 23ab0612-fa48-3a3b-9288-043a4f8343ae | -16.61049 | -57.30298 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e0d5c1eb-7ccd-39ac-bec3-6f3d7f7d092c | -16.60772 | -57.2988 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e9131d16-845d-348c-a0ac-d52ce85c3b76 | -16.60384 | -57.30188 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 80575231-5061-349c-af85-d786605c948c | -16.59387 | -57.30024 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 268cbe70-3bc2-30c0-a61d-0cb7ddd1ca56 | -16.58722 | -57.29914 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0b8e6c84-8ce1-3a37-bb22-57ae77e5e55b | -16.5205 | -57.3368 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fd63c2ea-cdf6-3e26-83d9-d773e26b8685 | -16.51994 | -57.34042 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dff9c116-0e43-38b3-863e-6c20276de4c2 | -16.50998 | -57.33878 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b7d7267a-d828-35aa-8de2-e35d76eb0043 | -16.50721 | -57.33461 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3440e17e-927f-3238-91f9-b611cca48817 | -16.49116 | -57.32826 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 746d5003-bccc-3d9c-90d1-86bed4c69ca0 | -16.48064 | -57.35249 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 69ea02ee-3459-3e71-8d93-4bbaeb6b5a4e | -16.48064 | -57.33024 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b19a53db-ef47-38d8-b72c-248f7c1821c7 | -16.47621 | -57.33693 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 581fee67-0f4c-3662-809b-d7294be76d71 | -16.47566 | -57.34055 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a2f26d40-38d2-3a97-8776-748b3c752da0 | -16.47455 | -57.32552 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2e1ee826-40d1-30b4-81a1-38507a75d3f5 | -16.47289 | -57.33638 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 66c6d15d-9dc3-3b6d-8826-808c10b21257 | -16.46957 | -57.33583 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e19bf0b2-c336-3dfb-874a-22ad3c7a6c2a | -16.46902 | -57.33945 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 23f716ea-df4c-39f6-bc20-40ba1a54cb32 | -16.46735 | -57.32805 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 18ef94d7-d012-3909-876d-4762ef92674d | -16.46348 | -57.33112 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0cbdd8bd-0520-375a-a57a-1e88247fe9a6 | -16.45355 | -57.41842 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 678c1db7-702b-371f-bbd5-b0877d1cafda | -16.45034 | -57.3288 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c8b80361-f766-3d34-b37d-c210e6fe56be | -16.44979 | -57.33242 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 912bb914-c92c-3b8d-8aba-a1ad35e0edb1 | -16.44968 | -57.42147 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 232935ab-ac0a-3970-9c9f-9a601e615755 | -16.10643 | -57.53135 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f6dc91c5-c020-3038-aaf9-163b9b7b158c | -16.1003 | -57.52625 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8159c9c9-d888-373e-b271-9ca091528932 | -16.09975 | -57.52981 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa796122-15a6-3084-a6e2-746154dd5312 | -16.6321 | -57.2507 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8b616080-c734-36f2-abd3-dfa444970041 | -16.63155 | -57.25433 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 75c9cbda-3302-31c1-96d0-fc5b954faa85 | -16.63099 | -57.25797 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.4 |
| e625fcbc-695d-3501-899a-a4812eb7a7fb | -16.63044 | -57.2616 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| a7e2d974-0d4f-3964-8597-31bb3b75d38e | -16.62989 | -57.26523 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 535f2663-b84f-37d4-af98-616370aec032 | -16.62878 | -57.25015 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a763373f-dd63-376d-bb18-a4c39cbf8b6e | -16.62822 | -57.25378 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 7a72479e-724e-314e-b43b-ff0c7342983d | -16.62767 | -57.25742 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 454cc155-8579-3404-9de8-67ddecf9f72b | -16.62712 | -57.26105 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| e9c8e389-c6ea-3b5f-99d5-f3f8b3d62024 | -16.62656 | -57.26469 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 8355cebc-9363-3498-adef-04a67bfcef3b | -16.62545 | -57.2496 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3bcfceeb-5612-35b7-a8a6-ae4397c23acc | -16.6249 | -57.25324 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 161.9 |
| 35dc9ac2-85ab-32b0-a223-e3978abacc10 | -16.62379 | -57.2605 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| dda18c3e-a036-30c9-b455-0371984088e1 | -16.62323 | -57.26413 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 4f946037-fe04-3bb0-afe9-d2b3df0d7d94 | -16.62157 | -57.25269 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 161.9 |
| 95d19e74-2c7e-3c39-b081-53e955d16907 | -16.61713 | -57.25941 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a46defff-000c-3703-aca7-fe336720f0eb | -16.61547 | -57.27031 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| b50ca6c9-148d-3a7e-a403-52236ef23f86 | -16.61436 | -57.25523 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 109e5188-defb-39c1-999e-b91fa865b652 | -16.6127 | -57.26613 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| f1062983-4a31-3fab-9ed7-5456f0740b7c | -16.60937 | -57.26558 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e45f53ac-df51-312d-89bd-eee3cd94a804 | -16.60882 | -57.26921 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 619b7d9a-b049-3cee-9857-4734bfc5150e | -16.60605 | -57.26503 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d1de4cd1-3676-35f7-9f07-d04eb29ef6d1 | -16.60549 | -57.26867 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |


[Clique aqui para ver as próximas entradas](README118.md)
