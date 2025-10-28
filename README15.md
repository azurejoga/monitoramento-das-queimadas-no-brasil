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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a91fb85b-2011-31a1-bf57-73e986ed08ea | -4.75107 | -46.42427 | 2025-10-28 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ee3eb1c-6060-37ac-ac23-95017d3c54d3 | -3.30718 | -42.35469 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af56d79c-ecea-3550-8879-0cef7ec21197 | -6.13703 | -41.83382 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c1218239-6cb7-320e-a586-27c56582aa1e | -4.17862 | -47.65015 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26288a1a-02c1-3566-842f-36e9e50b21bb | -4.20363 | -48.35979 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45b8cb5f-a9d1-3dc8-96ac-6a8f499f46c7 | 0.9827 | -51.12916 | 2025-10-28 04:12:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ddabdf8c-ed36-39a7-a541-84aff5b6f95b | -2.22604 | -48.37243 | 2025-10-28 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b48c49e-78f5-3498-9edf-c2ffa669f90c | -3.59338 | -46.11254 | 2025-10-28 04:12:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c5f1d59-e2fc-30cf-b389-1a2d6a2045f7 | -3.72332 | -47.65151 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d26e0b7-ea23-3cf8-9a76-0e3d490f4401 | -3.02171 | -45.36751 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 0a73eab4-073a-3a1a-b87c-683aab40f3af | -4.54152 | -45.15965 | 2025-10-28 04:12:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d78b896e-b297-39a5-a367-30d8ba4cdeaa | -5.59144 | -41.31683 | 2025-10-28 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b7785b49-262b-3392-8b56-15915ce3061e | -5.43762 | -40.88135 | 2025-10-28 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9a531f87-8f97-368b-8dee-9af031c15be6 | -3.59327 | -43.60768 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7368d954-29c4-3ebf-8384-5015dedc7ea1 | -3.5305 | -51.5762 | 2025-10-28 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08a60742-4805-385c-8e79-a05352b592e9 | -5.66245 | -41.13586 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bd89b4bc-7d45-3c32-a485-3c8b9157ed02 | -4.18933 | -46.22859 | 2025-10-28 04:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 607e762d-0d09-319e-858f-8be4a0ce6476 | -3.79797 | -43.32335 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26906d19-0d27-326e-8420-82c647c1a0ce | -5.80586 | -40.81425 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3f47d534-6de1-32c2-a3b3-37a23a87bbf4 | -4.18708 | -46.22918 | 2025-10-28 04:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5405556d-b640-36d1-88c1-0c0475dfe453 | -5.47059 | -44.06756 | 2025-10-28 04:12:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00902b2d-2e61-3c7b-b0ff-2124264acaa4 | -2.75324 | -45.40892 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2b5c9a6f-fdbd-3b72-a5e7-bb02e8001f0a | -5.966 | -42.76045 | 2025-10-28 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f6942847-262d-34a0-a4d7-b2153a10d27e | -5.26918 | -44.32275 | 2025-10-28 04:12:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7a73176-0d5a-3b5d-bae9-e48be4cf001f | 1.04329 | -51.31366 | 2025-10-28 04:12:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07c86ecd-795d-33a1-8ebc-85f3fcc092e1 | -4.734 | -48.30627 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 781ffe91-3535-3c49-b2a9-e1351b3ea8dc | -5.96876 | -42.7644 | 2025-10-28 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e114a8b5-3d5e-3baa-9f6f-b6866ec4a42a | -6.13928 | -41.84139 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 38f1bec9-ddb6-3388-8d81-3cdbaa90f4af | -3.11322 | -51.29197 | 2025-10-28 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db555795-6cb1-3936-aa67-023be73c2d6e | -6.1327 | -41.7067 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4c1bfd3b-dbcd-3c29-a0c0-3cc7c0a1f302 | -4.06509 | -49.44651 | 2025-10-28 04:12:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32e393da-e8bf-3f25-8e92-4b1406cc0a92 | -4.92615 | -48.5597 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b524ab35-0743-3887-8db0-f5f3609a295b | -5.41783 | -44.83967 | 2025-10-28 04:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc1dac74-ba79-3474-a28b-1b75e9e931c7 | -4.00913 | -43.21361 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b4a9d11-15d5-3a3b-9da7-5e52955ac575 | -6.16119 | -41.54329 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26845e5e-2aba-3409-8182-6bac9cc7af57 | -4.74116 | -48.01906 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42296cca-1caa-35db-8de8-fafe036388ae | -4.90707 | -48.56902 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dc61c23-fe7d-3d67-935d-2aed340e4ea5 | -1.00292 | -47.65354 | 2025-10-28 04:12:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a36b161c-66b9-377e-ad9a-75a56b4267c9 | -6.19583 | -41.51921 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dbdf8dab-94cc-36ca-bcbf-7e7700232e5d | -5.99878 | -41.38577 | 2025-10-28 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 20cd00c2-93a0-36fd-9d9e-fc53a41b8037 | -4.75552 | -46.42045 | 2025-10-28 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5aadb29-a235-301e-9f4d-3bc5a31a5536 | -3.65722 | -42.72277 | 2025-10-28 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 25ae4a8e-5aa1-3c34-bdd0-e33431f886a2 | -5.66294 | -41.10986 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9b339325-e97f-3f58-824f-e07c6be8d771 | -2.30773 | -48.14483 | 2025-10-28 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27cead3c-cd32-3f28-ae3d-412a51c6a446 | -4.43614 | -43.44199 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe275567-ec97-348b-9eaa-2325ea4a1cad | -4.46337 | -43.70149 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09bccf5d-c719-3611-9395-a3a585c5c00e | -3.581 | -43.59848 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecec4238-3af5-3033-9bb6-74e71ecd19c1 | -3.4443 | -41.8452 | 2025-10-28 04:12:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d7a31788-45a9-393d-8700-da2000619cbe | -3.82482 | -42.46132 | 2025-10-28 04:12:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e56852e-0739-352b-ad96-500aed565cf5 | -4.88753 | -45.74128 | 2025-10-28 04:12:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c944f2fc-a7e2-39e3-9377-19bcd6e7d112 | -4.02327 | -42.90767 | 2025-10-28 04:12:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59a8bc0a-8ddc-3265-857b-525a04fe6ff8 | -5.65403 | -41.14567 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 01792d3e-71bc-339b-82ef-d51f499f05d7 | -6.11831 | -41.73357 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24da0c9b-081a-3e96-a16e-d8d77f3f512d | -4.24062 | -45.77359 | 2025-10-28 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc7a5dad-d9ae-3143-8559-e223ae0081d3 | -3.70353 | -47.64424 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2bf5db4-44f9-30e1-9d4e-67a3c6b7ebf4 | -1.83811 | -45.29224 | 2025-10-28 04:12:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a95da88a-3f35-38b2-8d1b-917dcde81337 | -4.73179 | -44.45129 | 2025-10-28 04:12:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f49a065f-e32a-3c52-88b3-9fdba042b4a6 | -4.86545 | -48.40228 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a63f441b-2fc8-39b1-9223-0ad8bb0ce924 | -4.20296 | -48.36385 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b76a19c-a018-3a11-a139-bcda65bcd274 | -3.38392 | -50.14856 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 811ac61a-0048-309c-894e-75ea59284414 | -4.90652 | -47.42043 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9670db06-af05-30b7-8a6b-7c7d44dd9c27 | -6.12212 | -41.70871 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d5483dd3-5d44-326b-b0cd-cadd6ec2ea1a | -5.0332 | -42.56715 | 2025-10-28 04:12:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a612b0f-277c-3cbc-a05c-6ace86de1501 | -4.4401 | -45.98124 | 2025-10-28 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7aa38a5f-1635-3c35-b823-b8fbb07d88da | -4.22191 | -48.35479 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 475f71be-c327-37b5-a763-d6d4f6fb2678 | -5.62911 | -39.65446 | 2025-10-28 04:12:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 295905be-7024-36d0-a7bc-755075b3acff | -4.22423 | -48.36723 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e469a969-e7c5-3b70-8091-f763bb71a54b | -2.42325 | -48.43732 | 2025-10-28 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ea7f6f7-fc25-32d4-85e9-9c02cdf0a570 | -4.91782 | -45.48396 | 2025-10-28 04:12:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6e61872-fbf9-358c-bb79-e8bb0cd36072 | -6.16493 | -41.67521 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6da69834-67cf-3036-8398-c50e11a8d66a | -3.75212 | -51.75517 | 2025-10-28 04:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a061aca-c0f5-3738-be32-be4dcd623cf5 | -3.7064 | -47.65244 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 034a60cb-f7e2-33b2-83c3-5d20730df2ef | -4.50334 | -49.64668 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e0ad628-d954-372b-80cb-ff5eb1215023 | -2.58663 | -48.4045 | 2025-10-28 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5ca6170-279a-37b0-9d0f-0b4053cf84cf | -2.91841 | -48.72248 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 87214347-abbc-3bd7-a214-dce2f0e4ffd3 | -3.71262 | -41.56517 | 2025-10-28 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 16792daa-e666-36e6-9edc-f2bc2d7d08cd | -6.1437 | -41.83485 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 741a69cb-bc25-3147-95b0-d9ce2394bb86 | -2.80674 | -49.13696 | 2025-10-28 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2bcef8c-e4cf-3b0c-9cb7-9f69679151a2 | -4.74096 | -44.43758 | 2025-10-28 04:12:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95752f8f-4e9e-3358-a1de-47f678655985 | -5.65796 | -41.14259 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c79efad8-c3c8-3231-9efb-184399c1bd94 | -5.52702 | -41.7105 | 2025-10-28 04:12:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f9d23b0d-dec1-36f7-90d3-ce6b1f0a3596 | -5.25962 | -42.49022 | 2025-10-28 04:12:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b94e0788-ea98-33fe-8cd0-5c28d955a47d | -6.1892 | -41.56223 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 66eddbff-2449-348d-8721-b56fa8f0d17f | -6.16229 | -41.53614 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 520137d9-08cd-3d45-95e2-c49ac0c69939 | -4.51577 | -44.03774 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25004d3b-d562-39eb-8748-3e01cfdd66dd | -5.48217 | -43.08959 | 2025-10-28 04:12:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 989328c7-5582-3971-b808-1fc2f8b0543e | -2.80597 | -49.14172 | 2025-10-28 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e5a6bda-929b-3553-848e-e9ce55016080 | -5.5842 | -45.33533 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac48cfcf-3243-3a4a-8133-3cb9e76eba04 | -5.64636 | -41.11838 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16fc96cc-920c-3f13-949f-d01e30da007a | -6.16188 | -41.58356 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4501ad87-293e-3929-8af9-ace3def483a2 | -3.58435 | -43.599 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bebfa81e-88e2-399a-be33-bdd26b18f43b | -3.39841 | -50.27436 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b35c29e-f48a-3764-b350-c5f1b13f9974 | -4.69365 | -46.44736 | 2025-10-28 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 642e5f94-e719-3c71-915b-8c8d05ab8ed2 | -3.89535 | -47.33233 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c5fef08-9f45-31ef-b8f1-e3b4fccf2fad | -4.91878 | -41.15498 | 2025-10-28 04:12:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c03f7849-2488-3fd8-a909-fc2b94b76c80 | -3.52829 | -51.57591 | 2025-10-28 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 936b574f-84fa-3596-acad-0dafa2487418 | -4.44078 | -45.97698 | 2025-10-28 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9a29ae8-8c9b-382e-9269-b0b1be7b9f10 | -3.80225 | -51.10297 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c55c65c6-dde4-3242-bb0f-f99fbf8b2b2d | -6.09846 | -41.7738 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bc99145c-1676-3a13-8a48-64b4d83be5e9 | -2.86346 | -44.37963 | 2025-10-28 04:12:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README16.md)
