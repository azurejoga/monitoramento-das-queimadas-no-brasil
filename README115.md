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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bd7fdfd-881f-302c-b2b3-937e3583952e | -2.09608 | -48.89772 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 91649ce9-f302-3cc9-90e6-852ea5320054 | -2.68344 | -51.82548 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 3799f6ef-3acb-3ac5-ad38-0e2e49da2dfb | -3.22247 | -50.30414 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ec886d15-d53c-3e4b-bd30-3dcbdac4b138 | -2.87247 | -50.40439 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 36d15af6-a7ed-3915-a2e4-dea12323a8c4 | -2.54624 | -47.12018 | 2024-11-09 05:33:00 | AQUA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ce11018b-aaea-31e4-8685-025d99c50cee | -3.04643 | -48.03867 | 2024-11-09 05:33:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4abce10b-ce02-3c1a-b911-2b918f657a23 | -2.25017 | -53.67322 | 2024-11-09 05:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c6418475-7a3a-38bb-8334-89b1a6c8f0c2 | -5.2551 | -48.08257 | 2024-11-09 05:33:00 | AQUA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c8719692-53c2-3447-b506-a43723b414f6 | -3.3508 | -50.12329 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 15b7e1a1-54a9-3c77-8ffc-4fc38b92379d | -3.63939 | -50.17446 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 90835462-ee4c-31e6-8a1a-149703b3fc38 | -4.20842 | -48.53993 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 812aec6d-a41c-3f7d-b86d-ee55962f2478 | -3.28309 | -53.66936 | 2024-11-09 05:33:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 277402af-437d-35db-841c-5cd527e4afd8 | -2.40016 | -50.30761 | 2024-11-09 05:33:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e78e683b-f5f8-3687-b243-9fb0b5863bb2 | -3.50149 | -51.02961 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c5c5954e-9437-3968-bb03-59e68adb9bee | -5.19977 | -46.19139 | 2024-11-09 05:33:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4a9915a0-11d2-3dbd-99ba-afba71348340 | -3.89768 | -50.23179 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b7d96f4f-f8f9-312c-bb64-1fc94bccd06f | -2.83677 | -49.43063 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 548a1cf2-c466-3cbd-99ae-80ad2acd9e86 | -6.18501 | -45.44903 | 2024-11-09 05:33:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ee6c38d3-9719-311e-bfb9-c0fa54a7e7bf | -2.88991 | -49.38269 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0babbd3e-d108-3e2e-9469-ea339aca6e2a | -3.96024 | -48.16166 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| cf35c85c-1a21-373e-b83c-edcb58b4c7c5 | -2.6144 | -51.74741 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 380533dd-04a6-350f-82cd-3e93c5660b63 | -2.41103 | -48.51286 | 2024-11-09 05:33:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 0b074c39-11b0-390c-afde-e42047df94d5 | -3.12475 | -45.9537 | 2024-11-09 05:33:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b0d2412d-b2dd-34f0-a7da-1adcfec6a1e3 | -4.11213 | -48.50222 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 9ab2e2ad-2792-37bb-8dd3-cb95e2cd4142 | -3.56371 | -43.56897 | 2024-11-09 05:33:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 761ed774-14d4-3b7d-950f-8d7b77d8e279 | -3.90937 | -46.45203 | 2024-11-09 05:33:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ff0c15c7-bc2d-3b76-8b88-4eb495d58a62 | -4.20481 | -45.86129 | 2024-11-09 05:33:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 100c6fbc-964d-378e-be1f-80d050b2f354 | -3.35603 | -50.26697 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 891804f2-a76e-3544-8a9e-9922cd839e6f | -3.50097 | -45.70047 | 2024-11-09 05:33:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5e3d503c-439f-3fc5-91db-1e69b144273b | -2.84576 | -49.43194 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9bac198d-403b-3823-b737-411857037e82 | -2.67464 | -49.89243 | 2024-11-09 05:33:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ef5beaf9-379b-324a-939f-a3f65f60db08 | -2.9969 | -49.2289 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ce81913c-da87-39a6-94e8-1ba5417aac80 | -6.27484 | -44.53873 | 2024-11-09 05:33:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| e3bab254-3c98-3889-b106-12450b645d83 | -3.82635 | -49.85037 | 2024-11-09 05:33:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a10fada9-c13a-3727-96f3-65da8514472c | -3.59597 | -50.27565 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 750977d9-b126-3c58-9808-b7a42b41db1e | -3.23757 | -50.26676 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 6c75eccd-b5d6-3395-8696-3affb7542522 | -2.23735 | -53.75753 | 2024-11-09 05:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 8c9b29d8-4103-3e4b-98da-4c9daefe2b85 | -3.74496 | -50.44866 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5b47f9e5-d5cf-3b34-8eed-d8abc7c8674f | -4.7392 | -48.99684 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c6e80b97-2d92-3310-b3db-5d9970057782 | -2.79323 | -49.6615 | 2024-11-09 05:33:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ee8564e2-3d7c-3dbb-8118-fb3b14dc55bd | -4.60647 | -49.57762 | 2024-11-09 05:33:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 07cf3399-f1e3-3caf-8f73-0b9fe3af216a | -2.68528 | -51.81351 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 658a37c5-0a07-3757-a9d3-9722580b09bc | -2.46893 | -53.6839 | 2024-11-09 05:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 96d4bf73-583a-3ff8-a803-95fa6ba49930 | -2.69341 | -51.69325 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5f820039-df18-3c75-9d65-cae4430e3f5c | -4.15914 | -48.24812 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d5da6229-dfc4-30ce-8c9c-0a966bf3c211 | -4.77785 | -48.67842 | 2024-11-09 05:33:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2fcd0cb-d462-3808-a325-df95be0b1ecf | -4.49193 | -48.49246 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 205b53be-7100-3ab1-8eba-e7737bffc236 | -2.87153 | -47.9042 | 2024-11-09 05:33:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ba1ad846-4674-3741-855c-747db2457d23 | -2.79462 | -49.65223 | 2024-11-09 05:33:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0bf73dce-251b-377a-b1a8-9cd159ca38b5 | -3.03935 | -50.29447 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8a4d5727-8551-3707-9832-2752522e56a3 | -4.25523 | -48.52879 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b242fd4c-634c-3bac-90aa-47a0610510b0 | -3.35223 | -50.11377 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8fd6a833-b314-3616-b0e6-419248dff9e9 | -2.58479 | -49.138 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1873b792-6ce8-3ac9-b5ce-ad526e09c1c1 | -2.6245 | -46.15031 | 2024-11-09 05:33:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6630a694-2e20-3fd9-b85a-df0b7c18e622 | -5.44284 | -43.26847 | 2024-11-09 05:33:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 8dd93196-2a94-3ada-96c5-cb779bf3d637 | -4.36797 | -48.1464 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ecd8bea0-e423-357b-a3ef-730efd262ba9 | -2.2011 | -48.38002 | 2024-11-09 05:33:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 871ca99e-c37c-3053-82ed-068130ca497f | -2.07589 | -52.03847 | 2024-11-09 05:33:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f792da56-59d4-39a0-bfb4-1a5f2b32b7e0 | -3.09275 | -51.29458 | 2024-11-09 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 178c3668-04da-3bb6-aefa-1518a58632c5 | -2.88737 | -48.29062 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| e9b3bfef-0fe4-3b26-8b37-7feee951e2ba | -4.09473 | -48.85941 | 2024-11-09 05:33:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 002db04e-3602-312d-a735-0790a1f67553 | -2.24678 | -53.77629 | 2024-11-09 05:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 85549d9e-17b5-335d-905d-62337eb11997 | -3.34281 | -45.16189 | 2024-11-09 05:33:00 | AQUA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4f655509-e69a-3cfb-b257-70c07ab1ad6f | -3.97663 | -48.17307 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 1d3dd589-7317-315b-b662-d047013bb53b | -7.45986 | -43.57703 | 2024-11-09 05:33:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| d0f76b19-d69c-36bd-b4b3-b1996127d084 | -4.06926 | -50.00976 | 2024-11-09 05:33:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8a9ed6f8-b34e-35ad-a3eb-e3bff2c23389 | -4.21517 | -48.67573 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 05238823-2900-383d-aa63-9e75d56e224b | -5.47007 | -43.64726 | 2024-11-09 05:33:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 58f4efff-091d-317c-b824-f9a4cfa9d86d | -4.3207 | -48.64391 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9668d2e7-7c5b-3929-8e60-ecb11a50f7a8 | -6.13118 | -42.55361 | 2024-11-09 05:33:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| d3b561c0-ad68-35db-9b92-676add9ab91c | -2.62069 | -51.29562 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 6b948f38-9609-348d-856d-4c818d947b36 | -2.56774 | -47.34485 | 2024-11-09 05:33:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6991f44e-8f99-3735-8e22-017db8b1a492 | -2.45997 | -49.78487 | 2024-11-09 05:33:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f0875180-1c76-30da-9299-482de9be0a13 | -4.31582 | -48.61622 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fedadcf2-6bca-33da-a4a5-9264ef0f8aed | -3.0798 | -50.56963 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 89b220d7-f098-3dc8-8656-96a21d19c8ff | -3.08556 | -49.55412 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e801c8b-b68b-3bc1-91a1-edfd5d558286 | -3.04422 | -50.32511 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 434ea36b-91a9-3e96-9652-08234ca6f2f9 | -3.24377 | -50.45403 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3887867f-dfa7-3715-ae75-a228d5830410 | -2.63423 | -46.77518 | 2024-11-09 05:33:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2015c2ac-7a59-32cd-a3a4-8c7db70ba3eb | -4.23446 | -47.55669 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6efc4357-2309-3936-9215-c7dab72b7bd6 | -3.0704 | -50.56825 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 54ca02a6-8efa-3cad-b37e-ba88281aa2e1 | -2.51889 | -46.30871 | 2024-11-09 05:33:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8004a53b-3066-3b35-8bf7-3de961944102 | -6.18668 | -45.437 | 2024-11-09 05:33:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c889ac8b-b6f3-37dc-a1f2-154907a7a101 | -3.60663 | -48.91875 | 2024-11-09 05:33:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 77265f52-05bd-3814-bc74-5811bfd59388 | -3.24681 | -50.26815 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 14c69da5-cb2a-381b-98fc-12e94c0f5418 | -3.20681 | -50.63176 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 27bdf0f1-d74b-327e-bdd4-d89a61174aed | -2.18117 | -48.33224 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b72a8322-ee8b-3371-a60e-5488c189be05 | -3.26538 | -46.31551 | 2024-11-09 05:33:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 615973fc-ef28-37cc-8135-7d95b6d7b96c | -3.21999 | -50.38352 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ecbafe11-a292-32f9-9364-4adca958bf22 | -2.8803 | -50.41565 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 01ec0fc4-5814-3f2e-ba62-280782040fdb | -2.40482 | -48.49397 | 2024-11-09 05:33:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 57c45fd8-5c0d-3cd0-9677-a4b794438ff1 | -5.11645 | -47.14273 | 2024-11-09 05:33:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f1cbad3f-c2e1-398c-bc25-59254c082355 | -4.40985 | -48.60876 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6fff24dc-d77f-3570-a2f4-a2442271b8d5 | -2.86889 | -50.32682 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c2a35d2f-3407-33fe-925d-93aec365497f | -4.84805 | -48.64128 | 2024-11-09 05:33:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 81b3200f-727e-3f84-a93f-d35d4b88fd53 | -4.37846 | -48.57721 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6f222d55-f058-3b7c-ac17-7ae5965a01bd | -5.43101 | -46.94157 | 2024-11-09 05:33:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dcd02d48-bfaa-3a1b-b7ac-87fa431b48da | -3.38371 | -52.34732 | 2024-11-09 05:33:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8ccb4cf9-e3d1-3565-a7d3-45445658d6c3 | -2.84022 | -49.46838 | 2024-11-09 05:33:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7d526a51-13fa-3ec6-8e64-c725fb33293c | -2.93121 | -49.35171 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README116.md)
