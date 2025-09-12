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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfa4efc3-696e-305f-99ed-0c3892fdeede | -11.42846 | -43.54855 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c9b013a6-c337-3b18-8289-b7745cfd97e7 | -13.25292 | -43.7691 | 2025-09-12 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a21331bd-7ef0-3a7f-8ab1-c5de40654126 | -14.04678 | -40.63295 | 2025-09-12 03:38:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b799a283-6375-3806-a3eb-9576570835ab | -11.53195 | -41.91108 | 2025-09-12 03:38:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7513db9a-2bf8-3903-950e-a16f05e0a8b5 | -12.10918 | -37.97472 | 2025-09-12 03:38:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 50.6 |
| 5a092bae-063a-3b61-9bce-84d023917aba | -13.90063 | -48.23967 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8d1dcbf4-f3e3-3a80-867e-e1b9d8795b19 | -9.78133 | -47.85526 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e97c69ca-85d7-3a57-becc-646d379c4015 | -10.83572 | -42.76193 | 2025-09-12 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 014ee486-11c9-3b1f-a7c3-6faa7d9faaa2 | -11.67859 | -46.66928 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6aec1821-5f84-303e-88ab-410df5109f42 | -14.43077 | -46.40285 | 2025-09-12 03:38:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a37556af-9b5d-3c0b-807f-9f83e48b005e | -9.72431 | -48.34459 | 2025-09-12 03:38:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b4d5f251-8bf0-3856-8edf-82376bd6a3cc | -9.04408 | -47.04599 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee440566-e3d5-3180-a747-a3ed8a4acf21 | -13.14623 | -47.1412 | 2025-09-12 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17bad6e0-90cb-3f9a-94a7-df41de34da94 | -9.45353 | -46.41703 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19180fa9-b947-39c5-8c8f-20ae74a5442f | -10.67799 | -48.65972 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6679157e-5e4a-3489-9eee-310df3013bd9 | -14.18315 | -46.20223 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea2dbafd-abf2-3adb-b30f-b9fcf3ac1ccc | -8.48522 | -47.27433 | 2025-09-12 03:38:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fae24193-38fe-32a6-b8ef-035768507b28 | -13.90741 | -48.27153 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ff719ac2-b9ba-36d9-a9ea-e418e27e8130 | -14.12811 | -45.38305 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 46e9a162-6240-343c-b4d9-b577e03e7ef7 | -12.00527 | -47.76338 | 2025-09-12 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8feff98e-c739-3a01-bada-4a00ac3669a2 | -11.652 | -46.64774 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13660f7d-4ffa-3749-a703-6dac459a43ce | -11.6905 | -46.51883 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb238956-5487-39aa-88f0-1c3f5b81d7d4 | -11.67428 | -46.6323 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6b42bb38-6a85-38dd-a03b-7ad26ff1b21a | -13.31464 | -44.09122 | 2025-09-12 03:38:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c94eecb5-acf4-3e4a-b2a9-f6108b20aec1 | -14.47214 | -46.34962 | 2025-09-12 03:38:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 719fe1cc-f90a-3803-acc3-a50bc319eaba | -11.69314 | -46.56952 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 358ad791-bbc3-3499-a23f-48200edd90e3 | -12.46968 | -47.50077 | 2025-09-12 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1f8e851-cff5-33c9-8adf-772d4cd37ee9 | -8.94517 | -46.7192 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65de08e1-3f25-3fce-83f2-a4b2881db61c | -9.66766 | -47.55937 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b651bdf5-3fea-38c2-8160-9c3ba7cb2838 | -15.44657 | -43.63923 | 2025-09-12 03:38:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 223e7ddf-b5c0-3677-8a04-6fe79d92098d | -11.66808 | -46.6313 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ad372c66-fc89-3a28-a8bd-e611a2d7ae81 | -15.72144 | -42.19372 | 2025-09-12 03:38:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a6cee66-4a89-3a7d-aa52-b02db0b9540f | -11.68029 | -46.60211 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5408bcd2-5066-3bf5-8270-4e12e9e38077 | -10.85589 | -48.16498 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56939e32-6390-31a7-8987-b20753e8f934 | -11.67228 | -46.64235 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c509939d-8241-3065-92b5-11eee7151f71 | -14.28699 | -45.08126 | 2025-09-12 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e32608e-f848-33ca-994e-3ac1d77b345b | -9.66889 | -47.55317 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45af0207-d7f5-3b69-b188-d95d9614a61c | -12.85446 | -47.95704 | 2025-09-12 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1967f8e9-4f4d-3087-939a-319a6cfbfd43 | -15.12182 | -48.09176 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6735cee2-6e40-39c5-b661-95ed33856609 | -9.03344 | -47.08927 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 591e88fe-f404-3559-b63a-7468802118f3 | -13.89834 | -48.25037 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e755cdc7-6fc9-37b9-b4d2-ed22bbcd50fa | -11.43853 | -43.5674 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7113e24a-cfde-339e-b4cf-7c671ce169cb | -14.17675 | -46.17558 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47cece12-34a3-3f58-831a-1819de9d327b | -14.11845 | -44.32117 | 2025-09-12 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05843b5f-b27b-3c41-a8d8-ac85e2b092bd | -12.82451 | -47.96678 | 2025-09-12 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c412d03d-7eae-3a2d-ab2b-fd8e3ae92997 | -9.05186 | -47.04099 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e9e7f35f-b871-3d89-a055-a43dbe2647f8 | -10.68319 | -48.65738 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b334c5c5-63b5-395c-8c61-8f1c6d2490b9 | -11.44039 | -43.56953 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0f847282-25d2-3017-bf3f-e803fde118ac | -14.17198 | -46.19855 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e0ef916-e071-3a3e-906e-2d1a57f40aae | -11.49876 | -43.6398 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 582baaaa-ee69-3827-a3b8-85e60ac29f51 | -14.17453 | -46.2104 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d0ac37b0-d055-30ab-ad74-173f5b01a8fb | -9.03706 | -47.07104 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6ecfced3-cfb7-32b6-831f-f5cedcbc926f | -9.78255 | -47.84917 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c8f333b-8cad-3149-aa10-8707ae26e767 | -9.01321 | -45.73792 | 2025-09-12 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c66119e7-6037-32bc-86a6-0a751180ca23 | -15.68289 | -47.04797 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83df325f-7ba8-38a3-8b90-60e341feda1c | -10.56275 | -43.66309 | 2025-09-12 03:38:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2056903-17e9-3b11-a144-58cd027ddc00 | -12.10513 | -44.86858 | 2025-09-12 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a82c554-3b4f-3c6a-8604-ee8894488679 | -15.11328 | -48.1007 | 2025-09-12 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f3434bf-9c7f-3827-90e0-80169b861684 | -15.48685 | -47.34271 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b56e6415-82b5-3b3a-8167-2c88216f35c3 | -14.43494 | -48.42434 | 2025-09-12 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 897a70e6-7a6a-38f8-bba5-998b416f28d5 | -10.12695 | -47.91973 | 2025-09-12 03:38:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bd017579-b847-3d94-b147-87fb10efb890 | -11.68887 | -46.55894 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 726c00da-36a7-3be1-878b-54980e8af1a3 | -13.31524 | -44.08819 | 2025-09-12 03:38:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 46c0b122-0c97-3bf1-952d-2bfc2c37b88d | -9.71294 | -48.30267 | 2025-09-12 03:38:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b112410-5dfd-3541-92f2-71dda24b1850 | -11.372 | -43.51305 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60a297cd-813c-35a7-b7ac-648f49899d3b | -11.66 | -46.63975 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| df1bfe07-f2fd-3a1e-8a46-d5887362b681 | -10.84322 | -48.16308 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3dba1c5b-6ffa-34a5-b17f-828d25f41dc5 | -11.53205 | -41.91377 | 2025-09-12 03:38:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b6ceaa54-0d7f-37cd-a294-ac722717297b | -14.12736 | -45.38292 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d22b8e1-8a12-3d6e-bc9d-de7efcab8ea0 | -9.0507 | -47.04705 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 59da5026-9155-38d4-bc2c-fbd1289cf9e0 | -15.08694 | -48.00997 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6387ce0b-b12b-3728-94aa-5483e5671ccb | -11.6787 | -46.67447 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc240197-64fb-3da1-83d7-80504ec9d771 | -14.17528 | -46.20668 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd9ab7b3-76a9-3a00-a120-4d0f5653892d | -9.03757 | -47.11589 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c108219-eb35-3419-9673-f33e9e28a05c | -14.03908 | -42.15058 | 2025-09-12 03:38:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 18cb7a82-f7bf-353f-bd56-4ac63777eb26 | -14.28517 | -45.04488 | 2025-09-12 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24ca3b73-aade-32f4-99e4-c4338cb569fe | -9.68056 | -47.54421 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44550d10-84c8-3a77-b744-cf1693866102 | -13.89946 | -48.24513 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2602f11e-7fe6-3831-aaba-47826c6996df | -11.6571 | -46.65426 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 41e23778-bfd8-3d80-ad0e-947f2289e000 | -11.6776 | -46.67408 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76d04d68-60d7-3817-99bc-62d969c296ac | -14.45286 | -47.31654 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd54164d-a834-373f-b1e2-14bbf332758e | -13.5055 | -40.55867 | 2025-09-12 03:38:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 912652d2-0d02-3ad5-8766-01c8722a1c55 | -8.955 | -46.07551 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db9e5fb9-872f-3133-b934-e29518633f25 | -10.65434 | -48.65536 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 98fc09ec-40ee-3b88-9db8-ff7438cd5448 | -11.66887 | -46.59537 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c33359d5-117b-3805-b14d-f71218164411 | -9.68487 | -47.55737 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 417d234d-2085-3c1e-bd45-6387ff648445 | -13.36493 | -41.918 | 2025-09-12 03:38:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e3074d4c-8ea5-3800-ba90-948d1e811501 | -9.45689 | -47.64829 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48ae6342-12eb-3f6a-a4b1-ccf8f1877009 | -11.43344 | -43.56649 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7203baf3-0479-3262-8c1d-72e27c3cfe42 | -14.18409 | -46.16893 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79c6af4f-d3a5-3154-99a0-cafb8849513e | -12.82551 | -47.9657 | 2025-09-12 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7527aea0-1e09-363e-93e6-aa287efd4b27 | -14.18881 | -46.20376 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43c519f1-a3d4-3b27-a13e-e8cd24226abe | -9.88003 | -46.47068 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5f3dbac-01c7-3238-a0fa-91005322eecc | -11.70728 | -46.49818 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 426b14f9-c384-37d4-81fd-eb1428b458f7 | -11.69841 | -46.51098 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c334f6b0-7bcb-3a30-a424-3a9c83c4ecf3 | -9.69015 | -47.55133 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83781db8-e1c3-3d4b-8a87-036a14aed733 | -14.74301 | -46.29187 | 2025-09-12 03:38:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c81b8c23-1d44-34f3-b660-7879d7dad081 | -11.68861 | -46.52831 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 881281c9-50b4-38af-9d81-bd10d6da79a1 | -11.14352 | -45.23688 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 53d565c2-a2a6-3385-a268-488d416b7f15 | -11.6756 | -46.56165 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README20.md)
