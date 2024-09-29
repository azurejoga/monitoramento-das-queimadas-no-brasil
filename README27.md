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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3add3f24-0a5c-3412-b32a-ff11a2d899bc | -3.56524 | -50.58475 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 328ac3d9-6666-3c81-8bc7-c9fd183eeb23 | -3.56404 | -50.36999 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9c612616-3d71-3de8-812a-5f770146bc15 | -3.56329 | -50.37439 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fd661ce4-3a35-34e0-9e9c-7ab2325278a0 | -3.56254 | -50.37882 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 06e565dd-6ab6-3b40-9baa-9ca142ce4328 | -6.6091 | -51.03239 | 2024-09-29 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc8d4e07-9809-3fbc-8082-01bcf3ad2e12 | -6.60827 | -51.03684 | 2024-09-29 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d99cbff2-e5ec-31c1-a13a-6e12e758d670 | -6.60635 | -51.0358 | 2024-09-29 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 53a4f7ed-a439-34eb-8df9-b29c3ae9aea3 | -10.54337 | -51.09463 | 2024-09-29 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3918f8fa-5eb5-35b8-a3f1-5e1c858ab49c | -10.5378 | -51.09319 | 2024-09-29 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 655e8e0e-7490-3f0c-80cd-b790e267f33a | -10.52535 | -51.0971 | 2024-09-29 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 966fcc6e-7ad3-3c08-8771-51323ac39e1e | -10.52469 | -51.10056 | 2024-09-29 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adc2dcba-ad04-32ad-8bda-fddfc6a5fcf5 | -3.63668 | -50.79719 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d240c6a-b920-3c73-a160-5e34d96f80db | -3.51026 | -51.19599 | 2024-09-29 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 63122c5e-d986-3a76-869f-a34937d9bc3e | -3.50938 | -51.20109 | 2024-09-29 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 00ee1527-db83-3349-9c31-b83e152dabf4 | -3.82293 | -50.77508 | 2024-09-29 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac24bac7-37b0-3005-809f-bcc34aab9ef7 | -6.14412 | -51.25295 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ece46e38-6395-335f-a872-cae3e23c098b | -6.14406 | -51.25493 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 967cf957-e3cc-3c53-a893-38da1c999964 | -6.13709 | -51.25676 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82ca89ee-4777-3e13-9e24-9920d65054f6 | -3.89414 | -52.31083 | 2024-09-29 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 74e7aa99-c0a6-36bb-b264-9f4da5320d72 | -3.89217 | -52.30973 | 2024-09-29 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5cb040b-9b1e-3341-a65d-485db8abedc4 | -8.16554 | -40.96611 | 2024-09-29 04:02:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b308906b-502e-3dc7-8a4e-87c2f4804c34 | -9.03707 | -35.23918 | 2024-09-29 04:02:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4d91e96c-0161-3d44-b55b-2106e706e2bc | -9.03655 | -35.2428 | 2024-09-29 04:02:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 84827929-e0b4-301f-aeed-276f7fe29892 | -7.83565 | -38.16182 | 2024-09-29 04:02:00 | NOAA-21 | SANTA CRUZ DA BAIXA VERDE | PERNAMBUCO | Brasil | 2612471 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2991d25d-71b9-34aa-acc3-00d895695166 | -7.56371 | -38.33643 | 2024-09-29 04:02:00 | NOAA-21 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2bace516-5614-33d6-96ff-c4cf6beeea83 | -6.93141 | -38.1353 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9f7dfb83-f212-3fe9-bcd0-6147da71b638 | -7.44816 | -39.90319 | 2024-09-29 04:02:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 122dd6e8-ac8e-3bfe-b5cd-681f100f1a0b | -8.38624 | -40.88388 | 2024-09-29 04:02:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 855951fd-e4ac-37b9-b629-5f2a6fe9d954 | -9.3235 | -40.50769 | 2024-09-29 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 917deb07-45d7-3218-a494-964fad3f00ab | -9.26724 | -40.82251 | 2024-09-29 04:02:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b4228967-c961-3d20-83d2-c026ef17cda8 | -9.03809 | -40.56844 | 2024-09-29 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d526637d-f574-3cd6-9c6b-d59f9ce989f2 | -9.03479 | -40.56791 | 2024-09-29 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 94cc06ae-c868-368b-8f55-990de053c60b | -8.95947 | -40.57374 | 2024-09-29 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b6bf13a4-b7e4-3cd6-b9ac-f6431e7a2d6c | -8.95892 | -40.57721 | 2024-09-29 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 20e2b778-8ba0-30be-a582-2fb1fd40d9ee | -8.79673 | -40.8502 | 2024-09-29 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4ac699f0-0392-3668-93bc-0b9089963bdb | -8.41894 | -40.46249 | 2024-09-29 04:02:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5cb534bc-826a-3d70-9b16-5bcbec6b1622 | -9.56252 | -40.37185 | 2024-09-29 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4deb1d3a-3988-3b0c-a53b-0c65b51d113d | -7.91283 | -40.9504 | 2024-09-29 04:02:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f2c424b-617e-33eb-b3fd-1ef3e1c5fd34 | -6.74312 | -40.94201 | 2024-09-29 04:02:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4c9840bd-96b6-38a3-805c-0c47e1b7c994 | -6.45188 | -41.74957 | 2024-09-29 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9ff34004-b21b-340f-9e4c-ae10f685079a | -8.43333 | -41.93107 | 2024-09-29 04:02:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1f0099ab-7c14-39e7-be31-fc9044beda63 | -8.43056 | -41.9268 | 2024-09-29 04:02:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc300a64-5faf-333a-9861-f4cead3e9b46 | -8.09413 | -41.02993 | 2024-09-29 04:02:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cdeb33e4-83dd-3a55-a845-7a9f0a5ed7b1 | -8.68666 | -41.05035 | 2024-09-29 04:02:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2931ac4f-a350-3e25-bdd9-879ec32b6770 | -8.53663 | -40.96492 | 2024-09-29 04:02:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c5c7d64-9196-392d-82d4-0db5d2fec27e | -8.43728 | -41.92805 | 2024-09-29 04:02:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7be60baf-4796-3b81-a33f-a180e44d806f | -8.43669 | -41.93169 | 2024-09-29 04:02:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 91cfea0e-a89a-3d69-ad03-c8a23016303f | -8.3466 | -42.27238 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fca00443-0006-36bd-9284-a6abaf87f321 | -8.43451 | -41.92378 | 2024-09-29 04:02:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc55f225-8008-3e4b-8b2d-458e8166b8ca | -8.43392 | -41.92743 | 2024-09-29 04:02:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fe3cbb74-7fe4-3b02-8b47-f9917d5b315c | -8.42998 | -41.93043 | 2024-09-29 04:02:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eb0e3c97-87bd-3a01-9ed7-3b7d3adedf77 | -8.34318 | -42.27183 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c9ce7894-750e-315f-8acf-36bc25c0acde | -8.27731 | -41.46071 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7889ac8b-f35f-3e85-8be7-3375fc9b6881 | -8.43274 | -41.93472 | 2024-09-29 04:02:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 63e464ee-4e99-3aad-bd1d-efd07e7adbbb | -9.73266 | -41.96024 | 2024-09-29 04:02:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53a03018-9719-3278-891b-4c22445e745b | -9.72931 | -41.95969 | 2024-09-29 04:02:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 68b19b5a-1493-398a-8eff-718d66d14fe9 | -9.66068 | -42.5987 | 2024-09-29 04:02:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e33d4c2-a039-3a3f-9634-90546d3f9ee1 | -11.36185 | -42.92344 | 2024-09-29 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5fc38e8d-6d3a-3366-af64-46b5e059102a | -9.26667 | -43.49895 | 2024-09-29 04:02:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d2157c05-103e-386e-bdc7-95ea099d8de7 | -4.94457 | -41.85914 | 2024-09-29 04:02:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e950ac78-695e-36fa-b3aa-7842756df12e | -4.84946 | -42.78816 | 2024-09-29 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b9c7d46-3984-3ee0-a72c-f412c9a981a4 | -4.84786 | -42.77502 | 2024-09-29 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1c0a0f6b-f000-3d05-addb-6513e0c4397d | -4.84518 | -42.79177 | 2024-09-29 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa1c941b-8281-303f-a32f-a3c52fb5a4fd | -4.84425 | -42.77442 | 2024-09-29 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 145228ce-1cef-3374-8871-4ee5c70f9661 | -4.84358 | -42.77858 | 2024-09-29 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4bef9376-f63c-3346-875a-45ddd8c463eb | -4.84064 | -42.77382 | 2024-09-29 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe7cdbe3-6a8b-3778-a05f-eface8362f67 | -4.80836 | -43.0213 | 2024-09-29 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 004d92fe-d3f7-363c-a7e1-7693717b2887 | -4.74612 | -42.89735 | 2024-09-29 04:02:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1fb7be5-bfe0-3df8-9b0d-42dab5b2e312 | -4.74544 | -42.89857 | 2024-09-29 04:02:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81e36dff-4921-3745-9816-bfb3520db8e2 | -4.74248 | -42.89676 | 2024-09-29 04:02:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f30fe041-f21f-3aa7-8bf8-9f5b1ddd3eb3 | -5.06611 | -42.74833 | 2024-09-29 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b319095-34bb-330e-a106-009b98fc926b | -5.8975 | -42.78827 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e26d7100-dab1-3222-99c6-cbb884ec54e2 | -5.89393 | -42.78773 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b0f09010-40a1-3b83-a0fe-da922cfee721 | -5.80264 | -42.50198 | 2024-09-29 04:02:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b3a405fa-55ce-37d6-a955-31f199842aa2 | -5.73418 | -42.6099 | 2024-09-29 04:02:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 580a107f-b31f-3cb6-8bd0-4afd8bbc17bf | -5.48247 | -41.81447 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 54cc71af-e2d2-30e8-aa2a-7bc3dece00bd | -5.45435 | -42.58825 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f6026b0d-4ef2-39e2-b916-ea5eff1ae81d | -5.44876 | -42.60413 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 32faa6b8-3887-3f22-941a-f1ff002e5d90 | -5.44814 | -42.60384 | 2024-09-29 04:02:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 50e7a842-6026-302f-a263-34d9d7cb2221 | -5.34402 | -42.77638 | 2024-09-29 04:02:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9b358673-3bfa-3d1e-93a2-7b1a67d0db68 | -7.90618 | -42.66982 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| acc8312a-bdbe-33f5-9e02-9929606a5b27 | -7.88879 | -42.66702 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 59688ac5-5723-3444-a112-61182c6ff3b5 | -7.88816 | -42.67086 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 735c5958-89f2-3940-8a74-1229b043aba4 | -7.88217 | -42.68573 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 88fa1bbc-054e-3182-bf52-b00b13d54cdd | -7.8752 | -42.6846 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9cb58c94-380b-3128-a3c9-df557df6ab02 | -7.87869 | -42.68514 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6ad9cbc9-f033-3f42-baac-d8b5cb0e54d1 | -7.88627 | -42.68245 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5cdef758-00cd-3218-b005-4b31ec0e213b | -7.87172 | -42.68407 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7bac417f-f8b0-36f8-95d6-2639f8d217b2 | -7.76141 | -43.76291 | 2024-09-29 04:02:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 433c7452-a135-3075-b98d-fc4dad231ee3 | -7.88753 | -42.67472 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c45ecc51-eaa9-380f-b90c-a388c5776b7c | -7.88342 | -42.67801 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4c1e4325-aaf7-30c4-8e7f-d711efd55f27 | -7.58237 | -42.28106 | 2024-09-29 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f8efbbd4-f611-3a03-9592-ff7360e9729b | -7.57956 | -42.27671 | 2024-09-29 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9a28e18c-b3ae-38d8-81cd-851cd09cd883 | -7.21642 | -42.49706 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 825386d8-1661-3987-b8ba-c5283b3f8c4a | -7.21231 | -42.50039 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4e6340b7-af0d-3fcf-a24f-14ef64a27d65 | -6.51116 | -42.78728 | 2024-09-29 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c3bef39a-cbcd-3b2a-830d-9ce14ea477d6 | -8.72203 | -44.01668 | 2024-09-29 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6417bd00-1d0e-3b4b-ba43-f7caaebe2a86 | -8.72128 | -44.02112 | 2024-09-29 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e16b98d6-1e50-349b-8161-6d2e3c17c291 | -8.7176 | -44.02051 | 2024-09-29 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae45594b-76a3-355d-b483-67d618a31edb | -8.5016 | -43.92209 | 2024-09-29 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README28.md)
