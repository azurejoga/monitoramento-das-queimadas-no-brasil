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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc89d0c4-31e2-337b-8f99-b30d7c87e14b | -5.58378 | -46.38752 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71ee3f84-3d4a-31ec-9fd0-015a3a1ea00a | -5.49267 | -46.35867 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11411767-61f5-390b-99aa-4e8e6ca7d99a | -5.49134 | -46.36104 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c60ed53d-f44c-327b-a204-0ad4ae17e99d | -7.53679 | -45.84079 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ad4d95c-0eeb-3d64-8174-83fb808fabc3 | -5.48878 | -46.35813 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f7e02e6-8082-3a38-a96e-525bd0d7ce67 | -5.45807 | -45.88145 | 2024-10-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 181df6b7-3a18-37ea-9bb2-f754f06971e5 | -5.35636 | -46.24868 | 2024-10-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e118a7c0-dc72-3ca8-a5b1-533b63068187 | -5.20715 | -45.33269 | 2024-10-26 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c24dd96d-ef4b-3668-acd4-3e4f73689987 | -5.20534 | -45.33236 | 2024-10-26 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2a6367b1-e124-30d3-90b0-90a622b29370 | -5.20299 | -45.33218 | 2024-10-26 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3196be3d-7a94-3276-b214-9b97a3813edb | -5.17939 | -46.19865 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28d6497b-7d0c-3a3c-b315-f26c8f29bba0 | -5.17933 | -46.19981 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e91fe0d2-4a9b-3da2-80af-127699365acf | -5.11636 | -46.00754 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14c2eea2-8c33-32f3-86b8-f7f5ab86b3ca | -5.11591 | -46.00462 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1091eda-5258-33b4-9da4-7a51795d544d | -7.5632 | -46.79537 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 66186229-0dc9-3a8e-bca9-0bcf9b199ce6 | -7.5593 | -46.79481 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d0bd03f-d81b-3a77-8cba-5b3a2274ef07 | -7.55857 | -46.79975 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d371914a-c455-32e0-8aa1-218d7f5b23b1 | -7.5554 | -46.79425 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 625aa17a-6612-36d1-9d94-cca1faaff267 | -7.47505 | -46.7149 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2fef8ef-3e2f-3ed0-a3ca-c36a1bb46323 | -7.47431 | -46.71985 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4077cb05-4f6f-3b31-8b9c-82274bdca50b | -7.44822 | -46.84159 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd570646-408d-3d99-a22b-dbfcc45ee0a2 | -7.26938 | -46.75447 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 854248f8-dc71-36ca-9195-8a5a664f7668 | -7.26891 | -46.75235 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cbf17d2-197a-3e48-aa0c-b9fc0b3cced6 | -7.03281 | -46.69761 | 2024-10-26 04:44:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d8144b8-76d4-32e4-afbb-f234ec3dde76 | -7.03208 | -46.70254 | 2024-10-26 04:44:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1389ee4e-8a48-35e1-b088-282ed9aa9b42 | -7.71544 | -45.70337 | 2024-10-26 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad8cf01b-cd0d-3f23-bbd1-61cf7a55d405 | -7.71489 | -45.70714 | 2024-10-26 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03690bc3-4a39-374e-b1e6-b35175185940 | -7.71124 | -45.7028 | 2024-10-26 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f0baec7-8da2-3a82-b3a5-737815f0b7df | -7.54147 | -45.83763 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 638d2ec2-a1bd-36bc-889c-5fce099eba34 | -7.54093 | -45.84139 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 54cba7f6-0737-3c61-ae9a-8bddea7d6378 | -7.53986 | -45.84891 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90d4bb07-62c6-3914-9af4-a32e549c8b04 | -7.53732 | -45.83704 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7aae7bf-c833-3cc9-9f60-65b09201ed24 | -7.53518 | -45.8521 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2541a9d2-e3cf-3c1e-b475-5a775283e6e8 | -7.47707 | -46.4833 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c27162cb-9c4f-38be-a652-f48ae2a28895 | -7.41064 | -45.57325 | 2024-10-26 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a4e31c8-cc53-3d7a-8f13-108a1d94fe95 | -7.40644 | -45.57263 | 2024-10-26 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d745ecc-0629-3b26-b76b-72e4479bf4a4 | -7.27202 | -46.06634 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae6d13e4-d508-361d-9ac6-c495ce9d84de | -7.26084 | -46.05734 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97cd48f0-5fb8-34b5-9a39-8eb2c344794a | -7.26058 | -46.05802 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 565e46b8-374c-3432-b434-b051badb604a | -7.25751 | -46.33914 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3bfcf42-7c43-3801-9fa5-27ae970b541c | -7.17478 | -46.33218 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b5db347-e0d6-3a88-ac37-277078663d42 | -7.17427 | -46.33562 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19ab04cd-d102-3981-93ac-1a190cf6a88e | -7.17133 | -46.32793 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3afd686-52ac-3a24-9833-0054fbbafb96 | -7.17082 | -46.3314 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3845acfd-0fa4-3e00-8a23-9b29c66b1289 | -7.16119 | -46.17196 | 2024-10-26 04:44:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de7677f7-a8da-3382-8fa6-4ea8c168579b | -7.14063 | -45.44061 | 2024-10-26 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 388d18e3-81f5-3c4f-a694-1d5e968925dd | -7.14051 | -45.44106 | 2024-10-26 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4384c137-73f8-316b-b79e-b95026be3eaf | -7.12249 | -46.46829 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab166a23-7890-3570-9b82-6407f8dc4425 | -7.12057 | -46.3693 | 2024-10-26 04:44:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eb41a4dd-3be3-333a-ad88-064fec8ea8ac | -7.07478 | -45.50734 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00e11cca-4208-35d5-b421-e03f21f0573b | -6.96781 | -46.10049 | 2024-10-26 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 814f01ac-8c45-31fa-a82d-32982e79aa05 | -6.92919 | -45.62089 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 866985b7-249d-393d-8772-dd5b836da096 | -6.92503 | -45.62023 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 270aa81b-eea3-3229-9989-76993b239b1e | -6.86884 | -45.8946 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98dcade6-c52e-3d4c-acd3-579d5a3b2993 | -6.85397 | -45.88178 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ab7352d-ca59-3411-9aed-05ed397954d4 | -6.85382 | -45.88573 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be15b1df-f4f7-30e9-8887-74ad667d4575 | -6.85341 | -45.88577 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| faececf6-d92a-389f-ba97-ebc41da5f27a | -6.85032 | -45.88121 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a8ac8b7b-747a-3d71-930e-67a6d61297ff | -6.84972 | -45.88522 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 77005fe8-3443-362c-92ca-1b616cccd490 | -6.84915 | -45.88902 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0dbab10b-2577-3d0e-9089-4eceda4101c9 | -6.84863 | -45.89254 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec4f503a-27b3-37d8-8296-1424163e67b2 | -6.84506 | -45.88844 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| df86029e-b5ed-3f4c-8221-024d9526420d | -6.84454 | -45.89192 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85384516-4a37-30cb-ba6e-94bd345f1317 | -6.8307 | -46.21701 | 2024-10-26 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c1235bf-11d2-33b7-b8f2-6da7f17fca34 | -6.80183 | -46.4716 | 2024-10-26 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aee1e780-07af-3c5e-af61-8c679809773e | -6.80037 | -46.48161 | 2024-10-26 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdaebbc7-078f-34d6-88ac-aa08f1c778cf | -6.50394 | -46.5881 | 2024-10-26 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5661c69a-6fc8-32ad-b6e6-2534ce33f710 | -7.89976 | -46.6878 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a31d4f5-58dd-37b7-9549-0b7fa2de869b | -7.89656 | -46.68216 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6df98709-1204-3eca-92bf-d421b658477e | -7.89581 | -46.68725 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 813c99bd-3bd5-3378-aa30-76c27134a491 | -7.89262 | -46.68159 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d90587bf-d34f-3199-9308-2a71a5a060ba | -8.5233 | -45.63489 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a459bae0-536e-30be-96ad-aa4c00214d5a | -8.52049 | -45.6551 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea2503f5-ef33-3dab-9886-d38b560bce08 | -8.51848 | -45.63829 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba65af87-5039-33fb-94ee-d7e7ba07aa1d | -8.51626 | -45.65427 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61199069-62da-3c5d-984c-966c602a91af | -8.50173 | -45.64053 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38c14b0e-8936-351a-9928-833b112b036d | -8.49804 | -45.63593 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f86f3c3b-3310-32bc-8ad2-1048efd21167 | -8.49749 | -45.63976 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac0d2fc9-a759-3c99-831a-4007f4f5a1f6 | -9.30565 | -46.53852 | 2024-10-26 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6c76dd0-6198-3def-82f5-f5351feee2a1 | -8.74377 | -46.46198 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d06367b-b25e-3537-a306-eaca4fbb1a49 | -8.74327 | -46.4655 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45f06c3c-ca9e-3908-8528-8fabddeb8ba5 | -8.74278 | -46.46901 | 2024-10-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e748a38-0252-3e00-ae53-9d92266bafd0 | -4.91517 | -47.72658 | 2024-10-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 307fa401-f33d-349e-8c9e-d1fe9a980843 | -4.87426 | -46.8825 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bad41144-305f-3a54-9b17-4c508ebec4ce | -4.87346 | -46.87986 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c87ee898-b9a5-39f4-a26e-036ba95e549f | -4.87276 | -46.88437 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95038fe6-9525-39e1-be3b-874209fff279 | -4.87053 | -46.88186 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bab5df9-924e-3d04-8441-0313ca32a699 | -4.38932 | -47.59352 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f96cee7-86d7-3395-9396-3d20a1081d93 | -4.36614 | -47.48074 | 2024-10-26 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47bc1889-ebac-31e3-9fe3-b2cd86708504 | -4.36551 | -47.48486 | 2024-10-26 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b4e2876-0fa7-31ea-bc95-1cc38c0a521d | -4.24477 | -46.99801 | 2024-10-26 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d2b3e6e-3279-3673-9690-8e077727e77f | -4.77596 | -46.50584 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a77f799-0dfd-3b5a-a09c-c6e83e0d6504 | -4.60708 | -46.46803 | 2024-10-26 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 179af09e-d86e-3efb-a5bf-52b79023c316 | -4.60369 | -46.47041 | 2024-10-26 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8026e663-dad4-357d-9eea-327032b7c44c | -4.54191 | -46.46602 | 2024-10-26 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6c5a84c-3b7f-3b3e-b988-dd8f9e1bdfc1 | -6.51817 | -47.03555 | 2024-10-26 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ff6eeee-0f5f-3bdf-89f2-0364430f0577 | -6.51438 | -47.035 | 2024-10-26 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec075b1f-4077-3555-8aa1-e13d083c8331 | -6.46409 | -46.72277 | 2024-10-26 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b6f3375-8c84-3f66-a5fb-a1501db74776 | -6.3817 | -47.37627 | 2024-10-26 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37e5158d-5b2d-34df-87f8-4d5f7d57397d | -6.29304 | -47.34689 | 2024-10-26 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README77.md)
