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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 360b4d36-840d-3dac-8c37-f7c58cc01bbe | -6.9414 | -42.907 | 2026-09-23 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| f995a599-433f-34bf-a01d-01dd0195c446 | -9.9163 | -45.0885 | 2026-09-23 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 167.5 |
| fdc00b6b-cad5-3ed5-a4f8-170880075fed | -6.6317 | -43.73 | 2026-09-23 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| b68a77bd-d0c0-3754-a7ef-65fe5995698b | -9.6043 | -48.4529 | 2026-09-23 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| a1e82387-50e3-3d32-aeae-f2761d446d10 | -6.5763 | -45.4968 | 2026-09-23 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| ae9f372b-f00e-3d7d-9167-fbdd5eea49c7 | -6.5449 | -44.8871 | 2026-09-23 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e4821d34-5362-3ae5-8845-3aba59f924d5 | -7.4153 | -42.6479 | 2026-09-23 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 9022ec1a-67e2-32e8-a87b-dc328e9f6066 | -6.6127 | -43.7549 | 2026-09-23 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f408b944-e18b-372e-9ceb-993745b9f46b | -8.9165 | -61.4767 | 2026-09-23 14:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| eb1e3c2c-447a-3bab-b5c3-b0e02528f5b6 | -7.1049 | -43.4309 | 2026-09-23 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| ff2c00e9-a147-3486-a0c3-31011d818b92 | -6.3199 | -59.9381 | 2026-09-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a0dbcdba-7886-30f6-9fe9-0e376073478e | -9.5668 | -48.435 | 2026-09-23 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e64076db-9357-39ae-a34e-5133c07fb84f | -6.9841 | -49.7777 | 2026-09-23 14:00:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 0ba3246f-f701-371f-9d12-9cc8823538d8 | -9.5549 | -46.5134 | 2026-09-23 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| b271ebff-b9a8-3d84-a2d5-2e22949e6241 | -11.0237 | -49.7304 | 2026-09-23 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 03719b08-bf9b-3b7e-af86-b01cd66e2f94 | -9.9064 | -48.443 | 2026-09-23 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 9db679af-4619-3ea4-8352-410b85638790 | -7.1274 | -43.1009 | 2026-09-23 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 473df11b-0700-3429-a8a6-5e8744719a88 | -8.754 | -44.2589 | 2026-09-23 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 195.7 |
| fe3e8160-8cf6-3be5-b950-18f21e989380 | -11.3359 | -43.3793 | 2026-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| fd3ff636-16a0-30c0-b43b-5504946060ef | -6.3015 | -59.9387 | 2026-09-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 613e5321-1bfe-31f5-b52d-f4e8b27a0044 | -11.4018 | -47.3628 | 2026-09-23 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 2e019287-dcda-3087-a2bb-9a8c925f4a85 | -7.0115 | -43.3696 | 2026-09-23 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| b30556eb-a34b-3165-a661-b326f855be92 | -6.6331 | -59.9265 | 2026-09-23 14:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 294.3 |
| 4ac19248-0215-37c1-b7da-4b81f78a71a3 | -8.4983 | -57.6271 | 2026-09-23 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| b7170e63-558e-3ee6-90ec-73efa07690d9 | -9.8694 | -48.3814 | 2026-09-23 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| c9dda51e-92da-3854-ae59-b3a7402c3652 | -6.5941 | -43.7333 | 2026-09-23 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b07a14d2-929d-35d2-a318-7314fae702b1 | -9.916 | -45.1115 | 2026-09-23 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| c7398b58-b751-3e9e-bcff-e99d172b1c8c | -7.7634 | -46.6944 | 2026-09-23 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a6d221a9-1ece-33ac-ad22-1a1c0409f4d1 | -8.4797 | -57.6282 | 2026-09-23 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c90271e4-cd53-3941-bd55-e360c3a26c2b | -6.9228 | -42.8852 | 2026-09-23 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| b6811c5f-3652-3c43-b29c-9897eca4ef4e | -9.5549 | -46.5134 | 2026-09-23 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 950e16aa-3bd7-3f34-9729-3449579ee974 | -6.5953 | -45.4727 | 2026-09-23 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 386900d9-96d5-3551-8a3b-d98c4e11ee18 | -6.2399 | -41.6394 | 2026-09-23 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 7e401fc6-da4c-3394-9cdf-49334d4ca3e8 | -6.221 | -41.641 | 2026-09-23 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| a8ef4fd9-aeb0-3d04-875d-cd907e1a1c74 | -6.8381 | -45.543 | 2026-09-23 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 8f63a921-e44e-337f-ad4d-e068f75b6d55 | -11.699 | -43.4416 | 2026-09-23 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 246.0 |
| fa15141b-c035-320f-8f5f-0980177b4257 | -6.2208 | -41.6651 | 2026-09-23 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 44f55ab1-bf61-336c-8b28-235b47dfea75 | -10.2517 | -45.5039 | 2026-09-23 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 6d81ca71-88d6-31bd-8d20-b293f00d8645 | -11.6621 | -50.2169 | 2026-09-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 1c7b0403-f9b6-3275-ad5a-6bbd3ac2d246 | -11.7002 | -50.2125 | 2026-09-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| fd2eea42-dc2e-30ce-b190-c912080bd94c | -6.3014 | -59.9579 | 2026-09-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 3dd50298-8d2f-382d-9ec5-3b6da8aa112b | -7.4286 | -44.7409 | 2026-09-23 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 218359ff-7afa-3be0-b10f-3e5fec43f061 | -6.9138 | -43.7049 | 2026-09-23 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f1deb559-7dde-3788-a9c8-d26ac31b4ca5 | -6.3199 | -59.9381 | 2026-09-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 7f72e95e-187c-3d8d-bc3c-b96d38b522d5 | -7.4153 | -42.6479 | 2026-09-23 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 0c60409a-5ac3-3a7f-9a78-f62cbc803503 | -6.5763 | -45.4968 | 2026-09-23 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| aed24698-559e-37ac-951b-bf50a376e7d4 | -11.6802 | -43.4209 | 2026-09-23 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| ada4e34c-2c72-31da-a4ef-150f46c654b4 | -11.3054 | -44.0198 | 2026-09-23 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 400.6 |
| 7ac7134e-9e61-3423-a053-2f36bd0f85aa | -11.8014 | -49.8129 | 2026-09-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 40cbc631-ec22-3868-a3b5-61464297c3bf | -6.6515 | -59.9258 | 2026-09-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 5293b3e5-c132-344b-971f-ca734792e1e0 | -6.4671 | -59.9711 | 2026-09-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b7c3e73a-a4cc-395e-bd92-267563aa088e | -8.0921 | -44.3538 | 2026-09-23 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 00229600-c5db-3ccf-b232-4d184a495f01 | -11.0048 | -49.7325 | 2026-09-23 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 4bbaaa49-fc38-3724-b58a-30aa0a5a699a | -6.9135 | -43.7281 | 2026-09-23 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3d956a53-2654-3532-912e-8418cd07c10e | -4.0023 | -52.0875 | 2026-09-23 14:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e193b307-35c4-3685-9369-f6b703e1a4ff | -11.6601 | -43.4714 | 2026-09-23 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 6abf5a06-f70b-3bc8-80d8-4aa44a826909 | -7.4683 | -44.5539 | 2026-09-23 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 93e3f274-52a7-3c8f-bdfc-007ae1c86e75 | -11.4209 | -47.3603 | 2026-09-23 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| ec76f4fe-8f7d-3a9d-a540-6f07ba805162 | -6.6129 | -43.7317 | 2026-09-23 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 306.5 |
| d6b7e9ed-18b7-3c88-8e2b-56a9d386d786 | -7.0352 | -44.6396 | 2026-09-23 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 156.8 |
| d0453a63-40d9-3561-bded-5ec48299ff75 | -11.8753 | -49.9551 | 2026-09-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| bce35f1e-d407-3793-a0c9-bd9b813b27c3 | -6.2396 | -41.6634 | 2026-09-23 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| ef5e9b71-8baa-3b67-83c6-d25c9978d66d | -6.6331 | -59.9265 | 2026-09-23 14:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 255.2 |
| 64470286-8eed-3d88-8484-61d9abae50c5 | -11.6431 | -50.2191 | 2026-09-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| b701b281-e756-3721-b800-1dbd949570a0 | -7.41 | -44.7198 | 2026-09-23 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 3d0d9ff3-b4e6-3d6d-8584-34c36de0da49 | -9.5735 | -46.5337 | 2026-09-23 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| a8aeb010-0ddb-3c81-a3ba-0b4886853da8 | -6.5962 | -59.9279 | 2026-09-23 14:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 054051d8-0baf-392d-8505-f5afbf1feb10 | -6.6332 | -59.9073 | 2026-09-23 14:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5bfd135e-cc76-3d16-b239-91f58ec10672 | -6.9885 | -43.7445 | 2026-09-23 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 73be82cb-92b5-3320-b239-f4b02a994d69 | -6.9927 | -43.3714 | 2026-09-23 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 3a80809f-998f-3c39-ad03-63ec348424ae | -11.1541 | -42.8364 | 2026-09-23 14:10:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 6ab0b3be-7c36-3bd6-8498-0ca1b8013a0e | -6.4301 | -59.9916 | 2026-09-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| ac115d02-45cf-3074-945a-339ab79d50d1 | -6.3382 | -59.9566 | 2026-09-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| a15056f7-dc7c-3c1e-9bb4-2f83e1327567 | -7.1392 | -42.0811 | 2026-09-23 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 137.5 |
| 843a9190-f9ea-3942-bf9b-fdae4980d1d0 | -11.305 | -44.0432 | 2026-09-23 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 319.0 |
| 69972c25-da60-3905-ae43-2d47a14dcc06 | -11.7784 | -50.0743 | 2026-09-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| bbd37bb4-c988-33fe-a23e-3c9d8b387aa5 | -6.1178 | -59.8877 | 2026-09-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 808d4a62-9e43-381b-a35a-ef9d94d2a59d | -10.3941 | -42.567 | 2026-09-23 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 7a5269a8-897d-3441-bcd2-68e99a110e26 | -11.8563 | -49.9574 | 2026-09-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 0deef3f1-fd7f-3bd7-9456-3c6be77e69fc | -7.0115 | -43.3696 | 2026-09-23 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 0d10775c-e01d-349b-a2f9-53e77b0ee14c | -8.3591 | -45.6056 | 2026-09-23 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| fcd9dca1-b02a-343f-b04f-e1a8a4f022a4 | -6.9323 | -43.7264 | 2026-09-23 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 4ca24530-4b57-3b76-bd30-152596346bd7 | -7.4288 | -44.718 | 2026-09-23 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| e86308a0-08f5-3e1c-a3cb-36a237571e41 | -7.1277 | -43.0774 | 2026-09-23 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 59af94c2-5911-31b8-9e85-3490157fb400 | -7.4495 | -44.5557 | 2026-09-23 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| bb727b2a-ffd0-38bd-abf2-f23d25c09235 | -8.3134 | -44.7446 | 2026-09-23 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| c7a844d3-61a6-3075-8e29-57029e5fbf48 | -6.3015 | -59.9387 | 2026-09-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 51b1d2ba-611c-3f0f-bf9b-5f2725d7b52c | -11.801 | -49.8345 | 2026-09-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| d60c3945-9dc4-3cff-b9ab-c3347741d418 | -11.3551 | -43.3764 | 2026-09-23 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 506.3 |
| b5a1f6c1-164d-356f-aff7-a02fa7d38cf0 | -10.0072 | -45.3518 | 2026-09-23 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ca2b3479-096a-3178-922d-317e5e782336 | -10.7443 | -50.7663 | 2026-09-23 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 152.7 |
| cbc293f2-1ef9-31c1-b8dd-5ddaf9a98b00 | -11.0237 | -49.7304 | 2026-09-23 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| af92ee02-0aba-3c9e-883f-5fd1cbf6997b | -9.0242 | -48.1403 | 2026-09-23 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| c6c0e5ee-4037-3c65-869a-417ecf8ffe65 | -11.2858 | -44.0461 | 2026-09-23 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 265.6 |
| ec497feb-fb54-37a2-a2cc-218ba4dbec8c | -7.1088 | -43.0792 | 2026-09-23 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| c1ee0487-b794-3263-b792-5caf0a39f346 | -11.2862 | -44.0226 | 2026-09-23 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 238.8 |
| 0d6b0134-2cf7-3f47-b3be-a9ffbcf583f5 | -11.3547 | -43.4001 | 2026-09-23 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| c22b5e62-079a-33db-babd-e831ca6d0d8d | -7.1274 | -43.1009 | 2026-09-23 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 9bacace1-8fed-31ff-870f-f0b2761ff85e | -6.5941 | -43.7333 | 2026-09-23 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b490c101-5676-3c54-982c-62fb9cb7f4e1 | -8.8264 | -45.9185 | 2026-09-23 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |


[Clique aqui para ver as próximas entradas](README140.md)
