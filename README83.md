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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 985f774c-3591-39cc-87de-332d14e4b29a | -2.64189 | -51.72977 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6339a3ea-925e-3026-8b54-2e37f5cf2d82 | -2.64058 | -51.73856 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 65ac8c7e-8dfa-384a-9d5b-d50883f0cffe | -2.63926 | -51.74734 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a11179a-fe7a-3d28-a008-4344f4987fcb | -2.63915 | -54.29789 | 2024-10-28 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 986f62a4-d834-3e73-85b6-85bbecac3756 | -2.59863 | -51.77736 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e8c6e094-6995-3034-8b05-66027306cdc1 | -2.59389 | -49.19288 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ccd99402-2c1b-3c96-bc5d-4370b92269c6 | -2.58793 | -49.23372 | 2024-10-28 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| beb5396d-0ef6-3fa6-a9c7-88bd99356729 | -2.55796 | -49.82306 | 2024-10-28 05:44:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 03d14611-3059-3e3c-9f9e-d71b7a75667a | -2.53814 | -49.82996 | 2024-10-28 05:44:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 132b4919-9daf-3ad3-97fa-3f5ad285d3b2 | -2.53672 | -49.8395 | 2024-10-28 05:44:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a242891f-e5e5-322f-a5b1-a6349236db22 | -2.52214 | -47.44414 | 2024-10-28 05:44:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| df11f9f2-7d2d-3e76-beba-76dcb4de125f | -2.51276 | -51.17763 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 9a23e4c8-53fb-3269-b78c-79d6a5eeabc5 | -2.49184 | -48.05951 | 2024-10-28 05:44:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5960828a-daf5-36cd-a176-0caf248b514e | -2.46115 | -50.40877 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db05e366-40d0-3c13-b25f-4aef820965b9 | -2.43824 | -50.37751 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba876fea-5fbc-3567-8010-3791ba497b74 | -2.41176 | -48.54064 | 2024-10-28 05:44:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 04657ee6-eb50-39de-bc61-9fff2020fedd | -2.41015 | -48.5517 | 2024-10-28 05:44:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 10cb87d5-45cf-3aaf-980e-c997efb8eb85 | -2.4045 | -50.41919 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 52f2069b-a9f6-3fd9-8da3-ba3d67aac97e | -2.40316 | -50.42829 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| be241587-e15c-3e9d-ac1d-bd5b4ac6dcad | -2.4019 | -48.53922 | 2024-10-28 05:44:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| a4b61299-bc31-3bcb-baf4-ba5f5f82e00d | -2.4003 | -48.55029 | 2024-10-28 05:44:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 825fdd7c-d6f1-3afd-8801-17e724732420 | -2.39204 | -48.5378 | 2024-10-28 05:44:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3b553cf8-a128-3bc8-b21d-350670634588 | -2.36482 | -47.66581 | 2024-10-28 05:44:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 627fbc68-56af-3e77-9d6b-73910ce48fd2 | -2.34864 | -49.54348 | 2024-10-28 05:44:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d2529442-38b4-3775-a48f-990c918247e5 | -2.27902 | -53.76919 | 2024-10-28 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 79ad2508-89b0-394f-8e29-13d9a8d5f9c8 | -2.27748 | -53.77926 | 2024-10-28 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ced950e5-2777-3d30-a71a-0a27e3d43f26 | -2.26959 | -53.76781 | 2024-10-28 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| f9afcc15-b465-3232-8ae1-3ab5531ce557 | -2.26805 | -53.77789 | 2024-10-28 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| a4b9dba5-7b6f-36a7-a8b0-f0b3eae270d5 | -2.26649 | -53.78805 | 2024-10-28 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| d7950b57-b2fd-329c-9c15-5cd4e0669d66 | -2.19961 | -53.68005 | 2024-10-28 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 63a08913-1143-320e-849b-9811653a174c | -2.19808 | -53.69007 | 2024-10-28 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 62b10a41-d382-34ae-9a16-34b666e93f13 | -2.19758 | -50.75398 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7018c02c-b567-3bf1-9c16-6532b54d2e32 | -2.19477 | -50.58895 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 533a1f38-6fe6-3aa9-816e-0694cf0cba09 | -2.19344 | -50.59794 | 2024-10-28 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b0d89db6-ea25-3b2f-9a08-38d6a1f3b79e | -2.06001 | -52.16495 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5607c410-9f18-3fa7-9516-67b6bda6dd75 | -2.05112 | -52.16365 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| ec8e23e3-f805-3090-bb5a-3e501cb5a72a | -2.04541 | -52.07438 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 69fd3602-eb85-3298-8dd3-4a2be42434d8 | -2.04409 | -52.08325 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 4759087e-cd00-3447-8f7d-12d7822a74e0 | -1.9819 | -52.07418 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| c1576603-5dc9-3a22-8f36-0d978fe58871 | -1.98057 | -52.08307 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 274a3eba-8afe-36e2-bc7a-6b232eda30d8 | -1.97168 | -52.08177 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f5a89cc5-4659-38ed-8c37-d83662873beb | -1.92689 | -52.12396 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 99bbc459-4a3d-34a0-8769-e9aec57868fe | -1.91977 | -52.05031 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b8946731-4a7a-31bc-8e32-a5a2e407ca18 | -1.918 | -52.12267 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7ff5f969-371b-3abe-81ef-393f9d72971d | -1.91667 | -52.13156 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a20de37-7006-3a91-b07c-f30f053818e9 | -1.8961 | -52.32958 | 2024-10-28 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bfb2de3b-71cf-3251-b193-78478c77b7f1 | -1.76673 | -47.02062 | 2024-10-28 05:44:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2db194d7-38db-36f6-b11d-1d5982ccef6a | -1.53711 | -52.07868 | 2024-10-28 05:44:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 648c90c0-cd6a-39e4-84e7-e95f37170466 | -1.27809 | -54.12744 | 2024-10-28 05:44:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88e34696-99fe-3439-8615-da4fc3a88d6b | -1.18551 | -53.50684 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 25e502fa-b217-3351-8ff0-b7205bff5f7c | -0.97815 | -53.69735 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7cbe5ae4-97cb-3ef6-89f7-8f13af3d345c | -0.98611 | -53.70907 | 2024-10-28 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a6626bab-8aa9-3715-a15c-01577bbf5961 | -0.98766 | -53.69885 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f514482e-39cd-32ff-933e-50a41e45a8f1 | -1.07454 | -53.6662 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2630ca38-8d09-39ac-af99-446b782c2e66 | -1.07611 | -53.65592 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 83817f77-ab7b-3553-b458-ceec615ae0c5 | -1.17611 | -53.50537 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| b8323f62-2175-30cb-9f2d-a32660108700 | -1.16668 | -53.50418 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0653f883-a929-372c-9283-3bcc354f3c22 | -1.08402 | -53.66769 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bdd8e799-59fe-3412-a25d-648c546f10ee | -1.0856 | -53.65734 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 390f3245-81a2-395e-8955-821360a118de | -0.26673 | -48.77978 | 2024-10-28 05:44:00 | AQUA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dbb0d684-8354-3ee4-ae6b-a5b26f854322 | -1.17758 | -53.49552 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 96d8a7a9-31c4-379a-af15-a5e7fe74428c | 3.58866 | -51.28302 | 2024-10-28 05:44:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e375b427-2ec2-36ed-ab7b-77db88d730dc | 3.58751 | -51.27649 | 2024-10-28 05:44:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22c7f88d-7359-3bf5-bdea-2d55fd34649f | 3.47009 | -51.24792 | 2024-10-28 05:44:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a89e2963-a1c5-32c3-9ad3-c36dcf700959 | 3.46884 | -51.24649 | 2024-10-28 05:44:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24149a4f-bbb8-3dfa-942b-d2bb80c335fe | 3.46313 | -51.24915 | 2024-10-28 05:44:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d9a001d-f8b9-3826-aea6-6170193e79cb | 3.46305 | -51.25431 | 2024-10-28 05:44:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca52fb11-8737-321a-bdbe-4e4d2a3cce61 | 3.46188 | -51.24769 | 2024-10-28 05:44:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddc9ed6c-0ab4-33da-afb2-097875078907 | 1.92226 | -60.49307 | 2024-10-28 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fefc0b5-387c-35ef-bd47-b6c47add380c | -1.9763 | -52.0804 | 2024-10-28 05:45:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3b0fdfee-f3e1-3647-9785-d5eb242cbd11 | -2.4104 | -48.5479 | 2024-10-28 05:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0b88e465-8626-3d11-84a1-61d88d71cd77 | -2.8699 | -49.2615 | 2024-10-28 05:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c5c16ff1-114d-3a40-81ec-d8ebd9516d2a | -2.8884 | -49.2609 | 2024-10-28 05:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ac0c5380-5370-3f55-9a88-16f17ae52304 | -3.0317 | -50.4176 | 2024-10-28 05:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e4c903db-30f1-3df7-9bec-f0ad18bc0a54 | -3.497 | -45.7971 | 2024-10-28 05:45:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 16f3a810-eac0-3546-83be-4658bae16c91 | -3.5155 | -45.7964 | 2024-10-28 05:45:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1e4b68e9-e192-3d1f-825e-c839f8d11adf | -4.74354 | -50.82479 | 2024-10-28 05:46:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 988ec7e2-1e4b-3859-a1e4-35527c328bc9 | -4.47827 | -50.99181 | 2024-10-28 05:46:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f222fa0-0867-375d-9a3d-dfeece003ac1 | -4.46931 | -50.99051 | 2024-10-28 05:46:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7fa0c8cd-eaca-36d1-88db-5487ca54f7ab | -4.09968 | -53.9389 | 2024-10-28 05:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff9c0b3b-ac67-362a-8fd0-44be3da3ee4e | 0.11424 | -62.54228 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0fb0a453-43e6-3cc8-bd57-03ba0b70b2ef | 0.11387 | -62.54375 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d66f8549-252f-39ee-851b-6ea14e8744c8 | 0.11068 | -62.54283 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8fe141e-e32a-3972-a1e1-27c58e2305fb | 0.11042 | -62.58814 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bbd10b1-0cc6-3053-8650-56d91a2b416c | 0.10749 | -62.59269 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a079ec74-40ce-3c14-bbd6-1ddea8db9b23 | 0.10712 | -62.54338 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce5d9198-6380-347e-b283-22bdabee791f | 0.10456 | -62.59725 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2a2c240-0166-3dc4-a319-5ae1376bb6b5 | 0.10394 | -62.59325 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 714d3cc1-911f-3e69-a9b2-ae10164af2fb | 0.08974 | -62.59545 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49613746-d361-34fc-bb86-c6142e4c69ad | 0.08911 | -62.59144 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 210a369a-fc99-361e-8440-fde30fd45587 | 0.08619 | -62.596 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe3c3ff2-21ae-33c2-b92f-d95e3dde83be | 0.08556 | -62.59199 | 2024-10-28 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69236cd3-9e5b-3976-9cde-362dd55ca756 | -4.21461 | -55.50434 | 2024-10-28 05:46:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36d1eac2-39a6-3252-a19c-320661dedf71 | -4.09637 | -53.9455 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8375d16-cfe9-3a14-9d1c-165f7c4c3cb2 | -4.09066 | -53.93815 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8a534ad-8ddc-3773-a3d4-577716361309 | -3.59619 | -53.78523 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c24e22f2-28c0-3f44-8a83-706a506ce3be | -3.59193 | -53.78185 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d22fd6c8-288f-3470-b8e1-ec6d26addf98 | -3.59112 | -53.78725 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4064a57-f1bf-3106-881d-1a6e3a6851be | -3.58966 | -53.78358 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf3db5d2-c687-33d7-8fcb-177addb3f398 | -3.56842 | -54.67751 | 2024-10-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README84.md)
