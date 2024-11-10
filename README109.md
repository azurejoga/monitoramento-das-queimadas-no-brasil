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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 304e8ea5-8b9a-3707-b858-488ccfd787fe | -2.41053 | -50.55773 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 496138eb-6c9e-319b-af1b-f9c8562f0e9b | -3.11799 | -50.15239 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b04f70a7-987e-3fc2-9b80-a0e27ca36b72 | -2.59849 | -48.19487 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e49bbb84-6bf8-3763-98dc-566987b7a826 | -3.789 | -47.73782 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dbded82-d4e2-3545-975d-643bf97069fe | -2.87323 | -51.4754 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 1abdebd1-277f-3fb8-847b-2ac59b229ea7 | -2.66299 | -49.88948 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9713646c-bc29-3b40-8e0c-ded30d202461 | -2.19968 | -50.23547 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e545440-5fb4-3963-a966-c4072a83ed59 | -2.7706 | -49.35882 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bc32f7dc-5d29-3093-bd95-19b006fb7159 | -2.65124 | -51.87872 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9d20fc8d-1019-3b37-9e70-bf0ddae2dee2 | -5.69381 | -47.01751 | 2024-11-10 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b66bf88b-117e-386e-b185-c5aa56fd77e7 | -4.71075 | -43.79489 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5dc2997-0a1f-3c35-8677-f25ad065b40b | -3.69244 | -51.16307 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b9ab2c2-4c0b-3565-a538-6ed42bab13e2 | -1.57208 | -54.63986 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 990be374-7c56-3e88-9631-b1345a7428d6 | -4.10826 | -48.27777 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a70550e-a1d1-3c85-a85d-7f2956578c41 | -2.8873 | -50.41665 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c1786db-75b4-33e8-90d8-0f9f2d68afb8 | -4.23694 | -48.01567 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e4cb8fd-50f9-3356-93b0-7b2eefb637ca | -3.96486 | -48.17363 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c61dbb48-c0d2-3ef3-ab27-9bc46a16952b | -3.09089 | -50.95358 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f6fd47f-b13a-3a50-a79c-89f3dc0bb218 | -2.25917 | -50.60415 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 58e3ba12-6145-3087-92b9-82ad7577f3d8 | -4.21377 | -48.68059 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf5aac42-721a-37f7-aede-0089ee2f52fa | -3.35831 | -50.13385 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85cdf176-505b-3b41-86b4-5950aa750251 | -3.3067 | -50.08175 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6008d7ac-b8ef-33a9-98ca-6a59d28c8e7a | -2.81393 | -52.96438 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9fb922bb-91ab-3d67-921f-2313a000942f | -2.30963 | -50.48831 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26bf650d-0b27-3e88-8246-11174f55dc08 | -3.11775 | -45.96168 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6ded8e6-0c46-374d-b0d3-dfc62405c2b4 | -2.5681 | -50.68258 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1af4c3d4-c5b4-3c3c-aec1-1fa6f3508feb | -2.63595 | -49.88523 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e562ade-4d4d-3c70-80a1-46340e08df61 | -4.38193 | -48.57985 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3df677d-0905-36c3-b50f-67a31b72dc01 | -3.23599 | -45.38442 | 2024-11-10 04:38:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d33e0d0c-0701-37c9-a26e-d9028867c10a | -2.61212 | -48.34151 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f56ac36b-b0c9-3f65-a18e-d33c8d41b90f | -2.91005 | -49.24162 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 824a2e21-4f53-334d-8ad1-d9fa9485760c | -3.12463 | -45.23468 | 2024-11-10 04:38:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9c098e4-959b-34f6-8d87-9eb0f8262933 | -3.17912 | -50.57924 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da776b75-0b1d-3e17-b97a-67551c834e6c | -5.13789 | -48.24488 | 2024-11-10 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b63a2471-2519-3972-bb76-cbd3a1bda398 | -3.61933 | -55.47874 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d324934-34da-3bd9-b6e9-ed883aff34c0 | -2.89069 | -49.38515 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 282bfffb-c77f-3b3c-96d4-cc32b7b8a5f9 | -4.10277 | -45.70575 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33f8f00f-9a0b-30e4-8024-4217a8bd442a | -5.55574 | -46.34258 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3707bb93-84c2-3fc2-aa31-9a0efe463072 | -2.65841 | -48.47932 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acaed65d-7558-32b9-bb73-328aba8d5278 | -5.32201 | -45.05585 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ab9b8f2d-0396-3117-96b2-e853516cc9aa | -3.29454 | -43.54209 | 2024-11-10 04:38:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d587599-0100-327c-a474-0205164f35a9 | -2.61257 | -51.7463 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b6bc51a-f4e9-3e94-84e1-575b8cfd003e | -3.02791 | -51.09965 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6167036-8fc8-3440-9ac3-77e0d6a202e7 | -4.10592 | -49.08802 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77c8ed1a-c882-3e74-a535-3b29617b394d | -3.73354 | -44.535 | 2024-11-10 04:38:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be3e3c00-ef40-3614-8a93-19d941de34e5 | -3.53405 | -49.26082 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27bcdf5c-6950-382d-a8ad-f4aee12b2257 | -3.88423 | -49.9481 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43b7aae8-5865-3d72-826d-c41dbb2f4e29 | -4.50456 | -45.46758 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f82e728a-c36f-3acc-bc5b-c3474db0685e | -3.26564 | -46.31348 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cad55fb4-70d7-30ba-a55b-6c4729f4950f | -2.85578 | -48.45007 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1026b129-c85f-336a-b67c-610a7a85397b | -4.48711 | -45.91983 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 986da53f-5c5f-315d-a98b-daf8e2b39a2f | -2.86989 | -47.91077 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60ec8ef5-9417-3717-9550-89625b2f780f | -3.1208 | -50.15655 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6897abc7-f89a-34f8-8766-5942ee55b202 | -4.31125 | -48.61836 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e979ecd1-19c6-36b9-a3be-0795b16bbf1c | -3.46086 | -50.1903 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3e4d85c-bc2f-347f-9513-4908dfa1dfcb | -3.02789 | -49.55025 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51945623-8789-325b-9a8c-cd752194271f | -2.85294 | -51.29086 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a32119bc-1c12-3a21-9127-fed02c6d0146 | -2.81494 | -51.81107 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 989a3adf-5dac-3fbe-94a9-19f391ad18ee | -3.10329 | -49.41085 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 996ca9bb-d3fb-3760-be8d-dd30021d4019 | -3.78579 | -50.0388 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f95d0991-dca2-35c5-8bf0-f75cbe6e3d9b | -3.59858 | -47.34216 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0c124841-6b29-3b28-a21e-077ccee7c30c | -2.81144 | -52.54016 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 776bc832-3e19-30a6-83b8-d1ec37b37152 | -2.23425 | -53.78434 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab880dea-ade2-3e00-8f8e-5647d03d608b | -4.79489 | -48.47039 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 144281f7-cccc-3959-a650-8bea4171c140 | -4.40683 | -50.98309 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4cd1116-a2b6-3cf3-992f-ad3c4b04ccda | -2.65056 | -51.883 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 801a44ba-d1cf-3913-8c13-b6d4119e7d10 | -2.2043 | -51.40266 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd13d139-4899-3992-bd07-8a0be808db7f | -2.91425 | -51.67991 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec6183e5-e08b-3930-ab04-ef3e111ed906 | -3.95044 | -49.00008 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f7f015ee-b2b6-3704-8030-8d0b6e554ed4 | -3.04518 | -49.54934 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8427e557-fee4-30f1-91bd-f8d731cd314a | -3.13192 | -50.43938 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7c0852fe-a897-349e-92a3-796f52a84a7a | -3.95931 | -49.00854 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dcffc899-eae8-32a4-b12e-e14dee7bb7ec | -2.87592 | -49.11891 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8485b02-f34d-3344-9ad4-57ae04095ef5 | -2.6641 | -51.68131 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90c1c845-a3f6-3bd0-a891-703ec534ddad | -4.26899 | -46.91324 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 871d70c6-ce45-390e-be54-3b24832f9dad | -2.92642 | -49.50566 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73daf27f-1202-3577-8c2a-43924ee66822 | -3.02665 | -48.03141 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 262551a6-0e5f-328b-ae4e-d7cd0db6dbdc | -3.45036 | -53.84081 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 357244b6-339b-32ad-a30b-2cec2e1ca3f3 | -3.15945 | -51.13445 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77446bd2-ce99-313f-84aa-afd2b29d13d9 | -2.60219 | -48.32261 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caa1aad1-163c-35e1-999b-b12616b3cd35 | -4.49365 | -48.49446 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9a6d984-2e03-3de6-b1b5-ca2592664e31 | -3.97695 | -48.13992 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1f2d271-5b10-30f5-bb9a-efe545e57796 | -5.2435 | -46.26656 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 595afaaf-8539-3c2f-a263-bba3d3a9552b | -2.45954 | -49.78468 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31f576fe-1e95-3c24-9d3f-56c851583574 | -3.91544 | -47.95188 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f6dca50-246f-3968-8dc2-d8780851334a | -5.69 | -45.17514 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5117d502-e521-3467-8b5c-8b7095d03a3c | -2.95632 | -48.027 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acacb2b3-214e-3e78-a82a-548106fd99d4 | -2.63651 | -49.88165 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c6fde83a-84f5-35bc-829c-08df2643be10 | -2.48144 | -48.80877 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef921e39-2daf-3f3f-b5e8-fee26b38f425 | -2.20224 | -50.22118 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74c9a7d4-cc40-3804-b330-3e84a8a34c9a | -3.05185 | -49.52883 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7e9ccc5-4417-3136-9101-4789bc7d0847 | -3.09995 | -49.41033 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc6cd560-fbfb-3f65-8ee1-540f3cbcce8d | -3.53626 | -50.3326 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78496ea4-c7eb-39b3-98bb-b5b54b4c0b3f | -2.39585 | -50.32228 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7b837ce7-f34d-35d1-8517-fb8b18cd8adb | -3.95596 | -48.16512 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b621c74f-5258-3539-8b6c-e9ca80a2e88e | -3.09327 | -49.40928 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e4ba762-2fb2-3d19-8b00-b27df25e74f8 | -3.87552 | -46.61301 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f1123d2-a161-3654-8da4-c1a3291d931d | -2.60904 | -49.81497 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af9a49f5-ef67-32ff-a983-28e971861e33 | -3.24692 | -50.30639 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 661a955d-f38d-3352-aa2c-4568aa7774b5 | -2.29132 | -50.47005 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README110.md)
