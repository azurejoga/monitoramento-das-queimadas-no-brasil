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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50d01be3-f9ad-3c3a-a085-6bdde074125b | -1.47922 | -55.37996 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc428d02-4323-3ae3-b640-19de108adf68 | 1.21233 | -55.93652 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40a264a7-ff32-3acb-94d0-5a0c34647c44 | -4.54891 | -50.83357 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2551ea87-7735-3503-ab57-19da0cff5bb6 | -1.45058 | -54.48364 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b405234-209a-378d-8c00-2a1135ba489b | -1.66985 | -52.73226 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39b261ad-5d80-33d9-93c1-8784df45586d | -3.2019 | -53.42512 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 164333df-0688-3f0e-b47b-fe6b50a68c36 | -1.14645 | -53.663 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bc630c4-7e2f-3219-b760-4a98f80ebe1e | -2.59887 | -54.08786 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00d5ea86-9c54-30c1-970d-b958ad184375 | -1.98424 | -51.51878 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e27de93b-c234-3535-b4a9-8c2124eba3e2 | -1.2583 | -54.54539 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93839b02-5403-3142-94a1-ab299b743e3a | -2.89388 | -55.22501 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b327531-7647-34ee-a3c0-c0af7e211c80 | -2.84158 | -54.05083 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95c51aa5-31f1-3f67-89a9-08eafc120daf | -1.9525 | -48.68853 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5be12d9-3b10-3c6b-ac80-ee557aeace61 | -2.61419 | -51.81007 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0c6510f-0a6f-32d6-96d8-e6f2c6b6b5f4 | -1.12385 | -53.74166 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 304fc0d7-09ae-36f6-96aa-4a9dfed70dd7 | -3.34612 | -50.23856 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 728c1c12-b9ea-3bf2-9937-50f7c16f2426 | -2.07093 | -50.75103 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9e6de24-9ff9-3a48-b1a7-401776e10c0f | -2.82383 | -54.07675 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1cd1af95-bc57-3d19-9602-3a3fc5a14bb9 | -3.23713 | -53.91737 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5aa1ea8-7446-354d-a6ba-cacd25162f92 | -2.89879 | -53.9626 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c8f4331-2a2b-3f67-ab94-ca1bf360c041 | -1.61705 | -53.87529 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee45b27f-2e89-3c98-a0a0-bc77852ad569 | -2.86439 | -54.03644 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8937bcb7-6fa0-375e-b7c4-e441b6cec8bb | -0.34527 | -51.98276 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd46a28e-cdb0-32cd-8cbe-57dc2e2e66f0 | -1.80355 | -52.08839 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02b0dbf1-c1c2-316d-be11-1d4036a0af41 | -2.27009 | -53.46645 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d9a914c-bc79-336f-8599-09ef0de359f8 | -4.87754 | -41.302 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b03ba77d-fdb2-3aee-92ad-9cd7990e9615 | -3.26338 | -48.76512 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf152c7e-094c-38d2-a5da-f42274359d85 | -2.05495 | -56.07631 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ad8e092-d413-3dba-a6b1-b81ea2a0f0fc | -2.77612 | -48.57784 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 061fbe5b-0fb1-3fad-a6f9-903f1c6d2280 | -2.62591 | -54.00264 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da191e98-b250-30a4-9164-18e04688d53a | -2.8618 | -53.32168 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad04dd0c-3866-3f1b-a19c-6aae8c92d5be | -1.20343 | -52.96558 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cacfdf3-a2b6-36e6-9fa0-48bb9debbaf8 | -4.47484 | -50.42364 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8878f146-a575-3163-8064-0b02a7098ee3 | -2.41553 | -53.67842 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29df1fa4-96c3-3109-a3b6-5f1749ba37bf | -2.03971 | -51.20672 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9d6952d-7cd2-3774-bf49-d93fdec1f5ee | -2.86262 | -53.98229 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e0f86e2-aa2b-32b3-af78-14e760eecb4a | -3.12931 | -53.26073 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4829eac5-6ba2-354d-b21a-d2e6ab840b7a | -1.83077 | -54.52206 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3a03d576-cb2e-358a-98b2-7103ae6bde61 | -1.08381 | -53.63551 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2abef410-f2d0-3671-a8fb-953791d9ee21 | -1.19236 | -53.86635 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9833182-502f-3196-9f67-626d7e0d954d | -3.58347 | -50.50738 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88e312ad-c671-3843-a678-7eec3c20869a | -3.25513 | -53.64016 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ea3a4bd4-bb15-35e4-8b27-2355b1bdabeb | -1.22954 | -54.08509 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9da537ed-9a06-3825-ad37-672422ce3726 | -3.13234 | -54.18204 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa50ec7a-f0ce-3fbd-ac12-ed3452a17f6d | -2.82722 | -54.09875 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e266535-cfc3-3885-b063-a525e9dbc1b4 | -2.01576 | -51.20047 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a455d3e9-8300-3f64-b222-c6c3edb96ebb | -2.95917 | -51.69619 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d78baeed-e98f-3dc4-a921-a6de671ec345 | -3.502 | -53.80537 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2d72d54-7ff0-35f0-8504-673cd49829c5 | -3.60109 | -54.42597 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3851a8ea-f6d7-3170-8a11-bf900e0ab47d | -2.83335 | -54.10328 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9a0758b-c6f1-3345-95b0-0d7465537bb4 | -1.60542 | -48.70296 | 2024-11-30 05:01:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acd10a72-7f1f-3c78-b22f-0e750241ea0e | -3.99494 | -46.65657 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bd47a7c-cc54-3227-92df-ae50e5e61075 | -2.79962 | -53.0494 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe05e9a3-2d19-371a-aa15-bfa57db3d67b | -3.05906 | -54.04472 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7278636e-ddc8-39ac-95e4-37cbf965312a | -2.86596 | -53.98281 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41c9379e-337e-3bdb-a413-117c5a8071aa | -1.31451 | -51.73313 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b149fc47-e20a-3bbe-b14e-57f5758865de | -2.02516 | -52.07665 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 813b5d31-a5b8-364f-9a2a-e5438c5fc6f6 | -1.465 | -54.49997 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ff9fa5b-af89-316b-90ed-ed2d4a3c2ba5 | -1.08404 | -53.39416 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f933b76-28c5-30af-87f7-ca3870892b9a | -3.05771 | -53.67854 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1adb29eb-6599-303e-9fba-d8d7b17456f3 | -2.96184 | -50.57675 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f87ecfba-9c0b-386c-9302-9c95a4808fbc | -2.05895 | -47.56629 | 2024-11-30 05:01:00 | NPP-375D | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd6fedb5-d17f-3ddf-b3fb-321a1f0e1227 | -1.46338 | -54.51026 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52eaf820-bed4-3ced-b355-8fa6b479db4d | -3.27626 | -50.01839 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38ac463c-0a71-3e61-92f8-b6a5d21b7427 | -0.97067 | -53.68628 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaa4479c-9e46-3edc-80ab-3e7bb5e5c0a6 | -3.89147 | -54.23789 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0918d8b7-86af-3679-9475-99f1f5e745da | -1.24139 | -51.62367 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ffcccd09-577f-383b-87cd-c7251b23fce9 | -1.71115 | -52.49324 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a90b873c-072e-3161-bee3-c0fb14df4fd4 | -3.25119 | -53.62115 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e10b6d00-e926-3749-bc8c-53a76b8f7a10 | -1.24001 | -51.79669 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0b432f2a-6ee6-3ce5-b640-107d6b4a97ba | -1.99696 | -51.17531 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb78a4f8-e12f-3df1-afc8-c57b4817304f | -2.82116 | -55.66479 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0731fe4e-23f6-33bb-932a-60ba47ce3a45 | -2.8343 | -54.03176 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42671991-322f-3a5f-bdd4-7ac444d2fba3 | -2.8063 | -48.61758 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a720b9bb-71cc-3f4c-b7ad-707f37c28504 | -0.26533 | -51.64304 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b354205-1d2b-31e5-b240-4ac751b700d3 | -3.22983 | -54.09645 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3a6dfec-a428-35d0-97de-1378015e636f | -3.59608 | -50.37051 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2582fe54-25c5-3cc6-ac0b-f473a422a3c3 | -3.04489 | -53.71674 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a38ca787-d4e0-3018-831a-3e9ce72c578a | -2.59133 | -53.98299 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea4cc1dd-45fb-3129-a254-461404ef24e3 | -2.84387 | -54.07985 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a04e3869-b3da-3761-8db5-f5ff75382b80 | -3.18278 | -53.25402 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d43b699d-2794-3a1f-b2f7-a3ee9d1f530b | -3.07688 | -49.50039 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 812aadd9-9974-3a85-8ef5-683375907dc0 | -3.14478 | -53.71782 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49e601d7-c6d7-37f7-985a-946fa149b044 | -3.17992 | -54.32846 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1462d175-2ed5-36e8-af7a-7e608c3c0958 | -2.86384 | -54.03994 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74e6f314-1927-38ff-b8b5-a0a6627e2b4a | -1.03179 | -53.18976 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffb54656-4deb-33f8-a60d-d620694cdf35 | -1.35002 | -54.63026 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c26b62b7-f0a7-3006-8af8-635cabbc055b | -3.10605 | -54.13137 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7efddd3-2a81-3d69-b6bd-46ebd1a791ac | -1.70444 | -52.44564 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8db7e50-2e03-3811-9f01-8d5a3f4364b2 | -3.09272 | -50.35159 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 527c83d8-9406-3218-813d-c2a8de37976a | -1.33003 | -55.84696 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bd28cc3f-df2c-32e8-8e48-57990d00969b | -2.5529 | -54.08444 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af1353a1-230d-36c0-93b2-6e86ca395726 | -2.60136 | -53.98454 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2643378a-542e-3ff7-92c6-2704aa313627 | -2.82498 | -54.09125 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2053c47-2947-393c-8e6d-0cdef36ddd65 | -2.59662 | -54.08037 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0748fce4-848a-32b8-a4f7-3d1b749e837b | -2.11617 | -50.62694 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5548588d-30b0-3978-b25b-d24aa6d8f44e | -1.8048 | -53.58471 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db09c483-9725-386e-8e61-b91d148fd5c5 | -2.84268 | -54.04382 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39d4c4cd-aaba-354d-a73c-692fbda33ee0 | -2.00904 | -51.195 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5bb5dcf4-23d5-3fd7-ab1a-14488ca06558 | -2.03694 | -54.6702 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README105.md)
