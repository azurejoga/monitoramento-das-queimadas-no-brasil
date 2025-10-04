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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79c73531-e4aa-3690-a766-d90550a3c502 | -5.46652 | -42.77559 | 2025-10-04 12:17:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8b437e5c-6f33-3ac5-a378-1b62fa8ef717 | -7.72419 | -46.29984 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c17c9b4b-aac3-3d4d-86eb-b3d64b598348 | -8.59142 | -46.22947 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 8ee69f39-76b6-3531-898e-55969dab90b0 | -8.22136 | -46.82015 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 36ce5ef4-4a3a-389d-baf1-49e9ba8da049 | -6.54883 | -45.81406 | 2025-10-04 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dea416b1-8df5-3183-90be-f005a3abc4e0 | -6.07888 | -42.51575 | 2025-10-04 12:17:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| e175a147-94b1-38df-8ae6-8595f7900f93 | -7.46151 | -47.17747 | 2025-10-04 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 817c425a-8c4f-3091-b6b2-4f1186237b6f | -6.35126 | -43.46096 | 2025-10-04 12:17:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 32e87e8f-8988-3a6f-a166-3661f9e198b4 | -7.6378 | -45.47348 | 2025-10-04 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 53f47d6d-0153-3b27-a413-9b175c6a2bff | -4.96964 | -42.81029 | 2025-10-04 12:17:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| ad76dcf5-27a4-312b-851f-08b2b0a83bd8 | -8.17815 | -46.99603 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 9664f72a-a5fe-3a38-b598-eeeb63593b65 | -7.03994 | -42.77439 | 2025-10-04 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 84df571d-e1a4-3150-83a3-86bcd5a8e18d | -5.83554 | -42.88295 | 2025-10-04 12:17:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| a25c4f05-6070-3683-94eb-bcc2a9d3397e | -5.1976 | -45.06993 | 2025-10-04 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 2db2123a-13c1-339f-af28-dbcf7e8d4166 | -6.24169 | -44.25674 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ad0d3156-d1cf-36eb-bd43-960116bc220f | -7.0601 | -45.78284 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6fafe01e-3a9d-3f56-97d5-0b700d7191c0 | -4.71563 | -47.21716 | 2025-10-04 12:17:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 9a5fe9f7-96a2-317f-a8bc-bf14078d400e | -6.03409 | -45.1521 | 2025-10-04 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 49daa00d-0353-34af-be6a-7ab5e4fc9afb | -6.88259 | -47.22984 | 2025-10-04 12:17:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 13f5019a-4b91-3f62-a948-d7b51ed4e99a | -7.75098 | -46.30998 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 009d7d59-772f-37d4-850b-ca9417cc8662 | -7.05877 | -45.79218 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 14e868a8-a20d-38c8-85e3-ec50ed1f7a26 | -5.69032 | -42.83791 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 36c89274-47fa-3592-9ff5-aa3a6ff674bf | -8.84172 | -46.80444 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8a3c3e1e-4395-3687-9f83-596165242328 | -7.05308 | -42.78209 | 2025-10-04 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| b341c292-9875-35cb-8957-316514d0b467 | -5.80839 | -42.72559 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| d0d786d1-1d4e-3b83-aeae-b0d066e686bb | -8.22392 | -46.80226 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5a4d5f76-210b-35eb-96b2-4f18398328bf | -6.65948 | -42.81688 | 2025-10-04 12:17:00 | TERRA_M-T | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 669deac2-d806-3bd4-90ca-cbf62a4b702e | -7.04971 | -45.79099 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| d9abfcea-b1a6-3849-b715-a0ea2fbd146b | -7.70765 | -46.22308 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 71189a2f-bfd1-3b1e-a530-167b0d9d45ed | -7.85798 | -48.19769 | 2025-10-04 12:17:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 62632c58-afe2-3afc-aed3-415ae13b810c | -7.044 | -42.76677 | 2025-10-04 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 53.9 |
| f242d7be-3269-3bc6-b2f5-49018de31e89 | -6.17499 | -43.9282 | 2025-10-04 12:17:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9234d20f-18ea-3753-91be-2f4720bf7be3 | -9.10361 | -44.40274 | 2025-10-04 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c9185618-be89-3a03-bc46-8c9fd2c0a9dd | -8.52596 | -47.20594 | 2025-10-04 12:17:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 63a6187f-c4c7-3705-b13f-362849898321 | -6.41227 | -43.83501 | 2025-10-04 12:17:00 | TERRA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c943f8fe-1fc6-3497-aed2-229cf09ced77 | -7.10957 | -45.09396 | 2025-10-04 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7bf86b02-fd02-36f0-a723-ff5238dd90e8 | -3.95657 | -44.2054 | 2025-10-04 12:17:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4f3e147c-9f88-3015-bca5-581a1bc264ac | -8.90014 | -46.06171 | 2025-10-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 198f7526-08bc-3718-bcc1-b7a035e0ec5a | -6.76965 | -44.81858 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4268ff87-0812-3a65-baf2-49c8815b5ff2 | -6.63219 | -42.4077 | 2025-10-04 12:17:00 | TERRA_M-T | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| e0d80de9-9148-3ecd-9b12-17a0fc932ffa | -6.09333 | -43.4817 | 2025-10-04 12:17:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0c6c2901-58f2-3ada-9bf0-d7480828c05d | -3.45345 | -43.34585 | 2025-10-04 12:17:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 9cc09df2-55dd-34cb-acd1-0ece94faeb35 | -8.84421 | -46.85069 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5f5c6e72-5f76-3fee-b534-ab0686a4731b | -9.11361 | -44.40386 | 2025-10-04 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 144bfd07-2a07-3c9b-8ba4-3e0858ccaa49 | -8.17971 | -44.13614 | 2025-10-04 12:17:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 8578791e-a853-378a-8934-2b01be88b2d8 | -8.90146 | -46.05217 | 2025-10-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 4996230a-01dd-3da4-ac94-4b450d6cf2e4 | -8.16929 | -46.9948 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8af9f48a-2064-3617-9950-c5193c1d0752 | -6.64551 | -42.80938 | 2025-10-04 12:17:00 | TERRA_M-T | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| f60ce64f-2585-3633-af32-e4318a28a9e2 | -7.36863 | -45.5553 | 2025-10-04 12:17:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7a23cc3f-cf78-3be7-9d0b-1ad62676a290 | -6.4369 | -44.45815 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d4df98a9-3b6e-3ca9-9e8b-ce967321dac0 | -8.54589 | -47.26955 | 2025-10-04 12:17:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2cbe4eac-6105-3621-9503-73a5b229dcbd | -8.85962 | -46.74235 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 265ad783-7fac-32ad-b1eb-b3805ba59219 | -5.7225 | -42.68128 | 2025-10-04 12:17:00 | TERRA_M-T | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 8cd42ce0-18bc-3fbc-9658-75c75ee416f4 | -7.75226 | -46.30085 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 06cbed7d-76ae-3f86-9085-8dbc13e79973 | -8.25364 | -47.0494 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| dd4797a8-b3c5-3e17-bb7b-4c8f91d29871 | -5.90363 | -42.53681 | 2025-10-04 12:17:00 | TERRA_M-T | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 483b0507-296e-3a57-829e-4939a41d4775 | -6.36309 | -43.89762 | 2025-10-04 12:17:00 | TERRA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| feba7243-bfa5-370b-8904-bdb581381027 | -7.80587 | -42.54544 | 2025-10-04 12:17:00 | TERRA_M-T | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 56.7 |
| 6bf6d068-391e-32ae-add2-0c2204c6beac | -7.77789 | -46.24834 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 75d1453e-932a-372b-a55f-9a0d5015e81e | -7.72549 | -46.29069 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5fc88f56-78b5-313f-8106-c098b5da788f | -8.17813 | -44.14788 | 2025-10-04 12:17:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 8c8e5251-03d2-32e8-9e13-5936f338206d | -7.26893 | -45.47655 | 2025-10-04 12:17:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 20a28518-6a6f-3a72-b0c7-bb8e8e708b46 | -7.55005 | -42.40236 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 379e0c5c-a80f-3988-80d3-b1185bb4727b | -7.29082 | -46.04088 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e5489f5c-6e44-3fa1-8a5b-764570b2452e | -8.25491 | -47.04052 | 2025-10-04 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 416f3826-ab22-38c6-ad6e-62cb32948b25 | -7.86557 | -48.208 | 2025-10-04 12:17:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| ca34964b-dc96-3eb0-b4b5-3b9ad280d3db | -6.64739 | -42.79569 | 2025-10-04 12:17:00 | TERRA_M-T | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 7c7862a6-c6c8-3f30-a11c-755d77c83f23 | -6.27061 | -42.45389 | 2025-10-04 12:17:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 14c00dbc-c2e7-3441-9242-eb5808bf8c17 | -6.6027 | -44.30812 | 2025-10-04 12:17:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1958e67e-168a-3c7c-bc8d-cdd475306e26 | -7.80546 | -42.55116 | 2025-10-04 12:17:00 | TERRA_M-T | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| eb7fe8a3-49b5-34c2-bcb8-3c4ba6c88ffd | -4.43957 | -43.24368 | 2025-10-04 12:17:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 78669be9-d35f-3722-ae5c-a58d81f4b10e | -7.4785 | -43.03592 | 2025-10-04 12:17:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| d295c6b8-9280-3623-a3a9-1479c98d374c | -7.45296 | -47.03444 | 2025-10-04 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b528c3c8-68f7-3f93-91a8-20906b9e18cb | -8.13513 | -44.08865 | 2025-10-04 12:17:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0959910e-a8dd-3acb-8af9-b27a47defba4 | -8.55419 | -47.65086 | 2025-10-04 12:17:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1a81382c-d348-3a3e-b7ac-b2eca0b2abb1 | -6.36063 | -41.61882 | 2025-10-04 12:17:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 43f28926-6e5c-3d0c-8342-f3a0c7d853f9 | -4.95761 | -45.0766 | 2025-10-04 12:17:00 | TERRA_M-T | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9abcab7f-71f6-3851-b0af-dd88b269c6b5 | -8.04994 | -44.8037 | 2025-10-04 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b075f10b-eff9-38b7-9aa3-70baa28fcf8f | -7.77801 | -44.1629 | 2025-10-04 12:17:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1635c5c6-e7df-32cf-acde-9220cf0602f5 | -5.53562 | -43.22204 | 2025-10-04 12:17:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5372c459-10a9-3f4a-a1df-1dd1d2b15ee7 | -8.1713 | -44.12277 | 2025-10-04 12:17:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d020b08e-b3c3-3ac2-b00b-10db086a95e4 | -6.15279 | -44.61849 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 9696517e-29ea-3aa5-9590-ce3ea9c95069 | -8.27524 | -50.25618 | 2025-10-04 12:17:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 57e596e1-77f5-31f0-815a-5a92b16632af | -8.8609 | -46.73332 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4aef89d9-bc02-3d86-85cf-82b78ffd081e | -6.88132 | -47.23867 | 2025-10-04 12:17:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 70e843b8-c230-3fe6-8478-39d467a990bc | -6.17652 | -43.91702 | 2025-10-04 12:17:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 3244273e-5987-3255-8d4a-96b04225fd0c | -7.04936 | -43.21598 | 2025-10-04 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| df05984a-6732-3abd-85f6-f63a755e6385 | -6.28994 | -44.05259 | 2025-10-04 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bd353538-8203-346d-9cac-d26a23e92aae | -6.35292 | -43.44883 | 2025-10-04 12:17:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b180604b-e21c-377c-a70f-00e8a11562d9 | -8.27684 | -50.24532 | 2025-10-04 12:17:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e36cbbe7-ebc1-3523-bae5-84e1673ccc9d | -6.85975 | -43.9252 | 2025-10-04 12:17:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a0c69652-6fbb-3131-83d2-9e48d91b898e | -6.29808 | -44.44361 | 2025-10-04 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 08eaa083-1557-3770-8a2b-aaebb98337f6 | -3.33633 | -44.09826 | 2025-10-04 12:17:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 114a1b68-2cb2-3368-b851-49f0bc510454 | -6.18487 | -43.92958 | 2025-10-04 12:17:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 578114f0-87c6-37c7-add0-b6b7520da2ea | -5.73325 | -42.68275 | 2025-10-04 12:17:00 | TERRA_M-T | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 275981de-6750-315a-bd08-0be93ff2e047 | -8.51198 | -44.76163 | 2025-10-04 12:17:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 26a16f10-95f6-3a36-b45a-56dc3284a53b | -8.59529 | -46.26768 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 03c63101-447f-3821-b3ef-6f3af2f3f682 | -3.95513 | -44.21556 | 2025-10-04 12:17:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a5e93b37-1f44-3c5c-8471-d37f563fb715 | -7.70636 | -46.23225 | 2025-10-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 818d5b16-6f1b-394b-a4d8-155758f21212 | -6.60419 | -44.29733 | 2025-10-04 12:17:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |


[Clique aqui para ver as próximas entradas](README138.md)
