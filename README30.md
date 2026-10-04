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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dcc40d7-d215-3e33-bb41-373a6a3434e4 | -2.59205 | -51.85181 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| dc61514c-eb55-36a2-b22b-d7924ecdbc34 | -4.25918 | -46.36543 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8c494f9f-36e6-3051-92d0-fa8ebd88326a | -3.06733 | -49.52814 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d25bff11-6e3b-30ec-b954-a5e567c41902 | -7.97259 | -39.83519 | 2026-10-04 04:19:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a001ca82-34f8-3a2a-83f7-5b167e850990 | -3.08323 | -49.53449 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c73bcbb8-9ac8-31e9-989b-481a8e6dd24e | -6.2343 | -53.15335 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96deec4e-f922-3ede-b0e6-6f077d4d9cce | -3.12638 | -53.72635 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b7519590-8708-321c-a565-7f700515ed16 | -2.82281 | -54.12229 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 89c39638-0e3b-33b2-a388-4491f2d9cbb1 | -4.27271 | -50.26386 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e79d2f0-9498-371d-8ee3-8d69591fc2bb | -4.21041 | -53.45821 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ba08cdb-f39d-34f3-b5f5-fc6da543f005 | -5.7817 | -50.22363 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7e8d23f-a741-3382-bc67-19d5fe688e1f | -3.419 | -48.33669 | 2026-10-04 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 975c3da2-80f3-31ee-9cd3-3c7ebf4ec576 | -4.48631 | -45.53755 | 2026-10-04 04:19:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8b68808-afe2-3c71-aa0e-43e4fd1b06fc | -4.15437 | -47.54147 | 2026-10-04 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca97ce8f-9d6a-32d0-8542-707300611aed | -4.45647 | -50.97797 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc95e041-86cf-344f-89ad-89de131e4a39 | -4.2632 | -46.3622 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f41310fa-762f-3c12-b9da-7a41aa84eabe | -6.01268 | -53.53448 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 983ede0f-5b1b-3b75-946d-dfa3917a8a52 | -7.37072 | -44.7661 | 2026-10-04 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92789be6-a3d9-38f5-9113-7db360bb3410 | -3.50587 | -54.60802 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| baa75b4c-b514-36eb-af59-5458516ffba4 | -2.80084 | -54.11475 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b9dc2a4-132f-3f31-8a25-c655f490bf82 | -2.82847 | -54.1232 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f8d5463c-48ac-36f1-b3be-2006598898c1 | -3.31067 | -53.84617 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68389c71-2fdf-3186-aef4-10c19143b4b5 | -3.46595 | -50.10165 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0604688f-d244-34ac-a050-7a0db53b7774 | -3.52825 | -54.61609 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59865c0e-e915-3495-a478-0e0ee985ea0a | -3.0074 | -50.47311 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 00d05199-cfcb-3d50-9880-c095472909b0 | -2.96523 | -50.3188 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f40b6dd-4fbf-3f02-8bf7-7a89e040806f | -3.20652 | -50.74245 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88763579-7ed0-3016-9b43-7ac7728d582e | -3.04898 | -54.23081 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dacb176a-8ae7-356a-94fa-2eb33c3a8960 | -2.58297 | -51.85798 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb826b12-2eb4-316e-8765-b1f03db2da2d | -1.68923 | -48.20276 | 2026-10-04 04:19:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16440577-e5c4-3baf-b4e4-546a7249f3d4 | -2.79647 | -54.10621 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4795c3f2-d8e5-3c62-8d0d-a17651d3d141 | -5.36591 | -45.03197 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1a55165-e147-314d-82d8-7ca98ad2c835 | -2.94731 | -54.12435 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 099167dd-88bb-3d49-a133-897d84ae0469 | -2.58526 | -51.87492 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4372df80-e4a3-3117-a93a-ffd28f8b2654 | -4.20929 | -53.46482 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6b0ae55-f3d6-3e68-a563-86cdd59fc891 | -4.4425 | -54.96737 | 2026-10-04 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dff67a0-2833-3e75-a960-484633646ce7 | -5.74545 | -45.15203 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df792a88-d622-363d-afbd-d413edc2a3ab | -4.26662 | -46.36274 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 33.6 |
| e0c94eb1-81fa-383e-af4a-fcd054693912 | -2.5887 | -51.85342 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 02391484-b907-3919-943d-2c559f06dfa8 | -3.20647 | -50.75321 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 61ae455c-1cd4-31a0-a4c5-4a506985d17c | -2.58176 | -51.8833 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3fd367b7-a4a6-30ae-9e9f-b4b07de9a60d | -2.97915 | -54.09338 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f56a12b9-85d5-3b6d-bd78-62672542fbfc | -1.09433 | -54.1092 | 2026-10-04 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4ae4adb-d1da-313e-91fd-757c3f1e79c6 | -4.9285 | -45.6904 | 2026-10-04 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9870fe1e-093c-3cb1-8e80-d2e8c43a43f9 | -7.54371 | -46.69445 | 2026-10-04 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2348103f-d6d7-3a37-8c74-4292bbd41ed8 | -7.02683 | -44.6377 | 2026-10-04 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6634c258-aa1b-39a2-b5b3-6d8073aec9fc | -2.84746 | -51.28796 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a03af010-14f1-3793-b925-3e785eb48744 | -4.20456 | -53.46061 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea13f464-f6d9-3e7f-831c-64afadf5de41 | -3.30697 | -53.83444 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f96d96c7-f03b-3c7a-b2de-2e82fee3b161 | -6.01838 | -53.53229 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b5e0392-7c87-33d7-b980-9b80b4567b17 | -5.36823 | -44.47139 | 2026-10-04 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a18b0f8-24f2-346b-9199-81a6cdf94ebf | -4.2614 | -46.37344 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9847da1-83af-3966-8afa-48b36bc337db | -2.80892 | -54.13596 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98f6adb1-230c-32ae-8f91-8b61f91c36a4 | -3.54465 | -49.3655 | 2026-10-04 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb5aa9a2-30a2-3c93-bd4e-0d5940bf7a9b | -2.97645 | -53.26125 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0b22810-0d10-3521-aa6e-3be8335dd297 | -3.11793 | -53.74341 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b9779013-3e27-3440-83e6-bddcbd5cc83e | -5.04947 | -42.78931 | 2026-10-04 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7eeade6-95c7-30dc-8b58-6704b737a8de | -3.0433 | -54.2299 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 753eac74-71b8-3038-8f13-47ef16949bb6 | -3.03358 | -48.41986 | 2026-10-04 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c90a5c85-b8a8-3082-bd41-8a555270d03b | -6.20947 | -45.40248 | 2026-10-04 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60ff112f-ba16-3b56-8c83-b1a7335c6f76 | -6.20227 | -52.79676 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6238d77f-5ec1-333f-99cf-363bd01ad3eb | -3.12283 | -53.7479 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48d9d565-f093-3666-9f62-b7decd0a58ea | -4.26542 | -46.37025 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 36.8 |
| c06ebdea-586c-383f-a6d2-f9a51bdfc75e | -3.10933 | -53.72732 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c5c966ee-21ac-3a35-b12a-fef0a26ed0fa | -3.08734 | -49.53518 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ba028bb-c1cc-354a-86d4-72910eedda52 | -3.76276 | -49.56334 | 2026-10-04 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ddbc508e-48a2-3403-b305-5cc6d7fcbcb1 | -2.81908 | -54.10983 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d98c6a45-b8b7-3fe0-8841-43730d495a7b | -1.70017 | -50.03373 | 2026-10-04 04:19:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b46d7b11-0192-359f-8870-e883474e70e8 | -2.79712 | -54.10237 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3081d86d-3754-38a0-bc02-65d09fb7d1c1 | -2.59114 | -51.85719 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| e4b1e96c-2bba-3047-877c-617cc3b784ad | -3.10539 | -50.28846 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 420d80fb-22d4-34f9-a748-410abfb73b80 | -5.63792 | -51.75916 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47efea2e-29fd-35d8-bea5-2b5dfedd1a60 | -3.29474 | -53.83991 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9aa85b6-fa75-3047-9069-7bbb77e0278c | -2.9046 | -54.13699 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f2c818b-3169-3fc4-8953-b64284a26581 | -3.94104 | -55.83978 | 2026-10-04 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 93118b80-71d2-364c-a962-ef87995f9dd4 | -4.92795 | -45.69391 | 2026-10-04 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7409786-5b74-31b1-9101-1430077220fe | -2.79518 | -54.11387 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71da77bc-4b40-3ae7-a315-cc0ad3251a9e | -3.11244 | -53.74252 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a19bfca1-f8ca-3c75-8e49-ac3818ad90d3 | -5.05489 | -45.62365 | 2026-10-04 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f09142c1-8ee5-3065-937c-8c8cea38292f | -6.21312 | -38.52196 | 2026-10-04 04:19:00 | NOAA-21 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f29b56c9-c8eb-322f-9b3b-1c107cd1a781 | -4.46092 | -50.97868 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 79b051c1-a0aa-3945-8f44-fed9e770f428 | -4.26923 | -50.74069 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a016c8c3-4665-3c78-b2e7-748515575bc8 | -4.1322 | -54.15159 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36754c08-99cc-31d3-a4e4-8a47471be319 | -3.54693 | -44.65307 | 2026-10-04 04:19:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 427257a1-6bf8-30f6-97b0-baa64ef9be6a | -3.35739 | -43.37932 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2201d17-21ba-3b51-a6e8-1615d8eab412 | -2.24447 | -51.91706 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84bf5c6d-4ec4-35ed-86fd-b026c3e8c163 | -2.75435 | -51.55373 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14a36b90-f83d-329d-a4f7-b006ebdac6cd | -1.09572 | -54.10062 | 2026-10-04 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51be794a-6b97-350c-a372-74730b7f0a84 | -3.06042 | -54.16137 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7ed431d-6efa-3d53-bed9-c3846dc6afa3 | -4.26482 | -46.37399 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 32031e7b-715e-3a4c-ad98-78d70f573921 | -3.07018 | -51.27904 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07c0ac06-d72f-34cd-b4b9-db6f43ce4009 | -5.29773 | -46.59148 | 2026-10-04 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 985b3d9e-4155-3662-bc55-0308776e9c8d | -2.8065 | -54.11567 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3eb6648a-0b9f-37b1-bb59-873dd153282f | -2.58126 | -49.9969 | 2026-10-04 04:19:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a05a6df-aa36-30a4-8a0d-e0bd97b3a725 | -1.87358 | -50.61723 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 539b8ecd-9402-33ec-8e89-5576cf33baba | -3.04146 | -54.20581 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76f422e2-2ab9-3a1c-a4f1-20539f098e71 | -4.19872 | -53.46296 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96c22522-b99e-33fa-82b1-b5dc044fadd4 | -3.54389 | -49.36536 | 2026-10-04 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0927838-fe1c-36c4-8978-f1ff4ab2b24b | -6.19649 | -52.80116 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| deb8e8ef-098f-3c06-8da8-f9fbf33e1504 | -4.12665 | -54.15069 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README31.md)
