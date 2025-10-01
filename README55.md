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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e898c423-4b76-3f5c-8754-66e30c8b5721 | -10.91298 | -44.78829 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d76e65f-5de5-3dec-a38d-8f00a6ac89d2 | -16.84983 | -49.02961 | 2025-10-01 04:21:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6cde9fa7-2a91-3687-810c-1a5f19c221b8 | -13.25831 | -48.43757 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1a3e2eb-ee6c-3ccd-bfeb-f73221369607 | -11.465 | -45.0679 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b893228-00aa-391a-a3e4-1824d5994041 | -15.33928 | -47.93227 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14ab6053-d7d9-308c-b094-f40f17536e15 | -15.27562 | -48.01174 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1f39dcb-2f46-3835-8d90-3d2fb5438b98 | -12.91794 | -47.17405 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa043b2c-9bc9-3d01-991e-f1880ae1d906 | -14.70178 | -48.25415 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a1f61f7-aa16-34be-8be4-93a830e5afa4 | -16.40435 | -47.03688 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c0b43eb1-a6eb-3ba5-af8a-bba19b01c10c | -12.84045 | -46.86926 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4353d6bf-c257-3983-8e6e-f50fe8012f5c | -11.13731 | -43.38233 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| af2aec9f-d01f-3af3-a934-bfc1ca020eb8 | -15.30916 | -46.40196 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 132dea9e-dcae-34c4-816c-016bc63d7d0e | -14.78298 | -45.75566 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3efbc7bc-1881-399f-9dfb-ea56609c1489 | -11.20363 | -47.73552 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc25e6b6-0486-3736-8d6d-9b31c24989cd | -13.67373 | -48.06609 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9574d0c2-d708-3423-8d6b-9c59492459d2 | -11.46506 | -45.08971 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ba4005b7-1cee-33bd-9248-7fd6df0dfb97 | -14.75916 | -45.75554 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a69e0193-b03c-3ef2-8ead-130f3a7be39d | -12.8256 | -47.00533 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf795a22-001c-338f-a6f9-a2f12f483847 | -13.21181 | -47.3372 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d1c38ee-f0f5-38ef-8af4-97dca0a85e81 | -15.94319 | -48.11787 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1083b97-d2cc-3cf6-ae09-58240fe60df6 | -14.17683 | -46.1155 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36dee078-9cfb-3cd0-83b9-e712503b9459 | -10.97833 | -46.52662 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec4010d4-dfd2-3e12-a7ab-caf118153e8e | -15.79097 | -43.65878 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b16f3b8d-013b-3d08-9a7b-d0c144cf7cce | -10.64473 | -48.53674 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8340a86-c6b6-347c-b03f-3593b8288011 | -13.45461 | -47.24525 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8177e153-a1e5-32e3-8370-8114fddda6e8 | -15.17776 | -46.41694 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66915e47-aad7-35cc-961e-e3bcd5539781 | -13.92693 | -48.09292 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 097d0729-d431-3e69-8518-c2374fa47a01 | -13.35651 | -48.16239 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4f28373-c99a-3c1a-b017-433499642180 | -12.82503 | -47.00889 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45485fd1-fda0-33c2-81db-06449bc57154 | -17.51391 | -43.48503 | 2025-10-01 04:21:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2178a063-73d7-31d1-a253-ddf9ca76abd3 | -12.21947 | -47.80437 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4af6946-1908-3d3e-a5d0-8e399d0430ff | -14.03302 | -47.96319 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78dcec1e-31fc-3283-b43e-44fdc0bde5ad | -11.8175 | -44.96322 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b9d81f8-6576-3afc-8670-006facc9daac | -12.77807 | -46.87718 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d2a4639-8f2e-3748-9ec9-7faa278c33e9 | -13.76527 | -47.95948 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b8bb0dc2-c4e5-3be9-b49b-27f07bf40b0d | -13.29596 | -47.23692 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94513220-075e-3ca0-825c-1c5b3132b29a | -13.64262 | -48.02272 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79334a85-5ce0-3d5f-b341-305960011fb3 | -9.31897 | -50.6274 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9482fd44-f557-3eed-8c06-087edaf446e0 | -14.78411 | -45.79279 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5272ee5-45b0-343a-beea-74ff1fe79d8b | -14.68794 | -48.23281 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e96f05b1-1a26-316c-b3d0-ca3cc26358c1 | -16.19168 | -50.00292 | 2025-10-01 04:21:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31daa4a8-3291-31d1-8f03-326cdeb585b9 | -10.33471 | -48.19201 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4480d1d8-3a1b-380d-989d-7e69b2c87f8a | -15.07594 | -45.07397 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72d13583-8218-3e1f-bea6-939b4de6a1f7 | -14.79241 | -45.78304 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| efbb90c1-6e06-31f4-b7b8-04d0234fcae0 | -16.44016 | -47.02454 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e7582a2-e095-303d-b209-7a10be27c706 | -14.90259 | -48.10526 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5de86f06-d7ce-36e8-9289-3c5c0035c556 | -13.45737 | -47.24931 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 57ce968a-c315-3c8d-b112-8bd9f7ae98d5 | -15.13942 | -48.01062 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6a1010a-daa0-3891-af55-2bff360a1cd2 | -13.36438 | -47.31857 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 017e2013-463f-3464-8fbb-04c4ffa288c1 | -12.82883 | -46.87826 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64e730e4-356f-32d6-87c6-9ef0b862ad86 | -11.47224 | -45.08718 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e045fc2f-000e-3e3c-83fd-f996236c500c | -10.70783 | -47.99667 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68c6fabc-f033-3126-b313-4f5aed2a8b12 | -13.56173 | -48.06314 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23c598ef-5c68-37a0-be63-76d1b9f80b8a | -15.77296 | -43.68244 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ab65248-0fcc-3da7-82ee-4eb3fe59a24c | -14.59401 | -48.22517 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bbbc1c26-87d9-30ea-b43c-bf6287d0c5c9 | -13.32285 | -48.14934 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1764205b-6753-3a3c-973d-3d33459f8e87 | -16.67923 | -49.35749 | 2025-10-01 04:21:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec1676d7-b445-35dd-b5eb-3aa12ff799f4 | -12.77173 | -46.89449 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a563edb-ad10-302a-8c84-cc37236f5658 | -14.51832 | -48.36911 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1831bd62-ce42-370d-af7c-2db81d6b04f8 | -11.44974 | -43.50997 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97dd290d-daa9-3fa4-9eaf-32f4455a9466 | -14.79462 | -45.79078 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 12c96918-57af-344c-8dc3-c3759fcdc0dd | -14.89493 | -48.13094 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 369ac51e-a572-337c-86e6-bbe6a1e9801c | -10.48589 | -55.58168 | 2025-10-01 04:21:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ad84e8d-01ce-3869-82c2-047439f808f7 | -13.33526 | -48.14325 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08433189-57fd-3231-8874-a1616ae1038c | -15.26385 | -49.2786 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 469f2fdc-a8e5-3e7a-8337-afe79c94b6f6 | -11.94733 | -43.91427 | 2025-10-01 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29bf4ee7-bc73-3e19-845b-d2d209972d39 | -15.26308 | -49.26199 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5af77378-be68-350a-a82a-e8412f912ba0 | -10.93265 | -54.33385 | 2025-10-01 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce1ca0b4-3515-39dd-b60b-190e3032bad4 | -11.4703 | -44.98882 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 749c4f31-e2b3-3f7d-aa65-e03bcecb0ad6 | -13.81059 | -48.0321 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48c76f96-921b-3073-9e98-e1d951d65d2a | -16.38175 | -47.05143 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0b5afa4-6192-3f28-a011-92c2bffbe1e3 | -11.13627 | -43.37724 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d6902773-6957-3a70-9601-3c7a285a4c02 | -16.02785 | -50.88214 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 522d0574-7459-3e3f-898e-fc817c848bdc | -10.92416 | -44.3337 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22be6e80-e59c-38f8-bbfc-10355752870f | -14.72412 | -48.1593 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6340bba-fbdb-34c6-8f23-487c0dcbdc4c | -15.39613 | -44.97205 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad41bb52-1ecd-31a9-a6c2-695c95622735 | -13.09512 | -47.00272 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6743e90f-2efa-3499-967f-cd45b7a4b2fd | -9.95257 | -51.38118 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 551d4970-d49a-3759-ad28-1ceda7c253b7 | -13.99048 | -42.9677 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5fc2a099-374f-3634-821c-3c2ba49ebb72 | -11.83476 | -44.98415 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80056f82-97ad-34ff-ae91-9967aa2926da | -15.61227 | -46.90415 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bff2d48d-da03-363c-91bd-192b1b5285c8 | -14.17738 | -46.11198 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8be83214-a3d6-3c00-bbcb-a7bce25c342e | -12.82854 | -50.57718 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a24fcc00-6252-3761-85ea-bb0d15fd7335 | -15.26616 | -51.47864 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4252665a-de8a-3cc5-8ec0-9ada900a867a | -11.45265 | -43.5144 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41216daa-fb80-39c8-8b5e-971a226f9bb1 | -14.79296 | -45.80161 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 127fbbab-a9f4-31a5-907d-e92276811115 | -11.50935 | -43.53901 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7533e7bd-50d7-3d16-81cc-cc49d37b5e62 | -14.3537 | -45.918 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c18bad54-a355-39c4-8a3b-34b486230378 | -15.44616 | -43.64274 | 2025-10-01 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a9a421c2-b175-334e-bab1-4d77b54a09bc | -12.01411 | -46.6278 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f334d74b-c99f-30fe-a2a8-9611d8e5ecea | -14.52509 | -48.37027 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40582275-8cbd-349b-84d1-5c0e1999f880 | -13.363 | -48.14419 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ffc61ed-44c0-3a41-95c9-95fc585366f8 | -12.88776 | -45.25606 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae135bee-98e9-3928-a322-0172efac8163 | -12.93502 | -47.19526 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f4b40b2-f24c-390f-a38f-0c63e21f035b | -13.914 | -48.08717 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a884c8d5-d4fa-33f7-aed0-ec93c359eb6c | -10.33755 | -48.1965 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ae601e9b-a6a5-32d2-89bf-06efab1dfcf2 | -11.84529 | -44.98219 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3bfe9a2c-062f-37a9-bf5e-5fd07cad3dce | -11.4621 | -45.0202 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 693160a1-20cd-3815-a1b8-079db65805c4 | -12.46509 | -50.22775 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 399cf870-30f4-31b8-8775-c365395f61a6 | -15.83594 | -46.24977 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README56.md)
