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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eacc265e-2d1a-3f5a-947a-570ad1396269 | -10.82024 | -56.95599 | 2025-05-19 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8705c817-f51c-3d57-9e83-ca57c64f9ce9 | -12.13897 | -54.66473 | 2025-05-19 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b074a23d-0b35-3c7d-b952-053e72639eed | -9.32788 | -44.83506 | 2025-05-19 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0d0b38e-b4b4-3f77-a4d5-f209d9cc3c40 | -11.5623 | -47.87093 | 2025-05-19 04:51:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4710936-6bf4-310d-b3fb-e656cdb5a3db | -6.63659 | -47.85239 | 2025-05-19 04:51:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2619205-7757-3e86-aebc-bdb9fb9ab0e5 | -12.1351 | -54.66773 | 2025-05-19 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e80970bc-b612-32f4-8c96-289fdc608160 | -13.30623 | -47.60184 | 2025-05-19 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 289169a9-3a46-314d-9837-a4ee03250ad7 | -10.82604 | -56.94381 | 2025-05-19 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9867ac1c-1660-3192-9260-4723cfa81d3b | -10.82271 | -56.95777 | 2025-05-19 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26de5442-bf2a-399c-a736-6c3da5580a4c | -13.30575 | -47.60565 | 2025-05-19 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 621820cd-5b62-3570-a062-f6c02429e337 | -10.75869 | -57.23208 | 2025-05-19 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62626c63-07a9-3030-8e2e-1b2eb274e08b | -12.03848 | -54.9734 | 2025-05-19 04:51:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e0e6781-ae04-39b8-b200-61009617bbf5 | -9.48168 | -49.14407 | 2025-05-19 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ec43e9e-b49e-3ad6-869e-6e97b7b9569e | -10.8275 | -56.95713 | 2025-05-19 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b240fca-27c6-3aa0-867e-daf7f8394c8e | -12.12627 | -54.65903 | 2025-05-19 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd3cc875-ae36-3644-a6bf-8a1c6b84196d | -12.11019 | -44.7597 | 2025-05-19 04:51:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81677f41-bd2a-353c-a6d6-e5eb7f725a5f | -10.81909 | -56.95718 | 2025-05-19 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b5efaac-ff2d-3bea-bdba-0bd4d767a6c2 | -10.82387 | -56.95656 | 2025-05-19 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8e6b1d5-8ceb-3794-8899-6ecbd01e92b6 | -11.30868 | -54.01992 | 2025-05-19 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c66968f-fff1-37ce-bd4e-650b0632b12e | -12.13178 | -54.66719 | 2025-05-19 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b33f209d-ae7b-32a2-9f36-94a79317fec4 | -12.1049 | -44.75891 | 2025-05-19 04:51:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49ee2709-6085-30e5-b92a-865bab1d3bd0 | -9.48617 | -49.13995 | 2025-05-19 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 321b552b-79b0-3146-b297-618e8297495a | -10.45588 | -54.37468 | 2025-05-19 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f43581f9-8eba-3be7-aafa-977dea3252e6 | -12.30068 | -52.47496 | 2025-05-19 04:51:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c87a8d27-7dab-3c5c-8a93-552400991e25 | -12.03573 | -54.96926 | 2025-05-19 04:51:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 090cd35b-6da3-3e0a-bcdb-84b394ad0e71 | -12.12847 | -54.66665 | 2025-05-19 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad03fd76-b418-3720-b602-2eea33793149 | -12.03515 | -54.97285 | 2025-05-19 04:51:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 349f2132-878d-36f8-9d14-777b7dab3596 | -13.30655 | -47.607 | 2025-05-19 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b4425d3e-e986-35b0-bf39-270943bca6d7 | -10.45533 | -54.37818 | 2025-05-19 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c20763e-ad2c-3418-9fa5-888b829413ae | -12.67618 | -48.6375 | 2025-05-19 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce1b0b1f-260d-33f4-9254-2d9d06b73b70 | -12.13566 | -54.66419 | 2025-05-19 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d1f6236-ce5c-30b8-aece-7c6fb91d0674 | -12.29785 | -52.47076 | 2025-05-19 04:51:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7e921e4-0281-3e92-9bdb-71f3b72f38cb | -9.47407 | -49.14288 | 2025-05-19 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcf10d5e-825d-366a-b2ac-51e883570b0e | -9.47271 | -49.15235 | 2025-05-19 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aad5f7aa-0ea7-3efe-93f0-69cb32b088ab | -12.10978 | -44.76303 | 2025-05-19 04:51:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d943b5b4-03ed-39ae-a213-42ab52fda89a | -12.29604 | -52.47046 | 2025-05-19 04:51:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d687f2b-e522-306f-b72d-ee3da5e1d4af | -10.75574 | -57.22705 | 2025-05-19 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42816a2a-1d5c-3a90-8766-616254f2aa1d | -12.10449 | -44.76223 | 2025-05-19 04:51:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 217ea9ab-7bd2-34ba-a77c-18d68db9810e | -11.30813 | -54.02343 | 2025-05-19 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49c38a38-0d87-3267-9d50-481c76159888 | -12.03906 | -54.96981 | 2025-05-19 04:51:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35d32274-3a84-3b4f-b87e-659fe2467bdf | -6.15575 | -48.5139 | 2025-05-19 04:51:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06646d61-3acc-3a93-b679-48f83befb6a1 | -13.30703 | -47.60341 | 2025-05-19 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 278436cf-8da7-392e-b57d-049520672498 | -12.03964 | -54.96622 | 2025-05-19 04:51:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b840276-beb0-3e85-8483-aad25726639b | -9.63191 | -48.20702 | 2025-05-19 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 018aeddf-a38f-3a42-b279-26e798f318d7 | -10.75942 | -57.22767 | 2025-05-19 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b9a6c5b-5009-3f11-a720-15a2493efde5 | -10.76844 | -54.78303 | 2025-05-19 04:51:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7483ec4c-5f01-3b66-b354-4ec6ec484171 | -14.40306 | -46.04496 | 2025-05-19 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb779fe3-8ad3-332d-84e8-0f68a4f5f418 | -13.09278 | -52.28411 | 2025-05-19 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8ab82fb9-fa1d-32e2-a9e6-043e57dce27d | -19.45718 | -45.30865 | 2025-05-19 04:53:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eff0a062-0cd0-3cd0-afd0-9140b96e1ba0 | -12.6845 | -58.13535 | 2025-05-19 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b6539f0-041f-36e3-b366-ce48fbbbc491 | -12.47088 | -57.19515 | 2025-05-19 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cca7708d-469a-39e5-b854-75f8aee6b7a4 | -17.05975 | -45.02572 | 2025-05-19 04:53:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 09feaeb3-6af5-318e-b3de-152eadfe4e0e | -17.34411 | -51.90497 | 2025-05-19 04:53:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 538ee307-6f40-38bc-af39-f0b7f0ded3da | -13.04947 | -53.71934 | 2025-05-19 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b70ae160-6e0a-372b-82d7-fae57db79315 | -17.05382 | -45.02864 | 2025-05-19 04:53:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c6dc7460-a3ac-3744-8db0-79f07364656d | -17.69663 | -54.09197 | 2025-05-19 04:53:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dc76fdb-287d-3e13-a8e4-dee363afe081 | -12.68606 | -58.1293 | 2025-05-19 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 034519a6-28f3-32ae-a656-2eb0db3fc02b | -13.06859 | -52.02081 | 2025-05-19 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4b3c5e1-d348-3e0b-8596-a42aaba9523a | -15.09077 | -52.84494 | 2025-05-19 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab0026c1-fa67-30d1-96f4-1b2250ffe076 | -12.46729 | -57.19453 | 2025-05-19 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9bd9b7f-11cb-34e3-aa83-26d1281e3a82 | -13.16265 | -56.81964 | 2025-05-19 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bef988ed-88c9-3f7a-a078-f4873bd12d69 | -17.06014 | -45.02197 | 2025-05-19 04:53:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5a7ee13e-40da-3c23-9db9-f914a9a67f0a | -17.77868 | -42.8055 | 2025-05-19 04:53:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a376885b-e3aa-386f-b615-0c99855ee977 | -12.68529 | -58.13068 | 2025-05-19 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 697cd02e-c934-3618-91a5-7e6b791875f0 | -17.05421 | -45.02488 | 2025-05-19 04:53:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ec8bb1ee-0531-30a7-bda4-41ff04ab85a9 | -13.04562 | -53.72234 | 2025-05-19 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 401ffbc0-1cd8-3c10-823c-40a3a5cd6ece | -17.61938 | -50.91681 | 2025-05-19 04:53:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1894f14-2628-390f-bd90-802f2348d75c | -12.45651 | -57.1927 | 2025-05-19 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb5eab9a-d08c-3fb9-9649-1ef71e62cd68 | -13.80071 | -52.89381 | 2025-05-19 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28cbc99f-9463-38d6-be6b-4e3c8e78686c | -12.68524 | -58.13394 | 2025-05-19 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2aad7ac5-8cf8-3f6d-aca5-3ba26d4b678c | -12.86173 | -60.22752 | 2025-05-19 04:53:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d280fee2-f57f-3d61-ba19-13e8fa1fef1c | -12.85877 | -60.22789 | 2025-05-19 04:53:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90c4e9cf-8cde-3429-a8c8-6cd9b740b018 | -17.91805 | -45.53065 | 2025-05-19 04:53:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48b89d32-eaf1-375b-9ced-4c259e2943e6 | -13.04616 | -53.71881 | 2025-05-19 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afdd8dd6-abea-34d2-a86b-5d9dba8833cb | -17.62038 | -50.91533 | 2025-05-19 04:53:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e20766dc-5be1-3b17-9fef-5e0af95a179b | -14.02147 | -55.134 | 2025-05-19 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69ea705f-3e0a-3360-96b7-237bd95ee3b5 | -16.7559 | -48.60519 | 2025-05-19 04:53:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a8ad110-ab54-3508-bbd3-727f8cfd9b2b | -13.80744 | -52.89486 | 2025-05-19 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b12a64b6-1623-3e3f-9199-d02fb6f7338c | -12.53208 | -54.88973 | 2025-05-19 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f39ebf8-45a9-3837-a578-33d5584c610a | -12.45722 | -57.18853 | 2025-05-19 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 141d34cc-ae56-33a1-afec-a25de49899de | -13.04231 | -53.72181 | 2025-05-19 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 21a9f1d7-3005-3aea-9d59-0a8af0391c0f | -13.16198 | -56.82365 | 2025-05-19 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 92407d18-865b-33f3-88ef-7344f5b9d0d1 | -12.50453 | -54.33395 | 2025-05-19 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d715876-e358-3cae-ac0c-5468b1db1a6d | -19.06624 | -53.4594 | 2025-05-19 04:55:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36b8f9ae-08a6-3a46-a2cc-b04c4179c8e1 | -23.34035 | -46.7742 | 2025-05-19 04:55:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8b6384af-555c-3e00-b8b5-9d7e18fb83c8 | -21.03802 | -50.66444 | 2025-05-19 04:55:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ff18cb6a-33ff-3357-8d4b-6920e05e4bcb | -21.25633 | -48.63617 | 2025-05-19 04:55:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2cc232fe-2494-3351-93f3-a97213f39952 | -20.17809 | -46.96408 | 2025-05-19 04:55:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b228939-c21f-35dc-88ef-774f7c04e142 | -23.70989 | -45.42966 | 2025-05-19 04:55:00 | NOAA-21 | CARAGUATATUBA | SÃO PAULO | Brasil | 3510500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c45dc793-b2e7-3345-844f-2afe3cf86776 | -23.70953 | -45.43414 | 2025-05-19 04:55:00 | NOAA-21 | CARAGUATATUBA | SÃO PAULO | Brasil | 3510500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| dfc89ca7-25c2-3f88-ade6-b35dd0ec4a5d | -22.67861 | -42.85543 | 2025-05-19 04:55:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a17ab22f-2c66-3580-9291-696f8651b8fb | -21.13307 | -47.7897 | 2025-05-19 04:55:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38f1994b-66b4-3fd0-8733-b0e209a4fc8f | -21.0416 | -50.66884 | 2025-05-19 04:55:00 | NOAA-21 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e1b85c30-0fe0-350a-89cb-d01927e1473c | -19.06281 | -53.45885 | 2025-05-19 04:55:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b570378f-8ce9-3de6-a7b0-9b1c5b4887a2 | -21.87926 | -53.29388 | 2025-05-19 04:55:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ee10803-479d-3c1d-aaa8-bb93a14d6472 | -21.26469 | -46.58887 | 2025-05-19 04:55:00 | NOAA-21 | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c283e88a-fa43-3171-aa48-cb7835c402b8 | -20.17748 | -46.96979 | 2025-05-19 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff17a05f-921a-3008-84e3-17ef95f75eab | -21.25577 | -48.64131 | 2025-05-19 04:55:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| fd9e92c4-da29-3ccc-95a0-d8d519bcde7c | -21.87571 | -53.29332 | 2025-05-19 04:55:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb1540a0-3953-33b7-a657-32ed31c4edbd | -20.17718 | -46.9727 | 2025-05-19 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README4.md)
