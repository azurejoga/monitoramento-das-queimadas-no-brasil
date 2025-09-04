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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd4fe24b-45e8-36de-8583-1d4a813ddbc0 | -6.76184 | -63.12737 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0587a27f-29d4-300d-9f59-361673a81a52 | -3.43124 | -59.5704 | 2025-09-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44f4845b-8424-3b83-b007-dc17064f0b84 | -10.42833 | -50.37911 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5729fa45-56d7-375a-b334-7ab3ccc976d9 | -10.27559 | -55.01822 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95d1af15-9b5f-3728-a91f-3b09a3495fb8 | -6.66781 | -60.02757 | 2025-09-04 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac56c1c-d1b6-3912-881a-e58955e0b9af | -10.45893 | -53.62342 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49029968-d140-3cb1-9a6d-f690e2026bd0 | -7.27256 | -57.5612 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 803320d6-d81e-3010-b087-1ea662ea9491 | -9.61747 | -47.03609 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72ea576d-3445-3ab2-9081-3783280291ba | -10.14693 | -46.25954 | 2025-09-04 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8201949d-c685-3e21-b840-de23276f8c4a | -6.7545 | -58.7264 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5df870e1-f728-3606-8261-a2b815a5a7e7 | -6.54139 | -56.20078 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d2b89fc-2c67-391f-ac6f-1e5e7c3af76a | -10.4988 | -50.44394 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d93d45f6-1598-3c50-a7ff-4eb81ed0beb3 | -8.53178 | -51.31589 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 104ed8f0-e8e0-340c-9832-07505136ec1b | -6.87841 | -59.08332 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02c1da5d-3631-3641-9cc3-45136d799f2f | -10.46706 | -53.62903 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11031acf-0cfe-3936-9d62-13c0664bfc97 | -9.61496 | -47.03025 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aa4c9304-cf19-3920-9ee1-9c9dee279c57 | -6.73941 | -59.08261 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c39ea63-8864-3d7d-948f-840067dbd3c5 | -8.36559 | -48.33226 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cac09784-3bbb-37c1-b04d-e86f704a5d23 | -10.48775 | -46.76506 | 2025-09-04 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f99a9224-1d59-3055-89d3-e089eb7c225a | -10.26949 | -54.26675 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18e40673-ac8a-30d3-8626-52b16e28cd07 | -7.96932 | -46.34969 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d2047b6-3c4f-3bc1-93e9-f26c2e224175 | -10.97015 | -49.75377 | 2025-09-04 05:16:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5fe1895-cee2-3788-b5aa-dceac490f4b3 | -10.09847 | -54.75635 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f24a7355-f672-3626-949c-322741876bf5 | -5.10975 | -56.96491 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff8b1810-c41a-3d4f-bc5b-786e6b7efb0d | -10.98814 | -50.9194 | 2025-09-04 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66463277-d2de-3096-8508-66ba74d34c6b | -6.78302 | -63.14051 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eef8cd91-a986-30d4-81c3-7f652bb8e260 | -6.74071 | -58.72779 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e403b351-3edc-3b26-8c04-e6d4753c7ccb | -10.48249 | -53.65012 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6a9a792-b4a6-339e-a92a-841c5a76dc0e | -9.06109 | -46.995 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6939b149-7747-33a7-a693-c94ed0b76ca5 | -9.32811 | -55.2294 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61c5b57c-12ac-34da-b4f7-6db54df00de1 | -7.9769 | -46.34456 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b64ea634-4693-3faa-9c7c-4c0d73e69171 | -9.43206 | -48.09235 | 2025-09-04 05:16:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 550e76ca-b554-31e9-980b-1204ca7caba3 | -9.07255 | -46.99253 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ba93240-2df9-31ee-8663-0a020c68e4f4 | -10.06845 | -54.78843 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b78c3a1d-228d-31d4-bd4c-9e200b615324 | -4.42213 | -56.13317 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef637f75-619b-31d4-9aee-56a3bc1e5567 | -6.47103 | -53.39909 | 2025-09-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24f1f7e9-e14e-354e-9f92-6bb5d6a6d12a | -10.75343 | -48.27525 | 2025-09-04 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3414dcbb-f936-3717-9a19-c4e4a1da3bf9 | -7.70729 | -50.31974 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ad99905-6201-3312-a343-c912c676fe07 | -7.73948 | -48.76926 | 2025-09-04 05:16:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bdf7d2d7-aec7-327a-adfa-41bf0767fab0 | -10.47143 | -53.62969 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3db653c-3dbb-3178-a1ba-ac9c3b452d04 | -8.53538 | -51.32693 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5daf56d0-adb7-3457-ae39-bd87494efc98 | -6.67599 | -48.40575 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 09025f29-0de8-3976-8758-4b137f6ff69d | -4.99711 | -56.25651 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| ee7e1822-7908-366b-b6b5-dfd3e2832779 | -5.6877 | -45.94292 | 2025-09-04 05:16:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a921c40-d12e-3ded-b5dc-7095bb04875d | -6.69862 | -48.41627 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bca22bef-08dc-3198-ac77-360f7960b705 | -10.9649 | -49.74901 | 2025-09-04 05:16:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b168aa16-cb7b-3e6f-ad11-73eebbb17d73 | -6.32108 | -45.67977 | 2025-09-04 05:16:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdb0fe1c-4e58-329e-ab51-561284ec5962 | -7.34208 | -48.1892 | 2025-09-04 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8eb11e6-5cc8-335c-aa0d-7f5ae8b0dc1d | -8.53994 | -51.32575 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9073b30b-8fb9-3760-9314-1977c967677e | -6.86824 | -45.57422 | 2025-09-04 05:16:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8804e4f8-929b-33be-8d15-bc70055ba279 | -4.99499 | -56.26054 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f6cfe92f-7fec-38d8-8632-ecc0da04dc2f | -6.83994 | -59.15524 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85ebe6c4-5127-3cbf-9a07-c2dca0f3aa7a | -7.70772 | -50.31666 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03077913-2a7f-3784-81f5-65a83111c3f3 | -10.47661 | -53.62761 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c94152f3-836a-34c5-bfbf-ae9b268885c7 | -5.31403 | -55.85851 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99e941a8-2b31-3fca-a649-ed4184b1588e | -6.76864 | -63.13331 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 499c415c-e5a1-3b46-a728-d22017fdf3de | -10.09245 | -54.77007 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3060744-eabd-3050-8344-ca5fcf284624 | -6.87427 | -58.93727 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aed3214-e88f-356b-9955-2a8c140e94ba | -3.68151 | -61.67363 | 2025-09-04 05:16:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 105cddac-dcff-3b86-9606-0c4881393352 | -4.99769 | -56.25265 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| f3806a3f-95cb-3881-a99a-7c7f5ca9b959 | -7.97169 | -55.31293 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63a74893-a3b2-359f-991b-e43f57c0e85e | -6.7501 | -58.73281 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ec598358-3bd3-3784-8917-e13631e7ee90 | -8.52991 | -51.32483 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1af799be-54f2-3ed5-b0b4-89bda1674e06 | -10.42925 | -50.37199 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cc09bf22-c2f9-3af7-a689-33cb23924926 | -6.17791 | -47.28447 | 2025-09-04 05:16:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd70a62f-26b6-39d1-8c9b-2ea3270087dc | -7.07477 | -46.19373 | 2025-09-04 05:16:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9ed48e4-b406-37d5-a051-bc2a7b153c6c | -6.77622 | -63.1346 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76bd6e2e-c3de-34f0-8704-4a6c8ec67d1f | -6.46375 | -55.88687 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88e55dda-a514-3647-9fde-d707301457f9 | -9.46674 | -47.60585 | 2025-09-04 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1873b49-bb49-3e4c-b755-ded0055c0344 | -8.36585 | -52.54571 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a256a1b-43fb-3464-aab6-9f07cbac837e | -6.67815 | -48.40421 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 42950717-1871-34a5-8686-9c44c6692428 | -10.51149 | -50.43124 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb150fa8-8c04-3872-bf42-3efb55e0897f | -6.22797 | -55.93783 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95647481-32ef-30b0-a4c8-6feca6f704a6 | -8.36442 | -48.34114 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3364051-9194-3e96-be89-7d8270969c7c | -6.46736 | -55.8874 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e037cd1-3903-360e-9733-39fa31d16e4b | -4.88858 | -55.85154 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87d536b7-4559-39df-8741-5f1fe73405fa | -9.95591 | -51.64677 | 2025-09-04 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 686ad506-89fb-3257-8fe4-3b7a53f6f44a | -10.47223 | -53.62698 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3926de23-1038-3051-9d5b-7673e5d595b9 | -6.6884 | -48.41685 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8ba2939-cb52-3ecf-84c1-9981cc3c4f20 | -6.74293 | -58.73524 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 2ee55b14-6abc-338e-9f31-1b7e7a29b1e4 | -10.49391 | -46.77192 | 2025-09-04 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 417dd1ca-5138-3920-8d51-9e794305a05d | -10.44878 | -50.39262 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ebedc55-a04f-338e-87d6-efe39eb7f241 | -10.44642 | -53.61718 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70438c59-6e61-3845-9510-e60fc46a8015 | -5.60141 | -45.02973 | 2025-09-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 604d5428-9eb8-3b47-b48d-d52d2629a197 | -5.02299 | -56.10912 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 230cf31b-9edb-32be-8933-200fdbd6b99f | -4.99653 | -56.26035 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 2b8b4244-17f9-3d84-81d7-ecf15c96e62f | -6.76465 | -59.67294 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc02ea5c-fbb3-3087-8e9a-3e3d15cc276b | -6.7418 | -58.72086 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b39e1655-d700-314b-9af4-58068f0c787a | -6.46684 | -53.39848 | 2025-09-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe0b178e-48da-3789-8267-fe887a198195 | -6.16864 | -55.72097 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41d24753-8056-373c-8ced-c890f676599a | -7.34811 | -48.19007 | 2025-09-04 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53d97c1a-5925-31a4-91aa-1c4c9a92f2d8 | -10.9755 | -46.8535 | 2025-09-04 05:16:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 955f074f-72c3-378e-8273-8715a4ddefba | -7.97616 | -46.35037 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23028f87-9cdb-34d5-9c6b-f9fc0f44407c | -9.49872 | -57.81594 | 2025-09-04 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0f901e5-241d-38d5-8004-1cfbad696a58 | -6.76563 | -63.12803 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4a6c8d86-40e0-3062-ae52-3a4425416302 | -9.97314 | -51.63192 | 2025-09-04 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ed2a06f-ae28-39f1-a7b2-193e588762d3 | -10.42741 | -50.38622 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e824c630-e733-379c-9f77-613eb2399d83 | -7.71718 | -50.32127 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 42820a66-6b5d-3b5d-9966-73949ae54db8 | -4.98123 | -49.9059 | 2025-09-04 05:16:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eec6d138-3aa3-3ebd-926d-c41591621ab6 | -6.68136 | -48.41053 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README81.md)
