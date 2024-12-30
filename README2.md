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
| d8c9878d-ced8-37ab-898a-8fcfbbb13c01 | -4.90531 | -41.11168 | 2024-12-30 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 84fea657-e7b5-3442-aaed-efc56653e713 | -5.25281 | -39.41753 | 2024-12-30 03:59:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1f8fc83d-50b6-3eeb-8460-6160817f68d9 | -1.858 | -45.54181 | 2024-12-30 03:59:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e70e6048-91f2-34f9-b231-a374517ad689 | -4.13687 | -40.84686 | 2024-12-30 03:59:00 | NPP-375D | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 768e0bff-225a-3d9d-a069-f6f86cbf4f8c | -3.46421 | -39.5834 | 2024-12-30 03:59:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9d9406ed-6e07-3776-aeb2-adbee3f0aebf | -4.90869 | -41.11221 | 2024-12-30 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8c56e493-c88b-3a66-8c99-b59c10e868b8 | -1.65141 | -45.86802 | 2024-12-30 03:59:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1e0e6e0-1ebf-3489-8f43-a3ec9478182e | -4.71994 | -38.43214 | 2024-12-30 03:59:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1299beab-0a30-3309-ae2a-9e310b4f083c | -1.85871 | -45.5374 | 2024-12-30 03:59:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da9d4672-684f-3c12-868f-2749df4d0a48 | -2.88208 | -40.05772 | 2024-12-30 03:59:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 57e6e138-4f74-3e66-8661-5d5cac07090b | -4.90473 | -41.1153 | 2024-12-30 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 681ca3ac-c9eb-3930-b6a2-a68d4fce8957 | -2.90825 | -40.49152 | 2024-12-30 03:59:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aa389013-78ce-3515-8efd-25d9222f01e6 | -4.56954 | -41.30783 | 2024-12-30 03:59:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c7e7c193-e3a2-3a60-ad02-75db8079682a | -3.5649 | -40.84301 | 2024-12-30 03:59:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2c98bd96-bc9d-3d5e-b1bc-3dd27d1b0925 | -4.89921 | -41.09991 | 2024-12-30 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f1c6a8da-88fe-31f6-a095-8d60403bb4ab | -2.80077 | -41.78333 | 2024-12-30 03:59:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d09e3f1-d5be-3e71-ad51-003d1441faba | -2.90882 | -40.48796 | 2024-12-30 03:59:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 68a2d842-7e1d-31db-8393-2c8757600720 | -4.9026 | -41.10043 | 2024-12-30 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cadac690-a525-3995-9df2-5dac9c6de7d8 | -2.87874 | -40.0572 | 2024-12-30 03:59:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3b5a950-2f34-304d-852e-088bfd22a640 | -1.64755 | -45.86264 | 2024-12-30 03:59:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02e83ffe-e94c-3e19-893f-dad0913f67d5 | -1.64705 | -45.85955 | 2024-12-30 03:59:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2c5609b-7b36-3b9d-a0c2-07d4c8c9b301 | -2.80429 | -41.78389 | 2024-12-30 03:59:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf423099-9ea3-33df-8cf4-e069e95b046a | -1.65087 | -45.86494 | 2024-12-30 03:59:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62bae5d0-c62f-36f8-a5ca-57a7778b9615 | -4.90706 | -41.10081 | 2024-12-30 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| dc837b75-b554-3672-b542-d631705f6d13 | -1.64627 | -45.86425 | 2024-12-30 03:59:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cf3e6b3-635f-37e1-b502-9c2a854ec48b | -4.90589 | -41.10804 | 2024-12-30 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d6fca832-3ba9-3aab-9f94-70c4689b86d0 | -3.50335 | -39.31349 | 2024-12-30 03:59:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 300c4110-3d5b-3504-ade2-62c293c2f2bb | -4.90928 | -41.10858 | 2024-12-30 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b8fbbfd2-b660-349f-851f-5180f0791ba9 | -3.46475 | -39.57995 | 2024-12-30 03:59:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eceebdd7-04e3-3d61-a014-359c0eac2735 | -4.90368 | -41.10028 | 2024-12-30 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 3cfed128-94b5-34bf-b7da-cc006d22e699 | -1.64296 | -45.86188 | 2024-12-30 03:59:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b97ec4-0074-34c0-998a-ab1db26a9485 | -11.9632 | -44.31671 | 2024-12-30 04:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c660ac4-ebfa-3e34-89be-953778f8c044 | -6.94672 | -43.0078 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ef1217b7-cb46-3978-9320-f7b83d2952fd | -7.76789 | -34.94177 | 2024-12-30 04:01:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| c2d7627e-3ea6-31fe-a375-2475b77305c1 | -7.15246 | -35.04352 | 2024-12-30 04:01:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c036decb-8ea3-3c35-8c0f-ab64971d13e4 | -5.34128 | -40.56661 | 2024-12-30 04:01:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8993f0cd-33e1-3ffb-b950-22d656607601 | -5.94372 | -39.68957 | 2024-12-30 04:01:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 142a3bfc-2cec-3bdc-8252-20b296054f8f | -7.75956 | -34.94057 | 2024-12-30 04:01:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| deb810f3-d3e3-387e-b586-059950557654 | -7.14429 | -35.04211 | 2024-12-30 04:01:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 50b25003-e212-3fc7-aab4-c706d6854c9a | -9.84225 | -37.12222 | 2024-12-30 04:01:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 16120b1e-6db7-358a-aaaa-258078bdd734 | -7.72761 | -40.17687 | 2024-12-30 04:01:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d17a135a-31fa-34ab-87e2-a6b20ddc285d | -5.25533 | -44.98486 | 2024-12-30 04:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cbae2262-a88d-3fdb-994c-b55259f8cd0b | -8.5822 | -41.12156 | 2024-12-30 04:01:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 02f25de0-d973-32a8-b9e0-1a800a7cba76 | -7.76316 | -34.94505 | 2024-12-30 04:01:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 986ada01-76b7-3f5f-92c5-9b29ffb136ad | -8.37359 | -35.69627 | 2024-12-30 04:01:00 | NPP-375D | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b046abcc-8285-35ef-8c01-87e39cd45a1a | -7.23408 | -35.02952 | 2024-12-30 04:01:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4a95a095-5887-3174-9ffd-ab8363436d59 | -8.37034 | -35.69059 | 2024-12-30 04:01:00 | NPP-375D | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d0d38277-5c40-36e2-bb79-4878d54df547 | -11.96107 | -44.31818 | 2024-12-30 04:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bdc6a9f-767b-3472-8e74-682fbbd011f7 | -5.25594 | -44.98129 | 2024-12-30 04:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e67eae7-acd9-3b2c-a3f7-38afcaba31d4 | -6.9864 | -43.0256 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 133589b9-c8b4-3b4b-96b6-5a4eb38425fe | -9.4873 | -40.96102 | 2024-12-30 04:01:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| deac8a64-9dea-3170-8932-40f8e1396688 | -7.76372 | -34.94118 | 2024-12-30 04:01:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 88d90116-0f9f-324d-a191-f6db2f39cda4 | -6.97591 | -43.00837 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c3c7de1f-fdea-30af-b7e0-0d7ee8dc7803 | -6.97482 | -43.00709 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0b1ac8a6-a705-347e-a6d0-677b18a2cee9 | -6.95029 | -43.00837 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 27669031-623e-3d59-a22b-3737bffecf1c | -7.76013 | -34.93672 | 2024-12-30 04:01:00 | NPP-375D | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3aa43723-47d9-31ec-b5f1-2f18aead40c7 | -6.95808 | -43.00547 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| edfbd1c4-faf7-3894-8805-f4977f6237ca | -9.84356 | -37.12014 | 2024-12-30 04:01:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cc5486d7-b711-3902-9dec-fff90027d280 | -7.23354 | -35.03317 | 2024-12-30 04:01:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fc835efd-94b6-3606-be02-05184e1c32c8 | -7.76429 | -34.93731 | 2024-12-30 04:01:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fb333d98-42b9-3fa0-8df0-3f28af31ae0f | -6.98997 | -43.02617 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6d3570b8-dfb3-37d2-b823-18a3d874d7d5 | -5.25125 | -44.98418 | 2024-12-30 04:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9e59db38-8262-3b86-a5db-9a969c99ae7e | -6.96165 | -43.00604 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 212e4210-1800-3391-b51e-00dead6be992 | -6.96521 | -43.00661 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 84e98f40-b337-3c41-a4e1-ee475d714bae | -8.3696 | -35.69571 | 2024-12-30 04:01:00 | NPP-375D | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3106a52c-32a5-32f4-acd7-3f8d6c98b922 | -6.78091 | -38.59431 | 2024-12-30 04:01:00 | NPP-375D | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5b080755-55a1-3697-93f8-1ff9cbe2f3ea | -7.67149 | -46.10239 | 2024-12-30 04:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 332dfa7f-7569-3035-a43a-0626bbadd5c3 | -6.97656 | -43.00431 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 59d8aca8-6fd1-3361-ae49-0b985da3b388 | -8.00827 | -37.16927 | 2024-12-30 04:01:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 567944eb-ec64-36ff-8ef3-42a32dfb2790 | -6.96587 | -43.00257 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7d061b51-00c6-3b0d-9c70-bf611c812aff | -6.973 | -43.00372 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dc259365-5fe4-3b6d-b5f9-8e590bc9aa94 | -6.96878 | -43.00719 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5f1bf0c6-0c68-351b-a0e8-a4d3af186505 | -9.08781 | -46.36681 | 2024-12-30 04:01:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c22db668-8102-3fe1-819b-ae67db5e7aa1 | -11.2471 | -44.48003 | 2024-12-30 04:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06dc0f82-5892-343c-9718-bcd9db688b9a | -6.55091 | -38.61507 | 2024-12-30 04:01:00 | NPP-375D | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6efcd3bc-3c5c-3b3a-87d8-81ddb5037b5a | -6.5739 | -40.19763 | 2024-12-30 04:01:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5c181f46-182c-3bef-91ef-cf14828a5af2 | -7.7626 | -34.94886 | 2024-12-30 04:01:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c8c24ed2-2779-314c-9eb1-bc8e4bd397e4 | -7.14377 | -35.04573 | 2024-12-30 04:01:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 92d3fa2e-30e7-3792-874b-e2ac3c9d82ac | -10.80791 | -41.67551 | 2024-12-30 04:01:00 | NPP-375D | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 0ba386e5-5c1a-3d54-8a68-15f83fc8984e | -10.06689 | -36.14254 | 2024-12-30 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6c90592d-9a4c-306a-bfbc-d286eeb60a42 | -9.84293 | -37.11769 | 2024-12-30 04:01:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d11f1301-6b01-387b-9c68-5a7e340fc8b2 | -6.95873 | -43.00143 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b27b15b9-ec55-3c66-91ae-76eeb8fd3be0 | -6.96943 | -43.00314 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dad688d2-5b50-32f8-b910-eca8ac63dbdd | -7.15654 | -35.0442 | 2024-12-30 04:01:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3c1584ba-fd84-3a9d-a974-f56627ad35fb | -9.49473 | -35.95568 | 2024-12-30 04:01:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 170af46d-6067-3fe9-988d-262b1febcfe6 | -7.759 | -34.94441 | 2024-12-30 04:01:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6155d521-7c14-30d2-a582-57d64b0c2c27 | -7.15298 | -35.03985 | 2024-12-30 04:01:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ed61d30-89f2-3e33-a2f9-1568c1f11ae9 | -7.14786 | -35.04643 | 2024-12-30 04:01:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f333418d-0b47-38bb-821b-e244973a70df | -6.96682 | -38.65567 | 2024-12-30 04:01:00 | NPP-375D | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 993e8d11-5501-3058-9739-65ad29ad9e24 | -7.77692 | -40.4632 | 2024-12-30 04:01:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b99f91d5-984d-39f8-a462-c225145a1feb | -10.8283 | -42.69634 | 2024-12-30 04:01:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 06ff2a1b-b02c-3f83-8cde-9ef93c4196f3 | -6.97234 | -43.00777 | 2024-12-30 04:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| fd458b32-a278-3cb2-b1dc-d12c46f82a3f | -7.14838 | -35.0428 | 2024-12-30 04:01:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 72539edb-ad56-3730-96ab-19021dae10ab | -7.1489 | -35.03915 | 2024-12-30 04:01:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e5904c46-78d9-319e-bbb2-00d25b7ccd68 | -12.37359 | -52.49338 | 2024-12-30 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d09c7142-f028-3dc6-8ef1-584d79f98d36 | -12.36767 | -52.4921 | 2024-12-30 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d4e45bda-7382-39d6-aa33-4a27bd3f35c7 | -12.36677 | -52.49659 | 2024-12-30 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a4fc5728-1fc7-351b-b24d-03c796ba37cc | -12.3727 | -52.49787 | 2024-12-30 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 71540e2c-c653-3b27-a773-6dac670a232d | -12.37448 | -52.48892 | 2024-12-30 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b6d471ef-eb3e-334f-a29e-ef76f1bb982a | -23.59278 | -47.43865 | 2024-12-30 04:06:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README3.md)
