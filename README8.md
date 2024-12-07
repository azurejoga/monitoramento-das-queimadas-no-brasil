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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ae8b5b8-1441-333b-b970-6c4df8a5a20f | -10.53929 | -44.68487 | 2024-12-07 04:33:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e9c671c-7b6e-3c0f-ab01-2d6ab8d7a50b | -10.94058 | -45.12432 | 2024-12-07 04:33:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e0d6845-3659-3537-aead-c33649e050d9 | -13.66171 | -52.94795 | 2024-12-07 04:33:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cdd9b02-4724-30d6-a2b0-abbe5e4565f6 | -13.43777 | -49.65421 | 2024-12-07 04:33:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 790e13d1-df98-346b-b378-ca50a5fd93ba | -10.75848 | -54.78134 | 2024-12-07 04:33:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 882aed60-4929-30e1-818d-7528670e9240 | -15.15549 | -56.47939 | 2024-12-07 04:33:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63b71990-fa2e-3c7a-aabe-ab3c4dd21706 | -10.6624 | -44.496 | 2024-12-07 04:33:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd9fcab5-f7c8-3ca5-93f1-b8f0a48607af | -10.98054 | -44.73187 | 2024-12-07 04:33:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98a7106b-e92d-3d03-9665-33ba189fd147 | -16.68044 | -43.88404 | 2024-12-07 04:33:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 363b137e-3181-3aa9-ab80-d78a8897d7c1 | -12.91592 | -49.68089 | 2024-12-07 04:33:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65f656bb-277f-3d86-ac6f-fd16bf86da59 | -15.79466 | -49.01764 | 2024-12-07 04:33:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43a7ce1f-c23e-33cc-92a2-2ff72a157215 | -16.68023 | -43.88637 | 2024-12-07 04:33:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5561b113-257d-31ff-a788-1cf86e8ed513 | -12.85072 | -51.93104 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27cc98d8-23d4-3909-8323-0e2b080b836d | -12.67929 | -58.24184 | 2024-12-07 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 093ee3af-7c09-3c75-82a2-9f9c4c3c4349 | -15.5687 | -47.85658 | 2024-12-07 04:33:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec4dfda1-9c31-3a2b-9cc5-ad75e5f4f88b | -16.0129 | -51.8783 | 2024-12-07 04:33:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fc67a00-48d9-3a62-b8e1-f72f16c25c43 | -12.29102 | -45.5006 | 2024-12-07 04:33:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1cfd0c1a-c827-37e1-be0b-75206a8bab31 | -13.41057 | -41.32837 | 2024-12-07 04:33:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 42f5389a-0a47-3882-aeff-06db3d2a29d2 | -10.98121 | -44.72709 | 2024-12-07 04:33:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64ed3651-1767-31a2-8b41-ac8e439fc48b | -12.49986 | -46.3486 | 2024-12-07 04:33:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7e1a6b6-d8e9-39e9-9a56-1968a55e7fb9 | -11.87253 | -47.71216 | 2024-12-07 04:33:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e584e969-9bb2-3803-befd-5a33fdd40017 | -12.49322 | -49.59413 | 2024-12-07 04:33:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 832bdbdc-d1a2-34a3-9d2a-df2e9dd6fb9d | -12.28665 | -45.5046 | 2024-12-07 04:33:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1d4725f0-73dd-3549-9704-1a97cb9f89c4 | -13.02432 | -42.01057 | 2024-12-07 04:33:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| da5cb0cb-28e7-30ad-bebb-646633af3abe | -12.68051 | -58.23548 | 2024-12-07 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44b98838-4401-3e27-8403-6d5993626567 | -12.85291 | -51.93964 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57c10307-0896-3fbb-9bf9-69ad2c8e8102 | -11.11129 | -43.33998 | 2024-12-07 04:33:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5ba4574e-4549-30d4-92dd-4940d3b1f1ff | -12.8648 | -51.93351 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60e14021-9054-3449-81e1-9b211a7a0670 | -12.64091 | -47.54084 | 2024-12-07 04:33:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdc3b131-3bbf-3a95-a998-f1bebccf64a2 | -12.49628 | -46.34805 | 2024-12-07 04:33:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78c05cf9-37aa-3005-9f65-d5b6c68e1a8c | -11.16529 | -43.57161 | 2024-12-07 04:33:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d729e785-642c-32dc-a2ae-8c8f58fb63e9 | -12.9307 | -48.63587 | 2024-12-07 04:33:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63450adb-4e7a-3913-974f-89e5244e4359 | -12.23919 | -52.45603 | 2024-12-07 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9c13fc2-379b-3235-9833-db2209546e93 | -9.54631 | -48.95358 | 2024-12-07 04:33:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 422c5819-15b3-3ab9-9135-a764f5434b41 | -11.73549 | -54.30525 | 2024-12-07 04:33:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 017e634b-dba1-3c11-bb0f-515ab09f4cc8 | -12.27844 | -49.49692 | 2024-12-07 04:33:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6eb7937-ab45-3b3e-ad3d-29350b07960d | -12.63693 | -47.54406 | 2024-12-07 04:33:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14f76623-20df-3e6e-b4bc-b0e84260e8c9 | -10.04008 | -50.57853 | 2024-12-07 04:33:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 852f7f4a-2226-3698-8929-d883008d14ea | -10.6759 | -45.11852 | 2024-12-07 04:33:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca3bbe86-1bc3-3e80-a116-441e72cb383e | -12.40603 | -46.60086 | 2024-12-07 04:33:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0c5461b-c0fe-32a4-a7e6-22ad6ed9571a | -12.20023 | -47.15819 | 2024-12-07 04:33:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38a0b467-1648-30f0-affe-26b57fc8aed6 | -16.01227 | -51.88209 | 2024-12-07 04:33:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e150292-f928-326f-8b7b-635f66e4e31c | -13.07274 | -52.03009 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 404d7de1-9318-39ac-a2b8-801def719d3c | -13.40988 | -41.33395 | 2024-12-07 04:33:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| f1365bb1-5534-3ff6-a9ef-bf4f13177b17 | -12.84938 | -51.93903 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aa0be4b-ae63-3f65-81a4-42c9fbef56b8 | -11.73484 | -54.3089 | 2024-12-07 04:33:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58a9387f-dad4-3c19-85f9-46d649f2de4e | -16.19972 | -48.22401 | 2024-12-07 04:33:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62c85fad-d779-31ff-aaff-1827eaba72d3 | -11.41403 | -51.27508 | 2024-12-07 04:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 381a2d33-9af3-39c6-991d-99c88ef276fe | -16.68083 | -43.88173 | 2024-12-07 04:33:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c0d8d53-fb7e-35c6-bd6e-834d34aab00a | -10.46998 | -48.28189 | 2024-12-07 04:33:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 63b19d54-949e-3c75-beec-a0ebf55e0975 | -12.4601 | -46.93649 | 2024-12-07 04:33:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b96a54e7-efd3-35a2-b8c3-1c08b96c0b18 | -13.61815 | -44.08799 | 2024-12-07 04:33:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae19750c-cd41-318b-9fd0-b69bc16dd614 | -13.4056 | -41.32784 | 2024-12-07 04:33:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 50849a06-cff0-3637-b9c3-fbd4476fdd68 | -10.03665 | -50.57796 | 2024-12-07 04:33:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ef86ee55-2f44-3ec6-9a7a-d5ccd70fe166 | -10.75422 | -54.78058 | 2024-12-07 04:33:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d340edbe-9d08-3b71-8610-16be51981a32 | -10.53211 | -49.05481 | 2024-12-07 04:33:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ce0d9f1-7004-32b0-bdcd-08bfed6a539e | -12.85928 | -51.94489 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8e57f6b-62d3-3bbb-b5f5-3fcb48429bd1 | -12.65823 | -46.57558 | 2024-12-07 04:33:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3af4e1a-7150-302e-aecf-30839829bc1a | -12.23555 | -52.45538 | 2024-12-07 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf95574b-ea9c-37b1-88bd-0114b3ac6dc9 | -10.03726 | -50.57421 | 2024-12-07 04:33:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 36b719db-e24c-3cf9-b20a-c62aa5ad0fff | -12.28793 | -45.49556 | 2024-12-07 04:33:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 991d1960-ee20-3a69-ae14-175a8b6758d0 | -12.23484 | -52.45966 | 2024-12-07 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7050f95-4725-3c49-b852-9f02f5ead63c | -9.98625 | -48.49997 | 2024-12-07 04:33:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49a80558-3a34-32d6-b7a0-77ad9495a811 | -12.20368 | -47.15871 | 2024-12-07 04:33:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 178a280a-1c1d-3f10-8f14-eb7501c91ca4 | -14.38355 | -46.03577 | 2024-12-07 04:33:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6ff55516-9ba0-3c38-b162-122f53a1b4c0 | -12.65318 | -46.57744 | 2024-12-07 04:33:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27ce9c2d-ea57-392b-bc8a-7e58b07f24ac | -11.99699 | -47.16729 | 2024-12-07 04:33:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42e5c952-583f-3863-b796-19de7495d178 | -13.24813 | -46.54523 | 2024-12-07 04:33:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0736dd1-c856-3adc-8700-a9692d9a0e8d | -15.25977 | -53.5658 | 2024-12-07 04:33:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb964894-9f0f-3503-8303-1a4413614190 | -15.26346 | -53.56656 | 2024-12-07 04:33:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 375821fa-28f7-3d07-8753-06952bc69795 | -16.13306 | -47.66658 | 2024-12-07 04:33:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19c98ce6-34a3-3de0-b856-edfda17e8bcc | -16.01164 | -51.88587 | 2024-12-07 04:33:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35b96401-a9ce-3ed2-9592-9bba3ef45c93 | -14.77243 | -50.53191 | 2024-12-07 04:33:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad2104cc-e35a-34a5-8ff1-e49ef15dcd97 | -12.68112 | -58.23231 | 2024-12-07 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c57b340c-3b72-3205-9dae-c75f6658f9de | -9.22056 | -50.69134 | 2024-12-07 04:33:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8e266b1-4247-37b3-8bfd-090335fd7d8b | -11.8697 | -47.70797 | 2024-12-07 04:33:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ec40f04-c45d-36d7-bfc4-531c38497729 | -11.41055 | -51.27449 | 2024-12-07 04:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bff95898-ade8-3211-9e5a-da84134c92e2 | -12.86347 | -51.94149 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3179e7cc-a118-3b5d-92c5-35dcc9564c13 | -10.98294 | -44.73028 | 2024-12-07 04:33:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5ac8607-6a7a-36d8-a11f-e2fa624aa149 | -14.76909 | -50.53134 | 2024-12-07 04:33:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89eca203-819b-3a6c-a3c6-827d922bddc0 | -15.08009 | -48.94521 | 2024-12-07 04:33:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feaf98b3-a786-302d-84df-29fd33b3b87e | -10.04069 | -50.57479 | 2024-12-07 04:33:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6389953-2d5d-30d9-9bd0-8e8238398ccb | -11.46296 | -43.24643 | 2024-12-07 04:33:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5aa4baa9-178d-3bfc-8e2c-a7fe443e8049 | -12.85005 | -51.93504 | 2024-12-07 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d68074e-99ab-36b6-b2b3-d1fc22d4b4cf | -12.47937 | -46.27887 | 2024-12-07 04:33:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8b356fb-5a71-3e91-95c2-fe95fab2445a | -12.65672 | -46.57798 | 2024-12-07 04:33:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a76a912-7067-33ea-9654-01fd9caffdb5 | -10.41713 | -49.24176 | 2024-12-07 04:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb6fd767-b8d6-3b0a-b352-452ddf3fe5dc | -10.53544 | -49.05535 | 2024-12-07 04:33:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d924bc45-8045-339d-b7a4-ae2de2b134e7 | -9.13545 | -50.03703 | 2024-12-07 04:33:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7444b5d3-a08c-3408-aa8a-3fc334b85696 | -10.54311 | -44.68542 | 2024-12-07 04:33:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2464e231-8e88-36aa-ac13-fe0c74590a18 | -11.16066 | -43.57472 | 2024-12-07 04:33:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 246ae7da-2f68-3a1e-a928-6a81823d3357 | -12.65468 | -46.57506 | 2024-12-07 04:33:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75ee48eb-9988-3044-9b29-4673508d178d | -12.49568 | -46.35215 | 2024-12-07 04:33:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 557579e5-7f98-3ef9-995f-e8ead38ca5ab | -12.92736 | -48.63533 | 2024-12-07 04:33:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 527bf9ef-a3c2-3c3e-a23f-8bd4126bb85f | -12.48074 | -46.27812 | 2024-12-07 04:33:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 300ca73e-8dbb-3197-bce5-3bf5ede3a199 | -10.52879 | -49.05427 | 2024-12-07 04:33:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29af0461-5fc0-3d86-a028-b85a93ef57fc | -12.24604 | -54.29381 | 2024-12-07 04:33:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 205a5ef4-f93d-3b3d-beb7-9b10d456dc73 | -10.53616 | -44.67962 | 2024-12-07 04:33:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc62838e-ee64-3148-90e0-8eafa8465b20 | -9.11235 | -49.46707 | 2024-12-07 04:33:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e35d82ba-01f5-3765-a036-75aa7d7b237b | -13.02902 | -42.01134 | 2024-12-07 04:33:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README9.md)
