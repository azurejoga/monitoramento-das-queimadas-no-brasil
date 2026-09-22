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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18253dd1-94ed-3d56-9f64-da549d4f6bba | -3.44213 | -50.66158 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ed10e3-c1d2-3d82-87c6-98fc4cd9e3d6 | -8.83375 | -50.49361 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 197e2f3a-8950-3374-b7ed-3e730a624980 | -6.7113 | -59.00496 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9d6287b-62c9-38c4-81ab-d5b85ca5a993 | -3.37477 | -52.79728 | 2026-09-22 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dce69b2b-434d-3a61-b943-dc0a5059b7fd | -9.28619 | -46.18451 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 373c8c3d-d6b9-3095-a0ab-3d07c4526791 | -9.23274 | -46.16875 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19f6fe20-5a3d-3efd-9ad6-b0d7b4481dc6 | -6.45939 | -59.9939 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c2ff4a9f-0ef8-3b7b-b6e7-2cd62e0e9632 | -6.74985 | -55.09184 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d75e7ace-6188-32b4-b315-3da0cb339d54 | -6.65507 | -50.93084 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26fd4853-a649-3ef1-8734-642ffd1310b7 | -3.38664 | -59.52816 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13e25c3d-7df5-350c-aedb-364558344642 | -5.98458 | -57.6977 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bba02d61-3d91-3790-8ec5-e8484f84ef3f | -5.85698 | -49.77793 | 2026-09-22 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| de9e39d6-ff12-363e-bc85-d99d6839aa58 | -4.4207 | -55.49782 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6e25a445-ba4a-32e9-a32f-47683c51bde0 | -3.55769 | -50.28915 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d15ceb0b-4797-333a-b48c-44c406fd822f | -6.78553 | -48.67657 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dad33a16-d183-376b-9473-ec151dce33d4 | -8.13695 | -46.8266 | 2026-09-22 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ee95d8f-0fbe-3722-a575-8cd45dc57615 | -9.8754 | -55.85825 | 2026-09-22 04:46:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 854ab9d0-cc7d-33f9-b0e3-52cb2df118f8 | -10.52053 | -44.8782 | 2026-09-22 04:46:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 151e07ef-4935-34b7-be5d-16bab473d7e7 | -11.14338 | -42.83847 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3d98a803-2e8e-32d5-b2ea-dcd91c248deb | -10.45321 | -51.32746 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ec21dca-2d38-3f2a-81f1-2fd30e773dd1 | -4.02395 | -51.04905 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76a91868-7779-376a-bd34-d3b1a1753346 | -10.39468 | -50.23293 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b3459ba-f576-3aab-9626-7595879a5eee | -6.45277 | -59.97047 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2af074e3-1fa4-307f-a6a6-6cf6468051ca | -4.34848 | -55.64792 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36327619-b40d-334a-93a7-eac77782285f | -5.98482 | -57.77982 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0db35338-4658-31a9-a895-7e294c264711 | -5.7614 | -45.09051 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 49cb5576-3579-308a-93a5-fa78b5115133 | -3.05749 | -54.4057 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f9d061c-f032-39d4-86fe-00134d68b6c2 | -5.83381 | -43.8496 | 2026-09-22 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0e41a0b-5862-3743-977a-c67fb2ace214 | -6.72776 | -55.0762 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7d9df52-13e1-39c7-aac3-7afac5b65047 | -8.92792 | -50.90149 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 87fdb4e5-f0e2-3272-8cdd-ac899cd62f3b | -7.31046 | -44.17157 | 2026-09-22 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd6af832-1b7a-3e71-98b1-f0aa71d6fd7b | -9.97718 | -50.25822 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27e75724-7c2f-39b0-bd3a-587653366d8b | -5.74855 | -45.08847 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 21c86d68-3cee-3602-a04f-17e89c36b157 | -3.403 | -59.52745 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e72eb6cd-58f3-3c43-b09d-fecb03e914cf | -3.00779 | -54.18311 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec445f59-29c2-384f-88a5-b58486b9fd40 | -6.12245 | -57.75894 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 08a935fd-9161-3f8e-a620-24fbb31e78d4 | -6.63287 | -59.9331 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fed2102e-c232-383c-9911-0ea68eca1d34 | -5.80554 | -53.52365 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c32c3562-3521-338e-8a59-47a33dafdab3 | -4.83412 | -45.99061 | 2026-09-22 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a0c16c7-f6b5-37ef-8166-6c8766b699e8 | -3.45562 | -50.59688 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dd1e15e-78f0-37da-80bd-bb89edb1f8aa | -3.39773 | -59.5266 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8412807c-a222-36c8-b42b-acaedf134e9d | -3.11752 | -60.68357 | 2026-09-22 04:46:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d74ea68-6689-3a01-867c-56bc0b6a6622 | -8.1409 | -46.82724 | 2026-09-22 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db2bd1bb-92b7-3497-bf26-65d741a7bd76 | -7.32923 | -55.6059 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 03543661-9f31-3912-a6b1-11121f1524f3 | -3.60979 | -60.57141 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c598d33-cf77-35c6-9b8d-9f574a8df46f | -2.5658 | -54.74189 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb8a4d8f-2b68-3aff-82dc-f6f23f2510e3 | -6.74346 | -59.41693 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fe04a22-6dac-3798-b28a-6f6fcde388f8 | -3.04465 | -61.26271 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ab91006-b29a-3fa1-b507-e880f7960c96 | -6.64581 | -59.91954 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 9d44b33a-93a0-3749-8865-52a96ab25b3d | -6.94003 | -42.91243 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce5282a6-da95-31be-a5fa-b133a11ab426 | -8.6029 | -54.60766 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5710032a-f3b7-3b2b-8d8a-f0a5a496d6de | -8.27716 | -49.4925 | 2026-09-22 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3abe2d5-cc2b-3841-b256-6ecc1af7e7bb | -2.88271 | -54.08049 | 2026-09-22 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b0094ba-580b-3ae1-9a99-a9949dfbd3a1 | -7.58853 | -57.67601 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a204c67d-0afe-3543-b6ce-485bf34f6c82 | -3.89508 | -49.06086 | 2026-09-22 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73eaad7f-cb93-3cb7-8a2a-8083b5c018dc | -7.54418 | -47.32507 | 2026-09-22 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0993713d-fd56-3de2-b27e-58819a8caf89 | -10.84909 | -50.14624 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c752077e-d3b0-35a9-a0cf-84ef4db68f40 | -10.3494 | -50.20691 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 699a33ff-6d7b-39f8-84ed-effd4be68a63 | -6.16133 | -49.88319 | 2026-09-22 04:46:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 91867365-cf83-3052-bdc3-80c4dc410fd2 | -5.89238 | -52.04465 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56bc8b26-7b0c-37e7-9b72-ec84760dcdf6 | -3.22823 | -53.95699 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 16f86934-32fc-3c2b-ba07-425620ecb231 | -10.46587 | -51.31153 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f3f11fa-ef84-3581-b341-39fc7c32def7 | -3.23188 | -53.95758 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9262a666-1abc-36c3-88a3-faf75c2bf0fc | -6.35825 | -58.28237 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a48123e0-7026-3c20-979e-58c1c5fe9fc0 | -8.14766 | -54.81567 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 401b8f1b-7f24-32b7-a847-34330f45828b | -4.10416 | -52.11893 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6efb4896-a42c-34b2-b658-92912d4094a8 | -6.07212 | -55.61737 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b0be6f9-29e2-3910-8195-e2798d533560 | -5.72717 | -53.45592 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02b5ba8a-ab52-357b-bfe6-a26367a6d866 | -8.60955 | -54.63378 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c65d5928-c70d-3a41-8719-7e20217dd7ff | -5.98237 | -57.78191 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f2499a8-3d73-375c-a0fa-592ddc8c8eba | -5.93908 | -59.97684 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5494d367-5759-3742-bd23-0879543d7d77 | -6.7831 | -48.67486 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42bd33f8-1bd7-3f1c-b255-194b5d8f7201 | -6.38107 | -55.27327 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ec62626-de8a-3c5a-b74c-191a4a1b43a5 | -5.93853 | -59.97998 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97acfc9b-0a98-346b-8b4e-1918fb79c9e2 | -6.06895 | -57.87096 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e4b28afc-018a-3a89-a34b-0f59fec26437 | -7.35452 | -45.34091 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e1b9baf-eea4-33ed-a5d0-4103287b1a28 | -6.13271 | -59.94693 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8658ce9f-e239-37cc-9628-cb8270b8508d | -3.50533 | -55.48875 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e183e3c-eb0d-3326-b529-6a82b1323d00 | -6.74841 | -59.41777 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 197fbfa5-e36d-3003-a02b-3df4879c9960 | -5.88184 | -52.04664 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 379295ab-d548-38bb-b75d-505473590b53 | -6.66978 | -47.37835 | 2026-09-22 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0db1e1c1-d7b1-310f-a8e9-5f2de5cfd77e | -7.55859 | -55.0184 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a001eb12-cb6c-31b2-bde4-4f34c042c9be | -7.13663 | -48.4407 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a1f7174-8464-3cd0-a059-9562bb83e532 | -7.90447 | -49.01343 | 2026-09-22 04:46:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aa22cf7-8ed4-33f0-b041-12ecbe8d4c3e | -8.91796 | -50.89984 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 915e6f6f-38ce-3317-a6a8-9a6167d98798 | -3.9243 | -56.04945 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70fca33c-19c0-30f7-a220-29710b43acf4 | -4.48321 | -55.4866 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1276852e-7c76-33ef-a680-bb80750dfd64 | -3.48776 | -59.56846 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53679586-8082-3848-9a54-d1efe0483f28 | -5.82964 | -52.07456 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 141c51ed-1168-380e-b64b-f4b011b889e4 | -5.89404 | -52.09902 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 742cf2fb-3269-3c7c-9a8d-742f9c633694 | -5.80715 | -52.08908 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 109a5567-d6a4-31e6-b014-366b72994c95 | -6.0414 | -53.27467 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5641e3f3-3d94-3551-8507-c2b7f880092b | -5.76198 | -45.0865 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5c46bdad-249c-3f5a-894d-c4facbaf508f | -3.00832 | -59.36994 | 2026-09-22 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0e39349-27ad-38da-8bf9-24c25342a34d | -3.06547 | -61.28402 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d07b9fea-32c8-3950-a396-c2591865b46b | -4.56534 | -54.92752 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df219ca0-a937-33fe-a2ca-2162f29da050 | -6.38485 | -55.27391 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5bf2789b-67ef-37d6-bfc5-76ae13677368 | -11.38894 | -46.78912 | 2026-09-22 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bed4af8-7f5a-3792-a57c-59171dd21ee0 | -6.10419 | -56.10761 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff82e56e-7b85-35bb-a891-a41d6aaa47de | -5.60972 | -44.84182 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README61.md)
