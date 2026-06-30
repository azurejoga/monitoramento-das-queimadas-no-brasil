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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52f29684-2f51-35d9-9e26-a0f5539a1dd2 | -10.53303 | -48.16055 | 2026-06-30 00:22:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b6b66d9b-0d11-3b9a-9386-b3eeb829d7b2 | -10.2853 | -50.18352 | 2026-06-30 00:22:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3a58e24d-cd99-3626-b8f8-39b12f11c245 | -13.25654 | -56.79144 | 2026-06-30 00:22:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 4aac4e1f-cfec-3b17-b71f-c5f45abf3bd8 | -10.12747 | -52.41182 | 2026-06-30 00:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 4ad37fab-3f6e-3916-b434-2fb1bf487a87 | -10.13631 | -52.41055 | 2026-06-30 00:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 077e740d-877f-38aa-ac51-6e355ed85f12 | -10.90949 | -56.86195 | 2026-06-30 00:22:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f19e218c-d635-3438-a1cc-d0005d949c07 | -10.12625 | -52.4029 | 2026-06-30 00:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 880286aa-8f9e-33bc-afd2-ba7dcf1d30c1 | -13.27709 | -49.77611 | 2026-06-30 00:22:00 | TERRA_M-M | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 13d9f186-50ca-3195-a8a8-12daa7b64061 | -11.93343 | -57.70071 | 2026-06-30 00:22:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7032b286-5843-35d6-ac4e-1c111039d89c | -13.27008 | -56.80618 | 2026-06-30 00:22:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5df6dea9-0f62-365f-ab4b-beb10bc07f8d | -9.33012 | -58.02856 | 2026-06-30 00:22:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0d82d06c-8189-3791-a9a3-adc8cd54f58b | -9.33534 | -58.02161 | 2026-06-30 00:22:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 96f58e79-fc83-3282-9e84-b52cef3b03c6 | -9.44723 | -50.83602 | 2026-06-30 00:22:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1378f3ac-61fa-3583-83fe-4befebfc29dd | -12.5041 | -48.26444 | 2026-06-30 00:22:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c8ae9989-6f96-39e8-a329-e090edd39820 | -12.19545 | -52.86091 | 2026-06-30 00:22:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 25b9b5ab-0c88-3f5b-8c15-12515fda1844 | -7.63422 | -50.02608 | 2026-06-30 00:22:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 652baf09-5947-3140-b571-793e65a1c3c7 | -9.15642 | -58.29472 | 2026-06-30 00:22:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c94754e9-2ce6-3cf3-ad99-41c0b3020f04 | -9.32792 | -58.01142 | 2026-06-30 00:22:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| be9ada38-21e6-3ea4-a0d8-af2fcedc935f | -10.37491 | -49.59174 | 2026-06-30 00:22:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bc515c5c-c6ce-370c-b81f-2717dc1463ab | -12.84591 | -44.39275 | 2026-06-30 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| f07fa77c-5bf0-38e1-a4a4-ade387afed3c | -12.43956 | -58.48235 | 2026-06-30 00:22:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| cfe9e477-eaff-3c01-9a6b-b0c6ebaf3fbe | -11.63124 | -59.01301 | 2026-06-30 00:22:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 00f40702-b79f-3d9a-9a02-0f01b704cbc7 | -11.21563 | -54.34401 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 2336bc95-df90-363b-816f-a6e4ff97e839 | -9.74947 | -49.02205 | 2026-06-30 00:22:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 5dde49d5-a431-3f44-9620-214fa6d989af | -13.70458 | -47.87419 | 2026-06-30 00:22:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 97d8d293-df25-3df4-acc5-b26a324a1e5b | -11.4656 | -49.55451 | 2026-06-30 00:22:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 777a9ffb-5ee5-341a-8d43-d823dc0f877a | -7.40623 | -46.83517 | 2026-06-30 00:22:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d1af00fb-83bd-33b8-943b-bf3124cb1124 | -12.09711 | -52.00291 | 2026-06-30 00:22:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 401b3be4-3c5c-3d1f-8b36-c6ab9edf3ee1 | -12.22086 | -56.55025 | 2026-06-30 00:22:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 5a4cb4ab-b41e-348a-aef3-8025017aebe3 | -11.23763 | -54.32421 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a8b638f1-36cf-3d1c-83d7-4d555666c4c0 | -12.20442 | -52.85964 | 2026-06-30 00:22:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 68945f4d-f201-3619-8fbf-839561ba0c5b | -9.12749 | -58.26205 | 2026-06-30 00:22:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| db87d0b4-f672-32bc-913c-0217e8bf96c9 | -10.33607 | -50.15939 | 2026-06-30 00:22:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| df8f7ce1-f4a9-30f3-bbe1-e9809d858b82 | -12.20567 | -52.86891 | 2026-06-30 00:22:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| d17ec239-94c9-374b-a54f-5cbe03114677 | -10.14392 | -52.40036 | 2026-06-30 00:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 09058c44-1926-3faf-bbcd-174b5d2c6392 | -11.58273 | -47.93255 | 2026-06-30 00:22:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ee286a5e-0773-31b8-a89b-863a906ea942 | -11.94166 | -57.7052 | 2026-06-30 00:22:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 4100b71a-c9e8-3d62-adcc-95e5c1d1a678 | -11.04261 | -55.75668 | 2026-06-30 00:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d8e77fac-2d28-3b2c-bcd0-99549d63876f | -12.51609 | -48.28142 | 2026-06-30 00:22:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9bbf2514-552b-35bb-923e-0e7535f32b5d | -6.30036 | -43.63942 | 2026-06-30 00:22:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 5fcb448d-6b88-3098-aa69-84781dfc8b7b | -12.45516 | -58.50209 | 2026-06-30 00:22:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 0539da53-5e47-389b-aa5f-a1e1f8fb85b9 | -10.59138 | -55.42403 | 2026-06-30 00:22:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 21bf9b96-6669-3df5-8763-fb4e102074aa | -14.91431 | -50.72835 | 2026-06-30 00:22:00 | TERRA_M-M | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3bcb28b1-05c8-3f74-8c9f-81f757bc56ba | -11.92282 | -57.40046 | 2026-06-30 00:22:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| c6dcefe1-5c19-37b9-a326-50daa2ad00d1 | -12.84974 | -44.4155 | 2026-06-30 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 57fb365c-7a72-397d-bb2f-9e042dd0e32b | -8.70188 | -50.71124 | 2026-06-30 00:22:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 425f02fd-cae8-319a-b8ec-a18e91823aad | -10.14514 | -52.40929 | 2026-06-30 00:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| d8be9456-43ee-3e84-a11c-c3dc64714ff9 | -11.10856 | -54.15672 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0f7e2609-3496-3c59-ae78-b8923090337e | -9.45767 | -50.84415 | 2026-06-30 00:22:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6d624de4-955b-3a9d-9703-7342d94dc665 | -7.64388 | -50.0246 | 2026-06-30 00:22:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e7cb3570-888b-326a-8a4a-b6223e2cc1c0 | -7.4287 | -49.88042 | 2026-06-30 00:22:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a241ba2d-92d6-33b5-b5d1-e753e0270524 | -11.04421 | -55.76908 | 2026-06-30 00:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 56f29fe4-bb17-3e95-bc72-4a2318483e95 | -11.88938 | -57.11908 | 2026-06-30 00:22:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 986e8f29-8daa-3512-bd9f-0aff5825a85e | -9.32332 | -58.02306 | 2026-06-30 00:22:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e81e1fcc-7e35-363c-b354-87583a73450b | -14.95397 | -52.85979 | 2026-06-30 00:22:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3e08e2b0-3d5e-3584-a5df-5c69b2bae18d | -11.05456 | -55.76777 | 2026-06-30 00:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2a93dd35-9298-381d-88b5-387e2dedd0d4 | -12.51425 | -48.26942 | 2026-06-30 00:22:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 389d4ba7-7572-3152-835b-fa136b708573 | -11.9355 | -57.71865 | 2026-06-30 00:22:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| c165463e-4220-30c2-aa78-4a3258037082 | -11.23181 | -54.3208 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 810d0345-6108-3833-9764-cac0f5a22d14 | -10.77079 | -54.11914 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2f42242e-8a5d-3fff-b680-5b67fc270d3b | -12.45266 | -58.48071 | 2026-06-30 00:22:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 5cd2a6be-97c6-3217-87c8-6580362724f0 | -11.89129 | -57.13513 | 2026-06-30 00:22:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 2b23a50a-874e-3936-890b-7698d703f82e | -12.44203 | -58.5037 | 2026-06-30 00:22:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 3789ec88-a6a9-3dc6-9a69-5cc885410767 | -9.14398 | -50.90882 | 2026-06-30 00:22:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e8e09a47-630e-32f0-a941-44b70ddebf14 | -8.71109 | -50.70981 | 2026-06-30 00:22:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 5c4007bb-6d9a-3562-8d98-e636bfaade89 | -9.20032 | -45.31763 | 2026-06-30 00:22:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| aee76f16-7d49-3560-84ba-77498b7bd9b5 | -11.21428 | -54.33373 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d5c92964-4a1e-372e-aae7-c72fb9a1f7bd | -11.78159 | -47.56862 | 2026-06-30 00:22:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 92ff3793-ccbe-372f-84d8-a7a51987d89c | -11.92946 | -57.70673 | 2026-06-30 00:22:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d6917bdc-44d6-37b6-ad39-8799d6009628 | -11.05098 | -55.76195 | 2026-06-30 00:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8911065e-e2a8-353e-8c5f-3036b87686fe | -11.22152 | -53.83546 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4936746d-0f04-3952-8e8e-350fdbc35055 | -9.6122 | -56.92741 | 2026-06-30 00:22:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f5e3ffda-b72d-3cb4-9c91-7d8f8c220c68 | -11.23044 | -54.31052 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.6 |
| ff009bd9-c6a0-3370-a141-70cc60e9b800 | -9.60114 | -56.9288 | 2026-06-30 00:22:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 997bfd2f-e872-300d-9c9a-930b1fceed6d | -12.85176 | -44.34475 | 2026-06-30 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 627a110f-17aa-3f1d-9e6c-55a4b2c9a453 | -10.30332 | -57.14073 | 2026-06-30 00:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 27ee0f8b-5844-3918-b9da-80a4edfe6613 | -10.69664 | -49.60452 | 2026-06-30 00:22:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 0c308829-4fb2-3a31-b25f-12d7a1ec5da5 | -9.44857 | -50.84552 | 2026-06-30 00:22:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 541a1c38-9aa6-3ec9-aac5-aa3ade7d75d7 | -8.70326 | -50.72096 | 2026-06-30 00:22:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cd53bade-3778-3e0d-8538-74143c11b3a7 | -14.19591 | -57.43861 | 2026-06-30 00:22:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 0fffcaef-01b4-3f0d-a34b-71185d08e83c | -10.76949 | -54.10918 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 22fea8fa-92bf-3e16-90bb-f05bbd70b9bc | -11.221 | -54.31179 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| fd1b70df-05a8-369b-a25d-3ec6e56dba68 | -12.22267 | -56.56494 | 2026-06-30 00:22:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 589f63d9-6b5f-3bc8-a3a3-410b13aee814 | -10.13508 | -52.40163 | 2026-06-30 00:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| de9763a8-f49f-3eb7-815e-8d55897eb3c9 | -10.30139 | -57.12553 | 2026-06-30 00:22:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a8c85dfb-39e2-3071-812e-b06db9abedfc | -11.15665 | -49.19621 | 2026-06-30 00:22:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 93fd1b50-263f-332d-b32c-b9dc5057152b | -8.71245 | -50.71953 | 2026-06-30 00:22:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 745fd734-1d49-3d9d-9aee-8531539dd848 | -10.69819 | -49.61505 | 2026-06-30 00:22:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| c7bbe264-b08f-390a-b9af-fc021b9655a3 | -11.79617 | -57.00676 | 2026-06-30 00:22:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 5e06ea0c-b760-35f9-b0ba-58430b238b05 | -11.90063 | -57.3745 | 2026-06-30 00:22:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 93aca4af-109d-303a-9582-49d59734efd3 | -11.22236 | -54.32212 | 2026-06-30 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 296a2573-2535-3e74-85a0-52a39ff5f3d2 | -12.20969 | -56.55173 | 2026-06-30 00:22:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| d8b81a40-8533-3b7a-b4e4-540bf0501df9 | -6.26359 | -49.06609 | 2026-06-30 00:24:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| efaff40d-8401-37c9-a99c-6fbb62dfa0cc | -5.80825 | -45.06494 | 2026-06-30 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 196ba1d9-d7e3-3f61-b100-88498187ccf2 | -5.63022 | -44.29885 | 2026-06-30 00:24:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 9e1d59cc-69df-3a4a-8eb3-fa3a6a3796db | -5.62494 | -44.2943 | 2026-06-30 00:24:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 918d942a-96d3-3d6a-9313-7bbf3a0b2c0e | -6.92237 | -51.94843 | 2026-06-30 00:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 293ed2ed-eb3d-3007-963b-5840c76f2de2 | -10.1388 | -52.4017 | 2026-06-30 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 47d68dce-cec0-359f-a79f-8431284d863f | -12.4462 | -58.5023 | 2026-06-30 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 42abd365-0329-31de-9319-158f8b4e9ca4 | -11.2279 | -54.3036 | 2026-06-30 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |


[Clique aqui para ver as próximas entradas](README3.md)
