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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d91837f0-5e52-37f7-bbd0-43f1af136285 | -1.89073 | -54.57235 | 2024-12-22 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9fc0876-5f8b-3803-88b3-b5d6a0f70669 | -2.04341 | -52.10593 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d136bac2-bfa8-3c67-b716-51dbacaef533 | -2.829 | -51.78315 | 2024-12-22 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b20272f5-fd89-39f2-9eb6-890af031e6b1 | -1.29703 | -53.13029 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a12d76a1-4165-3674-934a-c9ae8187d6a5 | -2.84175 | -48.10734 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 887f37b3-a550-3674-9d46-09a558f8981a | -2.42716 | -48.59622 | 2024-12-22 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63361c50-a89e-3d73-a22d-f1bbce173ee2 | -2.81872 | -52.98175 | 2024-12-22 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 711c5490-c5bc-367e-a49b-797a60b19d77 | -4.03484 | -50.05564 | 2024-12-22 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbf0c1c2-d6ee-3724-8354-a6348b283b22 | -2.57554 | -49.4739 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 424f726f-0af1-329c-b7e5-214a85166f0b | -3.76122 | -47.20148 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ca2e55f-47ff-31ad-a6d8-f55d58762f79 | -1.31865 | -52.30502 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a40e5b14-2c00-3650-a233-1dd241ccb499 | -3.78802 | -47.10836 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a1b9f1ef-589b-399c-aa08-b42659c7f726 | -3.09185 | -46.56701 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c16b10e-0855-338c-a843-8b81e83dfd8f | -2.97436 | -48.07452 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9dbcf485-4b08-358c-b57c-3749b41a5683 | -2.56694 | -49.45782 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b32a518-dbc5-335e-9bfa-46a348938073 | -2.24041 | -53.74119 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe3d3ef9-d2d1-334d-94cc-7b0342f0cfde | -4.38708 | -47.20123 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21036b5a-06e3-3ccc-bbfc-379d46db1ba8 | -2.62958 | -48.03338 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c912fbc-304d-3316-a9b9-54e614740117 | 0.00255 | -51.6723 | 2024-12-22 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fea2e38-c238-3509-9e7d-70568801b4e5 | -1.7172 | -52.56785 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1182d6a3-a0ca-36f7-ae42-bc3cef21c152 | -2.7444 | -54.08353 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 531dfebd-03bb-3b89-9c56-679c978de776 | -3.9333 | -46.44263 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4aed19b9-8a75-3722-bf12-533a031f059f | -1.36626 | -53.70378 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c9e0db18-cf27-319a-8196-5b032dd5b392 | -1.71385 | -52.56732 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0366a78-8ee0-39d6-a914-f40b4c58d8f1 | -2.49912 | -49.06254 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ab6c42d-0e77-3fc3-a7d5-a9494f054932 | -1.30983 | -53.48849 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 330ba74f-f6de-3641-9a2d-004dab7a954b | -2.57851 | -49.4546 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb97a169-c609-39bb-9e1e-5a213bcd3cc5 | -4.10097 | -46.81657 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3cb8587-ef36-3dd5-8222-2fbadd55717b | -2.56813 | -45.96077 | 2024-12-22 04:50:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd77559b-1123-39c0-ae83-b9cf63678d31 | -3.0128 | -46.99884 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4ad58b6-e3cb-3e70-8bd2-22b05a2afbc0 | -4.72808 | -43.25636 | 2024-12-22 04:50:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ad69764-e614-3d60-b8b3-f231ca5b97cf | -2.82375 | -52.86334 | 2024-12-22 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d257e2f4-5f97-3608-98d0-594a9cf338b6 | -0.83973 | -53.10783 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 02b41328-7d34-3b08-9f2d-7667101ac4f8 | -2.57032 | -49.46125 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 445a38cb-f6ee-3746-b90d-b52136903aa7 | -2.5075 | -49.0556 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7cd4c79-6009-3f50-9789-baf38f492b4d | -2.56556 | -45.96177 | 2024-12-22 04:50:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e838798-6189-3a34-bf9d-0a50856a6ac9 | -2.05613 | -54.37279 | 2024-12-22 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc27ff8a-8fc7-3d12-a878-231c27d9d14a | 0.0053 | -51.19511 | 2024-12-22 04:50:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8a244e2-7eb0-3bdc-9a2e-58ec7fd8c9fe | -4.00275 | -46.92337 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cf19d1f-0289-3412-b06d-ac1a2dbba1c5 | -3.1118 | -48.28443 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2e11970-08fa-36a9-bc5f-ecac2c026acd | -1.32588 | -52.30258 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9196c2fe-2312-3f85-98b7-92694859d90f | -1.15028 | -53.5975 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b34518a-5a97-3b99-93bd-da4ae79978fc | -2.56222 | -49.46501 | 2024-12-22 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc428646-3ffb-3725-9260-6dfb16ef4b93 | -2.57204 | -49.47336 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a4bbeac-4a8a-3918-bf29-a34c682e3d03 | -1.56265 | -46.77433 | 2024-12-22 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3efd09e1-875f-3e6c-a3c8-b9cd89c7e31f | -1.70943 | -52.59539 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfc0f55a-58b0-3e39-93c8-90ce2e97bae7 | -1.36525 | -53.6879 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9ed64ee-9d05-3f61-8ff1-f2e3c367e327 | -1.95362 | -53.56804 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a93548f-812e-3782-a453-ff919682e40d | -2.04067 | -52.10544 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f06e8b62-976d-3f80-ad55-576290713959 | -4.10455 | -46.82096 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e02b422-e596-36b6-b326-5c473f3f300a | 1.06364 | -59.4076 | 2024-12-22 04:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81711abe-aeec-311c-81f7-3b94abfdb5f2 | -4.06436 | -47.08731 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0563912-cbd1-3cd8-b636-88486b533f45 | -2.58082 | -49.46287 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8f21028-c1c1-3118-ba33-2c9a82836a2c | -2.3796 | -47.4285 | 2024-12-22 04:50:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bc85d09-d8bf-3b95-9d22-907c9e659c1d | -2.57614 | -49.47004 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4779d2ca-9fb1-3068-b17a-818d12445328 | -4.07821 | -46.79849 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39f4c6af-3318-3dae-920f-1e6b11d346ff | -2.97743 | -48.07962 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f6eeb83-2c29-33a0-843e-74345355c27a | -2.50717 | -48.05387 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d597a225-5001-3ddb-b86e-5139212ac953 | -3.60382 | -50.63232 | 2024-12-22 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40fb1747-f584-3471-a299-8b2654352f8a | -2.34084 | -45.73769 | 2024-12-22 04:50:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14004d4c-c833-3036-ae6d-ef8fb9436a27 | -3.81007 | -46.71883 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa6b282a-7c90-3493-bfc7-0c7db98ab39b | -2.06104 | -52.05909 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f65e6b1-c198-35bd-aafe-5bee332ee402 | -1.70306 | -52.4187 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f68d4747-f7e9-3f1b-9baa-d61256cec09c | -2.88681 | -51.79964 | 2024-12-22 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdfa1f5c-a946-335c-a689-3980cc361860 | -4.03408 | -47.03885 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8225984-13c6-3f85-b7e0-3e8bbede563a | -3.91348 | -46.99245 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f15736fa-2382-3937-9916-bd5470531e59 | -2.57441 | -49.45792 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb9d2401-d774-3ba0-b4bc-70bea5424458 | -3.74522 | -51.52896 | 2024-12-22 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5eff034c-4df2-36e4-b73d-78e0f7d672d8 | -3.55131 | -51.08002 | 2024-12-22 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9a99fb8-3576-371e-bf60-54451795a07a | -4.81932 | -44.41596 | 2024-12-22 04:50:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6a8ad6cd-2296-3f38-a77f-016c0fc1c5fe | -3.75424 | -47.19331 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceba9a68-0b91-344d-9cb5-72609b9b2408 | -2.44828 | -51.79103 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09dfe0eb-38e3-329f-8afd-2d5f8b7d9443 | -1.20745 | -53.92543 | 2024-12-22 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25329421-6863-3f5d-bb63-c7b3d4a696b9 | -4.10039 | -46.8204 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a2ff2e5-9e79-37b8-9b6d-2ea93853b54f | -0.78518 | -48.77367 | 2024-12-22 04:50:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fd47f36-0039-3c71-ab28-474b3258c4ab | -2.379 | -47.66271 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d853692-058f-3c37-a245-e63c20da2179 | -3.37741 | -52.806 | 2024-12-22 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd708396-1ec5-3375-ac9b-2860d30abae7 | -2.8057 | -46.75364 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36deb2d7-6905-3c1f-900e-6d4c060d0045 | -3.92618 | -46.90097 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e5f1bcf-5f95-3ee1-b8c1-92797d8fac43 | -2.58568 | -47.54351 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3be82c6d-5ad7-3517-9c06-af366cc36531 | -1.25978 | -53.52301 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8dee5b2-e5df-3d78-905b-3f1fe518f963 | -3.3661 | -49.16628 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54a44a0f-43ff-3da3-aa13-e0e64d8e1b4a | -2.56283 | -49.46115 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76965dbc-6abb-3c3d-9c67-e423150dbf0c | -4.00276 | -46.55517 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69bdc2c6-3484-38c8-9d97-6237e67c82fa | -3.91281 | -46.99187 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e4757c8-31bf-367a-8b2e-1d8b5efc83b5 | -1.70663 | -52.59136 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d95b2a1d-9365-3767-9388-fbbdb49b5b1c | -3.90362 | -47.00218 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5414d94d-e24d-350b-a089-9156d411188d | -2.84551 | -48.10791 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff8a02aa-3b88-3c19-a4c3-ca22834b3e9e | -2.50135 | -48.06673 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7efb80cf-71d7-3a93-ae13-2b561cfa334d | -1.98052 | -54.26035 | 2024-12-22 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61091a3e-bc1b-3bd8-9d53-2552e917659d | -1.27648 | -52.06012 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ab723b9-14bd-31df-a21a-85f25a5eddac | -3.17835 | -45.97608 | 2024-12-22 04:50:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffc18fbd-03da-32cf-bd24-0151415e186c | -1.71613 | -52.59644 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 575df228-5df7-3ffe-aeb4-92c82b20b81b | -1.18293 | -52.5459 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 585760fd-7887-366e-ae80-98151cc9d063 | -1.27926 | -52.06411 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c1b6141-cdf7-36d4-a959-2c6645b6dafb | -4.32737 | -47.77742 | 2024-12-22 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7696e5f-e57f-3215-a75d-c72a5e91f249 | -3.72802 | -48.97675 | 2024-12-22 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaa8466a-10bc-3ebf-87ea-45b31afa488d | -2.75727 | -45.56185 | 2024-12-22 04:50:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8dd801b4-cdc6-3cc9-8673-e613dcb8c951 | -2.72331 | -51.63582 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6d4629f-8f07-3c15-9193-bd1c0b53f6ed | -3.91656 | -46.35023 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
