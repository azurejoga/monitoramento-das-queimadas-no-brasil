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
| 2a38e4e7-9f37-3798-ab91-726f3ad816de | -5.98334 | -53.60384 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b451847a-1cc4-3fcf-aeb6-9b6f8d8324e1 | -8.87323 | -47.91994 | 2025-09-06 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a302855-0617-34db-a9be-a678c018c1a8 | -5.31683 | -44.92642 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e81460e2-23a8-368b-ad9e-2c3ae5d41941 | -12.51722 | -53.84338 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c4aa71b2-d8d5-3c95-978f-907d965da737 | -5.95748 | -53.799 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4fceab0-4131-3094-8cc5-961f86323e67 | -6.18554 | -53.26344 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39611f1c-a55b-3b76-9ee7-015685ff81bb | -7.32831 | -48.49642 | 2025-09-06 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d2bfe4b-6eff-3c23-b28e-676585c02cb7 | -14.80679 | -48.12108 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 57ec27b6-3413-336d-a8b3-4ca1d7977163 | -8.4401 | -47.31901 | 2025-09-06 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8170a9a-fe7a-336b-a9c4-37a28d748ef3 | -7.41299 | -44.94688 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0eb6446-63b6-375f-95b7-e93137b46ac7 | -5.85127 | -46.10934 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cacc404d-ec42-31eb-9dbc-0e620c4f5194 | -12.95862 | -54.77723 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d3364d8-a9b9-3971-aea1-56ab321d802a | -6.83027 | -51.87631 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46f7554c-c7d7-3c50-959b-8484744c0a45 | -13.01304 | -54.84091 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbca6343-dc64-3f3c-9e98-337b955c396a | -12.92812 | -48.04827 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| be1cab2d-4dc6-323b-af79-c77ab3bd67e1 | -13.90423 | -48.02406 | 2025-09-06 04:17:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf4f8849-b00c-3517-9528-64d2e99c29b4 | -9.01629 | -49.80239 | 2025-09-06 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3f2dd7e-cd81-36a2-b358-e00cf92702d7 | -6.18188 | -53.25077 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80773bfd-21f2-3e6f-81a0-d604fbf53012 | -12.91072 | -48.01752 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5003166d-58d7-3e78-9831-8867f1c939fd | -16.29452 | -45.68967 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d74c8b28-381b-39bd-b078-a78cafd6add3 | -9.34209 | -40.39274 | 2025-09-06 04:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d72fbeb8-f247-397d-9c56-c9a92f25dfff | -6.87119 | -45.5537 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a1dae087-7e6f-37e5-8388-3f360ff69754 | -16.30451 | -45.69138 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5fb1c2f-ea1a-3dfa-ab4d-ec66284d14b6 | -6.17074 | -43.6133 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b800c4d-5475-3c42-9677-425629b7821f | -12.85395 | -47.99929 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09086281-b6e8-3eb1-a864-4b3d019dbf11 | -3.24172 | -50.80485 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 64c8760e-de3d-3e50-b358-2783ad956c50 | -13.71093 | -46.88425 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50089b09-390b-383c-a393-de0116f5abcc | -4.22082 | -47.21093 | 2025-09-06 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2f85682-bdd2-3de5-b0d8-e659cc7d1bab | -5.17722 | -43.05232 | 2025-09-06 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce3f9bac-19c2-36cd-80ea-48438b95ddd9 | -5.94838 | -53.80436 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04bbbebd-659b-3bb0-a14f-0ca458305bb4 | -14.89869 | -49.44946 | 2025-09-06 04:17:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f96a552c-b9a2-3fc6-9f06-3d20544be33d | -6.19467 | -44.76836 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f06591a8-6761-3292-8bfd-b93b62e7fbec | -14.84382 | -48.19112 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45a0bc8f-0909-31dc-937d-fb21f53b3094 | -6.17054 | -44.31333 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46b2d85f-98bc-34d2-bed6-471a5857d91b | -5.98178 | -43.61179 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| acac37e5-4030-3c19-83ef-c06ad26dcc04 | -6.25697 | -42.42642 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 08946e33-6157-328b-b614-4630bd3ea238 | -10.31858 | -46.41205 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 270817b6-0340-3bbf-801b-2a5b63c25969 | -13.27431 | -46.81611 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 736a9f11-adbe-3c59-a1fa-aac0f2c09441 | -5.40442 | -42.32132 | 2025-09-06 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 146b93eb-ef7e-3fca-a082-cc3a46874565 | -13.06431 | -47.10017 | 2025-09-06 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78d5bf1c-6c4d-34e6-ac85-28c5a0733e44 | -5.98101 | -44.72775 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04bbccd7-a209-34bc-8286-e73594d6db81 | -5.17507 | -43.10886 | 2025-09-06 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35a1cf87-a1e9-3ad4-9d4a-4ec11c3da941 | -6.14989 | -43.17141 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a33a595-6ac3-3c7c-9f94-451327941a92 | -7.36897 | -43.99803 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91c3dd80-482e-345f-b9d5-8f3f549860d9 | -11.64684 | -54.54571 | 2025-09-06 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6980ce88-0b68-3fb0-ac35-d69307d603c6 | -10.16676 | -46.24214 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6516c84-6b66-3fb1-be59-c857a148dd5d | -13.00713 | -48.06583 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4237ee36-e16e-3655-83c8-b5d4d9ad0cce | -5.93751 | -43.01658 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a717261d-d406-3317-80ca-8d2d1586a987 | -8.77591 | -49.63322 | 2025-09-06 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67258e3f-49e9-3463-93cf-d8a01f25dfa6 | -6.53554 | -49.49747 | 2025-09-06 04:17:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4040d201-76d2-30c3-835b-e7bc49b0da29 | -8.56951 | -44.33849 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a50e41d-fdee-3db1-8a56-9e9c38df60e8 | -3.42787 | -43.33102 | 2025-09-06 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43656230-6e95-3efb-9fda-23e057562487 | -8.44388 | -45.03223 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d54b745b-7937-336f-b854-8fdfb8c0b3c9 | -6.38818 | -43.82328 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d6c3ffe-e882-3378-9fe6-b0fe1c5d8531 | -9.0076 | -49.80083 | 2025-09-06 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0257258e-48ac-3a82-aff8-6a7457252b86 | -15.54844 | -49.81549 | 2025-09-06 04:17:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 156229f5-28ee-3dd9-acaf-8cdb38daedad | -14.56707 | -48.01635 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99dc30c5-a17d-3711-9537-f742732597eb | -12.50653 | -53.86961 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6d4887d-f795-31fc-bc9e-d64230c61e73 | -5.95756 | -44.74731 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07a3c3a6-1012-3f2a-8472-38f2d400acda | -12.95495 | -54.80835 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6e37f13-b963-3897-9f7d-88c44b17c0bb | -16.42196 | -47.82328 | 2025-09-06 04:17:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbefed24-f523-310e-a421-69aab72ba8b0 | -14.82934 | -48.18872 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45c8b5bc-ce8f-37d8-9003-d38c59b09418 | -9.82831 | -46.53728 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 951b8829-86a8-3751-ace8-dadba7c0b327 | -8.02113 | -45.43611 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f5707121-5703-3c48-9558-9ca74e9e0de4 | -5.86777 | -51.72381 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e85fbff5-e710-3b3f-94cf-d12a16977139 | -7.46012 | -45.19369 | 2025-09-06 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9029d5df-b3b9-3280-a3fb-e456f26ade8f | -7.99181 | -45.47493 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ed7cb3b-51c3-36a7-880f-5db17704d732 | -8.88387 | -47.25306 | 2025-09-06 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66e9c5eb-6038-3432-9824-6807457fa36d | -14.26029 | -52.18877 | 2025-09-06 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9c5db07-8d16-3ed9-bdcc-0fa97959f89c | -12.95562 | -54.77602 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba7b7879-0f69-3512-936a-964746872094 | -12.18735 | -53.90438 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6abb5785-4ed1-39cb-876c-f3ca606d027f | -5.99693 | -44.7379 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd351afa-db28-3ba2-92ba-269b7e31a7a2 | -6.27752 | -53.44666 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7277033b-881d-3775-b9b8-dde3f3d6e2f9 | -6.14659 | -43.19224 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a98baa81-560d-3847-8e86-d3948c4a16e6 | -6.06639 | -43.43962 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40330851-21b4-334a-b3a3-ebe4f6029475 | -6.87612 | -52.78028 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cee3b69-c92d-3f7d-b41c-8a9c5287e77e | -3.24468 | -50.79655 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2963c10e-de56-333c-a862-d57bf5f9c30d | -6.02096 | -46.69142 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e50ec47c-b244-37e7-bf56-0f394710ca16 | -6.82606 | -52.80855 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58ebea83-f4ef-304a-836f-e88d1c1a61a8 | -9.59282 | -43.79414 | 2025-09-06 04:17:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 42b307ac-8035-3330-80c8-644a9f9b9b8c | -8.01583 | -45.4468 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a2f03b1-df13-312d-a7c4-a47696ef5de9 | -16.31117 | -45.69252 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc45e55e-39fd-33d9-88b5-417c46795ed3 | -5.86786 | -51.72052 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bc41187b-c22d-3a65-b93e-43e73ca83850 | -9.6804 | -51.10202 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eecf6f26-9faa-3a36-aa8e-c58a35ba3745 | -13.8504 | -46.29237 | 2025-09-06 04:17:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea228d65-c71b-3d47-857b-cdbef9f5b30e | -9.38155 | -48.18422 | 2025-09-06 04:17:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb2588aa-a3c3-3c35-9aba-44a102bb0677 | -6.2797 | -53.43446 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6d4de28-7508-300a-a989-a4799a414514 | -3.24831 | -50.79665 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e0567255-0877-3d64-8974-67e7fcde4902 | -5.99955 | -44.15821 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9df92384-0986-3082-af69-66e2c2785e9b | -5.90689 | -43.36039 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62135752-0506-3133-919c-b0916a902510 | -5.21147 | -43.69159 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bad63c9-cfa9-3f96-8032-e8149d6fd288 | -7.58869 | -49.28189 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8297afe-834b-3a4b-92d8-ac19c618284a | -7.34981 | -44.321 | 2025-09-06 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 01f4aad2-29a5-303d-997b-ef641235d519 | -14.59166 | -48.00249 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8ac02d7-68ab-3f87-a3e6-59afc2485aff | -5.98233 | -43.6083 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5cb877f7-e50e-31b4-a46b-d9dfff99be42 | -6.66742 | -48.39296 | 2025-09-06 04:17:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 102be86d-5512-3f14-b02d-90e476f636c6 | -13.85655 | -46.25516 | 2025-09-06 04:17:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4f75455-9958-3422-a132-2593ee52651a | -12.95332 | -54.80454 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7c5be73-975c-3fa5-a540-96a0e9d6dd83 | -6.51273 | -42.41584 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a0bcc1e5-b7e9-3eaa-a354-8eb61de95c66 | -7.67916 | -50.29509 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README35.md)
