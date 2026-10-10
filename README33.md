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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca02eb1e-576a-3d15-972c-e1ea5975367b | -7.06486 | -40.9535 | 2026-10-10 04:08:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9f63acf7-483e-341f-a1d8-66d55f896b52 | -3.27402 | -54.69528 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aee719f2-1821-33a2-97bc-2f1f37ce0f16 | -3.04104 | -50.33799 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 004e43da-a647-386a-b5cf-33e43f7b36a5 | -5.70726 | -41.65481 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 12b4f7c0-457f-386e-8884-d0c082b033d3 | -6.04462 | -46.41098 | 2026-10-10 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18614954-8d82-3ec3-9024-36f304f1baef | -3.38387 | -44.48512 | 2026-10-10 04:08:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| d8734f28-848d-3e09-8388-cf52c1a4d36e | -3.89449 | -52.19024 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14057658-f35f-35c6-a865-c935aee03ef2 | -8.23876 | -46.43104 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc7b2b1a-a212-34db-9bb7-ae7054b30095 | -4.15267 | -43.18621 | 2026-10-10 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33e3d9ad-cd41-3a5a-baad-68c151a78d00 | -8.99831 | -47.73932 | 2026-10-10 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 031148f6-e2d9-392d-ade6-16ca83759eae | -7.07078 | -41.59847 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f2a0234f-2379-3d31-a510-b88646d97c6a | -6.43781 | -55.28028 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d59f141-26d8-30b8-b424-c629d062f301 | -5.89165 | -43.27312 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb9970ba-092a-301d-90ea-801f38b7514b | -10.28574 | -43.93229 | 2026-10-10 04:08:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd06e61d-0134-3344-b34f-a66bb1c13dfb | -5.74076 | -45.13379 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| becec4e6-0bd3-3e67-92a8-49ce55d1ee1e | -4.11326 | -54.01559 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13cb07ed-9d8c-381e-9791-9bdafc1f1072 | -5.33991 | -42.92704 | 2026-10-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 77de5829-2886-3ac3-b144-d4a0d1bfd0e8 | -9.30118 | -47.38628 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| defdedd6-06bc-3ca6-8e9c-3492df945456 | -7.21768 | -55.15193 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 98d69862-9e1d-3a5a-809a-51d54d470c37 | -6.33815 | -46.03043 | 2026-10-10 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c942f8b-5730-3868-b29d-297bc2cebcc8 | -9.02468 | -44.35785 | 2026-10-10 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bd3b4f4-467c-32e8-b415-cc0326d0c043 | -3.12181 | -54.18295 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c630b920-43b2-3d06-872a-655f0473b664 | -8.98023 | -45.89219 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df9cc492-8906-3109-b106-863b8f65e1ad | -9.30701 | -47.37632 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5a7f9d02-0073-3190-a2eb-f6d65fea4e20 | -9.28337 | -47.39408 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6a56e7f-0bbc-3d72-8125-9d3f8791cee5 | -2.06892 | -48.14726 | 2026-10-10 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 601c35ad-7b70-35cf-9f69-0799246c93b7 | -4.12611 | -54.0416 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0605a33f-b190-33b1-b153-0a69323547b3 | -5.81753 | -35.38176 | 2026-10-10 04:08:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e1cc7ee1-2508-3bb7-b720-bc33df7ac839 | -1.63827 | -54.39832 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 35a4e6c4-93b3-3a40-9c15-b4d25d7cf717 | -4.45405 | -47.92527 | 2026-10-10 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| cc041e2f-284f-385d-8794-43237cb0b115 | -8.96234 | -45.93536 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 219ee591-ce3d-3cbc-b7c8-68fe9325d63f | -6.41824 | -44.07043 | 2026-10-10 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a93b8833-6f22-34fe-bb76-94d2bd777e08 | -3.22288 | -49.44527 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 032a7073-510c-35ae-897a-c10692c22ae4 | -7.90769 | -54.71429 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c48f540-ef69-316c-b39a-719af49514f8 | -3.2832 | -53.87618 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4ead3be1-4ab5-37ba-9029-ef8de84220dc | -2.94102 | -54.08046 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ef4031ff-ed87-370d-881f-57c4088a3ade | -4.52959 | -43.64558 | 2026-10-10 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1adec3ff-0514-31d8-8183-e5aba9d15d66 | -7.9317 | -54.73152 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 06accc09-9ea3-3462-8f31-81226e6841ac | -6.32779 | -55.34283 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4a91595-158a-32ad-91d0-ddfffe976667 | -1.63255 | -54.43242 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c2e8b0da-c934-3b57-82af-affb329e31ba | -6.77136 | -48.6685 | 2026-10-10 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 20.7 |
| b0268433-0fca-3bf4-b340-65170df43762 | -3.35182 | -50.41239 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae730958-9ef8-3612-b803-f1b3d501b985 | -4.83316 | -43.34851 | 2026-10-10 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc39677c-2aa2-3ccb-9b25-b0e5066d012d | -2.73055 | -54.1468 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8b3e3b1a-cb6f-3acc-b7a4-270e9d9d2e43 | -2.92613 | -54.08062 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf328a1f-21eb-3324-ba84-57abe47bfefd | -8.36094 | -48.14408 | 2026-10-10 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7895d58d-be5c-3da3-8b2f-0bf4c8b1a44a | -7.04407 | -46.6979 | 2026-10-10 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f2027e6-f2e4-39ec-825a-3e803fd67cb5 | -3.74979 | -50.00842 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3ee46f3-2004-3bbc-949c-0cb74e210ee2 | -7.53559 | -45.315 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1701569f-c2b2-3500-86d8-a541a1ace7bd | -1.73892 | -52.24651 | 2026-10-10 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 448f32a9-87c2-306b-89d8-fa70cb531cba | -7.0325 | -44.33678 | 2026-10-10 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a476984-30f9-3e3f-b0e9-eb047d19eb5e | -3.22538 | -49.43026 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 69e17a2e-3204-3b04-94ba-74b9071536b8 | -3.0377 | -50.34462 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90695f33-ab56-37f3-a4e0-32f536b0c00c | -6.06426 | -46.29029 | 2026-10-10 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee19ac8f-1c01-3af8-a8c5-200487e948b6 | -4.09891 | -53.99922 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8349b856-1c28-31fb-b69a-8235f6611058 | -5.95734 | -48.91547 | 2026-10-10 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc151167-b3ca-3d7b-b567-fc0dcc7d582a | -7.92188 | -54.73705 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8ad63f4b-30be-3d12-aef6-ced4a32704f9 | -2.82702 | -51.28027 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ac7f6a9-2ad4-34bd-b144-be2f3639fd05 | -8.37457 | -46.91199 | 2026-10-10 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 239cea2f-d650-3f31-a729-659325cb26bc | -3.20517 | -53.85357 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61ec2064-68ec-3f97-b456-f707f48307db | -7.36959 | -44.05208 | 2026-10-10 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a667f537-02cd-3992-a0fc-6bc4d83e6259 | -3.26953 | -54.69459 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e31e60d8-7ec7-39d7-9e67-9864f387f8c0 | -5.74515 | -45.13001 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b08d289d-6147-362c-ac7a-6bf7266296cf | -7.6655 | -49.79052 | 2026-10-10 04:08:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16483f74-a3cb-35ac-9581-1970d1b95984 | -6.4718 | -55.06504 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af29a178-d415-3fb9-8a56-76770b63cc51 | -5.89402 | -43.41201 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0860d3ad-5558-3acc-8ec4-f0c7f97349a4 | -9.02065 | -44.36101 | 2026-10-10 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78656ace-72ac-3f71-aca7-7ab4d1652276 | -3.5485 | -54.74578 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5822d50-1ab0-3d98-8a99-90c817d883d7 | -3.01247 | -41.13179 | 2026-10-10 04:08:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec76b80b-8f52-3044-9627-8018e775a48e | -7.16283 | -41.98751 | 2026-10-10 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f11c5c5e-1100-3eed-8577-9c342cbb55bf | -8.65952 | -47.08839 | 2026-10-10 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00707624-354a-3539-b644-baf227aea44d | -9.02203 | -46.86991 | 2026-10-10 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b407530-337b-3b73-915d-0357eca5bb9b | -9.75273 | -44.78645 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8987a293-d256-38cf-b43d-4ab9aebd8541 | -6.15283 | -53.3144 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a93aacbe-f8fe-3707-b426-c7f8d5848ba6 | -7.9197 | -54.72287 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1cfaecbb-d0a3-337e-83f6-0b574f7e03b3 | -7.02909 | -47.66592 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1b414a5b-7a67-33a9-8372-c4891dc96145 | -3.10028 | -50.31556 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 354d66d9-632f-3a56-9de5-e69177ba0564 | -6.08618 | -43.5521 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb5a33e8-ac09-3c6a-81ea-47f462e5db45 | -3.56536 | -54.69206 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0e300676-7a1e-3a01-a7e8-3a247c32a891 | -7.91858 | -54.72878 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f5a885a4-5ae4-37a4-9a1a-2bfd7403d00b | -3.8858 | -52.19263 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22e12f6b-1855-3027-948d-5ec1fcb4bd71 | -7.10503 | -46.71642 | 2026-10-10 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dde626e4-f4d0-35f2-94f0-ace9bf8e1468 | -5.29354 | -45.36768 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4e61d1c-3671-35ae-a021-5e691ed0d54c | -7.52608 | -45.30478 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a84e50c8-3d5a-3ad7-9e15-ffc6333cbfe2 | -7.0874 | -55.73177 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e9da31b-1701-344b-805f-e784a3be9638 | -5.62849 | -43.64826 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d7d39ac-1c64-36ad-8d5a-3154f8d02f3f | -7.08386 | -52.67951 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d39294af-127d-3f36-9bfb-caf2504a5139 | -5.88441 | -43.40673 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8bb7ff19-475a-3e73-8b74-307d33457956 | -7.52695 | -45.32238 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b741d291-e679-3b6a-959a-27a1a73524b0 | -8.19022 | -46.3521 | 2026-10-10 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b303c114-ad6b-3022-810c-c47386c6cf2a | -6.99384 | -47.72057 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 474d994b-b01c-38b7-afb0-6b9c2fafc5a4 | -5.70673 | -41.65825 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3f267f08-2eb6-386b-a3d7-99a3b49952c2 | -6.36754 | -55.1651 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 58a757af-d36c-3599-abcb-d9bacd7346b3 | -5.0386 | -49.35435 | 2026-10-10 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 18b821ae-ce98-30b5-8d0c-6f2bffe75c37 | -2.75091 | -54.11084 | 2026-10-10 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f0f90f50-9ba0-3984-bd6a-c4a42ddc8ee8 | -6.64804 | -55.33692 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 14ec2e36-70e4-35fa-89fe-50677ad73de9 | -5.74587 | -45.12568 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4170c73a-60c4-3227-b561-c67d3cb3098b | -3.17903 | -50.59195 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b425c0ac-b108-3f7d-a40b-da4c2f0aa120 | -8.97863 | -45.9464 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34a4f2f8-4f36-3c90-8f42-d94961b1d770 | -9.12456 | -45.81587 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README34.md)
