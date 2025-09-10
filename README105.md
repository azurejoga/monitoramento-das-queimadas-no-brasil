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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f5e0933-1cf1-3aa2-b812-166922d2b5f9 | -9.3437 | -46.7603 | 2025-09-10 10:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.0 |
| df879f17-33e2-3aa1-87da-51f4819fd273 | -11.446 | -43.6461 | 2025-09-10 10:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| c079787e-3cee-3911-a917-c8d8c07fe377 | -11.4465 | -43.6224 | 2025-09-10 10:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 1d8f3375-73b1-326c-ab6f-b09ed28def23 | -18.0412 | -47.1509 | 2025-09-10 10:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 191.4 |
| d473d1a0-a86c-38ea-8a80-b55edbd0aa40 | -8.0416 | -48.6656 | 2025-09-10 10:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 774646a6-430b-3fb9-800c-93dfa47602f3 | -8.0416 | -48.6656 | 2025-09-10 10:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e26f646d-926a-3906-8eb1-ba31599c486c | -18.0412 | -47.1509 | 2025-09-10 10:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 8f796e67-fe30-3c69-a3bb-e67cc082d456 | -9.3437 | -46.7603 | 2025-09-10 10:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 173.9 |
| fabab25f-2a4a-3691-a91c-34ff1a9d7fbf | -11.4515 | -50.3268 | 2025-09-10 11:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 307107a6-a943-3ab1-854b-5ac5c576cd3f | -5.6788 | -43.3425 | 2025-09-10 11:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| de155ee4-9f38-345b-a8e1-af8bbb411137 | -8.0416 | -48.6656 | 2025-09-10 11:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 85.5 |
| a0dcff55-89c4-34a1-8792-b0c4d94fc87e | -5.66 | -43.344 | 2025-09-10 11:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 89b738a0-7835-3305-a6b3-9031e0f3e3ec | -9.3437 | -46.7603 | 2025-09-10 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 77855b38-5d7e-3230-9b83-3207060cf3c7 | -8.0416 | -48.6656 | 2025-09-10 11:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c15d01e8-f6a4-3757-b48c-fbe8558d0fde | -6.8897 | -47.8897 | 2025-09-10 11:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d0dbfe5d-2e08-31a6-9afd-1826035c0439 | -9.3437 | -46.7603 | 2025-09-10 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 1890fa96-8cfb-3c3d-b252-8f637d54bbb9 | -5.6788 | -43.3425 | 2025-09-10 11:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 98c5a23a-a719-394c-9a02-ccee1dcb9cbd | -7.35637 | -38.76749 | 2025-09-10 11:17:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 29.0 |
| afc2cd28-708a-3f61-9962-413129d65ea6 | -6.78096 | -39.17727 | 2025-09-10 11:17:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 29e7f9c5-89fc-3dd3-9cc0-aa5154fddd34 | -7.36296 | -38.76208 | 2025-09-10 11:17:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 32809821-6f0c-312c-b841-60a964a105f5 | -6.7776 | -39.17081 | 2025-09-10 11:17:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 65e6d7be-d48b-3e5d-a94c-daec4de12c0f | -5.03557 | -37.78503 | 2025-09-10 11:17:00 | TERRA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 16b43b4a-688a-3fb2-8ac6-4544ae43ef4c | -4.85408 | -38.01478 | 2025-09-10 11:17:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 56377053-fd53-3831-8cf6-f2d41984a524 | -6.77371 | -39.19598 | 2025-09-10 11:17:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 48c7f76b-f68d-3600-b245-a90209cae5bb | -5.56136 | -37.01317 | 2025-09-10 11:17:00 | TERRA_M-M | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 29c8607a-6abc-32ab-b7f2-a044e50bded3 | -13.76077 | -42.10319 | 2025-09-10 11:19:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 8a552f89-1771-3acb-bbb1-11f8b9b78b02 | -15.62265 | -40.15112 | 2025-09-10 11:19:00 | TERRA_M-M | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 69e8f62e-2aff-390b-9dcf-f71c10f6a7b6 | -13.76618 | -42.09812 | 2025-09-10 11:19:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 35.4 |
| 4bed2cab-5f2c-3033-aae8-29f4b3b74544 | -16.34978 | -41.47201 | 2025-09-10 11:19:00 | TERRA_M-M | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 8844755b-ce78-382f-9c27-53b77ac87ecd | -14.20286 | -42.04928 | 2025-09-10 11:19:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 00cec014-988d-3956-a5c5-38554a6edc22 | -11.4515 | -50.3268 | 2025-09-10 11:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e10fa118-23ce-3a0d-b4f6-cdf965d397d7 | -5.6788 | -43.3425 | 2025-09-10 11:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a84b705e-652d-3baa-aa8d-c73146f411f7 | -9.6821 | -46.8791 | 2025-09-10 11:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 44afdff9-0952-3a17-bb0a-0e0293ee80a5 | -8.0414 | -48.6873 | 2025-09-10 11:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 87c37760-63cd-334d-906b-dcb1f4f2f67d | -11.4465 | -43.6224 | 2025-09-10 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 982002d8-6aba-3221-9302-b05b1feb49da | -8.0416 | -48.6656 | 2025-09-10 11:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 4ace54e2-d3d0-351d-b227-5e4ba0b5f877 | -5.66 | -43.344 | 2025-09-10 11:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 38e39899-eacb-3d43-88a9-1526c046d879 | -9.3437 | -46.7603 | 2025-09-10 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 03c8303d-d5e6-3da9-8503-47a2e14e006c | -9.0957 | -46.9648 | 2025-09-10 11:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2bb95ff6-6ec7-3600-8c2f-e9d0f610d4d1 | -11.4657 | -43.6195 | 2025-09-10 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1759e982-d910-3a53-af2a-c6b4507a0fa2 | -12.0307 | -51.0083 | 2025-09-10 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d9861c98-9501-3100-85aa-cbeef9bb0863 | -6.8521 | -47.9143 | 2025-09-10 11:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| d02bab60-6db7-3582-a8f6-7a79229341bd | -12.0501 | -50.9847 | 2025-09-10 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 96e9606e-095f-35a3-af76-5e3ba431c440 | -9.6821 | -46.8791 | 2025-09-10 11:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 264.3 |
| dcbe5995-5e52-3be8-90d4-346367196ecf | -11.4465 | -43.6224 | 2025-09-10 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b074bdd8-0c66-33b7-8a0b-f0d82c3412bb | -11.4657 | -43.6195 | 2025-09-10 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 4207887f-397d-3448-9c1c-ab56e0d8a168 | -10.3334 | -46.3774 | 2025-09-10 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 611781d6-ab43-3929-978a-b35b5ffbf60f | -6.8521 | -47.9143 | 2025-09-10 11:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| df4fdba3-dce2-3d2b-be97-245cdef81277 | -9.152 | -45.5662 | 2025-09-10 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 890e5e1e-18d2-3f86-85ff-018b21638bdd | -8.0414 | -48.6873 | 2025-09-10 11:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3ea74602-a7e2-3718-a721-61d95a864dd0 | -9.6824 | -46.8568 | 2025-09-10 11:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| a6a1a52d-fe0c-3720-960a-ea52e0b8c9f0 | -9.7011 | -46.877 | 2025-09-10 11:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| f1c28a4d-fde8-3ef3-b959-c28f5c26dd51 | -5.6788 | -43.3425 | 2025-09-10 11:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 5c0a852b-3f92-336e-8e2d-20d4232ae667 | -10.1654 | -46.195 | 2025-09-10 11:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 0534043e-ca20-39cc-92e7-4361b24f3bf6 | -11.3905 | -43.5365 | 2025-09-10 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9257ecd7-0fd7-33b3-9c11-282fc65e683d | -8.0416 | -48.6656 | 2025-09-10 11:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 84.6 |
| cf0eb08d-8aa0-3647-a9f6-874f751c03ee | -9.055 | -45.7583 | 2025-09-10 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 11171a30-d54f-36ac-8cef-60951b5d084d | -11.4657 | -43.6195 | 2025-09-10 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 82ee948f-3c91-3b01-bfe9-ca93c23fd5c9 | -8.721 | -45.3181 | 2025-09-10 11:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 2dd0f029-ad3f-362b-a646-86072b6e43ff | -8.0414 | -48.6873 | 2025-09-10 11:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 101.9 |
| c982edd9-f087-3463-91c3-33be118d6d78 | -6.8519 | -47.9361 | 2025-09-10 11:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 25389551-e0c0-3d1d-bbb7-b974f9c276f9 | -12.0501 | -50.9847 | 2025-09-10 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a8e4bc94-12b9-3e58-9621-df6b770ff565 | -15.1374 | -52.4039 | 2025-09-10 11:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| a4ff4470-1011-3ae0-9583-0a984b05342e | -9.3437 | -46.7603 | 2025-09-10 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 81ce5541-8e05-3984-8550-b438f33892ce | -10.1654 | -46.195 | 2025-09-10 11:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| f7494cdc-841a-36d3-97f1-d8391320bc88 | -9.171 | -45.5641 | 2025-09-10 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ca49b8da-86bf-3b27-9a9c-e0430ac832ae | -9.9762 | -50.3121 | 2025-09-10 11:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| ba3b91fa-2a2c-32af-8c3f-b2f1649f5b43 | -7.8648 | -46.0372 | 2025-09-10 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 0ba9a512-3065-3017-95f4-597b276166d6 | -12.0304 | -51.0296 | 2025-09-10 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| ba14e290-9f19-3a57-96ca-a5309f0378ea | -12.0307 | -51.0083 | 2025-09-10 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 191.0 |
| d3de1f08-51ff-3955-b5e2-c394986d3e67 | -11.4648 | -43.6668 | 2025-09-10 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f07779d5-a669-354f-899e-5adb64da8aab | -11.4465 | -43.6224 | 2025-09-10 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 20dc3aa6-975c-3b18-bc2f-d42c194ab27d | -10.3334 | -46.3774 | 2025-09-10 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 5d696f90-5366-37db-b7d9-95ba576ab562 | -11.3905 | -43.5365 | 2025-09-10 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 0f3fb6ce-fc90-3f0b-af20-41f00ecdc7ca | -11.446 | -43.6461 | 2025-09-10 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7e2df956-ff82-3fc5-b108-e160ab089dc5 | -6.8521 | -47.9143 | 2025-09-10 11:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 100b731f-a8d6-3eec-97ef-8ae75ec30d83 | -9.9951 | -50.3102 | 2025-09-10 11:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 87a8573d-131b-32a8-8293-5f8a4eaab741 | -8.0416 | -48.6656 | 2025-09-10 11:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 1746cc5e-5130-30ef-bcc2-19440737adc4 | -10.3882 | -50.5477 | 2025-09-10 11:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 062319dd-5fa7-3fad-a7e9-016edd258329 | -12.0304 | -51.0296 | 2025-09-10 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b3e55206-e0a5-32f4-8ab2-862dc872a71f | -9.3437 | -46.7603 | 2025-09-10 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| e7f7b23f-30bc-330f-a90f-5adcd7503a1f | -10.1654 | -46.195 | 2025-09-10 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 908c8dfc-c604-34d1-a742-5b1dad59de29 | -9.055 | -45.7583 | 2025-09-10 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 77ca2c72-d361-387e-a14d-d3ea8134e412 | -11.4465 | -43.6224 | 2025-09-10 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 90ecf286-5541-3bc2-85db-c5fe1afba1d5 | -8.0416 | -48.6656 | 2025-09-10 11:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 7e9f455f-42c4-3039-9eeb-5546a4067ca8 | -11.4657 | -43.6195 | 2025-09-10 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 430f6275-cafa-3004-bf85-b5430d7abe4f | -7.4155 | -44.2368 | 2025-09-10 11:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 211.1 |
| f1ef111b-8eb2-38c8-941f-817b682f19cf | -9.0232 | -49.7834 | 2025-09-10 11:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 215e3654-a2d6-3a5c-9983-b9bfa9a530b1 | -6.8519 | -47.9361 | 2025-09-10 11:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 6d14d150-f19f-3bbe-bd20-a4e4394db8fa | -7.4845 | -48.2349 | 2025-09-10 11:50:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8103968d-3e60-3f14-b802-3eba312537b4 | -6.8521 | -47.9143 | 2025-09-10 11:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f2cf8911-63ad-3a0d-9d1a-f90c4794fa37 | -11.3905 | -43.5365 | 2025-09-10 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 43210ddc-7499-3989-a49a-3d7bcc4b9605 | -9.042 | -49.7817 | 2025-09-10 11:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 131ba23e-0878-34f8-b4cb-b37ea6b2f166 | -10.165 | -46.2176 | 2025-09-10 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 92deb2a9-155e-372e-883d-2d620cd4eb04 | -11.4648 | -43.6668 | 2025-09-10 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 8349d52b-0a46-3107-81ce-b2d95fb9509a | -15.1374 | -52.4039 | 2025-09-10 11:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6e8750cc-3627-31b6-8d20-24ac2c1ed6bd | -12.0307 | -51.0083 | 2025-09-10 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 27984720-0e20-3475-b6cb-b58e57846413 | -8.0414 | -48.6873 | 2025-09-10 11:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 07266579-e40d-346b-9ade-201d916397c8 | -6.8706 | -47.9347 | 2025-09-10 12:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 8d30d335-0ff6-3aee-ad7f-9e7760cd7558 | -10.3885 | -50.5264 | 2025-09-10 12:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |


[Clique aqui para ver as próximas entradas](README106.md)
