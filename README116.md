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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c30bbb43-f3c3-3583-b8c6-d2827c4a0dc4 | -13.63886 | -48.67218 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9249da71-ce33-38ee-a9f8-c8de5b80de01 | -13.73685 | -48.0128 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f5320d1-4b37-3e2d-8819-a6b9cc071fc4 | -13.96959 | -48.16911 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86dc79cf-b9dc-3f27-8b47-21496caab404 | -14.19033 | -46.66868 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b49658df-83a9-3473-924b-211c7128befa | -13.57129 | -47.58186 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 190f385e-165e-380c-977a-19d0245b9996 | -12.30229 | -46.88091 | 2025-10-03 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90aaf154-3c14-3bc0-9d4a-1521bde0cf25 | -14.65647 | -48.25031 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95964680-5e2d-3569-9faa-0567ec55a63d | -15.29333 | -47.94735 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f26c5328-d15d-32f8-a864-041a71972271 | -12.93381 | -45.0925 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e4487c0-999d-327c-804b-6b50014cfb7e | -13.76289 | -47.54085 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b292ff1f-47ef-311f-9e3c-6045b9443298 | -14.9155 | -48.34823 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 035ab182-bf79-3c0a-b0e9-866649ea11fd | -14.58506 | -46.71272 | 2025-10-03 04:34:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c89e888-e769-38ae-99e7-125cbb8dbca8 | -14.73747 | -48.08904 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 852c6068-93d0-313c-b3b2-ad4299f21bf8 | -13.73962 | -47.9946 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c4a5fc8-6c6c-32fb-acdc-1087ef4c38e2 | -18.26051 | -53.31721 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 605e9dc8-4fff-3c06-97d9-3cfe741da742 | -13.76193 | -48.06177 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 843beef4-5896-348c-be30-aae840755e58 | -13.20818 | -47.83026 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d28526c-43a2-3956-a217-b02f8f4d6e27 | -19.92851 | -47.07322 | 2025-10-03 04:34:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a09d940a-5edc-36d5-9bb9-47d97b737d48 | -13.12758 | -47.87411 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8595a294-589a-3bd5-8955-9eaa46541fef | -20.38508 | -44.12912 | 2025-10-03 04:34:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bc39fcdd-606a-3333-9d47-3804b2ad6d80 | -17.91292 | -43.93365 | 2025-10-03 04:34:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49ef1414-e178-3920-b9a0-18848cdeac2b | -12.94213 | -46.39397 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6ce76fb-c7df-3298-8a5b-f7bc532d3551 | -18.2522 | -53.30228 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 076dfdef-1a5b-3631-b26a-4ea060121aaa | -12.93068 | -45.08718 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d55e1276-0f60-3598-9073-3437a59b017f | -12.63374 | -46.973 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c241bdf-546e-35aa-b1f8-7b72522ded72 | -12.62969 | -46.95251 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1068d711-7da5-354a-a98b-51ff4135eee7 | -18.44586 | -43.70835 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94dc9003-d8db-30ec-b8c6-8119a33fddfa | -14.67652 | -48.07191 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f6158fac-cf85-3789-a50c-734cd28cc52a | -13.22878 | -48.49338 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94ba1719-61e2-3660-bfa4-810b1a6c9266 | -13.21326 | -48.5275 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8e4c6ce-a08a-3c93-b255-62429d3ad99f | -16.36192 | -47.07227 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33fae322-2daf-3e2f-ade6-c347b72052db | -12.62733 | -46.95358 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a09fc6e0-040e-33bb-996e-9b0e8d5d8533 | -13.53102 | -47.29137 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e18256b4-9299-30fb-9b5f-1a59ba1adbc8 | -15.25853 | -49.32248 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf4210bb-4cb3-30af-9db4-46b6d7e8057c | -12.85156 | -50.50388 | 2025-10-03 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af68b0eb-d110-38de-9e70-93f3a38556ef | -13.63929 | -50.27844 | 2025-10-03 04:34:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efa91a62-2952-3a6f-af2f-aba4c4b68321 | -14.66373 | -48.27058 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b381ca3f-8458-3535-a3c5-14fbf4341eaf | -14.73916 | -48.1009 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a794e5a9-cd14-36b8-9ef7-5a9dfc4ceafe | -12.91667 | -46.37437 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0b36e0e-b53e-3d78-8b9e-a0e8f722f2af | -14.7245 | -48.12098 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57203155-c10a-3597-8d0b-f7ae29ee997f | -13.47814 | -47.24453 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91274048-a633-391c-a4ed-a385d857a47d | -14.57688 | -52.46693 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d615d6cb-861c-3fc0-93fc-aab22f25b89f | -15.8059 | -46.26336 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62fbca72-eac8-3ca9-bced-b710b158c6d1 | -15.22458 | -47.96365 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19b52925-89ac-3404-a694-a657492fed24 | -19.86473 | -43.64402 | 2025-10-03 04:34:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bdc55e31-7bf9-3cd8-abc2-0788eacec109 | -19.72853 | -46.55493 | 2025-10-03 04:34:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8927326d-98a1-3d5c-a20d-9900561fec3f | -13.21958 | -47.36069 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8756cca4-c35e-341a-a8c6-8024e080b7a5 | -12.25552 | -49.15948 | 2025-10-03 04:34:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f68b8c6-c9c4-3c66-83e4-695da53cc4ed | -15.45925 | -51.56781 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7451b63d-9474-3266-9685-a566a9bb12e7 | -16.0278 | -50.93418 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c62cba9-9289-3e78-ba15-57d1ab8ac23a | -20.13341 | -44.00428 | 2025-10-03 04:34:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 60a4ae3b-ddb2-3121-b5fe-7277f2324d43 | -16.18351 | -57.60375 | 2025-10-03 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a2320c25-122a-30bc-a06a-02892601b601 | -16.28987 | -45.24343 | 2025-10-03 04:34:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab1fad44-2711-361e-8f3e-c13d00103274 | -13.79546 | -47.58009 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5325fa59-ead1-3f51-a03c-f54504b8b7fc | -14.73815 | -48.13071 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ed66f8d-d25f-3170-911b-dfa0d1b7546f | -12.64179 | -46.96637 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 83dbdd37-6d3b-3dea-8b10-5391d4f6de5a | -15.78703 | -43.68483 | 2025-10-03 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f0e761e-5585-3192-b2b4-8e2cdf77fa84 | -15.32381 | -46.30123 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef6cab11-3391-3b17-bcf1-1bb363616da7 | -13.197 | -47.81287 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ef79e8a-baa2-350d-88f3-4e94be4ff21b | -16.01649 | -50.92475 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb98b56a-af9a-3bc9-8e67-ec0bb35a4708 | -13.53446 | -47.29193 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a11de32-b343-346a-9032-bc10d04c5626 | -15.71634 | -46.26621 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 615ff3a1-13c6-362d-bfe1-2a71d0ec41f8 | -14.436 | -46.12016 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c4f7933-4059-3fab-9a57-88bd2cf4fb95 | -17.98303 | -45.03182 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23696658-0bbb-3e19-9ada-7bd803f1155b | -19.59306 | -45.90576 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcdc78f5-7ed0-3210-a6ed-964766c95bf7 | -14.9328 | -46.90019 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 557a703a-e48b-3126-9102-68a39b2cfd78 | -13.31021 | -47.24738 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e10c1221-c929-355d-9834-5afd43d33a7a | -12.34661 | -54.15564 | 2025-10-03 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ea53ffd-cc7a-3ab8-ad42-82c97d053475 | -12.6245 | -46.96378 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2dc4f78-8783-3411-9a9d-b4f8de5bf3fb | -18.20039 | -53.35045 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bc03f37-9e54-3ce8-ab92-c6044bd1d588 | -13.55424 | -48.2046 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4afc70f-8ada-3da8-9040-ea65368a1abc | -12.95846 | -47.16665 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7d84697-c9e2-3531-b0de-e4175ab14bf6 | -17.83347 | -44.37463 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cd3632e-d060-3a19-b968-7c20fa0e7d90 | -15.57017 | -46.95747 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bd77f4e-211a-3aab-8365-50a26acbe6d6 | -15.34882 | -47.06758 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83b817cd-1870-3915-ba5b-72c850415549 | -14.44337 | -46.37677 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c677b49-65e2-332a-9041-d30dce2c324c | -12.81821 | -46.91428 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7da29cf-0efe-3b53-8caa-e82f3e60d303 | -13.12759 | -47.89656 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94dbdcdc-61df-39fb-9526-d83a72c79305 | -13.14988 | -47.89618 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d436a70-b555-35d8-a0b1-3e9222c848b6 | -14.20228 | -46.08536 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e87346b0-3a52-3b8d-bac8-4b77db1ed7b4 | -14.32201 | -45.86923 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0fb0a4b-6d26-30da-9c3f-dde8b0cc051c | -14.89725 | -46.9707 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 292702c2-5900-37bf-ad6d-6c7a9adb56d2 | -19.71893 | -45.9194 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f814d344-f52e-35f5-a036-c867a991718a | -12.61236 | -46.95907 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e349cb30-860f-35dc-9416-2a058e459577 | -14.42205 | -46.08696 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da65cebd-c4d7-3d7d-91d8-0c698f1c4a16 | -12.606 | -46.97778 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d835a437-692a-318a-8bb3-d6bf89259b6c | -18.63687 | -50.68446 | 2025-10-03 04:34:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bfea1b9-f8dd-3f3a-8695-1284f7292913 | -19.01622 | -49.75179 | 2025-10-03 04:34:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1269595b-ee10-3133-ab30-826aa68d8e04 | -14.28665 | -45.88945 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 38edbe2a-301c-3507-82b0-fec941476594 | -12.79567 | -46.87501 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc7bf833-4ce6-3feb-b5ef-2502c9bc3c70 | -14.23453 | -46.12058 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d4c2ffb-519e-3f63-a1ad-ff19913308d3 | -13.14596 | -47.89931 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c49c8699-c180-3d9d-9474-c579c1127df5 | -13.67509 | -48.03325 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd785f1f-92ee-390a-9dbb-44b4288b8805 | -13.48445 | -47.2495 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79cdcfa0-b792-3d4b-b852-e3368ce9b889 | -14.429 | -46.34873 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ab517159-ae23-3989-af23-4e52630a0db2 | -13.6797 | -48.09381 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a3e928e-54bd-331c-a306-a90937f8b45f | -13.9685 | -48.17635 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 49225e8d-8158-3547-bf15-4223a5c5e9be | -15.51719 | -46.80004 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63875841-4bda-3fe2-b78d-ea2bd35ccc18 | -12.38251 | -46.52019 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aed2d5fb-ac28-3b4f-8dfe-c2234b0ccec4 | -13.21658 | -50.88887 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README117.md)
