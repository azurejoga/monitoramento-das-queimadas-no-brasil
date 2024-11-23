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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e76f9cf7-c6ad-3da9-8302-0c15115ec3e6 | -4.61424 | -46.50359 | 2024-11-23 00:09:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 306bbb3d-35cc-3794-b365-5c4e3552dcf2 | -4.53653 | -42.90511 | 2024-11-23 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 44815d17-c7f0-335d-b72f-411daafcbb36 | -4.03375 | -46.19118 | 2024-11-23 00:09:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 39.9 |
| e416fc02-e753-3e05-8b76-28a171f43aa5 | -6.50852 | -47.04548 | 2024-11-23 00:09:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| e80598e8-9801-3fc3-bace-95c86af21e6d | -4.38822 | -38.96661 | 2024-11-23 00:09:00 | TERRA_M-M | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 9056eb81-2714-373c-a0fc-73a38c92185f | -4.01037 | -44.33927 | 2024-11-23 00:09:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 44504bc0-5d79-31f7-b44a-c3f60e1f8aaa | -3.13734 | -44.26759 | 2024-11-23 00:09:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 9a5a70dd-415d-3421-9a1b-cba6778430f8 | -2.31876 | -45.43634 | 2024-11-23 00:09:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| f19a9b7c-7e08-38f9-a5df-0024a6affd84 | -6.14275 | -46.6731 | 2024-11-23 00:09:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| ee312a7b-c1ab-378c-a684-3185eee073b1 | -4.12173 | -43.22567 | 2024-11-23 00:09:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 6b065bca-0f24-3137-9b11-daf67cba7366 | -4.41071 | -44.12079 | 2024-11-23 00:09:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 68d9cf5d-e4fa-3abd-8af5-70c5a80174f7 | -4.27345 | -46.30212 | 2024-11-23 00:09:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| b5af1a85-4fbe-3131-847a-9bf092c2fa93 | -3.67408 | -47.12785 | 2024-11-23 00:09:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 4b49ad7a-d105-33a3-b18a-29b1afb115ff | -4.60224 | -46.47671 | 2024-11-23 00:09:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 110.1 |
| f517a317-4214-3f2a-9806-1b5314604345 | -4.67395 | -45.65911 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 9bd12cf6-af97-3291-8171-388bf94f760d | -4.61001 | -46.47051 | 2024-11-23 00:09:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 27.2 |
| f85a0225-c39f-3adb-803f-73c0ee4d5c47 | -5.12272 | -45.84623 | 2024-11-23 00:09:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 46b52b95-7dff-3a3f-ba6e-b9d6070b059a | -2.72052 | -45.70557 | 2024-11-23 00:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 18526024-c235-39f1-bc0b-a2ad58c60e7f | -3.83765 | -43.93409 | 2024-11-23 00:09:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f3ba80d6-8f0d-324b-adcf-d9c38d5fe472 | -4.28538 | -44.81199 | 2024-11-23 00:09:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| c7f6ed75-e670-3ab7-af48-dcac42166f81 | -4.11062 | -42.46368 | 2024-11-23 00:09:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| f7253edc-e6e4-3645-8fbc-0d38da0bbe8c | -4.55188 | -45.89492 | 2024-11-23 00:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| c5c02f4c-e26b-3597-a92b-c552a886902d | -4.53884 | -42.92237 | 2024-11-23 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 216a5d73-765d-34d8-98e9-3fa67626bf66 | -3.72728 | -46.06421 | 2024-11-23 00:09:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 4f62bfb9-fd2d-3688-9901-a6056cb96200 | -5.74901 | -46.27894 | 2024-11-23 00:09:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 72f04f53-bca4-305f-8a3f-1fe4ee7bf16f | -4.6588 | -45.66136 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 2c6a6f7a-6af2-3fb5-a74f-2a49e4989926 | -2.83118 | -45.17738 | 2024-11-23 00:09:00 | TERRA_M-M | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 148.0 |
| c66df578-b3b4-3def-a914-bc24719522de | -3.14291 | -44.3823 | 2024-11-23 00:09:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f64c0b1c-a5ad-3021-9a83-4e5491177a88 | -2.8278 | -45.15257 | 2024-11-23 00:09:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 301.9 |
| a4168897-b019-3511-beea-7478612a1117 | -3.85345 | -43.95288 | 2024-11-23 00:09:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c5215715-84cf-3b0a-96f5-5f5633d41606 | -3.99167 | -43.71738 | 2024-11-23 00:09:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5c847acb-9d5e-381b-8ede-72bbdcedb1ef | -4.65645 | -45.65647 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 3b691856-7026-3500-90b7-17c126801c87 | -4.70203 | -45.86747 | 2024-11-23 00:09:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| f31d8468-c4ad-32a2-b125-db639122d6de | -4.03255 | -46.21838 | 2024-11-23 00:09:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| e56c70be-80a9-3ffd-a4cc-f227b7609639 | -4.59809 | -46.50603 | 2024-11-23 00:09:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 69c27709-93d1-3c47-a216-8de387b2b260 | -3.61546 | -45.69459 | 2024-11-23 00:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 35.1 |
| d07236b6-5d46-3aba-833e-816d56a682ce | -4.09901 | -42.46523 | 2024-11-23 00:09:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| d3e91247-3f48-3137-b797-79ebbfc2d6ea | -3.85067 | -43.93216 | 2024-11-23 00:09:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 051e7354-ac3f-32ca-8b3f-6c553d14395a | -2.86253 | -45.3004 | 2024-11-23 00:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 6e8b42a0-dab9-3406-8b59-5d4fd0c0cad3 | -2.81364 | -45.1545 | 2024-11-23 00:09:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 4040fb84-77c5-34e8-abd4-5a92f4cb402a | -2.95169 | -45.17975 | 2024-11-23 00:09:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 219.9 |
| c7ef04b3-871a-312b-9c3d-c553b9c0bf29 | -3.14111 | -44.39798 | 2024-11-23 00:09:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 8abf2cd0-d0cd-3592-a27b-fc9bd2785250 | -4.11276 | -42.47951 | 2024-11-23 00:09:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| a701e841-e0ab-34c0-976f-6b59c52203f3 | -3.00873 | -45.14127 | 2024-11-23 00:09:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| da273c1d-8eca-3814-ae41-fd646e0b2090 | -3.60411 | -41.67949 | 2024-11-23 00:09:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f1bd1284-60aa-3bb7-819b-dd650bcc1dd5 | -4.68787 | -44.41298 | 2024-11-23 00:09:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 90b12c3f-3b63-3ff7-850f-913d4bae9069 | -3.53503 | -43.32231 | 2024-11-23 00:09:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 98653da7-a9f9-327d-b59e-49257dc0ac1e | -4.66272 | -45.69073 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7751b47e-d67d-39b2-a9eb-0ea35d5bf866 | -4.12416 | -43.24378 | 2024-11-23 00:09:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 1f159b01-4763-3d9b-9c5f-988ec40ba65c | -3.46483 | -42.10134 | 2024-11-23 00:09:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 5f98a7ea-b80e-3ddb-9e27-422f4bd69526 | -3.63043 | -45.69255 | 2024-11-23 00:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 58673563-8062-367b-9240-3e1585ae9d17 | -2.95524 | -45.17388 | 2024-11-23 00:09:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 296.0 |
| ccd0c057-273e-3af3-a5a5-2aca8eaa93fe | -5.10919 | -43.17695 | 2024-11-23 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c40a1476-e976-3f67-89ba-173ac2317f6b | -4.08742 | -47.03701 | 2024-11-23 00:09:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 680610c9-23b3-3ffb-8c5a-c6490f266ba2 | -1.5339 | -47.30545 | 2024-11-23 00:09:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| fa0c47da-50be-310c-8357-1bcc6e002005 | -3.14594 | -44.40393 | 2024-11-23 00:09:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 01541731-375c-3e01-8967-24cc5fd98b98 | -2.94825 | -45.1549 | 2024-11-23 00:09:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 60c8af2b-3bf4-3ce3-8cd3-44df6e47195d | -4.4212 | -44.09733 | 2024-11-23 00:09:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| e19a74e5-9cc8-36fb-b5ac-dbdcb3b24c57 | -3.1506 | -44.3883 | 2024-11-23 00:10:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e698323c-0feb-32ce-ac5c-035684db539c | -4.5402 | -42.93 | 2024-11-23 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 6ce55414-8bca-32a8-bb6d-aa060e4146aa | -3.5159 | -53.8132 | 2024-11-23 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 5c9b9e7b-6263-3f4f-acce-f5b94b7be15f | -10.5006 | -36.6944 | 2024-11-23 00:10:00 | GOES-16 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 61.0 |
| 99380e23-743e-3594-8c8e-26acc8b61da1 | -3.2569 | -54.2426 | 2024-11-23 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 2639a361-e00e-3fa9-bba7-4f4d24339905 | -3.2569 | -54.2226 | 2024-11-23 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 87d5e285-8364-3fee-b34e-1db1e8317bed | -1.7359 | -52.7181 | 2024-11-23 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 612a38b7-5451-3bd2-af5c-38781c3df313 | -3.477 | -49.9197 | 2024-11-23 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 29c21bb0-19ec-3fce-a090-16b799e3f1ba | -3.4954 | -49.9191 | 2024-11-23 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 036870c7-8244-32e7-a1a8-08a23b853eaa | -2.8308 | -45.1719 | 2024-11-23 00:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 37365eab-5dfd-3b0c-bb6f-aa4454102e47 | -3.1322 | -53.1158 | 2024-11-23 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 9574a51e-b25d-31da-9b93-1b93993ece1a | -3.4662 | -48.2565 | 2024-11-23 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| f46f8a2d-3700-3150-abc7-8be5d9c2ea65 | -4.6086 | -46.478 | 2024-11-23 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 1d25dbb3-1f36-3213-a795-fc6cb5f37d5b | -3.0764 | -53.2796 | 2024-11-23 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 09006caa-e577-34f7-9f9d-1b7310ddcd7b | -1.1287 | -53.3951 | 2024-11-23 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 057a5293-7e0a-359c-a247-81093e08e6ed | -3.7538 | -50.0152 | 2024-11-23 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 203.0 |
| e4a0f5bc-0207-392a-a0b6-94733c452e3a | -4.67 | -45.6722 | 2024-11-23 00:10:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 54210906-8a49-3ab0-8252-e33b84654ed4 | -4.5898 | -46.5012 | 2024-11-23 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 145417ac-2a9a-38a8-aba9-4db59bda17b7 | -6.5054 | -47.0414 | 2024-11-23 00:10:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 0bd52cd3-bc37-307a-914b-7b0271bc829c | -4.5614 | -48.0141 | 2024-11-23 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| dcaa4ee8-15cd-3d6a-8c9d-3d7f15e4f34d | -2.8124 | -45.1499 | 2024-11-23 00:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 14442a51-6509-33c3-b757-405f2e56260b | -3.1138 | -53.1163 | 2024-11-23 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| e59ec21f-6b17-3947-a3f3-b381516c3768 | -4.5403 | -42.9066 | 2024-11-23 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| fd073b2e-9e46-3d04-b40e-96f0b30920b2 | -4.6085 | -46.5002 | 2024-11-23 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 20e5ebc9-1e10-31a9-bae3-1c1d3febfea1 | -3.4663 | -48.2349 | 2024-11-23 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 17b4b432-d31c-39dc-b589-ce61c3febd24 | -3.1505 | -44.4111 | 2024-11-23 00:10:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| f3be0b76-9e0c-3bd0-b38f-2e4e950436c2 | -1.7175 | -52.7184 | 2024-11-23 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2e100c5d-0276-3471-8b65-8f026479eb0a | -2.961 | -45.1672 | 2024-11-23 00:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ec8b1506-36ec-3891-abc9-2ee7a6ebe687 | -4.5215 | -42.9312 | 2024-11-23 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b34cd441-b598-32c0-a88b-9a0c30a3a608 | -3.1138 | -53.096 | 2024-11-23 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 4c2274b0-0ea5-3680-8e1b-c1274c0df655 | -3.7086 | -51.7888 | 2024-11-23 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 41851783-6791-3ac6-8f0e-38582173d3a6 | -3.2768 | -53.8199 | 2024-11-23 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 2a3e2acd-f073-3b1a-8428-c1ef6ee4d5f8 | -4.1133 | -42.4614 | 2024-11-23 00:10:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 62bdae76-d936-33fd-aea9-75ba256e2ac4 | -3.6276 | -45.7021 | 2024-11-23 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 8a7a042e-f998-30f4-8939-3db208182162 | -6.4867 | -47.0428 | 2024-11-23 00:10:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 003a77a0-7b04-3992-9f79-641c7947d225 | -2.6963 | -46.2719 | 2024-11-23 00:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5fe1fc07-2011-3d69-8510-ebd7349a7daa | -4.706 | -45.8493 | 2024-11-23 00:10:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 88.0 |
| fb84d518-d430-32f6-b42b-ae8aa3894b76 | -2.6987 | -45.6705 | 2024-11-23 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 77a662ce-6bcc-38b4-bec6-0c9ef53a10ec | -1.7359 | -52.7385 | 2024-11-23 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a895f382-079a-3899-baea-09e5365e25cd | -2.7149 | -46.2713 | 2024-11-23 00:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 10a1b967-fec7-30f0-a737-9bd7b99c7bb3 | -2.8123 | -45.1725 | 2024-11-23 00:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 40a7f0ac-a373-3093-9936-fb771fcd4722 | -3.7353 | -50.0158 | 2024-11-23 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |


[Clique aqui para ver as próximas entradas](README7.md)
