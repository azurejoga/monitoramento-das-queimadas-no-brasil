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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba25e25a-e516-312b-acbd-ea93930d4573 | -8.31157 | -44.12488 | 2024-10-08 03:40:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10bf0d94-fedb-38f4-8bd4-1864d6c83d6e | -8.30973 | -44.10618 | 2024-10-08 03:40:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21193b3e-868d-38cb-878f-f964d04b65db | -8.30462 | -44.10537 | 2024-10-08 03:40:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c15d1c9-b632-38de-92bc-d459723510ea | -8.28162 | -44.09858 | 2024-10-08 03:40:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f69cf787-2939-3d68-83f6-31bb52fea45f | -8.13952 | -44.41502 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ca21cb6-ba00-38f7-9c2d-3fbbbe90aff8 | -8.13948 | -44.413 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce4fef09-bee3-35a6-81f1-536d7f9578c5 | -8.13893 | -44.41823 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 255dd593-2828-33da-9e7d-2498a4c36bb1 | -8.13892 | -44.41622 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3938684-5f46-38e0-ae61-146a3325881c | -8.13835 | -44.41944 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a22620e-da29-30d5-8c16-74763939a60f | -8.13834 | -44.42145 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5f521f6-852c-365c-af70-d42e6d5ef9ad | -8.13778 | -44.42266 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b7fc3d5-a844-3492-a08e-f753f4260e22 | -8.13775 | -44.42467 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14bd7666-0c0b-3b35-ab7f-bf2d01667bfd | -8.13432 | -44.41405 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37b3789a-e2f4-3973-ac89-d696130699ed | -8.13373 | -44.41726 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1020ad5e-42f7-3144-80e2-cb4124cba4de | -8.13371 | -44.41524 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3befdba-5802-3fd2-a47b-ade6b2b18832 | -8.00621 | -44.37321 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0db1507f-7ea6-31db-aed7-828748ea3e90 | -8.00564 | -44.37642 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1aa4392-7af6-343a-baa6-365ecb0a0284 | -8.00392 | -44.38605 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3371b4d-a621-3b29-9406-7b4c035d9a42 | -3.60953 | -44.79102 | 2024-10-08 03:40:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 049fe6f3-66de-31bd-82b3-cef0f2c42286 | -3.60886 | -44.79502 | 2024-10-08 03:40:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac5b933c-1e18-383e-8323-0321d44624df | -3.60378 | -44.79002 | 2024-10-08 03:40:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62176d24-410a-3e27-9b68-691a7e13670b | -4.92668 | -45.65515 | 2024-10-08 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ee34d76-8162-31a2-88f6-69e2d5ed22f1 | -4.92426 | -45.6527 | 2024-10-08 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75114145-9484-3ebc-b9b6-2c16de901167 | -4.92353 | -45.65697 | 2024-10-08 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 292eca11-53f3-3717-93cf-5d79cc3de400 | -4.92082 | -45.65354 | 2024-10-08 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7d265c8-e411-34cf-944d-60564a26c313 | -3.69727 | -45.08505 | 2024-10-08 03:40:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef6c302e-ee96-3e7c-ada1-f6745df76dd7 | -5.70993 | -46.46742 | 2024-10-08 03:40:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9eff529e-d6b3-3127-b009-9b32d1abc2ce | -5.56428 | -46.29161 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dac306c-fdbf-3e04-8ac4-ece923160bf1 | -5.56423 | -46.29338 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaf82d4a-5a95-3730-9df9-572c1440d151 | -5.56342 | -46.29639 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78453c6e-f315-38b1-94c5-99768c4733ab | -5.55815 | -46.2905 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f227ee6e-f6de-376e-8430-42433d026c94 | -5.5581 | -46.29228 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df7d9ea6-880a-3e02-954c-822a116b3132 | -5.91608 | -45.39754 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 989e71f9-eade-3019-b891-febaad9adcab | -5.91542 | -45.39781 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 30362c14-baed-393e-8061-de4d26d2ad51 | -5.91539 | -45.40135 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eeadf70b-2c66-35f8-baef-83a42f05a8c1 | -5.91476 | -45.40163 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4dd810b6-7e90-394e-886c-8fdde551bd93 | -5.90965 | -45.40018 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35e9aea6-9d1d-3250-9323-ae95c2ef8aba | -5.90902 | -45.40047 | 2024-10-08 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aae3b0df-44d7-3016-8ed6-d6f481d6db9e | -5.52107 | -45.26215 | 2024-10-08 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d6c7cf2-9de9-3846-a706-4f439e061106 | -5.51682 | -45.25752 | 2024-10-08 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5e9c86f4-5226-333e-b4c7-4f1edc03272a | -5.5161 | -45.26157 | 2024-10-08 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b50de821-1b16-3cf2-a952-2e4413adbd45 | -5.51594 | -45.25751 | 2024-10-08 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e94d52f5-5328-3df6-9cbc-0427627f47d1 | -5.51524 | -45.2616 | 2024-10-08 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4b45a778-5032-385a-a537-113e4690c70a | -5.39693 | -44.95188 | 2024-10-08 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 891272a8-07e6-3fe6-8608-c95d4f4e34d3 | -5.39627 | -44.95564 | 2024-10-08 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0761be9-d0ff-3a8f-8d19-4532f90686fa | -5.39061 | -44.95471 | 2024-10-08 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91800597-43a8-3893-baf4-f2601b1bf6eb | -5.27143 | -45.12115 | 2024-10-08 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fe5a443-f537-3bb6-b2ff-7db66577515c | -5.27075 | -45.12504 | 2024-10-08 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cea7376-425d-3fae-a1d1-cd6ec56e60dc | -7.52407 | -46.59347 | 2024-10-08 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5cae0c2-fe03-34e1-b2df-57642b968300 | -7.52269 | -46.59612 | 2024-10-08 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4edb6eb-06da-3e5c-8d2d-567428fcf778 | -6.93658 | -45.24326 | 2024-10-08 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8bb0923-eaea-3c36-9fb5-8fbaec08062a | -6.93584 | -45.24734 | 2024-10-08 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 731c5832-9ab1-3fdd-8c92-d5fc328dd7d3 | -6.93103 | -45.24191 | 2024-10-08 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec261225-720f-31bd-b81e-f0ae9505877d | -6.89625 | -46.08829 | 2024-10-08 03:40:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bea65e42-4f0f-346e-bfe1-638ebf21097f | -13.53183 | -49.48337 | 2024-10-08 03:42:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f0796506-b614-3540-aa4c-aff9873a0059 | -13.53121 | -49.48293 | 2024-10-08 03:42:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3bf35b88-6ea3-3661-9181-212831a6b341 | -8.75246 | -49.78807 | 2024-10-08 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b53136a8-1c93-3185-afdc-1144d0feecb9 | -8.75068 | -49.78275 | 2024-10-08 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b764ff9-eef6-36ea-a258-7dfc18b7ffd6 | -8.74927 | -49.78999 | 2024-10-08 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cc21405-1f5e-3237-9eed-8fa9e02a6a92 | -8.74526 | -49.78687 | 2024-10-08 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a768305d-d893-359b-bf6f-e50d8bbbedcf | -8.6043 | -48.8488 | 2024-10-08 03:42:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7d94132b-6dee-306e-b62c-66f21b856242 | -8.60332 | -48.84874 | 2024-10-08 03:42:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47f83814-e040-37a1-85d7-968e013d5b6b | -8.60306 | -48.85503 | 2024-10-08 03:42:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9045d320-7224-3519-af7e-6e067cbc086f | -8.60212 | -48.85498 | 2024-10-08 03:42:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dad3133e-f36d-3fdb-a0b8-46deb2511d7f | -8.59746 | -48.84765 | 2024-10-08 03:42:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bee0b8b-f3a9-31e8-bbd3-7cd24f3cd7f2 | -8.59649 | -48.84755 | 2024-10-08 03:42:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 239c2a52-e694-3d05-9774-06975b5328f0 | -8.16431 | -49.46859 | 2024-10-08 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a363ae92-15ef-3dea-b776-6d8570af4afd | -8.16293 | -49.47581 | 2024-10-08 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9f9d5746-04b8-30b5-8e71-4d02ee6417ac | -8.16058 | -49.46937 | 2024-10-08 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d80715e6-c5ce-3e68-8903-c3f1180c2926 | -8.15914 | -49.47665 | 2024-10-08 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8e8cc3f0-d7a4-36c2-9b1a-546781d3b46f | -8.15725 | -49.46705 | 2024-10-08 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f399f5d5-8f3e-3ef9-99bb-9295106c47fc | -10.07274 | -39.53178 | 2024-10-08 03:42:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dfcff40b-34a4-3408-9e06-65428a1ed43e | -12.13213 | -39.39883 | 2024-10-08 03:42:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec17a1e3-fb6d-3311-b72f-0170ab3167d6 | -14.25877 | -41.78436 | 2024-10-08 03:42:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c5f4b0d-4b15-3b17-b876-54441ee66d1f | -14.25733 | -41.78579 | 2024-10-08 03:42:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3ac6c2a2-e932-3ee1-aa2b-dd6357343ed6 | -10.49995 | -44.01888 | 2024-10-08 03:42:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c531c9c2-df6a-33ad-acf3-8b235162d583 | -10.49742 | -44.02049 | 2024-10-08 03:42:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3e2fdf5-ea73-338f-9c6a-96428aa2c4f5 | -12.73996 | -43.45807 | 2024-10-08 03:42:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c35b78c2-6945-35a4-acdc-18fb9b044f74 | -12.73546 | -43.4572 | 2024-10-08 03:42:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 230be8f4-b105-3b83-a3ec-88e5a68e49e4 | -12.5783 | -43.36697 | 2024-10-08 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 98546b4a-88a7-33ab-8b6a-c7ab9299f3dc | -13.22292 | -45.53437 | 2024-10-08 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5891c438-8c9f-3828-a9d2-6576b290de42 | -13.22232 | -45.53752 | 2024-10-08 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4294dee-b181-364c-a50d-be0d7c2e6c4e | -13.08418 | -46.34695 | 2024-10-08 03:42:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bf1db1b-1ad8-3b04-bd62-3532ff3164e1 | -13.08349 | -46.35054 | 2024-10-08 03:42:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36238594-d0be-3ca3-9641-45c209d40c65 | -13.07976 | -46.34859 | 2024-10-08 03:42:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6d58479-2214-3080-86be-8143d9ab6ae0 | -12.99636 | -46.21189 | 2024-10-08 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20bbd3ac-df58-3a95-be47-95cf9efbd539 | -11.91764 | -45.70244 | 2024-10-08 03:42:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c487e490-4afb-39e4-a5e1-1b4e0efb5dc1 | -11.9141 | -45.70082 | 2024-10-08 03:42:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07d1869b-b882-3d02-948f-803c50cacff6 | -11.91347 | -45.70418 | 2024-10-08 03:42:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15132ea9-13f1-37a0-ab2b-f26b1c59df8f | -11.91235 | -45.70138 | 2024-10-08 03:42:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fa10d62-9267-3a0a-a040-a6ea2e7c973d | -13.85054 | -44.58529 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93fbcf84-814b-356c-89b3-5c84bcc79b5b | -10.32811 | -36.67615 | 2024-10-08 03:42:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3a6e8c35-1f23-3ca0-a0a0-b53d83d0ee32 | -10.69452 | -37.06631 | 2024-10-08 03:42:00 | NOAA-20 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5e2762c5-3022-3c4b-bae8-b1fbb99a0cc2 | -13.29529 | -39.91669 | 2024-10-08 03:42:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 361db141-6936-34b7-bed5-03d7e310d486 | -14.03453 | -41.70618 | 2024-10-08 03:42:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a03572a-25b3-326f-bd3d-33a1687e2901 | -13.1556 | -43.1118 | 2024-10-08 03:42:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f99d502d-3cb8-33e9-9d00-0f227afbe091 | -13.13751 | -42.47666 | 2024-10-08 03:42:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9e220a29-145f-308c-be99-fa2479bca703 | -14.78631 | -42.8408 | 2024-10-08 03:42:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f4bde77-2c3d-3591-a6bb-8652cd60a789 | -14.78559 | -42.84473 | 2024-10-08 03:42:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ae9a4ee-5dcb-336b-b96e-7d52c46010b4 | -14.78214 | -42.83998 | 2024-10-08 03:42:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README36.md)
