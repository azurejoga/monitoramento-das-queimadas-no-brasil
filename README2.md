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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f6fb899-0ef6-37c3-a1ac-42be3f24bfb1 | -9.36772 | -45.73594 | 2025-07-29 00:07:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b0446600-6baf-3fcc-916b-297a84927322 | -3.2826 | -42.636 | 2025-07-29 00:09:00 | TERRA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 01f8b63b-b732-37f1-9f47-0f397c3528b5 | -4.60041 | -43.31427 | 2025-07-29 00:09:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5777b1bc-48c2-3e30-a12b-99e4d1c9c652 | -3.36699 | -47.15268 | 2025-07-29 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9a4d9b9c-e761-3b21-9ccd-ad93a99f0ced | -3.25894 | -43.26693 | 2025-07-29 00:09:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dfb5e003-2ae2-3012-bfae-02326001eb63 | -3.3691 | -47.16817 | 2025-07-29 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 15d9c961-003a-3916-bd7e-7932c7d044eb | -4.85143 | -42.99706 | 2025-07-29 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1cece197-9786-3be3-b1bc-cfd2be5f0ed5 | -2.90664 | -48.28288 | 2025-07-29 00:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| c5f8eeb2-fe24-32b7-a9bf-b19465dfb37d | -4.59913 | -43.30495 | 2025-07-29 00:09:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f5e04ea6-d83a-3915-a839-b05f3d42f0e0 | -4.96501 | -43.22025 | 2025-07-29 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d9ff7881-d161-3c0e-817d-9ed1fda144d3 | -3.82393 | -41.56414 | 2025-07-29 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| f1fbd88e-8965-3191-81c5-bf88a055f9e9 | -5.85829 | -44.22443 | 2025-07-29 00:09:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 69c3bdf1-bbfc-363b-a69b-d3d0685a2f25 | -5.35764 | -45.28128 | 2025-07-29 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| a0529595-9fac-356d-b8a8-65853906ab4f | -5.8626 | -44.22832 | 2025-07-29 00:09:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 73ab1b32-66dc-39c6-ac7c-dd8e6a1c51c0 | -4.80359 | -42.7167 | 2025-07-29 00:09:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69e92f03-c390-3a82-9f1b-7d9096d613a9 | -2.90765 | -48.30807 | 2025-07-29 00:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| e7b106fe-7798-3514-9450-8281105a3fd9 | -5.35715 | -45.2626 | 2025-07-29 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7222f799-8e93-3b7e-ac3d-2da26a8004a2 | -2.89258 | -48.29118 | 2025-07-29 00:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| d46cca22-e19d-3b1d-8daf-30c279cfaf2d | -4.80483 | -42.7257 | 2025-07-29 00:09:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6942b0a6-cd92-3d30-9074-b49da032237b | -4.00041 | -43.23609 | 2025-07-29 00:09:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e916cd5c-77e1-3de3-a18c-6d9cec734bbe | -3.7426 | -49.05643 | 2025-07-29 00:09:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| effac323-3eda-3215-9761-6cd17a7e5f59 | -4.12467 | -49.2829 | 2025-07-29 00:09:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 800e3c92-583c-3f87-9619-352d7aed73cb | -2.90907 | -48.30148 | 2025-07-29 00:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 385d6145-646d-3b71-a31c-dee183569331 | -5.86124 | -44.21795 | 2025-07-29 00:09:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5c144e9d-59a0-3077-9144-1229d67f2d82 | -5.19262 | -44.95697 | 2025-07-29 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 47fdd9dd-e9c2-30ed-bec4-bc06503e7123 | -5.65236 | -44.35156 | 2025-07-29 00:09:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| fe336873-f56e-34d9-92db-bea8ade84b67 | -5.65379 | -44.36222 | 2025-07-29 00:09:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a97e178b-16a1-3fb8-8859-086784caa486 | -5.35607 | -45.26921 | 2025-07-29 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 4e8ae84e-d3b2-31e0-9c82-32d0bb062059 | -5.34857 | -45.2761 | 2025-07-29 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 631c26a6-16ea-3bb0-a9d9-5dfd799fbbac | -5.35881 | -45.27464 | 2025-07-29 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6b916ca6-0c20-355e-8d34-b77c4498fe72 | -5.5823 | -43.22531 | 2025-07-29 00:09:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f6bad10a-56ec-34cb-9425-b001c39db336 | -6.03794 | -47.5672 | 2025-07-29 00:09:00 | TERRA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 2fdf0b9e-ae55-3405-b467-45a271ffd53f | -3.82516 | -41.573 | 2025-07-29 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 2722e768-f336-3cc5-8203-282e342ddf69 | -5.34691 | -45.26396 | 2025-07-29 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| fb2c356a-fe3a-3f82-a910-dca4f2f410dd | -2.98764 | -48.60365 | 2025-07-29 00:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 722a2e4e-4cb1-3eb2-a888-5640307dbc7e | -2.90508 | -48.28951 | 2025-07-29 00:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| dfb03757-2703-3c7c-958c-5abb5c539469 | -3.24996 | -43.26818 | 2025-07-29 00:09:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6ab9d9bf-62a9-3706-a5ec-311b37041857 | -6.09518 | -42.93637 | 2025-07-29 00:09:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 497f31a2-26a2-385c-adb4-f01fc08e79df | -5.85973 | -44.23494 | 2025-07-29 00:09:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 7e3e52cb-87d4-3e47-89f4-805aeaec626e | -3.8227 | -41.55528 | 2025-07-29 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 27dc1f1e-7d4c-314c-9bdc-b78f6ff6b783 | -3.98362 | -43.24779 | 2025-07-29 00:09:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e89188bf-7994-3377-9d61-da154794b17f | -4.86043 | -42.99579 | 2025-07-29 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d73fee58-70d3-35de-be85-d7b2f4724372 | -7.9445 | -44.0918 | 2025-07-29 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 5bb624da-8c88-3aa6-a7b9-0f8b3a8e6eab | -5.858 | -44.2319 | 2025-07-29 00:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 7c9bc134-68d0-3a99-aa4e-1b8c2a66d369 | -11.7317 | -48.1849 | 2025-07-29 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| a44601f4-f342-3db8-85c9-07f4f0143520 | -14.4943 | -46.5387 | 2025-07-29 00:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 86fbe330-ebaa-3282-82c4-ab7f836f5bcd | -7.8568 | -46.7304 | 2025-07-29 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 162.3 |
| b56945a7-6b75-34da-9eeb-3cbe2ba2766f | -2.9106 | -48.2971 | 2025-07-29 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 444cc187-839d-3f46-9fa4-229edb2db870 | -11.4389 | -45.1385 | 2025-07-29 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 3020435f-31e9-38a0-8326-d446eee0cee2 | -7.9256 | -44.0937 | 2025-07-29 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 97ddb5f6-9313-3230-ab84-2ba0c8adf2d8 | -2.8921 | -48.2977 | 2025-07-29 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| b9204cd8-d267-3e75-b5d6-32f10ccd68d1 | -18.4287 | -54.6704 | 2025-07-29 00:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 945041b7-c171-3998-906d-464cb03cc7aa | -5.363 | -45.2695 | 2025-07-29 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 46e5114c-aa81-3e8d-9ffc-794fbfb7ccbb | -7.4541 | -49.4018 | 2025-07-29 00:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| ace4b24c-f9b7-3e2d-b11a-b20bdc6cfec3 | -18.449 | -54.6462 | 2025-07-29 00:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3f6289ca-3077-32de-961b-6943ec4c0ce1 | -5.3443 | -45.2708 | 2025-07-29 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3fba371d-1b7d-31ce-9df0-83756a270c41 | -11.4201 | -45.1181 | 2025-07-29 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 33df9420-2e37-3845-8086-9fb3f2e989dd | -11.7508 | -48.1825 | 2025-07-29 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 801e0037-a8d5-33c8-9594-5918ec6c985a | -11.4393 | -45.1154 | 2025-07-29 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 87537ae1-b73d-367c-b59d-62ab0d2c331d | -18.4486 | -54.6674 | 2025-07-29 00:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 98002d63-c21c-3340-a170-15027c60e5d8 | -7.2408 | -43.0664 | 2025-07-29 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 5b51f8de-4cb4-3ed7-846d-f7a42d037526 | -7.9256 | -44.0937 | 2025-07-29 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 05abf5af-c99d-3be5-92e6-ffb68b9c420b | -18.449 | -54.6462 | 2025-07-29 00:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6fd120be-423f-3f6d-86f0-6557bfdb0417 | -11.7508 | -48.1825 | 2025-07-29 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| e50add1f-8c4b-3da5-98d0-31db8398c26d | -7.8568 | -46.7304 | 2025-07-29 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 648ddfce-6cc6-3934-9641-944cfc16bc02 | -11.4389 | -45.1385 | 2025-07-29 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 6cc263a1-4bbe-36f5-a8c2-be2847fa9395 | -7.9445 | -44.0918 | 2025-07-29 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 2503837a-e57f-37a8-8fd5-92325ac284da | -11.4393 | -45.1154 | 2025-07-29 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 7473e59c-0e0a-3e99-ad41-ce133c35b1a0 | -7.4728 | -49.4004 | 2025-07-29 00:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d560b48c-64f7-3f83-a660-895fdb131cea | -7.4541 | -49.4018 | 2025-07-29 00:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| db024486-fece-371b-9045-2e67ed239cb0 | -5.363 | -45.2695 | 2025-07-29 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| d9aff883-3c7b-3100-b276-328a23ca076f | -18.4287 | -54.6704 | 2025-07-29 00:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 96dfee3f-9811-3c5a-8e1e-c1a7f3e043fb | -2.8921 | -48.2977 | 2025-07-29 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| fd428396-8c17-3c30-a32a-bdaea18c495e | -18.4486 | -54.6674 | 2025-07-29 00:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 7b1ef64f-f07d-3e07-a56e-968706c779e1 | -2.8922 | -48.2762 | 2025-07-29 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 5189a145-a1a3-3d1f-a119-38b30ef9c845 | -11.7317 | -48.1849 | 2025-07-29 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 138b3df4-c2a8-3eb8-a6ad-f46fb65ed327 | -11.4201 | -45.1181 | 2025-07-29 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 9b29be82-b1d9-397d-913e-bcb89e8c7178 | -7.9259 | -44.0706 | 2025-07-29 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 36c6742b-8fa3-371d-b00a-552adff4d823 | -7.2411 | -43.0428 | 2025-07-29 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 0075e868-bb92-3f7d-8d8d-991b3fdaaf1b | -11.3514 | -51.248299 | 2025-07-29 00:22:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1bb95ca9-c995-36ff-bbca-117e65e63c41 | -3.7446 | -49.039101 | 2025-07-29 00:22:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e522b8-e614-3d9e-8a8f-1fbbcb592309 | -3.0928 | -52.914101 | 2025-07-29 00:22:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31af86a7-153e-30e3-9657-20fb6b5b52a9 | -7.8617 | -46.729198 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03f756e8-6022-312c-9bdb-934b3d0226b4 | -11.34 | -51.243 | 2025-07-29 00:22:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c54cccba-2363-30ad-b7f6-3d15205c1993 | -7.9115 | -44.062901 | 2025-07-29 00:22:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d5df4c6f-cea1-3312-b982-afad7088286e | -9.2173 | -48.587601 | 2025-07-29 00:22:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76d9736b-e2bc-331a-8c21-6118388e33e5 | -11.4271 | -45.131001 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a9a8227-06a3-324d-a6b0-47e3285eb7bb | -8.8902 | -47.340099 | 2025-07-29 00:22:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4b28ffb-06bd-3dd5-ab7c-6df05a859f67 | -7.9302 | -44.097698 | 2025-07-29 00:22:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2b955c6c-a824-36e2-ae36-408d7c0609ce | -3.2245 | -49.334702 | 2025-07-29 00:22:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df268db5-9d6b-36fd-9d22-c8f7328ab2ca | -14.4911 | -46.5284 | 2025-07-29 00:22:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d6d0f54c-3ba7-359a-9049-794fb4798078 | -11.9974 | -46.946999 | 2025-07-29 00:22:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e894a95-20b0-334d-afab-a0954bc09c0a | -7.4613 | -49.388599 | 2025-07-29 00:22:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51078872-668f-31ec-8b4d-95922a2e9312 | -6.4009 | -53.321602 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cfc15b9-5120-3a90-86d5-741164777e6e | -4.9425 | -47.4305 | 2025-07-29 00:22:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19b1eaff-9d93-3f0c-ac4a-1c95715f8c23 | -4.9327 | -47.4328 | 2025-07-29 00:22:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab2cae0-fecd-30e8-b205-e1f24ab0bc6c | -23.133801 | -48.7668 | 2025-07-29 00:22:00 | METOP-B | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a9854948-9a66-3516-aee3-655e303eb6df | -6.3992 | -53.313702 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47d583de-b63b-3b20-a6bc-d9bcd0778f54 | -14.3512 | -47.088299 | 2025-07-29 00:22:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a67d0277-8cf5-3553-8de7-648b6c9559dd | -5.8525 | -44.234001 | 2025-07-29 00:22:00 | METOP-B | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
