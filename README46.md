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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 172318fc-1e20-32db-ab5b-96749ebb28a2 | -4.3526 | -43.0116 | 2025-10-31 14:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 620317e9-00ef-341d-bf31-f19a442b358d | -4.3872 | -43.406 | 2025-10-31 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 054383fb-17a5-3601-ad0c-097c04871aee | -4.388 | -43.2896 | 2025-10-31 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 1e899593-46c0-3195-abb8-b36b2407f73a | -8.0212 | -42.5121 | 2025-10-31 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 612f689d-6b6c-36c4-95bc-cb2fd7ecce6f | -4.6555 | -42.523 | 2025-10-31 14:10:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 80bf3ca8-5088-3f79-9e9b-ad323f86353f | -4.4054 | -43.4746 | 2025-10-31 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 83a8fed3-9f4c-310d-8eb2-6752447a013b | -8.0401 | -42.51 | 2025-10-31 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 886d518a-cc92-38b3-bdff-195395d7e6ba | -5.8485 | -41.2637 | 2025-10-31 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 131.9 |
| f2284ace-f9b4-3772-8683-92da7a2b8e19 | -10.285 | -44.581 | 2025-10-31 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 52d00df1-a1ac-3ed7-8ca9-d9123429a5b4 | -8.0401 | -42.51 | 2025-10-31 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 1fa96412-b29f-34f8-bcf0-077a9d9fe078 | -10.2473 | -44.5628 | 2025-10-31 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 8125df08-8d52-3d69-b965-f1973b7bd4d7 | -4.4054 | -43.4746 | 2025-10-31 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 019dffe3-60da-3423-9911-0207265fcdb4 | -10.266 | -44.5835 | 2025-10-31 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 591a9e2d-4629-3269-bf91-d4ff0bd09c64 | -10.7587 | -44.7258 | 2025-10-31 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| a192691d-6f6c-350b-b40f-a8c9cd354e58 | -10.2477 | -44.5396 | 2025-10-31 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 05cd8ed6-54ff-32ab-b39b-f3d59366b955 | -10.2854 | -44.5578 | 2025-10-31 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 212.4 |
| 662d34b0-cfc3-3600-a9a5-b6a82428643b | -4.388 | -43.2896 | 2025-10-31 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2603a785-6306-3419-a263-41992374e61c | -10.2469 | -44.586 | 2025-10-31 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 6cbc4cd7-43a0-349f-96ea-53c33c11ec07 | -4.903 | -42.0085 | 2025-10-31 14:20:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 13008c19-34a4-39d3-b7b8-183d06241fd8 | -10.7396 | -44.7284 | 2025-10-31 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 594c114e-f833-3c3e-881c-339ed8e7d441 | -10.4417 | -44.3051 | 2025-10-31 14:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| d99a2462-a137-37c7-87d7-e561eb6d8826 | -4.4899 | -39.6533 | 2025-10-31 14:20:00 | GOES-19 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 147.3 |
| a8103226-e187-3c10-8bde-0a0aae21ee46 | -10.2858 | -44.5346 | 2025-10-31 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 75380c07-d7c2-31dd-9dc8-e39cd162eae3 | -10.2656 | -44.6067 | 2025-10-31 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 230.4 |
| 57dd89eb-1680-3aef-8ea2-b2b602da5108 | -10.7392 | -44.7515 | 2025-10-31 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 18cfebad-4e59-3e90-b1b4-87e066694c82 | -4.3872 | -43.406 | 2025-10-31 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 8707aa50-71ca-3f41-aedd-50a569df9608 | -10.4604 | -44.3258 | 2025-10-31 14:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 23c7ff55-d4ed-3f1a-9e02-92b5a0af84b7 | -10.4222 | -44.331 | 2025-10-31 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| c4cb9825-5c0a-3a27-9106-bb5bd8327c9d | -10.4413 | -44.3284 | 2025-10-31 14:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 9ba32cd4-18f2-31aa-881e-d940523040ef | -10.4608 | -44.3025 | 2025-10-31 14:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| c8e2ee6c-e200-3a97-b3c7-23d628d81c01 | -8.0401 | -42.51 | 2025-10-31 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| dc452608-bc7a-32eb-9811-688fb82b3927 | -10.2858 | -44.5346 | 2025-10-31 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 0f48122a-8461-356f-a95b-ae21f31dfbec | -13.3549 | -54.3386 | 2025-10-31 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 92f27fe2-92eb-32d9-b5cf-f596519f6fd7 | -11.8756 | -45.3284 | 2025-10-31 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 11759715-872e-399b-81c0-3b07ca13d8df | -4.903 | -42.0085 | 2025-10-31 14:30:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 8cdaae5f-1dde-3468-bb75-d56bef3a0d7c | -10.7392 | -44.7515 | 2025-10-31 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 6d1f5536-2e2b-3b20-9805-24a854b3b851 | -10.7396 | -44.7284 | 2025-10-31 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 785f956c-dd79-3b17-9751-9499b8ba2177 | -10.4417 | -44.3051 | 2025-10-31 14:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| a13ebcee-4865-3854-b7c9-7489cfb597bb | -13.3737 | -54.3572 | 2025-10-31 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c57d192b-cce5-33cd-be7f-1f4daebe1706 | -10.4222 | -44.331 | 2025-10-31 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 782a3fd4-8883-354c-be7c-24a17d5114ee | -4.4054 | -43.4746 | 2025-10-31 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 9a745bdd-44a8-36ad-9d45-a0d5b5c43870 | -10.2663 | -44.5603 | 2025-10-31 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 72a6b916-f24f-3298-9689-cd9f96d51026 | -12.2999 | -43.1781 | 2025-10-31 14:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 111.2 |
| 5b727990-b92e-3b81-bf51-9299095d42ac | -11.6305 | -44.0413 | 2025-10-31 14:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 63365cf5-7e67-364a-81ac-0a8735d1d272 | -10.4226 | -44.3077 | 2025-10-31 14:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| ba027f29-67e2-32fb-8ed9-c3b2141ab0e2 | -13.3915 | -42.7221 | 2025-10-31 14:30:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 2ac16dba-0166-3cd3-8507-01a8620c4a80 | -10.4604 | -44.3258 | 2025-10-31 14:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| d7fcc4a3-357f-39f7-9404-d0cfff12d2a1 | -12.5475 | -42.367 | 2025-10-31 14:30:00 | GOES-19 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 61bfe7e6-9abb-35c1-ba6e-e97b77c3e556 | -13.3546 | -54.3593 | 2025-10-31 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 05e84df2-dd0a-39c5-9e73-f2a371e5fde8 | -13.3737 | -54.3572 | 2025-10-31 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| eeecfc46-91bf-3548-80a0-eadfcbf50df8 | -10.4417 | -44.3051 | 2025-10-31 14:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| f74524bc-cb9e-390a-b736-b65488977034 | -10.4222 | -44.331 | 2025-10-31 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| bc969ae1-2959-3516-8b2f-093c4ff2e371 | -10.2858 | -44.5346 | 2025-10-31 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 8f1e74cc-b767-3bdf-b1ae-07be768c9ddf | -4.4974 | -43.6778 | 2025-10-31 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 786959eb-5932-3505-9d88-b1b8b34b60c0 | -11.7413 | -45.348 | 2025-10-31 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 71330b22-0325-3cb5-b768-6b6152c8d3a2 | -10.2477 | -44.5396 | 2025-10-31 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| cc2b795a-389e-3a1d-8437-891bc5fc25d1 | -11.8756 | -45.3284 | 2025-10-31 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 9e18f105-2c60-33e6-b5a7-dbca90555513 | -10.266 | -44.5835 | 2025-10-31 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| afc83b2a-fd44-3567-85e7-91bffedb742e | -10.7583 | -44.7489 | 2025-10-31 14:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| e96aab87-2e8b-31b9-8301-abf58a491047 | -4.4414 | -43.6811 | 2025-10-31 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e65dedec-3d64-376e-941a-fa3961aae48c | -4.903 | -42.0085 | 2025-10-31 14:40:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| f931b119-4356-32cd-b006-3b5115522453 | -4.2032 | -42.9969 | 2025-10-31 14:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2cb7827c-916e-3ccd-9d53-a95b80c22fd6 | -13.374 | -54.3365 | 2025-10-31 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| c2a3f0ca-c025-3d09-a202-9f2b5e8846be | -10.2663 | -44.5603 | 2025-10-31 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 129.2 |
| dd5b80b1-fb11-3eb8-b923-1cb17f43d2c1 | -8.0401 | -42.51 | 2025-10-31 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 80a95cac-d083-37ff-bd76-8040a213d1ae | -10.4413 | -44.3284 | 2025-10-31 14:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 57dda100-abab-365b-991d-98deb0dc0a56 | -10.7396 | -44.7284 | 2025-10-31 14:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |


