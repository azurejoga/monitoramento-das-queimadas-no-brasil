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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2c3a5a9-375e-37a2-8804-a1ef04cb1474 | -6.64375 | -58.82688 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 28225bea-4203-333f-8bd9-c934b1115216 | -6.62889 | -58.83521 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| cee4367e-e45c-3d44-acab-ac88f1df7223 | -8.9409 | -62.2141 | 2025-07-26 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd21d2c0-c7cb-3e97-aab5-867a1cd57c8f | -6.68497 | -58.84797 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 19270e88-54fa-3fb3-bfcf-c14a39f9760f | -8.52844 | -63.8835 | 2025-07-26 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a117853-088d-3b2d-9a0f-c7ceb8df262e | -10.85528 | -54.03992 | 2025-07-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07afc9d5-3302-3eed-86d5-4d5ecf6d0a21 | -8.96834 | -62.22996 | 2025-07-26 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0b90919-5d00-3a51-ab41-53da2cda260e | -6.67897 | -58.86477 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 178b0108-3b1a-31e4-b098-6075c62ba542 | -6.53491 | -56.26016 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc1bb080-c610-398a-876b-7e098ce777bc | -13.09113 | -47.35229 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c5713cd-68ef-3f8f-af4c-767f7ea6c6cb | -8.50189 | -64.04257 | 2025-07-26 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8eadabd5-f92e-3b97-a267-b03b6b3faa48 | -9.20401 | -59.6808 | 2025-07-26 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c514f656-b76d-3623-a482-569700993bde | -7.28855 | -60.18097 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 766ebee6-a370-33f8-b45e-fe377813d3ba | -6.67004 | -58.83502 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8a30ff72-996d-3124-be40-01ada720913b | -6.62228 | -58.83418 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 8347c796-f576-3fda-9284-811ab0d45117 | -7.89936 | -63.53009 | 2025-07-26 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 137cfdd0-abe2-3ecd-a62c-bdfced261927 | -10.85042 | -54.04339 | 2025-07-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c18d0f2-2b7b-30d1-84bd-4e7e3ce4159e | -6.67773 | -58.82913 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 34be70ee-0b1f-3eae-a238-a7e8febadc79 | -7.6565 | -69.93096 | 2025-07-26 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78d87f00-337d-305b-8e41-5aab55355076 | -6.62559 | -58.8347 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 44ca6efa-ed9b-3056-8e16-db74df218a91 | -8.50108 | -64.04745 | 2025-07-26 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3245676-563f-3a6a-b653-d7789cdb7327 | -7.57158 | -61.40396 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30c6eb0e-cc05-3e87-85ed-ed2a0cae1e5e | -6.63328 | -58.8288 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| c8f1342f-e594-3a86-b8bd-5c4943fa5a2c | -13.09788 | -47.35417 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 056ef833-27d6-3eb7-bcda-f588e8d81023 | -7.66228 | -69.93202 | 2025-07-26 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ce5e477-11d0-3083-9286-63643642596f | -6.63389 | -58.84663 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a2b956c9-c6f3-3f02-bb0e-6cf117b25709 | -6.53787 | -56.26477 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d96919e6-164a-3fcd-aeb2-2c6b7e5c9714 | -6.65651 | -58.85368 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e014fafe-d23d-3b8d-9c8c-c3c8d0973d73 | -6.66458 | -58.84836 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 136.0 |
| bd577bf4-1186-37c5-8b25-753363e15b3e | -6.54264 | -56.25718 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0063f4a7-fc3f-3922-9aa3-b0c1bc0c37ac | -6.67343 | -58.85682 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a676456-e011-37db-bc4a-3c1f9853cb5c | -8.06959 | -63.85952 | 2025-07-26 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb89ec61-4feb-306b-8dc1-5d6b227bf7a2 | -6.65705 | -58.85022 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 9d76eb51-716b-368f-a9f4-33ac434b65d1 | -6.63281 | -58.85354 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 1b6e75df-6921-37c3-b9d8-1f5595a4ef77 | -6.66503 | -58.8236 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 4dadd95a-303c-3791-8feb-715737fac43c | -6.67111 | -58.8281 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5e48e7d1-99a3-3612-b172-24c633589d88 | -6.68158 | -58.82617 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 311fbdfd-f3ea-366d-b047-e27988e27a12 | -13.11244 | -47.35714 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3379b6a7-71b6-3093-8959-ec1c74435e22 | -6.63551 | -58.83624 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b2848f5b-d7f4-3142-b1af-2720e3ad20bc | -6.5581 | -56.25121 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fc4385e-5e0e-3a83-89ec-96634f1530a2 | -6.54742 | -56.24958 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09d3e682-a687-368a-92e4-c89fc1e4041c | -13.108 | -47.33218 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 10791e7e-1a7c-393c-b4de-dfe0e3c121f4 | -6.54385 | -56.24903 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc53aef1-93e8-3519-9adf-386cddaec0e7 | -6.62451 | -58.84162 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| b33bfe96-bb22-3c07-bc85-9546d3dcfa43 | -7.29632 | -60.17498 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c499797-53ff-34f6-9d41-e6b1730451e7 | -6.64652 | -58.83086 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0a8f5076-287e-389c-bf27-bf2cdf9da595 | -9.46025 | -57.85189 | 2025-07-26 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e7d0cdc-cd6e-3536-8b7f-37a89f32eb60 | -9.81036 | -46.71307 | 2025-07-26 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7048bb6f-3767-37f1-a7a9-d01c66afc583 | -6.62282 | -58.83072 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3a42aa12-2d67-33fc-8272-a8d68f4b1173 | -6.54802 | -56.24551 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02d9ddd0-d9a3-3d4f-8f5d-fd1a9e47d68e | -8.07458 | -48.01048 | 2025-07-26 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cefdb58f-8829-3191-aa47-b4cb36fd3b15 | -6.64706 | -58.8274 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| d8a9d2f3-20be-36b6-afa2-1daf5de76982 | -6.67066 | -58.85284 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 526.2 |
| 0f835232-315d-367c-b10f-0b31a1184f20 | -6.64712 | -58.84867 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 6b9bd3c1-5dac-3956-94aa-d1cff1d3fc57 | -10.68055 | -51.88119 | 2025-07-26 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 961dc666-404e-3cb5-930c-693f72141959 | -6.64874 | -58.83829 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2d0adf0b-03e9-3fab-80db-6bca1897a9d8 | -6.65921 | -58.83638 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9f053b59-fb20-3063-a169-8c8ebcd4cb82 | -6.66342 | -58.83399 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e7a01ca8-a1be-3000-a429-600397132dfe | -10.35194 | -46.64532 | 2025-07-26 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25cb5540-b254-3b4d-b0d6-2360e1a633d7 | -6.67666 | -58.83606 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fd17c2c1-bd1a-3cc3-a5a4-2fe1d26d39d7 | -6.61843 | -58.83713 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 777a978e-2559-3cc3-a52f-bdd55347758a | -6.65482 | -58.84278 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2be8741f-206e-3936-93ab-a068b4a217cd | -6.6559 | -58.83586 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b2c958f5-e1a2-3fc9-a282-01e41d86b56d | -6.55098 | -56.25013 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de187db0-f59b-3ac9-abfc-653462f35b3a | -9.60781 | -63.46514 | 2025-07-26 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aa2a3ba-f2b6-3c0d-acad-b299919709f9 | -8.49579 | -64.03153 | 2025-07-26 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58d0eec6-3261-38c8-b488-51de5e3fed62 | -10.8472 | -54.03461 | 2025-07-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9f575c7-9d16-3256-967f-8aac603fe6e6 | -10.45966 | -52.72419 | 2025-07-26 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f020cad9-b92e-3f31-82da-1fcbe90845ce | -6.6212 | -58.8411 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e272c6b0-2267-3f57-8aa5-7c6df76db95e | -6.67727 | -58.85387 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 7510f52a-a25f-32a1-bb76-2efd06851cb7 | -7.27524 | -60.17887 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 099c6b0c-86fd-3077-98ec-92dde1d85969 | -6.65428 | -58.84624 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 961d16f1-87b9-3e56-84b1-1699d38d8c1e | -6.6745 | -58.84989 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| b7cfaf63-cbfe-3fa1-958d-dec1ed92e533 | -5.92011 | -61.30291 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2cbfb63-015e-3b93-b6ef-49ad88d2751e | -6.6602 | -58.85476 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a775535c-e8fa-3fea-b245-5ba8b8fa7c94 | -13.12032 | -47.33919 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0b80b69-4412-3308-b625-133175b96ae4 | -6.64051 | -58.84764 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f0a838a5-66b4-35cd-8ae3-4573161d80e0 | -9.3932 | -63.50739 | 2025-07-26 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04a926af-c03f-3d5e-a807-20c3bbb6d22d | -13.1136 | -47.34568 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 604a3470-9a83-39a7-a467-ccd44fb62ba7 | -9.73203 | -48.01998 | 2025-07-26 05:18:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 67a98f60-31e9-393a-b9f3-690b19bc08ff | -6.6678 | -58.82758 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 5f766625-f122-3562-a22c-a02defda1c78 | -10.67412 | -51.89213 | 2025-07-26 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 83c2e49e-ef12-3293-8dfa-dc4df96e5109 | -6.67397 | -58.85336 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 17f3d8af-0a2f-3bc6-803d-7c90fac0d69d | -7.44799 | -57.66782 | 2025-07-26 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f69c0ea3-3a1a-3066-b27e-068eb6e88f98 | -7.5635 | -61.41035 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bf512514-45a5-3495-bb93-da428992e4bc | -7.56068 | -61.40605 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f534281b-ce2e-32ed-b925-c0fd3d21d2e3 | -6.55871 | -56.24714 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 621d1eb9-7d3c-383e-b9ae-7638564e8ed9 | -7.46417 | -49.39438 | 2025-07-26 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49172dcc-79dc-3ca4-ba33-dcc4ebaafa7a | -6.54325 | -56.25311 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e95ae94d-4637-3ace-a921-d638e74dea24 | -7.57219 | -61.40022 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f854a72b-b1ca-3045-84f5-7869729d93be | -6.64982 | -58.83137 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ba3cac94-23ff-3f67-a50a-c71ef2d0dea2 | -13.11156 | -47.35614 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2efdf5c1-4745-31b8-a15f-39ea00d98fbe | -8.30706 | -55.10893 | 2025-07-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c160ec98-1c70-3bc3-831e-eea605d34a82 | -9.39434 | -63.50931 | 2025-07-26 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 435d9f94-9c6d-35da-8bef-0a3d7466e72c | -9.62847 | -61.46021 | 2025-07-26 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5583683-9cea-33d1-ac9e-a09e3b554fb0 | -6.53847 | -56.26072 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3424417-34ae-33aa-885b-2bd1da3f14e3 | -12.68803 | -46.99204 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 20230ccb-3e2b-3c65-b59c-eff43fe20f91 | -6.68712 | -58.83414 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 947570d9-272e-3813-a4b2-147fff0548e5 | -6.67335 | -58.83554 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b74f7e6f-c8e3-3b35-bf65-4c54590ad6e6 | -6.69158 | -58.84901 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README25.md)
