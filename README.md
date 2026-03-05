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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f905277f-48a3-381b-96fa-1fa0814e0bff | 2.7816 | -60.3528 | 2026-03-05 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 7a54cd6b-21fc-36f2-a8ea-67acd55af296 | 2.9627 | -61.0324 | 2026-03-05 00:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b2b2fcf9-6460-37e2-8b04-60ca9f61ec74 | 2.9809 | -61.0321 | 2026-03-05 00:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| ea82daea-dad9-31c0-b658-b50feca3e6ef | 0.0455 | -60.9799 | 2026-03-05 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 91badb91-4d80-32ac-a624-cc3220f41ab9 | 1.5047 | -59.9116 | 2026-03-05 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ba078341-f44f-35d0-b7e0-c7551f0c9d77 | 0.0638 | -60.9799 | 2026-03-05 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 14e2894b-be35-3bd9-8855-730782aedeab | 1.5047 | -59.9116 | 2026-03-05 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b28be479-9746-3aa8-855e-0cf852093b3d | 2.9627 | -61.0324 | 2026-03-05 00:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 2c7ed8a9-9459-3762-b3e7-5450c71aea35 | 0.0273 | -60.9799 | 2026-03-05 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c61cab68-1730-3e84-914b-c32937c8b762 | 4.5364 | -60.5837 | 2026-03-05 00:10:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 355673e9-a4fd-35dd-8d88-c923d94987a5 | 4.5181 | -60.5842 | 2026-03-05 00:10:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 7ef8df0a-e4fd-31d8-854c-26d805f7dcbb | 0.0455 | -60.961 | 2026-03-05 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 68b1bcc5-e75f-35f5-baae-af13de0024c1 | 0.6654 | -60.297 | 2026-03-05 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 7100104e-000d-3d28-ad78-c0fe54459cf7 | 2.9809 | -61.0321 | 2026-03-05 00:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| b119d17b-37fb-36dc-a0d7-4ac9b9626839 | 0.6654 | -60.3159 | 2026-03-05 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e43b9465-d8ba-3972-aa4a-c2c7d51599c5 | 0.0455 | -60.9799 | 2026-03-05 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 258.9 |
| 2a540a00-0996-38d9-8d32-addcb78cd4ea | 2.7816 | -60.3338 | 2026-03-05 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 7dc70ecb-2d0c-3488-9ab6-7b9f3a476c4a | 2.7816 | -60.3528 | 2026-03-05 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| fa8f1d1e-953f-3ca6-b550-d5d613548240 | 0.0455 | -60.9988 | 2026-03-05 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| c0b3ee5e-333f-3f74-be82-1607e5b3c7b6 | 4.5181 | -60.5652 | 2026-03-05 00:10:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 6cd2a315-0c87-341d-b99f-2660d1750525 | 2.7816 | -60.3338 | 2026-03-05 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 7e70f2ad-e57e-3157-aad1-3518dbb34883 | 0.6654 | -60.297 | 2026-03-05 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 5f085f11-2ea6-342f-9f18-fa5b05cc106b | 2.7816 | -60.3528 | 2026-03-05 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 47069676-e37c-3073-915d-784d87e0943a | 0.0455 | -60.9799 | 2026-03-05 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 223.0 |
| 1fead30e-2b18-31e6-9720-dea28625ad3c | 4.5364 | -60.5647 | 2026-03-05 00:20:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 48831621-ad73-3229-9636-40bc29e19c1c | 0.0455 | -60.9988 | 2026-03-05 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 01d198c0-2b04-3577-b810-84e1b9895958 | 0.0273 | -60.9799 | 2026-03-05 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ea857c76-8e5c-3840-ae19-9b27da6001b8 | 4.5181 | -60.5842 | 2026-03-05 00:20:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 89a0b796-35fe-3fc6-bbb4-d28eeb4c2ce2 | 4.5364 | -60.5837 | 2026-03-05 00:20:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| a2b420d6-0cbe-3f7d-b8d9-4cc28c7f8f53 | 1.5047 | -59.9116 | 2026-03-05 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| cee5a302-b3e8-3860-bf8d-11b173ebf128 | 4.5181 | -60.5652 | 2026-03-05 00:20:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 11b41d3b-e687-32ca-b3a4-274bb99db560 | 0.6654 | -60.3159 | 2026-03-05 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a864aaed-8c26-3b8f-8075-6d753dabc989 | 0.0455 | -60.961 | 2026-03-05 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 23781a21-5572-3b44-a1f0-fb059b9f91db | 0.0273 | -60.9799 | 2026-03-05 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 44331646-3271-3b03-885f-f72d4e0a17c8 | 0.0455 | -60.961 | 2026-03-05 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 05be6939-7b0f-3bc2-8855-e13201b2e4b1 | 1.5047 | -59.9116 | 2026-03-05 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ed7e3140-c62d-3932-ac23-74e5a4e1da4d | 0.0455 | -60.9988 | 2026-03-05 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1b2e7e27-0019-3621-80f3-f3cc8596e64d | 0.6654 | -60.297 | 2026-03-05 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 3c0244a6-dd2e-3c2a-a2b3-1fc87df59818 | 2.7816 | -60.3528 | 2026-03-05 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 331be7c9-ef4c-334a-85e6-a93ec8338c3a | 2.7816 | -60.3338 | 2026-03-05 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 157.2 |
| eb35c038-6685-3707-8674-76adc35db116 | 4.5181 | -60.5842 | 2026-03-05 00:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| cbe22083-45e1-3196-9e1d-c0634c8209b5 | 4.959 | -60.268 | 2026-03-05 00:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 7d04eb67-7353-31d6-96b3-ae7e7df66da3 | 0.0455 | -60.9799 | 2026-03-05 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 177.3 |
| e8166f3f-b441-321a-bf6b-9fed310aa3dc | 0.6654 | -60.3159 | 2026-03-05 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 22ba2bea-435d-3388-87c5-fbbd5c0a3f4a | -21.710199 | -47.099201 | 2026-03-05 00:37:00 | METOP-C | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 770440f2-87d0-3e70-a353-be6743d89699 | -20.942499 | -48.715199 | 2026-03-05 00:37:00 | METOP-C | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6f4a2bd4-10db-3071-8233-406152c163bc | -21.2971 | -48.599201 | 2026-03-05 00:37:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ceec019b-6665-3f43-991b-3bc0bb2e9a69 | -21.215401 | -49.486 | 2026-03-05 00:37:00 | METOP-C | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 19e678be-3cef-3e64-8d8c-dd5f64d437bf | -21.305 | -48.587898 | 2026-03-05 00:37:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a4be4b5c-cdfd-3590-9322-16dc67fe7982 | -21.2952 | -48.59 | 2026-03-05 00:37:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b007476c-ff5e-3ed0-97a4-6509217f2aee | -21.711901 | -47.107201 | 2026-03-05 00:37:00 | METOP-C | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3997b983-d607-338c-a695-17d217093703 | -22.960501 | -49.905701 | 2026-03-05 00:37:00 | METOP-C | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 65e06c64-db88-3e98-967c-6619caa4dc41 | -21.3069 | -48.597099 | 2026-03-05 00:37:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8fb1f87-95d6-32c4-a8e7-450544fb1790 | -21.476999 | -48.684299 | 2026-03-05 00:37:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d7942297-5cbd-37e2-a95f-ebd3a84e9ed1 | 0.0455 | -60.9988 | 2026-03-05 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e3578165-efd4-3a0a-af01-1f212a63f01e | 0.0455 | -60.9799 | 2026-03-05 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 188.2 |
| 8e0d61fa-7f02-3fdd-ab34-d28ed2d1c180 | 2.7816 | -60.3338 | 2026-03-05 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 802f99d2-2b89-32ac-97f8-480e780020a9 | 0.6654 | -60.297 | 2026-03-05 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8c61af63-4b2c-331d-ac99-97917256ec22 | 0.0273 | -60.9799 | 2026-03-05 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 4c24f09f-8269-311d-aa5d-ad6295ccfc00 | 2.7816 | -60.3528 | 2026-03-05 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 104.0 |
| f5df5dd0-0bb1-31db-9df7-3199380fc489 | 1.5047 | -59.9116 | 2026-03-05 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 28062656-a871-3c47-93cc-266998ef8cae | 4.959 | -60.268 | 2026-03-05 00:40:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 1452748d-c51b-34fe-9f54-9f04fe5f3c6d | 0.0455 | -60.961 | 2026-03-05 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 4a222b17-22b0-3a1a-a8ab-77a1d81c8627 | 2.9627 | -61.0324 | 2026-03-05 00:40:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 764171cb-b7c8-3660-9188-dfc6309ebbc0 | 4.959 | -60.268 | 2026-03-05 00:50:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| cef303f4-0e45-3594-b240-cc8baf51f395 | 3.2739 | -60.7243 | 2026-03-05 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f6f99770-5252-35a7-ad21-20622f29ba7a | 2.7999 | -60.3335 | 2026-03-05 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 733d9ea3-fe4c-3966-903b-76748e11f704 | 0.6654 | -60.297 | 2026-03-05 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 4b502ef8-a040-3acf-bbaa-21d45a17074e | 0.6654 | -60.3159 | 2026-03-05 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c2fbe518-d7bf-3a66-ae68-e0cb3486c84e | 2.7816 | -60.3338 | 2026-03-05 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 172.6 |
| 8d22cdd6-6f75-304d-adc7-845047488ed8 | 2.7816 | -60.3528 | 2026-03-05 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 100.4 |
| d6228a87-2687-381f-be67-5b6aaee270ea | 0.0455 | -60.9988 | 2026-03-05 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8c92fe98-5ed3-3f90-a6a2-5a34cb6d5bb9 | 1.5047 | -59.9116 | 2026-03-05 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 4d016adb-6761-304e-b08b-91ebeb429a06 | 2.9627 | -61.0324 | 2026-03-05 00:50:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 756708e6-4b95-37e8-9efc-ce4820ad69a7 | 4.9589 | -60.2871 | 2026-03-05 00:50:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 7907984f-ca75-3161-a331-5985472d8c0f | 0.0455 | -60.9799 | 2026-03-05 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 2afc1fcb-baab-3a82-a01d-e234aded79eb | -25.00844 | -49.29469 | 2026-03-05 00:58:00 | TERRA_M-M | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 87b46b47-aab9-3517-99e7-5af10e42e264 | 3.2738 | -60.7432 | 2026-03-05 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| df44d1a6-43fa-3130-aac4-9933d483c49f | 2.7999 | -60.3335 | 2026-03-05 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 78312a9b-3bba-30b7-9a2e-2e3c5b440609 | 0.6654 | -60.3159 | 2026-03-05 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b41d80a8-d9b0-3483-ad18-762a35211633 | 0.0273 | -60.9799 | 2026-03-05 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6127fe09-d493-342b-943e-ecb2738af448 | 2.7816 | -60.3528 | 2026-03-05 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 6c199402-0069-32e0-9db8-de42d48b8334 | 0.0455 | -60.961 | 2026-03-05 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e0d0ec36-9d30-3ef2-a1a5-c943a7c4f2a9 | 4.9589 | -60.2871 | 2026-03-05 01:00:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| c91ed907-2e71-3315-9fa8-6c9324320375 | -22.1472 | -53.8087 | 2026-03-05 01:00:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| c980a275-a6a1-393e-86ed-892de7b70bfe | -22.1679 | -53.8048 | 2026-03-05 01:00:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 85.8 |
| 76f1e17d-9feb-338b-9018-a8173a1e40c6 | 2.7816 | -60.3338 | 2026-03-05 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 183.9 |
| 3525da1a-3ac1-3131-83c9-8437bd2fb315 | -22.1477 | -53.7867 | 2026-03-05 01:00:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| e7605da5-7b34-3b62-8f15-6b27dd789b23 | 1.5047 | -59.9116 | 2026-03-05 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| be9b2864-55f5-399e-bd7c-669c9561dbfa | 0.6654 | -60.297 | 2026-03-05 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1cf2dedf-317d-3223-8883-0566b2312a83 | 0.0455 | -60.9988 | 2026-03-05 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 63bf907e-1297-3d37-8eb0-a225c3691603 | 0.0455 | -60.9799 | 2026-03-05 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 3a4ee459-5510-35fb-8058-659228a635bc | 4.959 | -60.268 | 2026-03-05 01:00:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7d4da2ad-179a-348e-8d5e-db6a83b42896 | -21.30005 | -48.59172 | 2026-03-05 01:00:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| ab70116c-5f14-3700-86b1-e7240010d3da | -22.14579 | -53.80146 | 2026-03-05 01:00:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 31.1 |
| d915b2ba-8408-3fdb-ad84-33bff665e484 | -21.30014 | -48.59827 | 2026-03-05 01:00:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.9 |
| 784a3f02-5b9c-3fd8-b45d-2ae564f4ba1c | -18.89649 | -54.73074 | 2026-03-05 01:02:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3b1b689e-d01b-3127-a09d-a5df5099dde2 | -16.58447 | -57.80922 | 2026-03-05 01:02:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 69808efd-ed3b-3826-ac15-ab0c126075ec | 3.28085 | -60.74808 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d3b14413-2678-352c-b760-01d4b5bab861 | 0.05107 | -60.99141 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 22.9 |


[Clique aqui para ver as próximas entradas](README2.md)
