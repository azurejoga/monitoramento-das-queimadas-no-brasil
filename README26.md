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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a01bf7f-4789-3d03-aa1b-2b8d785d9936 | -9.71521 | -48.9071 | 2025-11-16 03:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c083bb77-f742-3c23-8c65-5dc015c46bb6 | -14.66692 | -46.54041 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97c2fd3a-8e98-3ad4-820a-9bb7fa7c73fc | -14.20414 | -41.84504 | 2025-11-16 03:49:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5f5dd40e-d152-32b6-8514-a43834e01ea2 | -11.96769 | -44.95248 | 2025-11-16 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23f8a5c1-a58a-3dc0-949e-072105302674 | -2.5238 | -47.8115 | 2025-11-16 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 8103d837-0907-3181-86b7-4785f92db76b | -12.0004 | -49.2683 | 2025-11-16 03:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| abb95b98-c6eb-3a25-9b03-b71ffbb136f6 | -6.3121 | -43.7804 | 2025-11-16 03:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 0fc63918-6c1e-3924-8e51-d97e8b981a64 | -4.4246 | -43.4038 | 2025-11-16 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| d5d16617-ae4e-3b09-b70f-a6f3a760a155 | -17.14454 | -47.3157 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 215922da-5612-3812-9716-da06d17fdd16 | -16.56557 | -47.60992 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f23f9a2b-6032-3352-8600-d526696f6ec9 | -16.56419 | -47.61315 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aeea0263-a4bd-3b0f-8008-c239a32dffaa | -17.42667 | -41.69003 | 2025-11-16 03:51:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2ef51730-87a2-3f68-b8b1-b420d2cb3fcd | -16.57051 | -47.61045 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60e913a2-8545-3d63-bdb4-3541029b2918 | -16.57185 | -47.60727 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 708ef305-4400-3969-babe-f4db15f012e7 | -16.56581 | -47.60555 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e906c3b6-26df-343c-87bf-f1da06082a6b | -17.0486 | -44.04556 | 2025-11-16 03:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5d7b71d-465a-370d-ba67-62358f979c65 | -18.69776 | -40.10812 | 2025-11-16 03:51:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| db4f0eb1-d2e2-3ff8-83c6-b62aac504ba1 | -16.57131 | -47.60668 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02ea6fa0-bd5c-3d2f-92f2-834d72c98921 | -17.14384 | -47.31908 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 04e62636-b491-34c5-9a1f-fdc62e042140 | -16.565 | -47.60934 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dd64d549-2c8a-359b-a67c-58c65d0d0104 | -17.7859 | -43.86025 | 2025-11-16 03:51:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 717aa69d-1151-3cb8-93ff-9ded656496ef | -18.32563 | -47.18311 | 2025-11-16 03:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a13fe31-9ab4-3eb7-9e5e-76a344a74c53 | -16.56478 | -47.61372 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb3436c2-3e51-3238-aad9-5de70333f830 | -18.7012 | -40.10875 | 2025-11-16 03:51:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2f59f37f-adb6-3de3-be58-4924c424bb64 | -16.56635 | -47.60611 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9cfc87e-783e-3bf4-962a-4d92abc2c7ea | -17.14982 | -47.31713 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35db4d62-f1bc-38b2-9525-1474e4c753f1 | -16.56083 | -47.605 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43b31fb4-48d1-3f85-a08e-e3092915aa30 | -18.32049 | -47.18178 | 2025-11-16 03:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbdbfed8-d0f3-34e6-bd4f-0b9d4e7d46c0 | -16.57107 | -47.61105 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0343126-59d6-3889-b3ae-bf5d80cea1f1 | -17.14912 | -47.32056 | 2025-11-16 03:51:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ac4f6406-d17e-3c25-9873-7d66239931ac | -17.78087 | -43.86356 | 2025-11-16 03:51:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c44e1529-2c7f-3da8-bdc0-af95a6e4d79a | -17.42294 | -41.68927 | 2025-11-16 03:51:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3f16cb85-889f-36ba-bc2f-63b993a7ba85 | -12.0 | -49.2901 | 2025-11-16 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d63ca16b-c3a1-3eed-9081-a6133c5d474a | -4.4246 | -43.4038 | 2025-11-16 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3aaa00aa-6391-34a8-a6a7-43dad9296b64 | -2.5238 | -47.8115 | 2025-11-16 04:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 32501296-898d-3f47-80ad-7820eefceffd | -12.0004 | -49.2683 | 2025-11-16 04:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 1dba5727-8a30-3105-9773-e70c61f766cc | -5.33273 | -40.99652 | 2025-11-16 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 049a6c38-fe98-3eaa-b273-b2a20f8f1844 | -4.49375 | -47.65869 | 2025-11-16 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56bed457-a292-34ed-b272-8902dfb9f64a | -4.68904 | -46.31699 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1813f64-02bf-339c-8b96-5c83e943c6ed | -5.33594 | -43.04172 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37d9c117-d549-32c2-8295-c243b376e3e0 | -4.68811 | -46.52341 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcd95dc3-64ed-32ac-9808-ae56b3723405 | -5.7137 | -41.4031 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 97bd0a5d-55d2-3043-8b9b-f5f72f2791ad | -3.46232 | -50.1207 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb1c13fb-9227-323c-90b2-2b00baf78ff5 | -3.85486 | -39.8288 | 2025-11-16 04:06:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d13c630e-8dbc-3e5c-876b-de0a0666d467 | -3.56305 | -41.72145 | 2025-11-16 04:06:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c414cb3-1395-3717-a4bf-f960116bd6e0 | -3.78456 | -47.47681 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b370f67-4d6d-3ffa-8979-05eecbf5532b | -5.41991 | -43.25884 | 2025-11-16 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed059432-2860-39f8-8eb0-c52fd2c24ad3 | -4.6931 | -46.3177 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ace0e56-3fdd-37a7-8b73-fdd77c4ce242 | -4.36665 | -45.96778 | 2025-11-16 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11b27a81-4906-3c94-81c8-6eb8c9c49799 | -4.02014 | -48.80975 | 2025-11-16 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 48983183-5935-3053-b406-c32769627215 | -4.15394 | -50.22814 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdbb2483-a32d-3248-b25e-26d42c36db92 | -2.55223 | -45.33943 | 2025-11-16 04:06:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8927e3fa-a454-3268-af2a-d30c633c6521 | -3.32568 | -45.85138 | 2025-11-16 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de017948-43d5-3cc4-9b0c-7c800d81c76c | -5.11139 | -39.05448 | 2025-11-16 04:06:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2bfcc7e7-ec67-3193-9c55-366744f0443c | -5.32914 | -43.04062 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d95356f-3dc6-32a6-8ee3-e7d45085ae9c | -4.56887 | -45.81129 | 2025-11-16 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c588668-fb96-375f-b1e5-8f410e6ad595 | -3.78902 | -47.47753 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2046ccd0-6028-38c3-9849-70b9f7a51b38 | -5.32655 | -35.93075 | 2025-11-16 04:06:00 | NOAA-20 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de57a1c8-5145-3f9e-9db5-664b3ccd18bf | -5.05992 | -44.70444 | 2025-11-16 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6d641aaa-d956-3824-9ad2-ffa1bb994486 | -4.11607 | -47.30006 | 2025-11-16 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64720509-bb1b-363b-b6f1-10421cd235da | -3.95599 | -44.84998 | 2025-11-16 04:06:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a3ac1957-2d9f-3463-953e-bd8057e6f0b7 | -3.40575 | -46.90531 | 2025-11-16 04:06:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7117e3f9-82f9-32e5-b5df-23328eac85d0 | -3.32512 | -45.85491 | 2025-11-16 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6622b5af-5659-30a7-b88e-612b87cd5954 | -4.94874 | -37.39354 | 2025-11-16 04:06:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ac05d2b-f8ef-3269-834d-e1dafc33bf53 | -5.07787 | -42.74742 | 2025-11-16 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a31e1ca8-c768-3f4c-bb83-019dc70708c5 | -2.51854 | -47.82337 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| b9be93ef-294b-316d-8c53-df39b10b8c2a | -5.47342 | -40.96595 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c905139c-074a-382c-85e4-38a5075f9890 | -3.40258 | -45.84281 | 2025-11-16 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb29f11c-0569-342e-a828-031a032af29f | -3.60342 | -52.0545 | 2025-11-16 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c1e243a-fc09-33ca-93b1-935be2a99a6f | -5.46465 | -40.97869 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 88fbc8cb-93b6-33fb-bd3b-eba40d8f7fea | -2.88809 | -50.40783 | 2025-11-16 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e57a685-e004-30a6-b0f7-7ac5ad0eda0b | -5.46578 | -40.99301 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8a5fa767-f285-3700-a6ed-f5f098158aa6 | -3.45881 | -40.51116 | 2025-11-16 04:06:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7cab9099-0e23-3b63-baeb-d5fbfbaeb32c | -5.10653 | -40.7275 | 2025-11-16 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 594230e5-856d-3d9a-99b7-1d2b80231315 | -4.7358 | -46.38781 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 173cbc84-03d6-36e9-ad53-986eeff3371a | -5.2484 | -43.91035 | 2025-11-16 04:06:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb86baf9-6ef9-356d-b059-bd09abe70f17 | -2.82893 | -46.72956 | 2025-11-16 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9824909d-5675-3cdb-8e30-16b199ae8047 | -5.23443 | -44.34907 | 2025-11-16 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e5f184a4-a5c0-36e2-9bf1-ace19b1c75dc | -4.30404 | -46.27321 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11e5e5b0-8432-3fc4-b70a-2f6dcbfcd0d2 | -5.21775 | -44.51774 | 2025-11-16 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f4d65ac-37bd-329c-9c34-4a50684d10ed | -5.34459 | -40.8994 | 2025-11-16 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa346f47-726b-3f66-80ee-41d9f2455909 | -3.45238 | -46.12457 | 2025-11-16 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed7c9511-86ba-3986-bf1f-0c0abdde400e | -2.90272 | -49.1394 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4f07cda-5b78-3687-8ea4-828ca050e4bc | -5.33933 | -43.04228 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 126e45b4-50bd-3788-b71b-49534cb55491 | -4.97739 | -43.88428 | 2025-11-16 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 934f0a1f-a9ba-35d6-bb9e-23eaab407eaa | -4.43361 | -43.41454 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9b817ebf-6ded-3fd9-8387-c9dbf11f6a6e | -4.68842 | -46.32067 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cf1aac5-3ee3-34eb-90df-3ff9fc0c8be6 | -5.53437 | -41.76361 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e530372a-133e-3d06-bbba-16363f0fa739 | -3.94595 | -47.20936 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68b89367-f916-3267-bd01-76fd19684064 | -5.46849 | -40.97577 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 077a977d-3c66-39b2-927a-afee13737e0b | -3.63384 | -45.16035 | 2025-11-16 04:06:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5aca4c43-2464-317f-ada7-f2157e88a4e1 | -3.71962 | -45.99511 | 2025-11-16 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41b3728c-12e8-33dd-ad92-fa7fa05d3359 | -5.09403 | -41.4742 | 2025-11-16 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8fc3300a-e691-3564-a977-d573edad5172 | -5.22363 | -44.43694 | 2025-11-16 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7dce70fc-278e-3a44-91fe-ccb5df808771 | -3.59342 | -41.65824 | 2025-11-16 04:06:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e05cd08-10cd-3e0b-81bb-413bbaa90b00 | -3.4632 | -40.50476 | 2025-11-16 04:06:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| af4b27a1-44dd-39fc-8b6d-5bd93d1bac4e | -5.64694 | -39.74102 | 2025-11-16 04:06:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c3206a95-8bf6-3ef5-b47c-8c0cdac5111a | -1.93565 | -47.04015 | 2025-11-16 04:06:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f8c8ad99-52b9-3d3d-b1d1-76e443bfd220 | -2.89244 | -53.29248 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e023ea6-6563-330e-9ae1-7b87dd745027 | -3.32252 | -44.56354 | 2025-11-16 04:06:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README27.md)
