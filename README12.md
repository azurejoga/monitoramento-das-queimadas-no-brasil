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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c624fa44-1756-303d-954a-fae0acd4161d | -9.406 | -60.5711 | 2025-08-28 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 93cb726e-cb88-361c-b5e0-119805538715 | -8.948 | -65.9429 | 2025-08-28 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| bdb85481-0773-3cae-a2da-7f77e513d5bf | -8.9479 | -65.9616 | 2025-08-28 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 31ddeb57-c6d4-305e-985f-aff45e9ce677 | -9.1363 | -65.2835 | 2025-08-28 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| a0da1ae9-54d3-3e05-aa35-8a696fc07d36 | -9.1155 | -65.7699 | 2025-08-28 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 369.2 |
| c26c9d5c-f401-3919-8593-e76f6bf91c79 | -9.1338 | -65.8067 | 2025-08-28 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| cf280403-adb2-3a98-a28f-5bc9b83b3c2a | -9.0971 | -65.7332 | 2025-08-28 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 876278ea-638f-3bf3-b220-47572bd9cd0a | -4.8079 | -47.2604 | 2025-08-28 01:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| b0c21cf7-f3e0-3650-aac9-6bbcd1afb92c | -10.4738 | -57.9366 | 2025-08-28 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| bfb9ac45-3484-3f15-88ee-7e6de9670f9b | -12.4396 | -45.9551 | 2025-08-28 01:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 618badf1-0013-36a3-8fe8-52a5495d7b79 | -13.1837 | -45.2865 | 2025-08-28 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 3ea91bab-5cfa-37b0-85f2-f7bea87790df | -11.3526 | -43.5187 | 2025-08-28 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 19492b4d-25c2-3b48-a7d2-33f38c395a20 | -6.8774 | -43.5919 | 2025-08-28 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| bee81776-a1ca-3236-ad60-c4dfc214f2ea | -7.3357 | -59.6484 | 2025-08-28 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8790953d-7c21-38ce-be32-036177809b40 | -10.4736 | -57.9563 | 2025-08-28 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6d2cc9fd-ffdf-3257-b7df-d431a3335a91 | -13.1842 | -45.2633 | 2025-08-28 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 574e9ec0-0355-315b-b70d-e975e56bea6d | -9.1339 | -65.788 | 2025-08-28 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 497.9 |
| ddcbdf65-a4de-390f-8a69-5a13831d2cd9 | -7.3542 | -59.6476 | 2025-08-28 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 8f92dc2c-0eea-3f81-8e27-a918861cb6e2 | -11.3521 | -43.5423 | 2025-08-28 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 70486bf9-0cf9-320a-9f57-f57d4b16cc28 | -6.896 | -43.6135 | 2025-08-28 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 48bfd09c-b3d3-3c74-aaf4-d6300739a9d4 | -7.3541 | -59.6669 | 2025-08-28 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 2cec21ad-7ddb-3f43-9f07-ea1c2d948905 | -6.8772 | -43.6152 | 2025-08-28 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 177.7 |
| be7e62ff-4317-3279-a129-01de58c34c58 | -11.3334 | -43.5216 | 2025-08-28 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| b6b95dbe-0624-3fa9-b3a2-c1fdd0a0bb79 | -9.134 | -65.7694 | 2025-08-28 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 426.2 |
| 2d9a471f-9553-3864-a2fc-284c8b67892a | -10.5184 | -46.6917 | 2025-08-28 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 27db2dd2-d8bc-3240-84eb-4278806a50ab | -6.9129 | -62.9366 | 2025-08-28 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 83942a5f-1107-3ff2-a17b-b02566161a75 | -4.7893 | -47.2614 | 2025-08-28 01:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e42fd141-f40a-3385-ac81-1049bc4464e4 | -9.1154 | -65.7886 | 2025-08-28 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 444.9 |
| 5fb5561e-defa-3237-b36f-7dec6c1db8a9 | -10.5375 | -46.6894 | 2025-08-28 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 5e9d1e6e-426e-332c-9a9a-c05442b86bb1 | -10.5181 | -46.7142 | 2025-08-28 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 45488197-4479-3a3c-a56b-a285ffe4d658 | -8.9609 | -65.933197 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18f50e61-66c2-3403-815b-009ecabbaeb7 | -10.3818 | -65.315002 | 2025-08-28 01:41:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a8458e9-db32-3216-83bb-3ade566d2ff7 | -9.1318 | -65.784103 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85eb54c5-ec3d-3283-9a4c-21c572580743 | -9.1246 | -65.278397 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c76696e-7ead-338c-b57b-779582c93bd2 | -8.956 | -65.955704 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85df2d78-9025-3b9c-841c-358454cf52e2 | -8.6992 | -69.654701 | 2025-08-28 01:41:00 | METOP-B | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 80c2148f-9907-3901-8491-b788b280584c | -7.3697 | -64.365196 | 2025-08-28 01:41:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71a5b89d-c169-3b08-9ba9-b8a2582125f1 | -9.532 | -62.390999 | 2025-08-28 01:41:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be199f56-3a21-33ad-97b7-9d14220a5650 | -10.813 | -60.7817 | 2025-08-28 01:41:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 718bcdc4-9208-300c-a7f8-78a201774db5 | -9.1099 | -65.778503 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae65a5e5-323e-3b8b-b749-6315e3c4896a | -9.0853 | -65.718803 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e7fb722-301f-3936-a26d-f1100af5332d | -8.9414 | -65.937897 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55faf631-43d4-31a6-bf95-191b99d5d4b9 | -9.1196 | -65.776199 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9838d747-881e-3db1-a7a4-a029208da605 | -9.0903 | -65.739502 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01f4a89b-931d-3eed-ab9a-57ad1803c870 | -9.5018 | -62.7659 | 2025-08-28 01:41:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f71e016c-1eab-3e54-bd91-1d861fd5b5fa | -9.4119 | -60.5732 | 2025-08-28 01:41:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c547834c-6d40-3ae4-8f9c-a80d39ea2c3d | -10.2746 | -64.4851 | 2025-08-28 01:41:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e15c267-1abe-3a1e-9424-dc5052c8d8a0 | -9.1367 | -65.7612 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ebb9111-c293-30e1-a882-0d45afb9454a | -9.5514 | -65.6828 | 2025-08-28 01:41:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2339838f-c400-39b0-9907-8d5b36778a68 | -6.9104 | -62.938202 | 2025-08-28 01:41:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51f86dc7-5eeb-3dba-89de-60a525961cb5 | -9.1344 | -65.2761 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87aecc8c-4146-3c97-9485-c044cae0c987 | -9.0828 | -65.708298 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94265437-f4d1-3fcd-8207-0d7942f3014f | -8.9584 | -65.965797 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5a472f-acfb-3edf-a659-c7ca32970490 | -9.6592 | -64.9702 | 2025-08-28 01:41:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f221e9a-f607-3229-af11-4a6eed51ac49 | -8.9292 | -65.930099 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 358e9d86-1ca6-3722-ba1c-6487ade11ae9 | -9.1269 | -65.763496 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 293c2bd9-49c2-3765-b665-ff032333243a | -8.9512 | -65.935501 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 887e5d53-3c4b-3bf1-8b0e-ef9c709c96d9 | -9.1221 | -65.786499 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8220567-27de-36ba-9c87-3c2106ccd273 | -7.5401 | -63.8353 | 2025-08-28 01:41:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab943aa9-5372-3cd4-a9ad-6eae2af4bb1a | -7.3665 | -64.351799 | 2025-08-28 01:41:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95e94312-7245-3e02-9b6a-64aab824fd90 | -9.1147 | -65.755501 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ceb6cc2-155a-3c13-9049-d8b0fce00270 | -9.2488 | -65.8853 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 473549a5-9d63-3407-89e2-bbf3b2f1fae9 | -9.1074 | -65.768204 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cabe927-4dfc-3f43-a558-0c89ff72c2dd | -9.1635 | -65.7873 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab0d9725-0e54-34c7-9dec-51eae8c4984e | -9.3906 | -60.5303 | 2025-08-28 01:41:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9396554e-f9cf-3cdf-9362-72fe1b2f5d49 | -9.1317 | -65.264999 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bec9ea9-0564-3e02-9366-c4e37c12ffa7 | -8.9536 | -65.945602 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a50392d-b8dd-30d3-b631-2e4a58b4a29f | -9.3964 | -60.553101 | 2025-08-28 01:41:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd8286de-2a66-3b61-8450-dcdea19bf529 | -9.4022 | -60.575802 | 2025-08-28 01:41:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52401392-d888-334a-8116-f01749e2486b | -8.1068 | -71.237503 | 2025-08-28 01:41:00 | METOP-B | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 15bd8067-192f-39a8-aca5-d976ac023339 | -8.4477 | -70.138702 | 2025-08-28 01:41:00 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 041d7e65-a9fb-3b23-9eac-8109c6322bcd | -8.9633 | -65.943298 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3cc7ab4-17ea-34dd-acb8-1acbb5d63d18 | -9.1098 | -65.734802 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 296a2baa-469b-375d-9810-f18d21516e86 | -7.3335 | -59.660702 | 2025-08-28 01:41:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11368720-6bac-3e80-9e91-f53391fde75d | -9.2467 | -64.4151 | 2025-08-28 01:41:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dab858c4-9a0c-33ca-a106-6e4a0c7228b2 | -9.2609 | -65.893097 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa30012-4187-3e01-ac28-3ed4b37298cd | -9.5489 | -65.672501 | 2025-08-28 01:41:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| db050414-6a87-3a52-a2f7-506b9bfe2fcc | -8.9462 | -65.958099 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd3ee56e-8d31-32cb-badb-4c47a18aed6e | -9.4794 | -62.386398 | 2025-08-28 01:41:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab940c6c-0cb3-305a-b7ba-39ef6c065df1 | -9.1725 | -60.802399 | 2025-08-28 01:41:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2de8a3d0-213a-3dbc-b1a5-7d66d3d7c65f | -9.1172 | -65.7659 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e211678e-934f-3c82-9112-3c9c97d200cf | -9.2436 | -64.402603 | 2025-08-28 01:41:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e1fb72e4-7be2-3b9b-ba96-bba07c92a4e0 | -6.9063 | -62.921101 | 2025-08-28 01:41:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43c1fd53-abe8-3ac9-8dfe-34876eb0b882 | -9.7234 | -64.893997 | 2025-08-28 01:41:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 44c2bc45-fd16-3c01-9a12-ca242c58e480 | -9.4751 | -62.3694 | 2025-08-28 01:41:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d96ee368-7b07-3022-b099-0546c98ae59c | -6.8966 | -62.923401 | 2025-08-28 01:41:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b61a79cb-6f25-31a6-8971-52968ef39ae2 | -7.3262 | -59.632401 | 2025-08-28 01:41:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96c9a0e1-f929-3deb-a579-f1e558b24892 | -9.1294 | -65.773804 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9f4aeac-5196-3e40-a0d1-fb39c5f5c13d | -9.1391 | -65.7715 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97b9f79c-0c02-3a84-aa19-2a3382189d88 | -10.318 | -62.609001 | 2025-08-28 01:41:00 | METOP-B | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7f4cf03-59f8-3f50-9979-7004a097c672 | -8.9438 | -65.947998 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38351c61-25f3-30bb-b766-c2108da7a7f9 | -9.1272 | -65.289398 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f320575e-a109-3188-a4ce-891769207eb0 | -9.5058 | -62.781898 | 2025-08-28 01:41:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac8e7a4c-c9c0-3ca4-be69-91e09cffb759 | -9.1245 | -65.753197 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d518a828-2fc7-30c2-a8e8-95d87491ba52 | -10.1509 | -64.231102 | 2025-08-28 01:41:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 50746d86-d00b-371a-814d-fc2fee51ced8 | -9.2512 | -65.895401 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 618fb12e-1ea7-33d2-9149-082410ce09cd | -7.3358 | -59.629902 | 2025-08-28 01:41:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bf6d045-fd23-3e73-9a3b-1ecd4599d851 | -9.0878 | -65.729103 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3562449-1f75-3241-b899-4d8b5c92cc77 | -10.8077 | -60.761002 | 2025-08-28 01:41:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d448d30b-cff6-3ff9-8a3f-df8c5d5a1bed | -9.137 | -65.287102 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
