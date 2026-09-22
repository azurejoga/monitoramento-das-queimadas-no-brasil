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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d45e08c-2194-3b6a-b105-017764fedbd0 | -7.58146 | -57.68585 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bf67753-233b-3e63-a762-7da1d33931e1 | -4.56557 | -55.75228 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27337399-6fbc-3e1e-a7ea-6f9989a8ecc9 | -3.39137 | -61.29304 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d941243-5181-324e-829a-c6da122c6d19 | -5.89769 | -52.09174 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 139aa918-f671-3820-af26-60df014c22ec | -13.51722 | -51.51834 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 8d2e55d0-2b31-3659-8260-1146a146f476 | -7.24356 | -55.60762 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3d87d8c-9bf8-3ffc-ba45-2bd782c2516b | -2.73036 | -54.90344 | 2026-09-22 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a92726b-2d33-381d-aeda-660572103c4d | -7.27331 | -57.58328 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbbf9a8c-f17e-39ab-a0f1-5676c9f0f2f3 | -13.87609 | -48.5611 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9cf4feff-998e-35c1-8def-65fb24dd7a18 | -6.46695 | -59.97196 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe4106cd-3d19-3c5b-885a-4bd56be82acd | -5.20241 | -56.07233 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b02892c-dd3b-3c1f-a3a0-43bf6f307af9 | -1.24601 | -54.55431 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e694336d-5744-3f5a-9155-7d7305d40d3f | -6.24803 | -57.78015 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c937c13-4efd-310c-a867-a3dc56aeeaf3 | -7.32835 | -55.59716 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c16eb830-85cf-33b5-9ec5-64a6cfcc1856 | -11.75553 | -50.81706 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa669f61-6439-329d-ab0e-6afc01456aa9 | -3.69167 | -60.57733 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d378f9ba-b963-3407-b6d4-483dc47e667c | -5.74916 | -45.09285 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 25091de7-440b-3576-8fc4-163cd318f457 | -11.31841 | -54.05 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2281694e-3b5c-3b47-a232-5ac332369ea7 | -6.63265 | -59.9291 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 770ec27f-1247-37a3-92a8-825b198cabba | -3.45568 | -50.60165 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9220f039-ec66-35e6-9c5a-12a0e6a48ef4 | -6.74695 | -59.42053 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9426c6cb-915d-371a-97d6-8a9b00f671e9 | -3.85283 | -61.18468 | 2026-09-22 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b13be59-6b95-3df2-853c-47d63e1b71cf | -6.65059 | -47.4375 | 2026-09-22 05:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6686a2a-b8ff-3a23-8506-88937e74c748 | -6.83467 | -55.53794 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9df8c6f-ea65-30cf-8e36-17b3c0169049 | -12.8398 | -50.98787 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18630590-fd26-3aee-bfcb-bf56292a25b6 | -3.16257 | -50.82179 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fc0bde9-4aba-381f-9a04-07a87de06eda | -3.52652 | -58.65919 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 264e55fa-7a7e-3613-b3f7-83416b875782 | -6.57354 | -44.15135 | 2026-09-22 05:23:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb08d9de-9c27-3aa1-b0d9-f3df85e5faa6 | -3.45131 | -50.60106 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dda5681d-7b0b-394b-bbf3-5f075153b46d | -9.61866 | -43.9474 | 2026-09-22 05:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1ec6f078-15c6-3db2-80ea-9eacdf0e6e8a | -3.58299 | -59.06733 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5fbfef2-6407-33e0-8ac5-ee11400dc052 | -3.7741 | -51.35563 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ebcd158-d732-31a4-83c0-1264929b18ba | -4.56072 | -54.93078 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be114d33-1da9-354e-9ae7-ef5ce40c5e00 | -6.34874 | -59.96508 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6ade944-a889-34df-9fb2-aafd95185bec | -5.80746 | -52.08878 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39d29070-6cf0-37a1-81ab-598fbc0d77aa | -3.06081 | -61.28553 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a872522-3e99-339d-b5e2-2f84017342f7 | -7.58091 | -57.68933 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c61cd80e-df04-37cc-b843-832b4336c22c | -6.1172 | -57.74863 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd278cb5-1619-37fc-b331-20b157df1e65 | -4.55098 | -54.90225 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 208ef95d-b2ac-36b7-b56f-4e2661f6ec84 | -13.32823 | -51.2906 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c42c43b3-25ba-36e7-b1d9-9cd2503327aa | -6.29892 | -59.94187 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2269208-73eb-35a7-ba65-dac09729870f | -7.5859 | -57.67942 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1b69e4a-4076-3f31-80db-ac6752f95b82 | -11.31912 | -54.04509 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f5f64a36-8f0d-30ba-897e-cda744d1ed0c | -6.3808 | -55.27469 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb97a7a6-a96f-33c3-9302-4e08fd3b0926 | -6.43138 | -55.62196 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abf8c096-9550-3828-b3f9-c8d16050d555 | -7.58867 | -57.68343 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 34437d5f-b71c-31e9-bff9-67bdef6e2d9b | -5.76789 | -57.4542 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf043dd2-d5c7-347a-a2f0-48fb32ad4b67 | -6.20861 | -57.72746 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6620d1df-59aa-32a0-b4d7-e9a8d2142b15 | -7.587 | -57.67246 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| af75c45d-2f02-3716-ad2b-fd6a1e709b12 | -3.71945 | -60.57264 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e93e2d2b-1326-3aef-a590-954e9cec6e94 | -6.13778 | -59.95305 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2526cee2-7ef7-375a-80f0-46aca1ea1b7c | -4.50779 | -56.07644 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2e688a0-554a-3165-a422-0d7988bbe67a | -3.17256 | -51.3501 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93b1ac80-458c-3aaf-9e9c-de90d4b1dda3 | -1.46772 | -60.2697 | 2026-09-22 05:23:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 571f0bbe-c8be-3422-a824-333b7e3f2687 | -5.88332 | -53.63821 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97d6b5e9-37dd-31cd-ba04-25d3cf4b0129 | -1.74687 | -47.13655 | 2026-09-22 05:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2588ab0a-2b9e-3fa1-b6d2-121f6ededc08 | -6.15249 | -57.84355 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9495d06a-d870-3791-837f-5a7bc44eb44b | -5.84379 | -49.78387 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6954be9-51f2-3cf2-a3cc-b5cbe45e4728 | -2.85961 | -57.80946 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| edef508a-4873-377f-b81f-3cfb44610629 | -4.41106 | -55.24503 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f855aded-eac6-3109-9f10-1671b858dec5 | -5.85285 | -49.78928 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffc155e9-985f-33e6-84a1-a1d1e01315e1 | -5.92385 | -57.68891 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d983155-f79a-3982-9c34-b193731c821d | -10.58607 | -57.48679 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c06d5389-83dd-363f-9ab2-18ef39e75670 | -2.94887 | -51.03778 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efba4e05-4a8d-3cf4-8ac4-26e51684e79e | -8.83258 | -50.49121 | 2026-09-22 05:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 43524a95-525c-3a2a-9bdb-525be8660b66 | -2.54995 | -49.10058 | 2026-09-22 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dff04448-80ac-3dc2-be13-5f5a271ffb19 | -7.61489 | -55.35836 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7298edb3-d5a7-34e7-b1da-35cfdf3d4fbb | -6.13136 | -59.94794 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e40bd112-625c-3cff-89db-958abdaf4c25 | -15.35631 | -48.10397 | 2026-09-22 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6474ac7b-d1be-353f-91b7-a4fde0a52fa6 | -2.99971 | -60.79587 | 2026-09-22 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8739bf19-fd19-30f9-895d-0fbd370693cd | -2.26967 | -56.98252 | 2026-09-22 05:23:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4da35823-0a7c-34c3-ba85-831014c73520 | -6.08944 | -56.47024 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2796a96-8499-33fe-94ee-691602a19f0d | -11.31523 | -54.04449 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a4139315-17c7-3c2a-b05e-cdb603cc9ac4 | -4.96219 | -56.26602 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a3e2363-8211-3d2d-b556-96b56e13c459 | -1.45901 | -54.24311 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8dc17d8-9cec-3d37-903e-adef0622fc24 | -6.43805 | -59.97128 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5569be3b-2937-36ce-8246-eebb6637bc7c | -1.74453 | -47.13195 | 2026-09-22 05:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75861550-2c82-3e66-9aa5-e89a569e2fc9 | -11.03445 | -54.14314 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 564dd8ce-dec8-352e-a292-4ed1acdee0ca | -9.12188 | -65.86665 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f828424f-3772-385d-b98c-2011016fe64e | -6.46435 | -59.9877 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 644d04f9-4e8d-34de-bc0b-4a57633ee27b | -3.92421 | -56.05033 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e75670e-c3da-3688-8751-09aad2a4fe5d | -2.94361 | -51.97066 | 2026-09-22 05:23:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5db6ed64-e579-3f68-813b-53191b018d6e | -5.98381 | -55.69663 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0ae2dce-84a8-3e8a-99e9-9ec4b1b33299 | -3.54296 | -58.68855 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d92a7b17-7080-33c6-be27-c0b878a58711 | -1.74402 | -47.13535 | 2026-09-22 05:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 338375b6-072c-369c-928f-fd3d35b6842c | -6.6936 | -55.37085 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d237df7c-9c20-3703-a86f-09ae382fd708 | -6.45636 | -59.97019 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 759871e9-8b52-3c43-83ef-dec3dbff4dc8 | -3.68644 | -60.58574 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23fed7e8-05d6-3ba5-9148-f7b978e3ae05 | -6.74596 | -59.41993 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7a58940-a965-3430-82a4-7128de59079e | -3.3677 | -61.28918 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dea0731c-ed5a-3cfa-a666-ad1319b66788 | -6.69164 | -60.01095 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 349abf51-71ae-3807-ba92-46b2d05e1921 | -11.2571 | -54.14612 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ccbcaf1-c9b4-3b06-bf25-4ac0473dc86b | -3.14664 | -60.65477 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daeaa08d-7fdf-39fa-8725-77a6199d10ce | -6.35701 | -58.2832 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4dfd8d0-0110-3b83-a1d5-f35adfa1318d | -5.87655 | -53.63266 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 750b00e5-f201-3955-a86b-287d76f4ee70 | -11.33274 | -51.36976 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd2f2d4d-3177-3aee-8ff8-78941555930d | -12.93427 | -51.04039 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd736843-eeec-35d7-b4d2-c3f19fbf0dcb | -6.7471 | -55.09384 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95477bb4-f1fd-3426-a1ba-07c5eb1f47b6 | -3.5074 | -55.4907 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48ecc9cf-79a8-39d8-8c2c-cd0de7c9aa55 | -11.32444 | -54.03583 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README89.md)
