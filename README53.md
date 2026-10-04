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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b06e61e9-9f5f-3a5f-9c98-4e356eff8a61 | -5.37252 | -56.06112 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de0eaf73-d15b-31f0-becf-aa704f333d05 | -2.58432 | -51.85574 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a642180a-77e0-3d34-960e-5b0229d7876b | -6.21217 | -52.80252 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4df14b5-e2b9-306e-b7c1-635916e9a30d | -3.07292 | -51.28125 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc3ac7b3-b9a0-3414-84de-8cb1ed65d039 | -3.12183 | -53.73062 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 56cd44fe-83e7-3819-ac1f-7e9cc29604e1 | -3.81715 | -51.54294 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d04936a8-e210-3a1a-ad5b-b60f497a75cc | -5.55239 | -45.26487 | 2026-10-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d193ac4-c704-3cf0-aa24-3082a9c8db1e | -2.97102 | -54.09109 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 067cc577-e049-3491-88b7-9cab74bac6a1 | -3.84476 | -55.8614 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79c3a5b0-7926-382d-bb42-b9ea29512545 | -2.51852 | -58.10035 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa7774ff-0452-3a88-8311-099ce2156402 | -2.86935 | -54.11636 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc2a28e8-4427-3615-95a0-0c686de3f406 | -3.18383 | -54.09443 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94cf2749-6530-3c47-8260-11b672f009c1 | -3.28371 | -53.82476 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93b0fb69-7fee-3af9-a814-6ed00a3636a3 | -2.97394 | -54.09558 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d881631b-b35a-328b-b518-8c12993b1cd8 | -2.53604 | -58.03352 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebaa6620-cf1e-3163-8ed1-e52c8b577cd7 | -2.85536 | -51.28837 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39abf1ed-9dc6-31d4-b4e0-569ce88d90d8 | -4.21003 | -53.46984 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a3a6aaa-17c9-30fc-a5e6-d2b4ecf6c2cc | -3.07549 | -51.27322 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d14fa0ac-3b1d-3ff8-b059-a175591130cc | -3.17622 | -50.53373 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e281ecd-e7e6-3431-8a48-5be9de538330 | -3.51463 | -54.61535 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c88549e-b4fc-3721-97c1-4640ce52b145 | -6.20747 | -52.807 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ca1dd55-af6a-3ea9-b6d1-73abe3d69788 | -2.96465 | -54.10683 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80747fac-d0b4-3441-90f8-a2300b34138c | -2.97192 | -54.08372 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff707d48-77fc-3f5e-86fe-e3615c44f884 | -1.10799 | -54.14522 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49007396-bc36-3f53-b7d1-d624656a0181 | -3.0799 | -49.54391 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ba2f78c2-fe21-3810-91f5-32fc0d3d2cb3 | -3.46779 | -50.10976 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a14f5020-1abb-3fe5-8029-973c0f0c7e2a | -3.46848 | -50.10511 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e06cced2-3a0d-3bd5-8bbc-f157e73cdf46 | -2.9692 | -54.10293 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2109b330-2e71-3fa8-8cd2-ca33464a58a9 | -1.73396 | -57.17735 | 2026-10-04 05:16:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6518b6da-c580-369c-a0c6-a434beaed3aa | -5.99742 | -53.52469 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0a722a08-453f-39f8-9924-64ed5c7c778f | -4.2735 | -49.98203 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c385a19-14de-3066-9eab-79255e13d0c2 | -3.52097 | -54.62022 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f65132e7-58a8-3be0-b1c5-f7a2595d53fe | -3.16904 | -54.09631 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7d7405f-38c2-3638-bcde-80b4d9501662 | -3.10415 | -58.5627 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d548ef20-e2b7-36a4-98a7-b89ab360f897 | -3.98409 | -56.27058 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73c9822d-a880-3f0a-86df-96af66d85a4d | -5.99486 | -53.64488 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af6f160a-01ef-3c25-87b3-af4c3025587f | -3.30688 | -53.84094 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6d2062d-005c-38e3-af72-cbfe471bab04 | -2.5923 | -51.85691 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 54c77870-e674-3538-9aec-5022b01fedfc | -3.50611 | -59.80963 | 2026-10-04 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3ba62b5-d1aa-37b4-abcb-e436fdba4236 | -1.09957 | -54.10909 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e1e1f751-bcda-31ec-b00b-8d0b9141544a | -6.01928 | -53.53311 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a3cca3c-cbfc-38f5-995a-5a2f869e6b3e | -3.22623 | -54.30946 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1096971c-3560-3d75-9d5e-df4b82c35a34 | -4.26191 | -46.36686 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6227ec07-47a2-3357-8841-077ca591efe2 | -3.04294 | -54.23088 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da296c87-73a2-37b0-9e21-830aa83bc653 | -2.57877 | -51.86546 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f74c049-4955-34e9-a385-21abe6edc059 | -4.52986 | -55.99276 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3844abc9-2efe-3296-90e8-be5366a0123d | -2.48578 | -56.09985 | 2026-10-04 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a80624b8-82a3-3d3a-a1cd-6fe3cb83feb1 | -1.09671 | -54.10479 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9d267dc-08bf-373a-a9e6-3a3fab3dc048 | -3.12477 | -53.73528 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0ae1e8e-24be-3eed-8207-9ba2f414bd3b | -3.08066 | -49.53893 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e85650e8-000d-39b5-bddf-ef7ee7f02ddf | -3.4737 | -50.10121 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5ba9d743-d3a5-370e-8e20-45472025deae | -4.46854 | -50.97088 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df45cd3c-ad6a-3f18-9a18-cae2ea4aed7b | -3.0194 | -53.89419 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff64565f-ad3d-394e-a70f-ba134c9c19cb | -2.80544 | -54.10809 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a1b96e5-edaf-3d97-8fbe-ea9d4b3bbb3e | -3.1898 | -54.10279 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04430709-ec1d-3ac5-9461-f8fb82a8ef7f | -0.35651 | -51.98415 | 2026-10-04 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0056174e-6f19-3a58-b041-7b484ebca7b5 | -2.92172 | -54.10429 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14d9895c-3cc6-3aba-8668-7f04f42c7acd | -3.90107 | -55.82298 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2292874b-0f79-376e-9893-a502509288f0 | -2.83639 | -54.20871 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21877e77-99d3-34a6-bb09-70783a5c5b0f | -3.15741 | -54.07818 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf99f57f-794b-3d64-9362-9648dd5d497d | -3.93368 | -56.05151 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e2d9ca9-4bcb-3c78-a0de-fedd28f8cfa2 | -4.45967 | -47.9277 | 2026-10-04 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a2b9881-a0fa-346e-986e-dca69ec512f9 | -4.51151 | -45.88942 | 2026-10-04 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ae65d59-ec75-3d6c-a7cd-53296e7c80b2 | -2.24265 | -51.91457 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1457d34-ff5f-3096-90b6-11094f432168 | -2.97686 | -54.10007 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb34221d-9b67-380e-a247-731a9cd099a0 | -3.12053 | -53.73885 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2c6a98c-60e8-3281-bcf9-836c9701acdb | -3.0673 | -49.53185 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46734f99-bb59-30ee-a163-87b2827ed79f | -1.3647 | -56.89256 | 2026-10-04 05:16:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5217bc3-06de-38c5-a511-7fbcef8ff180 | -2.8963 | -54.12858 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be8d7e35-9733-3465-9f9d-06dad500c3eb | -2.82106 | -50.50192 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f53fae45-a54c-3a84-871c-00c3947251ab | -3.2818 | -53.83706 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e7ba1b8-94ed-356b-a85d-e8e3938f408a | -2.94973 | -54.13272 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aad34409-f4b9-38ac-a97e-7ff45a651665 | -2.54863 | -57.39802 | 2026-10-04 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 065e34cd-480e-3903-8766-c6c8db2d6314 | -3.8998 | -49.69391 | 2026-10-04 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56836dfb-fd7f-3525-8822-1583d177e46a | -2.9686 | -54.10686 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7a66089-073f-3d94-a92c-caf8bade751f | -1.3331 | -54.66893 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b954d50-683e-3a3d-b74a-64cf30bfb9b4 | 1.76453 | -55.64587 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae445173-fa61-3c69-93b3-240517bb9917 | -3.61201 | -55.50896 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6247f51-fe15-38b1-8593-4bd9b1a91725 | -3.13686 | -53.7287 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0bdcb669-66a3-35b1-9306-5c546f33a79e | -3.09331 | -51.09569 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de028a70-aea0-39be-8fd9-c89f2b959743 | -3.7102 | -50.66153 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4c4c71b-8e2a-3b5c-b10f-374d98e82eb4 | -3.52157 | -54.61639 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cd721ab-3698-3dc7-bdc2-c5191daac733 | -3.81336 | -50.84359 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c065d85-7aed-3a45-b9f2-f5123ee3a839 | -5.37756 | -56.05095 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e58dd9f9-edd8-3d90-a806-8bdca75a62c6 | -3.13621 | -53.73281 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7dfd4540-b0e2-3415-8c0b-b89ec59376a4 | -3.97536 | -59.3456 | 2026-10-04 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2272fb62-81b8-3c06-977c-fb30ade7b719 | -3.18062 | -50.53439 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce1213ae-a6d9-3f6d-b63a-23959f24e294 | -3.67111 | -60.62109 | 2026-10-04 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| af64f934-2928-333f-82f6-8f44c3ae206e | -2.82532 | -54.11919 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 548cf20c-b2a5-3ed1-a019-5d4f32c6977e | -1.27681 | -55.40835 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1e0bcef-c76b-3e89-9f4b-05a8ffdcda88 | -2.98811 | -51.04818 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50c467e4-0b92-39d6-88c5-8ab9e6d8fa15 | -3.11422 | -50.28472 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7156595e-61e0-30e0-8f96-46940c24d9bb | -4.92715 | -45.69721 | 2026-10-04 05:16:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e08aa964-e5c2-3b03-b504-d3286761261b | -3.30624 | -53.84502 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6f6aab5-5440-31c5-93e9-4cfc17c466b3 | -3.18626 | -54.10227 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfe67b87-ed9d-3a49-b8af-671ef9be281a | -6.01998 | -53.52842 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0b283e2-95d6-3f34-9191-ba11c6d96f52 | -3.08141 | -49.53396 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b05a85b7-07eb-3830-8b78-a12aca3070d4 | -1.76468 | -55.02648 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4439311f-b4f8-3071-b52a-325c8ae50828 | -1.79253 | -53.57316 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd090541-0da1-3146-bf16-4c558d53545b | -4.25542 | -46.36996 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README54.md)
