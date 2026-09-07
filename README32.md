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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa45e897-1048-3e06-85e4-776590e8bfb4 | -2.62995 | -46.77454 | 2026-09-07 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f15fc999-2c23-3a1a-9f0b-5fd92ff42daf | -3.92572 | -59.23312 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de3838bb-ce4a-3949-9de9-19db4f871e8a | -2.82218 | -49.23278 | 2026-09-07 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60502f9e-277d-3562-bdcd-851a578ef89c | -1.20331 | -55.72927 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c4f9b70-3ee8-354d-ad5c-02c7840e0105 | -4.20622 | -60.00515 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb574c55-1af3-3f88-af6d-2bfbd0fc0500 | -6.1231 | -57.70166 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1b54d0e-249f-3eb0-b4c0-b69648f5f235 | -3.80572 | -55.97934 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d2e952a-c4b4-32e9-99b8-315a0f94b787 | -4.28873 | -59.96343 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f5b6052-fd7e-3db2-a150-ef17a7004db5 | -4.47345 | -55.09331 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b37d937-a598-3f32-ba3a-1e8ec298ad80 | -2.71025 | -59.76632 | 2026-09-07 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9893c60-3812-3499-99ea-28d435421345 | -8.75225 | -62.4392 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49600d37-02b2-3286-9dce-c7612417b597 | -3.37654 | -59.41755 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55286234-3039-38f4-820a-a6479aa07e7c | -3.48757 | -50.60773 | 2026-09-07 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f762fa2f-e811-32ca-a482-2ec6c16f4b59 | -4.2876 | -59.97056 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69adbd28-1395-3400-a79b-ee0382909edc | -5.1596 | -56.18249 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7adf8c1-bbb2-3e57-8ea9-2bfff1ca4e40 | -8.72264 | -62.44252 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33c1a77b-05c0-3349-93bc-257cad53053b | -3.98417 | -56.08932 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66d3a571-c52a-3814-b3d6-45ba8695a18e | -5.36168 | -56.02398 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abc66bd4-fac0-3732-a0ec-7d9cbc23f8a0 | -5.16021 | -56.17852 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07f04165-8d7e-3b69-bb76-716ae702b9b3 | -5.38582 | -54.44797 | 2026-09-07 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b654877-fb2b-33f8-84aa-a4249a8b5c90 | -4.66338 | -55.6404 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 559d7610-4f14-3e95-95fe-9fbdd044839c | -8.54192 | -63.88592 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02f8a0bf-b567-3024-8677-d254d59601ad | -4.46975 | -55.09278 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a994ded3-fd41-37e9-8823-2dbaa8c30410 | -6.13848 | -59.88842 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3de420c-1906-3791-b898-797301e5ee51 | -2.78813 | -54.6755 | 2026-09-07 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fa32463e-5cbf-33dc-b0ca-4a4ef59d6dd7 | -3.47572 | -60.00748 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dc73e32-052c-38ad-b7f3-58988bf96800 | -1.49323 | -54.8252 | 2026-09-07 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7db260a8-942c-3b6c-9943-90842df308df | -4.29379 | -59.95328 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1f56242-d95a-364c-b0eb-957d0b893b98 | -4.67546 | -55.63368 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0222356-9c18-3d51-a45e-be0f9916f70e | -5.30463 | -56.01534 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc77e6d3-d693-376e-9e8e-5a36c62eceda | -5.27235 | -60.15921 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fe506b0-25a9-317f-aef7-23b858534dba | -5.99118 | -57.69582 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06beb590-381e-38c4-b31a-e6963548f42b | -5.15485 | -55.95842 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d039a57-d722-3164-af13-b9bd2072704a | -3.38342 | -61.32374 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12079da7-7c76-3c7f-bdca-e8f9355a1341 | -3.62729 | -54.60512 | 2026-09-07 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4badaee6-ecba-3ef4-898d-e4448a7c951e | -3.3732 | -59.41702 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f4223a2-6ba3-3697-b035-caec3d078f84 | -5.36755 | -56.03314 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f1e20b8-d400-3b36-bd87-0ae1fbe070bc | -4.12254 | -56.34563 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c957c594-db45-31b9-b80c-1b95ba17049a | -6.05853 | -57.7942 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94cdd0a0-9795-360d-af6c-0d4bb6243216 | -2.62922 | -46.77932 | 2026-09-07 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2e3ac0bc-96f6-3a04-95ae-34fae418194a | -2.35157 | -60.08559 | 2026-09-07 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56019c97-5c93-39c4-ba96-d8baa9244059 | -2.92144 | -60.99756 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7a90a34-5e00-3076-972f-b216c31d088c | -6.00073 | -57.70095 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d0c4530-e4db-3947-9913-48ac3992fd27 | -3.83074 | -59.40322 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed31ed8f-7a9d-386f-ac70-2ccb4f0209ad | -4.66652 | -55.63406 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9baf373-6b51-3376-8300-9d46c4436d9c | -8.71977 | -62.43792 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30ddbda0-9531-3e24-b8b3-e4133ba43a17 | -4.667 | -55.64084 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 056f1924-dbed-3c8d-bae7-3a967eee106c | -5.35686 | -56.03154 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d64b0ea5-1d36-396e-9e4d-14f9b2ee7918 | -3.14229 | -60.66332 | 2026-09-07 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f06b9c81-8cbf-3015-8529-1b957f08873e | -4.97466 | -50.62981 | 2026-09-07 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a62c403-5118-3290-89f8-7b3d1899d7c6 | -3.38265 | -59.4221 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 360c2b65-1a79-3b6b-89c6-12e3816073e4 | -3.13965 | -60.63573 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d6a19863-caaf-3712-b34c-3a1c166e084b | -6.05406 | -57.80081 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b29dd415-4f73-37b9-8667-f17be5c0a492 | -3.70124 | -58.93458 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e15b39f3-df04-3b6f-863f-41951a87d396 | -3.3871 | -59.41562 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 953a8981-8205-39ef-b9e7-1c700d46750c | -3.11621 | -57.69436 | 2026-09-07 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be3537bd-011d-3d9a-9d8d-4648f9ad8c8d | -5.36902 | -56.04048 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b3d31fc-8a21-3313-8d1f-ab111f06ef72 | -2.30269 | -48.5885 | 2026-09-07 05:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2296bb6-444f-37fd-954b-e3349ea93697 | -3.12341 | -57.69192 | 2026-09-07 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15452336-85a0-3c66-9d51-c49bdf430565 | -5.35623 | -56.03558 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa3f8e02-b787-378b-9e81-5137bc9bfa48 | -4.95613 | -56.25866 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29b1a94f-dab6-35ff-809d-c0dbbc734500 | -5.36433 | -56.0232 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 662df0f5-7f5c-32a9-929d-c9bf42e3c64c | -4.97294 | -56.28926 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19dd8a6c-6ab3-3e89-a9e3-ad307b37788f | -8.7149 | -62.44535 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11d4d014-cbe9-3c66-b0d2-c1e4546205bb | -6.05685 | -57.80491 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 904c8bc7-ab8d-3c46-bc32-aa9a7e8204d5 | -3.96282 | -55.40197 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28e7772c-c0b3-3c9a-b486-bb9bb5f1d141 | -3.90381 | -55.83572 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca97a0db-b122-3006-80bd-922b2e4d0533 | -5.26564 | -60.15814 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddbfd21b-b32b-3f23-bc40-5120af63601c | -3.51139 | -59.06107 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7730d40-60c4-301b-983b-664ae4f62030 | -3.04714 | -58.0027 | 2026-09-07 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| defbb511-c0d0-3a06-bd51-c5057cb7cff2 | -3.76355 | -59.31404 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dcd0cf6-3db6-3208-b611-c2be438ca710 | -2.45319 | -57.91275 | 2026-09-07 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2345ada8-7dbd-3165-98e2-6f96813e8a4c | -5.15778 | -55.96306 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab0a51d3-82cb-3bb7-8a8a-53c1479f9bba | -4.1085 | -49.06116 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b289dd04-66f6-3da6-9085-60b27b025eb9 | -3.41625 | -58.31133 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7edbb750-fdc2-3778-806d-24abfe5eb5c6 | -1.63367 | -55.12647 | 2026-09-07 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc970d48-4326-3a9e-8de4-fa9c123f0ebf | -8.75777 | -62.42778 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f72ef6b2-1848-392e-b43c-add85307d069 | -5.36295 | -56.01587 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12b5b3db-d2f9-32ce-b035-820ee3b5ecda | -3.15044 | -60.65684 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e26d0535-f2f0-3a2f-996b-58d79c122b5c | -1.19637 | -55.72822 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 978b4a3a-fae9-3df9-ae51-785d74a8ab66 | -5.36658 | -49.1978 | 2026-09-07 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff56f0a4-f46b-3d38-aa50-bebf0598ac48 | -4.10247 | -49.06387 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24d0563e-6e1c-37b0-b21b-c34e6ff2776c | -3.14351 | -60.65575 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 611486fd-e2f7-3ca9-9341-76aeb3ecfda8 | -1.19238 | -55.70829 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea02c0b2-d337-3863-8d76-86b769092dc4 | -5.29649 | -60.13751 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1da2d55f-1d08-3b8c-b791-5e9c08e892ce | -5.99062 | -57.69942 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fd7bd119-bd2c-3d13-8c2b-0d7d3c8d1359 | -3.49437 | -50.61097 | 2026-09-07 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f6607a3-8579-3adf-b964-aac87454aed1 | -3.79056 | -59.72089 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8daf48fc-903b-353a-9911-8f888f08e258 | -3.4211 | -59.64851 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 273d1765-7b8a-3045-85a8-0870edb12667 | -4.50909 | -55.71248 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 347ab70e-06a8-3450-bb1a-e1ff5fb1513c | -3.76989 | -61.75902 | 2026-09-07 05:23:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74305e88-93bf-3ac8-a251-d55127db0744 | -3.19507 | -61.23436 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98e3bc55-feb0-3030-a9d1-8d1adc9e1d41 | -3.49928 | -50.61175 | 2026-09-07 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 858b436e-14c7-31fd-a812-1ca67d5d48a6 | -6.02553 | -60.16619 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f77e769-edad-36af-b1b2-26d26370c66d | -3.70401 | -58.93856 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42897077-b547-31da-a3d4-1d6f470af562 | -5.15422 | -55.96249 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05057a71-445a-3b2d-8ea6-f1542b0fdafa | -6.44321 | -58.15574 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a16763f2-8229-379a-9916-94e74f17b45e | -5.36128 | -56.04345 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e92131e-cbea-384b-b5f4-a4f9faf28670 | -4.47783 | -55.0895 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e1ea3af-123b-3fca-b122-40fb7c0243ae | -1.48895 | -54.82883 | 2026-09-07 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README33.md)
