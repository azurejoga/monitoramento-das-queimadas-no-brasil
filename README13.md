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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8eab265-cc5f-3f9d-933c-0b29e04a0345 | -4.5207 | -45.7029 | 2024-11-08 03:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 54d176cd-ee40-3739-b1c3-ce74c43b0b5c | -3.9483 | -48.1724 | 2024-11-08 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2f88d1c4-9531-3bd0-b002-8842eed35636 | -7.4799 | -43.5579 | 2024-11-08 03:40:00 | GOES-16 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 3287bf3c-8139-3b85-866e-b360dbb5b107 | -4.5209 | -45.6804 | 2024-11-08 03:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 250.2 |
| c3d3cb8d-96f5-3679-9668-7cd8faabc9c0 | -3.1641 | -54.4854 | 2024-11-08 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 5714e7b4-42e7-3bd4-b8f5-299c5d33cfe7 | -3.5631 | -47.3847 | 2024-11-08 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 0d5719e3-694b-3f0e-823b-e92f56d6280e | -1.5165 | -52.0671 | 2024-11-08 03:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9b26fbdf-c279-3230-820a-9d6a573dcab5 | -1.1489 | -51.9894 | 2024-11-08 03:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 3f5d30fb-5ae7-3265-a824-ffde8c5d1962 | -3.967 | -48.15 | 2024-11-08 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 44bcc132-cb62-3734-8d87-67b156ebfe5d | -3.9854 | -48.1708 | 2024-11-08 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ca71b569-5a08-3fc8-8cca-48b666b5a893 | -4.5022 | -45.6815 | 2024-11-08 03:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| ecdf0b4f-fc58-3736-ac34-27c322467413 | -3.5446 | -47.3855 | 2024-11-08 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| a353e911-2897-3d8c-8262-71e7f31a0fda | -1.1489 | -52.0099 | 2024-11-08 03:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 09348d62-ab8b-36e8-ba72-76f88a4f2abf | -3.5447 | -47.3636 | 2024-11-08 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 43d70868-3ac6-346f-97d0-4cce762faa22 | -4.5395 | -45.6794 | 2024-11-08 03:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 2f5c304c-7a88-308c-a4b6-cad22e3c89e4 | -3.9669 | -48.1716 | 2024-11-08 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 366a6335-cd13-3f4a-965c-34c77dab0122 | -4.521 | -45.658 | 2024-11-08 03:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 05238313-bd51-3fce-8e64-d721d9809f7c | -3.5632 | -47.3629 | 2024-11-08 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| b854901f-c5f9-3046-a360-ce36a6ec14bb | -4.5207 | -45.7029 | 2024-11-08 03:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| fb82be04-5f98-3447-9253-e4f7dc043427 | -3.5447 | -47.3636 | 2024-11-08 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 943b38bf-c8f9-30e6-b626-9f2a050817fc | -4.5209 | -45.6804 | 2024-11-08 03:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 179.6 |
| 1ad9ab7d-153b-3251-9cd4-91796fd298b7 | -3.5446 | -47.3855 | 2024-11-08 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d13c4c88-76bb-3494-b650-42cbe5ce1747 | -4.5022 | -45.6815 | 2024-11-08 03:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 106.1 |
| f8bc5307-1bed-3a1f-a6ad-4128ce3c446a | -2.8016 | -52.9414 | 2024-11-08 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0ed1b42d-2387-3446-818f-17c796c8b859 | -4.521 | -45.658 | 2024-11-08 03:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 903b1931-4005-3fe3-babf-a73c770126af | -3.5631 | -47.3847 | 2024-11-08 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 7cff0686-d08f-3462-96c6-dfb9b34a6ef3 | -3.967 | -48.15 | 2024-11-08 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 686dc600-4f45-3c07-ab2d-532fdc0ae954 | -3.9669 | -48.1716 | 2024-11-08 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 8111493f-8ae8-3989-91af-abe3bd0828c9 | -2.6764 | -51.8189 | 2024-11-08 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| d0708a44-80a1-3d99-a1af-e3dfae171a6e | -4.55591 | -48.01678 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7340628-dab6-348d-82be-7d6122e4810e | -4.51015 | -45.68698 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98100792-a840-3f6f-bdc2-d885dc6dfc87 | -3.97106 | -48.18196 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 13e248ff-3c8a-32a6-8885-308b62a14832 | -3.74744 | -52.0971 | 2024-11-08 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fa688f7-43f8-3626-ad72-20e3a4b1d335 | -4.79808 | -37.74599 | 2024-11-08 03:57:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 06f28ee3-359f-3471-aa2a-5b18b7b879aa | -0.92426 | -47.13088 | 2024-11-08 03:57:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 593a0a98-887d-32bc-a2c9-bbd289278568 | -3.86448 | -40.76429 | 2024-11-08 03:57:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bbe6fe65-6d9c-32cb-9d0c-ab25c824c57e | -3.71604 | -49.00684 | 2024-11-08 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0746d555-880a-3368-9880-2dff71278c41 | -4.74068 | -38.54189 | 2024-11-08 03:57:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bfab0009-0e6f-3f25-9a21-651920061e04 | -4.50646 | -45.68219 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c1889e0f-52a8-3dc2-bd41-8f7ddd76f9a6 | -4.50874 | -45.67546 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 29bf2bef-cd6c-3071-9407-709af8d49dc4 | -4.40403 | -45.64582 | 2024-11-08 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3e5e5fc-ae83-3f4d-a5df-e89506b1de99 | -6.26891 | -39.3689 | 2024-11-08 03:57:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3fe12422-0fb4-3596-bd2d-37538228acf6 | -1.50034 | -52.1709 | 2024-11-08 03:57:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9669c005-5f94-37e4-b1a3-f2e7d8ca18d8 | -4.561 | -48.01766 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67f39aa1-966f-34a4-ac7f-769c98df02aa | -4.88903 | -45.42867 | 2024-11-08 03:57:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99917382-1c14-323a-8f9d-8c6061de3c77 | -4.52103 | -45.68196 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 68fc516d-64a9-3d44-b697-135a2bb97234 | -3.95802 | -48.16387 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aaa04cec-1200-3ab1-992a-58b830539fa3 | -0.92474 | -47.12791 | 2024-11-08 03:57:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cbd433d-e0d0-3cd9-8996-e385e9d4b94a | -3.96166 | -48.17411 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9c2d7172-b615-39ed-9060-52a357f9c332 | -2.70933 | -45.69709 | 2024-11-08 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7495fda0-367b-339d-b370-3406e9ec94ae | -2.63095 | -46.77652 | 2024-11-08 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eb2cccc-a272-3b2d-a410-424f2034a853 | -4.5167 | -45.68114 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 676b3932-6926-3920-ab75-b6436a80ef7b | -3.2501 | -46.47372 | 2024-11-08 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcd44108-72c2-306d-ad85-ef031b816401 | -3.96586 | -48.18102 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4e6fac16-6416-3aa0-9397-edeff982fc15 | -4.70486 | -43.79664 | 2024-11-08 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 711be4b5-7277-3014-90f0-0ef7de3ac43f | -3.54091 | -43.62342 | 2024-11-08 03:57:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 680f3e28-6060-38d6-b2c7-cfdf45bc018c | -4.13087 | -38.70483 | 2024-11-08 03:57:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d39c6382-12f6-3546-bd2d-58a08caa3482 | -4.08003 | -43.36501 | 2024-11-08 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ae7859a-e00e-35c3-9f32-8c837906b2bb | -4.77363 | -45.73412 | 2024-11-08 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dc4f28b-1290-3a74-86f6-f26cdb96eab7 | -4.40841 | -45.64624 | 2024-11-08 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c7f170a-23ae-35d1-8ad0-c31dbc786d0f | -2.17518 | -46.44207 | 2024-11-08 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 789a2b30-fb6e-37d7-af9b-efdabfa54d5d | -4.50812 | -45.69955 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 782c33a3-b1ef-3a7a-b019-be5690bc4251 | -5.0942 | -46.1111 | 2024-11-08 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee758905-1449-3b35-91a1-f9b49ab9311b | -4.61445 | -45.71071 | 2024-11-08 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be1a2efb-b7b7-307d-8270-c45c0d8b8291 | -4.76965 | -48.68303 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf0ad10a-2c46-30e8-b39f-158f33a96802 | -4.6808 | -46.4063 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c9f6ee99-2192-35c2-9c2d-75256a1bb670 | -4.80149 | -37.74651 | 2024-11-08 03:57:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0428ba92-7aa9-3e51-8e7c-1622ad7d919a | -4.30809 | -45.68587 | 2024-11-08 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd931b6d-8520-33ac-82af-7629482fcc0b | -3.91262 | -38.3639 | 2024-11-08 03:57:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f5211e88-8b20-3ef1-8b52-e5828c7f72ec | -5.36869 | -44.73233 | 2024-11-08 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a64512e-af98-3228-a17c-8bfdcffbc10e | -3.59222 | -42.85811 | 2024-11-08 03:57:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 734880fa-3f71-3e88-a940-dbef62dd73ae | -4.91597 | -44.03983 | 2024-11-08 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 539caf7f-28e8-33ab-a57d-dc3fb39f6871 | -2.56864 | -47.34237 | 2024-11-08 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85494076-3a29-3816-97bb-aedb72cb9ca8 | -4.6792 | -46.44437 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6a6248f2-d7ce-3b2d-b010-39f553509a76 | -3.96375 | -48.12932 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2eb4a87f-3b87-320b-91d1-69785448a48b | -5.18228 | -46.1847 | 2024-11-08 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27fa215a-f579-38e3-a4fe-7d6ebd2c5527 | -5.5566 | -43.70641 | 2024-11-08 03:57:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a509c854-592b-3f45-a27b-e7cd129969f7 | -3.54338 | -47.37987 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 64ce4fd5-14d1-36d5-b049-2b25bca26a8e | -3.60396 | -42.85554 | 2024-11-08 03:57:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7762c79-d2d6-3422-8c0e-2e43f81fabc0 | -3.24253 | -45.68879 | 2024-11-08 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 902cde4a-1a3e-32a3-9c16-f6319d54a74a | -4.99806 | -46.8989 | 2024-11-08 03:57:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b0cb953-d186-39ca-8bd5-4897752bdc52 | -3.72097 | -40.70171 | 2024-11-08 03:57:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1930ccb4-1414-35bb-a12e-91674649379e | -4.87393 | -45.72945 | 2024-11-08 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aafdfd48-f7f7-3fdc-b1b4-fcd2a890b5b1 | -3.07108 | -45.74979 | 2024-11-08 03:57:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dc96f76-be5c-39a2-bf6d-240ef5d7794c | -3.70243 | -44.89539 | 2024-11-08 03:57:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b410ceb4-a20e-384c-9e65-f3a0cb3f8e0d | -1.52114 | -52.17458 | 2024-11-08 03:57:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84bc3177-4551-3561-aac3-77af0fb16ab7 | -5.58058 | -41.68574 | 2024-11-08 03:57:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3550141-b5db-3a60-b416-fe6aa360ee43 | -4.51462 | -45.69352 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7c51bb85-0d3a-365c-a9a8-eb3f4bf31d01 | -3.88194 | -43.15157 | 2024-11-08 03:57:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f33751fe-a7bc-30ae-927b-08c33ed0cfcf | -3.54744 | -47.3862 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| fcd75441-23fd-3a44-9355-ceb325fada99 | -4.21304 | -45.74135 | 2024-11-08 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75e7a0d3-35e7-3969-9d0c-c7ad866c34a8 | -4.70385 | -43.79428 | 2024-11-08 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 138fed95-f39f-30cd-bbf8-0a157f0e2f38 | -3.55334 | -47.3813 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| e47cea60-56f8-35c8-898d-c2f2a778859b | -6.26836 | -39.37236 | 2024-11-08 03:57:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7c3b8f9f-02d7-3ba6-813d-048895a435fc | -3.95803 | -48.13171 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22b0b7e8-cd77-3011-961c-102aa88e16cd | -2.92787 | -45.15475 | 2024-11-08 03:57:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f65cf7b-5405-397a-89d5-36a017b37a52 | 1.66749 | -51.00656 | 2024-11-08 03:57:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 961c0446-0b50-3b28-b315-e90968dd0f01 | -3.72041 | -40.70528 | 2024-11-08 03:57:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8e71188a-6b09-3aa1-a3ae-dc6faa8f66bd | -2.01558 | -46.57831 | 2024-11-08 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ad4023c6-a7f7-3df4-aa90-23872fee56c9 | -0.92885 | -47.13471 | 2024-11-08 03:57:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README14.md)
