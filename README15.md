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
| 23314afb-aefd-3143-9d21-74980740a5e7 | -3.71074 | -51.84415 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d81c2c8d-9083-3484-9dfb-99e4d3505755 | -6.99023 | -39.65176 | 2024-11-21 04:08:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 49ee0d04-5f78-31f9-a36b-d9effbc5faec | -3.30088 | -50.36851 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9b47d7f2-3a7b-3efa-9f27-1d7810e336fc | -2.75424 | -52.11789 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 48bf6409-8c50-3931-ab21-227044dca9f2 | -5.12693 | -45.17244 | 2024-11-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98732ee2-a8f2-3352-9f7b-4805368320b1 | -3.30015 | -50.22259 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbdb4eff-95dd-383f-99a5-8aca9da764ac | -3.19288 | -54.3273 | 2024-11-21 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b08cf6c6-681d-35ab-bc32-bfe0893cca95 | -2.82657 | -46.67941 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 479c9bb2-2361-35e6-b8aa-a55362b3e8eb | -5.72053 | -44.81095 | 2024-11-21 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6c5b2692-f85b-3c13-b178-0a20f113fcd9 | -3.39961 | -49.78814 | 2024-11-21 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce38737d-2d6f-3c63-b42b-caa58ae64476 | -1.74374 | -52.05694 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 79c19777-112d-3f99-86eb-f72eb27b83a1 | -3.10547 | -53.17251 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea5b6746-5a63-35eb-9578-3df6334b99cd | -3.06483 | -51.36279 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6002fb0-f8bc-35d5-87dc-e70f9b32d1e7 | -1.59864 | -47.49194 | 2024-11-21 04:08:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78967a87-c38b-3c8d-bf38-7f507979cee6 | -3.56965 | -49.9939 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8491c835-4f37-3678-9c7f-915f9f7be599 | -5.70865 | -39.06776 | 2024-11-21 04:08:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c02a268-b8c4-35cf-bdeb-faf66e41e090 | -2.63122 | -48.48347 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a20355c4-eab0-38bf-8e06-095aac598daa | -3.39819 | -49.78698 | 2024-11-21 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6142dc41-2b4b-38f8-a6e9-5d3d74da7f11 | -4.60978 | -48.47926 | 2024-11-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44eec957-50f2-34b3-993f-9d267b4cac76 | -1.18862 | -53.71665 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ca31d8d0-2cf5-3b48-aa4d-56f939e12d95 | -4.414 | -45.96198 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61c864e3-1fb8-3a9c-b30d-697fe6d11419 | -2.57528 | -49.09198 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53ae38b5-10d8-3d93-aeac-5a787cc9db70 | -1.47248 | -52.51789 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cbb5612-18b5-3432-90c0-8b97d25613c3 | -2.69643 | -46.2541 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a24de222-6dfe-30b5-856e-749241af66d4 | -2.69532 | -46.23508 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8b9e54f-e47a-37ad-9d28-1f0b9a331e66 | -3.01079 | -51.01056 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 137bf69f-15ce-3d28-966d-b990e41ee01d | -3.63979 | -51.45528 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 858ec645-3177-31f8-8549-c873fba8fcb7 | -5.87636 | -40.04028 | 2024-11-21 04:08:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3242eb67-d062-38e8-8ade-56c3ba869d1c | -4.24299 | -46.12095 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5e7cb96-ffd0-3ce5-b1f6-750e38b88b7c | -1.44921 | -47.12154 | 2024-11-21 04:08:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 261ce052-d5bc-3bd9-9143-a13730046b14 | -0.41961 | -51.56827 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aacf334a-0459-3a9d-8916-6d0764a174c1 | -3.03611 | -49.476 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ee0d838f-8cb7-38b4-9448-a5dfcab7a518 | -5.89461 | -46.64776 | 2024-11-21 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6047dce-deaf-3feb-9b2f-75a348283ce3 | -3.9479 | -51.22709 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e1e6d18-72d5-3f0a-9209-2813e42bb3bb | -2.61921 | -51.80529 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1719324a-7e38-30e3-9ad9-79889669bc07 | -2.41876 | -48.97907 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17ba6f2f-d595-3bb9-880f-8471275bbe6d | -3.53735 | -50.44086 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 10604dde-f752-35d8-a62a-1a392a644fcb | -4.41085 | -45.95652 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2ce1856-aa67-3c7d-9f38-430285364c28 | -2.5748 | -49.09488 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a742ed55-ebe7-3cd0-907e-e5ede02a52c2 | -3.0095 | -51.01822 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5e3be903-fefb-3399-8b1e-efaeee7e8efc | -4.4843 | -44.75761 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4b9c3d6-544c-3202-9089-c93b155a69be | -3.9275 | -51.17701 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9c27a67-cb29-3521-891c-e6ddf6a45b33 | -3.56947 | -49.99324 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5e6e1d7-e0e8-3b1a-aa92-5dee03b15af4 | -5.19512 | -47.7402 | 2024-11-21 04:08:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 752b88ff-999d-30cf-b94e-1b59ad9f2ad8 | -3.85113 | -50.69534 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bc6c2e2-3032-3488-ba3f-dd77c43d3031 | -1.46409 | -52.68853 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2e3533a-2427-32ca-8889-5a28cd6ac417 | -5.60843 | -46.28991 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d326736-cde1-371a-acfb-7cf91ae77b35 | -3.12057 | -45.4465 | 2024-11-21 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d533a56-ebc3-343e-aa6d-d7aed9f8f3c1 | -5.50627 | -48.36129 | 2024-11-21 04:08:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8feacab0-6d34-3f89-a3bd-62d5ab1fb20e | -3.02479 | -51.52909 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1d7b8f9-67b2-3389-87c8-adcba4193ea9 | -1.25696 | -51.76343 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e3e5f7dd-df6a-3fb0-a3ed-73c5967447fd | -1.55072 | -47.64742 | 2024-11-21 04:08:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 939493c0-e86c-367a-993a-b63cfc9d520a | -4.17759 | -53.57854 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da4e4f9c-aa60-3969-9254-60a96b11aeab | -5.72377 | -43.50965 | 2024-11-21 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8217edb2-3b88-3b66-a52a-cd32d8db2fc5 | -1.65037 | -46.96017 | 2024-11-21 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e2694a1-7479-3b2f-8107-8d5f0c0ba69c | -2.06323 | -53.43345 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a06e11ba-a1b1-311e-8fdf-c015228c1dde | -3.95357 | -51.22788 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdbc7f6d-7956-347e-833f-0586c04ae02e | -4.07084 | -50.90562 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f9898ba-69ab-3aed-a3eb-f7c4afc31ece | -5.95211 | -44.24797 | 2024-11-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82d07a5a-ee52-32d4-833b-cf0854a75a39 | -2.14393 | -53.77508 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 41250fd4-b3dc-3ae0-a9cd-58a676941d61 | -4.99998 | -45.28713 | 2024-11-21 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92a1f9a3-c2e0-3a2b-be21-88cce10e86a1 | -2.91669 | -53.06529 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c50b3481-4086-3073-8b59-84fcadee91bd | -2.19825 | -53.65756 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| ef06f7e4-818f-37b8-befd-711c7cb7e365 | -2.95049 | -48.33198 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d51cd57e-4dec-36a9-a12c-10f777fd8e96 | -2.62485 | -47.96283 | 2024-11-21 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fc84440-c45c-38bd-9ee6-b6264b86f6fd | -2.67093 | -46.23513 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 197b11be-e922-3fec-b725-0658d540a7d1 | -3.28351 | -53.84374 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c8883ab7-e8d5-3760-aaa3-886677d86bca | -1.36737 | -46.0353 | 2024-11-21 04:08:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ba0b8f1-0923-3931-bd74-21057420c3e6 | -4.24921 | -46.10791 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a953bb4f-9b62-364f-9682-3d64c99bee00 | -3.3001 | -50.3576 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28dafaa5-6302-3d5b-92ba-11e2439a7886 | -5.82849 | -44.10958 | 2024-11-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a165bd2-7c79-3e23-b657-4b30749c52fc | -5.94982 | -44.46327 | 2024-11-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8037ded6-2e56-3cc5-a695-8011126e2d01 | -0.29443 | -51.60331 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b23cfca-502f-3ce5-bd31-137369c3f119 | -4.24609 | -40.75991 | 2024-11-21 04:08:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dac60bf9-1e1f-3bf5-98f1-5acbe53df7bb | -4.14665 | -43.88016 | 2024-11-21 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e9c58710-6d47-3eb6-97e5-222a59c55198 | -2.94105 | -48.33046 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4efca923-ccc5-3291-ba13-bdc091bfe769 | -6.12356 | -42.52121 | 2024-11-21 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| b8f7c796-1166-37ec-b554-136e4b95f2e4 | -2.06672 | -53.43521 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b9c84bf2-4800-396e-88c6-7e9ee39054d6 | -4.13948 | -47.73272 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a78e1088-a250-32e2-b7fd-8f58a7867c60 | -2.92995 | -48.33908 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c1d55b6-633a-37ae-9836-0d1455c99335 | -5.72437 | -43.50594 | 2024-11-21 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fbd0c02-9b06-34f3-9268-20ef1a6dce3f | -3.78395 | -44.06256 | 2024-11-21 04:08:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5025bfb-f31a-3e7e-b291-7c4ef5d53d0c | -2.2439 | -49.20121 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb76165e-7cfd-3687-9469-d361a434aa06 | -3.55021 | -50.17083 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57b5579c-6c8a-399f-87ed-7a8a9dc5498d | -3.02553 | -51.52474 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09765712-db62-314e-a39a-817af1460c33 | -2.08947 | -46.32381 | 2024-11-21 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| caabe2ef-a588-329d-aca4-0b3a93d6d0c9 | -5.30712 | -43.08062 | 2024-11-21 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b20bfc40-03b2-38e9-85e2-39ac2b603a3b | -4.38859 | -47.75687 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8577e915-1ac8-3ffd-995c-0d7cdbf93e59 | -4.38521 | -47.77262 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab24af2e-e849-39b2-a74a-827c9c7e8be0 | -3.51453 | -50.22886 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5391ac26-cb90-312d-8a35-099223ecc7ea | -4.39305 | -45.59028 | 2024-11-21 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 12003088-da1b-32db-bab1-d1609937fd22 | -2.61844 | -51.80975 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c52b92f0-5e66-3014-bc60-ff90cb40ab74 | -2.08175 | -46.2917 | 2024-11-21 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7576c1d3-7fc7-35ef-b124-9b89c18ef6a1 | -6.82963 | -40.34043 | 2024-11-21 04:08:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 718320ff-1e26-38c1-8e74-bb8c2541c189 | -4.03792 | -46.22276 | 2024-11-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ecd41e4-9d64-3eea-98f4-d81c1f63b799 | -0.86476 | -51.85109 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c480efc0-3770-3959-ab32-8f1ff83de223 | -2.18497 | -52.13192 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f401318e-659c-320d-bf5f-86d079d4d848 | -5.1406 | -39.80651 | 2024-11-21 04:08:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 75fb7b8a-355c-3837-bc99-b6116017c7cf | -4.06588 | -50.90128 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4806fc1d-fe29-33ee-886d-0110c1632d41 | -2.10233 | -46.62445 | 2024-11-21 04:08:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README16.md)
