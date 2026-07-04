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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 190af22d-e8ec-3b0b-9c00-7bcb0acf73a8 | -12.7544 | -44.5662 | 2026-07-04 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 3681b0c9-ef3e-31ec-8cd6-62b006824871 | -11.3202 | -54.4792 | 2026-07-04 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a4c6b974-d0c3-38fe-ad21-092c1ef31515 | -10.9401 | -43.0355 | 2026-07-04 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| da58777b-b113-3191-ab7b-c7296e74f1b1 | -10.9397 | -43.0593 | 2026-07-04 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b50791bf-6977-3342-9341-43f2f3a879d6 | -12.7553 | -44.5194 | 2026-07-04 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| f2d40597-d72c-3cd0-af20-89206d830503 | -10.9205 | -43.0622 | 2026-07-04 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 269.3 |
| f7478728-c35e-39a4-95e4-255dbf18aaa8 | -11.3205 | -54.4588 | 2026-07-04 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| d87be9a7-e601-31ec-817d-4169d53958e4 | -12.7548 | -44.5428 | 2026-07-04 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| ede88f44-e283-396e-947b-689028719aa2 | -10.9209 | -43.0384 | 2026-07-04 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 293.6 |
| 65797872-d18a-3949-a36f-2fef43dc3c62 | -4.1486 | -48.8306 | 2026-07-04 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 74316edf-8e37-3abc-b8b9-d6da334490e1 | -2.7668 | -48.562698 | 2026-07-04 00:09:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7c94c8-df6b-3979-b135-48f57623cf3b | -11.8637 | -45.5896 | 2026-07-04 00:09:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0375a103-7f8c-37e9-a677-90d0d34814ba | -20.030899 | -48.271999 | 2026-07-04 00:09:00 | METOP-B | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a7cfd71b-fb91-332c-bff6-202a8b3e3b72 | -7.8009 | -45.211899 | 2026-07-04 00:09:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ea24131d-727c-3f7e-906d-4a2e5effb6e6 | -12.7387 | -44.5158 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0aad53d0-07b1-3806-8bdf-b58d5539afc6 | -12.7564 | -44.547001 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95b2806b-783c-3a71-a911-6c41e226375c | -12.3219 | -46.7313 | 2026-07-04 00:09:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| edeec03c-4761-3b42-bb31-e777e09e9ad3 | -11.4502 | -46.572899 | 2026-07-04 00:09:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1275400b-aea3-3da7-b0d9-15b8ef373519 | -4.1479 | -48.833099 | 2026-07-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c075a5-8537-342d-8300-24cff7dd2c14 | -12.7465 | -44.5051 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a3be5f1-eb8e-3b48-8c1f-6612da607778 | -4.1381 | -48.8353 | 2026-07-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf33a79d-cc9b-3b6f-b53c-0905bca42224 | -10.9227 | -43.056801 | 2026-07-04 00:09:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 240f8f50-987d-3c4a-8f02-f85f73dfeb60 | -7.5087 | -49.523399 | 2026-07-04 00:09:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58321d79-d5cb-3047-ad87-f6d220de357a | -8.0281 | -46.2313 | 2026-07-04 00:09:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6246564f-d1e7-3610-b0ab-46b71e99b8ed | -5.3164 | -43.5508 | 2026-07-04 00:09:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71abcb53-d2b9-367e-8b53-3975654d845f | -11.3093 | -54.4506 | 2026-07-04 00:09:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e638a8b0-991c-33f1-9d2d-a06df6e34e45 | -12.7367 | -44.507401 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a37fb20-b31a-3435-ae0a-70748fc8c904 | -18.7166 | -47.528198 | 2026-07-04 00:09:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1e8cf605-806e-3987-9c2c-519e6e33a08e | -3.9942 | -48.3839 | 2026-07-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c06cf4ac-6685-3dc2-95ff-f6c265cdd953 | -20.7085 | -50.514702 | 2026-07-04 00:09:00 | METOP-B | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 23b3222a-f4da-34b9-b1ba-5fa95892ad5b | -4.5815 | -48.020302 | 2026-07-04 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00cbf09-5fd8-36a4-b253-d1c4def1feb4 | -7.006 | -42.775799 | 2026-07-04 00:09:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 21881e14-9958-3a08-a0f9-8778e282abac | -18.718201 | -47.535599 | 2026-07-04 00:09:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 549421a2-b31c-3614-b769-024ac295d12c | -10.9755 | -43.705898 | 2026-07-04 00:09:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e24523db-0103-3d83-922d-5acde1fd82e2 | -4.5799 | -48.013199 | 2026-07-04 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03271199-c26e-3933-951a-d9b7d817bc91 | -8.4524 | -51.563301 | 2026-07-04 00:09:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ce80eae-7206-32db-8575-e22ef45d61d5 | -20.0292 | -48.264 | 2026-07-04 00:09:00 | METOP-B | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a9e06c2c-aa18-30a8-bbca-f9b8906176d6 | -12.7602 | -44.519501 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10abc1cd-d8e2-3e2c-b931-d3a91aff7d6b | -10.9176 | -43.035599 | 2026-07-04 00:09:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce6c10ec-8704-30a7-b89a-77ecba930fab | -20.032499 | -48.279999 | 2026-07-04 00:09:00 | METOP-B | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f3ee0544-f507-3b30-9734-6c402bede249 | -18.774799 | -47.608398 | 2026-07-04 00:09:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5813f562-abd3-35d8-b3ec-c8bb859bfc5c | -10.983 | -43.693802 | 2026-07-04 00:09:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26aa9629-d2e8-3bbc-9c0f-c261a53f475d | -12.7485 | -44.5135 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74ed9725-9fca-3a58-8b81-31a8cb173a05 | -11.312 | -54.463699 | 2026-07-04 00:09:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d0cba80-7ab0-3be2-810e-d202ccac34f3 | -18.715099 | -47.520802 | 2026-07-04 00:09:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 13b93ed8-f8f2-3f8f-869c-af266c568a86 | -6.4258 | -43.711498 | 2026-07-04 00:09:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3cf3bff-a8e4-372d-9ae1-9dcc5b5dfc3f | -4.2949 | -48.345901 | 2026-07-04 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c6058f5-997b-3cc4-bc67-bc78118240ad | -6.9008 | -43.715 | 2026-07-04 00:09:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 53374cc6-c8d0-3e73-8844-a7b13fb14b09 | -5.4669 | -45.419899 | 2026-07-04 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0638c5c0-6088-395f-b391-095ccf00e681 | -7.5071 | -49.516499 | 2026-07-04 00:09:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0adb77e-d83c-3b66-bb7a-152945a83060 | -8.6932 | -54.559299 | 2026-07-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a61de1cf-3eae-33da-b3cc-571ac67bf1f2 | -21.210501 | -48.590199 | 2026-07-04 00:09:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3053faf-4cc9-33e0-904c-f1d4ad0e8c38 | -5.7994 | -43.6334 | 2026-07-04 00:09:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36b04e67-a730-364e-a319-1af77fe31658 | -4.3378 | -48.942799 | 2026-07-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 033c7440-265f-37cb-80b4-cea1885247fb | -10.9274 | -43.033199 | 2026-07-04 00:09:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9df66d97-b945-317d-88d0-9ea9f8b54bcd | -11.4518 | -46.580101 | 2026-07-04 00:09:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19db8f7b-a52a-3096-8ee2-6ec477f8c461 | -8.6834 | -54.561401 | 2026-07-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df0c43a-d087-3059-88ae-9c461c4e598f | -4.8772 | -49.6413 | 2026-07-04 00:09:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b44977b0-d169-3c0a-bfc7-51902d002f40 | -11.4566 | -46.556099 | 2026-07-04 00:09:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b34f850-eed3-39ca-b88f-03640f032913 | -4.2867 | -48.355202 | 2026-07-04 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8f947d-d2d6-39eb-8322-37ec4f9a1600 | -12.7582 | -44.511101 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2185321-b207-3dc8-9e27-f37163634634 | -5.3095 | -43.564899 | 2026-07-04 00:09:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b3bfd2d-e622-37a9-8b4a-1c8fb23d2c79 | -7.9004 | -48.241901 | 2026-07-04 00:09:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0b2b7af-148e-3d48-980d-72002be26eb9 | -4.3507 | -48.9543 | 2026-07-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee8fd35b-788b-3241-a502-76fc54c843ac | -12.3621 | -47.411598 | 2026-07-04 00:09:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e310e40f-f937-3e90-846c-00ae14fd3485 | -4.3393 | -48.9496 | 2026-07-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d65d51f3-c544-3317-b4fb-982f5734baef | -12.6747 | -48.213902 | 2026-07-04 00:09:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd3315ce-35a7-37f0-977c-e5f23179ad0a | -6.8982 | -43.704102 | 2026-07-04 00:09:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb50c65-91fa-36d5-845f-5197e470afca | -3.5009 | -48.029301 | 2026-07-04 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c2d1f74-8861-3f95-abb8-709f37445b43 | -8.0846 | -46.699299 | 2026-07-04 00:09:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e35753d-3993-3340-9831-c591a0f956ea | -8.4507 | -51.555302 | 2026-07-04 00:09:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2672a3e0-fa82-3e43-8814-a6b8cf4e3b40 | -3.5107 | -48.027 | 2026-07-04 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e215b3a3-3516-3aa7-a7b8-9ddfcdcf8ee9 | -12.5241 | -48.277599 | 2026-07-04 00:09:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2435525-c7cc-3c7d-9ce6-c4d1903a40bb | -12.3637 | -47.418499 | 2026-07-04 00:09:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2419643-d564-381a-8639-6ca33574cb6c | -19.8239 | -43.114498 | 2026-07-04 00:09:00 | METOP-B | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5c245153-2b7d-3777-b667-af0f94f6d967 | -10.9202 | -43.0462 | 2026-07-04 00:09:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f3da2c9-6bfb-3be8-b677-515251121490 | -4.3491 | -48.947399 | 2026-07-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 044e2829-151e-3867-8541-4c074658b160 | -10.9325 | -43.054401 | 2026-07-04 00:09:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5d5a57b-783a-340d-bee7-6e5f842e60a3 | -12.7583 | -44.555302 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 814f0bfe-dc2c-3ef2-b158-0c5c34f3ea1c | -12.7544 | -44.538601 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68b97d55-fe06-324e-b03f-e984aa5d47ee | -4.8756 | -49.634399 | 2026-07-04 00:09:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfb64ee3-3bfc-3a09-b749-21a4a12b8e08 | -4.0111 | -48.0509 | 2026-07-04 00:09:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7065c8d3-76d5-36cf-bd98-e55b244c683d | -11.3191 | -54.448601 | 2026-07-04 00:09:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4b869e6-250c-320b-adaf-a44bebcb1d10 | -4.2851 | -48.348099 | 2026-07-04 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 086e9bbf-2115-3d41-a5cc-a580732fd06a | -11.4191 | -46.572498 | 2026-07-04 00:09:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbdd1391-87b2-3ba8-9543-37ed05f1070a | -18.7763 | -47.615799 | 2026-07-04 00:09:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b6423247-0ae0-31f6-a2af-39f29e06e4fb | -5.4154 | -45.287601 | 2026-07-04 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 192931a0-d209-314d-b18a-ab828ff01ff9 | -8.6907 | -54.5471 | 2026-07-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03e3f592-363c-3e97-b3ae-9b1046cf24fb | -8.0356 | -46.710602 | 2026-07-04 00:09:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9794b35-dad5-3811-a628-6af0fc499b97 | -10.9853 | -43.703499 | 2026-07-04 00:09:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71e9598a-e7af-34e0-920b-b3998e181897 | -4.0127 | -48.058102 | 2026-07-04 00:09:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4180fde6-e4d1-38f1-a20e-7bd658b3669b | -8.0373 | -46.718102 | 2026-07-04 00:09:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc026b62-2899-33d9-89e9-610ab7530766 | -6.9327 | -43.719002 | 2026-07-04 00:09:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c44d6988-7373-3de4-a739-afdb02e5f8ed | -2.7684 | -48.569801 | 2026-07-04 00:09:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01405eff-f18d-3d7e-ac10-81a99162ce38 | -11.3804 | -47.813301 | 2026-07-04 00:09:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3be55d15-dc88-3b54-bcdb-18f7f26d91e8 | -5.4176 | -45.296799 | 2026-07-04 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b9a4e3c-7951-35b9-b2be-0f58db3c80b8 | -8.0339 | -46.703098 | 2026-07-04 00:09:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b173503-4fc6-3232-b9ec-c1cb7b921182 | -11.455 | -46.548901 | 2026-07-04 00:09:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59aca251-ff02-31c8-980f-44a95f370199 | -4.2965 | -48.353001 | 2026-07-04 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8f3873-cc54-3542-9c89-cd9681a5b072 | -11.9205 | -43.380199 | 2026-07-04 00:09:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
