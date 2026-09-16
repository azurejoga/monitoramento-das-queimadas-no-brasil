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
| 8cdeeb29-bc83-3adc-b05e-923f273cb8d0 | -5.63056 | -40.85244 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b7937b8-606d-3328-a10c-f817f4119ea5 | -5.99127 | -46.63559 | 2026-09-16 03:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b06a21b8-0db9-32c3-b880-0089f769a39f | -7.08338 | -43.56523 | 2026-09-16 03:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c102f570-8774-350b-9335-35433467b128 | -5.87932 | -35.34974 | 2026-09-16 03:53:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 11affa0f-3261-3739-9b45-97ee712fbf41 | -6.77989 | -42.97493 | 2026-09-16 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 516676a2-e9e9-3810-abe4-df76f0c15162 | -6.83594 | -43.51314 | 2026-09-16 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4950cb2c-672b-3716-a833-246fd24aaa15 | -7.34096 | -44.48632 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4a718a6-fc28-386f-8a5f-5a937542d382 | -5.63661 | -40.86003 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c052497-72c8-3cf9-b737-db2540e4e774 | -7.17331 | -41.81645 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 59ed5944-88b7-3c24-8e80-9493dbb66e30 | -6.81856 | -35.14676 | 2026-09-16 03:53:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9f9f8fdd-51eb-3ad0-a79e-d2b39aabd1df | -5.99215 | -46.63085 | 2026-09-16 03:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 895eb707-50e3-3354-a3f2-2d8d2a370532 | -8.39969 | -42.21672 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8c6f374e-83ce-3cf6-bc21-ff050de1abf5 | -6.83492 | -43.51895 | 2026-09-16 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b56b193-e282-3e1d-8a79-ab92fac7c53f | -5.77504 | -45.09496 | 2026-09-16 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c8ccec5c-b28a-3eb0-b36c-79e094d0d73f | -7.3404 | -44.48948 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14df4c06-3d6d-3ecf-90de-78aaa4982cd7 | -7.36107 | -44.49641 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df165286-7ca3-3a28-9d9e-28e89ecd6d2c | -4.98959 | -45.15829 | 2026-09-16 03:53:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa20e54d-9d12-3614-8069-41264d367bce | -7.1805 | -43.50877 | 2026-09-16 03:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a642b5d4-1316-3b43-a310-8322f3b1dcb5 | -5.12405 | -47.61787 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 02008054-d1ed-3197-95bf-bab0511e62bb | -8.40414 | -42.21758 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8bf8184e-eca3-3cac-bb75-25d0224c915b | -8.54896 | -44.49668 | 2026-09-16 03:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fadee569-bc56-3993-9bf9-be8c94ebbb43 | -7.17109 | -42.10842 | 2026-09-16 03:53:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f1f401d1-25e8-31ca-bd50-94e73007c3bf | -5.62169 | -45.24935 | 2026-09-16 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 990a9863-b480-32f2-8fde-c67e0a3151c2 | -7.09441 | -40.65337 | 2026-09-16 03:53:00 | NPP-375D | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 41b66bcb-9bdb-30ed-944c-337b4e574a8d | -4.98944 | -45.15847 | 2026-09-16 03:53:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b160e45-ed35-3b5c-b7d0-8bb9d07638dc | -6.39513 | -44.06091 | 2026-09-16 03:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9377fed6-3781-344b-bc45-dc8d022ce01d | -8.54385 | -44.49522 | 2026-09-16 03:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7301d8e5-1b32-360b-919e-1919d69ba011 | -7.03756 | -42.04064 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1b6ed1d0-f0c4-37e5-afb8-d68d550fd2f0 | -6.95092 | -42.58185 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8504dc14-b479-3f8e-ba5b-1460bf128390 | -7.15278 | -44.24359 | 2026-09-16 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f40561ea-4471-3ca7-89b8-e64bf1ce2882 | -7.15804 | -44.2444 | 2026-09-16 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e32e306-7731-3ca3-b3fc-e3f425f42a99 | -7.03801 | -42.03432 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d1efef61-0d02-32b2-891e-cef2854070d6 | -6.00436 | -47.39315 | 2026-09-16 03:53:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e526d5c-c079-36b4-8f2c-d71d62a1a1f8 | -7.04132 | -42.04569 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b92c9010-5e0f-30c7-aacc-f38ad0f93e59 | -4.90897 | -45.67451 | 2026-09-16 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 147d7cbd-cb9b-3f54-887e-443370eb88ad | -6.65297 | -43.64576 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fd1182b-21cf-3c97-aeb3-c2487742c705 | -6.00293 | -44.31592 | 2026-09-16 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fc28f72-e925-35f6-b459-da0a6ba4a330 | -7.08767 | -42.10043 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4a30dc6a-6320-3081-95a9-a8d9288d59a8 | -7.17925 | -41.80839 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0b8da732-a790-3f62-887d-a6037b5e7d2e | -7.3529 | -44.50169 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d5f6071-a21b-3b56-bf99-464f58a87cc9 | -7.03653 | -42.04304 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ff4757e0-cafd-3143-9e26-8340fef2d43d | -6.95481 | -42.58084 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b2337971-b244-3d12-9f0b-698fdcba4d8e | -4.34026 | -46.6101 | 2026-09-16 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ceaf2ab-e643-3ee6-9f12-3c6474996ae1 | -6.33144 | -41.75907 | 2026-09-16 03:53:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bcf99e27-b27b-30af-9dd7-49105d5f4518 | -5.6053 | -44.84473 | 2026-09-16 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 990d166b-efa2-30b3-9f54-37268cc3b72e | -6.10766 | -46.10299 | 2026-09-16 03:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 911502e3-a6a0-310b-8089-2228c5e109df | -7.09217 | -41.7681 | 2026-09-16 03:53:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9cb22dac-ede5-3863-bc47-a388f918162b | -7.08347 | -43.56184 | 2026-09-16 03:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0b13b7d4-076e-39b7-9b1c-294705d07966 | -7.14027 | -42.09806 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 449163b8-8b1f-37bf-a631-bef3cfad481a | -7.07705 | -45.2368 | 2026-09-16 03:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a714d60-9faf-342d-8558-05a454e7af53 | -6.78639 | -48.66037 | 2026-09-16 03:53:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b54a556-701f-330e-b877-442d5a4fcbbe | -6.65804 | -43.64668 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fee89b3-dbc4-3b13-98b6-56d81220b9bb | -7.2604 | -46.18261 | 2026-09-16 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43e76607-03d7-3b1f-b8dc-b3a307a5898e | -7.26235 | -46.67416 | 2026-09-16 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8022ece3-93b1-39ca-bce1-b877a0a83b6a | -5.99786 | -47.3919 | 2026-09-16 03:53:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73216cd5-706c-36ee-a346-53c66f1910b8 | -7.10373 | -41.82209 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fae01e88-1661-3545-a34a-74210451309a | -6.95742 | -44.55294 | 2026-09-16 03:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af54923f-bcd5-3dbb-be96-606f2ec6614c | -4.36483 | -47.7795 | 2026-09-16 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 06017c7e-a8bb-3ddc-a398-b7a751534f4a | -7.13737 | -42.08812 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 69e9f8e3-cf9b-3a8c-b8c8-d10db4e95650 | -5.62243 | -45.24728 | 2026-09-16 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e618e1e-0c6d-34f1-8c1e-6ca519642644 | -5.60401 | -44.85198 | 2026-09-16 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4076838b-852c-3e7f-a768-7d99a7eb2bb0 | -5.10956 | -47.62153 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0a629ada-9462-374c-a68b-89affba63970 | -6.65474 | -43.64659 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39385574-25dd-3d7f-91d5-0d5ab31faed3 | -5.10802 | -47.61395 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca4bbfbf-8806-3aaf-b44b-c9953e9bc929 | -5.99484 | -46.63044 | 2026-09-16 03:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 74f57153-066d-30a1-860e-504df2033f80 | -7.13981 | -42.09554 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 235aea66-22dc-341e-96bc-cc242d65a6ce | -7.33509 | -44.48857 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 627be6f2-4490-310f-b7ce-a8bdff5e9b2a | -6.26635 | -43.28395 | 2026-09-16 03:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e4a61645-9db3-3d50-8d53-954ffdfccd0d | -8.21434 | -43.78075 | 2026-09-16 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 83c570fa-2020-30b8-9977-f50d73ea9c1f | -6.81468 | -35.1497 | 2026-09-16 03:53:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 903fe39f-bf63-3c20-b4c4-a4e8f2a8838f | -7.34153 | -44.48314 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 895fdc41-4527-3c44-bac1-5988abf90c87 | -7.07637 | -45.24058 | 2026-09-16 03:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 258d287b-de68-3194-90de-38cebe247aed | -7.08836 | -43.56628 | 2026-09-16 03:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fce93eaf-a4b9-3c1f-b217-2ce109607ade | -5.77007 | -45.09007 | 2026-09-16 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 93c68a0b-c1ae-3d79-ae3e-e50e9a3f7396 | -7.09659 | -41.76892 | 2026-09-16 03:53:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9700a618-deca-38d0-9cc8-fcd87262ed90 | -8.47689 | -44.56795 | 2026-09-16 03:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffd4be0d-ceae-33c2-a48c-9384cf9bfe04 | -4.34669 | -46.61092 | 2026-09-16 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75b8c54a-8224-3907-a1aa-9aa555def75d | -8.47634 | -44.57094 | 2026-09-16 03:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ab884ed-eb7a-3de1-b4f9-2635178cb53b | -5.2952 | -42.71451 | 2026-09-16 03:53:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c03b121b-4580-377b-8328-7fcda0f86c06 | -7.35465 | -44.50175 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4fbfff0-6a1c-34b8-9413-9004e2b6b366 | -5.10908 | -47.60794 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67c0aca4-2e5e-37af-9ed0-76e9a99bfa04 | -5.62242 | -45.24511 | 2026-09-16 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a544be68-7490-3eeb-8d83-be306bc5b54e | -7.18812 | -41.8099 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8cdc77e5-6d02-34aa-ae17-61aac386318e | -5.62563 | -40.85576 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4fbfc231-9d49-3cca-9779-cc3ee74b55b3 | -8.0091 | -38.33724 | 2026-09-16 03:53:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 823af9ab-bdc9-3e6c-98f6-f45a76b20867 | -6.65981 | -43.64751 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4765f2a5-b011-35a5-9815-edad4ee37942 | -5.99399 | -46.6352 | 2026-09-16 03:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ec026a3a-cecc-32ea-87b6-7d46cc30490c | -4.33935 | -46.61519 | 2026-09-16 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c57f504-1d2e-3168-9202-25f3a18dfcae | -8.54836 | -44.50007 | 2026-09-16 03:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe36fcf0-08d3-331e-b7fb-8b4fcba99067 | -7.35937 | -44.49634 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cc2b32b-b8ac-3f06-90ab-947ca68c53b9 | -6.78046 | -48.65887 | 2026-09-16 03:53:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad57100b-07e2-3a08-bfc9-f13f3b645525 | -8.05534 | -43.74971 | 2026-09-16 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b71faa74-f216-3d95-b480-fa919f1976ce | -7.54383 | -42.66259 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 16e6dd8f-e4e6-3e55-984e-f689f8339953 | -3.31757 | -47.13958 | 2026-09-16 03:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ce78f13-795f-33c8-b7f5-0524ab2fa87f | -7.14738 | -39.53368 | 2026-09-16 03:53:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e2d32ba-031f-3558-a6bb-a7085cc91569 | -7.26119 | -46.17843 | 2026-09-16 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 160974e8-7492-3567-8322-59ed732a5979 | -5.17361 | -39.74527 | 2026-09-16 03:53:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b81c7962-fb5b-3c7b-b2f4-ed99e4f9a2b0 | -5.77575 | -45.09099 | 2026-09-16 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| acf9d7af-3e88-3d0f-a4a4-080a30c38b0c | -5.99758 | -44.31489 | 2026-09-16 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c97bc3e-bec6-3d54-91c0-1cf69a6c846b | -5.09925 | -47.62449 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README15.md)
