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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68c33412-8879-3af7-a552-ab59c5ad2e4d | -3.22704 | -46.93561 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c24114d5-01ac-3603-a400-d33fdbc247b6 | -3.22922 | -46.92952 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20743e97-999a-3145-b0e6-7368b2db2eb0 | 4.35135 | -59.7066 | 2026-09-30 04:51:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4409154-fb13-3d69-9249-5e1188db0058 | -3.22276 | -46.94646 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdf56577-8e44-334d-9593-dd1ac44c9007 | -2.97146 | -51.02227 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a910e00-4f7e-3a57-b750-286d6f3c090a | -2.97258 | -51.03663 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 991578f8-0826-3792-850d-1477fd9fba1e | -2.23767 | -52.35024 | 2026-09-30 04:51:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4987f2b-fe52-32c9-88ec-5d8e9de3eeb1 | -3.28887 | -50.30624 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31584cc3-2adc-31ba-b32c-ed9fc3dbc207 | 4.35198 | -59.71093 | 2026-09-30 04:51:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e26beb34-0d3f-3c53-8fc7-b337a2c12ec9 | -2.98694 | -51.0318 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 511bf0c8-e6dc-3eb2-9350-29d5f5f33e8f | -1.48852 | -48.90977 | 2026-09-30 04:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e16fac7a-5f69-3b18-9ece-f6e73255dc08 | -2.97313 | -51.03317 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a6661f43-f9c0-3680-9acd-92244e0830bb | -2.37902 | -50.40944 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2eb1846-886a-3bc3-9f6a-f3df4a70b01c | -2.97809 | -51.02331 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5048808-7c4b-35e2-aa7f-960a5452f674 | -0.41505 | -52.01752 | 2026-09-30 04:51:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2961dba-5654-31e3-8ba1-cd64012b13a4 | -3.03217 | -48.41452 | 2026-09-30 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d385f501-be0b-3d6d-ab10-88f481c8a2e6 | -2.26966 | -47.87089 | 2026-09-30 04:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 378cf929-c69b-3112-8054-c09d322dc6e5 | -2.49749 | -54.89243 | 2026-09-30 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0027c628-683e-33bf-96fc-760b17bbf570 | -3.22941 | -46.94487 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5ac33fe-26e6-3da0-a83a-6e4497b04dcb | -2.78809 | -49.41131 | 2026-09-30 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bb4f53b-03d0-3e32-946d-ac2f8f9bc273 | 1.69539 | -55.91658 | 2026-09-30 04:51:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f49613c2-ba22-38c2-9282-4b0ad6ee6577 | -2.36844 | -50.34795 | 2026-09-30 04:51:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da696ec4-7a1d-3d1a-ac99-9cd3b8cf70e1 | -2.97646 | -51.05499 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f43458eb-2213-3fd7-8e2d-163c88ed08e0 | -2.99193 | -51.04323 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aef641d5-5e86-3202-808b-f94b61a0ac17 | -3.24684 | -50.11986 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07192e1b-e0d7-30b7-bf3e-5d557e0c1a17 | -2.9864 | -51.03526 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e2f8d1a-c1d1-3312-8faa-16bbdde9500e | -2.48253 | -49.25899 | 2026-09-30 04:51:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a70779af-0464-327e-82da-d631a665fe49 | -3.23613 | -46.95037 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf8b145a-4e54-3f78-9937-a3fb031eec05 | -2.98141 | -51.02383 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94278b55-6d65-3bf0-8991-0242207ea3fd | -2.3804 | -47.60388 | 2026-09-30 04:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c3b0606-2026-328c-84be-a8715cb3a418 | 1.82203 | -55.62732 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e16e90c4-27f9-3681-b944-3ac938c7fb9b | -2.97422 | -51.02625 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e6575e4-1c1c-38ec-83d4-825cddec4316 | -2.97368 | -51.02971 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3c7227f-36c3-3133-9188-ea333b236e19 | -3.10643 | -50.27774 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7bcc66e2-bd1e-3d30-a8f5-0e767dd9efa6 | -3.23879 | -46.9329 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b15493a0-7066-3c6b-bd0c-bfab354bcbec | -3.22638 | -46.93999 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| eea31e29-b460-3fa6-9da1-ae7ddc5c787b | -3.10512 | -51.27076 | 2026-09-30 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 799a3ccc-70ab-392a-8254-47247498a54d | -1.33039 | -47.78652 | 2026-09-30 04:51:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ff0bbf6-dccb-3726-84cc-1f1fc49e3400 | -3.10865 | -50.28513 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a64fd542-13dd-36a4-991e-49da90d411c0 | -1.81277 | -57.1054 | 2026-09-30 04:51:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dc2b397-b4ff-3f21-a24b-6c0be9d63b49 | -3.18756 | -48.02198 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d4ac4a9-bb18-399e-8576-b3fc91235940 | -2.97701 | -51.05153 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4efd471d-c333-3241-a6f3-d9e98071256b | -0.67037 | -49.24812 | 2026-09-30 04:51:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 063ac88d-fa9a-3fc3-8796-336626b25298 | -0.67314 | -49.25211 | 2026-09-30 04:51:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a436dfc-c472-3e6c-8e1a-dd2141c9a173 | -2.98198 | -51.04166 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5fd70656-d967-390e-af4e-1c22c9d23b30 | -2.58011 | -50.79052 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbc8fb45-07e7-3d04-b8cc-b3f21af8769a | -2.97589 | -51.03715 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7712628c-98d9-36bc-81b4-5384bd355fd5 | -2.92572 | -50.43224 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0d19141-0cbc-38c0-9595-97b5e2558ce3 | -0.84236 | -48.71943 | 2026-09-30 04:51:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c1ec8d3-e141-3b02-91f5-93ab55cf5e01 | -2.9853 | -51.04218 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d9e45c66-c283-3427-a5e1-8e546f516a25 | -3.09283 | -49.35025 | 2026-09-30 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f90d497e-29ff-3e1f-b8da-883c58b32108 | 1.82003 | -55.61463 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c0fd25e-0d5b-39ab-9624-9129bdad34b7 | -3.10919 | -50.28169 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6261f576-2137-341b-bdf0-a3adcc1507b0 | -3.25069 | -50.11692 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97ab2bfc-a009-34a8-8598-c6358f1e385d | -2.97425 | -51.04754 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 43d0a8bc-1536-3e41-9d66-a22fa94e478a | -2.98807 | -51.04616 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 27d47445-830b-3fe4-a59e-6ded4a589995 | -3.00103 | -50.47261 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54a26b67-1389-3a9d-8047-034b053f41fb | -2.97203 | -51.04009 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53e0affc-fbbc-3caa-bdfb-705d7492c140 | -3.26885 | -50.08795 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2d0d4d3-da09-31c5-b8f8-b17becf2ddd7 | -1.79181 | -47.94427 | 2026-09-30 04:51:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42efbc2f-19cd-38d4-8e1a-5417bfaa07e8 | -1.28533 | -46.60707 | 2026-09-30 04:51:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb336688-a4d9-374a-8a54-26f45c63126d | -3.03619 | -48.41132 | 2026-09-30 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a949d5f8-9c35-3c94-a4fd-448801825f41 | -2.27144 | -54.50267 | 2026-09-30 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfb33a20-e421-38d3-9f25-200e190facdb | -2.97699 | -51.03023 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 813f1116-4f9f-3d8f-9d39-c77d9021deba | -3.10312 | -50.27722 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5791e352-115f-3dfd-8dc9-6bcc3cd44168 | 1.80582 | -55.63858 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ffd9e4e-351b-3845-8fc5-bcaf6c410a3a | -2.98196 | -51.02037 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32b25499-50db-395d-ae6e-b47944e6b0c8 | -2.64337 | -49.26976 | 2026-09-30 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44a2ad05-d020-3f80-8b76-663b849eab87 | -2.98916 | -51.03924 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 651d62ac-530a-3e21-a2d4-67a29f278907 | -2.44404 | -49.22057 | 2026-09-30 04:51:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d0a715c-6ba6-307d-8820-3b201aabcc4c | -3.2496 | -50.12382 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8ecf614-554f-3ffd-96e3-df997f925666 | 0.60745 | -51.56767 | 2026-09-30 04:51:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dab1c868-488b-3943-a7aa-73f70128c83c | -3.22268 | -46.93948 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f18ba8d9-161e-36e6-8502-6c9816bdb3a3 | -3.22572 | -46.94436 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78320a72-b4d2-317b-968a-0c3e09b6c236 | -2.9303 | -48.7506 | 2026-09-30 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0aa2805a-0130-3f08-985d-d887936988b7 | -0.66982 | -49.25159 | 2026-09-30 04:51:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9370d6ff-a11d-3a26-95d6-cab5acb33448 | -2.58066 | -50.78708 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2499f7e7-48b2-3263-b1f8-e3ecf52181d5 | -9.93109 | -50.15887 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ee115292-e601-3145-97d7-28eee6752df1 | -3.04929 | -53.86526 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81138b0f-59fc-3366-bb74-ceb8a3710a36 | -6.71755 | -45.58227 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46743314-27c8-30b3-8861-7aa20a55a355 | -7.92374 | -45.4444 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e424249-77b8-331b-82a1-be7e651ba2fc | -3.8569 | -49.74282 | 2026-09-30 04:53:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55969388-07aa-39e6-bc72-fb06db042279 | -10.72916 | -50.50363 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8185b65-8158-35ca-9d8e-8b2e80d82c46 | -7.50705 | -55.03462 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bc98316-9d50-3b8f-887e-bc1f2fe7dae7 | -9.78623 | -48.22539 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5da42b5b-3531-32b5-87af-7e4c3c6da420 | -3.82788 | -55.80028 | 2026-09-30 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 265227d0-ad6a-3b98-97d2-a17fe1a66c0d | -11.26398 | -43.52653 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f817577a-1a78-39ab-ac71-4b61addedf11 | -6.57648 | -51.49212 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7734b3b2-ea87-3d09-9842-a48923c08217 | -5.4068 | -45.90588 | 2026-09-30 04:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df604fb1-8f03-372a-989a-1343bcb5315e | -4.28773 | -48.56009 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc832682-db45-39f9-bff7-f4c55efa9dfb | -7.27091 | -44.31208 | 2026-09-30 04:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dee960a7-f9c1-35a4-85e0-6a5816d26162 | -11.39862 | -43.47461 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1c6b5bb-4c63-395b-b6f6-80bd2278dc64 | -10.90723 | -43.8541 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 372fb06d-1180-3342-a71b-b91d392badc2 | -7.38163 | -44.77855 | 2026-09-30 04:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a54d718d-3af1-3921-b6eb-90e094c41d0e | -7.0092 | -45.30215 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10b65f2a-a020-3ce3-82cf-966a231b7fa5 | -14.53729 | -48.29369 | 2026-09-30 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a66aa34-c1b4-3679-b11e-33a0500648fc | -8.39048 | -45.44287 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e06f8194-d28f-30aa-9249-2305d2189d87 | -10.77561 | -47.72108 | 2026-09-30 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c9549e3f-fb11-397d-8131-05e32f35ad79 | -7.45935 | -45.7944 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d0bc036-1599-3b38-9283-d7478fca13c0 | -11.37858 | -43.37949 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README42.md)
