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
| ee10aa1f-3c53-3ffb-94ee-8d1477497051 | -10.32766 | -36.71794 | 2025-01-08 04:08:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1bf8e415-de1a-3081-96ec-090fb6c8fddf | -10.3287 | -39.21322 | 2025-01-08 04:08:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ef1d6b97-1b25-3296-9634-9179119fd9c1 | -10.32715 | -36.72179 | 2025-01-08 04:08:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 739808a3-1659-3069-804b-1935c63aed2b | -3.02446 | -40.02481 | 2025-01-08 04:08:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f769ecb4-74d9-3e4e-83a1-db861b6c9865 | -3.32677 | -39.69855 | 2025-01-08 04:08:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 22642875-b6e2-3d3d-bee1-7a3f1ec3dd5a | -5.94738 | -39.6807 | 2025-01-08 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7a3fc9a-7878-327b-ba81-54755847f96a | -7.68567 | -35.2732 | 2025-01-08 04:08:00 | NOAA-21 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9f912965-8db1-3c69-a910-8d21103e7208 | -6.59356 | -39.19363 | 2025-01-08 04:08:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e44298ff-db6c-3771-860c-1d174694073b | -5.4013 | -40.77544 | 2025-01-08 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7729bcf1-3304-3b63-a469-c36591db7e7e | -8.34154 | -35.34026 | 2025-01-08 04:08:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e10eead0-0a26-3486-9206-9ce98bfade63 | -8.90214 | -35.35075 | 2025-01-08 04:08:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5eaed892-9f43-3db7-8533-36812b0b2bfe | -4.63356 | -42.02941 | 2025-01-08 04:08:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f25748e-8af8-3cf8-9e9c-170328e71809 | -8.33698 | -35.34003 | 2025-01-08 04:08:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cce4333a-d14d-3b50-9fc0-cacaba4729b6 | -8.06784 | -35.12676 | 2025-01-08 04:08:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 67a0b5e1-21dc-38e7-b7a4-e8da11b33309 | -8.89927 | -35.34819 | 2025-01-08 04:08:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5a387edc-4643-31f1-982c-33f291b9a24b | -4.142 | -38.6196 | 2025-01-08 04:08:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2fd386c-f3de-3067-ae01-f04d5ed00154 | -5.07998 | -37.91943 | 2025-01-08 04:08:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 77ff49a0-c836-399a-9da5-1c0514739492 | -5.95078 | -39.68123 | 2025-01-08 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 70c33383-a17c-3092-b74f-645c72212fab | -7.30373 | -35.10027 | 2025-01-08 04:08:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e80c2ac9-d21a-3820-8bf1-5feab54560c9 | -10.71129 | -36.9682 | 2025-01-08 04:08:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 219fa1e0-60c0-3bf7-9b44-300a2fd55876 | -6.81298 | -38.24276 | 2025-01-08 04:08:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1de7024e-b8f3-3514-b867-2cd38af61998 | -10.70711 | -36.96767 | 2025-01-08 04:08:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b6d175bd-16d2-3866-9b7c-1dacbcd9fc7c | -5.69488 | -35.56961 | 2025-01-08 04:08:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bd405138-46fc-3405-974f-212523d56d95 | -9.05117 | -35.32849 | 2025-01-08 04:08:00 | NOAA-21 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 00bb9dbf-397e-30d0-91dd-50b324f71859 | -9.36004 | -35.50114 | 2025-01-08 04:08:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 053ccf4d-69a1-33e3-a36e-b486f59045e2 | -5.94681 | -39.68437 | 2025-01-08 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7108fe3-85b2-3e1b-8a19-b64eb08ad2ba | -9.05181 | -35.32381 | 2025-01-08 04:08:00 | NOAA-21 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 6b9c852d-6bce-311d-b180-ec30f5b20629 | -7.30592 | -35.10363 | 2025-01-08 04:08:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 60672e83-a9e0-32e5-b94c-035e1313ecf9 | -5.48199 | -39.16825 | 2025-01-08 04:08:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2096e974-70f0-33e5-8917-1864b0d07650 | -9.06092 | -35.32512 | 2025-01-08 04:08:00 | NOAA-21 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9821bc9f-db54-37a0-866e-02689b365273 | -10.53071 | -36.78007 | 2025-01-08 04:08:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a99f7176-ab14-313c-a73d-a3b685739ebc | -8.26706 | -35.38175 | 2025-01-08 04:08:00 | NOAA-21 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0b957c03-4c14-33aa-bcb3-bafbb37573c5 | -12.40217 | -40.9068 | 2025-01-08 04:10:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ada1378d-a3cc-37e9-8506-4668bb348dbe | -9.99937 | -48.49718 | 2025-01-08 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08b25e88-f72b-3f64-aaa3-e05dd38b327c | -12.16126 | -40.94827 | 2025-01-08 04:10:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e495b6cc-cc96-3eb1-adca-49f5727bfffd | -10.00008 | -48.49306 | 2025-01-08 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c3155be-f01c-3b61-b6f5-1332baf5a6dc | -12.41493 | -40.48393 | 2025-01-08 04:10:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eed60f5f-518f-3895-9a77-885e7377168e | -10.96868 | -40.4175 | 2025-01-08 04:10:00 | NOAA-21 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a28c9edf-d7be-3adc-a84b-34437199259a | -12.46542 | -46.93462 | 2025-01-08 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b636a60-4958-3a19-9f36-92f57291586f | -12.08536 | -38.01447 | 2025-01-08 04:10:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c95134f3-e475-38f5-87bf-170162df0702 | -12.08834 | -38.01178 | 2025-01-08 04:10:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fbdc4686-5725-3bb9-bbd9-01cbfe239d2f | -10.00218 | -48.49681 | 2025-01-08 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6ca70df-ae5f-325e-b8d6-f8b20a067029 | -20.64717 | -49.30819 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d278dd5c-cea2-327a-86e6-a4860127415d | -23.33858 | -46.7747 | 2025-01-08 04:12:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8446718b-1248-3f37-9b64-d0e8148633f2 | -21.55732 | -54.20102 | 2025-01-08 04:12:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13ea097a-d6e2-3e2f-8be3-4a35b7f2e528 | -20.65095 | -49.30894 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ab071ef-f304-3406-a2a4-11d21e0ca13c | -20.64806 | -49.30323 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d55ab71-9ddd-30f8-8844-a4d128d4eb1a | -23.63023 | -46.4259 | 2025-01-08 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 669fad30-d83a-31b2-ba0a-7a49ec083a4e | -20.6509 | -49.30688 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5cbfed3d-01ea-3f87-bfd8-4480aeeaac72 | -20.37834 | -45.60221 | 2025-01-08 04:12:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5068631d-1132-38a7-9f4a-2cf2f1a80cce | -21.26018 | -49.03 | 2025-01-08 04:12:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d04165d8-fec9-3c71-9430-d7887f6cd523 | -21.25733 | -49.02463 | 2025-01-08 04:12:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b785ae83-4e3d-3e07-aafd-982618b38e1a | -22.41629 | -49.66677 | 2025-01-08 04:12:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bfc03938-fd9d-3e35-94d5-fd1d9a0f9862 | -20.96045 | -49.74945 | 2025-01-08 04:12:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e2c520cc-e9a2-36df-b8e9-e09a362ab890 | -22.92246 | -45.41461 | 2025-01-08 04:12:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b1b55341-a211-3b76-8b9d-18529b0f092d | -22.53923 | -48.81468 | 2025-01-08 04:12:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9867e240-211a-34b6-a7ef-b2a053a4bf39 | -20.9595 | -49.7546 | 2025-01-08 04:12:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| bb64dddd-2e95-3059-ab33-d17770817502 | -19.5852 | -49.37223 | 2025-01-08 04:12:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d1e63f4-0655-3ec4-9d47-939db9f64a2e | -20.65185 | -49.30395 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2680d18-d761-3a7b-bfe1-76a6b8c3f0b4 | -20.65563 | -49.30468 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eeb986b0-8520-39eb-8e70-06999e4cb8a8 | -20.64711 | -49.30615 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 289095a5-20fe-348c-93ae-f686f42312c4 | -20.96336 | -49.75537 | 2025-01-08 04:12:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 6ea2ab3f-6800-370d-bb62-9662e394edc5 | -20.65561 | -49.30265 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0165a71-516c-36cc-9290-6946f097313d | -23.52027 | -46.97515 | 2025-01-08 04:12:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a633b162-eb17-3268-ba3f-e69b3f579ead | -20.65182 | -49.30193 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97158e7c-d36f-37da-b48f-b5de82aff12e | -20.65468 | -49.30762 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50f90465-82fb-3321-935b-5e312cb77579 | -23.3392 | -46.7709 | 2025-01-08 04:12:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aac18ac6-96eb-3813-b4e5-ce7fde3a738d | -21.19467 | -44.93616 | 2025-01-08 04:12:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2b07026a-72c0-3886-90fa-6310300ff066 | -19.94675 | -44.71646 | 2025-01-08 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d5bf608-89af-34f3-b93c-313618fe3f5c | -20.64803 | -49.30122 | 2025-01-08 04:12:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be0fc9d7-c8b2-3756-92c5-3a2dd7d487e6 | -20.96431 | -49.75023 | 2025-01-08 04:12:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 383b4959-1c6e-38bc-a96a-bde46250e784 | -21.55799 | -54.19788 | 2025-01-08 04:12:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c03086c-24e3-361a-9c7f-36e1ddaaf489 | -22.78731 | -43.75583 | 2025-01-08 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 65623a92-2aea-36b2-93c1-6dfa1c0e69dc | -23.79171 | -50.27716 | 2025-01-08 04:14:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3ff3c088-3da8-3180-8840-f7454d665634 | -23.79831 | -50.2841 | 2025-01-08 04:14:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| fcd348bd-3bf9-3631-8e97-565cf9ea751a | -23.86835 | -50.22121 | 2025-01-08 04:14:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f2883629-3499-3b24-8eb5-6721e96ebc34 | -23.79551 | -50.27798 | 2025-01-08 04:14:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 03cda615-1166-36c5-b918-fc8ae9a646bd | -24.69086 | -50.31921 | 2025-01-08 04:14:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3a946520-a1e8-30b2-8700-8dc7ce169b25 | -23.7736 | -50.28944 | 2025-01-08 04:14:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aac5480d-34e0-32c0-9952-54fcc10aa713 | -23.86847 | -50.22431 | 2025-01-08 04:14:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7a207dd1-e003-3fdf-b4d0-cd5eaa7db37e | -23.79928 | -50.27892 | 2025-01-08 04:14:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 2d689238-060a-3f90-b5bc-8e2d9e15ca1e | -23.79269 | -50.27195 | 2025-01-08 04:14:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 086040ed-109d-3f8e-a124-0b7dbe0929f2 | -24.68714 | -50.31827 | 2025-01-08 04:14:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7164f5f9-c8d4-36d7-be7b-62f91976eede | -24.08027 | -51.0209 | 2025-01-08 04:14:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6c0a640f-7cbd-32f3-94f9-34304d6fcfac | -30.3254 | -53.41552 | 2025-01-08 04:14:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 91f4f566-a660-31c1-8dcc-112c0871ced1 | -24.08134 | -51.01538 | 2025-01-08 04:14:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9026fedf-e3f7-3735-b957-02572fc07053 | -23.79453 | -50.28321 | 2025-01-08 04:14:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 8af526af-242d-3d18-a22b-a648f1728345 | -23.79648 | -50.27279 | 2025-01-08 04:14:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 4dba88ac-02ad-37cd-bc45-314785f974b9 | -24.2439 | -50.73857 | 2025-01-08 04:14:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 13c39ae5-7301-3ed5-8da3-63df6cae028a | -30.32141 | -53.41435 | 2025-01-08 04:14:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 1498ec5e-58fc-3ad1-8898-72be53058244 | -9.04798 | -35.3248 | 2025-01-08 04:18:00 | AQUA_M-M | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 27.2 |
| bedb4a26-73f5-30a3-a74e-f611458c69d2 | -9.04984 | -35.33225 | 2025-01-08 04:18:00 | AQUA_M-M | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 2bb335f0-b5b7-3962-9c3d-349f22e339e0 | -9.05291 | -35.31418 | 2025-01-08 04:18:00 | AQUA_M-M | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| b25f3e0d-1410-3b34-83ea-3fa13b873642 | -6.54072 | -35.28619 | 2025-01-08 04:18:00 | AQUA_M-M | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 35.9 |
| 2ae4c7fa-05d6-302e-8428-df65557f3a37 | -2.60268 | -54.18001 | 2025-01-08 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8f0dae9-84ae-3f93-b999-32189a9056ab | -1.28092 | -53.17854 | 2025-01-08 04:31:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7613a6b-c41f-3647-87ed-37b47b2bfae4 | -1.95029 | -47.91312 | 2025-01-08 04:31:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6ec74c0-d3a5-3a2b-9a76-1e26e9ff599b | -1.01622 | -47.78917 | 2025-01-08 04:31:00 | NPP-375D | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24453e43-a1a0-33a7-956e-c65222f2b3f2 | -0.29036 | -50.42841 | 2025-01-08 04:31:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b69062cd-d78f-3300-8f5a-b07ccfe670bc | -1.01287 | -47.78865 | 2025-01-08 04:31:00 | NPP-375D | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README3.md)
