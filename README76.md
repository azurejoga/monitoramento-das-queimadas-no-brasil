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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c915484-481c-3373-adc4-05aabe879738 | -5.84458 | -46.23409 | 2024-10-09 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e578dd48-3224-3751-98ce-151db50220c8 | -6.34287 | -46.32713 | 2024-10-09 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e94689fb-6d20-3595-b0dd-6931b158d725 | -6.32538 | -46.38908 | 2024-10-09 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2439c4a8-2d31-3dad-9b9a-7b42a535bf69 | -5.8482 | -46.23468 | 2024-10-09 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 174c8607-db40-3434-9f95-3ce4f113b6e8 | -5.59631 | -46.37184 | 2024-10-09 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 857f5014-557e-3d30-9a8b-0000069a25a2 | -5.57966 | -46.31249 | 2024-10-09 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3915a423-9e1c-3b6d-ae83-48e4217fe488 | -5.53812 | -46.20147 | 2024-10-09 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f254c0d0-2780-3d7d-9781-40227d1622db | -7.7318 | -46.60395 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f12f304-4dc9-31cc-817e-5d6cb729a775 | -7.72656 | -46.73258 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e597853a-847c-3880-b22b-94deef4fbd0d | -7.58771 | -46.63764 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b715dcd2-54bd-322e-ac58-d86362b75be5 | -7.58701 | -46.64189 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8534945f-e986-36c3-b61e-23ecfb3e9831 | -7.5067 | -46.60399 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b24f17ad-7852-314a-9750-35d3c6213918 | -7.48479 | -46.6699 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 362d0df5-fd60-3b3f-bdd6-ac980e4c262c | -7.4841 | -46.67415 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98edf984-e041-33c3-9d91-812c27a345e8 | -7.37049 | -46.07897 | 2024-10-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caf9d52a-a19b-3f80-afc6-af2b7f55054c | -7.25861 | -46.33889 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7cff26dc-d560-3289-af47-1ebb817c1d35 | -7.02004 | -46.59761 | 2024-10-09 04:14:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c1e18f2-8018-3bbc-9c01-57aa4c736e95 | -6.68886 | -46.41388 | 2024-10-09 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55b10689-ba53-3127-9fca-4c25bf0b2939 | -6.66427 | -46.33699 | 2024-10-09 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50365b74-ccf8-3495-8b18-5e88b0e3834e | -7.10329 | -45.27344 | 2024-10-09 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1e987f3-e6b7-3674-a848-df5df2231511 | -7.06751 | -45.4492 | 2024-10-09 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48ad7bc6-0af6-3835-afed-4c626c3e6802 | -6.99066 | -45.38261 | 2024-10-09 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b5066bf-60c5-3bc5-b54b-b57d2d133987 | -6.98784 | -45.37829 | 2024-10-09 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24de6bc4-dd14-392e-be10-6189ad9a0eff | -6.98723 | -45.38206 | 2024-10-09 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb8dcf38-8aea-336a-ac12-f23046632f09 | -6.98661 | -45.38581 | 2024-10-09 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 232e8ba9-33ee-30c8-a5b7-cd0e77ab8070 | -6.9655 | -45.2779 | 2024-10-09 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c4f2088-0f93-3212-a884-8f41e55535d7 | -6.96208 | -45.2773 | 2024-10-09 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae269f1f-a1ca-30b2-a609-646e9e6f987b | -6.94876 | -45.22895 | 2024-10-09 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21a4448d-9e92-3ae7-b0b5-f14f206c21df | -6.94596 | -45.22459 | 2024-10-09 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 962ce914-ae4c-39b5-8e86-a02f714c4794 | -6.94535 | -45.22836 | 2024-10-09 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 195eec82-f48e-34dc-857e-c07f7d501a65 | -6.69031 | -46.41293 | 2024-10-09 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0ea252b-6cef-32be-8d2e-685cc99805ec | -6.66718 | -46.34181 | 2024-10-09 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 120b37eb-99fe-3955-abe7-2a3005f71791 | -7.95039 | -45.9039 | 2024-10-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 059a8ac9-0c5d-3ddd-b16f-83f5d00220ec | -7.74239 | -46.58421 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f035c5d3-0c1f-3e52-af52-0be5ca5ca3c5 | -7.72573 | -46.73292 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec6fe6d2-a833-3acf-b3f6-6edd9679cd49 | -7.51102 | -46.87521 | 2024-10-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6070bca0-b692-3648-b76a-e306118efbe7 | -7.22383 | -45.52829 | 2024-10-09 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aa5dd58-65f1-3ed3-ae64-6a4b23daad3f | -8.26755 | -46.86726 | 2024-10-09 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80a9d5a8-7896-3664-b93b-7c58ab0d1743 | -8.26394 | -46.86655 | 2024-10-09 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcc0f452-a679-32dd-94eb-808dc94be5bf | -8.24747 | -46.2896 | 2024-10-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 31c20056-9f22-3649-b408-0faee2d68ba0 | -8.2446 | -46.28503 | 2024-10-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0729887d-cc90-33f5-8461-51050fee3355 | -8.24107 | -46.28448 | 2024-10-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fa158341-c7d7-3abc-922e-47e2315c9ad0 | -8.23947 | -47.03471 | 2024-10-09 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f1c5899-d3b3-304f-9efb-4269d780470b | -8.2343 | -46.92895 | 2024-10-09 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df7801a4-f219-39a1-bfd8-29363e8536a5 | -8.67656 | -47.00526 | 2024-10-09 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de7cc046-8c87-35e9-af6f-7727572d1204 | -8.37561 | -46.30548 | 2024-10-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 965583e6-b2e4-3a24-a13a-3a331ae41dda | -8.24394 | -46.28902 | 2024-10-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 61352d5b-5b6d-3899-b92a-56009114073e | -8.23499 | -46.92755 | 2024-10-09 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 892269a8-eec7-3bbb-a415-d5d0c4ea5226 | -2.19104 | -46.07799 | 2024-10-09 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c63dfa0-0ec2-370d-add4-9283e7333d1d | -1.77802 | -45.66532 | 2024-10-09 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d47ec205-af8b-3d40-82ff-2ed4544ab9ca | -3.36515 | -46.5049 | 2024-10-09 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0e7f909-1b5f-3a4f-9d14-c735596a56a9 | -3.36213 | -46.49952 | 2024-10-09 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 748a1f1f-4da2-3c96-88a2-07bcc914fb66 | -3.31537 | -46.98904 | 2024-10-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac3832d0-898b-39b7-81dd-8fe2275b9870 | -3.31375 | -47.02444 | 2024-10-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c52aa24-d00a-339d-88bd-7656f73c1eaa | -3.31146 | -46.98841 | 2024-10-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27ce5c2a-660f-3fd5-99d7-0689e5d3f8fc | -3.30983 | -47.02383 | 2024-10-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 439abffa-8ecd-3281-967a-0ed1d7e4ec3d | -3.11975 | -46.65432 | 2024-10-09 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e37151a-3cae-3d35-9ef9-914fe2c12666 | -2.71554 | -46.81289 | 2024-10-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd9e7864-7f6b-3d57-85d6-c5d86109b537 | -2.64594 | -47.36694 | 2024-10-09 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7fd8122-e30c-3539-8ff2-7e002df85c73 | -2.6073 | -47.34497 | 2024-10-09 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7c4d1a5-41ac-3934-98a4-233fb3ae3995 | -2.53974 | -47.22584 | 2024-10-09 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c613d919-b362-33e7-a7df-ae040b64892f | -2.53917 | -47.22932 | 2024-10-09 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0fec6b3a-0bdf-3551-ad4f-05093f84d4d1 | -2.52959 | -47.22766 | 2024-10-09 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dd85008-a657-325e-99fd-479489c758d5 | -2.52557 | -47.22705 | 2024-10-09 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4182f65-cdac-3166-8d41-8fc3887e2db1 | -2.3651 | -46.49171 | 2024-10-09 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be78ecfe-08ad-3dac-bf51-36921adbfa8c | -2.36433 | -46.4965 | 2024-10-09 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba0f7477-8825-3962-a36b-244bdd1fde99 | -2.34463 | -46.84378 | 2024-10-09 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1d93be3-e764-3a4e-beca-e65c41d257af | -2.32375 | -46.72352 | 2024-10-09 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 147fcb4f-ac3e-3b14-8e1c-96bf01efc66b | -2.32296 | -46.72844 | 2024-10-09 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8745fd7b-49e2-3641-b89a-958ea8273262 | -2.30151 | -47.24513 | 2024-10-09 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 514758d7-1f9b-37b2-8210-381ec9a4541c | -4.01145 | -46.54343 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 691015c6-a2f4-3d14-b977-6b8ab3d164c1 | -3.94074 | -46.45024 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 8b563533-ecd3-3f4a-989d-3d39c888a017 | -3.93469 | -46.43999 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74cb452e-874e-3057-8f52-109979e280d4 | -3.93396 | -46.4445 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9399519-9cb6-31c5-bd21-8781ed7276e8 | -3.93324 | -46.44902 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0987679d-4afc-3274-a8c5-11913569cb13 | -3.93093 | -46.43941 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 459ecaf1-c7f0-3845-b8b8-334a694bdd76 | -3.93021 | -46.44391 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7121343b-c5f6-3fcf-a343-875198f5b241 | -3.92949 | -46.44843 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 21cc924f-5ddd-3e25-a887-c095ef075c03 | -3.92876 | -46.45295 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 916bd639-600f-3edf-8de6-37ea2c35a5ef | -3.90926 | -46.45457 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| eb32a2f7-350f-3497-adb8-1d85d7aaa4ce | -3.90404 | -46.46299 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 459a40b5-b6e1-37da-8861-9cde0e547007 | -3.90174 | -46.45341 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5012e1f4-9b71-3567-831c-343aeb9d0092 | -3.89727 | -46.45726 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e0061a51-1dd7-37d8-a83a-86ce14c594ca | -3.809 | -47.48981 | 2024-10-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99d446f9-d679-330c-8d06-9b06f0c42201 | -3.70343 | -47.59573 | 2024-10-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ed58aa4-971c-399c-8499-7db9de74aa8a | -3.70285 | -47.59927 | 2024-10-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82eec333-c8b8-3bb0-8ef0-46f0ad493316 | -3.70226 | -47.60283 | 2024-10-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b556d680-f81b-355a-8d31-a97b779f4a4a | -3.70168 | -47.60638 | 2024-10-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 383e8ffc-69a4-3909-b455-79f0f0e70df1 | -3.69939 | -47.59505 | 2024-10-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99dbd0c9-bb90-3e35-91b6-f948f680c0cf | -3.69881 | -47.59861 | 2024-10-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d14f177f-6fdd-348f-9325-9349c79d7044 | -4.73537 | -46.65569 | 2024-10-09 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f13525a-71e1-3970-9400-2d1f8dbad464 | -4.73464 | -46.66015 | 2024-10-09 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49768839-071d-36a3-bf5a-72325c077725 | -4.7339 | -46.66467 | 2024-10-09 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a93c6ef-9c18-38f2-8c96-675b68b6bcda | -4.52556 | -46.60776 | 2024-10-09 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9bfb698-d07d-39ca-befa-96e4e3d4f746 | -4.47431 | -47.73586 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 871c8122-a9b5-3d49-8a12-3754ddd031dc | -4.32054 | -47.70753 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e91d3cf-6545-36fe-a1c4-0a91de2572a3 | -4.31711 | -47.70328 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82659372-ff1f-333f-88e1-8a93a50b428e | -4.21104 | -46.84854 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1518d19-44b1-3ee1-8a13-ce28ae1777c1 | -4.01219 | -46.53885 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18af90a3-c441-33d4-96d3-3ea532b28703 | -3.94 | -46.45484 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |


[Clique aqui para ver as próximas entradas](README77.md)
