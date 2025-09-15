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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7254e85f-8261-3610-b654-bcbeb085911b | -16.65309 | -49.43609 | 2025-09-15 12:59:00 | TERRA_M-T | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 746c5992-93d9-34f1-8d75-e9410388824b | -17.73784 | -49.08369 | 2025-09-15 12:59:00 | TERRA_M-T | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 50638603-d19e-3630-bce9-dbe2457b4c04 | -20.52551 | -55.63365 | 2025-09-15 12:59:00 | TERRA_M-T | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| aed45b9b-bd0f-3197-ac9b-01babe440e03 | -21.56001 | -49.84117 | 2025-09-15 12:59:00 | TERRA_M-T | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.0 |
| c8d8185f-7af5-301d-86ab-434cac90bf21 | -16.0092 | -59.41483 | 2025-09-15 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9ab60507-ad3a-3d01-8b6d-567d3d4e68fe | -15.86316 | -59.4054 | 2025-09-15 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 68a89fa5-ced2-35f2-abd1-12fe43be757a | -16.0237 | -59.44275 | 2025-09-15 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fa85c94d-45b9-3a38-b0ab-be7db7a887d0 | -23.84226 | -51.79831 | 2025-09-15 12:59:00 | TERRA_M-T | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 626350a5-19f2-3aca-8020-e8600836540c | -15.77796 | -53.46263 | 2025-09-15 12:59:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 401e8b16-6f24-3b62-8c03-240d5ae265db | -16.03617 | -47.59793 | 2025-09-15 12:59:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 285.6 |
| 57dc189c-29d4-3267-935f-6eef61916592 | -21.56731 | -49.83487 | 2025-09-15 12:59:00 | TERRA_M-T | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.8 |
| 1d59ecee-a25a-3308-bb85-f647763a7beb | -16.04016 | -47.55563 | 2025-09-15 12:59:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 942.2 |
| 1d1d0919-ab0b-3796-90b3-405e1c9d7608 | -15.80235 | -52.18122 | 2025-09-15 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 606696e6-3780-3a45-839a-25adfac1ad51 | -15.90186 | -49.99444 | 2025-09-15 12:59:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 027efc65-1df9-30b7-8f5b-3d372660cdfe | -16.68138 | -49.75261 | 2025-09-15 12:59:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| f4df19c3-77de-3a6c-af81-019d73dca0b5 | -16.04062 | -47.56068 | 2025-09-15 12:59:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 833.9 |
| 4a68df34-22e4-35b5-8c83-1aacb5db7aba | -15.90288 | -50.00085 | 2025-09-15 12:59:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 60aa3f26-449e-32bd-9455-3f1c8bc8dd15 | -16.15979 | -59.08773 | 2025-09-15 12:59:00 | TERRA_M-T | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| dc7874a0-f869-3364-8103-434f74eaa8be | -16.01752 | -59.42262 | 2025-09-15 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8153aa88-d8de-3515-9a50-9921cfe42c72 | -15.74008 | -56.23869 | 2025-09-15 12:59:00 | TERRA_M-T | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a8937240-12ef-313a-8d58-10f7e9572a6f | -16.68325 | -49.74575 | 2025-09-15 12:59:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 63936230-efa0-3ffc-8fa9-c377207e44d3 | -16.70008 | -54.96172 | 2025-09-15 12:59:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| cd4031b9-04a6-32d5-b529-edb41023d944 | -16.00781 | -59.42422 | 2025-09-15 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ba91d452-968f-3bb8-b453-1f09c676fb69 | -16.6784 | -49.78299 | 2025-09-15 12:59:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 2f81d3cd-c382-3a6f-b72f-0a8d8d38d1df | -16.01611 | -59.432 | 2025-09-15 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 13ce22b3-fdf1-324e-9a45-7e5d379ade75 | -16.03691 | -47.60294 | 2025-09-15 12:59:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 80f816ac-33f2-3e4c-91a3-3b04343ada2c | -21.84385 | -52.6768 | 2025-09-15 12:59:00 | TERRA_M-T | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 7a2c0124-3477-3bac-949e-0f6c6300ce3a | -16.67993 | -49.77724 | 2025-09-15 12:59:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 9d799e8a-3148-3309-8915-86d47447cdea | -15.74142 | -56.22858 | 2025-09-15 12:59:00 | TERRA_M-T | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7f6849f0-45e3-3049-a0fa-57c0eaae6d43 | -16.16871 | -59.0891 | 2025-09-15 12:59:00 | TERRA_M-T | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| ab517b13-cc84-3737-93e2-e4e194233fd9 | -17.74555 | -49.0791 | 2025-09-15 12:59:00 | TERRA_M-T | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 5e3cad9d-e5e7-3d64-946d-0da4a751ab67 | -18.7551 | -44.462 | 2025-09-15 13:00:00 | GOES-19 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 11fd2e83-1efe-304d-89ba-198403bbef4f | -11.6434 | -46.591 | 2025-09-15 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 009b5f76-6354-372a-abea-7c168b434e0a | -6.1881 | -41.1855 | 2025-09-15 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 339.9 |
| 4b61d0d3-2baa-3263-a414-ada7bcc4942e | -8.9601 | -45.7912 | 2025-09-15 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| b8400498-7424-34c8-bd42-baa5312278b8 | -14.8218 | -51.6362 | 2025-09-15 13:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 128.8 |
| f71b7e03-fa71-3f63-b2e8-3529e702dc0c | -8.9604 | -45.7686 | 2025-09-15 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 8f8c1393-78d8-3bb0-9ffe-4ac6e3546e8c | -11.643 | -46.6136 | 2025-09-15 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| e3ce6c93-53b1-39e7-b4a2-269269868709 | -7.6564 | -49.728 | 2025-09-15 13:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| eef3728f-9369-3e53-be7b-506b6a9c6c3d | -12.1668 | -44.0988 | 2025-09-15 13:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 768eed7b-79ad-36ec-900a-08e3cf9e865f | -6.3372 | -43.1492 | 2025-09-15 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| a785a4df-b200-318d-866c-5688df82c4a0 | -10.075 | -47.1908 | 2025-09-15 13:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| e4d12a7b-9134-3e43-867e-ddba1cc83965 | -6.337 | -43.1727 | 2025-09-15 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d33d41be-7f5f-35ae-9ca7-08a789193010 | -8.4145 | -47.2324 | 2025-09-15 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0d43dfb9-e4ef-388f-9d2e-e7f0a51c2a0a | -8.9784 | -45.8344 | 2025-09-15 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 8aa99258-3fb6-3250-8220-5f16d5b1d2ef | -16.673 | -49.7615 | 2025-09-15 13:00:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6c3fd2bc-6218-3979-b44e-ae7ae4810b99 | -7.6377 | -49.7294 | 2025-09-15 13:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e4f61933-ecc0-3a8d-b399-ee33eaccf0bc | -15.9034 | -49.9996 | 2025-09-15 13:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 708fbea0-e172-3dfd-a4ea-3959a2f63bca | -6.9798 | -44.5529 | 2025-09-15 13:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| c0f4fa50-76f0-3632-82f1-5d7404e12939 | -12.6533 | -47.9507 | 2025-09-15 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 40b512dc-871b-3418-839d-d2521df6b539 | -11.791 | -50.5021 | 2025-09-15 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ed4bd19a-184d-3bb4-be2c-e82779b16245 | -6.356 | -43.1476 | 2025-09-15 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| bf90b1c2-f94e-3912-b3c6-93e9af67fce7 | -12.7879 | -47.9318 | 2025-09-15 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b888da7e-b418-3bba-81be-ed35d75300b4 | -13.1838 | -47.2929 | 2025-09-15 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 92cbb685-7c55-349e-9901-282a0ce00444 | -7.7025 | -48.8667 | 2025-09-15 13:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 236.0 |
| 34bfb386-1ea1-3363-a44a-a4fbbbb8c8dc | -11.81 | -50.4999 | 2025-09-15 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| bccc33d8-eecf-372f-9df3-76df44eb8f43 | -10.0754 | -47.1686 | 2025-09-15 13:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 146.4 |
| e165f9fb-03a4-3837-b7ca-e4c1ca014096 | -6.1695 | -41.1629 | 2025-09-15 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 38338b12-7bdb-3167-9b05-a26c69f23b2f | -5.7363 | -43.1981 | 2025-09-15 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 1db0285b-ead9-3a0b-9851-2a46b1db2f21 | -6.1693 | -41.1872 | 2025-09-15 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 448.0 |
| 64c98d0c-49ee-3051-9876-0034edff0b6d | -10.9639 | -47.3737 | 2025-09-15 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a80993cb-a677-34ae-a624-f48692757699 | -6.3558 | -43.1711 | 2025-09-15 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d73c958b-1463-3c94-bbcf-f4be0b5b41ae | -12.1663 | -44.1224 | 2025-09-15 13:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| bad210ab-968e-3951-9b37-52ab3df528f1 | -10.9452 | -47.3538 | 2025-09-15 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f65b64de-3d5c-3a23-aec4-8e9efd35a893 | -8.9412 | -45.7933 | 2025-09-15 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 15284439-fc0f-3ef7-bc0f-cd7537f8c2a6 | -14.5168 | -47.3304 | 2025-09-15 13:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 6b2186c9-c750-3ff3-ad72-0724abcbbf37 | -12.8404 | -47.1417 | 2025-09-15 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 192.1 |
| d7677746-bd78-3254-82e0-edbe811a7cdf | -11.6622 | -46.611 | 2025-09-15 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| cc54fee3-d9e4-34bd-9c38-347140fff651 | -12.8212 | -47.1445 | 2025-09-15 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 72d6105a-bb90-3bd9-afe7-95243ab6cc63 | -6.1693 | -41.1872 | 2025-09-15 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 332.1 |
| cf10b12f-9d49-3e1d-b2a7-4f444abd8fe5 | -7.3057 | -43.9699 | 2025-09-15 13:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| a8ec7d75-fd5c-3e43-bc5f-451ba46e952d | -8.9604 | -45.7686 | 2025-09-15 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 400.2 |
| 66cb75f1-2198-305b-9e05-79aab20c2dbc | -11.6626 | -46.5884 | 2025-09-15 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e039f775-14c6-3153-9f75-527c361bb0a5 | -6.9798 | -44.5529 | 2025-09-15 13:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ddbece53-7f0f-38ab-87d1-bb11068b642c | -6.1695 | -41.1629 | 2025-09-15 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| 678ae359-6b2a-3d75-8108-0966aaef5b43 | -12.6764 | -47.725 | 2025-09-15 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 6a3e70a0-4a08-3f10-b55d-f23bc88ddb79 | -10.0754 | -47.1686 | 2025-09-15 13:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| ea20f1ff-5d1d-378b-8361-59e2aa6505d1 | -6.1881 | -41.1855 | 2025-09-15 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 269.1 |
| e0530d4c-89e6-3eed-95e0-96663e4677e2 | -7.9634 | -45.6449 | 2025-09-15 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 01e8c67b-5288-353a-9040-06fe9720e3d6 | -12.9599 | -47.974 | 2025-09-15 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3a6b1956-34b0-3f5f-b51c-bc164535b8ce | -12.1668 | -44.0988 | 2025-09-15 13:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| b7f00990-c6b7-3751-a438-a08859d25317 | -6.3558 | -43.1711 | 2025-09-15 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 2306ef01-bbf2-37c1-b266-f08ba853b376 | -7.676 | -44.4879 | 2025-09-15 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| dcb5ce55-be41-3089-87cb-54a1aaf3d1cb | -5.8399 | -44.1642 | 2025-09-15 13:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 32770b53-43eb-37ce-a502-014d1da6dd37 | -8.5947 | -46.3471 | 2025-09-15 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 4a1e8904-3803-3750-a67f-4cd80e6dc242 | -18.7551 | -44.462 | 2025-09-15 13:10:00 | GOES-19 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 8690a6f7-bd06-3d11-b58f-4a0ca621755e | -8.9784 | -45.8344 | 2025-09-15 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a95ada57-77e7-3028-ad47-dd8325c2e80b | -8.9412 | -45.7933 | 2025-09-15 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 167.6 |
| ab61fe12-d6b2-347f-829c-74a9f68ae8d0 | -6.337 | -43.1727 | 2025-09-15 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 5436f35e-c69c-3504-8019-d182786f6703 | -11.6622 | -46.611 | 2025-09-15 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| f8be01f1-3361-30bf-8191-72b9f76b2e62 | -7.306 | -43.9467 | 2025-09-15 13:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 96f0d069-fc35-32aa-9efa-8dae5f601863 | -12.7879 | -47.9318 | 2025-09-15 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 11f1facc-1f87-3c6e-9d86-746b4d239e0d | -16.673 | -49.7615 | 2025-09-15 13:10:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| bdc1b9b4-1770-35f1-a98f-6e299ef728be | -14.5163 | -47.3531 | 2025-09-15 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 87.5 |
| aa586758-5d27-3a7d-aec8-dc11e8d7c2c9 | -8.9545 | -46.22 | 2025-09-15 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 378.3 |
| 26c4c6d3-6157-3cde-bd82-92aae0ae990b | -20.9096 | -46.4681 | 2025-09-15 13:10:00 | GOES-19 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 122.4 |
| 70bc9e89-672e-388c-8599-8717489ee0ef | -11.4512 | -50.3483 | 2025-09-15 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 895c2c86-2835-302c-ac8f-48e331af6249 | -14.8218 | -51.6362 | 2025-09-15 13:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 40c64d26-cf63-359b-b2c5-bc6c0fb462e8 | -12.5975 | -45.7251 | 2025-09-15 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2de90835-5ad9-3e55-8dbb-2bb945dfc889 | -8.9734 | -46.218 | 2025-09-15 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 302.0 |


[Clique aqui para ver as próximas entradas](README72.md)
