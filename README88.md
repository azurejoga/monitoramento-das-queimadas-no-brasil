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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c4e885c-b38c-3c15-89c6-dfc77d3e92ec | -13.16448 | -47.81787 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6016e1b-a537-3468-b0cc-ae2cec16d677 | -12.79971 | -46.86443 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7baba59-cef0-3342-a268-43a8acee9655 | -12.41257 | -47.49977 | 2025-10-02 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b92f5705-77c3-3eef-a503-9eeb679fbc99 | -15.40555 | -47.04254 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42face18-7a22-3b94-a7a9-bc0c099be221 | -14.22096 | -46.11734 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2350f4b-968a-39c5-ba44-da78da236b5c | -14.08675 | -46.65861 | 2025-10-02 04:32:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ba9d4ac7-95b7-34a3-a3ac-dd22623e0cc7 | -12.0231 | -49.71465 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 413c03c5-ce89-3b80-a3d9-22b09876df6c | -15.84364 | -46.23956 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9504a1f7-63bd-33de-a267-11e1d46d6062 | -17.11208 | -47.1127 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42099807-6c50-3f35-92e0-3adc9a1424b7 | -13.96142 | -48.12323 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf66df27-7699-3b06-8e3e-b2b0b66071b8 | -12.80363 | -46.90564 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dde4231c-3278-376a-a311-d350894d80eb | -13.86667 | -51.24649 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fbce86d-44d9-327d-8fe2-de207665e855 | -14.88434 | -48.31554 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 769bc391-ee71-3ea4-a2e3-a5f3529e1572 | -18.5864 | -43.04246 | 2025-10-02 04:32:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 940b3e65-e104-3b82-85f0-9954f01aeb68 | -15.35331 | -47.08404 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e9611f3-5006-34c1-84a5-bea8b58aa121 | -16.00338 | -50.90743 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bd1967f8-16b4-35c7-af14-bfbb9e1ba6e8 | -13.81538 | -47.54444 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28a22803-a407-3bc4-be8b-26f6c05cb761 | -18.84182 | -43.1448 | 2025-10-02 04:32:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1d5ddafa-e8fd-37e1-9015-3c04487356fd | -18.50405 | -44.04274 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 24e255fd-05d1-354b-b9cf-0a2393faf8d4 | -12.70117 | -48.57795 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30728708-3299-3a9d-9ba3-98df7ad49a00 | -14.42359 | -46.13558 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52f452ea-4a1c-3877-a194-5aef73ba1d36 | -13.24694 | -47.31355 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b554083-e2b6-38a5-b88f-48d1bf0703d6 | -12.68791 | -48.55367 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5cb03b13-e256-3bfe-afdb-70a3b34f86a9 | -13.18222 | -47.83535 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 010dd3e7-c9a6-397d-b4c6-e2ddcaf22b31 | -18.66515 | -43.87916 | 2025-10-02 04:32:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1135a041-8715-33c3-86a2-ae047e13fcff | -12.83969 | -46.95147 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2eb18f0-3039-36bb-aa00-7cb1d87e33fc | -13.95866 | -48.11912 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| affb6a6b-2b7b-310f-b865-ce29e9b8f2b1 | -13.94917 | -48.13583 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 682f08c3-9977-34e3-bb41-9963753f9e02 | -14.98578 | -46.90951 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bcff3512-3575-3f4a-a27e-7394fe5907aa | -12.5107 | -46.83737 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40bd6e77-c0c2-3051-9d6e-2d25e65cd74d | -14.80386 | -46.96338 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a55e5caf-7b3a-3917-88a3-20f0d45fa449 | -13.31015 | -47.86032 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa126378-5555-3db9-a7d7-c753f083670d | -17.09161 | -47.10937 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2db2b8d-dd24-34aa-8730-32672623c57e | -12.47196 | -47.27321 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e107123e-72f1-3a87-9ac2-e2ec761fe4af | -14.21061 | -46.11577 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 09078b0c-63e9-388b-8b1c-3121a518b3b0 | -13.80255 | -47.52366 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa4b441d-c451-37c8-ab49-dbea5e88e4e4 | -15.92573 | -43.30114 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bfe52ff-399d-3db6-b670-6090aaa0c211 | -14.98607 | -46.91286 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d14db29-5173-3860-858a-7c0e4c35edd8 | -15.50525 | -45.9013 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fac7035d-d975-3c17-aeef-f49b02f6c834 | -12.28264 | -45.36843 | 2025-10-02 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cf3728f-0a1d-37d1-aaf4-82f483d1d6f6 | -16.03647 | -50.86039 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a001113a-5015-33cb-a400-6355698ed644 | -15.25659 | -49.31639 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c518948-5ef6-3501-a02d-ea2d62fa14a8 | -11.5791 | -50.17007 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c61c37ca-ddaf-366b-b8eb-b0c3ed8011aa | -16.01386 | -50.9092 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd042e60-5003-3df4-8f25-5d948c50dab2 | -14.21056 | -46.09258 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c17eafc5-a914-3713-a606-d3a69865530d | -15.39653 | -44.97724 | 2025-10-02 04:32:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a1e9eee-f793-3e58-855e-b386a9321b9b | -13.07984 | -47.08566 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67bcd8d9-d95e-3d8c-aded-8a59a84fed8b | -13.97053 | -44.9231 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17abf45c-85ba-3f0c-b3a8-1f0885d7e74e | -19.2629 | -47.34983 | 2025-10-02 04:32:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d81b3275-f3be-3c5e-b46d-595aa0c100d2 | -14.36333 | -45.96093 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a682d0db-c322-3cd5-87ad-e9173d76432a | -14.81538 | -51.40393 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5632eed9-1d4e-3c78-91f3-c9ac2f01f22b | -14.88536 | -48.12184 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ee1cd1a-d998-3ad4-a90c-01cdc2741b1b | -11.85323 | -48.0256 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd451ca4-5e78-3ed3-9704-14a5cbc9a1d1 | -12.95461 | -46.42702 | 2025-10-02 04:32:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7e7282c-9d41-32af-a18f-6172b64ff842 | -12.47252 | -47.26966 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 23a4cfbd-4285-3f09-b68d-49f0c2a4f419 | -12.41954 | -54.35315 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d77ebfe2-1cc5-3b28-9174-9cfe73bcd653 | -12.85193 | -46.93896 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae6cb399-3e86-3df5-8954-d3545716704a | -14.68987 | -45.19093 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b45808c-c9df-3551-b19e-2b1e32ecc3f4 | -13.57515 | -48.19486 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c343f40-415a-37db-9bd4-0867dcc5d619 | -15.15938 | -48.39826 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b5e7547-82f6-349c-9a49-b09c342a8a74 | -13.68581 | -48.07047 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29bd7f39-c208-30ea-9829-19dede518b41 | -19.95582 | -43.65183 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 3c5ddc78-878e-360a-951d-57d15c6fce6a | -15.92951 | -43.33433 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 402d8268-41f4-349b-870e-2ed32c4e5770 | -18.18041 | -53.27328 | 2025-10-02 04:32:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 771ad385-fe74-39d1-ae06-a3b86f62c6a7 | -15.225 | -48.7326 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae890cbf-f3de-3f3d-8238-89d49609569b | -13.70016 | -48.61829 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 380d5090-a9fa-3b87-ab84-86de6ce80804 | -15.22445 | -47.17636 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82a6f97a-26c4-3559-8f29-019324282999 | -17.21465 | -46.98679 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9667e988-153d-3426-8313-e58a03837dc9 | -14.19627 | -44.75117 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7773d7f5-ec8f-3967-819a-7d8b520edf94 | -12.49623 | -50.25906 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ea574c2-b408-33e9-8300-9b5466b39f39 | -13.17615 | -47.80887 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ec3ac19-5e1b-3070-82b8-531705907ae9 | -14.65096 | -48.12738 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0347301-f4a0-3c43-9808-0dab3cde8f90 | -12.83693 | -46.96935 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04411532-e822-34c9-8bbf-ade43e77fc4f | -13.3151 | -47.85024 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eefa8d94-9aea-309e-930a-f8ae3558dcd4 | -13.94308 | -48.13117 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9776d08-4766-320d-b92e-da2e5b3f030c | -14.22326 | -46.10207 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb5a217b-5d89-359d-a776-ae6c84c47d09 | -15.50818 | -45.90585 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3f55191f-a8cf-3774-a00d-25680249daa6 | -19.45425 | -44.27556 | 2025-10-02 04:32:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97a0b096-b5ad-36fa-95c7-6b682f44d8b0 | -12.82084 | -47.02917 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 785df1e2-59b0-378d-b31f-c29508df3d7f | -15.46553 | -45.8796 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64469fed-34e5-304d-8d9f-bdd1c118123d | -13.86711 | -47.94724 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18853337-af91-37a3-a330-a1cd91d4d139 | -14.8965 | -48.09439 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cea6a4ed-80fc-3ccb-99b2-ebebd9ce019d | -12.02072 | -46.63128 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08c6b592-42b2-3561-ac3e-3a455e38977e | -13.95307 | -48.13282 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3dd68ede-d0c5-3da0-abc8-691bc1c0582d | -16.76881 | -44.93795 | 2025-10-02 04:32:00 | NPP-375D | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccc0269e-1820-3b64-87c8-46baaf2f37b8 | -16.57904 | -45.12019 | 2025-10-02 04:32:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5f1725e-9eed-317a-8110-f071816e2b8a | -14.58356 | -46.71616 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f280574b-6255-3996-9dd6-3b95100419c8 | -13.31032 | -48.70074 | 2025-10-02 04:32:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 404bc456-1625-3caf-9cde-7383d43a8865 | -12.24291 | -47.78735 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3caa6fa1-e649-3e2a-9614-b11241213a8b | -17.91004 | -44.60785 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c63bf7e-c85e-34b0-bfb1-d0d48b5ebd75 | -14.30378 | -45.97945 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46e15694-c336-3474-90b5-971f0bbd1724 | -12.67102 | -48.57305 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17a88353-99b4-309c-9be2-4029c2686ddc | -12.76195 | -50.55094 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95bcb6f6-7c60-3949-8165-0b75c8f949fc | -13.30928 | -47.58349 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4b17fa5-f7b6-3a76-94f8-ab874a2bb54b | -16.13582 | -46.67664 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b851ebb-b8f5-3edf-938a-b68f216c77ce | -14.21406 | -46.11629 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2ec94aef-aea4-36bd-bff6-b017542e61ad | -13.54533 | -47.28089 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ef03371-ac79-366f-b006-1c060d8335ff | -14.3113 | -46.0004 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b79d52c-ba29-31e2-9851-da5fd754eefa | -15.28077 | -49.30528 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71ccb475-ba74-348a-be43-d7be3654f458 | -12.51273 | -50.28967 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README89.md)
