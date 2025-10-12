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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a95b370-b006-3c9e-a584-439e6b490549 | -8.0211 | -44.47062 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c447c5ec-0a6f-306e-9537-da4f46af7173 | -7.02092 | -42.09803 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dba28ae3-9e3b-3b17-80cc-2d0b8edba29c | -6.49928 | -42.43711 | 2025-10-12 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ae360ebc-e6d7-3288-be5d-5128f8cfbec3 | -5.80167 | -44.04021 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ddbd53b-1c93-3402-b285-52a6dc877c1a | -8.42 | -41.1752 | 2025-10-12 04:14:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 11186a23-3e31-373f-a07e-b81fa0ccc80f | -11.50179 | -43.49656 | 2025-10-12 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8993a33-11b0-3f76-8863-e8695aefcab5 | -5.74155 | -40.76044 | 2025-10-12 04:14:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| df216afd-c60e-39d1-bea6-eb522ca67855 | -7.86287 | -44.52459 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cba55fa4-5beb-34ac-8302-46e54e48b6df | -7.6262 | -47.50443 | 2025-10-12 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df7cb706-db68-3bda-baa6-c48945d7ecd9 | -5.62903 | -42.69305 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b4b42d8-b15f-39ee-81f8-d555f958f8ac | -7.40979 | -42.97102 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b9e803b1-e36f-3101-9381-f18ac41c7230 | -4.82042 | -43.13932 | 2025-10-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56e37fe0-5056-3bf2-8b71-1212daf3ab96 | -6.71491 | -42.88604 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 64c4fa5c-4232-347d-8e31-c0f25deb0031 | -5.36406 | -46.29519 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fced4d61-8f51-3ec5-b13b-3348fdc6e737 | -5.58018 | -41.1243 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 00c62ecb-3fcb-3c51-8baf-679307db3faf | -7.74498 | -42.40936 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ed18b4cf-895d-39b0-b29a-d28be7f867f1 | -3.81797 | -51.05777 | 2025-10-12 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1b4f97a-9091-360b-b1e8-837e670de2b5 | -8.49648 | -46.25792 | 2025-10-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f36d0bf5-c920-3317-a493-24de4de25b37 | -4.61387 | -45.77673 | 2025-10-12 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bc23ae7-2ce8-373c-8733-2689950fb34c | -9.40093 | -42.67381 | 2025-10-12 04:14:00 | NOAA-21 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef2227a2-de21-37d9-bcc2-a826b558ab05 | -11.75861 | -43.30795 | 2025-10-12 04:14:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c220ec9-6808-3b8e-b851-c603d8e53667 | -10.17812 | -44.54184 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec35363f-97ea-3125-a36c-fe456df085b2 | -7.70993 | -42.37138 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b3b4b75a-2ad4-3d90-9d1e-2d6eef635452 | -6.22222 | -42.66294 | 2025-10-12 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 19263ed9-eaff-3cd4-b456-742c1a496f07 | -7.65029 | -42.58113 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 922455fc-4b50-377d-9403-b9f81538a348 | -7.42461 | -42.96271 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 28670cfe-e5eb-3a1e-ae1f-8c8d187d6e4a | -10.14561 | -44.55447 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 475f68d3-df53-326f-94af-e0b160ece2af | -11.25617 | -41.89727 | 2025-10-12 04:14:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 37dffcd3-6520-39fe-9315-a03c74486bb9 | -5.05855 | -43.27264 | 2025-10-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b28e9410-5da6-3914-bd4a-32787abbb163 | -7.85514 | -44.50872 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9db03dd-d70b-327f-ab80-a4add46d9aae | -5.65293 | -44.4833 | 2025-10-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5f26747-0523-3884-843f-2e5965431a34 | -11.49679 | -43.4849 | 2025-10-12 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23b660bc-cec1-3cef-965f-fbe834ac4c7f | -7.35315 | -44.79458 | 2025-10-12 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c5b488d-074b-3521-9f37-a69253d31ae2 | -7.40542 | -42.97741 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| baaec61d-0173-3341-a48e-3ec37e9a045b | -6.32262 | -41.59672 | 2025-10-12 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13c30525-db8e-3a68-94d1-f89cee7427ec | -5.55939 | -41.32559 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54576703-928c-3d7b-83d8-b51970cdde0b | -5.58225 | -42.9921 | 2025-10-12 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f4c64bf-521b-377c-bd04-52945b1cc122 | -8.04732 | -44.11143 | 2025-10-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90cad74b-b479-318f-9a8e-315c08b69f60 | -8.01672 | -44.45538 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83d845f6-e390-32aa-a4fb-1d8ad73e5e36 | -5.67458 | -42.68252 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 283de960-389a-351e-85dc-2d08920bf816 | -6.56926 | -39.56092 | 2025-10-12 04:14:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 01bc60d5-5428-354f-bde9-0d7a8364eb1a | -10.78515 | -43.95023 | 2025-10-12 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c3d382bb-4c15-3bca-b045-6585e239d6de | -8.70537 | -47.05545 | 2025-10-12 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc672179-0af1-37cd-856e-ea380e32ac80 | -8.02394 | -44.45288 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09b4cbbc-dc24-3834-ac9b-5025140a3a6a | -6.24715 | -43.02695 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 45517a42-71a1-3edd-94c5-6695235e5834 | -7.49499 | -42.77127 | 2025-10-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e7bae4e-1436-35c6-b095-5d89e1b96c13 | -7.14783 | -42.51 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8f7f2d36-1676-3427-aeaf-838539ee34e8 | -11.91376 | -44.17498 | 2025-10-12 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8dd2412-221e-367d-b595-6161bfd4714e | -10.18454 | -44.61117 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95ca26ca-11bd-303e-825a-0e268bb2829e | -6.65872 | -41.37275 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0b8640ac-ac4e-3a5c-9f5a-fd7853f310f7 | -5.22277 | -45.46175 | 2025-10-12 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 330c4da0-ac08-38ea-a5e7-58363e5895a1 | -6.73683 | -42.15526 | 2025-10-12 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c9067af7-8a51-33a5-abe1-4d18dee55517 | -5.52095 | -44.95565 | 2025-10-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2db675c6-cddf-33b6-8487-74f634565f02 | -5.59693 | -41.11207 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 401096f8-8887-3472-a7b4-5b38c37aaae3 | -7.65138 | -42.57414 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a30d87f1-5837-386a-a67f-268323756b34 | -7.46317 | -43.88991 | 2025-10-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b89fcfb0-b2d4-3b9e-9917-a30e60935be0 | -6.31507 | -44.25879 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e00381c5-fccf-352f-b5cd-2a1167fc9c56 | -7.84386 | -44.79556 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a633831-b637-39ba-baff-31437b51ba15 | -6.76717 | -42.83765 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a5c7c535-f6f3-3f45-b1c4-2146705378c1 | -7.67747 | -42.38406 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 075d129d-4cc3-321f-9f5c-edec61b1e133 | -5.75441 | -47.25734 | 2025-10-12 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83a6c5c6-f90a-3ed6-aeba-f67a4539bcf2 | -5.35067 | -43.42862 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6e9f810-23b7-3673-9db4-12a6ac52c285 | -4.67919 | -43.25853 | 2025-10-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52d03c33-3d24-347b-a63a-1f2f05538396 | -5.63563 | -42.69408 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fabb3802-5d3a-3e88-b579-ee776d1b14b9 | -11.50011 | -43.48542 | 2025-10-12 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 781c56ba-f646-3338-b786-fd79f5a028ff | -6.25061 | -42.74529 | 2025-10-12 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b4e3c26b-f18e-3c9b-b530-796c6113ee02 | -6.26955 | -42.99166 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 08ea97c9-9886-3229-b0a1-777a6cc1babb | -5.18032 | -45.43506 | 2025-10-12 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab3a1a6c-ac66-3366-b63c-35bacc6c218d | -6.17134 | -44.66937 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8c53393-4e35-3250-aa8c-6e5c66ba6326 | -6.24385 | -43.02644 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c3cd8287-f6c4-3612-be68-8c223efded74 | -6.21957 | -41.58125 | 2025-10-12 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| af0e9c7b-b38c-3475-872a-c43249ca4267 | -6.84755 | -47.34603 | 2025-10-12 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f01e30f-5c56-3f16-9aa3-9d45f6f93f50 | -5.58816 | -41.86223 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4635e707-da8a-33c2-ab54-85136993608e | -9.52518 | -47.8706 | 2025-10-12 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f14a3b73-e667-3f17-a2b6-33236f1a1b9c | -4.27265 | -46.93222 | 2025-10-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5a770e51-1815-333b-970d-2360cf78b5b3 | -7.83937 | -44.80217 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58b7616a-b533-3c1d-b798-324c8eb77f63 | -5.55321 | -41.3209 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| df1dca0a-de40-3205-9d3a-c80d05e06297 | -5.59404 | -45.84174 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b46ecc1-d98c-316f-a5d2-f205eb0f9b15 | -6.73962 | -42.15928 | 2025-10-12 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c3f95f14-063a-3bdd-908a-55d2c8106585 | -5.33572 | -43.43343 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcc8cb5d-30ef-3a58-82ea-9eeb412384c5 | -6.2596 | -44.07288 | 2025-10-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a148cc0-8f5f-3212-bec0-9069ea778c25 | -7.69552 | -42.37638 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd99a7fe-15ab-3dc3-bafe-1e794573b6c6 | -5.40046 | -40.97355 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5dc0703d-2134-3c9c-9fd9-d387c6511de2 | -5.34667 | -43.4068 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 548b4eea-616c-35b2-9e96-54b16f483f98 | -10.96888 | -43.02362 | 2025-10-12 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1267b5ac-ff30-39e8-a085-fcf1e4470317 | -5.48488 | -43.3967 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82ce44f9-f2c3-3b7d-9246-413a052f2835 | -7.86757 | -44.87626 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c80c2921-adc2-3619-be42-609299cd457a | -6.25703 | -43.02849 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8013f4d8-bc1a-3adb-9a9f-031c444df1cf | -6.7539 | -42.81436 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1f6b5afe-326b-3667-aac8-14695609177d | -6.7605 | -42.8154 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9d24be5a-0b9f-34c2-b3e3-79eceaab6f82 | -5.26453 | -43.10727 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfe567dd-780e-36d9-b4fb-fdca825cef21 | -5.73942 | -41.3231 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0288701a-8c9a-3c10-b235-e50f8bffb13f | -3.58213 | -51.23808 | 2025-10-12 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ec29195-483b-34bc-9446-8c87c0ad040e | -7.85621 | -44.52351 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9965dd9-7d6e-3203-a9e0-65efa93142ab | -5.58244 | -41.10974 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dfd16b86-3341-35ae-a009-1f82b42dbb90 | -6.08213 | -44.30955 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 127277a0-a5a8-349f-88af-c16f88244cff | -7.07332 | -42.7477 | 2025-10-12 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f0bfccd-e059-30ad-8601-3e37c03a2708 | -5.41638 | -40.98347 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f037103-57c8-3650-a073-44fb1e1e8914 | -6.22012 | -41.57766 | 2025-10-12 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d7f6f5b7-193a-3b4c-a907-fbb3958b5239 | -9.40426 | -42.67433 | 2025-10-12 04:14:00 | NOAA-21 | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README19.md)
