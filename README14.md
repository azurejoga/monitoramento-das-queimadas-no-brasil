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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 000053fe-ea2a-3a06-9c77-c21269e28fb0 | -7.2402 | -60.1904 | 2025-07-21 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| aa8f1c60-3da6-3bba-b953-6bbf20382ac4 | -22.67759 | -50.46683 | 2025-07-21 06:20:00 | AQUA_M-M | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 14438834-0a25-3b9d-84b7-a85e8620fb23 | -7.2402 | -60.1904 | 2025-07-21 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 82225481-8d2c-3e4e-ac64-4ab5d46bcff1 | -7.2772 | -60.1698 | 2025-07-21 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ec41ec5a-1838-346f-83c1-c2f09578d4df | -7.2772 | -60.1698 | 2025-07-21 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 971197e3-9261-3c79-b6fc-d3efc45777df | -7.2402 | -60.1904 | 2025-07-21 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 49a7063c-6dcb-34a6-838b-420514e8c4d2 | -7.2772 | -60.1698 | 2025-07-21 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 73a479a0-1f50-38c0-bd49-15d2942852a1 | -7.2772 | -60.1698 | 2025-07-21 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| abd2ccfa-f6a1-30fa-94b1-0548a3795bc7 | -7.2402 | -60.1904 | 2025-07-21 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d834315b-d531-3934-8c87-36b406e0f59c | -7.5622 | -44.5678 | 2025-07-21 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 4fd15b36-fe88-30ac-bee3-b36fd6aa7ad8 | -6.896 | -45.38 | 2025-07-21 11:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e6e3ee53-5d58-3f30-b8f0-bdb3bcbb12a4 | -7.5622 | -44.5678 | 2025-07-21 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 14f25d6e-1fe4-3e45-a0a8-a17429c5525b | -6.896 | -45.38 | 2025-07-21 12:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| b542ce5f-4ee6-3497-b141-406ef7641d2b | -7.5624 | -44.5449 | 2025-07-21 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 3d44b2e3-812e-3e77-8a43-96225bca8638 | -3.8161 | -43.0205 | 2025-07-21 12:08:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| c8cd706c-ee34-349e-906f-f3cba9246051 | -3.28728 | -42.53318 | 2025-07-21 12:08:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 198cba6f-8c81-3f1d-82a6-ac0c093fddcd | -4.19616 | -38.37604 | 2025-07-21 12:08:00 | TERRA_M-T | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 4622f489-d3ef-3f89-b47d-035723d3f78a | -3.29612 | -42.5344 | 2025-07-21 12:08:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fbc32525-f012-3819-97c3-b7652f781907 | -4.19827 | -38.36082 | 2025-07-21 12:08:00 | TERRA_M-T | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| ad8b2865-7141-3525-ac22-3bee1c539ee7 | -6.9801 | -42.809 | 2025-07-21 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| b9f41084-cb3f-3af6-b3c6-ffc626c363a9 | -7.5622 | -44.5678 | 2025-07-21 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 1fa497d1-9eb4-3ff9-b785-b64621c7ca4d | -6.85924 | -43.09967 | 2025-07-21 12:10:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d0cd2920-6226-3102-954e-996261dd98d9 | -7.86664 | -44.70145 | 2025-07-21 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b8dfc504-5be9-3ec8-bee9-42a62fb94a73 | -7.96288 | -43.97493 | 2025-07-21 12:10:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 8ea5b6c6-bc5f-30e7-9fd5-b2b585716215 | -7.3642 | -44.34792 | 2025-07-21 12:10:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73f4f962-ac2c-3a31-aae2-7e00ae19d8bc | -6.97601 | -42.80006 | 2025-07-21 12:10:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 875242ab-e233-31ae-9be1-3a6decccfaf2 | -7.2736 | -44.27455 | 2025-07-21 12:10:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b822737e-f24b-35f1-aef3-1abbcf0dbcb2 | -7.96414 | -43.96611 | 2025-07-21 12:10:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 28bd66e8-4fb1-3915-aa38-c4f06de1c0d5 | -4.67004 | -41.95474 | 2025-07-21 12:10:00 | TERRA_M-T | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| fae741d4-f164-315d-92eb-cd8735f26629 | -6.89973 | -45.37349 | 2025-07-21 12:10:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bb894d3d-c53b-3f5b-8a57-02f41c9fa6f5 | -6.89836 | -45.38282 | 2025-07-21 12:10:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c3e7961f-d687-3b26-89d7-10278d6847f3 | -6.6877 | -43.00863 | 2025-07-21 12:10:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9114fed-719c-33df-9e0c-4b540188e7c0 | -7.7563 | -42.16278 | 2025-07-21 12:10:00 | TERRA_M-T | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| db20cc92-60b0-34e6-94a7-a4d68d87ced0 | -7.56167 | -44.56939 | 2025-07-21 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 155.5 |
| cf49553d-d59b-3483-b723-fcac3870c9e5 | -5.37327 | -43.93196 | 2025-07-21 12:10:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6d1429cb-8d2c-3a46-a1e2-ac97f86f3c3d | -6.75889 | -44.12826 | 2025-07-21 12:10:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7ca26b4a-fb8f-3713-8246-b45150dc02c2 | -6.72944 | -44.33128 | 2025-07-21 12:10:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 781ed61c-2d13-3356-b767-aad1e93e9c2c | -6.33355 | -44.06409 | 2025-07-21 12:10:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 22260114-4f07-3191-9358-383f604eed50 | -6.89528 | -42.78291 | 2025-07-21 12:10:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f66ab4d2-103e-32fa-87a8-c3888591a6de | -7.29603 | -44.36794 | 2025-07-21 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 01fec038-780f-388e-9fa3-0dd71c924cfc | -6.50432 | -43.51983 | 2025-07-21 12:10:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9a7bc7f4-a91e-306d-94e3-83a5cba83e93 | -7.86794 | -44.69255 | 2025-07-21 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5ff85584-fc17-3785-8347-cfa67eb456fc | -8.27574 | -36.90084 | 2025-07-21 12:10:00 | TERRA_M-T | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 5a2b1209-ac80-34da-9457-dc05d951630f | -6.64065 | -43.21152 | 2025-07-21 12:10:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 941a62bc-4a5c-32db-9def-65a403dc61ae | -5.7304 | -43.95328 | 2025-07-21 12:10:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 594148d7-f629-3fda-9ac4-ecd2674a3e12 | -7.27488 | -44.26572 | 2025-07-21 12:10:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 82b9f473-0bf3-33d5-8bf0-bce2cda44278 | -6.73827 | -44.33253 | 2025-07-21 12:10:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2aa6c296-372e-3c49-8660-efc06852ebbb | -7.55283 | -44.56813 | 2025-07-21 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 375e9633-4ca9-351e-a59b-02ad3b023a6c | -7.56295 | -44.5605 | 2025-07-21 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 810eddf6-fe89-384b-9b7a-1351c88c67cb | -6.20291 | -44.39138 | 2025-07-21 12:10:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d370ad8f-44a3-3446-93fe-9409aa8f071e | -7.35539 | -44.34666 | 2025-07-21 12:10:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 26b4415d-c4a0-3c99-907a-59482f82787e | -6.32474 | -44.06286 | 2025-07-21 12:10:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9aedf3cc-883d-31fb-afd6-432a65f4a8be | -7.13151 | -43.33543 | 2025-07-21 12:10:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| bda14bc4-27e0-3143-9aeb-82d44691d88c | -6.37379 | -44.74521 | 2025-07-21 12:10:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| e8b4be5f-2211-3f43-a1ae-4fd133130558 | -6.8893 | -45.38154 | 2025-07-21 12:10:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 1f49cbd7-a881-3ebc-87b3-bfbb055e9d29 | -7.25942 | -44.29349 | 2025-07-21 12:10:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 694b0742-828d-345b-a0a1-976289ac0d33 | -6.73073 | -44.32244 | 2025-07-21 12:10:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e953e277-4170-353b-b3fb-b90f85e3cdf7 | -6.73955 | -44.32368 | 2025-07-21 12:10:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 112a6b64-728d-3335-9d8d-510c019a0913 | -5.37454 | -43.92316 | 2025-07-21 12:10:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 04f7de20-9a12-31a7-b710-5bf631134e0c | -5.56621 | -45.21026 | 2025-07-21 12:10:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ab85f138-38c1-3909-ac3d-6ae6da5bebac | -6.88792 | -45.39095 | 2025-07-21 12:10:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f4c60a94-480f-3c8f-941e-3d0e034ac91b | -4.59484 | -43.31929 | 2025-07-21 12:10:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 08bddf5f-e98a-3b8b-a566-ee1864891351 | -5.63489 | -43.1471 | 2025-07-21 12:10:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 5bcb9e32-c89e-3c6b-b6a5-d6323d42fb30 | -6.97471 | -42.80918 | 2025-07-21 12:10:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 59d86726-030c-3120-87d4-0b0a1e76b44c | -6.80159 | -42.98459 | 2025-07-21 12:10:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 3253fbd2-1a91-35fa-9706-9dcdc3661703 | -7.35668 | -44.33781 | 2025-07-21 12:10:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4dd17593-1622-3fe2-8e1e-ac3a76baf64c | -6.14569 | -43.96223 | 2025-07-21 12:10:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8f64f85b-d4bc-3d8f-858d-cca1fe87850b | -14.85139 | -46.85732 | 2025-07-21 12:12:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 747416ad-f144-3966-940f-34e3fb7eaab0 | -11.78074 | -46.45573 | 2025-07-21 12:12:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a1bc7cce-6b8f-3220-85cc-bdc0583439c5 | -8.27532 | -46.06367 | 2025-07-21 12:12:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c0e04fa4-4c0d-3d03-9539-b5875d5bf650 | -11.94399 | -46.3517 | 2025-07-21 12:12:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 0c5a9e81-aebe-387f-9069-5c966b49ffe8 | -14.60996 | -48.87467 | 2025-07-21 12:12:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| dd72d7cf-9b1a-38c3-8d86-2ecc2dc85603 | -14.21606 | -45.46758 | 2025-07-21 12:12:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b01ce02b-40c6-3139-82b6-7f33e534f2e6 | -11.12966 | -50.36673 | 2025-07-21 12:12:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 64292de9-9ec9-37c7-935d-3342b27b977e | -12.36546 | -46.43642 | 2025-07-21 12:12:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1c75eef3-782e-3985-b1c2-fc5de90f3dc3 | -8.99474 | -41.00976 | 2025-07-21 12:12:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 20.2 |
| c775b475-3ae5-393a-95bc-c51437af9e8e | -11.15196 | -45.77807 | 2025-07-21 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c1695593-7e9d-3b21-9d65-b1fbf9c47838 | -8.83264 | -44.53033 | 2025-07-21 12:12:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 650731c3-5362-3228-b270-d481cec8acc8 | -14.61104 | -48.86924 | 2025-07-21 12:12:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 2ed5a37c-89e0-3d57-9d36-0640968640ce | -13.89439 | -44.01791 | 2025-07-21 12:12:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 3b1d37ca-8f34-3b8e-8b50-167e8a26e389 | -11.77932 | -46.46521 | 2025-07-21 12:12:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dea26ea7-09cf-396a-90c3-76e9c58d7457 | -9.87817 | -44.69433 | 2025-07-21 12:12:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 19bdb55e-37e5-3130-9cb7-4d517841c8c4 | -11.57456 | -44.83941 | 2025-07-21 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 278632aa-f5b1-3464-8000-9a1b0eb01286 | -13.89308 | -44.02738 | 2025-07-21 12:12:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c117553b-cdaf-35b3-8d67-d011755b7003 | -10.14056 | -49.64742 | 2025-07-21 12:12:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1f902b16-dc6c-37ff-ac9e-4d151fdb6e7d | -12.37453 | -46.43742 | 2025-07-21 12:12:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 14d081f1-2066-3782-ad3c-0cb33bb70267 | -11.56447 | -44.84706 | 2025-07-21 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 147ad084-0de5-34c7-aade-210904f4b50b | -10.90482 | -43.51691 | 2025-07-21 12:12:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4715cde4-c469-39e8-aad4-a8168a791f00 | -11.79768 | -43.78916 | 2025-07-21 12:12:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0fd3ccb5-05b5-35ba-9379-0188d96fad83 | -9.87945 | -44.68545 | 2025-07-21 12:12:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 23bc8de3-70ab-38b8-a9b5-c08c88ec5311 | -11.56576 | -44.83814 | 2025-07-21 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 543e5450-6df3-3629-9494-d5f934bf817a | -12.47684 | -45.86637 | 2025-07-21 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3342412-9e2b-30e7-b486-03305e3790bc | -10.14037 | -49.65739 | 2025-07-21 12:12:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 68cd8c57-a6f8-3339-83e6-1b9debbe5c77 | -14.68882 | -52.68604 | 2025-07-21 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3fcdac35-b5d8-31e7-bb11-484a920aa5d5 | -8.26611 | -46.06236 | 2025-07-21 12:12:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f62e4e73-211e-3f9a-8498-4bb5fe90d532 | -10.64688 | -44.48262 | 2025-07-21 12:12:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 657d3500-695c-3923-83fc-4e1be88b4b1f | -14.72771 | -48.26245 | 2025-07-21 12:12:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96f0ae9c-de23-322b-82d1-4b8760874918 | -10.15178 | -49.65925 | 2025-07-21 12:12:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 165fd1fd-6d41-3cf2-868a-c0cd0b9e84d1 | -14.86038 | -46.8587 | 2025-07-21 12:12:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 93d7b663-7def-3837-b3c9-7c8b64735789 | -9.98846 | -47.70689 | 2025-07-21 12:12:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README15.md)
