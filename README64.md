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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1130f11e-4ca7-3917-9a90-823e304afee3 | -1.6604 | -52.7503 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab4304f4-e534-32db-ad8f-3902984c1ee2 | -1.70775 | -52.44521 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e846ca4-e86e-33fc-adc2-7ef48c3aad95 | -3.09927 | -54.01313 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e17a476f-5267-3d73-89e2-6a383250ce65 | -5.8195 | -46.4929 | 2024-12-03 05:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| bef22b56-2140-3cb3-ae9c-4fece59c970f | -1.0919 | -53.4561 | 2024-12-03 05:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f3f9559b-69d9-36aa-914d-066fcb7a4091 | -1.0735 | -53.4562 | 2024-12-03 05:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| c6aa7669-4a27-3503-b1e3-47a261507914 | -3.3285 | -46.0494 | 2024-12-03 05:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 95.2 |
| c49d0886-a5d5-38b6-975f-2685171fcdaf | -5.801 | -46.4719 | 2024-12-03 05:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 167.0 |
| f66d8866-95ea-3f90-ad7a-7bf7b6e896c5 | -3.259 | -53.6388 | 2024-12-03 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 37f1eb51-b791-341e-83ff-b51956a8b919 | -3.2591 | -53.6186 | 2024-12-03 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 188185a4-dd64-38f7-b5f4-190b4df87cdd | -6.1229 | -43.9578 | 2024-12-03 05:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| b6925a00-1751-3cb2-9f02-f199af2d649f | -5.118 | -43.2198 | 2024-12-03 05:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 80a023a7-4dc2-3a56-8dd8-22e3b91d1255 | -5.8197 | -46.4706 | 2024-12-03 05:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| c1c85d1f-d324-39e5-8541-bcab3fa404c5 | -3.259 | -53.659 | 2024-12-03 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| c990c44e-dc57-3c17-92a8-53b932b6f413 | -3.076 | -53.3808 | 2024-12-03 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d8aad29c-536c-346a-9633-ccc500b23ed5 | -3.347 | -46.0486 | 2024-12-03 05:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 176.5 |
| a66fe5ad-efac-3b1b-a8b0-b3fcd90e41de | -3.0944 | -53.3804 | 2024-12-03 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 1d241a21-37a6-3c91-ae50-e630f04615b8 | -3.2774 | -53.6383 | 2024-12-03 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| a1794c75-a531-3949-8e78-dbb03270d79c | -5.8009 | -46.4941 | 2024-12-03 05:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 9789bb0b-304e-3182-89ee-31b161f10c1e | -3.3472 | -46.0264 | 2024-12-03 05:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| aa0bd9e5-5b74-38c6-a5f6-40102af7116c | -1.2713 | -54.55452 | 2024-12-03 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ca5c66-6b6c-3674-8ef7-23ac14a5372f | -3.1778 | -54.33474 | 2024-12-03 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4b3442d-a3c6-3769-a37d-0661ea0213fc | -3.2621 | -53.62553 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ac148c40-b4e9-3eb3-a128-1dde1a2c97b3 | -1.76047 | -52.78987 | 2024-12-03 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 894bebd6-d4cb-35d6-a071-7695a13d60b8 | -3.08762 | -53.37498 | 2024-12-03 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a21fda3a-9b2a-3781-b17c-7bbcba979687 | -1.52296 | -60.32361 | 2024-12-03 05:46:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69d6d44e-3662-3d3b-97aa-bf31e7045f79 | -3.26794 | -53.6322 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1aa4e935-c20a-3927-ac64-f9b1abec0ab4 | -2.3361 | -53.8101 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdb30ba6-6578-3647-9fe2-b828434b3f2d | 1.68588 | -55.99235 | 2024-12-03 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0860dfea-0f9f-3b34-8c7a-e792b34d1a79 | -1.7536 | -52.7888 | 2024-12-03 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f66934c8-cc69-3389-8a96-2b4e78803576 | -3.18341 | -54.34085 | 2024-12-03 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c59e91b-b6e6-3b32-bc02-94f4e519296b | 2.73813 | -60.39425 | 2024-12-03 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 90df4f4d-f2b6-3c7f-8b51-84a5c64f9908 | 2.73425 | -60.39486 | 2024-12-03 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 009cd87b-59dc-3285-9fdf-b028bd86f7a7 | -2.9741 | -53.87468 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7116ea6f-511b-3f5d-95fb-b96d559a6d2e | -2.20221 | -53.77956 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b40ced5-111c-38b1-a050-9fbb94cef2e3 | -2.97409 | -53.87976 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f398bec-17df-3278-b755-50122acd557e | -0.70275 | -63.22088 | 2024-12-03 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a5cae06-c992-382f-8d4f-49560e265e2e | -1.24957 | -54.53829 | 2024-12-03 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b8ce23a-94fc-35e0-a1d6-985f8afacbfc | -0.70335 | -63.21705 | 2024-12-03 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b03320ee-3890-3226-ab03-5835490a89ef | -3.24956 | -53.66486 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e8cf020-7eb7-3cf5-85ab-7341b2f39825 | -3.17706 | -54.33977 | 2024-12-03 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd79c2b6-62fb-3fc9-9ca8-e1117f5df8e5 | 1.52683 | -60.67409 | 2024-12-03 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3dd945b-1da2-3872-9b5e-b7a34a3cc1e9 | 0.8521 | -59.76568 | 2024-12-03 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c2ff671-15fb-3ac7-a9c3-37f174995aeb | -2.75225 | -55.3357 | 2024-12-03 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8979bd6f-28ae-3190-99ae-abf3a5bce0a1 | 1.68478 | -55.98554 | 2024-12-03 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bec52fb-543b-395c-96b9-558f5f4b355e | -0.85816 | -52.71177 | 2024-12-03 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80b070b9-9a4a-3a26-8d26-eb80e3e056c7 | 0.85626 | -59.76503 | 2024-12-03 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2caf954-1deb-3f38-ae16-b39535c61d7c | -3.25123 | -53.6534 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9053536e-b51d-37fc-8086-c4a96dca9321 | -3.30378 | -53.66602 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df2d30fe-840b-3199-a80d-32e9f552a2d9 | -3.07999 | -53.37999 | 2024-12-03 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8f6ea6c1-ff86-347a-b49d-bdbace8e95a6 | 4.06586 | -60.68081 | 2024-12-03 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e2d211c-0b4a-370e-ade4-06aaeff48afd | 1.68053 | -55.99304 | 2024-12-03 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2b11906-e334-338c-aa2f-0166c1d0e329 | -2.97983 | -53.88124 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0f4db38-da2d-358b-b98e-ff3bbed03ceb | 0.9199 | -59.70089 | 2024-12-03 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bcf6db36-c755-38ff-9559-e4a0ab2d9114 | -1.75174 | -52.80129 | 2024-12-03 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ef463d4-0fcb-3a35-af6d-9b7e607069b4 | -1.27815 | -54.55069 | 2024-12-03 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16f34039-1b29-3309-8587-7a056112a758 | 1.68 | -55.98972 | 2024-12-03 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70d5452e-f51e-34ea-a9a8-64c4f38fd007 | -1.08116 | -53.44725 | 2024-12-03 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 017e9ccc-5dde-31fe-a8fd-79756152f762 | -3.2622 | -53.33977 | 2024-12-03 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48745bd6-048b-3ebd-9c0a-75436ea4f6dd | -1.94995 | -53.347 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50100721-8223-3d88-b28e-82fa58d50feb | 0.90945 | -59.44974 | 2024-12-03 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46b993d8-8b96-3695-aac3-0722cd8f2698 | 1.0027 | -59.46865 | 2024-12-03 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbfca998-652e-359d-b0c6-b0fea9cb40e1 | -2.33532 | -53.81546 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc41105b-2dbf-3026-9bb7-7ded8ca98008 | -2.63705 | -54.40589 | 2024-12-03 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d03318d-f404-3a07-93c1-41a5ad5efe04 | -1.0729 | -53.45737 | 2024-12-03 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f94610b9-5d1f-3827-ae00-b06fa2b92915 | 2.72958 | -60.39062 | 2024-12-03 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.7 |
| aeec72f2-4373-39f3-812d-783675a7e074 | -3.26297 | -53.61957 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79c2910e-7b3d-3979-bf0e-718244c9d5a8 | -1.08597 | -53.4594 | 2024-12-03 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cad2cb20-d863-3149-99f4-7bfc908ed204 | -1.07471 | -62.64413 | 2024-12-03 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b39ef1ee-9f3f-33a6-8c7c-ace2faa25082 | -1.7586 | -52.80238 | 2024-12-03 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9ca6e55-1fec-3104-91f5-ba338d85077e | -2.9476 | -60.02085 | 2024-12-03 05:46:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c66c8d99-0876-331b-b1a3-3fdc743539e2 | -1.75454 | -52.78252 | 2024-12-03 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c6d7484-0101-3512-8310-a4b479a12e74 | -1.75188 | -52.80201 | 2024-12-03 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79052d06-bc7f-3018-9e18-d9a03840f9e5 | -2.46162 | -53.62555 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92ebd131-2595-315f-b554-8590d97e141e | 2.42377 | -60.65261 | 2024-12-03 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b53fd86c-f741-3dca-8149-144246517b02 | -1.27744 | -54.55541 | 2024-12-03 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b4eaece-1205-3e12-bc47-93669856ff37 | -3.28733 | -53.70811 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5444e5c4-e5f6-3c6f-a0aa-b8efd6f29930 | -1.95083 | -53.34123 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b10a5b1-1aef-30e6-a522-9c8252063f75 | -2.3295 | -53.81165 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c7a03f7-8d95-3617-a32a-2d5b4b940e0d | -3.26132 | -53.34588 | 2024-12-03 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9733ee9e-4b24-3aee-86f6-9e5aaca09dc2 | -1.08685 | -53.45376 | 2024-12-03 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9cb047d9-db7a-3a38-a7ce-37d42b26097f | 1.1368 | -59.54806 | 2024-12-03 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1712d4e5-ae2a-3d82-9be9-8ab8b5b4d111 | -3.10551 | -53.75841 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 140417cf-b79a-3d28-aaf7-b034b596879f | -2.3352 | -53.81792 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 889ed38f-8ce0-317c-b1eb-59bb494e6146 | -2.61516 | -60.02481 | 2024-12-03 05:46:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8baa3a1e-5d3a-3c10-81a8-ab1691dea02c | 4.06958 | -60.68001 | 2024-12-03 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d628bf6f-9f70-3020-b955-61b67dd0822a | -3.29715 | -53.66488 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7f1f11c9-ef9e-3d17-916c-11ed82facdd5 | -3.25039 | -53.65914 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70313903-3e22-3346-9923-d0e428f629ab | -3.25621 | -53.66587 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1bd51301-429c-3297-b81c-db420bc39e84 | -3.25704 | -53.66016 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b6661699-44eb-372a-96e7-d8390edd366b | -2.98061 | -53.88084 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7248a237-542b-3f89-a043-5d4daa7ddbe7 | 2.73347 | -60.39001 | 2024-12-03 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3439626b-df1e-3ebb-86f2-15511fc1fc50 | -1.0738 | -53.45155 | 2024-12-03 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6786071-f78a-3735-af79-d8e7fc005e95 | -1.25567 | -54.53941 | 2024-12-03 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bb75c0d-e806-3c08-b461-fa0066698206 | -3.01685 | -54.03683 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d677259-cc01-3834-a2da-9801fef2e3f0 | -3.08676 | -53.38082 | 2024-12-03 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e4cba4a2-2147-3081-a040-e4bbbfd84710 | -1.08033 | -53.4526 | 2024-12-03 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c0bc7a9d-132d-34bf-aa9a-374866d44681 | -3.01764 | -54.03149 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ccd7466-01ab-3f72-95f1-56041c46b304 | 2.57808 | -60.69767 | 2024-12-03 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a35a4aa3-41d2-3a49-aed9-8956ba068095 | 2.57426 | -60.69829 | 2024-12-03 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README65.md)
