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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fcfb878-5cce-378b-99a3-f54daad85449 | -3.12266 | -50.35008 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b628060d-ccaa-3310-9ad2-038fd350cb4d | -3.12206 | -50.35369 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7e3ebf8f-1590-34e5-99ff-c5e210bc0bb9 | -3.1172 | -50.34908 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8f4378e-747f-321b-8b02-cb73726f2993 | -3.1166 | -50.35269 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 340bd27a-c1d2-3457-bca2-1a3e78aa44ff | -3.116 | -50.35628 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdfeab29-1127-39d5-a6f7-1599784aef4c | -3.04357 | -50.41748 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c06ee4ce-a11e-3f00-9dbe-5f8b36a01c97 | -3.04342 | -50.41801 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 116cb0d0-cc24-3f40-b94a-2beb1d1be980 | -3.04296 | -50.42122 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 384d2052-9eb8-3ded-b043-967e9764a052 | -3.04279 | -50.42173 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a667985d-0a14-32fa-bb2d-624a5e9a544a | -3.04235 | -50.42501 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6499d00e-37ca-3c0d-922e-8fb6ceeab854 | -3.04213 | -50.42558 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5328255-5d9b-3f53-abd7-5aa6bb5b69f2 | -3.04173 | -50.42883 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b57aef47-1d9b-3e16-924e-fae37a567889 | -3.0415 | -50.42932 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1a61bb0e-a52e-3b24-991e-eae6faf2c00b | -3.04114 | -50.4324 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d421735-9967-3f9c-8535-1c8811efbefc | -3.04089 | -50.43287 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1991f36c-3307-3271-a75b-0e8ca5f28e98 | -3.03791 | -50.4171 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8712bee2-e31f-3e2e-ba21-8015949cdcb8 | -3.03745 | -50.42027 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bebbd9c-2860-3d6c-929d-1453bcc6cb46 | -3.03728 | -50.4208 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcc20713-255d-3f3b-9ef6-4305cbec3e2e | -3.03683 | -50.42406 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1daa35b-ff6a-354e-bc0e-9fbd373b7c60 | -3.03663 | -50.42458 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08e5a504-cabd-31f8-96a8-916aa113b067 | -3.03621 | -50.42786 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ed0d638-f45a-35fe-893e-7ec9a2217628 | -3.03599 | -50.42837 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ec58b98-606d-353d-be05-cb55b137244b | -3.03561 | -50.43156 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e25d57aa-7bab-3691-a0a3-45a9340e54c2 | -3.03536 | -50.43201 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57dd0d8d-2bcc-3f5c-a7c5-a81131134c37 | -3.03256 | -50.4155 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ff69187-1767-3f09-a6ff-a5c5e1d50950 | -3.03242 | -50.41604 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3899b504-cf52-3082-844f-9af2038edf39 | -3.03197 | -50.41912 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 800dea7d-6445-3626-ad71-f73daccf7944 | -3.03181 | -50.41963 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a2e72ff-23d6-3e6b-aaec-ceae099ba8d0 | -3.03137 | -50.42281 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aaf3f15-e180-3a7a-a47e-69f89b030327 | -3.03115 | -50.42346 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d606e6f9-d453-349b-8498-21e52b5a8fa8 | -3.03073 | -50.42674 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d119cfa5-2acb-3442-be13-f3928dd88a33 | -3.0305 | -50.4273 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69ad1acd-5f16-3aa7-afc1-388e4f0e12ac | -3.03011 | -50.4305 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a8ea934-b0a4-3a2f-882b-0afa7585dc5d | -3.02986 | -50.43099 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a035794-5531-3edc-b96f-7c2d00747b10 | -3.02766 | -50.41087 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10b10b56-a78b-3d0f-a95b-06518fe93a85 | -3.02706 | -50.41451 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04b84ca9-7900-3f67-ba42-932076640d68 | -3.02647 | -50.41809 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df682e47-e846-3094-8d1d-e73621fab811 | -3.02587 | -50.42178 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e777962-7211-3a2e-b95c-9c7d8d943956 | -3.02524 | -50.42562 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4599240b-d5c2-3f76-b73a-21e4b05a7a1c | -3.02461 | -50.42944 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eab2b2ba-e778-3cdf-a7da-71d90677d22f | -3.02156 | -50.41349 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3498e4d6-41d5-3026-a404-0ce9a880d8d1 | -3.02096 | -50.41715 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa45a46d-2917-3b43-8ccb-d433d9a9e8b7 | -2.91914 | -50.28074 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e755ec3-3a7b-3d07-aeb0-53bcaeb7c856 | -2.91853 | -50.28439 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f60453a0-1078-3289-9c91-3b5ba645d379 | -2.91367 | -50.27977 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f13dedb-2db9-3e1e-976d-48462d327320 | -2.91307 | -50.28336 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c14a7a76-501e-3681-829f-50901a4d74b3 | -2.91248 | -50.28696 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e83badda-4ebe-3de6-84b6-77951d169e59 | -2.91188 | -50.29059 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50c8762a-5098-3a83-9b95-2e014d38c69e | -2.90701 | -50.28598 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c3578b9-c340-384d-be8f-729e7a32463f | -2.90642 | -50.28957 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93041cf4-a7a1-3f1f-90d9-32694f8899a6 | -2.89896 | -50.40284 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f49b2767-5842-33e1-abe2-b2f54e4972fd | -2.47753 | -50.28342 | 2024-10-28 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f279bd93-e131-3e86-a989-599a8052d016 | -2.4558 | -50.41529 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be89427d-8c16-3ae0-bb21-ccd6fb141b56 | -2.45517 | -50.41908 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 386ecdf3-171f-341a-990d-094233ac8e79 | -3.01512 | -50.48732 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bd90702-be4a-3c1b-bac7-355c24478c14 | -3.00958 | -50.48636 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a33afd79-3d4f-3f82-b256-7b7037a866ad | -3.00837 | -50.49374 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5ec4ad6-ac1b-337c-ad2d-46a9e613eeb5 | -3.00776 | -50.49742 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7fd238c-a1d4-325c-be7c-cb47a13eef46 | -3.00283 | -50.49277 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c86184eb-863e-30f8-bfff-47582be738d3 | -2.9979 | -50.48813 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42c7f285-8bb3-3c50-ae27-04a540200784 | -2.9818 | -50.48215 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2dffa8b2-3885-3e07-bd84-7ee7f50fcb00 | -2.97685 | -50.4777 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 33500e14-5924-3797-bb51-ae1d8595a3ec | -2.97624 | -50.48136 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d7a3663e-85d6-3ce0-ae04-71a19b8be9d0 | -2.97566 | -50.48483 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 83660354-3860-36c4-8a2a-74dbc4c32d45 | -2.85298 | -50.47406 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 210b1baa-1d2d-37a1-92bc-e2e028cde43d | -2.85233 | -50.4779 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb8a5f58-60e4-3257-8c46-6118991abc08 | -2.19552 | -50.76332 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e55bdc57-d083-37f0-bdc5-ecf5c1814d01 | -2.19344 | -50.59852 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5335dd42-d99d-353c-be83-128d5fcfaa0f | -2.1928 | -50.60239 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3820a066-a576-3c45-816d-950da76c0675 | -2.18778 | -50.59763 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc1fb5ed-b835-3d2f-a9b9-62c9da0185ff | -3.25767 | -50.65835 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d21415ff-08dc-3e82-99f6-eb5d9f5f44ec | -3.25398 | -50.64624 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6af01613-6d56-33c1-a7e5-d92560f53bd8 | -3.25336 | -50.64992 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 257c1e92-77b4-3172-a9f7-6707dacd24b0 | -3.25274 | -50.65359 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06142ec6-c64f-3487-9d30-1979a06f1b5a | -3.25211 | -50.65731 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82bc5d60-0d4f-3a57-9f5d-a35d38ed2a6e | -3.12473 | -50.60477 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a245242-43ec-3f56-a858-3da4643a4266 | -3.12406 | -50.6087 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f52bf358-44a5-315e-81ad-555cd7161b12 | -3.07999 | -51.14481 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f2271eb-fe53-368e-ba5b-f7347c6f8ea5 | -3.07834 | -51.11934 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eca75db0-4773-31d3-9ef1-87cd8dff9826 | -3.07764 | -51.12346 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60738517-5795-33b8-a798-04f135524240 | -3.07695 | -51.12755 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bfade12-bdb0-3fc3-96cd-f9b30f3b16e2 | -3.07627 | -51.13163 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69988339-476c-3071-9460-98dacb690d8d | -3.0749 | -51.13973 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9710d9b-d3ab-3109-b441-f5f5498dd24a | -3.03211 | -51.46574 | 2024-10-28 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 095e4801-c31b-38dd-a737-e209138d7044 | -2.95384 | -51.00408 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1f6a239-d2ec-3e40-8d77-59f387a77dce | -2.88205 | -51.75922 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 045abf27-c24d-39fd-bf87-5ddc18620379 | -2.84282 | -51.80785 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 601ff99f-a27c-3461-8785-c24081f722d3 | -2.83677 | -51.80681 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 305c4171-7ef4-34f3-8c1f-3ca41b996760 | -2.836 | -51.81134 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db7c4c4e-735d-3aca-a592-fd1d1493522e | -2.80496 | -51.81082 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db6da4bf-5c2b-3a01-8aea-d59634567450 | -2.80422 | -51.80717 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ec7b7a3a-597a-3c95-85fa-a1ef7eafb2c4 | -2.80348 | -51.81164 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8f5efb9-b115-3c42-8900-1e1502e00d6d | -2.79965 | -51.80548 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 335b928f-e781-3cf2-8f9e-d00ece36ce6c | -2.7989 | -51.80985 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46d0c72f-734b-34d4-9ca9-0d9f6924eda1 | -2.79814 | -51.80627 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9223a1e5-5516-3296-ae30-491870f2a903 | -2.79813 | -51.81431 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d4ca198-ea8b-34ba-9385-bccdc221baca | -2.79742 | -51.81063 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0fbaf6e-7d13-384d-8ec8-b2a2aefdafa1 | -2.79358 | -51.80457 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1eddacf9-5402-3837-8928-013d707b8970 | -2.79282 | -51.80896 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87509c7b-c90b-3304-b9c0-fc3febb89a83 | -2.79207 | -51.80535 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README35.md)
