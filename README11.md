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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d010dfb7-60db-3842-a4d5-0ff334144989 | -8.6115 | -54.64363 | 2026-09-22 00:58:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 7e33db59-8c7e-308c-a44f-2e04845923c4 | -7.33023 | -55.60476 | 2026-09-22 00:58:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| bb20d37c-1bcb-311c-8d96-ab81f8bebabf | -8.25426 | -55.2641 | 2026-09-22 00:58:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 333d2ac9-1326-3db2-8684-8dca141625bb | -11.32373 | -54.07685 | 2026-09-22 00:58:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| ff6a0cec-b2b9-311f-b558-4da6784abffd | -9.56508 | -66.04749 | 2026-09-22 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1971758b-420c-33c3-b0f2-92440ecff8ce | -9.37716 | -68.65595 | 2026-09-22 00:58:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5c104c38-55f7-3c7a-9e05-28c31022252f | -9.10277 | -67.83297 | 2026-09-22 00:58:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3b92628-f0ae-3e20-a732-554b36a5e5c5 | -9.18133 | -65.85945 | 2026-09-22 00:58:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5187f9c-cd62-3da8-91a1-0c8f19650e2d | -9.39817 | -65.9126 | 2026-09-22 00:58:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7cc912aa-4ed3-39f0-b528-de8020ec6a2a | -11.30953 | -54.04985 | 2026-09-22 00:58:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 117a270e-126f-39bf-84f7-d473ecbb8a32 | -8.25017 | -55.25798 | 2026-09-22 00:58:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| a615ce7f-62f2-396d-8e60-a372fea528c9 | -11.60228 | -62.40357 | 2026-09-22 00:58:00 | TERRA_M-M | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e0b29f78-441c-357e-84a3-06d8e2aea7ae | -10.35177 | -64.97834 | 2026-09-22 00:58:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 18bcdcc3-348b-392b-913c-1926410cabbb | -8.60353 | -54.63978 | 2026-09-22 00:58:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e0f05166-e1d3-38d4-8d32-f10e046e756c | -10.86988 | -57.17039 | 2026-09-22 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 342d4f38-946c-332d-99aa-e878212dc0f0 | -9.54234 | -65.6799 | 2026-09-22 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f4ad9891-8dc0-33cd-9e83-e3ba2736200d | -3.0542 | -54.4081 | 2026-09-22 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f9355ab0-21e1-3a31-85a1-ecaced2a278b | -9.2576 | -46.1422 | 2026-09-22 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 3f716511-84d5-3a21-993f-5f6dae66b455 | -11.6793 | -43.4684 | 2026-09-22 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| d0b5c020-bc94-30f7-9d16-2abba20b4a37 | -7.5888 | -57.6953 | 2026-09-22 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 8787aada-da23-3da4-8bc5-35fca4e0df45 | -6.571 | -44.1516 | 2026-09-22 01:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 6420c560-72d4-3361-80bc-adb574b10902 | -7.5889 | -57.6757 | 2026-09-22 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 157.9 |
| 4b0547cf-2229-3687-8fe4-e621289274a9 | -5.9334 | -59.9707 | 2026-09-22 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 84fb529b-d084-3a06-8a82-32e7edcebf89 | -11.3257 | -54.0282 | 2026-09-22 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 8772437b-dadc-3874-97a4-7d2e39c3f706 | -18.7472 | -46.93 | 2026-09-22 01:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 9b8cdd2f-e9c3-30fe-9a05-a96e63d093cc | -9.2383 | -46.1668 | 2026-09-22 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 267.0 |
| 008d5e9a-394b-3c06-ac46-0bed2906bccd | -6.0365 | -57.8235 | 2026-09-22 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| fe36e7d5-505d-37e6-bfc5-158a34df44e5 | -2.8608 | -57.7994 | 2026-09-22 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 05ac9824-13d3-3108-a749-98514a30e36d | -5.7569 | -45.084 | 2026-09-22 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 391.5 |
| ce84a61a-01db-3c5d-b3c0-42bffe79870c | -9.257 | -46.1873 | 2026-09-22 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| e700defb-cef7-3b59-93fc-095c5dfee0ba | -11.7675 | -50.804 | 2026-09-22 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 4ce138f3-77d8-34bf-9f69-25c7d5a1a74a | -11.7672 | -50.8253 | 2026-09-22 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 62f53ed0-2ca9-3961-965d-acf5fe37b019 | -5.7567 | -45.1067 | 2026-09-22 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 3c14fab1-e68e-3022-b0ef-55a9876e65f0 | -3.3867 | -59.5223 | 2026-09-22 01:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| dbecd5d9-c82c-38b6-8b7b-a7a7401d60fe | -6.0925 | -57.6847 | 2026-09-22 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 04ba58c0-aa9b-3a87-b2d4-d387fad21883 | -6.0928 | -57.6262 | 2026-09-22 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7386a8bc-7c56-35bf-b65c-76c8873f4599 | -6.0549 | -57.8227 | 2026-09-22 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| cb977bc9-b8b5-3c13-a622-1a5cf35ca3fc | -6.1109 | -57.684 | 2026-09-22 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a1b4606e-13f6-3887-b062-0bceca4ff061 | -2.4206 | -58.2712 | 2026-09-22 01:00:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| d962f07f-0a5e-3088-a991-73ec4582508d | -6.467 | -59.9902 | 2026-09-22 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 21558851-16e7-3b4b-9004-569ceb1b43af | -5.7864 | -43.8684 | 2026-09-22 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| e90e0ba7-47b0-351b-b71b-2ef2cebd7d8c | -9.2573 | -46.1647 | 2026-09-22 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 250.0 |
| 33e21729-7657-3078-b486-2c68a09701e4 | -11.3255 | -54.0487 | 2026-09-22 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 114.6 |
| be2ecf6a-f6bc-31cc-b4e2-cd874e61b319 | -5.7756 | -45.0826 | 2026-09-22 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| ee97fba5-12f8-34bc-ac3b-55f9b01cf71c | -8.6169 | -54.6328 | 2026-09-22 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 492195db-7a1e-3adc-96e9-5be063541a36 | -7.5704 | -57.6766 | 2026-09-22 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6492fcd5-9e7b-30d4-b21d-93212b1b0f46 | -6.5898 | -44.15 | 2026-09-22 01:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| dbc10d9e-90a4-3522-a85e-70ade5b0a0fc | -5.9333 | -59.9899 | 2026-09-22 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| bcea0b20-6032-3485-9f29-134ed7a73f6c | -18.7466 | -46.9534 | 2026-09-22 01:00:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 468a22ce-d58f-33d3-b1c9-7eee6f9b2656 | -8.7916 | -44.2778 | 2026-09-22 01:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ee386fbe-ec70-3dc4-9f07-5aa2fa79668a | -12.1458 | -47.3974 | 2026-09-22 01:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e6b3b633-5596-3490-b5e1-1ea1a4d11ca0 | -9.2386 | -46.1443 | 2026-09-22 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 229.6 |
| a00878ed-145a-329d-8c6c-a076e07afe28 | -5.7382 | -45.0853 | 2026-09-22 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| f0c74118-faf5-365d-9478-995dc1ab6fb2 | -9.5594 | -66.0359 | 2026-09-22 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 96dcf463-81c6-3c9f-960e-839653416b49 | -3.3492 | -59.867 | 2026-09-22 01:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 942440b9-e35d-3c32-a0a0-6fdcd3cf4ac6 | -11.4113 | -46.7798 | 2026-09-22 01:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 48e4091c-0bed-36fa-9c0d-0a0849868620 | -6.4671 | -59.9711 | 2026-09-22 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1b288f9b-bfb4-303d-83ca-b597b699e729 | -8.2574 | -55.2604 | 2026-09-22 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6c2dca3c-69f2-3762-a4e7-bf643f225b05 | -9.2762 | -46.1627 | 2026-09-22 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 830fbe2c-78a4-3d64-bd0b-a624159229da | -6.19605 | -57.79145 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| af4aad99-8d50-3f42-a972-8f764f488d40 | -6.73741 | -59.43092 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 9c0f71c2-5cd4-36f5-9895-11d21ed132ca | -7.05999 | -62.95155 | 2026-09-22 01:00:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ffab30d8-830d-39f0-a6d5-238abb1c4260 | -5.91337 | -55.71276 | 2026-09-22 01:00:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 523b47fb-996b-36f0-bc1b-ddea4733b664 | -6.19277 | -57.77052 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| f6985bda-c178-3864-8192-456f292ed028 | -6.46193 | -59.97395 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 563cfeca-6848-3245-9f07-b92ae3f94375 | -6.70766 | -58.99823 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 93485c7f-5835-3fdc-854c-d5782278bfa3 | -6.64033 | -59.93492 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ac9e2351-8c4b-3130-ace0-2871d3685a27 | -5.41519 | -60.21854 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 0c00f979-9632-37cc-8c9c-9ef171627261 | -6.61639 | -59.92429 | 2026-09-22 01:00:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 020c1d9f-0786-37dc-9f70-44145c868375 | -6.36554 | -58.28756 | 2026-09-22 01:00:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 444ac95f-048b-3b2c-ae1f-a2fce396bb80 | -6.3877 | -60.02011 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1ec43568-ac28-3deb-80e3-045d46acc9a7 | -5.93405 | -59.98925 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2d9ed2bd-0141-346c-91e9-c08323ad41a4 | -7.69724 | -61.54539 | 2026-09-22 01:00:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ec411511-417f-3c36-aa31-9167025bd7ce | -4.20895 | -59.91008 | 2026-09-22 01:00:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 60b7dffc-d39c-357b-8245-ead55f59ef1e | -6.62521 | -59.90856 | 2026-09-22 01:00:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 5e7fa135-e76b-3538-b096-4af0aa4cd843 | -7.57454 | -57.69791 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 16189553-f159-36b9-a41a-171b72634103 | -6.69608 | -60.01126 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 045b4ff1-3395-322a-bb1b-c1be6a1e844a | -6.7432 | -59.07612 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 047594b4-dab5-30b6-ba75-823a49f5400a | -6.13794 | -59.88219 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9773019f-7d22-3a37-82e2-4201a65d15bc | -4.20689 | -59.90393 | 2026-09-22 01:00:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| c1357ba4-18a8-3666-8921-c229a8b7e3dd | -6.70303 | -59.96223 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| e570c1bb-17d0-37f8-b385-964fbe144cbc | -6.43271 | -55.62401 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 729961ae-5e1e-340b-a371-a6cd86d93418 | -6.42725 | -59.98563 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9ee48554-e63d-3e9d-a860-9dec43bb03e4 | -7.7245 | -61.25417 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e4d143f3-8eb8-3bda-a6a7-ec0bb5bd489a | -7.29267 | -59.52919 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4d000456-8d49-3b2a-b787-5d16fb899194 | -6.61257 | -59.91698 | 2026-09-22 01:00:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9fb7ced6-c1b1-3967-ad62-e8d616e5e0dc | -6.75046 | -59.06897 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 807d4c7a-0b2c-3844-8d23-c209259eb94c | -6.88396 | -59.86574 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 15977b94-9a86-393e-bc56-32d3031638c4 | -4.20918 | -59.91921 | 2026-09-22 01:00:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 1ebee3c8-9d06-32ca-840a-34b7b13e5c17 | -6.10078 | -57.68236 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 4f96637b-6dee-3f2a-a112-1b236643d339 | -7.57151 | -57.67771 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 09850b35-b83f-3cd6-9e56-f03ede10270b | -6.70714 | -59.45755 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6bad6da7-70e7-30dc-88cb-36c4dd8c74a7 | -6.09126 | -57.69037 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| fc036836-aad6-3e17-b01f-9178a4dd454d | -5.94503 | -59.98742 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9254e328-0823-3032-ae3e-fa5c8c4a6d2c | -6.10446 | -57.68813 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 05ed855b-65c6-386b-b0ec-9ba894743b79 | -6.34301 | -59.961 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| dae4f8cd-a755-30ee-89d4-1cf57eedef8d | -5.82118 | -57.74494 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 0e13d3d9-bdcb-36e2-ada8-413d5ab87638 | -4.27593 | -55.44316 | 2026-09-22 01:00:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 8190eb55-aed6-300e-9ea5-ca19741c5ae5 | -6.13718 | -59.88799 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1a22f1c5-ea79-3631-8b7a-286d02306a30 | -6.13645 | -59.96085 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |


[Clique aqui para ver as próximas entradas](README12.md)
