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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 677e42df-c813-3669-8cab-4a4f40de7936 | -6.92681 | -44.72514 | 2025-09-03 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b854995-5a47-359b-8a2f-8aff14ce5812 | -6.09943 | -43.2878 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5d49a8d5-18d4-30c5-9501-3fd237503bb8 | -5.26247 | -50.76469 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa50f28c-0ffa-3c7e-992d-5083a2c57a35 | -5.88236 | -43.01599 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 686b3c5c-2fad-358b-9024-d461ae5c17f7 | -7.62864 | -46.54614 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 686add67-ae0a-377d-9495-daf2fe0a95cd | -7.50273 | -45.35107 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f627ec2-f01d-3220-99c3-9075bde33cce | -8.01493 | -44.1132 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f2e7384d-c6f3-3a71-906e-6a0910946910 | -6.46201 | -44.67159 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95af13f9-9eee-3992-8ca7-4830d71135f7 | -6.57901 | -44.57 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4db840f5-0c3d-30f2-9b98-5cc5eae9138f | -6.05205 | -43.42411 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 072ec792-e9b6-3ba5-bee6-f5573054e140 | -7.18276 | -39.29555 | 2025-09-03 03:53:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| acd51e25-1bad-32a4-9aa7-ea664d95c053 | -7.50114 | -45.34444 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95d97514-bbd1-3714-a251-59edf80a1fb1 | -6.21889 | -43.40158 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02f65406-fff3-35eb-bb85-ff391dce572e | -5.61125 | -45.01512 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bce3eb2f-c41b-3263-95d7-e61513cbb4af | -7.92275 | -46.43264 | 2025-09-03 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e12a536-3a5a-3906-bfb7-97473401c65e | -5.89357 | -43.34691 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f1befb8-3ad8-384b-9aa7-88fe46aa7138 | -7.91316 | -46.43075 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe3fbcab-829f-3cb3-a3a5-35eb48db9612 | -6.27391 | -44.50367 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98d5cf98-cdf9-355d-99bc-75d440f3011e | -6.26625 | -43.51596 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8949a4bc-00bc-3156-8be1-15f24def86c0 | -6.49953 | -44.09573 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99f81930-2ba4-3d91-90c2-7a13b92d6276 | -6.78495 | -44.47969 | 2025-09-03 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a503224-a82e-384c-a4b0-f3eb9d4cf004 | -6.25813 | -43.5146 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b0bddaa-e549-3468-a915-dd964e22aad7 | -8.05792 | -45.36681 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bf3d1117-7457-36d8-a732-c9598f4efbe3 | -7.90368 | -46.45637 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 26d863d3-7ab5-3acb-8d18-eed283699fb4 | -6.9693 | -44.37001 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03258e72-8e4a-3ce1-a4bb-ba6eef82f024 | -6.40891 | -43.75935 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9eac70af-30ed-3132-8c0a-c0785814c49a | -6.46393 | -45.40031 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5a157f41-ad23-3cbd-b08f-44fb6f1b51c9 | -6.19755 | -43.35116 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b67701fe-26b3-3b10-9d67-e1bc8767317f | -6.47235 | -45.40632 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6d7d0bf-a1d8-3b6a-acd6-3453fc113008 | -5.8849 | -43.00077 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d83f66de-e8e7-3ed8-bd40-664e77f17432 | -6.26189 | -43.29384 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b47031a4-620b-3e9b-81eb-3dd956576c31 | -8.45942 | -45.06354 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 195a7e32-e4b0-37f0-b0a9-474832107b99 | -7.01737 | -44.36623 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44b31629-64bd-3150-a03a-00e4cb73318f | -5.95051 | -43.72768 | 2025-09-03 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0058da50-4e12-379e-8c71-57859ef6a61e | -7.11583 | -44.75671 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f00e7e3f-aa71-3432-9744-fc71046f3c4c | -8.54437 | -47.4783 | 2025-09-03 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2015db3c-bb5f-3ba4-aeea-7498a20f33c5 | -7.66682 | -42.71329 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 191ebc02-bddf-30b4-9028-36dee31bf0a2 | -6.84759 | -45.54931 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa65c6e4-56ac-31e1-8b74-a9a312e12545 | -6.75339 | -45.91517 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e4dbedec-ff4f-3594-baec-4336a9f18169 | -6.51398 | -43.5091 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ac06aa6-755e-37c2-bdfd-70bb8e71addf | -6.16305 | -46.60592 | 2025-09-03 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 115d6846-b978-3946-a706-754237aab8ec | -6.47532 | -45.41665 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3057f88c-c1f6-3c11-98be-b1f9380989a7 | -7.72048 | -48.74497 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83b39148-2219-30e2-af7f-5ffcd6b46791 | -7.00146 | -43.2475 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3d376bf8-9822-37cc-b6df-9608074ae62c | -5.93685 | -43.03065 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 84e01734-9bf5-3605-8a91-a4a40cd95500 | -6.9897 | -43.10352 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5fed35ed-26fb-33c7-894e-666bca686f3d | -5.96789 | -44.28753 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33ddbac4-f10a-318a-888c-1a787e4c4d0b | -6.78065 | -44.47905 | 2025-09-03 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3faafa66-d1ed-3646-a573-722d8b8728fd | -5.96358 | -44.28689 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 171b8deb-c672-31f7-a1e0-20e9646f8354 | -8.46303 | -45.06853 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 263b95c9-9485-3303-8959-ea8b643467d5 | -7.48188 | -44.83255 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ef9e94d-ad47-366c-ba51-4d331464565d | -7.9874 | -48.43077 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 874b0be8-1fc1-3863-8e48-360f85313701 | -7.43564 | -46.01268 | 2025-09-03 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70d530f3-2a69-311a-b035-b01137436f4e | -5.86067 | -42.97581 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6fb99255-829a-33f3-a27f-661457a47d44 | -6.69422 | -44.17631 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18e32ac1-80d0-3c97-87bb-c2e21f28e4d2 | -6.26438 | -42.63093 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ef56c2a-af5f-35d1-ba0f-13fd653986ab | -6.97315 | -43.27709 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cca01a2a-53bf-3aa4-9f38-cc042a4787e4 | -8.3551 | -48.31208 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50ec6318-6708-33a9-ba53-bcd12474c5c0 | -6.54427 | -44.11401 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef0d0d39-1248-3282-989c-12fba19a78f3 | -7.11221 | -44.75169 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 746f2d23-ecb0-3d09-a87d-ade787ac8eed | -6.72765 | -42.25145 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 15c70375-2f55-3e26-ade7-e4b60f8e57b9 | -8.05873 | -45.36219 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 73a509ae-9185-322f-a7ee-d2ddd5a45fbf | -7.91222 | -46.43613 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b334daee-387a-3525-a5f8-d22ebd61096e | -7.48685 | -44.80984 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c17a6a9f-4875-336f-a213-085f1027aea5 | -6.09428 | -43.29403 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dd68d7e0-01fc-33e5-a67f-b43a9427ff9b | -6.7915 | -44.08845 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cd0aba9-157d-3331-a6b7-3088e4044211 | -8.87999 | -45.83482 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5073a34-5f9a-3098-87d3-70eeaa3b2408 | -7.70361 | -48.74185 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 995e47cc-4203-35d4-8a51-9612c3067f2c | -9.16686 | -45.20815 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fa22dfa-02a1-354c-ac07-95b7a01c0503 | -5.80474 | -43.23397 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7f966d7-8aa1-3d1f-9ef5-b46b2ab9c606 | -5.80934 | -43.23118 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a9c10362-49b0-378f-b05c-03b1eebe66f0 | -7.93701 | -46.54171 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8fcd1b31-f003-3003-81ab-a682d430ae5f | -7.93895 | -46.53097 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b473243-6690-3a7f-8e6e-d93cbc998c45 | -6.2659 | -43.29446 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c8f9d80-b11f-3b30-9f6d-f3251eae26d4 | -7.25807 | -43.84692 | 2025-09-03 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 070ad22b-fc7b-3d84-b93f-26b78b719e45 | -6.84844 | -45.54446 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d813242-610b-3dc4-9b15-ca0cbde33ddd | -5.93933 | -43.03338 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aee49c8b-a71f-33e3-950f-93167245f84e | -7.90165 | -46.43979 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d11373da-a983-3508-a2d4-cbabc1c32f4e | -7.01561 | -44.35434 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96eaf841-6a8d-3bc8-a1c5-a0e59f5f9167 | -6.1169 | -44.12638 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cf1101f-5d8e-379a-a747-38fdf18c6ae3 | -6.5783 | -44.57415 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 82ebe318-5c58-3441-983e-6bd6eda95ae4 | -6.17461 | -43.31511 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2ed41af0-9d7b-37af-86a0-701d40523cb0 | -7.70134 | -48.75428 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 443152e6-adcf-3b0d-b338-a530d987ab98 | -6.73358 | -42.26181 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8073d10a-447a-378e-bd6a-467ed4a3c3c8 | -5.88716 | -43.01155 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| de660c5f-89d3-3f73-bf15-2c98c17c253f | -6.22694 | -43.40304 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cf45713-2c71-34b1-8b1d-10bdc8c250c5 | -5.77799 | -45.28548 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7909811-6c29-3bb3-8a4a-658125baa8f0 | -6.27075 | -43.58997 | 2025-09-03 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0376fdb6-c981-385f-abf8-50ae47117ba9 | -6.49536 | -44.09482 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d4c5dfc-7a32-3121-98dc-f4487d98a806 | -6.29837 | -43.59773 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24baf973-89de-3d7d-b743-a588208629b3 | -8.02026 | -44.10664 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 105e0f14-800c-36ad-b414-9443156abe31 | -6.70267 | -44.17759 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4f93c4ab-2c8a-32e5-8f7b-5b82b6651b25 | -6.51457 | -43.5057 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d6bfafd-a667-3f97-8572-edd7e3e47834 | -6.72683 | -42.27182 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c18ca549-194c-368c-8f7f-9576df9c2cc3 | -6.24053 | -42.63194 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 775123c1-db66-33a9-91bc-8a5ef8ca6fee | -7.80032 | -45.45744 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2b3cc5a3-0294-332b-8133-8d87de6aa608 | -6.25123 | -42.63875 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 76e4a37c-d430-364b-bd6a-dc1b0032cdff | -7.01626 | -44.35039 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29831eae-7079-335b-952f-5c481cd21b3e | -7.7058 | -48.72987 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f60b9843-8ad1-31d4-b2e1-3820ba0b75be | -6.50289 | -43.57338 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README33.md)
