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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5018ad8-96a6-3f80-badd-ae390b5d9bad | -9.78128 | -47.85034 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e02e9c8-91a9-3176-8557-00d2ac5ab40a | -9.10005 | -46.94448 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9230c2c-4453-3c54-8e1c-4db41d364139 | -9.06428 | -47.04477 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 36812e82-9bc3-3c24-897d-743c47e8e456 | -6.83653 | -47.86886 | 2025-09-12 04:04:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4a12091a-3616-3533-b087-18f64af57538 | -6.67695 | -44.13865 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 791e6391-fdd3-31ba-b0a4-27eb17187848 | -8.95326 | -46.06657 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a2de2eb-acd0-389c-869c-26cbb3b28c09 | -7.32419 | -49.64043 | 2025-09-12 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9a59ee9-9982-35e7-a0e3-e9670d9814ca | -11.93405 | -44.30872 | 2025-09-12 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46414834-80f4-371d-8067-f998dc1dc891 | -10.41006 | -50.60186 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7010d65a-bdcf-3ae6-b176-d9c88e2e2099 | -11.68659 | -46.52593 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbb9bf92-73cf-3f7c-8a2e-67b2189ea3e0 | -11.6776 | -46.54074 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9c9ca5b-b517-344a-8688-2c93025f5ad5 | -8.18085 | -46.10225 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aeab57c7-498a-3002-93e6-7ad718c55666 | -7.31846 | -44.16361 | 2025-09-12 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e94e155-498a-3497-8e2a-7a14ccd64186 | -3.69545 | -49.10381 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6845de26-9893-3756-86c8-aa21d996ed32 | -11.42217 | -43.69285 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8218fe9-0149-3dd1-9473-84035d79c843 | -11.49635 | -43.63977 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57471596-900e-342a-b313-7337a5f56f23 | -9.06646 | -47.11159 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26a3339d-4277-33d3-9a30-49f83ea48511 | -6.21927 | -39.24862 | 2025-09-12 04:04:00 | NPP-375D | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| db4e97bc-5e85-3034-b319-48d3a8bc7643 | -6.76791 | -41.59626 | 2025-09-12 04:04:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a3b34e3-fa88-3c8d-be8a-8bf69772a348 | -8.87337 | -49.5411 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb1679ec-f61f-3c32-b848-1bb2a590f9d1 | -6.83185 | -45.65466 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ebd61794-d74b-39fa-8b20-72b9ac4b5bf1 | -8.17835 | -46.09934 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f6d200c-f07d-3227-bfa0-25b83341eae0 | -10.12904 | -47.91861 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 081597df-482b-3c45-960b-27672b2ccf0a | -10.37754 | -50.50824 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e361b8fa-08f1-31d0-9b09-8d4629f38258 | -11.15524 | -45.31348 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60a00e35-8daf-35de-a9cc-7431740bfba2 | -5.9814 | -44.72501 | 2025-09-12 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9010ddd6-2a6d-3416-b466-4aed589a0a58 | -6.16129 | -47.27608 | 2025-09-12 04:04:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3eee3994-0e4e-3a9d-a9a0-4f680fcdf7e9 | -3.59656 | -51.53139 | 2025-09-12 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 637d5d8b-86ef-3264-8111-4a8e2fe4c18e | -6.45119 | -44.04015 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66de7d6f-6310-39a8-ad10-1bc2464f005d | -9.07004 | -46.95956 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2462033a-c0f7-3d7b-8dcd-7812f22a7ceb | -11.66854 | -46.61769 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 020e531b-5aa4-372f-8a68-ba0b47b9149f | -12.13161 | -44.83715 | 2025-09-12 04:04:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7364d73-2229-3f05-b85f-c1f6737215d1 | -7.32617 | -44.37368 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 522356bf-dcff-3286-8267-25acf9a9bc6f | -10.4387 | -50.60154 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ab0ba1f-3405-3e6d-b40a-cd3717fba790 | -6.18349 | -42.62497 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c7d1d0e9-a4f4-312e-b0df-614af4885fb4 | -6.68467 | -44.15155 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c0413d7c-f2b3-3b28-9551-ebfb555ff084 | -10.53503 | -51.52747 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7754aa0-ba25-364d-91e8-b0c1e70aa186 | -9.04516 | -47.07517 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 46b06640-1d9c-3b5b-b2e7-85245d41a403 | -11.68263 | -46.59522 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d83bfe7-1f4e-3254-931d-05b53f4ac5dc | -11.02559 | -44.6516 | 2025-09-12 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd82fe84-89da-3dc8-8be4-0284348d3ff5 | -9.69351 | -47.55032 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f9ad835-b2bf-3087-a2cf-bd9186d4ce2f | -11.67975 | -46.54021 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 420b65bc-2ee1-3030-a86c-026bf8525ab4 | -10.74538 | -48.18745 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8652313-2a84-3d59-ab3e-151c8536ac8f | -11.42946 | -43.54369 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 38063791-ce39-3bfa-a8ec-0fc43d3c54a1 | -10.84901 | -48.15874 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7eb1c5bf-a84a-3312-897c-960e8493850d | -7.41082 | -50.6484 | 2025-09-12 04:04:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23fbcbf5-f09b-3ae0-a292-bf752b43eba6 | -6.63178 | -49.78611 | 2025-09-12 04:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30023012-0b23-385c-acb0-ea7bc9c42ecd | -6.82765 | -45.65387 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 033f510d-3293-3174-bae9-c36f47d4264b | -10.65238 | -48.65446 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8932786e-bb25-3dc0-b7d0-fdd122f549f1 | -10.42224 | -50.59797 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09bd0c59-8c1e-347f-a063-8fa549f1db7b | -8.9439 | -46.09309 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 551c95ff-dcf3-37e9-ab61-27a50897923b | -7.40795 | -44.36495 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bd5d43a-b92c-3cfb-ba9f-3026dcfd4be9 | -8.08532 | -42.56334 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a4667676-bd81-3c3f-9c90-da92809de021 | -7.24811 | -44.47758 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfee8ac0-2fcf-3875-ba06-2b5e260b93b7 | -6.65173 | -44.13603 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 219279c5-fb2e-3f59-bc83-81843c1ca27e | -10.65631 | -48.66041 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b251664-9392-3d74-a780-e8fa183ca85f | -8.89211 | -49.94006 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c5170c45-cc22-39dc-9a11-a921c7cf1efb | -9.01239 | -46.12345 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0f4704a-a1bf-37d3-97d3-16e655b1726b | -11.67365 | -46.59766 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e906ccb-02e2-3289-9554-b32996ef1c81 | -6.89307 | -44.35168 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc624ebd-767b-3127-b420-e68af731a311 | -12.02453 | -43.78748 | 2025-09-12 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fe29649b-adc2-3e89-936a-8cee5cc07225 | -12.13609 | -44.8332 | 2025-09-12 04:04:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b94b77f4-f6ef-3fbc-b448-9155db7b6d4e | -8.89399 | -49.9367 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bfc8f8d5-3616-3403-a7cd-c34958ff4666 | -8.94433 | -46.09267 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d549d86-a18b-3fc9-b06c-46f7ee9f1ef2 | -8.94907 | -46.0659 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29e2144b-290c-300e-985a-ff8526bb4ac7 | -7.32482 | -49.63688 | 2025-09-12 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 573589d7-741d-35b6-ad7f-d4d753c550a3 | -6.62503 | -44.08335 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e47c9a1-48a0-300c-8347-845ea64008a4 | -9.06817 | -46.57987 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8bdbf88-1fc8-3902-9b47-150d3088b38c | -10.69104 | -48.65235 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0fb19da0-9ef1-3d67-9b0f-797280490995 | -7.29186 | -44.48254 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c80122b3-8ec2-3e26-856d-f3d69547f71d | -8.18511 | -46.1029 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 659054ff-5af1-392c-9afb-d26f4a3852fe | -12.13531 | -44.83776 | 2025-09-12 04:04:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8922f0db-ecd0-378d-b6f7-37a0a421cb41 | -10.12663 | -47.91623 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e66d59a2-7707-3dba-b05e-93bc7c2ad985 | -11.11969 | -45.12253 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c848770-f7fc-358f-94f4-452d75d169c6 | -6.88263 | -42.83645 | 2025-09-12 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 94a69fc4-e665-3484-b153-535fc6c553bb | -6.17992 | -42.62444 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 0b5cbf9c-fb7b-3678-a867-ca89564d382b | -9.77578 | -47.85425 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2784287-0c74-3ccf-b052-bb62b1ea4365 | -10.43609 | -50.61524 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ac5ffc5-69bf-3bf2-95af-176395cbbb10 | -8.89334 | -49.94019 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2af5b870-416b-31df-8f92-14638a3d456e | -8.87748 | -49.53789 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 561bccfe-4ea5-3819-ac0c-6f8d22936463 | -9.72186 | -48.33915 | 2025-09-12 04:04:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 268a4333-6b21-3626-af8b-d4fae11821d2 | -11.69217 | -46.5659 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9670ee1e-3e57-3856-bcf1-b0b46794a939 | -11.09139 | -48.42229 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97bcba5f-a83a-30c1-b543-ae207e04607a | -8.87986 | -49.53536 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 847a615e-3779-3e96-bd0f-165c15924434 | -4.48557 | -48.11671 | 2025-09-12 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7547cacd-fa67-3b0b-959b-a8affcc914db | -11.67433 | -46.59387 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 234dd56a-77ff-364f-83af-f8fdf43f482e | -8.21723 | -45.79279 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6895b79-c95a-39cd-bb07-c76f3a87e69b | -8.00564 | -45.51617 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 207f3d96-e262-35a9-b700-49156e7020cf | -8.02639 | -44.80519 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc887062-04f5-324d-a015-69310ce74d98 | -6.36378 | -42.54235 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e287fe64-7d3f-3993-96d2-52cac52cc34e | -8.94618 | -46.71437 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee1b1ea6-2c15-3b6a-b910-85027eba59b5 | -10.8866 | -45.5878 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0a67009-f808-3ff6-aa5f-c26fba91867c | -11.67358 | -46.57435 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 48bdddb2-297b-3b33-a81a-3ba67f5f03c7 | -6.54001 | -43.70986 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddf5a2cc-7744-3879-812f-72b6795d4975 | -11.45224 | -43.57883 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d9b9b5d-8795-33a3-825f-9854fa3fc26c | -10.83323 | -42.76264 | 2025-09-12 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f3857b1-9f2b-3e8c-9fd0-3af097040e37 | -6.25399 | -43.42672 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 226b5b90-25f5-3f46-8bf9-57fb04d8c22e | -7.31765 | -44.16834 | 2025-09-12 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50159a20-dba9-3eac-af9d-b5d698639204 | -10.79047 | -47.26624 | 2025-09-12 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c0e341b-1ede-371c-9424-ab4b5a9d388f | -9.02383 | -45.76154 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README36.md)
