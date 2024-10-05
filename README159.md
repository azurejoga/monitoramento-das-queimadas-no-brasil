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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ce7bfdb-fc30-3b78-801b-ac4f0dc973b2 | -6.6444 | -41.99236 | 2024-10-05 12:36:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 533a7ce1-2b84-3f93-a613-fa0bb762fc72 | -8.95108 | -41.30011 | 2024-10-05 12:36:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 00f6ab87-f13b-3453-8f57-cca501b0f949 | -11.66563 | -42.67617 | 2024-10-05 12:36:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 122ea52e-968e-38ea-ac54-9ca6e75b3183 | -11.64849 | -42.64983 | 2024-10-05 12:36:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 8f50be1a-a725-38e5-bf28-85c22004cf75 | -11.6469 | -42.66174 | 2024-10-05 12:36:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 0c71c1ed-c1c7-3c48-88d6-e4d4f7d45e8a | -12.87881 | -42.82571 | 2024-10-05 12:36:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 34ee873d-a7f5-3cd8-bcf5-bf0e3b30db77 | -12.48583 | -43.02581 | 2024-10-05 12:36:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 865640b0-cc6a-3412-98ed-68b04ea52d3d | -6.36047 | -42.92557 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 3e99c225-ca8f-316a-aad9-41f6db21d7b7 | -5.95141 | -43.27986 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 990bacbf-6111-3a8d-8d28-cad07c094132 | -5.54166 | -42.78808 | 2024-10-05 12:36:00 | TERRA_M-T | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 76bb4e3b-d909-342f-b9be-dfbb0d648e6e | -6.44343 | -43.12382 | 2024-10-05 12:36:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d57df9f8-1439-3d6f-b449-29e41f27229e | -6.29587 | -43.44865 | 2024-10-05 12:36:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2a618880-5f67-3bb0-9b78-350fdbcd0901 | -6.28486 | -43.0102 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c4f40173-ec65-3241-8f45-b99dc42c37b5 | -6.28347 | -43.01997 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8f1e7c03-217c-3d5e-b41a-809899e2357c | -6.19554 | -43.10707 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ac4dbc53-633b-3e18-81a1-07bbb060edbd | -5.49562 | -43.3111 | 2024-10-05 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0a0bb43d-140e-3c2a-b110-37cd63131ab3 | -5.37506 | -43.24969 | 2024-10-05 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7a8a28b3-bd62-39b2-9a1a-b2fcacab43f3 | -5.37373 | -43.25909 | 2024-10-05 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 21781aee-265d-3d3c-9a42-62f7244886ac | -7.79766 | -43.10998 | 2024-10-05 12:36:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 9f110c69-15af-3a41-9005-e4766840c25b | -7.78826 | -43.10863 | 2024-10-05 12:36:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 35f2751a-5905-30c7-bb9d-4e5226666223 | -7.7529 | -43.04668 | 2024-10-05 12:36:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 7eec4ce2-e3a2-3cee-9ae9-45430c00093e | -7.74866 | -43.07675 | 2024-10-05 12:36:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 600e5804-2f03-3214-bf89-0ea1a9661bd4 | -7.74205 | -43.05548 | 2024-10-05 12:36:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 23cf71b4-1d74-3150-b02b-a88049ea3b50 | -7.74064 | -43.06551 | 2024-10-05 12:36:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 0641c877-c9fa-3cc7-804a-0263af029447 | -7.73925 | -43.07542 | 2024-10-05 12:36:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 85c87296-d3ab-3a69-b292-cfa15d4baa39 | -7.23391 | -43.32778 | 2024-10-05 12:36:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 7482ba45-d8d8-35f6-826b-344725fc1525 | -7.23254 | -43.33747 | 2024-10-05 12:36:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| a7cb188e-b474-3e61-8958-3867081fff0e | -6.9176 | -43.34467 | 2024-10-05 12:36:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| f9fe0f49-f9b4-3f57-8969-95bbd2bd1813 | -6.84524 | -42.81879 | 2024-10-05 12:36:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| bb9399da-421c-3388-8c85-192981e2da8d | -6.8438 | -42.82899 | 2024-10-05 12:36:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 048eaeb5-c372-3c46-86b2-5b08b990c6d7 | -6.8372 | -42.80732 | 2024-10-05 12:36:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 89aeb255-03e9-3b62-a144-32f05c500815 | -6.83578 | -42.81748 | 2024-10-05 12:36:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| af58e5c6-18b6-3703-b524-adde8fb81d1a | -6.82633 | -42.81617 | 2024-10-05 12:36:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 14936c9d-aeb7-34e0-ad53-f5bf5b1a30d1 | -6.47389 | -43.36013 | 2024-10-05 12:36:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7ea0d05e-2d95-3925-8d76-d96dccae6ed5 | -8.18147 | -43.72369 | 2024-10-05 12:36:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 382843f9-c093-3942-a4af-7c5bbf4eb917 | -8.18012 | -43.73323 | 2024-10-05 12:36:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| abbef6fc-e2a1-3c38-bbc0-8c04cb0f9743 | -8.11021 | -43.7752 | 2024-10-05 12:36:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 2495d4cd-64c6-3764-9998-695cdb9c059f | -8.10887 | -43.78465 | 2024-10-05 12:36:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |
| d64e1d22-f15f-3d51-8d5b-684831aea8ff | -8.36602 | -43.65371 | 2024-10-05 12:36:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 30f4e986-b9e9-3e0d-a111-96ceaa9cf8e7 | -12.86118 | -44.6175 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c43a1a13-dfb1-3f70-8d77-3c79d4f1f7fb | -12.82565 | -44.60256 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| af319f57-c10a-38ba-86ce-f36679975b6f | -12.8243 | -44.61238 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6c584b5b-bbe7-3f6c-894c-62beeae7a4d4 | -5.73098 | -43.79298 | 2024-10-05 12:36:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ac5ef06-eb54-30ec-943b-f00fa6ce650f | -5.72254 | -43.78542 | 2024-10-05 12:36:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 65587f2a-287d-30f3-91b3-8ca6526002fc | -5.72123 | -43.79453 | 2024-10-05 12:36:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 83fb9a54-8811-354c-a493-1ae7dca862b5 | -5.71354 | -43.78419 | 2024-10-05 12:36:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| d425a9de-853e-3270-b767-be419f073bc2 | -5.71223 | -43.79329 | 2024-10-05 12:36:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 243.5 |
| 4aa208bf-b617-3b74-9165-d347f71048ae | -5.71093 | -43.80238 | 2024-10-05 12:36:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2f501cd9-8e55-318f-860c-4e926d896d43 | -5.65435 | -43.55439 | 2024-10-05 12:36:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 05696dea-0998-3ad5-b608-8d44f8cb7014 | -5.54621 | -43.72984 | 2024-10-05 12:36:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2b95b9d6-8be7-3bfc-92cf-758573c31aaa | -5.37088 | -43.34475 | 2024-10-05 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f9c8ee5b-658d-3772-ae84-dafea997b442 | -6.11142 | -44.22141 | 2024-10-05 12:36:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2ce0ce2b-0f28-3203-8f8b-52f80d851114 | -6.06949 | -44.0044 | 2024-10-05 12:36:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a3eef8b8-f5b5-3cf3-87a8-25e95d1d5f43 | -5.82145 | -44.12541 | 2024-10-05 12:36:00 | TERRA_M-T | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| d02c6657-9b9a-3c12-8727-edbae34ad44d | -5.82016 | -44.1344 | 2024-10-05 12:36:00 | TERRA_M-T | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| fbbcdfde-8d7a-3ba4-90ff-ed89b1c40516 | -5.52622 | -44.00151 | 2024-10-05 12:36:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 04208bb6-c065-3112-a6e2-6bab323688cb | -5.49538 | -44.3438 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d154a484-eb49-31b7-a33a-ba027fa7d727 | -5.4941 | -44.3527 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8d237941-c32f-36a4-b2a5-0b5bc41b74e6 | -7.60653 | -44.78318 | 2024-10-05 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 78e2c9b3-e7c0-312f-bca8-b172534b090a | -7.56318 | -43.92766 | 2024-10-05 12:36:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| ec7def34-ce48-3b9e-aa5f-3a2cc464082c | -7.55965 | -44.66711 | 2024-10-05 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 26ccbabb-520f-3014-a09f-422a5dee7765 | -7.55836 | -44.67611 | 2024-10-05 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 494d5209-de49-33ef-ac88-6357968ddd23 | -7.5541 | -43.92645 | 2024-10-05 12:36:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3e9c6f8f-980f-3fb9-8fae-e59a3a1a97f4 | -7.52627 | -44.96291 | 2024-10-05 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 95e17385-76c4-3486-9bb3-b27ed220412b | -7.52499 | -44.9718 | 2024-10-05 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 90b3ab7a-dd7f-39cd-80d2-32867306b190 | -7.50796 | -44.82714 | 2024-10-05 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| fec830de-5251-347c-b063-ce4814b2dade | -7.50668 | -44.83604 | 2024-10-05 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8d71eaf2-6e23-3be2-ae50-7f8f0898aca3 | -7.4484 | -44.7368 | 2024-10-05 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5587fa4c-1e16-3e67-90c3-c95446f47b80 | -7.4435 | -43.99331 | 2024-10-05 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5e8ede83-7e0c-35f6-aada-121b2220c017 | -7.10329 | -44.43764 | 2024-10-05 12:36:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2e1c46e1-326d-395a-a9af-59c66d044277 | -6.65991 | -44.51506 | 2024-10-05 12:36:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 559ad9ca-d6b2-316b-b27c-6dde5e50814e | -9.20815 | -45.69352 | 2024-10-05 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 931fe07e-8478-3b6e-b19a-e7c55b122bed | -9.19076 | -45.56355 | 2024-10-05 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0dc04425-6234-3185-8560-e15551cd69ac | -8.99294 | -45.2068 | 2024-10-05 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0a431628-6252-3972-bc1b-d01c7d01b0ab | -8.86919 | -45.17409 | 2024-10-05 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 458.4 |
| 5819cf1b-7a89-33af-a9fe-c3dae4420b4c | -8.8679 | -45.18303 | 2024-10-05 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 3f148fdb-82f8-3fc9-92e9-d9b0fcbb4c1e | -8.90642 | -44.91387 | 2024-10-05 12:36:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 102233ac-74da-3cdc-984f-da33858c7a1d | -8.90514 | -44.92287 | 2024-10-05 12:36:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e5a9f6c9-20d9-3abc-b0c2-b3c254d96dff | -8.77089 | -44.82738 | 2024-10-05 12:36:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 560919ee-ad26-303d-bdf9-d0c109ec5ba5 | -8.21794 | -44.44423 | 2024-10-05 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 51cb3204-931c-3200-a000-e9edfa28405a | -10.6749 | -45.10661 | 2024-10-05 12:36:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e5f60ed9-f749-30af-8b1a-30d589b43673 | -10.28736 | -45.43919 | 2024-10-05 12:36:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0bf35005-6fdd-3e2d-b866-94d86bf6b647 | -10.28093 | -45.48408 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 457363ee-a62d-3b16-b58a-c8164c75e61f | -10.2767 | -45.44035 | 2024-10-05 12:36:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 419189bf-038c-3ab1-876e-fce64a813daa | -10.15343 | -45.14996 | 2024-10-05 12:36:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| fa7e824c-61cc-39b4-8779-0c82fd54b194 | -11.67642 | -45.25245 | 2024-10-05 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3c99f38b-6c76-3094-96a3-5c7a86179bcf | -11.33346 | -45.52831 | 2024-10-05 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9358d958-4098-35dc-93b1-e34c0ac25fba | -11.33216 | -45.5374 | 2024-10-05 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 41f3c2f7-698e-384b-8544-4a58463f96fc | -11.33085 | -45.5465 | 2024-10-05 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d53390c1-184e-3a7b-9450-47e3b6f80349 | -11.32455 | -45.52706 | 2024-10-05 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 0fbe35bf-48ed-3c6f-babd-34605ad5baba | -11.32325 | -45.53617 | 2024-10-05 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 72f9f56f-e0b9-3af9-a216-a9d3dbaf2dbd | -6.17605 | -45.43641 | 2024-10-05 12:36:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3e08529c-0945-31f9-9d09-746235fe64fe | -5.57172 | -46.28622 | 2024-10-05 12:36:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| e63cf6b7-e4f9-3400-8eaf-1c8f72814d4f | -5.57032 | -46.29565 | 2024-10-05 12:36:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ddbb4697-7baf-3055-bb1c-3c694ad16a87 | -5.5626 | -46.28487 | 2024-10-05 12:36:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 2ed5ba34-5399-300c-b435-dbbdfb3b8f03 | -5.07007 | -45.87379 | 2024-10-05 12:36:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 29.0 |
| e59141f7-aaa8-34d8-8f61-99e1047996f2 | -5.06871 | -45.88296 | 2024-10-05 12:36:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ba5e1032-225f-3a0e-b107-e4b71f80628d | -7.01516 | -45.75536 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6103327a-39f8-3d1a-81f1-1538709eaf19 | -7.01384 | -45.76433 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a52ae91b-a35c-35cf-a9a8-69ee802b1b68 | -7.00455 | -45.75695 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |


[Clique aqui para ver as próximas entradas](README160.md)
