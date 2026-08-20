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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feebdce1-3643-3393-ba00-84e4161b16d5 | -7.60316 | -45.16943 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 79b7a671-571d-3209-8b51-2f6e14021ad5 | -7.25218 | -49.89812 | 2026-08-20 04:19:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 18050688-7a62-31aa-a990-52866c4ec6b3 | -7.74993 | -49.46414 | 2026-08-20 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bf785e4-452a-3592-9a04-a8f5bfd66515 | -12.25565 | -43.16558 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f337443f-d078-35cd-8eb1-9467b412aec2 | -8.5664 | -54.76749 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b301266-739e-3d71-8829-362c6020eeb7 | -8.81155 | -44.21149 | 2026-08-20 04:19:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bd2aafb-e1a5-31c4-91df-6c8df4539f09 | -12.23314 | -43.15457 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a420893-4c98-39b7-8e86-d13aeb70751a | -9.45585 | -51.6057 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 49b62756-95b9-3303-95e4-09276d1b1a15 | -8.58998 | -54.7403 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6c67e09-3db5-32e8-8521-22c8620397a3 | -10.76468 | -50.34781 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 054fb5d1-b14e-3ce1-9152-4440564f7ddf | -4.39094 | -55.47333 | 2026-08-20 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a5138b7-d420-393a-a0eb-54c8e2c63245 | -8.5659 | -54.67295 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39c554d3-6420-39b2-a0d3-53acce627c1b | -6.78617 | -42.88502 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 46cd57fd-9182-3626-bf2a-94a349c1da1c | -7.35299 | -45.82344 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a952d126-ffce-3cf7-bbe5-bcafcc00c83f | -6.78231 | -42.88797 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6851a77a-42a2-3945-83db-453a2083e3c2 | -8.67235 | -54.64798 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02fc385a-5d19-3abe-b7ad-35cc30c5c784 | -5.80233 | -55.71055 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b73a220b-25e8-3a3f-9992-12f9b491b1f7 | -11.42942 | -47.24466 | 2026-08-20 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d31f16a-335b-315d-a35d-f1a9b79aff65 | -7.96657 | -44.67225 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 48d61d42-1d2b-3625-be82-0f0927102e4a | -11.31814 | -45.00341 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a74a584-1386-3361-a241-8970ff8f281d | -10.83528 | -50.29773 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a6425a9-ffd2-3ded-ad06-27289588ba81 | -12.19707 | -45.15928 | 2026-08-20 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bde91396-674e-3bb9-af0d-59e5df8ff6d2 | 2.15688 | -50.71871 | 2026-08-20 04:19:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d10484ab-9dac-34c8-a371-5fd17a3290e3 | -7.96827 | -44.66165 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ecc51dff-3f0a-3e57-9563-2c6d92e64988 | -12.25806 | -43.15812 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 30837d20-aed8-3797-b3b3-9545ac55d9aa | -8.57148 | -54.77325 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d990e8c-fedc-34d4-bc74-28d3700ab868 | -7.95892 | -46.91503 | 2026-08-20 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 871ab87c-27d4-388e-aa65-00147734a4d5 | -7.52696 | -55.58052 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b82d0f4-3c38-36c3-9f45-c5d1113e29ba | -6.43946 | -52.7333 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b54b926d-cd1c-351c-9cc5-852bbeb16465 | -6.23844 | -43.68463 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2b827ce-1d60-30f2-a307-138102758719 | -8.47829 | -46.9663 | 2026-08-20 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ce0b380-1e9c-3d14-8c25-1a9f6b66abd5 | -7.34766 | -45.83439 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 61e58547-7182-3aa9-99c2-649bef6638b7 | -6.42797 | -41.60521 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dbc1cd25-f826-3cf3-b8c5-9bc07dd00a41 | -6.29193 | -43.64696 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66876257-fb8c-3fef-83b9-1b239ec8e5d8 | -8.67989 | -54.64042 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75eb9d55-9ac5-3af7-9267-893ae997fad8 | -12.22811 | -43.16487 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9807cbd9-ebe9-3560-8de5-b4a5bdce6328 | -8.48688 | -46.9592 | 2026-08-20 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f860c1e2-4d64-3155-8163-061216116953 | -11.42874 | -47.24869 | 2026-08-20 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21c7902e-54b5-334a-b80b-f18d1602f83b | -6.4453 | -52.76307 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0233e197-11c9-3c1d-b613-1f4d79592c47 | -4.18446 | -49.40539 | 2026-08-20 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7504539-1cd1-3562-a7e4-a546d8243f58 | -12.38264 | -46.45314 | 2026-08-20 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6b612d7-4ac1-3ebb-91a5-76b6a8f5669d | -8.71656 | -49.6209 | 2026-08-20 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f43c7c01-2913-330b-b798-34cc8d822faf | -6.43822 | -52.74021 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b08507b-cf90-3185-90bb-c5a51e357ad7 | -9.74887 | -43.30649 | 2026-08-20 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 454077b4-674b-3497-bcfb-b71398f38e61 | -7.54408 | -55.59443 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90eef43b-488a-3088-9a0f-8f4fa3589a64 | -8.57658 | -54.77885 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 939be7f4-d4a0-3573-aeb1-cf6f38993a13 | -8.66811 | -54.63826 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 77f2cc9f-5e67-35f1-bff2-327e367fe3c3 | -5.52469 | -44.11113 | 2026-08-20 04:19:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75eaf3c8-6609-3c8a-a244-c801b5b4c209 | -12.24889 | -43.16458 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bae3c3ae-e5f7-3e68-ad7a-bb90e4d03dc1 | -7.53087 | -55.58541 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 35f86d72-f68a-3e56-bbf9-b6cbd809efa5 | -8.66243 | -54.64687 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4bf305a3-be5c-35f2-a72f-c2ea5831deb6 | -6.52062 | -45.88728 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c722768-978a-3940-a364-2551a7e11217 | -8.52742 | -54.87521 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b397abfe-8902-376a-a06d-d7f3ff2b4cc9 | -8.66755 | -54.65221 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 76cb2b06-75c3-3214-b7a5-1210a8fdd2cb | -7.3489 | -45.82671 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c266ae9f-abeb-3d64-8242-e1c42a545e6d | -10.25943 | -46.99802 | 2026-08-20 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa100a76-8936-3103-8284-67f9181ba7c1 | -12.24496 | -43.16767 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7e1f898c-55b6-3c21-8e71-1bff9db7439c | -9.75497 | -43.31107 | 2026-08-20 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f42ed196-0323-3fc1-a306-1b3d7105ffc3 | -8.56243 | -54.65898 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 650bc4fe-f921-3445-83e6-2d5ff0d33fc7 | -7.9582 | -46.91929 | 2026-08-20 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04ad7cac-a271-39ef-8f60-0302550211ee | -12.25064 | -43.13078 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9cc82e83-d3eb-35d6-afa9-a6b314378eb9 | -11.81456 | -44.81036 | 2026-08-20 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 490a1641-b330-30ed-b138-bd28e6783248 | -10.24411 | -49.42098 | 2026-08-20 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb675884-12e0-382b-bdd2-39426aea998c | -8.47468 | -46.96569 | 2026-08-20 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47435f92-d033-35e5-b745-b68c6cb3ba85 | -8.66021 | -54.59276 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d6d3921-2129-3f14-a86c-51bd13447873 | -8.71372 | -49.61232 | 2026-08-20 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1de6f326-b9c1-3ae8-95e4-77e111dbe82c | -6.27286 | -43.27559 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49291511-7379-3262-83cf-2d3185c57761 | -10.63211 | -51.61854 | 2026-08-20 04:19:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89da8c81-6498-301b-bc9a-24d28cf44751 | -10.24473 | -49.41737 | 2026-08-20 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8670cb3d-acf1-3401-92ae-07a43d9371b5 | -6.17159 | -45.23335 | 2026-08-20 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 794ab41f-812d-32fd-b490-bad9b4022806 | -6.4376 | -52.74365 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4502087-8573-35b3-b031-e2ca2ba83ba3 | -7.63651 | -42.79005 | 2026-08-20 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 873bdd34-bc90-335e-98de-62476281af15 | -6.42423 | -43.06939 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53685ddc-b7cf-30fc-b7e8-adec1eccd1a5 | -7.34419 | -45.83382 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2d8828c3-76ce-33ec-837f-df9b1e753a8b | -7.28426 | -44.07291 | 2026-08-20 04:19:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 187a667c-8045-332a-882b-be742d8bdcd5 | -8.65872 | -54.59184 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d6b96df-75ea-3ad9-a148-e52331353c45 | -7.60197 | -45.17673 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b3ae492f-6cb2-3df2-8f8d-539ca5197e4e | -8.09233 | -51.66402 | 2026-08-20 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d094f3d7-206c-35ad-a39c-0a6eb29074da | -11.31228 | -45.2091 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9848c8a3-4cbb-3875-83d1-3cb61b0168ef | -8.53951 | -54.87688 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a543d6d-8771-3f82-9f9a-c6ee67f7737f | -6.24429 | -55.41939 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d0c7903-1b98-3f12-8597-357d0a1801e3 | -6.42783 | -52.7669 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fdb4fd0-8e49-37c1-b4f9-a0c0c40ee814 | -8.57381 | -54.72831 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f15b014-3a8f-3c78-999c-a7609a76faca | -6.35006 | -54.89988 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37167793-f801-3c37-8421-8cf4ab50f0d6 | -8.53347 | -54.876 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a0827c1-9364-3846-8701-f80c18cbe8ad | -8.66598 | -54.66074 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0c2c7f91-b9e8-377c-b016-907856cb90a0 | -8.67663 | -54.65756 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cc000a9-bc8d-3e5d-90e5-00db4eac9514 | -7.01972 | -45.89006 | 2026-08-20 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68d4a30a-8508-3eb5-a6bb-a0419cc611da | -6.44132 | -52.72297 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 571f0f94-936e-365e-96dc-61ab802a8026 | -5.80021 | -55.72204 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7cf09494-a57d-3dcd-bd7c-e0ce1091d981 | -8.48831 | -54.87472 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91619e57-e852-3383-a623-433c4f9a65b5 | -11.37724 | -46.37855 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e56ec3e0-e185-3d08-b5a8-0867a1a33f08 | -8.49513 | -54.87141 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b8c5a7e-beda-3641-ba84-227e03f97310 | -7.34828 | -45.83055 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ee6b1f14-4c27-3bb4-b54f-5b453a1dd1ef | -7.35522 | -45.83171 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 82ec827c-9b64-379e-bb96-5c0593067226 | -10.63303 | -51.61359 | 2026-08-20 04:19:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62daf7f1-4d0b-3f11-b7c9-6291c7da9cf4 | -5.83745 | -42.63237 | 2026-08-20 04:19:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 04c1a4bb-fd34-3167-903b-20ff054b82bf | -6.17098 | -45.23708 | 2026-08-20 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e2b90be-763d-3615-8e94-3841d4a9ae6a | -7.97048 | -44.66925 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d608dbbb-9c54-370b-ae88-4cdce8d7f870 | -5.4333 | -48.41457 | 2026-08-20 04:19:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README33.md)
