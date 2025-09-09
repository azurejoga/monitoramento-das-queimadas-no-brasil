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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68a6abab-abeb-3fb7-b26f-92402d296851 | -4.2748 | -48.19589 | 2025-09-09 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf1cf893-08ac-364a-a116-927cd2d77482 | -5.58146 | -42.90719 | 2025-09-09 03:40:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a5fd21ce-e5fa-3e51-a44d-fa303d2fd34b | -3.48455 | -40.67686 | 2025-09-09 03:40:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f26c3963-ba2a-3c85-bc9c-183b64c540f9 | -5.5353 | -42.66102 | 2025-09-09 03:40:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 98167072-7903-37e6-a217-95704bcee9f8 | -4.55813 | -40.33882 | 2025-09-09 03:40:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fe8ca0ed-3cbc-39c3-88fa-0a3f351f0e02 | -5.26476 | -44.45472 | 2025-09-09 03:40:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 63452ff1-554b-3209-bef0-cbb809b17f31 | -5.35736 | -42.63406 | 2025-09-09 03:40:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7c34f469-d8d6-3530-82b5-2d2d2f88acc0 | -4.6135 | -46.59776 | 2025-09-09 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 729df411-de6a-39fa-96c1-56e5ac1a6f60 | -4.27308 | -48.19716 | 2025-09-09 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d7d6bcf5-d3ff-3144-a872-cf7a0d041ffa | -5.49587 | -42.6597 | 2025-09-09 03:40:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1713e8c-3f72-3e19-9779-d94b38fcc2d4 | -5.42439 | -42.81307 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f0f6929b-885a-3d1b-ba5a-c2c05ec78bcb | -5.58237 | -42.90189 | 2025-09-09 03:40:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cf9c0bae-988e-3932-a04e-9c31a8093d0d | -4.89276 | -42.21353 | 2025-09-09 03:40:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2e711470-1d79-39df-b8e0-ba6d6f4ab0f3 | -5.42603 | -42.81658 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1142754b-8b0f-3a3e-a8ea-83d9beadacd1 | -5.16183 | -42.95416 | 2025-09-09 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fc13ba67-a909-38fd-bc95-3491f9882a2a | -3.48523 | -40.6727 | 2025-09-09 03:40:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 28d97259-03bb-3e33-92f9-e388374615ab | -5.76894 | -40.95167 | 2025-09-09 03:40:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 62fb77ad-002c-3d4d-baa6-26388f412203 | -3.96645 | -43.24207 | 2025-09-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab5cae1a-a9af-3b3e-b17d-82463c2dbe91 | -5.44766 | -42.79467 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c003c6ec-d79a-3932-a146-6aabc4a09f93 | -4.60061 | -43.31882 | 2025-09-09 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54630815-8413-3b1f-bbfd-5f088d9ca772 | -5.2637 | -44.45683 | 2025-09-09 03:40:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e8364757-6ce1-3f7d-aa0e-971d62a8ec4b | -5.49106 | -42.65885 | 2025-09-09 03:40:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 715457a0-f58a-389b-8dd4-786afcd36575 | -2.62307 | -46.83977 | 2025-09-09 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4a7522a4-014d-3285-b01a-c515f3033083 | -5.49895 | -42.99628 | 2025-09-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d785f7c-126f-3265-b4b7-d8c79e59c5e0 | -5.49404 | -42.99532 | 2025-09-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55409492-4acb-32e0-bae5-cf0cacfcb908 | -5.41564 | -42.84877 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0e0179c2-03b5-3c99-a4ad-8b1481e15b9b | -5.44425 | -42.79744 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 414bee5b-48b7-3fce-b854-956a6b99ca33 | -5.53619 | -42.65572 | 2025-09-09 03:40:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f0d6e93c-1715-3854-a837-c0d2823bec79 | -4.60008 | -43.32185 | 2025-09-09 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| defda6a4-d7f5-3e7f-9928-461292062a2e | -4.27426 | -48.19063 | 2025-09-09 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 846b0a09-4a1d-3b1c-963c-fb99beb30256 | -2.62961 | -46.84129 | 2025-09-09 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 70db1767-aeff-379e-9665-95b0017e5853 | -3.9613 | -43.24128 | 2025-09-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2293fb7-8584-3c6a-a3d9-dc9e850233da | -10.96396 | -45.09998 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 987d0dbc-044e-3c37-bcd2-3e090ffac844 | -8.37591 | -45.02377 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1efd8cbb-aba8-369c-b233-95a4d40a06b4 | -8.37606 | -45.01033 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24d07aa9-9b27-35e5-a222-e0944dc81528 | -6.55316 | -43.91264 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33ca6147-7db8-3f20-bcdd-1ef66894c229 | -9.70673 | -46.8204 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| ac829646-040c-3c66-be61-bfbf383372b7 | -5.67916 | -43.91022 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b6a7d57-d90a-34cd-8fe1-962b0f559ac6 | -6.5537 | -43.90965 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd611704-e7ab-33bf-a758-79141497f5ab | -6.86704 | -47.91353 | 2025-09-09 03:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c8b3b7b0-4369-3369-b69d-a591e3793004 | -10.77077 | -47.73205 | 2025-09-09 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed175b56-4150-35b8-9c5a-565f2bf3238b | -11.36817 | -45.59269 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a8f189b1-983f-34f1-94c8-d8b3843b77b5 | -9.7244 | -46.79192 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 268f553b-7e5d-388a-a83d-26f023424ed8 | -10.9706 | -45.11565 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d0b794f9-6e7d-3cf2-a2b0-93c7ff29c276 | -11.15348 | -45.26948 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ba3c7b0-9baf-3129-a3e8-8eb8cb118eec | -11.37335 | -43.5332 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea6d05d2-b6ac-39ba-8840-ff50e83cbe10 | -9.14232 | -45.57386 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba6ab428-a43f-3a02-a5ad-710766d39b8b | -8.21917 | -44.76378 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d658bb5-8a7a-38dc-8ce0-f80bc5eb432d | -5.66721 | -45.3181 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e1a9603-317a-3577-8b8b-8156c20e17e9 | -7.2827 | -44.56916 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfaaa98d-3890-38d8-a908-1d0ae5c24948 | -6.37539 | -42.57717 | 2025-09-09 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b8398b12-16f4-31e6-ad59-81128e943e70 | -5.99327 | -46.20712 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9a4d061-0eed-3ee8-ace8-146a24863c9d | -6.18882 | -45.81118 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b470ae98-1597-3b0f-b23f-dcba67fc28ad | -6.30403 | -43.81884 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c811242-db9a-34fa-8a81-df150306c308 | -9.71932 | -46.78659 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f420c70-c259-3daf-8657-abd77b95d2db | -5.54756 | -45.17773 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e755f444-f198-3a6a-b105-74deaf7d3735 | -8.05114 | -48.64906 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 97503ecd-dfed-3ca4-92e2-513c24c1c7e1 | -8.22011 | -44.7676 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 402bb71f-a2ed-34a8-9707-ebe107e5f9fb | -9.8192 | -46.03014 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f822bea-10ae-3b27-be17-2602f71efaec | -10.33318 | -47.73244 | 2025-09-09 03:42:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9d083ac-c024-3d03-a9b8-526f1850ff99 | -7.10236 | -43.89135 | 2025-09-09 03:42:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86c4fbff-2464-3456-986d-6ca985cab6cd | -10.97187 | -45.1146 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 651184b6-6c15-3c82-83fb-8d8cd897ad4b | -6.8255 | -43.62582 | 2025-09-09 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37a00e3b-d41d-3a23-aecb-81899cf38454 | -5.94748 | -44.1685 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b401072-23cc-3a0e-8da2-b333d52777ad | -8.06086 | -48.6351 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cff5ae0a-3edc-3460-881b-e51f1abd9cac | -6.10333 | -44.13636 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cb17538-b64c-36f0-9e0f-c3c89682bb30 | -5.71692 | -45.40828 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a44ba079-8a9c-3157-9785-c93ddb61c9e8 | -10.95877 | -45.09914 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b317957f-a3c7-36a0-ad3c-0d7f1232a642 | -5.6802 | -43.90261 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd9a6642-5079-39d6-ba17-d95ee8694770 | -7.07097 | -45.20685 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8fa0b22-155c-342c-8a11-a38a4a81e194 | -6.25685 | -43.49763 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81e39a85-9396-3051-9967-8d02de3fde96 | -5.54825 | -45.17373 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5520a18d-e848-3a12-b74f-3d14d6dc940e | -7.7214 | -44.7435 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1710b8e-2908-3888-8c3d-03c2938ec325 | -5.8214 | -44.11596 | 2025-09-09 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3bf4b14-3f89-35b9-b738-61ad77eb6da0 | -8.03872 | -40.9551 | 2025-09-09 03:42:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e82c8c6-3dc3-30fb-981d-0de6700a4c08 | -8.03712 | -48.63876 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdc4f2a3-26e4-3b15-be24-cd295a9d41a9 | -5.58033 | -45.03776 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 993d5372-68d1-3eb7-880e-2f5f51e17c61 | -9.84645 | -47.79729 | 2025-09-09 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ec2d2ad-93e1-3a35-afc9-1db85f2dbe77 | -6.23185 | -43.5221 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c169b7d2-f085-3c46-9771-4170fb699200 | -9.35305 | -46.51037 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4ba8857-9253-3dcc-b0bc-2fee5d795d93 | -9.49661 | -48.28103 | 2025-09-09 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d72fe457-2f0f-3e66-8871-ec2aec2505c8 | -7.07162 | -45.20318 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12e43b40-57e0-3904-a5e4-dbc4dc7bba82 | -8.34019 | -45.05507 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73ca7368-559a-3d29-a3c3-cbe732394348 | -5.54307 | -45.17973 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b7079f9-4bd3-3add-ba68-a438044ff326 | -6.4064 | -44.439 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00e9dd44-65fc-3fb6-9fb2-09484710df8a | -10.15432 | -46.20316 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd54e408-f206-3cb4-afcf-2cc54a3c3379 | -5.81412 | -43.97045 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec4f5f49-82d5-3a6a-95de-f4caee8c1930 | -6.21316 | -43.36281 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b30ed33-3aa3-32b8-b3e2-ea6c9c4b0b00 | -5.83738 | -44.21392 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 391fdde1-412c-32ee-bee7-05d7ee1d6412 | -11.14757 | -45.27215 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efe56002-e4b6-3c7d-820e-96fa10f84239 | -8.03106 | -44.0308 | 2025-09-09 03:42:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f3af6dc-6926-3f77-9644-ff371b7304a6 | -9.1528 | -45.58047 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eb82355-1044-306e-9948-cd5ff7a65040 | -11.39836 | -43.55302 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c42f2fd3-47d7-372e-aebc-c7edf87ee176 | -6.34434 | -43.78286 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 668d7405-a502-3f83-abcc-6067ca07e5eb | -6.43523 | -44.05854 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c0dd568-8e23-31bc-8a72-632babe30b3a | -8.04887 | -48.66072 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da54850b-0c2b-346b-8520-09d1280281b2 | -7.90933 | -46.8511 | 2025-09-09 03:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b85dd3d1-2a10-3437-97c4-1a4abb4b713c | -10.81097 | -48.29185 | 2025-09-09 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0a31b65-eed4-3d1f-aaba-70bcdd3c46ae | -9.13504 | -45.58428 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3798ea6b-aaeb-3345-8147-a245a554ed05 | -5.80822 | -44.84727 | 2025-09-09 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README9.md)
