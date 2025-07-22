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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 529a121f-a61c-3e65-9fba-a80b642557b0 | -11.72678 | -48.17609 | 2025-07-22 00:24:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| a5f78bb7-265b-329e-bace-9766cb4a307c | -9.96106 | -44.29065 | 2025-07-22 00:24:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 578197a8-4436-34bf-9c85-da7668ebefdd | -15.93289 | -43.52917 | 2025-07-22 00:24:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d7a8cae5-6c55-3b1f-862e-8529f75fb2c9 | -12.65501 | -45.0517 | 2025-07-22 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 6767b875-440a-39e1-b295-cbfb2b5c5c0b | -9.59436 | -43.84921 | 2025-07-22 00:24:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ac9f564b-808c-3bb3-8658-1377cb37e85f | -11.71514 | -47.77489 | 2025-07-22 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7d47b5b3-f2d7-38c4-b2b0-ce7a60dfa0fe | -11.90996 | -44.06283 | 2025-07-22 00:24:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6d192de5-8f01-3be8-a9b7-3e4f6c8622a0 | -10.23492 | -48.07116 | 2025-07-22 00:24:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ae8f3d40-d33d-32f6-a5e2-daef3d741ef5 | -13.3639 | -44.77274 | 2025-07-22 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e988f2ae-baa7-36a7-adbc-0b31f83d2130 | -13.30904 | -42.40337 | 2025-07-22 00:24:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 531ff3e8-9ece-3a77-aa0a-aa018857b41e | -19.41255 | -44.96927 | 2025-07-22 00:24:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 495b0269-0d54-30e2-bbc0-27a1d344fc6e | -11.80914 | -44.26715 | 2025-07-22 00:24:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6cc02d7d-e250-3926-aca1-2e19473c83f6 | -16.47299 | -46.15936 | 2025-07-22 00:24:00 | TERRA_M-M | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 81d1544a-9c3a-337e-84ac-e3fdd1b28914 | -11.73678 | -48.17472 | 2025-07-22 00:24:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4924e6c5-f30d-3496-8dd5-e0014b2c451f | -17.02383 | -47.20156 | 2025-07-22 00:24:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2d94fb82-e92b-32f5-9da3-474e3579245c | -10.55847 | -50.37123 | 2025-07-22 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f49b35de-8657-3c6d-8600-02274ae1d360 | -11.24207 | -50.367 | 2025-07-22 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0037247f-cf91-30a3-852f-c94a8eb5f42a | -11.81041 | -44.27624 | 2025-07-22 00:24:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 31cccd24-1dea-3da0-963c-12933d72d665 | -10.62741 | -45.2334 | 2025-07-22 00:24:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 11194adc-5ecb-31eb-9595-cf9af1c408e6 | -13.68867 | -45.67741 | 2025-07-22 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3e7c116e-e8f8-3d24-ac4c-8377fb46cf8f | -10.62617 | -45.22445 | 2025-07-22 00:24:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| bfc7a32e-2c33-3b40-a342-dedc61085319 | -4.38545 | -43.28625 | 2025-07-22 00:26:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 457.8 |
| 66986150-0372-3c2c-8b00-9e4e1769cfab | -6.19915 | -44.3958 | 2025-07-22 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9c6e4ab4-70d3-3517-885b-0e4a5ae6a9ed | -7.09149 | -49.1617 | 2025-07-22 00:26:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 00b0a261-afda-38c8-a781-6e6b2cb27f97 | -5.68755 | -43.6579 | 2025-07-22 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a9a20268-7a20-3b32-841d-f9c9f3f1b93a | -4.38706 | -43.29765 | 2025-07-22 00:26:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 4d3ecbaf-b689-395b-a16c-26eb857b4c72 | -7.51663 | -49.44207 | 2025-07-22 00:26:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 87589d35-b13c-3bce-a3e8-a5803b90c9e1 | -8.51044 | -43.29417 | 2025-07-22 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 98227aef-1044-3bea-b47c-645081b29cae | -6.67294 | -45.66546 | 2025-07-22 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a6aaa84c-0bfc-39de-9e09-8631e613df68 | -9.05743 | -45.07247 | 2025-07-22 00:26:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| caeea637-d99e-3bd9-ac20-a7230a497ccf | -5.56724 | -45.21088 | 2025-07-22 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6ec0768b-1263-3df1-976b-29d257b44880 | -7.20518 | -45.32512 | 2025-07-22 00:26:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fe3d11ee-b3ad-3c71-a1dd-c3c409c8f884 | -6.19779 | -44.38617 | 2025-07-22 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6d7535cb-68e7-3007-8196-d103a88c8f7d | -8.88343 | -50.15779 | 2025-07-22 00:26:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 6f438263-c64b-3656-8657-42f7bc03e10a | -6.97637 | -42.80747 | 2025-07-22 00:26:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 50a67293-ebde-3264-b6a1-2b6b8dce726a | -8.91232 | -47.3649 | 2025-07-22 00:26:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 3a5d191e-898e-33df-be0c-b87840260e95 | -8.92155 | -47.36361 | 2025-07-22 00:26:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c7e9d9a7-7d3b-3b49-8c30-96156086e053 | -3.65005 | -48.32892 | 2025-07-22 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8957d25b-e173-36b9-ac32-82215b680d8b | -7.27646 | -50.31865 | 2025-07-22 00:26:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e4b2f881-61c1-34ec-9b9d-1df360ebaf0b | -5.66989 | -43.67119 | 2025-07-22 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 660c634e-b2d2-3853-8c40-f83e4b15e6e2 | -8.911 | -47.35516 | 2025-07-22 00:26:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8dcea4a1-9d36-3a14-a28b-3c053bb7aa80 | -5.68907 | -43.6685 | 2025-07-22 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| b8cc10ca-5e6f-3a97-95d9-079b182fcfc9 | -5.73039 | -43.95644 | 2025-07-22 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b26cb6d6-c932-3ab1-9333-8df57ceaf02b | -3.18722 | -49.44783 | 2025-07-22 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f5c06a59-c51c-39e1-b765-e8aa196545f3 | -3.18869 | -49.45858 | 2025-07-22 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0a37bc93-900e-3099-aa11-881d2bad8e90 | -6.51136 | -45.30958 | 2025-07-22 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bf117f1f-24dc-3b65-ac0c-1a09f641d3da | -5.69058 | -43.679 | 2025-07-22 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4aa7656d-d7f6-34fd-b3c0-8515e5e98206 | -4.37546 | -43.28775 | 2025-07-22 00:26:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ee24d653-e6e9-307e-b09a-46569c146d26 | -4.4812 | -46.07587 | 2025-07-22 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2d0ed0ea-47e2-38b6-8fc9-c10479b40220 | -8.51192 | -43.30442 | 2025-07-22 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 41fd7443-fb70-3602-8976-d95c583ab479 | -7.09302 | -49.17332 | 2025-07-22 00:26:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 39.3 |
| ae18a5e8-18b4-3a98-a218-0bcbba3b528a | -5.84414 | -48.15502 | 2025-07-22 00:26:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d2f788a0-de02-3003-90eb-54490c68ff43 | -6.16266 | -43.75916 | 2025-07-22 00:26:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2592e3b5-d053-3497-b977-8419e6f6ff11 | -7.25438 | -44.30484 | 2025-07-22 00:26:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 12c2c73d-afb6-3461-b968-63ac69843f8a | -7.083 | -49.17468 | 2025-07-22 00:26:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5a6a8ab6-732a-3323-a2dd-bbf1bb182ae3 | -7.14647 | -46.09736 | 2025-07-22 00:26:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 05498b33-d518-3480-8ecc-8c3d979b5a52 | -8.10236 | -46.82431 | 2025-07-22 00:26:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e618ba53-4c3a-3506-b1bf-1911282f36d1 | -9.06504 | -45.06224 | 2025-07-22 00:26:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 2a73b2e6-b51e-305d-8267-596b9e73f6da | -5.67948 | -43.66985 | 2025-07-22 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 196b9da8-66ed-3a80-858c-8a18c363c7fb | -4.37708 | -43.29917 | 2025-07-22 00:26:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ee0a0188-f4eb-3b76-b1a0-11908d8a91c7 | -8.92499 | -44.45428 | 2025-07-22 00:26:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 42887642-9bc3-3676-a327-a4b7bf183706 | -7.13439 | -48.7169 | 2025-07-22 00:26:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 22.4 |
| c7351f8f-d3ed-3e8d-b4fc-cde786dfc03c | -7.20643 | -45.33405 | 2025-07-22 00:26:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7d1f5e0c-3303-3ceb-8fc4-9596e0246229 | -6.48598 | -47.18816 | 2025-07-22 00:26:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ab17ee52-e422-3cc4-9a17-97067b8e1427 | -8.89452 | -50.15639 | 2025-07-22 00:26:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e5880868-011b-3881-8457-08af3116983d | -5.56852 | -45.21999 | 2025-07-22 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0a55997a-b771-384c-a3ad-06100181bbcd | -8.92023 | -47.35386 | 2025-07-22 00:26:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c7f1a41f-132b-3ac5-ad0d-b8762a60cbf6 | -5.67796 | -43.65931 | 2025-07-22 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| eca0ecb7-0a19-33e4-9cfa-e2a6734d1892 | -5.66837 | -43.66068 | 2025-07-22 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 331bbfb4-484d-35f7-ae47-0186e5c070c9 | -3.49976 | -43.24506 | 2025-07-22 00:26:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8e9495ce-bb67-3e72-81dc-f737f4948704 | -6.64034 | -49.75772 | 2025-07-22 00:26:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 6413f321-52d5-3253-acf4-64f0eee217ee | -9.67498 | -49.89848 | 2025-07-22 00:26:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3bcd9a98-803a-36cf-866c-0e73d60a53d9 | -3.179 | -49.45988 | 2025-07-22 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 2aa793b2-1c43-3e09-8d0e-2d3fd1c8a281 | -4.68331 | -48.2751 | 2025-07-22 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 79259217-3402-3a90-b496-8cfd33a5d752 | -3.17754 | -49.44915 | 2025-07-22 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 328.8 |
| 40478559-1da5-3c9f-8276-03f98c247b4f | -8.5134 | -43.31467 | 2025-07-22 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 01cd8b40-c67a-3fa6-84cf-760ae3d5f7e2 | -7.1477 | -46.10622 | 2025-07-22 00:26:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 293cf8b6-0db3-3a64-aa4c-6f89da61613f | -6.62995 | -49.75909 | 2025-07-22 00:26:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 5d71c3cb-2eb6-3aa0-8bcf-a06ca423e550 | -7.25304 | -44.29539 | 2025-07-22 00:26:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 177e2946-3017-3d0b-813b-8f8779cbf682 | -7.17719 | -44.14685 | 2025-07-22 00:26:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a9965951-bbce-3fe7-a014-e2238bd47816 | -7.2783 | -50.33255 | 2025-07-22 00:26:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| b97043fe-58d1-316f-b182-f37d75973cbb | -3.35415 | -42.87403 | 2025-07-22 00:26:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4a783443-c9ae-3cd3-8459-e69860d555fb | -7.87744 | -47.75463 | 2025-07-22 00:26:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f153c644-73a4-381f-bd8b-ad7640fe820a | -5.91645 | -43.46574 | 2025-07-22 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ae399c55-eb46-36ab-8dc7-f7dcc8d6ed3d | -9.06629 | -45.07117 | 2025-07-22 00:26:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| e3514dd8-86ba-37be-ad5b-f357b3f26214 | -9.9182 | -47.82812 | 2025-07-22 00:26:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eae0e5ba-0389-3027-9044-89f4f79ab57a | -4.388 | -43.2896 | 2025-07-22 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 215.5 |
| aff0da4f-a768-34be-873a-756c7ee2c7e0 | -4.3882 | -43.2663 | 2025-07-22 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 6b27b523-4210-37bd-8c11-7e6b704e1c5b | -3.1649 | -49.4435 | 2025-07-22 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 7c25cbaf-43ca-321b-a3f0-5348ab34d914 | -3.1832 | -49.4642 | 2025-07-22 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 191.5 |
| c25dda21-0604-3c6b-93b6-56fdcd1bb377 | -5.6946 | -43.6669 | 2025-07-22 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| a96a8bfc-c6b0-3eac-bf16-0525f000e573 | -4.3693 | -43.2907 | 2025-07-22 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b13163b1-a655-3489-8454-95a06f2cae71 | -3.1648 | -49.4648 | 2025-07-22 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| b2d2575c-a965-3fb8-b712-9c25abcba06c | -12.511 | -57.7825 | 2025-07-22 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 78619f29-d1c8-31be-9052-670497a71368 | -5.6758 | -43.6683 | 2025-07-22 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 68071f39-9ee8-30a8-a83b-61bcaf94de94 | -15.9333 | -43.5166 | 2025-07-22 00:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 25c38fab-e2bb-39a4-bf4e-e38205c95fc1 | -12.5113 | -57.7626 | 2025-07-22 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 94d2fe6e-173e-3042-be67-939816c6f538 | -4.3879 | -43.3129 | 2025-07-22 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 12eeaed0-eb7c-325e-9d05-0599277d2268 | -12.4923 | -57.7642 | 2025-07-22 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 943c7eaa-6c94-36f5-9354-7624ddce965b | -8.5211 | -43.3063 | 2025-07-22 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |


[Clique aqui para ver as próximas entradas](README3.md)
