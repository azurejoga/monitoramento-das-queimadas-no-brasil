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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d77cddca-6d73-3c5e-a5f0-861f8901bc57 | -16.7575 | -51.3482 | 2025-09-30 14:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 0a35e902-c9c5-39e1-ab92-3a87f87085f3 | -15.7719 | -43.6714 | 2025-09-30 14:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1227.4 |
| 838e2ddc-ceb8-32af-918c-2a03f8c4e4eb | -9.4005 | -54.7186 | 2025-09-30 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 53434f9d-ab80-379d-ac73-bd5d221b37ca | -7.7624 | -46.7834 | 2025-09-30 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ae399601-8c44-3cd8-988a-6d71c14d3afb | -5.8144 | -42.8637 | 2025-09-30 14:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 2b3137f8-471c-3d63-a4a9-883aefb764c9 | -18.2171 | -53.3392 | 2025-09-30 14:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3dc5e55a-e7ed-37a5-b9e7-fd27bbe72f24 | -7.9194 | -44.6016 | 2025-09-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 07ad5912-0651-392d-a5f5-c0980bb7928e | -8.5407 | -44.6745 | 2025-09-30 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| c6dec407-ce1d-3e6d-8394-bbca888fda75 | -9.7681 | -46.1519 | 2025-09-30 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 205.1 |
| 101798ca-2a0f-33a5-8b42-d63a50f6fde5 | -7.4131 | -44.4443 | 2025-09-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 1c70903a-e129-3953-afd6-804c67ae3eab | -11.7537 | -46.8461 | 2025-09-30 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 85f08dc2-477c-36a1-9a35-c94216b8117a | -7.4958 | -45.4402 | 2025-09-30 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7dedddcf-e666-3601-a2f9-ec5129f04fb5 | -12.4055 | -50.1924 | 2025-09-30 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| df7337e3-c891-311e-9e39-4a4835120262 | -5.7413 | -42.6576 | 2025-09-30 14:00:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| bfdf3238-fe76-36a0-9e94-62afa1cb646a | -5.475 | -43.0774 | 2025-09-30 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 3d07e8a0-842e-3731-b5f1-783c0f31a813 | -5.9004 | -43.6976 | 2025-09-30 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 4ec3ef72-4359-34df-aad2-77508d6d7827 | -7.8538 | -46.9969 | 2025-09-30 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| d5065c65-d0e6-397a-bde5-c1fea160b0de | -8.8516 | -51.6998 | 2025-09-30 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 57e47ff8-ef81-30e3-b091-586c361d1a92 | -6.0623 | -42.466 | 2025-09-30 14:00:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 6d9846b2-70fa-3f40-8b46-1ff85fc43cf9 | -10.1042 | -47.8072 | 2025-09-30 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 70867a72-6c2b-3b6e-8872-155df9536b62 | -11.071 | -47.8262 | 2025-09-30 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 11f1416c-5976-3833-8ddd-2cb91d902a20 | -9.1246 | -47.6476 | 2025-09-30 14:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 569ec56c-d4c0-3b32-91c0-e771b4538702 | -17.7149 | -46.6631 | 2025-09-30 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 116.7 |
| d54fc695-f045-3af7-a34f-310894aec1b7 | -15.9273 | -46.2101 | 2025-09-30 14:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 46ec8266-b89f-34c0-aca7-1abe4130469a | -14.5141 | -48.4299 | 2025-09-30 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 111.4 |
| ed19049c-4fc8-3779-810a-8684b479f75e | -15.758 | -54.6793 | 2025-09-30 14:10:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 818ef652-7dca-327a-8303-5de5358d52b0 | -6.0978 | -42.6758 | 2025-09-30 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 062f3fa8-0876-350b-bbec-679188786d5a | -8.541 | -44.6515 | 2025-09-30 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 24afbbcd-020c-320f-8663-bd0b0711d87a | -10.1042 | -47.8072 | 2025-09-30 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 901eb8db-dad8-375e-8ff0-d0de6935b4e1 | -6.7168 | -44.5758 | 2025-09-30 14:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 2fa9f5dc-f746-3e1f-9eeb-cc616f385a2f | -18.2171 | -53.3392 | 2025-09-30 14:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 134.4 |
| f646eb81-4dcc-3f86-97e5-aa817b1e4b6d | -14.7367 | -45.2255 | 2025-09-30 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 426.2 |
| ca01a4b3-97cc-3049-a935-cb859419839d | -9.9581 | -43.5987 | 2025-09-30 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c7155bf4-4eb0-3808-bb83-40af0319f94b | -15.1684 | -52.8453 | 2025-09-30 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5af3becb-280d-389b-bb7e-20aa8903110d | -7.938 | -44.6226 | 2025-09-30 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 3cd7476e-0a01-3226-9a48-07e85a3a5799 | -14.7166 | -45.2525 | 2025-09-30 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 370.2 |
| 9c021a73-b546-3dff-b252-f632a134957c | -14.6603 | -46.9663 | 2025-09-30 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 289.2 |
| 50db5180-1f07-3bde-81c3-942997d8000c | -7.2999 | -42.8486 | 2025-09-30 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 5e8be522-99c6-3cf6-ad31-35300bd17cef | -7.4414 | -46.9888 | 2025-09-30 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 2c5fab13-3199-38fd-9159-83b5b11d47be | -6.098 | -42.6521 | 2025-09-30 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| c9e39431-260d-3015-8589-42c151516bca | -15.7719 | -43.6714 | 2025-09-30 14:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1091.9 |
| 9fbc02f2-0cd3-3bc7-9a18-c23ba2d6bd55 | -11.2707 | -47.2236 | 2025-09-30 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 55ed43f3-23b8-35cf-8b22-b367046cdef4 | -9.1434 | -47.6457 | 2025-09-30 14:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f7393438-e863-3158-bbdd-18b0709f7a05 | -9.8845 | -45.9576 | 2025-09-30 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 240.7 |
| 777cabf1-02b2-3a99-be2d-00b4939187b3 | -11.1944 | -47.2334 | 2025-09-30 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| cb22524a-d719-3855-aa95-668b090d15c7 | -5.7601 | -42.6561 | 2025-09-30 14:10:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 84373228-65ac-30d7-9e7b-2eaf5fd9a367 | -12.4246 | -50.19 | 2025-09-30 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 185.9 |
| ccde1914-b293-3b49-97a0-58ed6f04e323 | -8.5829 | -47.3046 | 2025-09-30 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 597a611d-de2c-3bdd-8370-6afdc3538cd8 | -12.7018 | -45.2947 | 2025-09-30 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 2e717058-8b4e-393d-8553-0e880859f92d | -9.0685 | -47.6093 | 2025-09-30 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 42e458ee-2c40-3b19-8ec1-d6cb3815db38 | -12.8823 | -46.9554 | 2025-09-30 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| baef5712-56f8-366c-a019-ac42366b01fc | -5.8615 | -45.9551 | 2025-09-30 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 241.5 |
| b120cdef-57a3-3de4-a288-b37f5d7d22dd | -6.504 | -45.2312 | 2025-09-30 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| dc5fcab5-9d92-3c76-b2f0-318503d90580 | -9.8658 | -45.9372 | 2025-09-30 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 01b9e107-ba47-34c2-86fd-2c41ffe9fda2 | -7.9191 | -44.6245 | 2025-09-30 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 1f281d5e-0da2-3e2d-91e2-a31ab1e377d3 | -5.8612 | -43.8858 | 2025-09-30 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1c31d310-c1de-359d-b529-2c68af5ea708 | -6.5227 | -45.2297 | 2025-09-30 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 255.3 |
| aef2b214-7c0d-3c49-806a-4d3004f48362 | -15.919 | -59.4925 | 2025-09-30 14:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 514cde6d-4736-3b1d-ba75-153349274df5 | -7.0481 | -45.1856 | 2025-09-30 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 0754b18b-59e5-373e-a1b0-703453f70dd5 | -22.5205 | -44.597 | 2025-09-30 14:10:00 | GOES-19 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 209.8 |
| 7df0ab2e-4e60-391d-86d8-a14295c73663 | -13.2161 | -50.9286 | 2025-09-30 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 62a7d372-60e4-3336-ac14-4d18025d66c3 | -10.6419 | -48.6021 | 2025-09-30 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| be5bd79c-546e-3f7b-88d3-e9e1e8a0e8e7 | -12.7022 | -45.2715 | 2025-09-30 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| a47aa344-041b-306b-984f-9dcaf6d863a2 | -7.0291 | -45.21 | 2025-09-30 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 08df8ca1-0756-32bb-aac5-0328fe507523 | -11.7023 | -44.3113 | 2025-09-30 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| b018023d-96ce-333f-b058-e41a101addb3 | -7.0478 | -45.2083 | 2025-09-30 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 1e943699-3830-3353-ba22-22c5d99c8395 | -5.4565 | -43.0554 | 2025-09-30 14:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| b5cfff05-fdd8-312b-b507-f830dc070caa | -6.523 | -45.207 | 2025-09-30 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 9e94a60a-1a8e-3b11-b2e8-3ed15ee3a509 | -12.2153 | -47.8112 | 2025-09-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 2a926207-043f-3ce0-95d1-d521150cf1f2 | -7.819 | -46.7561 | 2025-09-30 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 209.4 |
| b363b672-dc35-369a-95d1-48e7bc81cf80 | -9.4007 | -54.6984 | 2025-09-30 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 93dec853-06dd-327d-9a3a-d07ac825cf90 | -7.8538 | -46.9969 | 2025-09-30 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c1618449-4775-39cf-ae5f-39e8fc4a8283 | -18.4862 | -44.0191 | 2025-09-30 14:10:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 976fead3-bb7d-335c-93ba-c2d281228fbf | -14.7171 | -45.2291 | 2025-09-30 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 258.6 |
| e120de2a-966f-317d-bdd2-909f53839b0e | -11.8868 | -48.0323 | 2025-09-30 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 71e5f8ce-dac1-36b2-8291-01e67e6e3d8e | -15.2746 | -49.263 | 2025-09-30 14:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 126.3 |
| b8f43b3f-db29-3419-a9ef-d08c670c1d0c | -10.1045 | -47.7851 | 2025-09-30 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 2f4d5a6a-c7ab-3721-bce8-a7f3ce7162a4 | -9.7684 | -46.1293 | 2025-09-30 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e9531028-c427-3837-86c5-582dc8deb4ba | -12.9524 | -48.3963 | 2025-09-30 14:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 34293096-cbb8-3e02-9f98-51a70e67deed | -12.2344 | -47.8086 | 2025-09-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 236.4 |
| b913aae9-9f92-30c6-9a7e-a931c8ac282a | -12.4055 | -50.1924 | 2025-09-30 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 552.9 |
| 319aacdb-ef28-3efd-879d-dcdfffa25722 | -7.115 | -47.785 | 2025-09-30 14:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 330d7c55-8027-3e54-8824-66c54459c9f7 | -7.835 | -46.9986 | 2025-09-30 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| a6e2ca5c-9570-3a51-b30a-a7412d0aedc2 | -12.3867 | -50.1731 | 2025-09-30 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 316.5 |
| b8b633d8-f66c-3667-b499-880d3309d8fa | -5.9192 | -43.6961 | 2025-09-30 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0e5a7bee-069f-3353-b02d-e98d3d90b331 | -5.7413 | -42.6576 | 2025-09-30 14:10:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 43e6da22-0dda-3974-9809-ed3097742107 | -18.1977 | -53.3208 | 2025-09-30 14:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c013a5e2-4669-3601-a8b5-85458ccc957c | -9.9585 | -43.5752 | 2025-09-30 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| cc4cbc22-acb2-3d42-bba4-61a872979351 | -9.0425 | -46.7032 | 2025-09-30 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 37d05038-ab5b-3592-a372-29704f618cc6 | -12.9712 | -48.4158 | 2025-09-30 14:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 06eb1dc0-228c-3cbc-8d61-789e132b2534 | -8.8516 | -51.6998 | 2025-09-30 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 1f09dd9b-5231-3201-ab85-2b5d11cc3e83 | -14.4041 | -47.1454 | 2025-09-30 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 211b8203-dea0-3552-bb7f-bc33cd27e07f | -7.9194 | -44.6016 | 2025-09-30 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a5c42b49-b822-308b-8b8f-9e9e7d5aff69 | -9.0682 | -47.6313 | 2025-09-30 14:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b6c7f416-d464-35be-b716-e1996c460d37 | -16.7575 | -51.3482 | 2025-09-30 14:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| b64a7dfb-9cac-3d39-8603-4e14c5513e7b | -9.8848 | -45.9349 | 2025-09-30 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 184.1 |
| cff0dfd5-e957-3f2d-989b-e5456891d64a | -11.7537 | -46.8461 | 2025-09-30 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 670a129a-dbde-3915-bc27-a752899e9e88 | -7.8188 | -46.7783 | 2025-09-30 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 190.4 |
| e2479e41-c5de-392f-985e-0e7cd219a44c | -11.1546 | -54.126 | 2025-09-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 2e10a417-02d0-3a3d-aa8e-d185e767dd13 | -8.9264 | -51.7146 | 2025-09-30 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |


[Clique aqui para ver as próximas entradas](README120.md)
