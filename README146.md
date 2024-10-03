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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c96969c-939a-3f48-8eb2-d356d7497187 | -19.69466 | -56.49403 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2cb41b19-5c8a-3979-96f9-d728c84ea29e | -19.65943 | -56.46935 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 627d269e-d1dc-30e4-8191-8d3cda7e471d | -19.65608 | -56.46874 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 134934e8-ddb3-3308-b96b-bbda162ed6eb | -19.65548 | -56.47245 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9cb33ddb-1d95-3cc2-a2ae-d28ab394f76f | -19.65213 | -56.47185 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9e6ba560-b689-3c56-b271-ecc764d9469e | -19.65153 | -56.47557 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8d2e11e9-bae7-3c1a-b5b5-3aa98cffb6bc | -19.64039 | -56.56551 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ef58e89e-cdc3-3376-b104-31a679d940fb | -19.63704 | -56.5649 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4a45d211-5e1f-3219-8738-12596704ad73 | -19.58097 | -56.5279 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| da4e7023-8887-37dc-8af0-b5523df80651 | -19.58036 | -56.53162 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 80b957e2-612b-3c92-98de-41f41c510d55 | -16.55202 | -57.41157 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 2282af8c-c58a-3083-8426-a26e28bdbca3 | -16.45759 | -57.30856 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| af7a71d7-e051-3b91-9055-0085751f6337 | -16.45258 | -57.44475 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 70be5975-1df1-30ef-82a3-a26f8544d776 | -16.44906 | -57.44412 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 65c2c97b-bb12-3c7b-bdc5-ec5c38003fcd | -17.03484 | -58.04015 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 06beb447-c468-364a-a6ca-caa3a0a8b32e | -17.03054 | -58.04373 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7985ed2e-3e0e-3e13-bdac-efd31574b170 | -16.92099 | -57.70568 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d0fd82b6-3c61-3a4c-a9bd-ac7d5e2e559b | -16.91745 | -57.70503 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d7e4af65-48aa-31e3-9fc3-724267ded1e6 | -16.91392 | -57.70438 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 289c981b-e99f-3f88-a8bf-c76e0ec14d02 | -16.9125 | -57.71261 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1d14bcd7-a5e8-3615-9840-6c3b3e7de901 | -16.91109 | -57.69961 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 58002839-e0f7-3d1f-a5f2-ead538598b07 | -16.90403 | -57.6983 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 148297ae-01e1-3027-8586-7fc620d570c6 | -16.90259 | -57.72779 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 93f34a1c-b13c-33dd-b127-1c2f878d4cdf | -16.89905 | -57.72714 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d97e440c-256e-3afe-83ba-7009e3b15e5d | -16.89277 | -57.68505 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 45921478-5f92-3e38-b7ee-37277a5db586 | -16.89203 | -57.68336 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 789595e3-d617-32ae-b145-480c4ff76b38 | -16.89132 | -57.68747 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2e65f71b-7994-3186-9674-9eefa2722c95 | -16.88778 | -57.68681 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5114e98f-c753-39da-bf4e-b2e984a033c9 | -16.88571 | -57.68373 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7a5258c0-f492-3ea7-b67f-60e2e31e93c9 | -16.87302 | -57.69411 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3b395120-ad1f-36c8-bd9e-663507be919e | -16.82285 | -57.77436 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2fecfc34-8cfd-3c92-ac11-f70eff8672a3 | -16.78441 | -57.82735 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2982e603-4a60-311d-a40f-b9fedb73215e | -16.78369 | -57.83152 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fd278f95-3774-3b09-94d9-41d1a550ac3b | -16.78086 | -57.82668 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 413c0a8c-ea74-3dae-a68a-d0fcf1272c0b | -16.78013 | -57.83086 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| f6fb299b-2835-3d39-b5c6-38bcbae7bcf8 | -16.77461 | -57.75687 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 611072b5-8c61-3dbe-9589-35d3224554e4 | -16.7739 | -57.76102 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2ab6b366-009b-3eaf-a5e5-16233fc57982 | -16.77018 | -57.82471 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 642e4793-2469-32a4-a616-5780e097318b | -16.76735 | -57.81988 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6e2045bf-4efe-34ff-8310-37e71f4690a6 | -17.1857 | -57.3843 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 0bffa076-9032-31c8-b055-46b37068cffe | -17.18502 | -57.38829 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 7e04bf41-71c6-36cb-b7d0-72de57d06bb7 | -17.1829 | -57.37967 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 25db3a80-a135-31b9-88a6-f599ebfc3c63 | -17.18222 | -57.38366 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 11f820b5-7ce3-31e8-838d-5023302cd527 | -17.18154 | -57.38765 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| f6bb6e86-fe57-3388-9faf-0d367812194c | -17.17942 | -57.37903 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| ea5857cb-61ac-32b7-868f-e97432bc680a | -17.17874 | -57.38302 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| debd4214-52a7-3285-ae5c-65589fed089f | -17.17806 | -57.38701 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 8ce076fa-f52f-3f39-a47c-366f60da69f1 | -16.77062 | -57.46559 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e3074edf-00e3-3f09-8b19-85a9ce1f0033 | -16.76994 | -57.46963 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e14b446e-74df-3aa1-b503-480a6fd6c76a | -16.76788 | -57.48177 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f233b15e-05f1-3cb9-9d41-36ad48e5dc70 | -16.76575 | -57.47303 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ec7b559a-f2ca-34cf-857d-88598f8318c3 | -16.76567 | -57.45219 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 742299ff-965b-3820-b48a-af9907ca1f27 | -16.76506 | -57.47707 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| afae074c-5af0-36a2-b4e6-3c26924c9fd5 | -16.76457 | -57.3525 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ce316485-b43c-34f6-abee-08a21a87d515 | -16.76389 | -57.3565 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7b03cc97-3ff0-35db-b910-5d0ae57d3434 | -16.76321 | -57.3605 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d8ee6539-8adc-3622-a215-f63a579f0482 | -16.76285 | -57.44751 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b044e4ed-9425-37e2-b36a-bb74d3987132 | -16.76155 | -57.47643 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d4f640e7-7a8d-3623-a054-c771e3606710 | -16.75972 | -57.35986 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b7c378ca-d74d-32b5-baca-ad10fa900fe9 | -16.75942 | -57.4677 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c7e60a1b-e900-3fbd-ad72-5a94425d2b28 | -16.75934 | -57.44687 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b032b304-c9d3-323f-8d46-f577770e5774 | -16.75873 | -57.47174 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a26c182e-9fe2-392f-86b0-39f0cc5ae45d | -16.75682 | -57.33458 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| cac20159-cd75-3c30-bd3c-df8d26db0c44 | -16.75614 | -57.33858 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ec5611cb-7610-348c-a6aa-ede712effb2e | -16.75591 | -57.46706 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| daf68baf-c137-3a25-9c87-7d66bab7d74b | -16.75584 | -57.44623 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 49d871f1-8c23-3ed2-acd2-27754b282a61 | -16.75546 | -57.34258 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0351b982-6c95-3160-8211-497dac1fe999 | -16.75522 | -57.4711 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e02b8605-98fd-3149-a80b-7f3175e546b2 | -16.75478 | -57.34658 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 151b9409-bd41-3bb6-94f6-61adf8157eda | -16.75334 | -57.33394 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c4eb11f4-d3b7-36ac-a2d7-88c520f3cd49 | -16.75266 | -57.33794 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a69291d6-b507-33e4-b7bb-cdca01e289d5 | -16.75241 | -57.46642 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e875f885-ff93-301d-a8c8-51b03a2cf4eb | -16.75197 | -57.34194 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fdf3763a-9609-3dbf-bfe7-3ad86d0d2ce2 | -16.75129 | -57.34594 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4836d108-6dfc-30f4-81ae-5a817d18b760 | -16.75103 | -57.47449 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 621576c7-7348-35a5-b44e-20e46ba43b45 | -16.74985 | -57.33331 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 449198b4-9cd0-36c0-a162-b5d168a86095 | -16.74917 | -57.33731 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 3995354a-3710-3302-9a27-aadce993a3b9 | -16.7489 | -57.46577 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f7aca184-760e-3785-a789-ece0b37ed3b1 | -16.74848 | -57.3413 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 0112141e-cad6-3493-a06b-4e781b508aee | -16.7478 | -57.34531 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| abd64728-8e58-39b2-b3ed-0507f4b9439a | -16.74636 | -57.33267 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| dc4904a4-bf35-38fc-8640-8f69d496d072 | -16.74568 | -57.33667 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| bd478c4d-6a25-3f22-a436-d01605ca89f4 | -16.7454 | -57.46512 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 36c65d69-6f36-38c9-9d5b-ebea845ed4e9 | -16.745 | -57.34067 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| a3c60e14-5eb9-3011-b253-0e25adbbd1f5 | -16.74471 | -57.46916 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0649543e-35a9-368f-9d90-2eca1ead28eb | -16.74465 | -57.44833 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 6dbd873f-46bb-3b62-95e5-721dbc014790 | -16.74431 | -57.34467 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b3ab436f-475e-3adc-855c-dcc36e045851 | -16.74402 | -57.47321 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6f74013a-7931-349d-8c85-1b1d4906da78 | -16.74396 | -57.45237 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e14b043b-1f8f-3b0a-9ad8-b283c9df5e5f | -16.74327 | -57.45641 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e1c344a6-0ffa-3f80-b961-af19a036b2a2 | -16.74287 | -57.33204 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3c659e67-25b5-3025-9701-19464a25e06a | -16.74219 | -57.33603 | 2024-10-03 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 020d9cee-b5c0-3c6d-a53d-83803bc4277e | -16.74114 | -57.44769 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| be561bb1-d6ba-36ed-8b64-de3fcf9d8a55 | -16.74051 | -57.47256 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 775247ba-83ae-3aaa-91cd-8c9fa91e3812 | -16.74045 | -57.45173 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 88d51b9b-88d9-3ea6-b005-582852e683e3 | -16.73976 | -57.45576 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 94a71296-622f-3eab-86d9-b03c369939f1 | -16.73838 | -57.46384 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 6a51eabf-4ae7-334c-97ba-4e38d9ed0d56 | -16.73769 | -57.46788 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 806f0abb-8498-36fc-81fa-61087044464f | -16.73764 | -57.44705 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e860bee5-2f68-342d-8b1a-70df5f39642a | -16.73695 | -57.45108 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |


[Clique aqui para ver as próximas entradas](README147.md)
