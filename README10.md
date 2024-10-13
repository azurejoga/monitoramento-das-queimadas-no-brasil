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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfc04018-932d-3838-96b1-c04908bf0c96 | -4.8992 | -47.67566 | 2024-10-13 00:39:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9a329179-8485-399c-b77e-9592d1d685ec | -4.89761 | -47.66383 | 2024-10-13 00:39:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 44.6 |
| ac345a78-870d-32cb-9556-56d25176a75e | -4.87897 | -45.76923 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| a48f1f85-6c20-312d-9d73-4b9bb99427e2 | -4.87769 | -45.75983 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ccfe25ef-2ae0-3d47-992d-3417ff353edc | -4.86155 | -45.04322 | 2024-10-13 00:39:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 3c72891d-c311-32e3-bdfb-a6444e97d86c | -4.8603 | -45.03424 | 2024-10-13 00:39:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c289e67e-a467-3cb2-b164-b170ace252d4 | -4.8584 | -45.7492 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6cd1aec4-6806-3918-9d42-71c905c9b1ae | -4.85711 | -45.73989 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 63796083-fde9-3bed-9c75-de31319ff409 | -4.85449 | -45.85539 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1485e061-1863-385a-acf1-bae88077c962 | -4.85265 | -45.04449 | 2024-10-13 00:39:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 258b337a-0893-39b8-b08e-af538bea58a2 | -4.85141 | -45.03553 | 2024-10-13 00:39:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 00b27f41-7bf3-35ae-b4e5-3c073d564ae5 | -4.84836 | -47.74996 | 2024-10-13 00:39:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 54433121-fdc4-392b-a0f6-e6d396fa34b4 | -4.84672 | -47.73796 | 2024-10-13 00:39:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4505acb4-6991-30d9-90e8-459f4a17bd6c | -4.8363 | -46.91989 | 2024-10-13 00:39:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d59475df-0a9e-302c-a015-b95457e4e3d0 | -4.82082 | -45.67822 | 2024-10-13 00:39:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f348d431-5497-3918-973f-0ac866407f5f | -4.8193 | -44.07759 | 2024-10-13 00:39:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9f6ad9cf-99f6-3760-879c-236c1ce29de7 | -4.81928 | -46.86773 | 2024-10-13 00:39:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c3403703-03a8-360d-93a6-9e3db73861e4 | -4.79113 | -45.92875 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3a488393-1544-3bf5-972f-d7ee850600fd | -4.69187 | -46.75285 | 2024-10-13 00:39:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 677e0782-dad1-36b9-93cc-e9c7806f4d4f | -4.60751 | -47.33596 | 2024-10-13 00:39:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ce285a7b-a2ad-3b33-ad15-db5e7a890cc5 | -4.48756 | -48.11059 | 2024-10-13 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 00934485-9d6d-3336-845d-61110aac2093 | -4.46838 | -48.12604 | 2024-10-13 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 912c133f-bb04-3ff7-b63f-341c870ac96c | -4.46239 | -44.82406 | 2024-10-13 00:39:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b1e3bba6-c0e6-36b4-832c-b11a42beff82 | -4.41405 | -50.31858 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5654bfbd-3d21-3db2-9543-f6eb5bc4cf52 | -4.41371 | -49.76752 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| aec664a7-6c3d-30cd-813f-c4e9a38815d9 | -4.40799 | -49.7618 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 8f103e30-73fb-388f-98d1-ea0a93d76ad3 | -1.2582 | -47.09042 | 2024-10-13 00:39:00 | TERRA_M-M | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 45f74b18-acf5-30b5-ae80-a83d18e8c019 | -1.43051 | -52.85736 | 2024-10-13 00:39:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| df56927e-4393-3ca0-8b70-7e420cdaf5fa | -1.43233 | -52.85193 | 2024-10-13 00:39:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f6622da9-769a-3ca2-8f8c-d7343b85536c | -1.4358 | -52.87774 | 2024-10-13 00:39:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 62731303-6af5-39d1-9f66-2752d113f002 | -1.66453 | -52.12484 | 2024-10-13 00:39:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 45fbbbc4-25f2-32f5-9d63-f22f835bf212 | -1.66776 | -52.14804 | 2024-10-13 00:39:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 7927d848-0995-38be-b13b-aba91469c7d4 | -2.02669 | -46.92796 | 2024-10-13 00:39:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9b4db87a-d8a1-3d0f-8bcd-79131c91f6f7 | -2.02806 | -46.93787 | 2024-10-13 00:39:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0397a286-2477-3d8b-92c0-1494fdfaf97e | -2.1663 | -48.81476 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8211d299-4c75-3bd2-ab32-50cc98247ed2 | -2.24109 | -46.73549 | 2024-10-13 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ae7ab8b8-1b20-3c19-9430-785a8f99e863 | -2.24849 | -46.73858 | 2024-10-13 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d8ca8b38-29ab-30ee-867a-cee1a0cc4fd7 | -2.43158 | -48.2346 | 2024-10-13 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 299ac092-6134-3799-bf75-dc7bf8e9b345 | -2.43324 | -48.2465 | 2024-10-13 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9fcc3b1b-d5d4-33fd-9cc4-b3a13e74f17e | -2.47699 | -48.19839 | 2024-10-13 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8caeee3a-b778-3a1c-b589-fe758f3bd754 | -2.52333 | -47.26321 | 2024-10-13 00:39:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b54625e1-353c-33a3-9c6a-7d70af9c273d | -2.52475 | -47.27361 | 2024-10-13 00:39:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 9cb49404-3677-34af-bcb3-8c5a9814b159 | -2.52618 | -47.28409 | 2024-10-13 00:39:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8192b21b-c005-3354-b653-2b145ae4fc89 | -2.53291 | -47.26189 | 2024-10-13 00:39:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 36ff1ff1-8508-394f-a202-e3e41c89e66b | -2.53433 | -47.27226 | 2024-10-13 00:39:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 1f837b25-00e6-355e-8bdb-5e02f6061508 | -2.54804 | -48.41024 | 2024-10-13 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 45d11c3a-cf2a-3788-958a-8bdad04b86a4 | -2.61612 | -47.34021 | 2024-10-13 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 48ec3c84-4143-3d74-af35-d8ad1f30e1b6 | -2.61756 | -47.35083 | 2024-10-13 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ec601bfc-0f33-3078-85a9-8c8d4a948d02 | -2.65049 | -51.87746 | 2024-10-13 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| e125e499-a678-395f-bba4-e74a5edfa90c | -2.65366 | -51.90041 | 2024-10-13 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 0dc46024-3e1e-334e-b9f9-0a061115b9b1 | -2.66025 | -51.89298 | 2024-10-13 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 450e64b2-56d7-356a-9920-bccf8eeec6a6 | -2.74854 | -49.51899 | 2024-10-13 00:39:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 82f8808a-b953-30ff-a435-877149ad7d9b | -2.77327 | -49.36551 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| a57945b9-d2ce-351b-91f0-bfb3acc49ada | -2.7833 | -48.7005 | 2024-10-13 00:39:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4fbfaaba-cc74-3999-9aa4-46c95e3c0153 | -2.78539 | -49.29005 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 8995a45f-804c-3979-aa53-b4fd472609b5 | -2.78588 | -49.28433 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9c0e9595-2578-31bf-bb23-8ab6d767110f | -2.78742 | -49.3044 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b08cfdf9-ba08-33f6-93dc-1b76d412f9d5 | -2.7878 | -49.29867 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 219c82da-3ffa-34cf-8e0f-0471db241a1a | -2.78961 | -48.70655 | 2024-10-13 00:39:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| de6a1435-099c-37b1-9a04-a534f8c20f19 | -2.79698 | -49.28276 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f63c905f-0466-3156-b9b3-25f40a4dd764 | -2.79892 | -49.29713 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9974e151-3a46-38f5-9fd9-2f314a7f0bdc | -2.99001 | -49.51963 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 72d7d18b-e136-3bd4-81dd-75ddaf1af3bf | -2.99051 | -49.52899 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| df00db87-9dce-3b4e-b0ad-1b062b7e3c25 | -2.99212 | -49.53468 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 67bfb5a2-74e7-3943-9ceb-6c2b8f46a8b8 | -3.04426 | -49.41486 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 77781863-2de3-327b-b55d-8080d6d82e59 | -3.0676 | -54.25309 | 2024-10-13 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 4c565d74-68e9-3066-b044-29fbeda05107 | -3.07306 | -54.24687 | 2024-10-13 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 90edb3b0-3457-3bcf-9ec6-06648e1bde0b | -3.08416 | -54.2505 | 2024-10-13 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| e2238f49-d492-3136-b39b-6c7e45ff8636 | -3.08965 | -54.24452 | 2024-10-13 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 111e6291-17ed-3ed7-85b3-4c2d423a4171 | -3.0956 | -53.01981 | 2024-10-13 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| d8d16010-f278-3420-9bec-00951330d160 | -3.09763 | -53.02477 | 2024-10-13 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 181.3 |
| 41e11339-b1f5-365a-90a0-767a6baf3503 | -3.09934 | -53.04854 | 2024-10-13 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 412.0 |
| 8755ebf5-b015-3f0c-88f0-fe0416990304 | -3.10159 | -53.05349 | 2024-10-13 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 271.6 |
| 01b5f291-1187-3957-81a5-4874c1018d24 | -3.15107 | -50.37144 | 2024-10-13 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 06694f67-c29a-3c2b-aa59-a601da82643d | -3.16312 | -50.46054 | 2024-10-13 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 124f280b-47e0-328e-8894-3b2c53c260ee | -3.16555 | -50.47855 | 2024-10-13 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 6831b2d7-0c72-31d8-9af8-7cd4f13bc318 | -3.17543 | -50.45894 | 2024-10-13 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 251.3 |
| 8fae888a-9662-3cdf-82e0-46aa228abafe | -3.17787 | -50.47686 | 2024-10-13 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ea775812-765d-3f24-b590-2d6f4606afd4 | -3.18776 | -50.45745 | 2024-10-13 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 662f0808-5c52-37af-a1d8-fcc9b299b795 | -3.19019 | -50.47521 | 2024-10-13 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| ec544d3a-8150-3257-bc44-4df4b9b004e6 | -3.38634 | -52.45225 | 2024-10-13 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 4cc5ebd1-b7b2-3394-b88c-dbc55a6eb724 | -1.25682 | -47.08053 | 2024-10-13 00:39:00 | TERRA_M-M | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| ced687ea-d887-3811-96a5-d7f0720f4ed3 | 0.74861 | -50.87557 | 2024-10-13 00:41:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 63f41123-6211-33fc-8be8-b3f81fa423f6 | 0.75702 | -50.86638 | 2024-10-13 00:41:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 019ab649-3198-35ce-82d1-60780fe9fd7e | -1.733 | -54.173 | 2024-10-13 00:45:16 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| ba5df9df-9f77-3e15-87c0-cd16fee4c0a6 | -1.9486 | -56.4692 | 2024-10-13 00:45:17 | GOES-16 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 749efa06-ee9e-39c9-9df7-b9c453e6f64e | -1.9486 | -56.4496 | 2024-10-13 00:45:17 | GOES-16 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| dfbf8eee-3777-3486-8a95-e4a492166d17 | -2.1692 | -48.8322 | 2024-10-13 00:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| fa10ea2b-77d6-3f9f-baf2-785a028afc63 | -2.1693 | -48.8108 | 2024-10-13 00:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 38593cd3-0d5e-373b-9c55-144831ad90a8 | -3.0731 | -54.2473 | 2024-10-13 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 052839dd-64c0-3eab-acdb-1be78ba12b28 | -3.0915 | -54.2469 | 2024-10-13 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b0a2c1c9-76fc-386d-8bbe-c6f8cf0c7e24 | -3.0956 | -53.0559 | 2024-10-13 00:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 0de8f11a-f60c-3b38-bf71-8dbd9aec6642 | -3.0957 | -53.0355 | 2024-10-13 00:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 288.6 |
| e4e60bd1-48c6-3c69-966c-87f470285852 | -3.0957 | -53.0152 | 2024-10-13 00:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ecbf6beb-f0e3-3627-ab46-08e58c124e02 | -3.114 | -53.0554 | 2024-10-13 00:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 34ea0ef4-d6c7-39ef-b11f-cc7df27b7507 | -3.1141 | -53.0351 | 2024-10-13 00:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 6cb7ff33-fdb1-3dfe-bea0-0fc08dc8c2cf | -3.1791 | -50.476 | 2024-10-13 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 57c8ee78-69a9-3254-b9f2-4310846e5e3e | -3.1792 | -50.4551 | 2024-10-13 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 38970a36-6e5a-34a4-b451-ccba4652bb86 | -3.1976 | -50.4545 | 2024-10-13 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 144398c9-fc89-3ceb-abd6-17903b3daeaf | -3.7128 | -40.7102 | 2024-10-13 00:45:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 79.6 |


[Clique aqui para ver as próximas entradas](README11.md)
