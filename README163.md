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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c314b34-971a-3b20-b1de-1d2f1d6c517c | -8.03786 | -54.89469 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3b97a134-3af2-3d5a-8515-aa4940700eff | -10.82591 | -57.22879 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 141741f9-e050-37f9-ac83-758ace92baa1 | -9.19106 | -45.84682 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 59263726-b732-3139-a1c3-fb6546a37c80 | -6.34952 | -45.80782 | 2026-09-28 17:09:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 634a9382-03dc-3fa2-988e-a61e8770780e | -5.12919 | -48.68879 | 2026-09-28 17:09:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3dcef344-d1db-3ad1-9716-725da2612bb3 | -9.65494 | -42.31765 | 2026-09-28 17:09:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 09eb5819-de60-323c-b739-297cacc38912 | -10.51493 | -45.36213 | 2026-09-28 17:09:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 930bc05d-5601-3201-957d-0ad76f6fbf96 | -6.8969 | -52.48277 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5604a71a-ca09-34f6-9c78-e217ac6dd463 | -12.37406 | -50.24009 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 46a342cf-2b9f-3163-aec9-204a65d1d119 | -8.03072 | -54.89224 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 659071d0-34b5-355e-9084-1ba461ac736f | -11.55673 | -47.39199 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c8fdec26-669f-31c9-bd02-c5209d6ef88c | -8.97479 | -44.14871 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| dd5074d7-8151-3fcf-bebb-4e792d00732d | -6.16773 | -52.91455 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e443f95a-924d-3bf0-aae1-c6f6b45bc1e9 | -8.03733 | -54.89122 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6312026a-ef25-3bc0-862c-9158e3c27ea1 | -8.67151 | -45.37866 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 96a852f4-5946-3490-88c1-7eef6f3c4aac | -8.17825 | -44.4386 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2fd453e1-455f-33c8-81e1-3016d25fe05a | -9.76284 | -44.84878 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ce4e0ef0-df0b-3d62-8234-507f8c19a49d | -8.26751 | -54.73025 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5feb7e1a-3907-3ad5-abe2-0881e11c47c5 | -6.14948 | -51.57327 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fd9eebaa-a99b-304a-870f-25bd06c8169c | -10.06639 | -59.41433 | 2026-09-28 17:09:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 225802ca-f121-3357-a0c0-d97ea0930282 | -9.40487 | -46.38718 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 52e49dda-711d-30e7-82d1-29c15eb8743c | -12.13433 | -50.34688 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 8c0f21b5-00cc-3732-aa82-0dc5381ffe3e | -10.39127 | -43.20725 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b3c9707d-770e-3864-8536-ebe2ccb013b7 | -12.7624 | -52.8162 | 2026-09-28 17:09:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7e49bc41-72dc-3f20-b18e-22ad8ab364aa | -8.67517 | -45.37458 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 765666dc-d180-384c-9ce3-88a443270f26 | -11.86598 | -50.88403 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8d673aa0-59b2-32c4-a8e4-d13068caf893 | -10.71001 | -60.73281 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6d9f3c08-356c-3550-bc36-e2c226616256 | -9.98153 | -45.34842 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9972d024-92a8-3a6a-90f6-cffcb4d89130 | -9.09206 | -46.83309 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1aa65f6a-b64d-3690-aafc-0593ac74e3bc | -10.91827 | -43.86163 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 851fd4cc-8ea6-3e00-a698-7381b34831b1 | -8.77204 | -45.92318 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce0bb73a-3b73-3f30-9827-cba1029f7a08 | -9.77169 | -44.8372 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ef5e09fd-f908-3bc8-bab0-372aa9c03940 | -9.45056 | -41.82149 | 2026-09-28 17:09:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 42.5 |
| 194b5dc0-ece8-3b0c-9707-48b05f57e936 | -10.83691 | -60.74236 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d912b446-d6e9-3486-9ed4-daf23b357734 | -10.09434 | -50.39267 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c8144e8a-817c-3712-a008-612c91bed6f3 | -10.90436 | -44.65401 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 93aab4b0-0c8c-307a-b531-acf8e242c89e | -8.98355 | -44.15775 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| dfbfd38f-9360-3106-bacb-2fc139dcbf23 | -11.75967 | -50.76229 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 26863c61-1ca5-34d0-9b5c-8f132dd5d685 | -9.3327 | -45.36535 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.0 |
| b5ef201d-4917-3239-bb23-133929426dcc | -7.37745 | -55.19802 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d81e27b7-8a4f-3900-81b0-d464e1e7ff1c | -11.74192 | -54.51196 | 2026-09-28 17:09:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 6dab4048-fd2b-3fdb-9f41-efa514850512 | -9.68216 | -45.5686 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 682a9cf8-8fc3-30ae-bb68-0550685428e7 | -11.07971 | -46.0871 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1f740d6d-ec50-3027-8fa9-32ce9b3db726 | -11.64949 | -50.68539 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 24daca33-f667-3a96-9a2c-779accc48b6f | -10.96064 | -50.65179 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef202b2b-bb74-35d2-bde4-0fec28a49d56 | -8.28553 | -54.71268 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 62fac50f-92e0-3972-8525-664886692728 | -8.66428 | -45.37652 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4a60d6c8-366b-3fba-baa5-246611d03a1b | -11.87254 | -47.10014 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 51e7fc87-458a-3f6c-b11f-e4723d60141b | -9.438 | -46.54317 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 76f9e7b8-e747-3d13-ab06-cd71ec4c7272 | -8.73876 | -44.91002 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4937d65a-ef7f-369a-826b-8e4b433051b0 | -5.48546 | -45.30664 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0461c2e2-deb4-3334-9008-53fe6a137711 | -11.71735 | -50.66562 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 61a3e935-ae0c-350b-a11f-71df3fd9f3fa | -9.13346 | -56.55753 | 2026-09-28 17:09:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cf6ce261-8969-3de3-bce9-aea551461aa1 | -12.07384 | -48.53204 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 927239d9-d374-399b-aea8-31056a7db929 | -10.96362 | -50.69295 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9061ffbe-9404-3c21-80a4-5fee6f15e33f | -8.63939 | -49.47905 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9f6c3eb8-10df-38c3-a061-2eb4b9c0649e | -10.82383 | -61.41532 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 770a0310-d41c-3a26-871e-3f58495bb889 | -8.19701 | -54.73404 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| de380d0e-43d9-3b00-a12e-acd3426d6245 | -6.8927 | -52.47925 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a9b5549e-3573-3bd1-ba23-97f3860d4845 | -6.15032 | -51.57479 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71b3e382-c8ed-3f98-9511-1b1742d5aa43 | -10.20942 | -50.01132 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 592d4d98-391c-3faf-8bc0-a24a9c44abbe | -11.16581 | -48.32249 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 555e4672-67ea-3cd0-9709-ff3452726194 | -11.52943 | -47.16277 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 2809bd20-b783-39bc-ad09-e9fb27d1a3e0 | -7.58327 | -44.78987 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| efe62c25-a917-31d9-a422-9fd14106d98b | -8.67014 | -45.34623 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 911cb152-0ebe-302d-be9f-7632cff44fee | -11.57281 | -47.40349 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f91a5904-6bbd-3edb-a489-5f055b20af3e | -6.21729 | -48.12358 | 2026-09-28 17:09:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 18762724-209f-3154-a98d-226503a3e63d | -9.73975 | -53.86913 | 2026-09-28 17:09:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 235c07bd-7fca-3e9f-bd9e-9c815cc92a82 | -5.72936 | -45.0606 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3fa0a4c9-6508-33e3-ac41-57a2715c86f8 | -7.23745 | -44.86219 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c82ec49b-6305-387d-857d-587a5e65ca21 | -11.09871 | -51.16828 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 05a09537-f12e-3beb-8e71-00a5a7ff23fa | -10.81125 | -41.33033 | 2026-09-28 17:09:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 479bc96b-ad82-34c9-a2e1-88c6e54582a9 | -10.29891 | -48.16225 | 2026-09-28 17:09:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 60eb6fea-4c1a-345b-82b4-a37d28f4ee78 | -11.84577 | -50.85208 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 42e07d6e-f114-3c03-9921-4f0e91e23beb | -7.39486 | -55.6281 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0ec952f2-388d-3122-ba2f-48e27e2584fe | -10.92358 | -50.7044 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| db44b9fd-e3fa-3306-8a8b-013fb5d0455c | -5.32105 | -47.88764 | 2026-09-28 17:09:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e281f57a-57ca-33f1-ba90-a3513eb4dc2a | -9.89272 | -60.20898 | 2026-09-28 17:09:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5ba9d146-b746-35f8-ba43-c66cb85b39f1 | -9.44155 | -41.81094 | 2026-09-28 17:09:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 83d615bc-54b9-3034-a430-d7d4a16a4856 | -10.82406 | -57.18901 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 216.1 |
| 8bba04cd-665a-3fe3-ad37-d234e01043ac | -7.26096 | -43.35838 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 211df917-e3d8-3630-9850-2fdfc9ff5ad2 | -9.49108 | -66.78345 | 2026-09-28 17:09:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0d224c05-7765-361c-8781-a1885cf67128 | -8.39806 | -44.75471 | 2026-09-28 17:09:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4460261d-b040-331e-8699-5ce0fd125534 | -6.06371 | -53.40862 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d7c7f6d-bc41-3e31-ba09-929f42c2b8e9 | -12.16923 | -50.4199 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5c1f3718-2099-3dbc-9a4d-ce797038a1c3 | -9.1781 | -51.43065 | 2026-09-28 17:09:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2787e3a1-27c1-378d-bd7f-d647dd63bb86 | -6.06834 | -53.41561 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03ba894a-6f25-36f7-935e-9b5212148a30 | -9.97054 | -66.80262 | 2026-09-28 17:09:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3ada27b1-5f21-3b07-9169-8f7d012c46a7 | -9.0799 | -46.50373 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ac2c58a3-8929-3c02-9309-5cf5a03fb8e3 | -10.77896 | -48.74772 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 217ff001-5ad5-3101-a87b-747876f27c46 | -6.76567 | -45.36955 | 2026-09-28 17:09:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c8848799-6cf8-388f-aa78-38abc4279e1e | -11.20223 | -44.81148 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3deab723-598a-3275-bfa4-2330cc4d2d2c | -7.27792 | -44.31861 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cd843cb3-70da-3a8f-ae84-17d5009e38d6 | -6.18091 | -53.28183 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e798f89f-d445-3151-8fbf-a539156ea5fa | -9.77387 | -45.98046 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| fc8b1819-41e8-3eff-980f-4d5ef19655f0 | -10.94823 | -43.89334 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 3b2c51cc-7c75-3153-9f41-29a7098ba6fe | -11.03419 | -54.12739 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d7c76439-2326-3a19-9bcf-28b91d6bc205 | -8.28926 | -54.73701 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a0bb7b15-9ea7-3ef0-87c9-99afff07fdc7 | -11.53356 | -47.3674 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c5436955-4942-3593-81ff-69283dc59fcd | -10.68456 | -44.45702 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README164.md)
