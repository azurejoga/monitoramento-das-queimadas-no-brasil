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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dab79da4-4855-3a10-992e-c3d290ea8244 | -15.8352 | -53.5798 | 2025-10-26 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 455835f6-38f2-31c7-90d5-da10a828b2ac | -11.1419 | -55.1869 | 2025-10-26 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 118be4fd-5412-3e40-afe1-d8dc8b682612 | -6.4053 | -45.758 | 2025-10-26 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| fb20b53e-f0b6-31a2-a303-cc7e3d7d979d | -4.0338 | -46.1965 | 2025-10-26 14:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 94e11c3e-8234-3cdb-bdce-28329df97641 | -5.5465 | -41.3852 | 2025-10-26 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| bee63a10-d5d7-32f1-b18e-2d28f8284d5d | -6.4395 | -42.3383 | 2025-10-26 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 00c2a243-edba-3abe-894c-fbf1876275f0 | -4.1846 | -42.9745 | 2025-10-26 14:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 82bbe867-65bb-3925-aa97-42cdb7328afe | -7.1581 | -45.4253 | 2025-10-26 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 0cb33fb3-1fdd-39e2-a16e-91fdcfee79d7 | -3.9166 | -44.0097 | 2025-10-26 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| c96f516a-2020-3b87-b6b0-eb8c2c46bef3 | -9.265 | -45.5989 | 2025-10-26 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| a0bcad70-4d77-30b3-a57d-b0bd8e3c3c8a | -8.4475 | -47.626 | 2025-10-26 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 213.7 |
| a2bc256e-c2f9-3f6a-a83a-e00d29004952 | -7.1135 | -47.9379 | 2025-10-26 14:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 026ade1c-3980-34d0-ad01-3216d4b9d105 | -7.8884 | -47.259 | 2025-10-26 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 97b5b4ee-39c4-37bf-881a-f72feaf5cef3 | -12.363 | -48.1238 | 2025-10-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c7fd9d9a-161a-3137-ace5-70684efb2d88 | -13.2777 | -54.3882 | 2025-10-26 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 382.2 |
| 1837aa64-86c5-3b0d-a4e2-c92e0bddfd62 | -11.327 | -53.9254 | 2025-10-26 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 0f0bbdc6-a7eb-3dd5-9cde-f7e305875a5f | -4.912 | -43.2337 | 2025-10-26 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| e9679693-4d01-3087-815e-cc6d1796b3ab | -6.3866 | -45.7594 | 2025-10-26 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 8e475e19-4067-35d8-9727-e5a7a62de40e | -3.9396 | -43.3146 | 2025-10-26 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 94bd8946-ada4-35b2-a562-1448e81dc1c9 | -6.7274 | -45.3715 | 2025-10-26 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 58b1bfe2-5f86-30d1-8409-2c658f073a49 | -4.3239 | -41.7839 | 2025-10-26 14:30:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 117.2 |
| 21c05e7a-dcca-3ee9-84a3-959d6e73f3d5 | -4.3426 | -41.7828 | 2025-10-26 14:30:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| c10c27aa-4ee7-39e5-8b96-d0e2d52cfe34 | -12.3634 | -48.1016 | 2025-10-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 46405148-7528-383e-b2c3-4de1e89f890f | -7.8138 | -43.9894 | 2025-10-26 14:30:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 0895ca7c-9ff1-32af-94f6-ec3e1f3d5323 | -9.284 | -46.9894 | 2025-10-26 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| f500c300-9677-3bce-98cb-a8bc70863e00 | -3.6533 | -41.2464 | 2025-10-26 14:30:00 | GOES-19 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 157.8 |
| 9f655309-715c-3c3f-bc49-d8875de6522a | -12.2977 | -47.4658 | 2025-10-26 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 91c5fbce-b5aa-3b19-8db2-65065a8cef80 | -4.5712 | -46.5022 | 2025-10-26 14:30:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8b877921-14a0-34dc-859c-ca1c4c31bb6f | -9.2653 | -45.5762 | 2025-10-26 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 575edc77-bfed-334d-a3a4-9fa85d636028 | -8.0446 | -46.7353 | 2025-10-26 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| fa4c79fc-473e-362e-bfe3-8024552879c7 | -13.6249 | -48.4323 | 2025-10-26 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 8918a3f3-a7cf-3430-bb9b-7292b5a9fde8 | -13.2586 | -54.3902 | 2025-10-26 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| d0e40057-9e6e-3742-a492-3e01f52cbf26 | -3.7898 | -43.3921 | 2025-10-26 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b1f80640-6169-35ff-b2b2-cec428ce78eb | -6.212 | -42.5243 | 2025-10-26 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 0ba98202-09bb-38e7-b736-d23472670905 | -3.9822 | -45.4838 | 2025-10-26 14:30:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ec0f444a-474f-34ef-83c7-e3af1cd8b99a | -7.8413 | -46.4423 | 2025-10-26 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| a61e6b60-9cfb-3a11-b7ac-9f14e37e5a70 | -8.559 | -47.7252 | 2025-10-26 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e57073c4-d3e8-39fe-a1fe-292d6f3aa134 | -7.2382 | -44.964 | 2025-10-26 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 33971c5e-37a6-3b33-87b6-d737aaa452cc | -14.2978 | -51.7713 | 2025-10-26 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 5aa023c1-32ed-38a8-897a-d728bb38ca55 | -6.3866 | -45.7594 | 2025-10-26 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| a7542ef2-e000-3a48-bcfa-28cdcff5b1e3 | -3.7024 | -42.3892 | 2025-10-26 14:40:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 114.3 |
| 1edfd160-42f9-3359-8bdf-d962e73a796b | -17.4311 | -46.884 | 2025-10-26 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 138.4 |
| a8c4b552-918f-3c16-bed5-b2c736ea874d | -7.8536 | -45.3839 | 2025-10-26 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 78fc155b-d595-34d1-aa82-8f7153840b1d | -3.964 | -45.4173 | 2025-10-26 14:40:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 73c947b7-c46a-36d7-aa3a-f025b96d45e9 | -12.363 | -48.1238 | 2025-10-26 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 20f2c377-04c9-34b8-a037-963fb3c8ed78 | -3.9166 | -44.0097 | 2025-10-26 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 15170b06-d8a7-36af-94d5-8a873d166a14 | -3.771 | -43.4162 | 2025-10-26 14:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| cf133d3b-32be-3733-b95b-c1f0045f4181 | -7.7783 | -45.3911 | 2025-10-26 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| b34ff0dd-74a4-32ca-a3b4-d161defd14bb | -6.7274 | -45.3715 | 2025-10-26 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 6502b7df-6b02-3a8b-baa2-26c99ea7e6a0 | -2.9181 | -42.3544 | 2025-10-26 14:40:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 57533bb0-f433-3d3d-88ba-1576b61eaa31 | -11.3457 | -53.9442 | 2025-10-26 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 532e1665-fc53-3328-8cc1-9c12ce7e04e4 | -9.5267 | -45.8184 | 2025-10-26 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| ed175aa0-1862-3efe-bc48-af78d104fdf3 | -10.4068 | -45.3014 | 2025-10-26 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| de3f5674-e745-3cac-a992-f7cac6d3182d | -7.7971 | -45.3893 | 2025-10-26 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b794b5f5-0e43-3965-a4ec-d7d6a140db80 | -11.346 | -53.9236 | 2025-10-26 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| b3cef1c4-ce03-3227-a763-6a5ed86dd134 | -7.8884 | -47.259 | 2025-10-26 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 754bdc30-ad9d-3efd-963f-4f30a1066778 | -3.6531 | -41.2705 | 2025-10-26 14:40:00 | GOES-19 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 156.5 |
| d970d410-35a3-37d5-a872-c28af4d5d2d5 | -12.3863 | -50.1947 | 2025-10-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 5a181a13-5249-325f-b442-48a81c21ef11 | -4.8935 | -43.2115 | 2025-10-26 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 9d682705-ba52-34cc-b1bb-42f9859cca22 | -8.5781 | -47.7015 | 2025-10-26 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 7dc6f7f6-8576-3eab-b8f3-91450994a6b1 | -11.4042 | -46.058 | 2025-10-26 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 321.1 |
| 42a8dc3c-2be7-31b8-a90a-69766ec504d8 | -9.2039 | -44.5536 | 2025-10-26 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 7180cfaf-0e3d-3e32-a930-6d9679fa0398 | -13.8949 | -48.4364 | 2025-10-26 14:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 7dd66e2c-728d-3c1f-9dca-2e1ed7e069f2 | -9.2728 | -46.4101 | 2025-10-26 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 5801dfcf-e5f9-381b-985a-66d3c294118b | -6.802 | -45.4105 | 2025-10-26 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 7e7b9554-f85c-3670-a697-5f80e0376a87 | -3.6533 | -41.2464 | 2025-10-26 14:40:00 | GOES-19 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 200.2 |
| cd34d967-140e-3195-b1c6-5fa58eeabee3 | -7.8413 | -46.4423 | 2025-10-26 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 215857d3-8e86-3a34-9b05-c8bb19597bb9 | -9.2542 | -46.3897 | 2025-10-26 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 7c03148a-5b42-3d34-87b1-c901a5af09e5 | -6.92 | -44.8782 | 2025-10-26 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 7f4f8ce7-9157-39d5-9f3a-0f0b068c35bd | -10.3604 | -47.1131 | 2025-10-26 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 79ae0b19-3af3-3e8e-9b73-0b5ce76190ed | -3.1073 | -41.872 | 2025-10-26 14:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 4f178f64-c99c-3dc6-b0cd-b75850b7982c | -4.2019 | -43.1838 | 2025-10-26 14:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 7851ce29-19aa-35bd-b152-8ec47c3ff5df | -12.2348 | -50.1272 | 2025-10-26 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 4e68d8ac-0c4a-3510-865a-7a77aa1e1458 | -12.3867 | -50.1731 | 2025-10-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1ca53d9e-f240-3e59-9f33-0f74cb354361 | -15.2649 | -50.7535 | 2025-10-26 14:40:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 4bfda9dc-62ec-35e2-8c1c-cd0146d48ee5 | -14.8273 | -52.4244 | 2025-10-26 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7782f224-7950-3fbc-8190-b867a339728d | -3.7896 | -43.4153 | 2025-10-26 14:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 30427361-59bd-3748-9181-21d9a740f797 | -4.3237 | -41.8078 | 2025-10-26 14:40:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| cad73109-5e81-3bb4-b010-0df86b83964f | -8.5593 | -47.7033 | 2025-10-26 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| e0bcb5f6-811c-3ec0-8943-b8f0aa997ee1 | -6.3864 | -45.7819 | 2025-10-26 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 1aee7c67-0502-3b1b-9f71-923f8890dc5d | -12.3634 | -48.1016 | 2025-10-26 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7ef139b4-1196-31ff-bc24-2510e01a3c66 | -8.563 | -47.3948 | 2025-10-26 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 954e98a6-88cc-3a73-8a0b-b2e22e419596 | -11.3268 | -53.9459 | 2025-10-26 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 62ef85fe-bf45-34a1-b671-e6ad24bf502a | -9.5264 | -45.8411 | 2025-10-26 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 961d1b78-d8b9-3c00-a54f-f017519c975f | -7.8348 | -45.3857 | 2025-10-26 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 8edd1620-28c5-388b-8ab0-775c58d50191 | -9.265 | -45.5989 | 2025-10-26 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| a6fdc45a-18ee-3d01-bf59-7a0f93a2d160 | -9.284 | -46.9894 | 2025-10-26 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 7e3a18f9-20e4-3d30-9c47-aa4fdb86a7f0 | -6.4051 | -45.7805 | 2025-10-26 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 869deaae-866f-348c-95db-65df4507cc2a | -13.4979 | -48.0067 | 2025-10-26 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| a733f920-bff5-3e04-ba6f-852df1312443 | -11.385 | -46.0606 | 2025-10-26 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| e85ba59b-1c19-39b1-8c03-f7299a516051 | -8.0443 | -46.7576 | 2025-10-26 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 1226b49a-ed7d-3af1-8699-5b0531741755 | -3.6719 | -44.4113 | 2025-10-26 14:40:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7d6b3e13-c1b0-3242-9f5e-2f61d6278c20 | -13.2586 | -54.3902 | 2025-10-26 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 8c6cea96-b61f-3727-a45f-9aa730367740 | -4.3239 | -41.7839 | 2025-10-26 14:40:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 7ed2e16b-b058-3473-be14-632bfc46d7d9 | -6.4395 | -42.3383 | 2025-10-26 14:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 13d91381-cf04-39b0-b519-61e02ee8dec1 | -11.4045 | -46.0352 | 2025-10-26 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 96dd9d36-35cf-38fa-bf3f-58446e8ee4f2 | -7.4007 | -43.8913 | 2025-10-26 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f8124050-ec26-3ba5-9b89-328cca879b81 | -4.8931 | -43.2582 | 2025-10-26 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 0bdecd6d-656e-376c-bca2-117e2871a7b9 | -7.7968 | -45.412 | 2025-10-26 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 478d194f-cc51-322b-9126-fe9149694181 | -14.9037 | -52.4779 | 2025-10-26 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 135.2 |


[Clique aqui para ver as próximas entradas](README62.md)
