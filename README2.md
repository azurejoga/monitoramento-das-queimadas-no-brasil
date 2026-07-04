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
| babb01d5-339d-36c3-9073-ace778f8211a | -10.93 | -43.0438 | 2026-07-04 00:09:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d7c6b6e8-3226-3571-ad77-d783736b8841 | -11.3218 | -54.4617 | 2026-07-04 00:09:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bafce19-5ffe-35cc-88c1-b8d5c3e090b0 | -6.1955 | -45.7589 | 2026-07-04 00:09:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd368640-5314-3122-be61-fef412619d20 | -18.9484 | -50.6245 | 2026-07-04 00:09:00 | METOP-B | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 00481e71-f706-35d7-8be5-b242afe25db4 | -4.2932 | -48.338902 | 2026-07-04 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5bda785-ec1d-3429-a701-612140816ff8 | -2.3611 | -47.145699 | 2026-07-04 00:09:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2032e0b3-fa15-391b-96a4-56365a0b37a1 | -6.1936 | -45.750401 | 2026-07-04 00:09:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34497dc9-22c4-3b73-bada-a09a87476b70 | -21.2008 | -48.5924 | 2026-07-04 00:09:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a648eba2-3a54-3c68-83a4-60d97fdc4b01 | -5.4281 | -44.636501 | 2026-07-04 00:09:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8142d96-7e53-33b3-adb9-c5250ec8869d | -9.2634 | -46.441601 | 2026-07-04 00:09:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea63d557-4105-35ad-869e-85293b98dd67 | -12.7562 | -44.502701 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f3d8e0c6-36a8-3e7a-8d6b-42f68dee175d | -5.3192 | -43.562599 | 2026-07-04 00:09:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c05a0b0-d5de-3032-a5b7-7d95e5c41011 | -8.6809 | -54.549198 | 2026-07-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53a9d4d8-6bf5-3e0a-bfaa-f0ebbaf28803 | -21.903799 | -48.478802 | 2026-07-04 00:09:00 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6a776a05-1cc1-300e-9c1f-c09410c80d52 | -4.1366 | -48.8284 | 2026-07-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80c01983-c1fd-376f-a255-1c3530c7e8b7 | -7.5169 | -49.514301 | 2026-07-04 00:09:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b669c5c8-b0cb-3cf2-a602-fdec46dd5d88 | -7.803 | -45.2206 | 2026-07-04 00:09:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7aa72235-c352-3239-85fe-144e9fe12df3 | -7.5185 | -49.521198 | 2026-07-04 00:09:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d45f2b4-6466-3e6c-b2ab-e33187fe48cc | -20.458799 | -41.611198 | 2026-07-04 00:09:00 | METOP-B | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8223d9b4-52f3-3c35-aa82-f423387d04f2 | -5.4305 | -44.646599 | 2026-07-04 00:09:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e96e0c0-01f3-303f-ae6e-dbde3c9b504f | -6.9301 | -43.708099 | 2026-07-04 00:09:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eadd2867-ab50-3882-bfd2-01812cc0d578 | -5.3067 | -43.553101 | 2026-07-04 00:09:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d636d85e-8f7d-3133-89e7-7bc64f5e4db8 | -12.5256 | -48.284698 | 2026-07-04 00:09:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c31009f8-cda8-3da5-aad1-8dfc81f23545 | -8.0863 | -46.706799 | 2026-07-04 00:09:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b766a783-9f35-3082-bedd-a97fcef482cc | -3.5124 | -48.034302 | 2026-07-04 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0465e37-039a-387f-8010-89cf30c34275 | -7.0029 | -42.763199 | 2026-07-04 00:09:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d9045029-73ca-3a69-ba88-e2c7b3cfaf52 | -5.4328 | -44.656601 | 2026-07-04 00:09:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 467bcf22-f11b-33ac-b29a-3f15cf870664 | -18.777901 | -47.623299 | 2026-07-04 00:09:00 | METOP-B | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 162dcf65-c846-3c6a-89ae-c6bdf6c49d04 | -12.7504 | -44.5219 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b439c7a-cf40-3fc2-8920-f75b17ef0c62 | -8.0299 | -46.239101 | 2026-07-04 00:09:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4d685ce-a5f3-3b0d-b378-89f60a6ff04b | -12.7466 | -44.549301 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65449e52-36eb-360c-9ce3-16791e67b735 | -4.1464 | -48.826199 | 2026-07-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46719f9e-a96c-34e9-a485-7d3986a8b942 | -12.7621 | -44.527802 | 2026-07-04 00:09:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c85d1cd-82ce-3102-9456-60a34732302d | -10.9732 | -43.696201 | 2026-07-04 00:09:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fdafcee3-1fba-3248-987b-dfeb871b30a9 | -3.4259 | -41.714 | 2026-07-04 00:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| e8162cad-993c-3ef8-acad-74f78e022ef3 | -10.9401 | -43.0355 | 2026-07-04 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.2 |
| f634bc16-b589-3790-880f-7c0ab1000e9e | -12.7548 | -44.5428 | 2026-07-04 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 8208a3e3-9a52-3036-934e-1b3dbabb5754 | -10.9397 | -43.0593 | 2026-07-04 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 467b013c-94d7-3e3d-824a-fff440191ef9 | -4.1486 | -48.8306 | 2026-07-04 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6ceaa8bd-a31d-3697-8140-a249a6c53aa4 | -11.3202 | -54.4792 | 2026-07-04 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 4788afe7-7555-32f6-8f97-c27768a34474 | -12.7553 | -44.5194 | 2026-07-04 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 09cc59a9-f38c-315d-a03c-e8f73bd8e75e | -10.9205 | -43.0622 | 2026-07-04 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 4e9ef72a-9400-36c7-985c-daf131e2d4f9 | -12.7544 | -44.5662 | 2026-07-04 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 4db3220f-fa92-3e8d-9dee-561ee68245ba | -10.9209 | -43.0384 | 2026-07-04 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.1 |
| 100f617c-7897-36c0-8fe9-4e83aad3d107 | -12.7548 | -44.5428 | 2026-07-04 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| c4129302-815c-3064-933c-4e8f9055c89c | -10.9401 | -43.0355 | 2026-07-04 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| a122ab46-0d23-3946-8391-86b5a9fdfe28 | -12.7553 | -44.5194 | 2026-07-04 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ec9d499a-e8b9-3227-86a2-21b539a14139 | -11.3202 | -54.4792 | 2026-07-04 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| aff10ea8-0b2e-3a2b-aeb9-7b536dd46c95 | -11.3205 | -54.4588 | 2026-07-04 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 10df1a23-62d3-30f7-ab27-38737b38d43d | -10.9397 | -43.0593 | 2026-07-04 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 498bdc36-bd68-3207-b804-427834e7da5b | -10.9205 | -43.0622 | 2026-07-04 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 3074fb48-2922-33c0-810a-86c597831dc9 | -10.9209 | -43.0384 | 2026-07-04 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 292.2 |
| e4ffbd64-8849-37a8-84f4-8bd67508ec3f | -12.7544 | -44.5662 | 2026-07-04 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| a89bff29-377e-3de3-8df2-1401dd4389ce | -10.9209 | -43.0384 | 2026-07-04 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 225.9 |
| 978db024-0075-3b12-8dd1-4506fa5dae8f | -11.3202 | -54.4792 | 2026-07-04 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2838a56f-928c-38dc-a667-ca180aba3f97 | -12.7548 | -44.5428 | 2026-07-04 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 64999d31-3781-356a-a0a6-3b248b7de786 | -3.4259 | -41.714 | 2026-07-04 00:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| b354b74c-84df-3dd2-811e-e6106322fd73 | -12.7553 | -44.5194 | 2026-07-04 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| cff0104e-131e-32a4-9a0d-dbc0df4038eb | -10.9205 | -43.0622 | 2026-07-04 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 224.4 |
| bca29a4b-76ee-33bb-8bcf-d1ca7d3510b9 | -3.4072 | -41.7149 | 2026-07-04 00:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 35.9 |
| 5c313ebc-4675-3b80-90b5-0b2d29064e01 | -10.9397 | -43.0593 | 2026-07-04 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 28b9fe3c-ac8c-3faf-a505-748018a4ad81 | -10.9401 | -43.0355 | 2026-07-04 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 976f2cc7-ac2c-31e7-be73-e4728eb4bd06 | -11.4596 | -46.576599 | 2026-07-04 00:36:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 870ec4ce-698c-3f86-9b76-addb4723910f | -5.323 | -43.558399 | 2026-07-04 00:36:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35fd2076-fa7f-30da-a918-0d7f1b1f1b1d | -12.7608 | -44.5527 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2eacc465-7962-3367-bbf1-ecc714d75bb8 | -4.2909 | -48.363201 | 2026-07-04 00:36:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abde8a62-7ea3-33c2-acbf-ae3b7b07f27b | -8.0381 | -46.7145 | 2026-07-04 00:36:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99b3a984-c53a-34ec-97f0-25a9d0db6bcb | -5.4345 | -44.6478 | 2026-07-04 00:36:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97e45bdc-876f-3162-bc21-50e278e18052 | -11.3175 | -54.481201 | 2026-07-04 00:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d853899-8d96-3dd6-8ca2-dacead20b8b3 | -3.4264 | -41.7234 | 2026-07-04 00:36:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 47e05bc3-902c-399e-943d-01cd0b87adbd | -4.3439 | -48.958801 | 2026-07-04 00:36:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49f4dc26-21a2-301b-82aa-b76f385ddec7 | -4.5735 | -48.020302 | 2026-07-04 00:36:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1bb857d-a5f2-3a0d-a659-3a32d5a62b1d | -12.5267 | -48.282501 | 2026-07-04 00:36:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3fce0c9-9bbd-3aa6-8cf9-92ff18d41aee | -12.7425 | -44.518299 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5bec1cad-f8c0-3b90-9cbc-c40f33db5ee6 | -4.8799 | -49.643002 | 2026-07-04 00:36:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 699dc83c-d9c5-38db-8ab8-887f04db59bf | -12.7625 | -44.560001 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee1bce1b-eff1-3b7f-be94-82053fbbac1f | -20.028999 | -48.2756 | 2026-07-04 00:36:00 | METOP-C | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac5bc121-48cc-3008-8cc7-6f2564b9dbdd | -20.466499 | -41.617599 | 2026-07-04 00:36:00 | METOP-C | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a557c9f1-1136-30a0-90fc-be4cae9f6448 | -21.2043 | -48.607101 | 2026-07-04 00:36:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bfed9fac-4b10-3a18-93a7-f0b691f7678c | -9.4423 | -40.329102 | 2026-07-04 00:36:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0e2f133e-d3aa-3ccd-8b87-b2ad616ec607 | -12.3202 | -46.7402 | 2026-07-04 00:36:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1638738-7f12-31d3-84d2-107b2ff80b77 | -12.7591 | -44.5453 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36f81365-1e3d-3690-a1e7-d1d68a49d4b2 | -12.7638 | -44.520901 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fffd8546-6cdb-3983-8754-a2a3da33bd67 | -12.7523 | -44.515999 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e45e3662-ef91-30e5-b788-eb0f20bbcf24 | -8.0397 | -46.721401 | 2026-07-04 00:36:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b33d080e-d257-3bb6-b24b-aa05a50d8bbd | -7.5075 | -49.522301 | 2026-07-04 00:36:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8974fb56-0835-3369-80d7-07d678b88abb | -2.3637 | -47.151001 | 2026-07-04 00:36:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae644ceb-9314-39f8-8bec-fb4a3bc37a62 | -12.754 | -44.5233 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f3b5c66e-2f2d-3f55-9450-13d7d631dab0 | -12.7557 | -44.530602 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2465ee3c-64fa-31e8-80fd-7670f0412a62 | -20.4645 | -41.609299 | 2026-07-04 00:36:00 | METOP-C | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbef2d80-3d31-3246-b0df-afe8410785aa | -3.433 | -41.708 | 2026-07-04 00:36:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0b960c3b-6151-380b-9446-e20a3409af40 | -6.9081 | -43.719501 | 2026-07-04 00:36:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 34bb5f8d-354f-3dea-ab13-79658cb6da4d | -4.0153 | -48.0588 | 2026-07-04 00:36:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe754bee-b3d8-3fff-98ed-b40498c10acf | -10.9283 | -43.040699 | 2026-07-04 00:36:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2722c14c-8ec9-3cbb-b42f-37d60f378265 | -5.6555 | -49.110298 | 2026-07-04 00:36:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 593f3e4a-1c77-38fe-a419-eb9ff90823e5 | -10.9324 | -43.058102 | 2026-07-04 00:36:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4080767c-df39-385a-b3b8-71e79f757992 | -5.8047 | -43.633598 | 2026-07-04 00:36:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4817a69b-4556-3532-ba83-1fe69e3ca298 | -6.9395 | -43.7216 | 2026-07-04 00:36:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a21e7c3d-ff19-3116-8f4d-abbbb890ba63 | -12.7655 | -44.528198 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f55e007-0abe-34a4-9043-953da3aaef5c | -5.3252 | -43.567799 | 2026-07-04 00:36:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
