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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb79c885-1cf4-360f-9fec-83b9b07b190d | -23.06955 | -47.42904 | 2024-11-24 03:40:00 | NPP-375D | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2b1dd8d3-cbb9-3145-b858-24da709fcdda | -22.05444 | -47.1066 | 2024-11-24 03:40:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2332f12-dd2c-3f8c-8fbf-daa67c424a1b | -21.11873 | -50.58371 | 2024-11-24 03:40:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7880effd-9db0-3b52-9678-8d0e761091c0 | -20.76528 | -46.77138 | 2024-11-24 03:40:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6a9cf610-3ef9-3e17-8c26-60993f9116bc | -23.46635 | -47.51627 | 2024-11-24 03:40:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 67ceabbb-1fdb-35f0-8a35-ec441eee7093 | -20.32526 | -48.82141 | 2024-11-24 03:40:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8082379e-a5f7-3a9e-bd43-fcd628f95e7c | -20.3264 | -48.81646 | 2024-11-24 03:40:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f27b894-c2a1-38c1-91e9-f9d040dd76ce | -20.3192 | -48.81982 | 2024-11-24 03:40:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ba02cc0-bece-3f90-8bde-f12fb1ac1b96 | -23.46901 | -47.52087 | 2024-11-24 03:40:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 594b5ae2-b85a-39db-9b55-bb35cc2c9ae1 | -22.05366 | -47.11008 | 2024-11-24 03:40:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4eb9c001-d1c1-3eb1-99b4-5c347ee78551 | -22.53967 | -48.81385 | 2024-11-24 03:40:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ebba6b1-7cba-3437-8579-1397aeffd9f4 | -23.4698 | -47.51743 | 2024-11-24 03:40:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fa39bccd-8fb1-3e7a-bfeb-a25738f2efbb | -23.00595 | -46.60097 | 2024-11-24 03:40:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0d16d6d5-5a61-34c6-ac93-b9c361197e8b | -23.07034 | -47.42544 | 2024-11-24 03:40:00 | NPP-375D | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 725ee81a-f877-394f-aa5e-4ff46a2b1083 | -21.12082 | -50.58982 | 2024-11-24 03:40:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| dc4dd8c1-577a-3016-b9eb-f741510eb773 | -21.11726 | -50.58965 | 2024-11-24 03:40:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 869538db-32e9-31de-bded-630587d5bb91 | -1.5129 | -54.1959 | 2024-11-24 03:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a37421f0-3c95-319e-82c8-4f211e2f9409 | -5.0998 | -43.151 | 2024-11-24 03:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| d7a53906-35be-35af-adfc-a17209797385 | -3.0355 | -49.4476 | 2024-11-24 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 83c3c67d-bc00-3207-9f6f-75491f6a7cd9 | -2.47121 | -47.08781 | 2024-11-24 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| f4130e05-a96b-3f9c-b19c-3d289ee33016 | -3.74902 | -50.01387 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86680adc-7b25-3f03-9655-3cde54a93dc7 | -3.24129 | -45.54908 | 2024-11-24 03:57:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 042579e6-39a8-3d46-9148-b1a6da6855fd | -5.19636 | -49.15528 | 2024-11-24 03:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a3bc07c-1106-35e0-bb1a-b02eb49e65b0 | -5.94656 | -48.05757 | 2024-11-24 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd1cff10-cadf-399d-88e9-e773efe5a724 | -6.04256 | -44.03782 | 2024-11-24 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c8d0f82-ed46-3096-a6b6-2973b74216e4 | -4.03322 | -45.45245 | 2024-11-24 03:57:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef261614-2b4a-3e63-babb-798e586b2da2 | -2.73577 | -47.54184 | 2024-11-24 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a801725-a2ef-3f5e-bb72-9459b2f49e36 | -7.0978 | -39.93222 | 2024-11-24 03:57:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 38531ea4-e7da-390b-9d76-ca45ff7ca0c2 | -2.2865 | -47.31176 | 2024-11-24 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89437119-a318-301d-87c6-bf3ea1fc39e8 | -1.60883 | -52.58299 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c037211-bd63-3ed0-b1ca-d5e5e2b44116 | -5.9521 | -48.05542 | 2024-11-24 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 770c6432-2dc3-36f6-9216-285af4ba425e | -4.69737 | -47.18553 | 2024-11-24 03:57:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a75897e9-dfa3-378c-9782-8ec41c399822 | -4.63252 | -46.87397 | 2024-11-24 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10d8b91d-6367-3638-89e4-62f2f91971a0 | -2.69597 | -46.28739 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdf45d82-a37e-3141-97f5-ab496b5fa658 | -1.42225 | -46.05995 | 2024-11-24 03:57:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa848743-b76b-3d16-ac0b-231a4c82ca32 | -6.83418 | -39.18582 | 2024-11-24 03:57:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 294251da-a3be-3e7d-a859-908ff1f12baf | -4.02217 | -46.67506 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72099ca2-5609-3eb4-815b-2e89f62bbebf | -5.46919 | -43.22972 | 2024-11-24 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35a8eecf-8dc2-3f87-aa54-8a947c35d73c | -1.86869 | -46.4504 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af16848e-15b7-3229-a0c6-d0f9bc87fd85 | -2.86984 | -45.83105 | 2024-11-24 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 6876523d-763e-3ec9-a4ad-2d4312249321 | -4.63723 | -46.87484 | 2024-11-24 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 412c5b29-c404-34f0-8200-eaf48127c0f3 | -5.88278 | -39.05929 | 2024-11-24 03:57:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3719b0b0-5700-3185-b5a5-b88a21277a49 | -3.28901 | -45.73193 | 2024-11-24 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 24b910a4-fcce-3644-979a-6788b6e29cad | -2.00436 | -46.2852 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f09f7319-1f69-3578-a2ab-06547ed07e71 | -1.46784 | -46.04666 | 2024-11-24 03:57:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bce12cd1-42f9-3637-8706-0e7558c51436 | -4.40686 | -49.66275 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25e9e8a2-0156-3370-8dfd-e0b672df6de1 | -2.73529 | -47.54479 | 2024-11-24 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f929ce06-65e0-3b91-b6f2-9ab96defd993 | -5.71514 | -43.83314 | 2024-11-24 03:57:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7158b1cf-20fd-3c45-b75b-5f8a774790d3 | -3.24566 | -50.6669 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b543caf-9ffd-3740-88b3-4ac58f02925d | -2.28546 | -47.31025 | 2024-11-24 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dbd70750-52bd-38ed-9399-8da2824cf2f9 | -4.19298 | -42.9677 | 2024-11-24 03:57:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76ee5317-620e-3601-9080-fb5bd92c6812 | -5.44559 | -45.5103 | 2024-11-24 03:57:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9757cc5-5129-3ddb-a8ed-0f45dd048ab6 | -4.06899 | -49.19353 | 2024-11-24 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 171b295c-d747-33d7-b1c4-32fe466efe9c | -3.1341 | -45.3791 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51afc032-f38c-3cf5-a0b8-5545b2baf227 | -2.75408 | -48.66932 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2df3a3b-6fc7-3821-9f0c-fe35187639c7 | -1.60052 | -52.58878 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e27af99-1d1a-3e23-ba46-46f260c64629 | -6.22814 | -36.52431 | 2024-11-24 03:57:00 | NOAA-20 | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bfe69c3a-c49c-3fe4-bfc8-a18d69edd2c3 | -4.14167 | -38.26981 | 2024-11-24 03:57:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 321a5d4b-c574-3ac8-b382-9c5d429c47ea | -2.51353 | -48.37538 | 2024-11-24 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f36bbd7-edea-304b-a1b8-690fc73c3461 | -1.79261 | -45.71861 | 2024-11-24 03:57:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65fe7d08-726d-3e01-8aa1-dd9c11201b3f | -4.23234 | -48.70247 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c747a518-275e-39eb-a320-bfc2011728b9 | 0.41373 | -50.85376 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5d4972e1-06b5-3780-9911-e13bd8721710 | -2.44707 | -49.0842 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf61b671-960b-3345-9e23-b36bb0827d1f | -4.52953 | -46.42965 | 2024-11-24 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 302fc870-0eb9-385e-b1d0-a98bf8148bde | -3.97749 | -49.93575 | 2024-11-24 03:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 536b11ca-4058-3b32-861a-ee24b7e2a59f | -2.80186 | -46.80369 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6938171-4cec-3792-81e6-0ee69f64ea19 | -2.71003 | -46.28968 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 54d2c741-52df-3b27-be1b-0b0f2cc6abec | -2.73262 | -46.09367 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b429400-2cd6-39e0-9c6f-4ec3d9c0c579 | -4.25506 | -48.69925 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcdeb885-a2a5-3296-b059-adbe336754a4 | -2.27212 | -47.97652 | 2024-11-24 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40380802-255b-32a9-b524-ef7fd7aaf820 | -2.70093 | -46.11297 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9de1b0d1-8dfe-3ec1-9c4a-215503d8c615 | -4.24791 | -48.70868 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c28f47d7-b5b5-3761-ac88-5525196b5c7c | -4.01404 | -46.19299 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a634d74-2907-3818-b79e-617953b3c178 | -2.2221 | -46.39277 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3237c6cc-315f-339c-bb97-6490fbf004b6 | -3.97821 | -49.93165 | 2024-11-24 03:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52fd08a8-fdae-3e8b-bf94-def349c75171 | -1.42307 | -46.05494 | 2024-11-24 03:57:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90954501-83aa-3f1b-823a-bbbdfa9434b1 | -3.11901 | -45.27504 | 2024-11-24 03:57:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 37ba77e5-c303-378f-bd63-64cfacd6de5c | -5.09995 | -43.1538 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dce377a5-81e7-346a-a354-6ce613824804 | -2.74798 | -48.67199 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b9f3015c-a427-32bb-a5d6-10444500c55c | -3.13014 | -52.98872 | 2024-11-24 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f13b96a-f87c-3976-b801-6e6ae714de73 | -3.29347 | -45.73268 | 2024-11-24 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 95265abd-ad41-3639-a401-db7a103cce90 | -3.69659 | -42.30684 | 2024-11-24 03:57:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cb51c123-ed4a-37eb-8ab5-ee55f53b61bc | -5.40409 | -47.22092 | 2024-11-24 03:57:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4f042b5-a8a6-306b-9592-4a1062d4e15d | -3.39063 | -50.32363 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aeb97f57-fefa-3f35-a067-c41aa8ce4364 | -3.77506 | -44.04609 | 2024-11-24 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 431c9ddf-bf9a-336a-9d4b-e8ebccb225fe | -3.35277 | -50.51318 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd1b9d03-65e4-38f0-82f3-66de005dabc2 | -2.64607 | -46.86343 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f7af660-b385-3dfd-b026-66564fed4c9e | -3.03391 | -49.45939 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 47ee7bed-8e57-3a77-8c74-3683124f212d | -2.69786 | -46.10968 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f215cdc-d9e2-3763-bf86-23d26485c7aa | -7.09834 | -39.92876 | 2024-11-24 03:57:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9cd053cf-14d8-31b5-bcf6-c82c167c8235 | -6.06028 | -41.9322 | 2024-11-24 03:57:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c914973c-daf8-3377-af58-2942bb2cf6ce | -2.53431 | -46.39991 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9175dd75-0aee-3a16-af3e-58d8312e7a92 | -2.57209 | -51.88776 | 2024-11-24 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2d4d0364-4f55-3ece-b90e-948fcf6612c9 | -3.29865 | -45.72898 | 2024-11-24 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2866d5d-5edd-370c-9bbb-3bd9ceecbad5 | -3.28972 | -45.72749 | 2024-11-24 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c8fe288e-3aeb-32b5-85d6-d029ef9bf411 | -1.46314 | -46.04588 | 2024-11-24 03:57:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99368787-5c78-33e2-a1b0-371074858b03 | -4.81913 | -48.51736 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c34a618-0713-330f-bfdf-29bc0190b558 | -2.27214 | -48.43505 | 2024-11-24 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68de243c-3286-30af-beba-9e4dd7bc01a6 | -4.52857 | -42.90995 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f78fc41-cce8-3af0-89c9-3e5da1db3457 | -8.07172 | -34.97621 | 2024-11-24 03:57:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
