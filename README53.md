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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b2f3b1b-7526-3fc2-b401-c13dd7657fe7 | -4.41923 | -55.47718 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 735826e7-e2ee-38c2-bff7-2742b8d4c85c | -5.67038 | -45.1974 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69e0827d-6292-3f7a-b379-8ec50f977d73 | -7.13396 | -43.07989 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc9bcfc1-be06-36c3-9922-98ad7cfd08f2 | -6.22385 | -41.67648 | 2026-09-23 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fc408c9a-130b-3c72-9adf-c03d055df6f0 | -5.82961 | -50.21321 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a3a6bdb-b43f-3762-b8d8-2bf2ea730a04 | -6.13537 | -43.85617 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be9bd70c-7297-3b9a-a0dc-b74aa38360c9 | -6.20146 | -47.37487 | 2026-09-23 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9578c8fe-50c8-35b4-814f-5cffcf13e284 | -5.76176 | -45.1106 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| dc4cc692-4970-3f8e-be57-f5a2a981051e | -3.36258 | -50.76398 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0a7c23b-54af-3213-bfdf-37f1e274359e | -5.61282 | -43.35962 | 2026-09-23 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebe546fa-2c12-3e98-8ea4-0755af48719b | -5.81949 | -52.06045 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 892811ea-bd48-3600-b5ac-5520b5edda95 | -3.39162 | -50.82281 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a45eb2b7-59ec-3d41-9a1d-2c88df7fff92 | -6.37583 | -42.79123 | 2026-09-23 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f455f263-4349-3cef-b35d-9a7453752e95 | -3.5318 | -44.8423 | 2026-09-23 04:25:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c8e3fe2-bf37-3246-ae23-cc2b3b507e23 | -5.00313 | -49.4747 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36b62c64-f03e-3884-bc91-fd534e201e8a | -6.00075 | -45.23434 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1862d5fa-0f56-3153-9aea-de6401ff7903 | -2.81902 | -49.24925 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c24825bd-ffc8-3f85-9759-26856d3b666d | -2.76259 | -57.03503 | 2026-09-23 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7313836c-c215-3d3d-863c-fb7e949656f9 | -5.35262 | -45.16287 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5f172a29-9c30-34c3-87ba-3300b2c57c9b | -3.81848 | -58.88517 | 2026-09-23 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bcbf6e9f-fd98-3f4f-a78e-a718ec67161d | -0.83139 | -48.51749 | 2026-09-23 04:25:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 616c0b30-efd0-3817-b7b4-8445e71530cb | -1.41305 | -49.30292 | 2026-09-23 04:25:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b99cc42e-2976-31d4-8ee3-0957f2d8e619 | -4.09949 | -56.20383 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc83612-9531-3ec2-8d10-3dc34e95ad62 | -5.8735 | -52.07373 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bf71130-58a3-3b6c-a244-805e18d9299f | -2.95572 | -54.08022 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 949bd2f9-90ad-36f7-8be8-3a1459335874 | -7.03059 | -44.66097 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 628108b8-18db-3dc6-a924-bccc510592c9 | -6.17507 | -44.12671 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3152bac-0539-3259-b80a-2ad7da140c18 | -5.52639 | -45.64408 | 2026-09-23 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b866dce1-c050-3528-adf7-bb898a08af3b | -5.15432 | -48.88587 | 2026-09-23 04:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce61dd6f-c4da-3940-958e-c11f8a702747 | -6.1371 | -43.84462 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b741961d-cc32-3360-b342-d6b7fe4cd43e | -5.77971 | -47.15733 | 2026-09-23 04:25:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4f3e4e67-4d0a-3133-85a6-0c5d84994685 | -2.73604 | -49.45836 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d47d29a6-e0f4-3d01-89cd-bf1363f32b64 | -6.99206 | -42.59637 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| db8e8f96-a328-3acb-9597-03b937896ab5 | -3.65977 | -54.26772 | 2026-09-23 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f1d6376-6279-3d9f-aa02-03bd596ad3bd | -3.15339 | -48.07127 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5a7db3d-b44c-3a4a-bd26-b6de8dad86d7 | -6.16332 | -44.14061 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66ed652c-fd01-3c5d-9b33-614cd8239e7a | -5.56939 | -42.73366 | 2026-09-23 04:25:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2d150a68-0412-3754-8072-08e6ade3a37b | -7.31895 | -42.26038 | 2026-09-23 04:25:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2491c79f-d97e-34ea-aa53-78c816c5c845 | -2.95797 | -54.08955 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdd83962-7f61-3ed6-8bdb-eebca87f23fd | -5.80093 | -52.09364 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65d242cf-41fb-30e4-9512-9db4ddf9e6bf | -2.94833 | -54.08497 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1995d0d6-13c1-3afc-8430-a38ddead6b6f | -3.96588 | -48.12497 | 2026-09-23 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab98051f-ceb5-3c16-8001-3d218ec26626 | -6.43745 | -48.46202 | 2026-09-23 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b16a54e4-066a-3bbb-93a2-642112dbe335 | -3.23368 | -53.94909 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c740d1a-c5ab-3c96-8a61-b951ec88fad5 | -7.13833 | -42.06491 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 26269bce-90df-3e67-bc54-f30e9b5c89dd | -4.5756 | -45.65479 | 2026-09-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57da6d67-eae1-3372-8874-abf2548b2764 | -5.82934 | -49.95705 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7cc3e3f-140b-35ea-8b08-46f7be94dde9 | -4.37322 | -55.27305 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b0ff7eb-e938-3f40-9788-c8022354c148 | -5.82733 | -52.19608 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 188b2b87-95ad-332a-aa14-1bfdaac92749 | -6.48164 | -42.78245 | 2026-09-23 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0cc1a9ab-311b-30f8-8b79-dd60cc30c63a | -3.23428 | -46.94003 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f90025f7-7a68-3af3-a81b-091068404ea3 | -2.62515 | -59.38042 | 2026-09-23 04:25:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b45debf1-a03f-3dec-b41a-9c71f25fd846 | -2.23805 | -48.75098 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0662ed09-c33b-3880-8485-87ae63c80bef | -2.96699 | -50.39296 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45a5e675-0bf7-3903-afae-24bd4135d369 | -7.02831 | -44.65299 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 91b57bcc-b4ca-3e6a-978e-396d66f63b84 | -3.0677 | -54.39574 | 2026-09-23 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37d802de-b9c5-38ff-8ab8-263bfd7c1c93 | -1.3855 | -49.04114 | 2026-09-23 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a90bde5a-8028-3bdf-9665-82c0f0fbd7b9 | -6.57474 | -44.15459 | 2026-09-23 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f8897007-85fe-391d-98ed-af3ba2b798ad | -3.13287 | -45.76647 | 2026-09-23 04:25:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2069cd0d-0ae2-3a2b-8c12-083608abf267 | -5.82887 | -50.21776 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd569085-b28d-35b9-b4c1-5dc23888c971 | -5.99414 | -45.23657 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2bf904c-65f1-37bc-8c23-a3fd596fc7c3 | -4.91905 | -45.65538 | 2026-09-23 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb459ea7-e03a-3676-8f71-9192048f3fef | -3.66027 | -54.26463 | 2026-09-23 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62249165-9a9f-3f5b-876f-2dbc4552417a | -6.30988 | -47.42075 | 2026-09-23 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5760807-e004-33af-bed4-a5bbfcaab8c6 | -6.53976 | -45.57703 | 2026-09-23 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99572154-df0f-39cf-ba77-04cffccacc2d | -3.03944 | -50.26856 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdbc498b-217b-345e-89ea-7c46f5c845ae | -5.61831 | -45.24699 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| da8b5464-92c5-3818-8309-5f76e068b852 | -7.13764 | -43.08043 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54fff032-4faa-353a-9faa-32074492fcbd | -1.21539 | -54.55561 | 2026-09-23 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0acd720f-d4cf-3339-9b92-bb4cba44c1b9 | -4.9369 | -37.95658 | 2026-09-23 04:25:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 560ad8b0-8a8c-3869-b453-e886c148a06a | -6.61547 | -43.74397 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 478f6054-f61a-3c3f-8921-310ac64d314e | -3.15399 | -48.06742 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 857649d8-d1a0-3464-8c31-e32e8ab64818 | -4.45763 | -47.9248 | 2026-09-23 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 66276b29-794a-38c8-8efa-b15a9b8cd5d8 | -5.88656 | -52.10094 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa1c94b9-1758-374a-9073-9dcba97f39d1 | -6.97835 | -42.16697 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a8e3cbb4-60a8-3441-a06c-c25a0891d8ee | -6.89647 | -43.63021 | 2026-09-23 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1bb50d8-3af2-369c-8448-c47a6e4c1387 | -5.56637 | -42.72873 | 2026-09-23 04:25:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f42cbb03-de18-3d28-9881-ebceb744ccb8 | -3.23037 | -46.94304 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| caf7289b-4ff2-3b47-a567-50d9d5c8f682 | 1.43797 | -50.83048 | 2026-09-23 04:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5aefa83-658f-3cf7-b1d0-9e0e62d0528c | -3.23372 | -46.94356 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e98076e9-6c1a-356a-9df9-3ed6088fbe19 | -3.3815 | -50.44186 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 687ac4f5-dd2b-3ab6-9e29-623a2da88690 | -2.45212 | -49.21891 | 2026-09-23 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b50bc8d0-9091-37e2-a56e-8d782c2ba8d2 | -6.609 | -43.73891 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| fb044f53-f12d-3cfd-a01b-5c7f6c235003 | -3.5194 | -51.63095 | 2026-09-23 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0208958c-40cd-3ca2-a03e-94fdf8a175c0 | -1.13914 | -47.71222 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ddee666-6239-37c6-a8ee-83d173840c1a | -5.87711 | -52.13105 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dfed8cd8-9e3b-367f-89a8-ba517f328156 | -5.78355 | -43.78198 | 2026-09-23 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9b5b03c-778b-398e-bae2-27c57233a3f9 | -6.13395 | -45.01455 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb743909-6f29-3c21-9d6a-bdbff1ceef5a | -4.57018 | -49.55461 | 2026-09-23 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2fbffef-c839-3487-91b6-1ad91e4a3e30 | -3.0734 | -54.3933 | 2026-09-23 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe526e57-6e95-3295-ac49-3c5955cdc81a | -5.61158 | -43.36769 | 2026-09-23 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b29ac5c0-fef0-3834-b0de-4083e310416e | -6.88862 | -43.63816 | 2026-09-23 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1dd1a93-7f10-367f-8953-767185e3e207 | -3.75044 | -58.86352 | 2026-09-23 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e5055a1-a158-383e-8476-ea718fa76de8 | -5.61777 | -45.2505 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 44fded5d-ce95-3519-a7e2-1582a9b9d6d5 | -6.89492 | -42.92199 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d53bd8c6-3e1c-3df7-9dc6-ef7fad09a189 | -5.17644 | -56.18171 | 2026-09-23 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a6f4ba3-9ae2-3982-bd33-fb48ec14d201 | -5.8102 | -47.76382 | 2026-09-23 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1584c57-6568-392e-a227-92825ac32fe8 | -4.22324 | -50.6621 | 2026-09-23 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15e3bb1d-8dca-3ca6-8da4-a6ebb64f66af | -1.39222 | -49.0467 | 2026-09-23 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51b996cd-83c6-3aff-8fe9-71fccce48f68 | -3.23731 | -53.95815 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README54.md)
