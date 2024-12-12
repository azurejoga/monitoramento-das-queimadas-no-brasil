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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d836789-43d3-3146-b93f-bf0913058315 | -12.1386 | -57.796398 | 2024-12-12 00:50:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c85d38e-6957-308e-89d4-45a4e82b26c4 | -2.0412 | -53.692799 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7114578-e6ed-3b4b-89ec-a66866c94672 | -17.6231 | -53.023201 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5e77caab-39d5-3094-9907-080f48eef38c | -10.771 | -53.875099 | 2024-12-12 00:50:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25e607f8-c044-3a47-9160-3de0c5e6814a | -4.7161 | -44.436501 | 2024-12-12 00:50:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d55c12c9-3eec-38b4-ad50-56b64bff7e3e | -14.3154 | -52.723499 | 2024-12-12 00:50:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9e6c35f-e289-3ae5-859a-725f8ce2ebe1 | -10.7741 | -53.888901 | 2024-12-12 00:50:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc945f42-546a-3cfa-88fc-97714ae07250 | -10.6761 | -54.701099 | 2024-12-12 00:50:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cb57225-7b34-3e31-89a9-fc198179dcbe | -1.8576 | -53.973499 | 2024-12-12 00:50:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f73141fb-509a-32e6-9419-f98fd0f97b62 | -2.6131 | -53.896599 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ab825e-e563-3ea4-bee2-0e94f74edb60 | -2.036 | -54.078602 | 2024-12-12 00:50:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae8a6e1-a621-3aeb-b1fa-6c2f426d2340 | -5.4984 | -48.1339 | 2024-12-12 00:50:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ca00926e-b5d4-35fe-b4b6-af9ab93c937f | -1.7896 | -53.7645 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fbd4167-50f8-3aea-951d-95570cf3dea9 | -2.6114 | -53.889301 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90f5e433-f3a9-338a-a49e-d6d1b89c1eed | -2.0171 | -53.7682 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8addc066-6f47-3a8b-9b94-c2fbc45c9eb1 | -2.6931 | -53.341999 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98f4ee73-3282-339f-b0a0-0ccd782143a5 | -17.6164 | -53.040001 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 553196db-5dd4-340e-ba69-844f12c031ef | -2.8308 | -51.601299 | 2024-12-12 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0afca84a-4e94-3d99-b3e5-57a8efd96e44 | 4.0549 | -60.401798 | 2024-12-12 00:50:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 70420ce7-345d-38a4-95eb-cc4b1715cd69 | -6.4891 | -43.597698 | 2024-12-12 00:50:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa2a8e17-1785-302a-a167-c4c908924042 | 4.0628 | -60.4123 | 2024-12-12 00:50:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 675d5680-6ff8-3395-a8f8-9dc44a45f5ad | -12.6306 | -52.107899 | 2024-12-12 00:50:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a49aa758-8de9-34a5-9901-19aef480696a | -1.1744 | -54.7337 | 2024-12-12 00:50:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51f7a446-48f4-3464-88e2-fcab711fe863 | -15.5552 | -56.318501 | 2024-12-12 00:50:00 | METOP-B | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82d10d73-8f7e-386a-90d6-d6c7bcb1a188 | -1.8559 | -53.966202 | 2024-12-12 00:50:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7843980b-9ba4-360f-b81c-3ff33d788d98 | -10.7839 | -53.8866 | 2024-12-12 00:50:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcf6bb54-d199-3b10-902d-2c8ac41f2325 | -2.0331 | -53.7024 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73f8ba4d-00f8-3e39-884f-fabe8d30232b | 3.7396 | -60.114201 | 2024-12-12 00:50:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dac46b65-5247-3256-a296-6f1bfc09840b | -2.6948 | -53.349499 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 984740dd-6a7e-3387-84c8-fcb9acd715cc | -14.3139 | -52.716499 | 2024-12-12 00:50:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c99ad3de-7912-37a0-b5ad-6815e228c7b5 | -13.2613 | -54.815601 | 2024-12-12 00:50:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7968a21d-3d84-36ba-8513-5d028089131f | -2.8189 | -51.594398 | 2024-12-12 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8f1833-9245-315c-8aab-0572ed2c37c6 | -1.8337 | -53.550201 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50efa269-09fe-3728-b4e1-5a25bc94dade | -5.9185 | -48.0449 | 2024-12-12 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a276b178-e6b4-3cd8-981f-83a01667185f | -5.9369 | -48.0654 | 2024-12-12 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 15318bb1-c6bd-3775-b62b-d0171a443f60 | -5.9183 | -48.0667 | 2024-12-12 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 6dcf7893-f44d-3a0a-9098-c83c24609089 | -18.046 | -52.9798 | 2024-12-12 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 164.5 |
| f59e188f-88ea-3b81-9474-1e96dca1b9f5 | -18.0261 | -52.9829 | 2024-12-12 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 9c75e554-9498-3d36-a8fa-e3cb5c1bd41b | -3.2317 | -46.8716 | 2024-12-12 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 08c32aa4-9832-36f2-87e2-dda881617285 | -6.9346 | -43.5168 | 2024-12-12 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 297.6 |
| 954555e0-e116-3848-9435-35cd2560ad6b | -15.0867 | -59.6288 | 2024-12-12 01:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| fc187746-b40e-3d03-8840-f5de69562eca | -6.9344 | -43.5401 | 2024-12-12 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 136.7 |
| a952a084-b4e3-3aa7-b174-2d7ac20809f8 | -5.9371 | -48.0437 | 2024-12-12 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 67a5c31d-a0c9-3c96-ba5b-6c2a3329cb0e | -14.7461 | -52.6471 | 2024-12-12 01:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 62bb6bb2-bbc2-3030-b253-4b78d4c59a78 | -6.9156 | -43.5418 | 2024-12-12 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| e8433e4f-4c1b-30f7-a927-59b17c081730 | -3.2502 | -46.8929 | 2024-12-12 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a8505fc3-f50f-3954-be57-c4881922a7d6 | -6.9161 | -43.4952 | 2024-12-12 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 81c24712-a527-3e68-b582-c442d9a1c954 | -3.2316 | -46.8936 | 2024-12-12 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a075414c-2e66-31ce-8bb2-191938dee07e | -11.1959 | -53.8348 | 2024-12-12 01:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 90fd7863-9e14-3673-ab62-c15589290e77 | -6.9158 | -43.5185 | 2024-12-12 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 421.9 |
| 30859701-7bf1-3106-b864-accfba8632d5 | -15.0865 | -59.6487 | 2024-12-12 01:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 35db6f7e-35c7-346a-b481-a533742e5e7d | -14.7655 | -52.6446 | 2024-12-12 01:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| cbf90287-5984-3fd0-b58c-9d467de76d9f | -3.2503 | -46.8709 | 2024-12-12 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 366cdf5f-5fe1-35e1-b59a-16a1a51d9f79 | -11.2148 | -53.833 | 2024-12-12 01:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 23811208-7feb-378c-9c43-47ff624d8988 | -5.1648 | -44.3727 | 2024-12-12 01:00:00 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 569e7393-7ab2-3955-aa6a-cd2accd23c71 | -13.6933 | -54.7555 | 2024-12-12 01:00:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 0c8f446b-8fab-3be6-b928-5773c5a95a72 | -6.9349 | -43.4934 | 2024-12-12 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| ee159a49-e0f5-3412-9e03-1848c3f7abb2 | -18.0659 | -52.9766 | 2024-12-12 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| eb8d6028-b02c-3640-8f01-e0ea8059d7df | -14.7457 | -52.6683 | 2024-12-12 01:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d988a5ef-70f5-3f6a-a591-728b6ce91291 | -18.0464 | -52.9582 | 2024-12-12 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 0fd1ad9b-9753-32d4-98e9-3c8102989ec4 | -18.0663 | -52.955 | 2024-12-12 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 44ebc19f-e06a-3431-bb26-1b7d466a828c | -6.92 | -43.52 | 2024-12-12 01:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 574f2a1b-2984-3a3d-99fd-4111cb0070d5 | -6.93 | -43.56 | 2024-12-12 01:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 62de30c9-6b89-31c1-bb63-6d1a72535422 | -6.9 | -43.51 | 2024-12-12 01:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 52a5501d-3346-3c2e-bb86-84d84e844f13 | -6.9344 | -43.5401 | 2024-12-12 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| e51d3ded-42f6-3207-9eb1-d8f383a3cc27 | -3.2502 | -46.8929 | 2024-12-12 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 2dfd2e94-cf68-38af-a5fd-380751b29480 | -6.9156 | -43.5418 | 2024-12-12 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 5bc2260a-51fb-3b06-8b56-4393c9912158 | -13.6933 | -54.7555 | 2024-12-12 01:10:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 325a62b5-800f-3526-9bed-1509e3426f7c | -15.0867 | -59.6288 | 2024-12-12 01:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3ed4185e-6121-3ef6-8731-0529a42d86ef | -1.8788 | -54.6908 | 2024-12-12 01:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 878414f7-6748-313c-bde9-db7eddff2ada | -3.2316 | -46.8936 | 2024-12-12 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 82539920-052b-3536-b649-c9c10ee705d7 | -6.9349 | -43.4934 | 2024-12-12 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 75ace024-ff9c-32b1-be45-01c18f3e7c35 | -13.693 | -54.7761 | 2024-12-12 01:10:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 59359843-fff6-3689-9ca7-065f6a1bb41f | -14.7457 | -52.6683 | 2024-12-12 01:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 27e1300b-d12e-394c-b0ec-61977ea54876 | -5.9183 | -48.0667 | 2024-12-12 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| f756333a-093c-3e87-b2e7-82fe275453b7 | -5.1648 | -44.3727 | 2024-12-12 01:10:00 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 478757e1-c2f2-30e6-b99c-96739468fd7e | -14.7655 | -52.6446 | 2024-12-12 01:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 71a44ec6-b747-37b0-a500-be40ab3a3bc4 | -14.7465 | -52.6259 | 2024-12-12 01:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 7ec971e0-1c70-3a41-b5f0-bc22ce6a0b0d | -11.1959 | -53.8348 | 2024-12-12 01:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c39de8ed-b371-396f-a198-5b419766b2ed | -5.9373 | -48.022 | 2024-12-12 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| ff1d80ad-ab83-33a1-b6dd-19ff4ac17733 | -5.9185 | -48.0449 | 2024-12-12 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 3ec26fb6-9ba1-3157-aeeb-512ebcf8ec44 | -6.9161 | -43.4952 | 2024-12-12 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 139.2 |
| a50747bd-31ac-3887-a1d2-8061194e93d5 | -6.9346 | -43.5168 | 2024-12-12 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 258.6 |
| 1296d911-48cc-38d3-8727-eed80108ae2c | -3.2317 | -46.8716 | 2024-12-12 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e81f7632-1f4a-3a41-b3aa-2247b188870b | -6.9158 | -43.5185 | 2024-12-12 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 361.7 |
| 0117c46f-540e-3091-a2a1-de13e19605b8 | -11.2148 | -53.833 | 2024-12-12 01:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 841b660a-724c-3ced-9f53-9217aaef1825 | -3.2503 | -46.8709 | 2024-12-12 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 8ea9a6f1-8293-3799-9d8f-d5510428126b | -5.9369 | -48.0654 | 2024-12-12 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| b430c4ee-5999-369b-a732-5f2f0aeb6148 | -14.7461 | -52.6471 | 2024-12-12 01:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 70cef2bc-06f8-375d-8d29-bd2b5677e862 | -5.9371 | -48.0437 | 2024-12-12 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 189.4 |
| dd5fd3ee-6631-3142-b364-22b213c96198 | -18.9465 | -53.70168 | 2024-12-12 01:13:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7807c941-3738-3918-be74-6453ae940099 | -20.72772 | -54.41816 | 2024-12-12 01:13:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 67ea3d1b-63b2-323d-b03a-d1d88b3b6ec3 | -20.72914 | -54.42948 | 2024-12-12 01:13:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d4589758-ad92-3416-b397-f3c2673676a3 | -14.75728 | -52.64633 | 2024-12-12 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| d0a5b187-b473-3412-81d4-afe4574ade97 | -18.04342 | -52.99031 | 2024-12-12 01:15:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 5a7e9c86-aec4-3708-8398-dfe616ede6b8 | -15.98135 | -56.27691 | 2024-12-12 01:15:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| ad9a5ece-dbcf-388c-aedf-1800e277c2fc | -18.02552 | -52.99299 | 2024-12-12 01:15:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3b92ab88-306b-3bcf-91d7-f65edc10ab03 | -15.08505 | -59.6306 | 2024-12-12 01:15:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 0ff616a6-8fd1-3935-b375-63df2bfd8c2c | -18.03319 | -52.98221 | 2024-12-12 01:15:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| e1b0cf91-764e-37b1-a27c-b83c459d54fb | -15.98289 | -56.28934 | 2024-12-12 01:15:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 23.7 |


[Clique aqui para ver as próximas entradas](README6.md)
