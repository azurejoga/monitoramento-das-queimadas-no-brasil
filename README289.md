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

## Dados Diários - Página 289

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2234be9e-120c-39f7-932d-03864b7bceaf | -6.02563 | -51.72795 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1051bcfa-70d2-3183-883d-d0dd6113c9e7 | -5.50896 | -42.85268 | 2026-10-08 16:20:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 17f4a9ab-8880-30fe-b3b7-2ca7353f41fb | -7.80836 | -44.59297 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 70967952-01e1-3a5e-8831-47efc44073e1 | -6.40801 | -37.78919 | 2026-10-08 16:20:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 74f44199-9ba9-36e6-b5e8-c7961488c9b7 | -5.99735 | -44.13305 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6f1fbcb3-5b37-39c4-9b9e-38c4e446ba85 | -1.37545 | -48.04284 | 2026-10-08 16:20:00 | NPP-375 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a655a69d-ab14-34ce-945f-fdae9e631db2 | -5.28018 | -42.73771 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| effbb6d7-bce1-372f-8af6-67eb1a2b8c08 | -3.79373 | -41.65826 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 66e34d4e-c35c-3fa9-8bb3-1651f88f2986 | -6.13587 | -47.94942 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac24f89e-b604-3f87-81b7-68f382c08b46 | -7.26868 | -45.34994 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b33f7cc-e9eb-3156-8fe8-c57e47a74707 | -5.49839 | -42.85268 | 2026-10-08 16:20:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 7829c1c0-b4ff-3d07-a03d-66285bff25a8 | -6.13804 | -47.94133 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 39f7fd3d-7f2f-3daa-8771-787620011f1f | -6.63459 | -44.89383 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 46ac4342-fe82-32f9-acc1-023f9c17593d | -6.90924 | -43.93335 | 2026-10-08 16:20:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1fc00fb7-0ee8-3b07-bf5a-e2ea64dc86a2 | -6.4067 | -44.9533 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| fc754bf2-afa0-3657-8d4e-47d32383bb69 | -7.04131 | -44.33624 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e6b20d67-3814-3308-8cda-a7a1930f243e | -6.46634 | -46.54133 | 2026-10-08 16:20:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3d5ed65b-dbb6-3474-8150-791a8fe47f69 | -3.08908 | -53.94153 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 4747ddf6-e78e-3bf7-900e-e5a4ba14bf44 | -6.19114 | -52.87264 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4438f97d-cdc6-3d6c-9183-2eed76fefc36 | -6.13652 | -51.76318 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 33e0b795-12c3-3070-b913-ec50e3029fb3 | -7.68746 | -44.74132 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 217caae3-6fc2-3b44-bca0-fc55d661dcda | -7.41196 | -43.74519 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2d984116-740c-3a40-bdd3-b13685531143 | -3.79317 | -41.65458 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 1745b76b-32d4-3a61-8036-245e173e4afc | -3.09616 | -53.94964 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 0864db48-dcb7-393b-a986-e3302a176357 | -5.93382 | -44.28428 | 2026-10-08 16:20:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bfa9745d-c671-37c9-b97d-94f8db1feb7c | -5.22289 | -36.75184 | 2026-10-08 16:20:00 | NPP-375 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 3899ad3f-7b8f-38fe-8db2-51e7ecf9c6b1 | -5.70384 | -41.72778 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 02032e61-53df-35ff-afd1-4ef90c9eb17c | -2.74067 | -54.11671 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 90ac027b-4e4b-3a42-acf9-9e9780418dd4 | -5.41887 | -45.86683 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| f2edc7b8-6586-3474-b41d-ab9b94d6a0ac | -6.19685 | -51.4383 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 85c0cff6-5d86-394f-9542-f0bd6a9ec07e | -5.618 | -43.05726 | 2026-10-08 16:20:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4a800c5e-22f4-34be-ac1d-14152cec069b | -5.28584 | -48.10505 | 2026-10-08 16:20:00 | NPP-375 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| f431f1e3-d055-34ba-98f9-9f4c5042210c | -3.09626 | -53.94025 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| b60af13e-1ae6-33c0-8be2-53bad5203c3c | -1.88318 | -53.97284 | 2026-10-08 16:20:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 41b4a3e9-bf26-3a8b-80df-e839e047f7a4 | -8.01834 | -47.1721 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 04394f8e-60b6-354f-90e2-1933b7ef992a | -6.33128 | -35.12767 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 781e0121-d6ff-3b5e-9b72-15c23452b727 | -6.14549 | -52.64441 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 6d6d6446-4edb-33a4-8f37-b6ca8efc4832 | -7.04997 | -44.33858 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 30fcb82e-a6fd-3227-adb3-089ccc52a792 | -4.17703 | -42.04752 | 2026-10-08 16:20:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 443c8ddf-3439-34f4-bbe0-4e3f86ed2b8a | -6.22531 | -44.97778 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 695760b1-97c9-328c-a613-02edd49d5dbb | -5.41468 | -45.86531 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 541f943b-5560-31a7-876c-081cb6d6deee | -6.37374 | -45.79374 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 95c4a6f5-7204-3b2e-a728-18e18c76dd56 | -7.40135 | -45.65125 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 46eef028-fd98-3bf1-b6e9-f3ae44e757d3 | -4.20629 | -41.75834 | 2026-10-08 16:20:00 | NPP-375 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 0ed96428-0fdf-3386-985d-3a623dfcff14 | -7.3842 | -46.233 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8b280c74-2f8c-39f2-aef0-77ed7a88ae56 | -4.36078 | -40.41299 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7767f6cd-d871-37d8-97ab-c84f7083c2df | -6.35577 | -42.91275 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 013c55fa-8a56-3960-b62e-49caea0cf02b | -6.46721 | -44.98436 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91f105a1-1ff1-3bbc-9007-67b31f4df134 | -6.45546 | -46.01596 | 2026-10-08 16:20:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a8d404e6-f6d6-3384-911f-c1961fb24f4a | -3.91637 | -40.73946 | 2026-10-08 16:20:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d1c69e86-8add-3c60-80a8-ddf79d609534 | -6.15506 | -39.4337 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 15e58b62-e405-38f2-bfa1-22aedb665c78 | -4.76496 | -49.12208 | 2026-10-08 16:20:00 | NPP-375 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c6a59711-ce93-32a3-b3a6-ac7cab27f897 | -5.7473 | -41.70958 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1cb46466-43d7-3f99-870d-9df36611a376 | -6.0507 | -42.5876 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| bc0064ce-cb17-3854-a404-b8406bf94199 | -3.0766 | -53.96671 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| d70fd658-e249-31ce-8e1e-37fad1756319 | -2.92327 | -46.72729 | 2026-10-08 16:20:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| bf1a2e2c-8610-334c-b5c0-16d2a99d5e22 | -6.15045 | -47.94067 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3d83e5dc-523f-3361-b270-832dbf25ba8a | -4.09124 | -44.11363 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 60a7a953-d998-374d-a3db-67426c75c893 | -8.21065 | -46.41771 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| c209296a-3c14-39d6-9b77-084a18879dd2 | -1.95748 | -54.05444 | 2026-10-08 16:20:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d87ebcae-9301-3dda-a043-d7175ef35f01 | -3.77038 | -44.34924 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 1980bdee-d693-3da6-95cd-80f9850ced67 | -4.63339 | -50.95579 | 2026-10-08 16:20:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 777895d3-b5cc-3b64-ab8f-5bbcecd188c3 | -4.93721 | -37.38297 | 2026-10-08 16:20:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 172287d1-98af-3cc3-8fe4-35404f16bde3 | -3.78138 | -45.27654 | 2026-10-08 16:20:00 | NPP-375 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e54bf114-ce54-39ab-af40-c93067c6adc1 | -6.22507 | -44.8546 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f61b52d5-1e75-3165-9f49-d6ab7f5fc419 | -6.72528 | -45.17435 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d44b54d-4730-3260-92e1-a5a2909252e1 | -6.21786 | -44.83952 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e82a0435-54db-3e08-b112-fa0828c66fdb | -8.20498 | -46.37605 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 78ecba79-73e4-3a8a-993e-8797a856ac00 | -5.74996 | -42.06237 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 61abe808-bc98-3e0d-b8f0-f56d98a11afb | -7.08989 | -43.08638 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| eda31c4e-6bbf-3dfb-930a-f2a52bb3e6b5 | -6.81426 | -38.5341 | 2026-10-08 16:20:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 25fd49ef-2171-3971-83ef-226805812394 | -2.98128 | -54.08488 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 0bd77dea-12a9-35e3-ad47-5f168a587b36 | -2.84552 | -54.12407 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f0a057cf-5565-32db-a617-d9a4f5b974aa | -6.46661 | -44.98452 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4c19c9cf-61ab-3014-808d-35233d03314b | -6.57764 | -53.03169 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| dcf8df92-162f-32f0-80f1-6759b7b8bda5 | -5.28218 | -47.91264 | 2026-10-08 16:20:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bfff81d5-0b6d-3f93-9345-adbe0084b0b2 | -5.74407 | -42.07131 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 44.3 |
| 5cf60588-6fd2-3f35-bb49-2b9019fb311a | -6.72472 | -45.17031 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| acf60f26-7e58-3f79-b48b-8f7a168c5dd5 | -5.09306 | -46.20753 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 868f38d9-c895-379d-ae89-3ed2ac283289 | -7.09866 | -41.74222 | 2026-10-08 16:20:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 61e66019-93bf-3a32-826b-0ccb015535ba | -3.73187 | -43.33572 | 2026-10-08 16:20:00 | NPP-375 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4a66a9d1-0f8d-3677-bd0c-df46dd7ef9b0 | -6.24058 | -43.86031 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8285d3df-c820-3dc4-a8ae-50629b490f7a | -3.89827 | -44.13335 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 80aa1b56-8bd4-3ee7-b99d-ced762b2f681 | -3.26203 | -54.04515 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7a5ff5c7-5c4f-3743-9529-5e2be5103328 | -6.13502 | -47.94319 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c4f1456f-444a-3971-9dab-8973250cf6a4 | -3.19423 | -43.37494 | 2026-10-08 16:20:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 78c84d1e-2cd4-3086-a629-0a95ee7a552a | -7.0491 | -45.44278 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 72bf90a9-a9ac-316e-b62d-a20066250b68 | -4.85311 | -44.08684 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 387ef30c-cf01-36c5-85df-07abdf606566 | -6.97645 | -45.12193 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 35c58dda-12bc-36d4-9759-e4e448b441bd | -7.26465 | -44.21897 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f8586ab8-42d1-36d0-be79-918366fe1999 | -6.851 | -41.74561 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 8c57a8ee-6a01-300e-91ea-9e2f3109a553 | -6.56474 | -44.38448 | 2026-10-08 16:20:00 | NPP-375 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 999fa004-ac65-3d09-b7f3-d170b44d5908 | -6.33588 | -35.1318 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ee86a849-62cd-368b-a6a6-9eee6cc2eba9 | -7.94675 | -47.62539 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e87f7257-2471-3246-a2c4-3c8482b8df0c | -3.30061 | -39.27533 | 2026-10-08 16:20:00 | NPP-375 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9ece63b1-a479-349f-b05a-82005edb2473 | -3.50707 | -43.83424 | 2026-10-08 16:20:00 | NPP-375 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6e87ae44-3405-342e-bc60-28d4593a85ea | -3.28841 | -42.28839 | 2026-10-08 16:20:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b429cea8-bd69-3992-897b-964f29d08ff7 | -5.0969 | -37.50641 | 2026-10-08 16:20:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 10.5 |
| a55db37d-ebd0-39af-8cc0-2f21528413ca | -7.46168 | -42.83489 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 58ddb59f-ac16-32a5-91bb-dfeb44340b94 | -6.85276 | -39.46494 | 2026-10-08 16:20:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 24.3 |


[Clique aqui para ver as próximas entradas](README290.md)
