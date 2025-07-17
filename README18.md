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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f011a724-034c-3893-babe-63c529881317 | -22.39174 | -49.79138 | 2025-07-17 03:57:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2edab96c-cdfd-3a28-bf96-bff8b40489a4 | -19.53528 | -49.67433 | 2025-07-17 03:57:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5492fe24-1566-3c25-8139-e0b45a0f5fcd | -17.15936 | -46.1145 | 2025-07-17 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dab6726c-65c2-37c9-a711-59c91da09cef | -22.69777 | -43.34649 | 2025-07-17 03:57:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8ad9d9a-905a-3129-93c7-f218362ff60a | -19.48628 | -41.97682 | 2025-07-17 03:57:00 | NOAA-20 | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8686f459-5eb9-3a88-86eb-6ca5298db145 | -20.18554 | -48.72746 | 2025-07-17 03:57:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2eb85396-e6ce-3d21-82f3-a54454897f56 | -19.81813 | -48.97042 | 2025-07-17 03:57:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed5f6dab-6e39-394c-a83b-b89b6994c311 | -18.40324 | -44.18917 | 2025-07-17 03:57:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cab2184-cb8b-34b7-ae72-ea28218613a8 | -18.84774 | -45.20481 | 2025-07-17 03:57:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34eca3a8-060e-3a9f-9e43-1fd83da46075 | -19.74745 | -40.6937 | 2025-07-17 03:57:00 | NOAA-20 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6e41816c-d365-3800-8586-c4e56080ea42 | -23.08767 | -49.73641 | 2025-07-17 03:57:00 | NOAA-20 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2f4fd2ad-6c79-3419-ae46-fa796fa36a9b | -21.08182 | -48.68541 | 2025-07-17 03:57:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 29f87232-6365-3d7b-bc47-87f5b5d5e79d | -23.06126 | -51.51647 | 2025-07-17 03:57:00 | NOAA-20 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e3adb0f8-7726-34a5-8e5a-5c172bc067be | -20.01171 | -49.04609 | 2025-07-17 03:57:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f4f0dced-9341-3344-9c9f-1a88f1014a0b | -20.99552 | -49.765 | 2025-07-17 03:57:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 80cb3a51-eb05-39e8-af68-978d5c1b7b3f | -19.96106 | -48.99155 | 2025-07-17 03:57:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 69babf32-81d5-365d-905b-a0de7aa3bdaf | -23.08869 | -49.73142 | 2025-07-17 03:57:00 | NOAA-20 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7e08621d-47de-3f64-b7bc-6b958f9ab85c | -17.35839 | -44.14077 | 2025-07-17 03:57:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7098ebcf-f3cb-39a4-ae8f-ec469bb95dbe | -18.91913 | -47.00521 | 2025-07-17 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc84f827-f6cc-3435-bf10-c3958a7044f9 | -23.18065 | -46.8395 | 2025-07-17 03:57:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 81399c5a-0dd9-3674-94b4-38ee37e9a4d9 | -20.99444 | -49.77025 | 2025-07-17 03:57:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 3543e94f-0395-329d-9b39-883056a74926 | -23.2793 | -47.70646 | 2025-07-17 03:57:00 | NOAA-20 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f9675250-a05e-3b15-8ba1-818a1078720a | -22.99831 | -47.1202 | 2025-07-17 03:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 223d5dd6-f51b-33d9-8009-bdc81c4b110e | -17.36197 | -44.14144 | 2025-07-17 03:57:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ff78f99e-b8a1-3952-8465-19abece0546d | -21.08091 | -48.68997 | 2025-07-17 03:57:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| cab38479-bf0f-38ed-b874-e36143627b41 | -22.95803 | -46.73726 | 2025-07-17 03:57:00 | NOAA-20 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4010149a-d060-3b57-ae35-ae80ba0a286d | -6.7194 | -44.3231 | 2025-07-17 04:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e4569132-014c-3503-8946-4e026a42483c | -3.3958 | -47.4785 | 2025-07-17 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 4f6bf76f-d86d-3f9d-bc27-cd76838176d0 | -5.6567 | -43.7161 | 2025-07-17 04:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 342.9 |
| 990168cb-63c5-37eb-8507-8dc456979ce0 | -5.6754 | -43.7147 | 2025-07-17 04:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 98584e19-2a54-3f0b-9ad0-88d13437fa3c | -3.3772 | -47.4792 | 2025-07-17 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 3802d316-58a3-3c37-97fc-07c57c9aafaf | -5.6565 | -43.7393 | 2025-07-17 04:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3a4ef995-ef8f-337d-9d5f-8d4d4def595e | -27.20877 | -50.66034 | 2025-07-17 04:00:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 92970a11-9ddb-3764-9647-bd758c81b839 | -25.11609 | -49.18835 | 2025-07-17 04:00:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fc76bc54-35e8-318a-a5bb-f5c5d4c3214d | -28.89668 | -50.13436 | 2025-07-17 04:00:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0131d8cf-7af5-304f-a2d8-ac2f1f3c4ba9 | -25.11601 | -49.18588 | 2025-07-17 04:00:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c8f42efe-99b8-3678-8dfd-bab9dc3db397 | -25.117 | -49.18388 | 2025-07-17 04:00:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8029d564-f9a6-32c9-84dd-351a0709cec0 | -27.07869 | -49.42963 | 2025-07-17 04:00:00 | NOAA-20 | APIÚNA | SANTA CATARINA | Brasil | 4201257 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b36ca288-76b4-3fdc-b305-ffc857620aa2 | -25.11687 | -49.18147 | 2025-07-17 04:00:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| abb9f198-4df0-3cfa-b902-961f23fb5ba6 | -28.22542 | -48.93065 | 2025-07-17 04:00:00 | NOAA-20 | SÃO MARTINHO | SANTA CATARINA | Brasil | 4217105 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 546b385f-b4fd-3094-8001-f1a43d8d85ff | -23.61673 | -50.77647 | 2025-07-17 04:00:00 | NOAA-20 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3c179e5-43ea-3d7a-bb9e-ae352c1336eb | -28.69791 | -49.88796 | 2025-07-17 04:00:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4969d2c8-cf89-37f6-8afa-44b06f04b8e7 | -3.3772 | -47.4792 | 2025-07-17 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8715161f-04a9-3b06-ad45-72707d88286a | -5.6565 | -43.7393 | 2025-07-17 04:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 71f4938e-acbe-3ea2-aee1-cb8b2ae6cc91 | -20.9993 | -49.7744 | 2025-07-17 04:10:00 | GOES-19 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| 4edab968-3eed-337a-afb8-6be04d730efa | -5.6754 | -43.7147 | 2025-07-17 04:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 680fcd5c-fc35-3cf7-8233-71ca51c137ff | -3.3958 | -47.4785 | 2025-07-17 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5c4cb977-9611-300b-9221-6669117e230f | -5.6567 | -43.7161 | 2025-07-17 04:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 330.7 |
| c00dcdfc-9549-39f5-ad85-2b9f7a229ff0 | -6.7194 | -44.3231 | 2025-07-17 04:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 69a6474c-ffa1-36ec-a64c-7aa002272816 | -3.3958 | -47.4785 | 2025-07-17 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e362f821-0399-3f11-88a5-4fd70df6d7ba | -6.7194 | -44.3231 | 2025-07-17 04:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7868bb9e-3ebc-3c03-a85e-005ea648a6de | -17.3628 | -44.1399 | 2025-07-17 04:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 4d1093c4-9fbb-32bf-9fd4-6e7155d6b5ed | -5.6565 | -43.7393 | 2025-07-17 04:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 961c9684-af9c-3ebf-b7a0-6be01d014421 | -5.6754 | -43.7147 | 2025-07-17 04:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| ea3c6bb9-69fa-3ba5-b0dc-2b6ed1fd1b2c | -3.3772 | -47.4792 | 2025-07-17 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| bc8bc0ab-809d-3509-a142-c722350c66ec | -5.6567 | -43.7161 | 2025-07-17 04:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 268.7 |
| 8a42d502-1bb3-35ae-806f-4342e4c10f78 | -5.6754 | -43.7147 | 2025-07-17 04:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 68786f38-1f01-303f-965a-65ff4a737a8d | -3.3958 | -47.4785 | 2025-07-17 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 8751579f-7f03-30a5-8eab-d86e9064b520 | -6.7194 | -44.3231 | 2025-07-17 04:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 76cc107d-c228-3672-be6b-d1cfabc3dc65 | -5.6567 | -43.7161 | 2025-07-17 04:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 252.1 |
| 561cc85c-3373-3f31-920a-221dba4abfb8 | -5.6569 | -43.6929 | 2025-07-17 04:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 57598c08-f3fb-3736-b735-7307ae728ee6 | -5.6565 | -43.7393 | 2025-07-17 04:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 9a693469-d2ac-3932-9c0e-860f95b0d25e | -17.3628 | -44.1399 | 2025-07-17 04:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ad6820ff-ec99-3a66-909d-73e6e4111491 | -10.978 | -46.4766 | 2025-07-17 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 485f7cdf-63e8-3fa7-a136-9e1a2dc2064b | -5.6565 | -43.7393 | 2025-07-17 04:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 36d25900-f49e-3b18-bfb2-d0f7ba52ab2a | -3.3958 | -47.4785 | 2025-07-17 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 75e0d933-c81f-337d-b916-6c77532f5af5 | -5.6567 | -43.7161 | 2025-07-17 04:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 229.0 |
| fd391301-284c-3ac4-b7b9-65baf5191829 | -6.7194 | -44.3231 | 2025-07-17 04:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 15c165ee-3a6d-3e07-8fa8-1c775f79cd43 | -5.6754 | -43.7147 | 2025-07-17 04:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 36e9a1d4-9f5b-3701-bcd3-ea7e16e49888 | -17.3628 | -44.1399 | 2025-07-17 04:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 104.2 |
| ea4ed081-6d7e-3ebd-b67b-92c01ed377dd | -4.4529 | -38.44606 | 2025-07-17 04:44:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 28aa33fb-cc10-398d-a559-4909f7916add | -2.58703 | -51.92105 | 2025-07-17 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9394e02-c339-3c4e-a7fe-578849ef3a62 | -2.44128 | -47.3247 | 2025-07-17 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d2ba49d-14c7-3318-a376-ecadbda31c86 | -3.84905 | -47.75543 | 2025-07-17 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac5299ab-064d-31b8-a4af-cea001b8454f | -3.54813 | -53.5728 | 2025-07-17 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93df9306-52a8-3e11-a901-5297c4877f0c | -2.91846 | -48.24747 | 2025-07-17 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41d092c2-fdee-3e20-b57d-1c8f805a70f7 | -4.80374 | -43.2239 | 2025-07-17 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a7538328-d686-3dad-8656-ac47cb893369 | -5.01701 | -38.53354 | 2025-07-17 04:44:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 75795974-9165-382a-9100-06badc197c4f | -4.10958 | -48.20825 | 2025-07-17 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| acfb673e-c518-3a36-b3c7-d43872388f67 | -3.8455 | -47.75491 | 2025-07-17 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d3880d8-2d4e-3683-9d65-5301ea763b3c | -3.54559 | -53.57349 | 2025-07-17 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef17bf36-0f66-3ea4-9858-0c5e9be52436 | -2.91273 | -48.2389 | 2025-07-17 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| adb90189-effb-3b3c-8ac9-e228a675454b | -2.47617 | -47.20719 | 2025-07-17 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bccb13df-3bdd-39e2-8b9f-17093462d7d3 | -3.99528 | -43.22873 | 2025-07-17 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d843fda-87df-3d39-8aca-6cf5ee748531 | -3.04809 | -49.42939 | 2025-07-17 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6075761-297b-3b7f-ac28-6deabfba4d64 | -2.44422 | -47.32932 | 2025-07-17 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ef9dcdd0-e87c-33a4-a505-ed018686d422 | -2.66191 | -47.39805 | 2025-07-17 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 06666b3a-659e-3688-bb25-04d073442542 | -3.66892 | -48.31626 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 880cf37a-a4d8-311c-abab-e9beda120e7f | -3.39427 | -46.90694 | 2025-07-17 04:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7635e7d2-c339-36b4-9db3-96b991a504f1 | -4.28719 | -48.06332 | 2025-07-17 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcdc288e-cb0c-33fe-8407-dca298d0e077 | -4.11016 | -48.20442 | 2025-07-17 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d109d51-9936-3052-8f18-25d139ea8dc6 | -4.11101 | -48.72683 | 2025-07-17 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 924e483e-4f23-35ff-8015-8b9d1393b875 | -2.91559 | -48.24318 | 2025-07-17 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90a66271-9092-3fa9-aa81-67e1bf2bdddc | -3.04143 | -49.42836 | 2025-07-17 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11fa9637-62d2-3d32-a4c1-27c4568e4395 | -3.38512 | -47.47532 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 0a158850-be9b-317c-88f3-2529d377b176 | -2.58646 | -51.92467 | 2025-07-17 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d23f107-caa2-3d44-ba7a-bea4914a0443 | -3.4064 | -47.50356 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0514d59a-46e2-3e6c-a5bb-46a60d74bf06 | -4.80987 | -43.21848 | 2025-07-17 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37893ae7-5fea-36ca-9be7-70e0f33123b0 | -3.02422 | -49.4293 | 2025-07-17 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17c0ef78-58dd-386b-a1a4-23acc3aaae2d | -3.39924 | -47.50249 | 2025-07-17 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README19.md)
