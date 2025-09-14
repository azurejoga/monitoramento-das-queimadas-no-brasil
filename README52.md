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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c4d47b6-f926-34d9-8adb-5401baadb2f0 | -24.08054 | -51.06629 | 2025-09-14 04:44:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b5ca7fc8-9a57-39c0-84a5-110524890273 | -22.18254 | -49.61696 | 2025-09-14 04:44:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6ad73c3c-d201-3a65-8a5b-1fac73e183ba | -20.2633 | -57.1632 | 2025-09-14 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4984520-b509-3ecf-aa1c-63b46ef5b3d1 | -20.56868 | -54.5937 | 2025-09-14 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e88d782e-53b1-3d28-9103-3693c4cd0d10 | -22.52009 | -52.99593 | 2025-09-14 04:44:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f3cd459d-43e7-3ff0-9a16-87a712c43a6e | -23.13918 | -49.65213 | 2025-09-14 04:44:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6a567574-8142-31e8-bd17-54d912ca267d | -22.17583 | -49.61121 | 2025-09-14 04:44:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9a2bba52-f621-3c54-9b5a-be77427ea4d4 | -21.65603 | -50.19921 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 78e6b6e3-e702-305f-9594-cd6e090fc17f | -20.56932 | -54.58984 | 2025-09-14 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 369e1f5c-af02-35dc-8ca8-dcb83178c945 | -20.77234 | -56.93978 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f0e3185-4412-3239-a973-c3c63a67b5b8 | -21.30714 | -48.55485 | 2025-09-14 04:44:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60457444-5812-3600-b1d1-d2016d30dead | -23.37547 | -46.7799 | 2025-09-14 04:44:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 257074bc-b4d7-3b0e-b533-7631fa58cc88 | -22.72655 | -49.89644 | 2025-09-14 04:44:00 | NOAA-21 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c28cf52b-851c-30a5-91d2-e56690ce790f | -22.66409 | -53.12067 | 2025-09-14 04:44:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 340322c3-012e-30ad-af61-93ef800a0f33 | -20.12727 | -46.87275 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7331d6c7-5066-393c-9f80-65e81d80b908 | -25.17725 | -50.07619 | 2025-09-14 04:44:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 80be3d4a-c3c4-3aa4-bf6c-fa7c14767491 | -21.65895 | -50.12514 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 51dba14b-b2fb-3667-a272-b9ec9891e36c | -21.65955 | -50.1208 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b22148ea-b669-3f38-adfb-829c744ece3f | -23.15598 | -47.57704 | 2025-09-14 04:44:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 95a30720-5b98-3c29-921a-db6166646614 | -22.23099 | -48.60031 | 2025-09-14 04:44:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e0b2c45-d18c-3c78-9556-736dc1c7b64f | -21.75352 | -53.31108 | 2025-09-14 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fb9394b-f009-3794-8e2e-ce27c9f9359a | -20.09052 | -46.8955 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 941acdd7-61c5-38ea-8efa-5dd94aa38ac2 | -21.59393 | -50.96749 | 2025-09-14 04:44:00 | NOAA-21 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b51a7603-66c7-3663-abb6-1bff94a8d626 | -21.62951 | -46.81257 | 2025-09-14 04:44:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 787b3d0f-b726-3fb0-98d0-d86c9a731c11 | -22.19471 | -49.60991 | 2025-09-14 04:44:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7ee500e2-fef9-348c-ba67-d6805997f59c | -23.66002 | -47.59612 | 2025-09-14 04:44:00 | NOAA-21 | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 613e61fc-0128-3409-918a-14a18885f544 | -21.26661 | -57.90206 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2da63de8-9f0b-30cb-b8fc-57775910d9e0 | -21.0786 | -47.11419 | 2025-09-14 04:44:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d9e23d3-4bd7-375e-b459-eefbcbda0c2b | -22.99724 | -49.9363 | 2025-09-14 04:44:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3d84897c-2c95-319d-a563-f65c13397600 | -23.66047 | -47.59846 | 2025-09-14 04:44:00 | NOAA-21 | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4139780a-4c72-3e20-b8ca-40af9baa3f31 | -23.61906 | -50.77761 | 2025-09-14 04:44:00 | NOAA-21 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 03f5477f-b725-30f8-bae1-9f2c93cd44b1 | -21.62904 | -46.81666 | 2025-09-14 04:44:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 47dd161d-cc34-3de5-8e5b-8518c634a307 | -23.47893 | -50.85238 | 2025-09-14 04:44:00 | NOAA-21 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5ba59804-d776-39a6-a91c-98301dee21fe | -20.79121 | -56.9629 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf99c610-b587-37f4-9ba1-0626d79931e4 | -23.84117 | -55.18629 | 2025-09-14 04:44:00 | NOAA-21 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c16c6a29-897e-35ae-9d06-9f3f48a54f82 | -23.6595 | -47.60042 | 2025-09-14 04:44:00 | NOAA-21 | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e79de096-e1c8-33df-8d5d-87dc52b2a346 | -22.78886 | -46.79828 | 2025-09-14 04:44:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e59ffde8-2fd8-3277-a898-4ca923df25f1 | -20.90589 | -55.18512 | 2025-09-14 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a14db8c-bc75-3ec3-83a2-aceb0ffdd13f | -20.26708 | -57.16397 | 2025-09-14 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75afbcb5-d406-3106-98eb-2b1c6dd15e50 | -20.90932 | -55.18578 | 2025-09-14 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9674897-eabb-3b88-a2a9-cc6128feb351 | -21.64836 | -50.20231 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c4514129-f2f2-3924-88cd-2d2a66ccefb8 | -22.6128 | -47.6635 | 2025-09-14 04:44:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2b0e3a9f-a814-3386-8a9a-974bf4f52c64 | -20.90448 | -55.17255 | 2025-09-14 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b308ae0e-4feb-33e5-8746-26ea09f687d5 | -20.95773 | -54.98196 | 2025-09-14 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b179861-1967-3d33-89df-35c8ac2fdc93 | -27.31803 | -51.85112 | 2025-09-14 04:46:00 | NOAA-21 | PERITIBA | SANTA CATARINA | Brasil | 4212601 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a844ab38-f559-3942-aa72-f4b888f596e7 | -28.88367 | -55.13811 | 2025-09-14 04:46:00 | NOAA-21 | ITACURUBI | RIO GRANDE DO SUL | Brasil | 4310553 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 2da28fb0-be1a-3ff8-b769-05577b026cc4 | -28.96013 | -52.78022 | 2025-09-14 04:46:00 | NOAA-21 | ESPUMOSO | RIO GRANDE DO SUL | Brasil | 4307500 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| bea47c26-6887-320c-9161-348713807bed | -28.73178 | -49.16724 | 2025-09-14 04:46:00 | NOAA-21 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 23c4b295-9a6e-3bb8-a706-3649b3c51c63 | -28.43426 | -49.38735 | 2025-09-14 04:46:00 | NOAA-21 | LAURO MÜLLER | SANTA CATARINA | Brasil | 4209607 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a5b04e3d-1631-3375-b84d-032fd9476023 | 0.5887 | -51.90321 | 2025-09-14 05:04:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29e22e28-fbc1-3b9e-a48f-a8075df8b11d | 3.00214 | -51.44565 | 2025-09-14 05:04:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79d9949d-44fc-392b-893f-7b86a42bf1e9 | -3.79549 | -47.58293 | 2025-09-14 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fcfdbee-7a7b-3113-beaf-192e6349bb43 | -8.13783 | -43.66767 | 2025-09-14 05:06:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6485da73-9ab0-397f-a6cf-8d51a1b70427 | -3.07477 | -48.82031 | 2025-09-14 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b82844f-9959-30b6-85ab-bf5103fa86c7 | -1.58666 | -55.85249 | 2025-09-14 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf886a24-6aba-3841-b0e7-82fe5c32bf27 | -6.68235 | -45.52264 | 2025-09-14 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b53ccc99-d4b5-3aa7-9eda-d5d843da9a79 | -5.79066 | -43.89217 | 2025-09-14 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15d967b4-a1ea-3445-a395-b1793974291b | -5.79614 | -43.88757 | 2025-09-14 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 90b9e2f3-90e6-3ff7-b499-9327229d623e | -3.22891 | -47.62751 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e377e877-e8e7-362d-87ee-e2e1a1c4090d | -4.41229 | -47.60701 | 2025-09-14 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 299f136d-9a61-3d64-8805-3570f43d1e5c | -6.33437 | -43.87306 | 2025-09-14 05:06:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a66ea7a0-7613-3679-9a73-0ee72f7369df | -4.28389 | -56.33246 | 2025-09-14 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5363cce4-8b45-3a4a-b805-9f8d205b0553 | -3.22413 | -47.62678 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cddfc698-dc3d-3662-8bb1-bb165045720d | -7.3068 | -43.94274 | 2025-09-14 05:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4c48c8a-7008-31af-b969-d15e016eedbd | -6.87963 | -45.63219 | 2025-09-14 05:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69c4f652-dec0-3d5d-b0c4-f300036054f9 | -3.73737 | -55.94328 | 2025-09-14 05:06:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6139d475-c7e1-3a02-a2f2-d63769885ae2 | -4.48686 | -48.11494 | 2025-09-14 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bf364c60-7071-3394-bdc7-58bf17991db9 | -7.31388 | -43.93892 | 2025-09-14 05:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6168f8ac-64b0-3f8a-a09f-220e9eab65ab | -3.22357 | -47.62927 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc3e959e-ff53-3544-8ca2-ff310841e229 | -5.12896 | -45.11711 | 2025-09-14 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac759f59-c9d8-355f-af1f-a6014b68694d | -1.59002 | -55.85301 | 2025-09-14 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dec13d33-ab71-3a56-aa91-a0a70ddf5726 | -4.29639 | -56.10355 | 2025-09-14 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17cb56cb-2572-3aff-a58c-2c0515169ebe | -1.22734 | -54.12064 | 2025-09-14 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 422b40bf-1874-3ee9-9c72-626fa6383439 | -3.22339 | -47.63187 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49cef8dd-046d-3fbe-b20d-75011c9fcb96 | -6.11161 | -45.93153 | 2025-09-14 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfd0cfd7-a4c5-3ae5-bed2-299b4595f1fd | -7.31459 | -43.93356 | 2025-09-14 05:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fd9dd58-63ff-37de-8730-28eba7d2af45 | -3.60145 | -47.51286 | 2025-09-14 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 98938f09-d1a1-3910-916c-240c1f33a35d | -3.60067 | -47.51815 | 2025-09-14 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 6e9ac067-d27b-3c8a-a5f1-7b3bb48b3e08 | -5.96222 | -43.2191 | 2025-09-14 05:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0755c810-dfe8-3165-8758-272d65b081e3 | -3.59177 | -47.51139 | 2025-09-14 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04b4f260-5e8a-3060-8b0a-8bad8ee4e21c | -5.20417 | -44.31746 | 2025-09-14 05:06:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d683158b-21b8-3d3e-bedb-ae4bcc664df1 | -3.22756 | -47.63504 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b2c4c98-20b6-3856-a6c4-5b92bbf08236 | -8.13461 | -43.66654 | 2025-09-14 05:06:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92630b04-b7de-38f3-a040-5de5141713d0 | -3.22816 | -47.63258 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b936bccb-c6a5-3342-99fa-d0cfcb6eaffb | -6.68294 | -45.51839 | 2025-09-14 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 117c77cc-a13a-307c-a569-9787684164af | -3.59662 | -47.51212 | 2025-09-14 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 75510fe3-99ee-35ec-8158-2a277c550ed6 | -7.30748 | -43.93754 | 2025-09-14 05:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c2e9ec2-0242-3024-aa7b-c63e0536b00f | -5.77147 | -52.35323 | 2025-09-14 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edc3bdea-7858-3cd2-b2de-7d72dee55cf9 | -3.21572 | -47.12341 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 35909339-8274-3a9e-95fe-c61f11aeba0b | -7.5246 | -47.63659 | 2025-09-14 05:06:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d42e9ad5-0830-3932-a76c-06934770c48e | -3.23052 | -47.12584 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bfd5799-ebf3-332a-be49-9c6402010cd8 | -3.00792 | -47.83427 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d0b547d-51d8-36ed-94bb-90131b472e0f | -6.67773 | -45.5133 | 2025-09-14 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f012aa4-8fc4-33da-8311-2a59327c2633 | -2.30293 | -48.14528 | 2025-09-14 05:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12bce809-1993-32be-a3d0-88328c135e64 | -2.25912 | -47.84609 | 2025-09-14 05:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 493f36fa-6e8a-3c29-994c-593622076ebc | -6.1111 | -45.93512 | 2025-09-14 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29e4ccbf-58ae-3519-b0e9-a1736cad54d6 | -3.22913 | -47.62492 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18fddb4b-9251-3738-beda-c055608d7795 | -5.79133 | -43.88718 | 2025-09-14 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9044d81d-5d8f-31e9-be05-4785a0759749 | -2.25839 | -47.85091 | 2025-09-14 05:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5e587ad-83b9-37de-a9fe-bc85d16d250b | -3.22065 | -47.12422 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README53.md)
