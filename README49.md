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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a679911-740d-3868-a7a3-fde38013469f | -3.23905 | -61.24784 | 2026-08-30 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b514f629-86f2-3c0c-b739-186419555ef2 | -4.9661 | -55.83742 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67cf281a-beb3-3e1b-b043-ead5691f034d | -4.96131 | -55.84498 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c0137f9e-db54-3f55-9ef6-062d832981b2 | 0.87558 | -59.70456 | 2026-08-30 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42b4af3f-d1a7-30ab-8c06-951d23cd83a3 | -4.95713 | -55.84852 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5491e92b-e116-3e3f-a64f-338284727866 | -4.95834 | -55.84043 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1bb6989b-e41a-397a-b403-f49deef8c498 | -4.96488 | -55.84549 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 5964e83c-3bc9-35d8-8ac9-e8f950e56fdc | -3.72785 | -60.60683 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 647fe08b-81d3-3acd-9127-bf4452b58b08 | -3.62817 | -60.54936 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e36aff8-c6ef-36bb-a150-ba340a990308 | -4.15322 | -60.69128 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd1b6447-2f6f-32fe-94d6-1fe68354e608 | -3.62699 | -60.55685 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 47b41825-2eab-353a-b732-fa72229ff0e0 | -4.15381 | -60.68753 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b31fe8eb-2d1b-32bc-b0b8-482373e41b30 | -1.24933 | -55.70622 | 2026-08-30 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ab00898-efa9-3e03-996b-ce119d75662d | -5.8898 | -47.72392 | 2026-08-30 05:16:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 54f69c2c-15c0-3d56-934d-dc37f10c175d | -4.47789 | -55.76422 | 2026-08-30 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4ee44cf0-ca97-3f20-a786-de1f72c75b6b | -3.66582 | -57.07959 | 2026-08-30 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d9e77db-40a2-3893-94b7-a083d62c49e6 | -3.29277 | -61.59078 | 2026-08-30 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47bd936f-0f56-3571-ac18-06d20631a25a | -4.9607 | -55.84903 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7a6489f3-f489-3365-aa1d-82ccd8113e4e | -3.84307 | -59.67536 | 2026-08-30 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15136535-2884-36ed-adc6-82f767584814 | -2.10931 | -49.00131 | 2026-08-30 05:16:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c769f86e-60e6-303a-9b4b-dee1c786061e | 0.13725 | -60.40553 | 2026-08-30 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2dc47934-923f-3fcd-995c-de853592ba76 | -4.92328 | -55.76489 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58575b5a-365f-3d85-9d67-bf31b473324a | -4.48144 | -55.76482 | 2026-08-30 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d06d0f43-9259-30d1-80d9-8218e81fa769 | -4.92881 | -55.76907 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c989be9-9f58-3a2a-ab90-7d5b3153d65f | -3.07078 | -61.07535 | 2026-08-30 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7072c73c-977a-3f70-a9b9-c967403cc9a8 | -3.64507 | -61.70697 | 2026-08-30 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98e5ae7c-37a7-3bfb-8de1-47e9c5b45667 | -4.08347 | -54.11052 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74e4b303-7e22-339f-8ae5-aa0fd17a24b9 | -1.24991 | -55.70242 | 2026-08-30 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e064dcc-c75a-30b7-b07b-2254e7818fd3 | -4.97028 | -56.2911 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4714cbaf-de42-33e7-a110-cdb82a072d10 | -4.69548 | -55.66622 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a264908-30c1-30b9-843d-9f5ca8a9e13c | -5.28983 | -50.94072 | 2026-08-30 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6658e0f-a283-334e-9a42-b96eda0e17ff | -3.49781 | -54.65127 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b3cc4f4-c669-3803-a35e-38820484b531 | -4.15263 | -60.69505 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3818a51-093c-3bd1-b39d-ad3deb7c23e8 | -4.15598 | -60.71869 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0dbfd61-ec5a-3668-8a1d-e8704d65f156 | 0.58139 | -60.44398 | 2026-08-30 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63a38d90-6e7e-3780-80b5-ecc71aca41ac | -3.62758 | -60.55311 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1f3c248f-9601-3823-9dd3-e798db40019a | -4.22171 | -59.56155 | 2026-08-30 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1625eb66-0015-362a-871c-8d0f19e5ed2e | -4.3715 | -47.77327 | 2026-08-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 5356f77c-5270-3811-b761-5fbeac868f00 | -4.92623 | -55.76954 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d41313e3-efa9-34f6-b0b8-cc64b82273c5 | -1.25337 | -55.70292 | 2026-08-30 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5727f11-40ed-3907-baee-fe4149c1f739 | -3.76713 | -59.33635 | 2026-08-30 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 277fa433-78da-3ec0-8315-c2fc4d84f214 | 0.13726 | -60.40575 | 2026-08-30 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb831aba-499f-374e-b8cd-937f716574b1 | -3.22393 | -49.22613 | 2026-08-30 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a48d6026-fd9b-3c49-8852-eb3b223669bc | -3.61843 | -60.54402 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c103f11f-47e7-3a0b-92c8-6bed3f38bef1 | -3.94141 | -59.33131 | 2026-08-30 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09b2a5f3-8c10-35dc-b19b-abea3edae01e | 0.58257 | -60.44687 | 2026-08-30 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ea10a24-6b79-317f-b8ca-1db06cd3fc3a | -4.96135 | -56.27095 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5485442e-6e42-321c-a60c-e7ad721a6e06 | -4.12172 | -60.77909 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a05fe1ff-dfae-307c-9875-1397fa59b7ad | -4.15608 | -60.69559 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f055dca6-0e65-39a5-9c2b-aab5682073a6 | 0.01458 | -51.11006 | 2026-08-30 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09ffe9f1-8658-3920-b39f-14b663ae80f1 | -2.01871 | -52.10948 | 2026-08-30 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0123b3b8-3de7-3497-a76b-00c8bbc019f1 | -4.12517 | -60.77962 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0d41100-aa33-3226-ba9c-d19ecb6694a9 | -1.24645 | -55.70193 | 2026-08-30 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb0b5d80-fdce-3b95-91af-6126cad05179 | -3.63043 | -60.5574 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5ec77c10-8ac2-39ab-a152-8ab2f8a639f5 | -4.96671 | -55.83333 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5f9fd38c-4e19-38ae-ac13-18e8de9a9916 | -2.80096 | -49.58289 | 2026-08-30 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc3850ce-b7b1-33ca-830b-ba5a709ca8f4 | -3.937 | -59.33777 | 2026-08-30 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 917aad04-ad8d-3132-8646-201b0cf20a62 | -3.1677 | -60.13278 | 2026-08-30 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e8629d2-ddd9-380a-be21-16b36db7b4e9 | -4.36554 | -47.7723 | 2026-08-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e7112d8-1555-3d79-8f63-e029a697f963 | -2.0346 | -48.78305 | 2026-08-30 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d04deabd-31ef-3270-9b67-c1fd2f1d4cc5 | -4.2187 | -56.08297 | 2026-08-30 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1dd4caf5-ea9d-3fd9-bc78-a5a069572664 | -4.9298 | -55.77011 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a415f036-486c-3a8b-851e-745f0e35f503 | -3.48833 | -54.66363 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f31e5026-a949-396e-acd9-04189a84e101 | -2.02301 | -52.11013 | 2026-08-30 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38d09ea5-2613-3c40-a4f5-edab3d973d09 | -4.95417 | -55.84396 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ec38b560-c66e-392c-a08a-e6e80b96a234 | -2.0046 | -44.80272 | 2026-08-30 05:16:00 | NOAA-21 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c50f2330-466b-3dd6-90d7-e2b0238c2fd8 | -4.92686 | -55.76546 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d5e39f-8370-310b-86a6-7e5c417f6799 | -3.27324 | -50.02078 | 2026-08-30 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7168b8e3-e7a6-351c-96ba-6e33e9ce2d03 | -1.36339 | -54.63316 | 2026-08-30 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7239b255-cbb4-3095-abce-6a7dd29a129c | -4.69485 | -55.67035 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29738d53-ddf6-3055-90cd-1faaee88ba1d | -1.88035 | -55.13521 | 2026-08-30 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3185893d-f5ce-3e4c-b595-d56926e91011 | -3.489 | -54.65913 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ec779e4-e315-363e-8c9d-8e6d13fb17d5 | -3.18946 | -48.02038 | 2026-08-30 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70a33093-09d1-3b9c-a69a-5181d642214c | -3.62875 | -60.54562 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac437557-61c7-3179-a88b-c148d1bc63a5 | -4.08897 | -54.10799 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d03bb28-6bca-3055-b65a-f61b2edf96c8 | -3.63446 | -60.55419 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ae01af02-94c8-3153-a285-7878a729666e | -3.45194 | -61.7181 | 2026-08-30 05:16:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 889c4526-671f-3a36-ad4d-4a0e16823ed3 | -4.9732 | -56.29544 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da498657-44e1-3cbc-9741-b507ab1cbe01 | -4.08422 | -54.10559 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78bbceca-d79a-3b5b-9beb-e46b64e73275 | -4.9256 | -55.77364 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16f53f71-8213-316e-b8ca-cfd8860e293c | -3.09472 | -61.51537 | 2026-08-30 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84b58445-e6f0-3a43-9fe3-f577cdbeaa73 | 0.19889 | -60.49891 | 2026-08-30 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f9777fe-f973-3842-88c7-820463226559 | -3.62414 | -60.55258 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27260eeb-fb02-3206-ab4b-5790ed0acf81 | -4.96252 | -55.83692 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1c5d181-67ca-3bf0-8257-dcef0174d595 | -1.44088 | -60.26199 | 2026-08-30 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90e02206-61d3-302d-aee0-345ea55000e9 | -1.20779 | -54.20983 | 2026-08-30 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 627415a4-f3eb-31da-b0e8-2c8f083b9cd6 | -2.75048 | -60.23837 | 2026-08-30 05:16:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b94adee3-55b0-37da-acf4-aded421fb1ab | -3.62473 | -60.54883 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e12b457-9676-3b69-a7cd-471a0b0db36d | -2.02076 | -52.10759 | 2026-08-30 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9d80b1f-fc41-3820-85d8-8f10b1ee4255 | -3.63161 | -60.5499 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18e69769-edc1-35f0-a751-20fae14c771e | -4.3649 | -47.77673 | 2026-08-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 12185c20-57cc-3912-8797-07ab96e1b423 | -5.94328 | -57.73849 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abeb8bb2-f81a-3ca6-bcb6-8904a9fe27ce | -9.16376 | -59.51527 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5567716a-7754-3794-89df-aeba34a6d9b1 | -5.89411 | -57.75257 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eaa3cd1-025b-376a-afed-b58c0eecf3c9 | -7.24265 | -60.6316 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5d3f253d-c866-3d27-ab71-218902b3a1ac | -5.96152 | -57.68641 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc4d9aae-0038-3f85-80f0-d69446de84fc | -11.03584 | -57.24658 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13959c7c-6d62-36ab-8c4a-9e7d7c6f7af0 | -9.41877 | -56.9832 | 2026-08-30 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dfc4651-8df0-3766-b2d2-04258beb2339 | -11.18783 | -55.09615 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f18ae38-16ff-3600-9fcd-1a5ac693b11c | -6.79354 | -58.99125 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README50.md)
