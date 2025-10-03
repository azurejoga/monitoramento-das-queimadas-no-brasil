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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aca43fbe-e767-3122-8c88-579cd1d53046 | -14.43326 | -46.35128 | 2025-10-03 03:45:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 161d03b6-3271-394a-b99f-18ce2da6a27a | -14.19119 | -46.66822 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77332039-3552-3265-89fe-d4f6832cffcd | -11.44232 | -43.49873 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7ea8ff5-d372-3821-9239-8b74017bc817 | -11.61743 | -45.05835 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc8075f6-0dd1-3d8f-a39c-b444458b9bda | -14.89147 | -46.96947 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03c3023a-1b39-33a9-8e55-892e9742353f | -12.61174 | -47.00278 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 980fe7ba-66ae-3c33-b4aa-8b07e2896456 | -13.19952 | -47.79686 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42f55e5a-e8c7-3acf-a7a5-be005422212a | -11.92179 | -46.27365 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 0b3d8d09-0bf3-3576-8cb8-5cd50393f31b | -15.36784 | -43.66908 | 2025-10-03 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b59cb93c-43ab-32b0-9f60-61bf45e527f6 | -11.61557 | -45.05967 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e940ca1b-f085-3538-86db-e6b7a11f673c | -11.1051 | -47.83446 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 31ee53c5-208d-354b-a77f-46b8cdd6f3a3 | -14.94284 | -46.90878 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d0e92d6-3f16-3c3d-95e8-0e76861c313f | -14.9379 | -46.9055 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9bb8d1f8-a8c3-398c-95a2-88a277683997 | -11.14234 | -43.40559 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f5de8ff4-3ede-3085-a771-5c564cd14dfb | -9.92346 | -43.76152 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4dc82f66-434b-32aa-950e-546a87eb4e30 | -14.9084 | -46.96912 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c7b3d22a-e055-3b3c-a072-46a87a9d9ed1 | -13.96848 | -44.8652 | 2025-10-03 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae2e2623-7c3d-3e20-90ab-5c01df068f4d | -11.86023 | -44.9745 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb7225f5-8db7-3e0b-8490-87c1c6816d85 | -15.27286 | -47.90744 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 785314ec-db0a-3452-86a5-f67613f98121 | -15.84102 | -46.2403 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8ae0afd-702b-3cd7-bc0d-9b847392a066 | -11.90774 | -46.28269 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a64273ae-9f29-30fb-ac22-def0a7cbfc27 | -15.12136 | -48.4929 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d148dff7-1ae8-3234-b052-7554d40ed479 | -12.11488 | -44.20477 | 2025-10-03 03:45:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b40cc998-5f7a-34ca-a19f-4ac9340ae18c | -13.752 | -48.0751 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 532669b2-16b3-3c5a-ba68-5ae51797c66a | -12.901 | -46.89986 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0ef7204-f9ce-33ea-b110-dd814e17bda6 | -11.81197 | -45.03846 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b9cb348d-4564-328c-93fd-c97378fde76a | -13.19433 | -47.82248 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 242f48b4-4f94-305e-a1ae-3a14bdc38141 | -9.92456 | -43.72864 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f1c5abbb-db70-3783-a133-4e9e00bff3b7 | -9.93438 | -43.58886 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a37e6a6a-201b-3a68-9852-6a92c58bfce3 | -12.6289 | -46.97504 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8f8d508-7e7b-310e-ba7e-c0c2a8508946 | -11.60008 | -47.64699 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18e1d399-7ee6-3c3f-9127-1bc9cc72a554 | -14.00239 | -42.53297 | 2025-10-03 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7dabbcdf-711a-3b56-81d9-6db8bec61ef0 | -10.8822 | -46.71509 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d2ef85ca-9e4c-3735-8f94-d7d6c65302b6 | -9.91867 | -43.76067 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ace8795e-62e3-39b9-9808-d14d5b4bda75 | -14.23229 | -46.10091 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a772c14-afd0-35b0-a994-81baa0c39325 | -13.19439 | -47.79206 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a2926ec-0f77-3171-90da-db87a5377e7f | -14.69835 | -43.89243 | 2025-10-03 03:45:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b07abf04-a85c-3964-82cb-ceaae2c7e07f | -14.87708 | -48.30994 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6a12fc44-ddf9-355f-bbd5-ea6c002b6b01 | -12.80228 | -47.0174 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cac226e9-0cfa-3cce-855d-f7b8fc382e4f | -8.82866 | -46.77664 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 928ef96d-6c00-346f-b3d9-c2aa5f5d9b77 | -12.80307 | -47.01342 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 269d784c-9f17-3a33-a734-6f346d5f2057 | -9.42891 | -45.46569 | 2025-10-03 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e5014e8-3120-338b-9d17-2891590ea563 | -13.63645 | -48.67913 | 2025-10-03 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5da9986f-73f7-3c70-bb52-1deff86b37bf | -11.67752 | -47.49274 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6772e9a7-b526-391c-a7cd-b40750fc13f1 | -14.20339 | -46.11139 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 668e8d82-c76f-36d5-9c8e-8f3060acfbf2 | -14.3111 | -45.87211 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d110ab2f-bc30-3117-b023-6f36baf77272 | -14.30291 | -46.02116 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ae7d9985-45bd-32c7-a481-23ac2b783239 | -15.27883 | -47.91657 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fbef96c6-6789-348d-9e88-a44418a31b53 | -11.46541 | -45.03759 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bdcd3b3e-c861-307d-b80d-6c40a4adbd4a | -14.73833 | -48.10287 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6e7b27a-ae60-35d8-b0dc-00795e4c8ca7 | -13.35749 | -47.3363 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3e9bc47d-9be0-30e6-b233-dd2816735fc4 | -13.86295 | -47.93387 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54f38782-6f9c-33a2-ac5b-985b551c3520 | -9.95703 | -43.71266 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00143c33-e742-334f-a852-6360e01fa8b2 | -14.11599 | -45.65756 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1580b167-4681-34e5-a09e-0ae803a3763e | -11.01633 | -46.55386 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a141330-184b-399f-940b-229aaffa42af | -11.80871 | -45.02798 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bfe4e5a-abd8-316d-9933-480e73324083 | -14.3105 | -45.87514 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 062eae41-c513-34a3-bc88-8ad166465250 | -9.71489 | -45.43599 | 2025-10-03 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fff61a3-1fd1-3941-b718-09459d00050b | -11.55536 | -47.65306 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1893ab0-3f56-3d79-9207-c9d926a94cf0 | -14.6823 | -48.0839 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7e1f229-3668-33b7-a0af-8735f9052d96 | -12.62796 | -46.97984 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 38b02fb3-f01f-375b-922b-041b2db0547b | -12.76272 | -44.90927 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7430631d-78f0-3776-89a9-96f72effb111 | -9.9522 | -43.65815 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 599fb6fa-87e6-33a9-8a1f-10ec50682daa | -12.94131 | -46.37145 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcd77bc3-6030-3c75-bb8a-2c405145a601 | -13.31604 | -47.57777 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d16149d-5381-3722-b9fc-c1b1d648773b | -13.2281 | -48.49784 | 2025-10-03 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bef12542-a70f-3775-aa58-395398be923e | -13.30541 | -47.60063 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0d90cd89-12b3-3c62-820c-c5073b666d26 | -15.92374 | -43.33636 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 246ca212-aa91-31b7-8758-ea5e38dd83fb | -13.97625 | -48.17616 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e1e0ccd8-9291-39e2-b5e0-f156c00180f5 | -9.06273 | -46.65014 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56e4b0e9-b344-3b04-9d6c-0f5b0679af68 | -15.20275 | -47.98771 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ed653b5-020d-373c-8f1d-f13a80fb37d8 | -10.2268 | -48.24031 | 2025-10-03 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55770c1d-b5fd-35c9-9069-9f17146b4d01 | -11.6811 | -44.27642 | 2025-10-03 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e50d73e1-34fa-3940-b57d-182ad18b4c8b | -9.06782 | -46.65534 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ce01a5e6-63f9-3b60-bb37-4b04bd7287ec | -14.74791 | -48.11507 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 92cbc36b-38ae-325f-951a-5a4f270c5a27 | -9.06192 | -46.65439 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72563376-b3fb-359d-8b24-7d98d00f56f9 | -13.27597 | -47.24247 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d2b90848-95fc-3848-9db4-a96fe3a40e93 | -11.07446 | -48.36141 | 2025-10-03 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6fae47e-1a05-36a7-83f3-9ac5278cb205 | -10.76948 | -45.33612 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9c938b9-1a48-3d62-8d81-cd06bd11861a | -13.24224 | -47.35018 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c9f6d8e-7a38-3968-b7f1-919e94391dcc | -15.92299 | -43.34041 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c31b268-d3e7-3c22-979b-f5c3df549e17 | -13.77836 | -47.58477 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| acfd4461-71af-3a0a-aa90-95d9f7bce251 | -11.10764 | -47.82283 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f77d5e92-2c1b-3112-9011-a26674f87f82 | -11.83506 | -44.99829 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8837a46e-7522-325d-b6c7-70aea6d8fa5d | -9.95381 | -48.77991 | 2025-10-03 03:45:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 07b0aedf-4f16-3ea8-9a81-eb7e97b41cc2 | -14.19233 | -46.69057 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc3f95c1-a44a-3803-9b57-7e45fd28e1d6 | -14.88134 | -46.85341 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2aacfa47-5bb3-3488-9a72-0789d0405d56 | -10.28369 | -44.33014 | 2025-10-03 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d82b19a3-e957-3376-a834-4a8b5937eff3 | -11.50576 | -43.51315 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caf134b9-1745-356b-8d0e-70270114ea1e | -12.93487 | -45.09264 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19ba1e30-dab8-3287-b9d8-e1b880993148 | -14.10371 | -44.30725 | 2025-10-03 03:45:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7cb2004-8891-3615-9711-eeed57274596 | -13.13197 | -47.8876 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 698dc3e6-4d2d-3eb8-9ff0-740c2d348310 | -11.13954 | -43.3948 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a10bb5e5-ff79-3a99-8297-0939aa4473cd | -13.33759 | -47.22834 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8c18963-9214-3473-af30-d56676b06a3f | -14.89787 | -48.28989 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1a2ec15-d81f-3e9f-96f2-4d8566fb7efa | -14.41936 | -46.09114 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d48fe43-6793-314a-9be9-fa1d2ac70968 | -11.848 | -44.95641 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f740f3ca-8c0d-3b66-8468-5103c9d2ba62 | -12.11436 | -44.2025 | 2025-10-03 03:45:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35a8e5dd-1414-3f73-9d40-d9fddee8b93a | -11.86767 | -45.04149 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e72d809c-2cd5-3d92-9558-ff1d2ff01943 | -8.90751 | -45.03868 | 2025-10-03 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README27.md)
