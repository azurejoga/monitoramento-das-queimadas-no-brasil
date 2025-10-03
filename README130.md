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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68970727-6a3d-3ba0-ae2f-b571cb8d2ccc | -13.74693 | -47.94661 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe56ed90-553f-331b-a586-f8d2b5a594be | -13.22822 | -48.49698 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52c57a9d-734e-3642-9f22-13b9245d8a2c | -15.51896 | -46.81317 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7535734c-6f41-3265-88ec-f0a336bbb56d | -15.60797 | -47.0474 | 2025-10-03 04:34:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ab0bb1a-8a09-3a91-be60-0371061dd5a3 | -13.29712 | -47.26438 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b7e680d-41eb-37fe-b6a4-a618e71b66cd | -16.04079 | -51.02286 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17b44a64-5390-3acd-b2d7-dde09102d333 | -15.2825 | -47.90319 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef11c785-bddc-36bb-abd1-3552d6c9cafb | -12.4323 | -46.47491 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 948621ad-e41e-30ce-b7d8-c2b1ba52f533 | -17.90919 | -46.8366 | 2025-10-03 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c247993b-c0a7-3ac6-9ba7-c5d136807993 | -12.63314 | -46.95311 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b14d665-800a-3e18-b1fc-615d70cebcf9 | -18.20457 | -53.36864 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c2e842c-14c4-3cff-a450-d49728290e94 | -12.62169 | -46.98287 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5f55ca4e-4e18-35cb-a7b6-bfe6e4c7273c | -13.35215 | -48.0839 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62a13bce-a25f-363f-8f43-d1085f8aff5c | -13.87425 | -47.93604 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75805654-0c71-3444-8d71-0a1df67bb3dc | -13.96833 | -48.12129 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 820736a3-e73d-3742-962f-6f13f357bc57 | -12.60472 | -49.90836 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a16f8f3-d236-3b14-8052-9eab32869409 | -12.79979 | -47.01361 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b7bd537-2012-3545-9237-cfc097a84362 | -13.15092 | -47.82047 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d24c51d5-93a8-3546-9ddf-8c6257635821 | -13.12311 | -47.8583 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eab30f5-b192-3e1c-be1c-2b9d045194a3 | -13.1425 | -50.03048 | 2025-10-03 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f039a8ee-3205-3b02-ba40-9a831559cc2e | -14.29382 | -45.91808 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69ef9264-696d-3d26-bbe8-8d59acc1b7ae | -12.62224 | -46.97913 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2a62b020-80fd-335d-887c-60db8d335552 | -13.47245 | -47.23531 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9789681b-510f-3949-809b-37d41a518be4 | -15.0842 | -42.12001 | 2025-10-03 04:34:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 180b3a68-a8a4-3dd0-a0fc-18f896182db2 | -12.79451 | -46.88282 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ac177c6-cff6-32e8-9808-4021d226ee72 | -13.21832 | -47.83176 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca03d519-432a-3c0c-8e7d-2b73cd55958c | -13.20321 | -47.88561 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f4361c6-bbd4-389a-84d6-015110b519c8 | -14.64147 | -44.74013 | 2025-10-03 04:34:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d41b1649-4935-384f-8eac-0bfb4849f3ba | -13.27651 | -47.26107 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 298451ce-8d5b-36a8-b965-024124b7b29d | -14.90105 | -46.97045 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 9a1493f0-7251-3e3a-8d96-a618b334cbf8 | -13.12536 | -47.84359 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97ecf2e3-bf26-3774-aa4c-06c800b84eb5 | -13.33543 | -47.22014 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e66a764-cc11-31b9-a05e-5ecf7ca9086b | -14.2947 | -45.88604 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34ce1f66-9a27-3597-bffc-e8fc8c1c4c99 | -13.19526 | -47.82438 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 80510068-623a-3571-96eb-de02ea7e500a | -13.51885 | -47.25508 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b56ab1e-3e9e-3383-a65d-c5679146155b | -20.00753 | -44.18771 | 2025-10-03 04:34:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e68501cf-96eb-366f-a6ff-5bef93ac697e | -12.9022 | -46.93454 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3435268-7bd3-3e1f-a177-5677d1a801d2 | -14.19379 | -46.0663 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5200ce30-eab8-3fe5-a3d4-30c66a15047c | -13.54997 | -47.30584 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a99c1222-36a9-3978-98a7-da62a8f66aeb | -13.2178 | -50.88147 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02f48baf-7f79-3588-8a7e-f77a92746238 | -12.61921 | -46.9839 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 38be8bb8-679c-39ab-ad94-6308ff0c51e2 | -15.31644 | -46.30043 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 249c0eea-8714-3b6e-88de-be8c84293db3 | -14.19809 | -46.06233 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2b39b3d-fc1e-36d9-b92d-cc2616205a3a | -19.97066 | -41.6602 | 2025-10-03 04:34:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4c2790ed-bd85-354a-8b8d-1795530c76da | -14.42414 | -46.35677 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06de8106-8cc4-3048-b14b-57e731eae191 | -12.92972 | -48.43045 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 545e3f3c-4709-3753-9ef6-2fba9101b680 | -13.54876 | -47.29047 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ea66642-abb5-34ef-b670-ac1d1eba0bcf | -19.01899 | -49.75606 | 2025-10-03 04:34:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29fee8af-b44e-3bfa-b825-3b8ebffed79e | -12.93525 | -48.43878 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14262d2f-9419-3586-b2a1-000400bc1376 | -15.32244 | -46.38832 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6e9afe9-cf3a-3e04-923a-7ee773c75cee | -15.23864 | -49.29726 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49730f6e-ed0d-3cd0-b597-6e2c4c72568e | -14.43201 | -46.35344 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8aa98897-7940-3cb0-a48d-1752e8700dd6 | -12.60946 | -47.00171 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9fdd6bcf-57b2-3d86-abd5-7e424be4d6a0 | -13.33039 | -47.60256 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 57b859f8-665a-3aa6-af98-06c400dd0e66 | -13.30508 | -47.25819 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bc99ce1-ad96-3800-9338-4388959bc52a | -13.57753 | -47.58671 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| cecab7a7-50c7-3487-8e80-2279fcf76b7e | -14.35854 | -43.84697 | 2025-10-03 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d482404-3894-3eaa-8bc0-2322a72939f0 | -14.65696 | -48.26973 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4721540f-99c1-3013-aba0-60c1ae5b655b | -13.17065 | -47.89558 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fcb4afe6-42bd-38fb-a65c-856ec3c69064 | -13.63871 | -50.28203 | 2025-10-03 04:34:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6abec020-dd28-3687-944e-3dd74e424ffc | -13.66785 | -47.30824 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d13d3dc-1524-3b20-bc3e-4d5fe68ea18e | -15.28841 | -49.30534 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a3e423c8-8ae6-3934-89e3-529cc9e4eb43 | -14.74482 | -48.10934 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5099a209-3fb6-3ca7-92a6-5ec8522495a9 | -17.96784 | -44.3956 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 29027141-9a86-3658-ae4e-44241b3fc826 | -13.52355 | -47.24725 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7f13a8d-21e1-3940-97c6-a9c49a76db67 | -13.73644 | -48.69872 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 236e3318-fe3e-3926-8c5d-1b37fbd89fb3 | -18.22867 | -53.35563 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28bbc04c-3470-3a46-a934-81da57a5f4ba | -18.65168 | -43.87722 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1790295-4caf-3c1a-a865-b5dcd8ce0e35 | -19.7229 | -45.91984 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a10269d3-cef9-37a4-9056-e49db40b40e9 | -13.74862 | -47.95821 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5907ab0e-991a-3bb4-b194-3b89717284e9 | -14.94157 | -46.88956 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a529088-abb3-3f1e-b92e-1e03ecd0f55c | -14.72169 | -48.1167 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50b717f6-70ea-368d-80ec-28e77410a298 | -15.60089 | -47.0463 | 2025-10-03 04:34:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1ac614d-e6cd-34d2-9051-c07fef64baa6 | -14.2097 | -46.05952 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 04b79e42-f4dc-3723-a7f3-9674d62c8ec8 | -12.39422 | -46.51381 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c859792-b054-37d8-a67c-618e144d5c54 | -13.08739 | -47.07534 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3956a764-cf2c-364d-ae77-e9800c011f5c | -18.20176 | -53.36375 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74f003ad-1f30-3430-a8ff-aabd19b09e87 | -14.90229 | -47.82606 | 2025-10-03 04:34:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d1031e11-d34f-3636-9b07-5ae4e3df4d75 | -15.20873 | -47.18805 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51dc7832-c619-3bf3-9a48-82c30d880b54 | -12.76595 | -50.53057 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df9927af-c3e8-3e32-a8dc-a70db0eb4125 | -13.27542 | -47.26842 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba31668c-716e-3a9b-aa84-b5735f855bda | -12.18939 | -47.81398 | 2025-10-03 04:34:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00395d1a-8e62-3b84-ad7b-69780e9afc74 | -15.91657 | -43.3474 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc0ddbcc-e4eb-3d30-bfc3-5cbc044abf3d | -16.68625 | -53.01205 | 2025-10-03 04:34:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a015a3cb-f6b5-3f17-9463-7b73d2aa1d5a | -13.6253 | -49.04164 | 2025-10-03 04:34:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 93a879d2-2b0a-3331-bddc-f851b76659f7 | -13.34212 | -48.10464 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e952b176-1207-3b85-bdde-9e9b33f941a4 | -14.90142 | -48.29328 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcbb0946-8a06-389d-b7dc-7bf157f282f8 | -16.01094 | -48.34368 | 2025-10-03 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ec701b5-029b-3bbd-803d-1265e4a2d37e | -14.21864 | -44.79362 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3449926-242d-3e54-8a17-a28498a5fb23 | -13.19926 | -47.798 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae94719e-db9f-36c5-b1b9-74406e570cf5 | -13.78748 | -47.58663 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc9be90a-ebf5-3eb3-ab13-ba1b1a0fe4d3 | -20.12966 | -44.01498 | 2025-10-03 04:34:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cabc4e11-f7bf-353d-92b7-e9c9b4580003 | -14.19684 | -46.07113 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a1003dee-af6e-3008-920d-d1d8599e80f0 | -12.62437 | -46.97312 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f19c1650-6e3d-3065-8e0a-832c45d3e763 | -13.15379 | -47.89307 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc1cdfe5-48fc-3cea-82e3-00b0838c4472 | -14.88348 | -48.34312 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff18f277-ea40-3a09-963f-00d41967d53d | -13.679 | -48.03014 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0b52fb3-1e62-353c-bc51-4dddd9135a27 | -18.20601 | -53.36021 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc2087b5-58de-3d49-9e9b-429bd1c153e2 | -14.2897 | -45.89451 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26286dea-a3e1-3245-ad58-902af0a3835b | -12.61001 | -46.97462 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README131.md)
