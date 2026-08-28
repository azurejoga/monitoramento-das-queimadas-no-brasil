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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f8a9cd0-8569-3921-9468-56f8e3f7d6b4 | -8.0737 | -45.8598 | 2026-08-28 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5117b8d1-eb5e-37f0-a760-ffe9353db34c | -8.0548 | -45.8616 | 2026-08-28 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 7dbaf6b3-d81d-3f54-9a36-9f7dc2c1b5a4 | -10.8996 | -46.6216 | 2026-08-28 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 6ad4d75f-d3d9-370c-ac91-ef2d2d6fc720 | -10.8992 | -46.6442 | 2026-08-28 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 5921e3c6-3e4e-39bc-a210-320f3dcd63e4 | -11.2111 | -51.2264 | 2026-08-28 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| dbb16ad6-f20e-3d2d-b986-c6825020755c | -10.7649 | -50.6366 | 2026-08-28 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| cd173ee3-f7f7-3f93-9d59-a04852b8a4f9 | -12.2086 | -50.5815 | 2026-08-28 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 417cb20c-fe8f-3d60-8c5e-df1bf197d49d | -11.2109 | -51.2476 | 2026-08-28 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c5bf0150-9284-3885-9171-648daa7c7b25 | -12.3038 | -50.5915 | 2026-08-28 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 6406805e-5769-3400-b31a-d8d22bd48792 | -10.8801 | -50.5179 | 2026-08-28 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f6ba327c-3dfe-3c14-9336-45d2b1275f8e | -12.2847 | -50.5938 | 2026-08-28 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| eda150c6-ed55-30eb-a5d9-da51b0c993a3 | -10.918 | -50.5138 | 2026-08-28 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 189fe280-ce27-39f8-aa1a-297f017ace1a | -12.0158 | -47.1693 | 2026-08-28 12:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 179b6fcb-e71f-3aa2-97e4-b8724f6da83a | -14.9791 | -52.5951 | 2026-08-28 12:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 43070f76-550e-3902-b4e2-445b40f95ed6 | -11.2493 | -45.0501 | 2026-08-28 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0d1eb398-075a-35e4-b7af-768576a9b07e | -2.7304 | -47.0424 | 2026-08-28 12:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 224.8 |
| c3bb5098-c9d2-39c5-bc48-f3353faedf33 | -2.7303 | -47.0644 | 2026-08-28 12:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 4c41fb48-ca3c-37d5-aea9-f16e9dde156d | -10.899 | -50.5159 | 2026-08-28 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 8c7172fd-12e9-3665-9690-0c62541d136c | -14.8172 | -48.8043 | 2026-08-28 12:10:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 9e016cf6-a4cd-373a-9129-67c169476f3c | -10.7839 | -50.6346 | 2026-08-28 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 165.4 |
| b04c884b-6312-356d-aaa1-1a8cc6c83bd9 | -12.2277 | -50.5792 | 2026-08-28 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 91a2e7bb-d55f-3e63-bd60-06ed03c63fbc | -10.918 | -50.5138 | 2026-08-28 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 62796587-e5ab-3a32-b49a-cdb53d733b0b | -11.2493 | -45.0501 | 2026-08-28 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 74624970-d6fd-3b43-8c74-12bc4a10212c | -11.6586 | -50.4532 | 2026-08-28 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 991c8900-7184-3424-acca-08bda59a8f46 | -10.8996 | -46.6216 | 2026-08-28 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 191.1 |
| eb82a9de-c9bc-378c-b101-5b781dab0472 | -2.7304 | -47.0424 | 2026-08-28 12:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 203.3 |
| 48b5826c-a0c2-3d81-b1b9-6f8c475df96c | -6.1656 | -57.7988 | 2026-08-28 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| fed1fcc7-0cda-3f99-a3d8-166e8323ea29 | -14.1784 | -48.7703 | 2026-08-28 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e56936e4-6822-32b9-b11a-f484006e56cf | -11.2302 | -45.0528 | 2026-08-28 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e4564317-7f19-34a6-8f81-c1414c4a0c91 | -10.899 | -50.5159 | 2026-08-28 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| ee2c0479-b813-32a8-ad91-5cfef8cba107 | -8.093 | -45.8128 | 2026-08-28 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 8428f36f-6f7e-3818-9404-bac833ae4307 | -11.2497 | -45.027 | 2026-08-28 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 24399e56-b1e3-3c08-99a9-e637a300f791 | -10.8992 | -46.6442 | 2026-08-28 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 332.2 |
| 6895e66c-110e-35be-b5f7-b85f08aba16f | -10.7596 | -54.0384 | 2026-08-28 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a2f5cdff-9c75-38cb-be00-8b2bfe6d361c | -12.2277 | -50.5792 | 2026-08-28 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 2d6de0ea-f4e5-3348-b313-aff833b38ba1 | -10.918 | -50.5138 | 2026-08-28 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 59034e7b-45cb-3869-9dd1-2f634a3148f5 | -10.937 | -50.5118 | 2026-08-28 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 3dafe0ea-eddf-3b2a-827d-54cb48f5388e | -11.3476 | -48.3872 | 2026-08-28 12:30:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 08d43d57-5032-3cfc-ab9b-b760d1533b6d | -11.2493 | -45.0501 | 2026-08-28 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 19b7844c-de59-3970-990f-930397b705a3 | -2.7304 | -47.0424 | 2026-08-28 12:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 207.6 |
| 0c0d3d32-b0aa-3733-944b-8faa51e499b7 | -10.899 | -50.5159 | 2026-08-28 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 5109830b-5536-39f2-b083-09f143f94277 | -2.7303 | -47.0644 | 2026-08-28 12:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| c7c383d6-6e2e-3e49-b824-15ca02f381a2 | -10.8996 | -46.6216 | 2026-08-28 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 92bd01f1-0187-3acb-bf3b-471983ae5406 | -8.0548 | -45.8616 | 2026-08-28 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 408324c7-ad85-3d07-9096-d6f3c9f53d70 | -14.3182 | -51.7046 | 2026-08-28 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 739a0615-9b8f-3b41-91f4-64d30584cce3 | -6.1656 | -57.7988 | 2026-08-28 12:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| d8412bc9-848d-3d06-bf29-d086c91476f7 | -12.209 | -50.5601 | 2026-08-28 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| eae0f20e-6836-30fa-b361-d3242501e8cd | -8.093 | -45.8128 | 2026-08-28 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 7a44fa9f-4236-3952-ae44-dea2554b8730 | -10.8992 | -46.6442 | 2026-08-28 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 6559bb89-246c-301e-b4ab-3f2c4b41dbb3 | -10.8996 | -46.6216 | 2026-08-28 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 27b50058-72bd-3b92-b46e-5954958896eb | -8.0737 | -45.8598 | 2026-08-28 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 9de6a302-4bbe-3711-848c-0cd5186c2dda | -8.0548 | -45.8616 | 2026-08-28 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8399baf9-4379-387d-ad84-639299427ed3 | -6.1472 | -57.7995 | 2026-08-28 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 64625fc4-a3a6-3da7-9f02-b1bdf48cb2c3 | -11.2109 | -51.2476 | 2026-08-28 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 277e2c8b-0dda-3e5a-bd9e-a686e31ddf9d | -14.1784 | -48.7703 | 2026-08-28 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 910eda8e-8161-32c7-9fb1-765adcef9ac3 | -10.8028 | -50.6326 | 2026-08-28 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c352d911-a4a9-3771-9f62-422bfdbede70 | -11.2493 | -45.0501 | 2026-08-28 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5233ea1b-7220-3988-973b-899ad0052a93 | -10.899 | -50.5159 | 2026-08-28 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| d899bb08-c238-36f4-972e-0d9d68368576 | -10.918 | -50.5138 | 2026-08-28 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 884ba503-cd95-3e5f-bb19-7226d8031127 | -8.0928 | -45.8354 | 2026-08-28 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| deba6c21-71ef-3a00-8989-7ba98763a6f6 | -6.1656 | -57.7988 | 2026-08-28 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| e8f06275-be54-330d-b5fc-cdecdac16ebf | -11.7786 | -47.6474 | 2026-08-28 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 9545c8ff-a719-3fa6-93b4-bb9a2f48a34c | -2.7304 | -47.0424 | 2026-08-28 12:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 339.0 |
| c933ea40-a295-3efb-b1af-3115b4521324 | -9.9708 | -53.9419 | 2026-08-28 12:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| c69737ab-afeb-3f3e-b2f5-e2e1ec3a3fd3 | -8.093 | -45.8128 | 2026-08-28 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 194.0 |
| e40e7788-20a9-3523-b563-f19c4fd0ca8b | -12.0733 | -47.1614 | 2026-08-28 12:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 248cce6a-b6cf-3d03-ba80-712cae72e069 | -10.8992 | -46.6442 | 2026-08-28 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 261.7 |
| 8d72dc6f-b4fb-3c36-a510-f758551f7e90 | -2.7303 | -47.0644 | 2026-08-28 12:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 3a5077e6-cee3-3264-bfd9-e17bfe687a5e | -10.937 | -50.5118 | 2026-08-28 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9bbf2893-f448-3772-8900-c3bf18992886 | -11.8239 | -47.2178 | 2026-08-28 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| a8d683bc-d298-38a0-91c1-ddb09b1b5e83 | -10.7596 | -54.0384 | 2026-08-28 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8760d3d8-5b1d-3339-95e2-6454fae7d6f9 | -10.7839 | -50.6346 | 2026-08-28 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 66b20f7b-4bbf-3c8e-8eaf-ca2e496bf69b | -12.0733 | -47.1614 | 2026-08-28 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 193.0 |
| b5ddd4c9-690f-3fb7-8b24-b22b359cded2 | -10.7839 | -50.6346 | 2026-08-28 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 6de6bf73-eead-3ad7-9d2d-4932174ade06 | -14.1784 | -48.7703 | 2026-08-28 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7e3bac71-06db-3b4b-9cb4-1c6a76246761 | -14.6024 | -53.1508 | 2026-08-28 12:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 8069feb6-d793-3b79-8c96-c9fbf1610989 | -10.5444 | -46.2386 | 2026-08-28 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2db66045-516f-3149-8d19-63182fe266e4 | -13.4191 | -51.4159 | 2026-08-28 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 41a7a119-0808-3143-98c2-437edb4fb046 | -10.8028 | -50.6326 | 2026-08-28 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| f6bf8cb6-f250-3318-9d1c-2a0069d0b32b | -13.4194 | -51.3945 | 2026-08-28 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ea7c5696-9b5d-31a3-a013-5eee7e368e28 | -11.7786 | -47.6474 | 2026-08-28 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| aa440f89-b0ed-37f0-a074-add2d0d46fc7 | -9.9708 | -53.9419 | 2026-08-28 12:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 6115397e-a793-3b17-a106-ca6d364ecdd9 | -6.1657 | -57.7793 | 2026-08-28 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c58dd316-af23-3666-9b63-e834718cb4fd | -11.2879 | -54.0317 | 2026-08-28 12:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 9b5b182f-1c4a-3565-afda-32e45652cc24 | -10.7596 | -54.0384 | 2026-08-28 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 6556d4fd-9cce-388a-b95f-48412efa46cb | -8.5969 | -54.7755 | 2026-08-28 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 15bd4090-655e-3beb-a86b-b8b286a09f1f | -10.899 | -50.5159 | 2026-08-28 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| d4e17f97-ba8d-373a-9b9b-9e2289e57111 | -8.093 | -45.8128 | 2026-08-28 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 0e101f84-ac5e-373b-8eb0-4ada3682a913 | -11.2109 | -51.2476 | 2026-08-28 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 04bbb396-0224-3a06-8420-945bdc454fe6 | -6.1656 | -57.7988 | 2026-08-28 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 3e9a3348-848c-3b30-8143-01b51847cd3a | -11.2493 | -45.0501 | 2026-08-28 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 37be8560-84bf-3388-83d3-89c77f417f15 | -10.8996 | -46.6216 | 2026-08-28 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 8b12d750-4099-34d9-95fe-8999c48b23e9 | -6.1472 | -57.7995 | 2026-08-28 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 95979c11-944d-35ca-9b67-1a589ba9cb2c | -11.8239 | -47.2178 | 2026-08-28 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| ea75ffc4-2cf7-3db1-8a16-2935510f33d5 | -2.7303 | -47.0644 | 2026-08-28 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fcbb2d49-63f5-3923-b6fb-4d33501ba3b8 | -2.7304 | -47.0424 | 2026-08-28 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 354.7 |
| 0d1bb39d-2a60-3fb4-b7db-aa91d44b6061 | -10.8992 | -46.6442 | 2026-08-28 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| e5802aff-9967-3036-b038-ea2b6e05ffb0 | -10.918 | -50.5138 | 2026-08-28 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 711ad2d6-533a-3ed1-9fae-56f7273d921c | -11.2882 | -54.0111 | 2026-08-28 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| de02fa07-dff0-3c87-b730-a8845582c595 | -10.7596 | -54.0384 | 2026-08-28 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |


[Clique aqui para ver as próximas entradas](README74.md)
