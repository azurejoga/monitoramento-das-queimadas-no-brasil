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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78dfffe8-98f4-36d0-a21d-ca12c4d29a6a | -8.52335 | -46.28082 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddc073c2-f3a9-3544-a9e2-4bcbb0ef11f4 | -11.79419 | -45.11279 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 483b87bc-5dd3-3a3c-8c43-13346505af49 | -6.01673 | -45.88165 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f12f806-88ad-31cb-92d9-2fc9bdd8b834 | -9.13357 | -50.0586 | 2025-10-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a16d680-7145-35cf-ae0c-53a5b444866c | -9.97732 | -48.78167 | 2025-10-08 04:38:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a6c9da50-ec30-3589-aaa1-b715d66e9ddc | -7.45195 | -43.12963 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a021809c-1726-38a9-8611-5e964fb4355b | -11.79816 | -45.04283 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be4a1154-703b-3aa0-9282-0d174cbe7357 | -5.16192 | -46.22338 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4dec03c-49d4-3076-987e-90272dae5890 | -5.58949 | -45.83984 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0cdc8e3-be82-308c-b3ec-d964fa49748d | -11.15542 | -47.74643 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2ec4d30-9101-3eb9-b525-d23571dfcfec | -7.35315 | -43.85908 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67c4fbec-d8b7-308e-ab53-a4d7a047a9ea | -3.46376 | -50.09272 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e4c9618-8a9d-3735-a2f6-915d58e27786 | -10.26044 | -45.3702 | 2025-10-08 04:38:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a82a905-3c08-3eca-a992-3e891a6d198e | -8.24802 | -50.09442 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 59a65374-b2e8-3494-b070-964774b9e02c | -6.01738 | -45.87741 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dde971c-b139-335a-b5ab-70f9862f2913 | -7.25534 | -44.11289 | 2025-10-08 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df0d2b24-eee3-39b9-a769-a51047736e22 | -8.92644 | -46.58507 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d192afaf-3b55-32ae-9b1e-3c3cdebcdc5c | -6.37314 | -41.61873 | 2025-10-08 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 89713336-b29f-3f02-ab4e-493c3d01b87b | -6.06452 | -44.31899 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66c6249c-ba04-37b9-9e3d-967650d538c0 | -9.91897 | -52.9415 | 2025-10-08 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df99cb2f-8e03-3063-b3eb-4a2e12b69048 | -5.74315 | -44.98275 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5221401d-5a36-3b8f-a173-de4bc0e396e2 | -4.68738 | -49.49528 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61a23665-0802-316e-90be-cc1a55a53348 | -10.34923 | -50.2535 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ec34a2de-e231-3892-8705-db9226f0ee0f | -5.77983 | -45.74347 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b2fa582-22b6-3013-88da-857a34ae9e6a | -8.1894 | -43.34263 | 2025-10-08 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e3e59f04-a74d-38db-8211-e0c6ccff4b56 | -4.50135 | -46.35774 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae42fba7-4601-375b-a044-314584d034dd | -6.45793 | -44.57931 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb93fd2b-6cf4-3a53-85f7-b8237032b8ce | -3.50129 | -51.11296 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a463db52-35dd-370b-b766-10d9433c32fa | -8.23383 | -44.1819 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b228778-e9ce-342a-8da6-66bc4e17e829 | -9.17336 | -47.82949 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa2a344d-5036-3862-b972-54fd2d2cc7c5 | -8.23271 | -44.18953 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 957b562d-d645-3480-bf63-76bdfa4f2e55 | -8.99642 | -40.4206 | 2025-10-08 04:38:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c9776271-50a5-354b-9525-8e41a3f851d3 | -9.78898 | -47.72121 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf8b9537-9922-3a19-bfa9-680dc5f76ab1 | -5.86938 | -44.30128 | 2025-10-08 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6921e4d1-3a51-3f53-a50a-3a6921334578 | -4.68732 | -45.84969 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 406fdf07-c465-3fed-b14c-551be83f9c43 | -10.17454 | -45.55341 | 2025-10-08 04:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bf92c2b-49db-327e-a2c0-b8c3fd73c668 | -8.23216 | -44.19334 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| afb14c9b-d206-35a4-99f2-056d2a3305d2 | -8.92882 | -46.59403 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d56c483-074d-33f4-8c8b-475628c42a50 | -10.42729 | -45.38224 | 2025-10-08 04:38:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6a603f6d-9573-3205-9be6-2d03ce2b3898 | -11.19142 | -49.77813 | 2025-10-08 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aae21d61-ed4b-3621-ac44-1b6310d98158 | -9.1946 | -47.80566 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b62f773e-16f9-3ba7-94e3-6916dbd6222c | -10.48396 | -50.30412 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ac758d5-6102-3a52-8d51-3bc2ea47cf49 | -8.27059 | -47.00916 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd612daa-3ced-3583-9d85-8bb447e39312 | -7.22492 | -47.18127 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c5c6722-859b-3de7-8c3c-bbd644b4bbbd | -4.85354 | -45.66554 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cde78ba8-4301-33ae-b148-49e7f149685e | -10.46558 | -47.81909 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cc33893-10c1-3a96-88ad-a21183befe52 | -6.50325 | -41.49219 | 2025-10-08 04:38:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d6b8c952-bf62-33ec-8f4c-765be597f984 | -8.53949 | -50.16284 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c32022f7-af3c-366c-bdd7-917a2cfcce14 | -4.30896 | -48.08043 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4697fce0-767f-3356-8e76-095ecde03439 | -10.34978 | -50.25001 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b425b6f2-6770-3b5e-8161-b14f6971fbe0 | -11.86816 | -44.93268 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2e6e59f-0204-3c52-9bf9-120b9281fe7d | -5.27272 | -49.5096 | 2025-10-08 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d18665a9-038c-38a6-818d-7ae8377d72bf | -9.17879 | -46.92673 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb459f4b-03ab-3439-aa33-7e158e684236 | -11.1484 | -47.7453 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb7ac5ac-59ef-364e-b996-fa90078a2be2 | -4.69278 | -45.83801 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6ffbef3d-05f3-37aa-80ed-a37847d02995 | -9.78551 | -47.72066 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1a0bc13-f044-3daa-82ba-3d51aa67d602 | -7.67435 | -42.40775 | 2025-10-08 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 53b66484-cd8f-3257-a9f6-f886245c4d4c | -8.15184 | -54.84746 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed0a48fc-94c1-3007-82d4-38bdecac3719 | -6.30317 | -45.13759 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dab289f-eaa2-3374-874b-479d5b186b68 | -8.68168 | -44.72867 | 2025-10-08 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a14b055-d80e-30c9-8814-1f632c3e5e93 | -10.1753 | -52.57418 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d6a031c-e8b3-35b8-8838-a08ba7970917 | -11.27207 | -48.85381 | 2025-10-08 04:38:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 404e0838-0eaf-3ef7-a16a-2710bc750312 | -11.85671 | -44.92318 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f171d0ed-2b37-3233-a862-d245f0dc036d | -3.46434 | -50.08915 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b3037c0-7ce2-38ff-9d9e-17079d9ad13c | -7.46103 | -43.03246 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 25ddd039-6f7a-3ad6-8aa5-449d77174160 | -8.55982 | -46.23758 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5524a898-8a12-3106-bd86-b8723db960e5 | -5.15953 | -46.92677 | 2025-10-08 04:38:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25840ccf-ddd7-3157-870b-5987780c80a7 | -7.58213 | -47.20601 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50d34eaf-ac0c-3f86-9172-78fcd0eb1867 | -4.39988 | -49.76447 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 614a7d4b-0785-30a6-959f-7557fa22dab2 | -9.6684 | -49.94073 | 2025-10-08 04:38:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e5655aa-d6a1-3180-a49b-c511fc7cc919 | -8.22048 | -44.15675 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ac89fc6-dab1-30d3-826e-1630df3d4b35 | -10.2282 | -52.69549 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a56947a-5fab-3ff1-991d-02a5049e5d20 | -7.82282 | -46.71928 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f09f77a-8f30-3a59-a1f3-8f47e864d2df | -11.21306 | -47.77402 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75313529-5e2c-3897-9a50-573f07dc08de | -5.13523 | -44.96022 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9f4ed770-2b9b-388e-80b7-3f3c4a152dbc | -6.7025 | -58.81181 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0ac52f1-0c34-3790-8199-1fde8fa8abc3 | -4.69215 | -45.84209 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0b1976d2-79dd-394c-b13b-62582e5c86b0 | -5.71733 | -43.61414 | 2025-10-08 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97fec587-6f67-3311-bd8e-34fb6c499cf0 | -11.79301 | -45.1125 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e0c1e04-d970-3738-adde-b821456e38f5 | -9.20158 | -46.89648 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29709308-1ed7-327c-bec3-a11475c445a0 | -10.64443 | -47.80217 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2020c1e0-90b1-3bda-9740-ef52768ab8a5 | -9.77506 | -48.29122 | 2025-10-08 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29bad620-92ab-3f4b-a20d-f0dfae55d07d | -6.71354 | -42.86116 | 2025-10-08 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 434ad148-fcc4-30a3-b3d6-020b0c5866fb | -8.46906 | -46.2966 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27b7dddb-a867-3161-ba2f-c2ece6ada82d | -9.64102 | -55.0802 | 2025-10-08 04:38:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 769b1486-294b-3830-9a83-0d175e778146 | -9.79423 | -47.74499 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66856e46-979b-3b64-8ef4-129c86b88f99 | -9.20517 | -46.89699 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c4d6b29-ef2d-3049-8c7d-9e9966e94229 | -4.49785 | -46.35719 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b7ba4f67-5b1b-36ec-8190-0a1947ece5da | -9.65609 | -56.96528 | 2025-10-08 04:38:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f450c08-ce39-3008-be3c-d12fc30503ee | -5.84747 | -43.4088 | 2025-10-08 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29a729b3-f785-395d-95a7-b325f8e44cc6 | -5.90821 | -49.42274 | 2025-10-08 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5775b0d7-f113-3e83-8326-f26a23ae9db4 | -9.19 | -47.81272 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee50b586-fa5a-3175-8131-a4635ffe200f | -10.80536 | -48.8089 | 2025-10-08 04:38:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92aa5ee7-3008-3233-b9df-23d9f298bea0 | -10.26542 | -46.49405 | 2025-10-08 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26d0c5f0-6c04-3d35-a1b9-5c58fb83c323 | -4.57447 | -44.98228 | 2025-10-08 04:38:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad484661-f021-3dfa-b53c-945ec33dab33 | -4.42475 | -47.75418 | 2025-10-08 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b430d970-8619-3b92-aa11-d464dd07e53e | -7.45765 | -43.03392 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a54db8e9-de02-3dc0-b916-4879298edddc | -7.47394 | -43.1017 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ae304999-154a-3194-9951-13dc60790b9b | -8.56845 | -46.23018 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e3d5d96-6fd9-3c00-9e54-b16ca626aebe | -7.78666 | -44.19993 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README67.md)
