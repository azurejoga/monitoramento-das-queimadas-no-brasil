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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f4bfe91-e48f-39b9-9cc2-104d4ffa559f | -3.0931 | -53.2514 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6abae0fc-f57c-3581-96cd-3264329ef882 | -3.08864 | -54.13265 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 476c76c1-2e6c-3dbf-9f67-ffac4306b91e | -3.67464 | -53.55429 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a38def03-04d6-39b6-b2e6-f0b7caf80628 | -1.78265 | -52.73957 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d94d48fe-c3f6-30eb-a3b8-7bd0c7235bc2 | -3.68791 | -50.22898 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1d85f2ef-ed65-353d-9cee-67e5943c8943 | -1.66756 | -52.71407 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e31bde13-a2fd-3a86-9f89-212b98790c68 | -3.0993 | -53.24844 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 25ad3eb7-e7f3-3a1f-8376-13408e0ab5a9 | -3.90396 | -50.60049 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ffbfe83c-457f-3756-9028-e2e2c9afba9a | -3.30869 | -53.75077 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27a48417-db57-3db6-acb0-7d0ca4576348 | -2.98185 | -60.98238 | 2024-11-27 05:35:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1206ab6-f623-3f2d-979f-74fc0edfccd5 | -1.06308 | -52.42178 | 2024-11-27 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11db4192-6b7c-3467-ba2f-fc5741bf02e3 | -1.39668 | -53.5518 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7ee256c-d5a8-38a9-97fa-71578f8b49d3 | -2.89474 | -51.38488 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e9c681d-c4b2-3dd5-a81d-af7dca4efe85 | -2.1858 | -53.7785 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 17f07080-162d-3d66-a5b1-24983292f77e | 0.65322 | -50.82759 | 2024-11-27 05:35:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b2f1de9-4028-3e33-ab2c-77fa8b98d9e3 | -3.12012 | -53.10516 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58772987-604f-3c5a-a165-d36b8f909d2a | -2.24098 | -53.63293 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec008fcc-8815-34c6-bf06-298dc9ae8ede | -2.80569 | -53.02119 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cbb366e-fe7b-3cf0-8908-6a7fa82381a3 | -2.24333 | -53.62973 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74df5e5f-ec89-3018-b8ce-d99f16caaded | -2.96251 | -53.72072 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c54aa38-6031-3f2a-bd4a-80e60d93b6cb | -3.1083 | -53.26576 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce3b95d0-b298-3b81-b944-11c3aa261ad6 | -3.08378 | -54.12867 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c8f0468-c040-3e45-8d03-298f9804467d | -3.38139 | -50.10554 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7fdf00bc-0c26-3fd8-9f95-11e726054c87 | -3.2324 | -50.67863 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c657a9a-1295-3878-bc95-6d0d692175d4 | -3.66959 | -53.54975 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47adde36-c11b-325f-9365-f9975ef90823 | -3.24616 | -53.63462 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7ca92ff-3015-3357-b816-91582f293b35 | -2.24695 | -53.63026 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b5dd616-f4c7-3e9c-8910-6d9c70532fcd | -3.11448 | -53.26293 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54925ed9-dd10-3dfa-990f-49fc6b492093 | -2.77364 | -52.90872 | 2024-11-27 05:35:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4726b31e-dfa7-3a4a-8acf-afc4b13dec80 | -3.71555 | -51.79914 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a9806ec-923a-3e66-8e84-a18588928d10 | -1.99308 | -53.29336 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdbb0b56-31f6-3053-8c45-489b7341e8a8 | -3.50244 | -50.49142 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 05618c3c-cf6e-3532-a33d-ca3fc43e41f6 | -1.98755 | -53.29248 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1029c68-5b47-30a4-a195-f04446b84348 | -3.24857 | -50.6157 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 499c9ac9-76e1-32de-8f83-be4e482c31fe | -1.7935 | -52.74534 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed0464ce-3d35-3039-80a9-b2f5b5a51029 | -3.5016 | -50.4973 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7759fb0a-ac67-3bd3-acb0-b700fd99727b | -1.79862 | -52.7502 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf4d195f-e41d-3026-a584-76715b9a5435 | -2.83263 | -54.11852 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 75d9fd94-4c15-3ec0-9029-907eae796768 | -2.94039 | -54.79472 | 2024-11-27 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32d99dcc-013a-3fbc-a99c-085d85e2692c | -3.75791 | -51.58992 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e9921d7-6476-3eec-b463-9972ff08fac8 | -2.83071 | -54.02954 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2c9ae53-da5f-3f55-82b4-3384b579e7b5 | -2.2586 | -53.75256 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 584d7504-4e61-3bbf-a1d3-d953e98daab1 | -3.71486 | -51.80399 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65723bb1-ddfe-3877-9050-142602547dfa | -1.71884 | -53.6078 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b048cd9b-849f-330d-8f6c-7f8b51da5e8b | -3.09423 | -53.24362 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 679e4bb5-fe91-31ff-9bb2-87f4ce34a382 | -2.80365 | -52.91433 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 143fbdcf-7f33-3b9b-9ec0-df3c187e5b1f | -1.04466 | -51.73969 | 2024-11-27 05:35:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f05e0233-b041-3c7b-a6db-7b0db5048ca8 | -3.25435 | -50.62264 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b621bb8-2bf1-37da-ad35-afb63d5e060a | -3.33017 | -53.71809 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 423abfd0-6fda-38d4-8e05-401fdfd502fc | -2.82448 | -54.10663 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c10558-9785-39e5-a020-d97af18788ab | -3.09986 | -53.24458 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71c8b27c-df66-3131-b198-0f63367b0942 | -3.53385 | -52.15654 | 2024-11-27 05:35:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 030881e4-f1ed-31d4-8a8d-34189c081b6f | -2.95213 | -53.7155 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 976b053a-feaf-3c3e-8eff-c5765939036a | -3.10942 | -53.25811 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1a27d115-561b-3dc1-8990-b9fe1c62fd65 | -2.89057 | -51.38707 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a4b6996-45ae-31ec-9360-f0591e795e80 | -2.8384 | -54.11608 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c632a3d0-7701-3862-a05a-b3739add217e | -1.60765 | -52.75105 | 2024-11-27 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b25bd77-1873-3191-a93f-f7afd064abbf | -3.09026 | -50.36156 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 485c2297-5e5b-3b95-90b4-d589f4fb3b56 | -2.82308 | -60.11188 | 2024-11-27 05:35:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5842fff1-879d-3e6b-a070-5f283b86874a | -3.51485 | -50.3063 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f1df4cd-9b06-322c-85d8-2c9dde475518 | -2.62048 | -52.53685 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd72ea27-c008-3705-9c55-72cae84fac5c | -1.84376 | -60.00249 | 2024-11-27 05:35:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b0036de-a978-3681-8a47-59d0a20436b5 | -1.38661 | -53.62014 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f00b112-3a54-39e6-a334-ad7567653e18 | -3.10289 | -50.36977 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1fad377c-8fce-36d8-94c8-3fe339a56e70 | -3.59704 | -50.36359 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9e1df5b0-17df-3fd0-9f7b-6cd10cf23980 | -2.16296 | -54.47168 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 274d264e-5b87-350e-9cd9-353ce297ed25 | -3.10885 | -53.26198 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 6312c6d9-1fea-3a03-a1c3-3c3015ca839d | -1.45246 | -52.59551 | 2024-11-27 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e28c9561-513d-31d7-bee6-a3c5424ace00 | -2.26023 | -53.46964 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa48b1fc-c297-3d2c-a4da-7e4fd40c7f1e | -3.7501 | -51.59943 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06c1b198-2539-3cea-850a-4850b89e83a7 | -3.10436 | -53.25326 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| aff2420b-9647-36d7-9c0c-5f464a134530 | -3.09873 | -53.25233 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 58dfc685-46fb-3bd7-abb6-c49d0189e6f1 | -3.72282 | -50.182 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af682769-1d79-37c2-ba63-1a89af2b5d42 | -2.59711 | -54.25825 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0178cee5-5af8-3b43-894e-797fc46bfeb8 | -2.2591 | -53.74913 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 38540100-2bea-35cb-9e0d-1b3408490210 | -2.33648 | -54.38219 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2c45e16-0206-3bf5-828c-c0795075d38f | -3.78601 | -50.13447 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 482e8a3d-beb0-30e3-bdc5-1cb00a61e27b | -2.89127 | -51.3821 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e55bdb2d-7f44-3914-b4ac-4c77bf5017bf | -2.82119 | -51.79353 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8eed1a0-d4d5-3bdf-96ec-81d49d00e91e | -3.2477 | -50.6215 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b5b7423-9599-3dd2-8b56-18fbea5c7bb2 | -2.83168 | -54.1251 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b4ca3912-a394-35b7-a170-d1e36926c861 | -3.23022 | -50.31915 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43c5a1eb-09d1-3ce5-ac9f-16f437f211e5 | -3.10999 | -53.25423 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8a20913c-9df1-33e5-864a-760e41c6304c | -3.09704 | -53.26393 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86999736-b38f-32c2-964b-ec5f63a154d5 | -3.09367 | -53.24746 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d57754cb-bb9e-3f71-bac5-0b9932a3a975 | -2.84508 | -49.40533 | 2024-11-27 05:35:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 429cd204-82d5-34be-928a-6551bca9f72a | -3.52839 | -52.15107 | 2024-11-27 05:35:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 218e7770-bb2a-34e0-936c-188221fdbbf9 | -2.42652 | -53.84576 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e832e3d7-d3fa-34eb-9233-e80bc48e3cb3 | -3.45224 | -50.29758 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2232397f-30f4-32f8-824a-446b4732a7f1 | -3.59318 | -50.35537 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 308fc0f0-4754-33c2-8682-bbff075b1165 | -1.68937 | -52.60723 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7195f071-5c83-385a-8b96-2aa0694b30d9 | -3.52772 | -52.15587 | 2024-11-27 05:35:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 213f9c4f-3490-30fe-9492-174b4d34e110 | -1.763 | -53.62392 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a43192-b4be-3db5-bb89-32d301f185c7 | -4.22704 | -50.85614 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b76ed66e-9c8b-3738-a248-8f22f3a616e9 | -3.38049 | -50.11205 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c5e70fd-0933-3bfe-aa79-c209fd171f27 | -3.38105 | -50.10456 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 686d2f8e-dd43-3d20-9d67-40d01caa4061 | -2.77424 | -52.90471 | 2024-11-27 05:35:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c62ebbe8-e5f6-33a1-90c4-d5976d12c1eb | -1.35947 | -54.63515 | 2024-11-27 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 947a8983-48ec-3854-8a37-9bf209264744 | -1.4467 | -52.59472 | 2024-11-27 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 701d52f1-720e-38e7-a5d1-d21dc8bbcd9b | -2.80512 | -53.02513 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README78.md)
