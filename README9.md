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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c36a128-15ca-351a-9512-0fe9c6c41d62 | -2.9338 | -53.924 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88f50b15-2b9d-315c-be91-5756d8283b07 | -3.5496 | -59.472698 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51cc9f8c-52e5-38c1-a732-8fc21ebc9499 | -7.6007 | -46.770302 | 2026-10-08 00:26:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cfec3dc-e7ec-3b80-a1a9-3a526e43b0bd | -1.8038 | -57.089901 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43094fa4-03e4-3e9b-9424-618c8378cd6d | -2.6125 | -57.573101 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| daaa53fa-47ef-3798-8672-c0a65b00b812 | -3.2856 | -54.020199 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8ce5403-b8bb-32cc-bfee-5d5c50b06a57 | -3.2546 | -54.019901 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8abd034f-6044-338d-97b9-701a0403fa10 | -2.886 | -54.1675 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db268e6-d80d-3283-99fe-9b06b2deab6f | -9.4803 | -64.324501 | 2026-10-08 00:26:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6135fca9-39b2-3487-9bec-efcb4d3b60aa | -3.0695 | -54.249401 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac98e3ba-134c-3fdd-a143-289548e66bbc | -6.2185 | -52.860199 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcf01415-7bbb-30d8-84b6-47fd06a940a6 | -3.0727 | -54.263199 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7499d990-f2d5-3b94-900c-1f8b5771b7b3 | -2.9979 | -54.07 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 446e6728-9ca5-35c3-9b8b-bf30daca8c18 | -1.5374 | -54.813499 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f41b47d-aba8-348d-ab7b-6aa10c2b906f | -2.9542 | -54.195702 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7bce5bc-b4cb-328c-83c7-354308f63853 | -3.0514 | -54.2607 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4df4aa80-6957-3115-8d2f-b28e097db45e | -5.7024 | -53.492802 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2398a523-f651-3448-9cd4-6359c1f5ed24 | -3.1712 | -50.459202 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c28e8672-3284-3623-8027-2e9bc4cd2556 | -7.8944 | -54.715401 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4411dfe7-1f99-3365-904b-975be91bf14b | -9.4758 | -64.352798 | 2026-10-08 00:26:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bb4301cd-f6c8-3179-a6b5-028c78eb268b | -5.839 | -50.144299 | 2026-10-08 00:26:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 714b4ca9-3218-34b7-8a1a-d452480095f5 | -3.5818 | -54.645 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 356127c3-e5f6-3b0a-8f49-73b288402328 | -2.9849 | -54.0583 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd74b5c6-e0cd-36c5-9992-7ac166d7bcda | -3.9598 | -59.983898 | 2026-10-08 00:26:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 968750b2-13c5-3bc8-a937-e55b1084a1db | -4.066 | -59.8144 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a97bcdf3-1a1b-35fa-b3c6-fdd36f7afa62 | -3.0044 | -54.2351 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05329854-109a-331d-b569-486c2d0a5de7 | -8.2922 | -50.268002 | 2026-10-08 00:26:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b73fb519-f4ec-332a-bf6c-a4005b373739 | -3.3068 | -54.0228 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9970c811-23d5-3266-bbe6-d6fe686acdb8 | -3.313 | -54.0504 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec88fdc4-c2be-3a86-8980-6b3e69e2be9a | -6.5262 | -55.275902 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a06f2e12-278b-368a-a3ad-38de64111289 | -9.8647 | -50.503101 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f300cb47-43d0-3879-b7b3-24a386479c28 | -7.1481 | -46.519001 | 2026-10-08 00:26:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74a64c23-27fd-349c-949f-67c4d00b2647 | -4.9349 | -55.804901 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66a55cbb-1a40-34c8-89f9-83e6398947e0 | -10.8788 | -49.1511 | 2026-10-08 00:26:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3dd57de-7b56-3d05-a536-327efe57beb8 | -3.2609 | -54.047501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 710dcf09-abe8-3151-a468-185c926c74b8 | -6.0545 | -51.739899 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29032605-a3fa-3aaa-aab4-24e517b66a14 | -1.5193 | -54.824699 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa80b33e-2ed2-3278-8686-7d8bfba1cba6 | -7.2127 | -55.168201 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90819290-0fe8-3af8-a03c-7182e81e3e6e | -3.2529 | -56.801201 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5360ffbe-76f3-3d55-8e55-47a7772eb8b6 | -13.1756 | -54.312401 | 2026-10-08 00:26:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ed92e9e-34d8-338b-a4d6-f2c01f1367ce | -3.5849 | -54.658699 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79320048-0d55-3378-8425-e409fe04eafe | -2.9985 | -57.7346 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1225cbe5-27c9-3ae2-81a2-b4be91f8ca9b | -2.8915 | -54.101002 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 800760ac-8215-3fcf-a325-dc40405ba6e5 | -2.7545 | -54.088001 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30473ece-f5f0-372d-9071-247c9fd7ef7c | -1.3197 | -56.405201 | 2026-10-08 00:26:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| decb5140-d743-31b6-b098-e4e45da12a74 | -9.8126 | -44.766899 | 2026-10-08 00:26:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 415e96c0-860b-34aa-a4c1-f99bc55f93ba | -1.4754 | -54.5396 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 209adbba-7c5c-3dd7-801b-5c9a46299c20 | -3.0504 | -54.2104 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85eca30f-fa62-3b0c-80e3-a1df771e7513 | -8.2548 | -54.715801 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ecf11fa-4311-3a6e-ae89-2e811b448c4f | -6.2382 | -52.675598 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c20063a3-e45d-3792-8455-3d52c70c8ea6 | -2.0548 | -56.374599 | 2026-10-08 00:26:00 | METOP-B | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52dd4829-e7bb-3854-a4e4-ca1b31a0565c | -1.4547 | -54.7673 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1030540f-8c22-330c-896c-d591c917b42d | -2.9712 | -54.133999 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5f7c577-adbc-3ab1-aedf-e755a55b91d7 | -3.0221 | -53.904301 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39d832e8-cbb4-3935-b81e-acffe6b50233 | -7.4438 | -63.516899 | 2026-10-08 00:26:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 737a1054-288f-3723-948d-027fc2dcbe4d | -3.1443 | -53.7155 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cffab344-b1a0-3b80-a98b-f3a0f02b6c53 | -3.532 | -59.393398 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f16fdf4-06e6-3e99-bdcb-c14155f2a628 | -3.0285 | -53.932098 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a57cc761-8f12-396c-af26-cf2127fcb654 | -4.9415 | -49.2173 | 2026-10-08 00:26:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6e6d966-d34b-3ae2-8b23-ceb999180245 | -11.0096 | -45.4632 | 2026-10-08 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7888d64-078b-34d9-a5ca-bbee4cedea30 | -6.9201 | -49.609901 | 2026-10-08 00:26:00 | METOP-B | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23ff8b8b-7384-3413-87f5-d14fef5eb5b6 | -3.2225 | -54.287399 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e5295e4-966a-311e-930d-42002c24ffda | -3.0057 | -54.1045 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c173f7f0-b71b-3b5d-8fd3-b4d753135dcc | -3.2593 | -54.0406 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb81a8d0-0dc8-3320-8275-699aba415403 | -6.2381 | -52.855801 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f6062a6-b04e-395b-8df0-25388f7de8f0 | -2.7772 | -54.097401 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78d4b99f-6141-3b0d-b048-6401c73e5fba | -3.2723 | -54.0522 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74320b7d-9456-3475-9cff-5ff0a29b5d9a | -2.4683 | -58.077999 | 2026-10-08 00:26:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0afce53-7b3f-3a9a-95a0-40cb218f0883 | -5.2642 | -45.408001 | 2026-10-08 00:26:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 652dc5df-df93-3d54-881b-c5021e588186 | -2.9547 | -54.152199 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3026bd60-17d0-3a02-b9ee-d5636c9a4e3e | -6.3233 | -43.353802 | 2026-10-08 00:26:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f4b163f-f8c7-3d51-91e1-018c45b84acf | -3.8518 | -51.937 | 2026-10-08 00:26:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b12f1d4-7f04-3706-ab75-f4811b0997a7 | -3.2199 | -54.367199 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9124a5b-83df-3b7b-a162-e23c675af03c | -5.8559 | -57.545502 | 2026-10-08 00:26:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31282cbe-a6b4-3e11-b26e-988e36ba45e0 | -3.1597 | -54.738899 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 377ca561-4af6-34df-83b6-962d164312ee | -2.9747 | -54.104198 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8d6cc7e-ea8a-3e47-a0d8-28fb3826dca3 | -8.2507 | -54.6507 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6beb195-ac52-36be-882f-c088a4392969 | -2.9916 | -54.042301 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6604dfe-82ff-3c53-bec4-9f1836a6914f | -3.2711 | -54.001598 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f321e2c-2558-31cd-932f-8acc4f12797d | -6.1034 | -55.688499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35266d93-3ced-3d8e-9456-f1402ab55d18 | -3.0563 | -53.918598 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bc26f1a-9585-37f0-ba0e-2c59ac47e244 | -3.4909 | -54.608002 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2d7812f-3de6-36c1-8b89-4201a0910ee6 | -2.7576 | -54.101799 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3c6d6bc-4bec-32b1-99d5-bb154cd194ba | -4.0694 | -51.046799 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90fd3839-de39-3683-9823-ccbb3dde83ec | -2.9975 | -54.113602 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb10eca9-341c-332d-afb3-60a9773f857a | 2.4413 | -50.819099 | 2026-10-08 00:26:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0edc2715-fefc-3f6f-bfdb-17105c73f9ad | -4.2718 | -54.870701 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 637955fc-a610-38e5-932a-0a396e53618e | -3.5692 | -59.468498 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7730d4d2-653e-31df-817a-bab775f56020 | -3.1462 | -54.087601 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 269db846-2875-3115-9b7f-b5fec10fef58 | -5.7369 | -53.4632 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3bece93-879e-34d3-890b-73aeecfc29d6 | -4.4486 | -47.9128 | 2026-10-08 00:26:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 463d6b9a-54fd-3f40-849e-2d96904a8d55 | -7.7614 | -54.9506 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c014523-58f7-3a49-8d2e-8304ec49bd72 | -3.5789 | -54.359001 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3e7985f-8f46-3667-bc6d-337e1bb5f06d | -3.1226 | -54.165298 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6f4ce0e-34f1-3e74-a403-17ab36f91feb | -3.7126 | -54.221199 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 211b7097-4a3c-385e-b49f-36c415d1f2c1 | -5.2095 | -56.065899 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62d3e25c-f8c2-3a9a-af8a-aced31a115ad | -7.8818 | -54.983002 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c1a4009-4733-3c46-9c05-471b9711f0c5 | -1.5404 | -54.827099 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2308fff5-d299-3c88-a8dc-c285ab080d90 | -3.0234 | -54.136799 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f1cb86f-0287-3f3b-879d-ff69bddeea8b | -3.0969 | -54.2794 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
