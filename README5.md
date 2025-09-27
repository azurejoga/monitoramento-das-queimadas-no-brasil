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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50f0dd69-6fdd-3e58-925b-eedb7c5530fc | -6.25652 | -42.47254 | 2025-09-27 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 390f7540-30a7-3314-928b-b741fd57cdc4 | -8.70018 | -47.02492 | 2025-09-27 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| be836cf9-40f0-3ad9-9190-ab603eff4097 | -5.93516 | -43.9982 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d8c82908-f6d0-3722-805b-de0af0e7a497 | -6.32019 | -43.45242 | 2025-09-27 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4cc1a9e5-ae58-385f-933f-e57cb9ab9cf5 | -4.57317 | -44.08547 | 2025-09-27 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ffe7fcd0-b485-3c32-804d-000b6b02c30d | -5.81504 | -42.8073 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 6fee6aad-ca6d-34e3-89e1-53b25c973b46 | -6.99103 | -42.3842 | 2025-09-27 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0db31b91-db04-3893-bfed-db1623c697e4 | -7.37355 | -47.03694 | 2025-09-27 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a69953ae-0d74-384d-9f3f-89f2563c90ed | -5.94731 | -44.88387 | 2025-09-27 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bcae3563-33b0-323a-b682-3df96e293f58 | -5.50455 | -43.87692 | 2025-09-27 00:13:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 43da0cce-6b5b-363b-b1aa-25a982152540 | -5.07758 | -44.85303 | 2025-09-27 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| ea951d15-2872-3997-ba0d-eac79f6b7393 | -6.27026 | -44.07875 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 128294e5-ea01-3140-b0a0-8af0d942c793 | -7.81517 | -46.90086 | 2025-09-27 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8701ee54-b683-3976-be9f-cc76e04be5d8 | -7.72624 | -47.3076 | 2025-09-27 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ad7caa65-bcd8-3194-8f10-3b391327464a | -5.48438 | -43.07728 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 54897811-e613-3061-aeed-1459f34d8611 | -6.70938 | -42.73975 | 2025-09-27 00:13:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a0d68757-51e7-31e4-8215-83bbd2bb16ac | -5.4767 | -43.0877 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 22da62b7-538b-3293-ab52-7c085d6c025b | -5.51338 | -43.87567 | 2025-09-27 00:13:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 17161fa0-2a8e-3c02-b3ae-a202aab1aa2e | -5.81373 | -42.79805 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 06e71fd8-c174-3392-a38f-7efcb87da84f | -5.83021 | -41.28501 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7736a589-a889-3045-b15d-a0e9a62a1001 | -5.63171 | -45.3368 | 2025-09-27 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c7922d48-afd5-3219-bb4e-c432e5dcc3a8 | -2.95248 | -49.09378 | 2025-09-27 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bbd64908-244d-36c6-abd9-2780713a0748 | -6.32143 | -43.46133 | 2025-09-27 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 265d89ee-5a5f-3d43-9938-969097984863 | -5.67639 | -44.85859 | 2025-09-27 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4738e039-6908-3263-8931-c6aa3e79fd64 | -5.4741 | -43.06937 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 231f0e37-edbe-379f-b653-cff45fa01177 | -5.72209 | -44.52208 | 2025-09-27 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f4f01fd6-751b-3064-a23a-f731483561e4 | -8.13344 | -42.37735 | 2025-09-27 00:13:00 | TERRA_M-M | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 05714ea6-efc2-380e-a1ea-d02fc49f525d | -3.7036 | -49.01975 | 2025-09-27 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 36ca5a32-8c7e-32cb-bde7-4a40ca21ef46 | -5.79535 | -42.8634 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| dd2c2966-d75e-3ce2-8f52-4559126e255e | -6.55094 | -43.8501 | 2025-09-27 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 09091330-2886-3fcf-837b-67aa9eccf949 | -5.07031 | -45.34111 | 2025-09-27 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a672010-5517-3942-a117-68e2d2709248 | -5.07879 | -44.86184 | 2025-09-27 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 2c8ecff2-7a9c-3097-b9f1-ca9ae23c8330 | -6.32033 | -43.38852 | 2025-09-27 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 4a6ffcf0-75df-3a5e-b3ba-cf4078c25034 | -7.87366 | -44.01705 | 2025-09-27 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5ae9b1c6-5e7b-39f5-b56d-224236b9bb1f | -5.30505 | -47.22461 | 2025-09-27 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| cf1bb603-e6aa-33e0-87ee-9814382911f6 | -7.14441 | -46.09452 | 2025-09-27 00:13:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a4c08fe8-e29d-3d56-826d-bf32413f7eae | -4.99474 | -47.35898 | 2025-09-27 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| bc90210c-738c-395e-9d1a-84927c96844d | -6.79103 | -41.76164 | 2025-09-27 00:13:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 336bf736-b18b-3e5b-8371-f26118d18945 | -5.57234 | -43.44401 | 2025-09-27 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| f7178664-e87b-3b71-8228-624b894852ab | -4.16654 | -44.26613 | 2025-09-27 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 85164f42-c12e-3d4c-ad1a-bb1391463312 | -7.56737 | -42.41694 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 6d7c7970-a9b1-31b8-8b53-d5612af8d395 | -5.91266 | -43.96547 | 2025-09-27 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dd7e5e98-4639-39c5-8fdf-e1733b8350fe | -5.31337 | -47.21261 | 2025-09-27 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 81d65538-adc8-346c-a452-53f4c8ed8b51 | -5.75413 | -42.89768 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 9ae01cdc-96d1-34f9-b176-4c8183d4cb32 | -5.46642 | -43.07986 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 9e9df95c-242b-3c82-afe7-b9399cdefd66 | -6.10699 | -43.90767 | 2025-09-27 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 35cfd458-84dc-3a2d-a9df-8eb60adf84c0 | -3.6448 | -43.11231 | 2025-09-27 00:13:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b64bedad-e080-3ada-9e37-e00ea9913f3c | -3.70182 | -49.00618 | 2025-09-27 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 56f47c4d-840c-3ed4-a8ed-e2929b579c27 | -4.48597 | -47.67987 | 2025-09-27 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 81963a1d-b273-3828-8aea-235ce86c0b05 | -7.0465 | -43.03609 | 2025-09-27 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 68039cc7-281a-3c2b-8f03-5e601c4cf43c | -7.00019 | -46.99753 | 2025-09-27 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d28215ea-39b9-3969-b5c0-9df59613c93a | -6.22801 | -44.18075 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c61f69d1-54f4-3a25-b724-4b9a2486cb54 | -3.69892 | -49.01241 | 2025-09-27 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 0797076f-3934-3e6d-8405-d44372b814dc | -4.80012 | -45.12374 | 2025-09-27 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 8c37af03-7c3c-337c-b59b-050a5f64172d | -5.91923 | -42.95576 | 2025-09-27 00:13:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| bb5e167f-ca58-3b3f-99d8-3438bc516493 | -7.05662 | -46.4114 | 2025-09-27 00:13:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 15ee9ac6-e5f0-32c8-86da-eed40313883c | -4.57955 | -44.06657 | 2025-09-27 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e996e858-2792-375c-971b-28f692b2f5ca | -5.5222 | -43.87443 | 2025-09-27 00:13:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ae467629-922d-3869-91b9-352422a0a846 | -5.4754 | -43.07856 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 241.1 |
| df7c88a7-1b29-311a-9278-acdd89b4f829 | -5.91389 | -43.97428 | 2025-09-27 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 04bbf74a-6fde-3790-98c2-93f0733da321 | -5.33833 | -47.40069 | 2025-09-27 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a9bacf64-49db-3bf3-a74c-8dc818fd56c7 | -4.67759 | -46.4485 | 2025-09-27 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c8f3c93-c147-3f5d-8224-9f6e7acbb3b9 | -5.25624 | -46.1679 | 2025-09-27 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| faa78d79-5d22-3d72-be0f-a41f35c4c300 | -4.00282 | -46.9753 | 2025-09-27 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| dd92d46e-d84d-3993-86a6-3d0cdfa4587c | -4.1778 | -44.28247 | 2025-09-27 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ff953a2e-4141-3ec0-99f4-0aacdc3b09de | -9.10232 | -48.90981 | 2025-09-27 00:13:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| d1d660a6-221f-39f0-be77-073d5835a301 | -6.26904 | -44.06996 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2d051c07-e621-39bd-83e3-5317920b163f | -4.57195 | -44.07666 | 2025-09-27 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a93019dd-6c1f-3a79-bf33-bd3fd48ada32 | -4.6263 | -44.06263 | 2025-09-27 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2fed6477-3ee6-357b-bc14-b3d98c0dabc7 | -3.58771 | -43.0976 | 2025-09-27 00:13:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 43503e8d-9d4b-36e8-bf52-a95c5738fad7 | -7.71611 | -47.30898 | 2025-09-27 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 57980c48-cee3-38e5-8305-dd77a4146b76 | -7.88368 | -44.02464 | 2025-09-27 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 35a75261-0f29-34b9-9e35-d3c7a6c0564a | -4.93746 | -45.58419 | 2025-09-27 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5f49ad26-0ea2-3ad1-9ff9-1cf70083303e | -5.46512 | -43.07067 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| deba4f53-793f-3277-99c1-182e9b5ddf52 | -4.53544 | -48.64723 | 2025-09-27 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| fb7895c4-87e7-3f2c-89b5-439f946436b4 | -3.45335 | -44.11886 | 2025-09-27 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 01aa5156-6fdd-3ae5-87a9-a809474b0277 | -3.58272 | -44.25647 | 2025-09-27 00:13:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 711c84cd-778f-3c66-9461-d2cfc2957126 | -2.27366 | -47.19636 | 2025-09-27 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6d5380af-fd91-3d91-ad55-c53f9da60a83 | -6.63052 | -43.8235 | 2025-09-27 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee81460a-a223-3989-be9e-b77370e50fea | -6.78959 | -41.75161 | 2025-09-27 00:13:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 39c07517-942a-33c6-8888-a2d67e0d8575 | -5.60487 | -45.81538 | 2025-09-27 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f50b22d-be75-3431-8f70-9c788e9e4bbe | -5.7996 | -42.82841 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| ef886e12-d48d-3fe5-97f5-9152d6523d1f | -5.86284 | -47.27053 | 2025-09-27 00:13:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cdde9978-8db4-3f77-b901-3ca6fa9d95eb | -6.54849 | -43.83244 | 2025-09-27 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24e96280-de47-35ba-b6c1-e7cb7dd91e68 | -6.22923 | -44.18954 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c34be9c6-2a75-37b8-81bf-045135f492be | -6.70093 | -42.74688 | 2025-09-27 00:13:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 80bff428-9c4d-3cd8-89a4-fe43d28715ff | -4.01084 | -46.96365 | 2025-09-27 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 55b9bdf6-b9b6-3265-9623-54e6bd8c535f | -6.63588 | -40.96896 | 2025-09-27 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 48af814e-9786-3505-99aa-75556f7d69d2 | -3.31691 | -44.18917 | 2025-09-27 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e9599f3f-5976-316c-b5fa-56b124a4720e | -5.08761 | -44.8606 | 2025-09-27 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b49465b7-471c-3af4-8a11-ec7d8faec2b9 | -7.87488 | -44.02588 | 2025-09-27 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 103a8978-bb38-30cb-92f6-84c36ed614cd | -6.31146 | -43.38981 | 2025-09-27 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1f8d7a64-a187-31ac-a660-fb4a3f6bc336 | -5.22069 | -44.48864 | 2025-09-27 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ae02011d-75a2-32c6-be2d-1583bdf64eeb | -6.66306 | -43.86382 | 2025-09-27 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b80c501-c200-3894-822c-ed199b8ee4a5 | -6.70222 | -42.75614 | 2025-09-27 00:13:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 11ee019d-d892-3e2b-be10-d4f0ad9f59df | -3.87763 | -40.43259 | 2025-09-27 00:13:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| b97d6c75-e0db-3660-800a-e49f8ed0669d | -5.89982 | -43.67887 | 2025-09-27 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 962b6336-39ff-3cab-af04-5363564b6e24 | -5.74003 | -44.97966 | 2025-09-27 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2e5c21e5-4f89-39b0-a952-0c1cdb8b880b | -5.67516 | -44.84969 | 2025-09-27 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0f6fb893-a0ac-3606-8006-522aa32fefa0 | -6.27905 | -44.0775 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |


[Clique aqui para ver as próximas entradas](README6.md)
