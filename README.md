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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d9d8120-d3a7-35e5-85e1-08662a0466ab | -4.5684 | -44.2036 | 2025-08-03 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 50602b7b-c9c7-3672-ac49-b72513ceb1cd | -6.656 | -59.0981 | 2025-08-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 79bcb1b7-e051-34dd-a2d3-bb50e7c8e57d | -8.0324 | -43.1022 | 2025-08-03 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| a18b57ef-bf96-3bf1-861a-e7ad967ecb13 | -18.8407 | -46.4417 | 2025-08-03 00:00:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d83138bf-d743-39cb-ac21-31da91d6092e | -6.633 | -59.9457 | 2025-08-03 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 8b1adb0c-c1d4-3135-86ee-27c0fa15d3e5 | -6.6145 | -59.9464 | 2025-08-03 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a1c53937-ad5f-387f-a1c2-367c3774fe78 | -4.3196 | -48.1125 | 2025-08-03 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 5ef2cda6-0ba7-3e4a-a693-e0531f4151c9 | -6.6742 | -59.1553 | 2025-08-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a6c282da-239a-3e8c-8fe7-1174219264f1 | -6.6559 | -59.1174 | 2025-08-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 87313754-0785-3573-9fce-8d9b803ca266 | -12.0337 | -44.0259 | 2025-08-03 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 1f31be47-77a1-3b0b-9074-c0feab1fa7c1 | -6.6375 | -59.1181 | 2025-08-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 20964297-d3e1-35a6-8ba2-86f6704f2119 | -22.0297 | -47.5605 | 2025-08-03 00:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8c158699-2941-3db2-ab6d-8f420c3f9008 | -21.4603 | -55.1063 | 2025-08-03 00:00:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 289ff240-64f4-36bf-b91b-c5ed0676b789 | -9.3989 | -45.4928 | 2025-08-03 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 93302ed7-ac56-3946-962b-dd775ccecd0e | -7.0208 | -59.8346 | 2025-08-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 44930e1a-9238-3c6e-96fa-c4602ebed04c | -6.6741 | -59.1746 | 2025-08-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| f724b297-8e83-3404-8419-83826fb84113 | -7.0207 | -59.8538 | 2025-08-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 44ece735-5ab8-3959-ab88-637a20e05705 | -6.6376 | -59.0988 | 2025-08-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 003fe7c8-aa27-397c-a535-6c643574f12c | -6.6144 | -59.9656 | 2025-08-03 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 985c7118-6057-3bc2-97dd-6332583e6f2c | -7.0391 | -59.8531 | 2025-08-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 07e0b032-b79d-382a-96df-1609b44c051e | -4.3197 | -48.0908 | 2025-08-03 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 1f659d74-402d-3574-bcdf-792448114f87 | -6.6329 | -59.9649 | 2025-08-03 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 880c1312-ed51-35a2-a887-510e023a3f07 | -21.26433 | -48.40126 | 2025-08-03 00:05:00 | TERRA_M-M | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 61.9 |
| a33652bb-8287-370e-aed8-d352bf97fb96 | -21.26152 | -48.36517 | 2025-08-03 00:05:00 | TERRA_M-M | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 75.5 |
| e1b8fb0e-8eec-3c1d-88e6-a5e9d4f3fd33 | -18.00514 | -42.41125 | 2025-08-03 00:05:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 68cb8cd7-608f-3361-8fca-6fe8300bb06d | -16.83059 | -42.8766 | 2025-08-03 00:05:00 | TERRA_M-M | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 80da0b68-b38e-3d1a-9549-6a7f5f9246d9 | -22.02906 | -47.59175 | 2025-08-03 00:05:00 | TERRA_M-M | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 24a8cd9b-a5a1-3197-8ad4-9c7d2b462501 | -18.83846 | -46.45391 | 2025-08-03 00:05:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 254ef842-3a08-317c-9e61-1a1e134acaab | -22.02621 | -47.55942 | 2025-08-03 00:05:00 | TERRA_M-M | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 371c28c0-d503-30e7-bd74-dd6b29e4a68b | -20.15181 | -41.64551 | 2025-08-03 00:05:00 | TERRA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 0123dd8b-4caf-314e-ab98-abaabb265baf | -18.84447 | -46.46017 | 2025-08-03 00:05:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 3aab1ed8-591c-3400-b621-91c29c6821a8 | -21.26995 | -48.36944 | 2025-08-03 00:05:00 | TERRA_M-M | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 77.8 |
| eb15b69d-254e-360e-8888-9ea9e0644708 | -22.02501 | -47.58548 | 2025-08-03 00:05:00 | TERRA_M-M | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 25fed25e-a227-3854-a9e0-fa77d7b130ba | -18.84201 | -46.4366 | 2025-08-03 00:05:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 1a53ec92-7ce0-3b13-9c27-5dd6731cfa49 | -12.65722 | -44.52465 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| f21c3a64-bb67-3721-94d2-dc3408b7d8ce | -12.01949 | -44.81624 | 2025-08-03 00:07:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f57a62da-da6e-3b0b-b529-a6a0f1d7a26f | -12.44618 | -44.86104 | 2025-08-03 00:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a6af578a-eabe-367c-8db8-dde67624d911 | -12.02115 | -44.82991 | 2025-08-03 00:07:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e74bd07a-6acc-378e-8627-92524cf3013c | -11.94487 | -44.95543 | 2025-08-03 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ed95cd15-8ec9-32f3-be07-0f63b1fa3d0c | -12.66453 | -44.49671 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a3b6b507-7259-3d78-8476-b27cb2549636 | -12.62213 | -44.50229 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 1233b558-c8ef-36d6-9f19-f6f280ad496a | -12.65392 | -44.49807 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 9ae177f9-07df-3d12-bc3e-dbc114536f5a | -12.03315 | -44.01571 | 2025-08-03 00:07:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 110e5b94-072e-37f9-8c1e-d44be1b67a4c | -12.64496 | -44.51274 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| d16d6229-0719-36a1-ae17-1ba3dee544d8 | -14.16306 | -45.43686 | 2025-08-03 00:07:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 68c944f0-fc45-3ba5-9ebb-be81bb1e9210 | -12.67346 | -44.48209 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| fbe31e18-10bd-3eb6-b8df-9f81197ec43e | -11.80266 | -44.92968 | 2025-08-03 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 66294696-3525-389a-80b4-a8765931c1f0 | -12.66784 | -44.52325 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9f98641e-708b-371b-b9b8-a6345b3dc2ac | -12.65557 | -44.51134 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| f7a376fa-bfec-3f41-b801-e98cf0692841 | -11.94232 | -44.96238 | 2025-08-03 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 56212333-ee81-3308-a1f1-f3bdc799a766 | -12.42438 | -43.48421 | 2025-08-03 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2adb30d3-12d2-3736-8a30-86dcb25ccd87 | -11.93581 | -44.97183 | 2025-08-03 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| beba5611-30be-3d6d-ac2f-630de244c0ef | -10.34424 | -44.90713 | 2025-08-03 00:07:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 3f23b67f-4655-3b7a-b6a5-bddbb2e3c32b | -12.64332 | -44.49946 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 6f9d8e25-41ab-33db-9e4a-cb2258b2d9bb | -14.13779 | -45.42332 | 2025-08-03 00:07:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| bcd0bef9-8381-3636-800f-ac6394d2e9ca | -12.65228 | -44.48486 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 004b3a60-9f4a-3303-a68c-60ea92c363a2 | -11.04512 | -49.54618 | 2025-08-03 00:07:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 34dd85e7-7295-384f-bb93-428632c6858e | -11.94057 | -44.9487 | 2025-08-03 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4e1fde74-f0df-3d07-a103-0b3d4a4999e1 | -13.68308 | -41.37187 | 2025-08-03 00:07:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9c0c36cf-28fd-315f-8059-ec7ccb611853 | -9.55653 | -47.88283 | 2025-08-03 00:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c6a2c978-fd73-3ba0-aaa8-fdd9eb5d6d4a | -13.68184 | -41.3625 | 2025-08-03 00:07:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| fb287830-49ab-38e3-a51a-ffb8c93aaa99 | -12.64169 | -44.48624 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| ed2fe5fe-90f3-36af-8590-897eba183c9c | -12.66287 | -44.48347 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 7c9da853-0f23-3a2a-92a7-b83de833bd62 | -12.43534 | -44.86261 | 2025-08-03 00:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 84a546e7-0a37-34c6-a03b-801cdd60e541 | -13.67341 | -41.37 | 2025-08-03 00:07:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 234c57ea-5c0c-3633-b6ec-6f536df6cc49 | -11.04912 | -49.55301 | 2025-08-03 00:07:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| a40ce17a-7dc8-3353-8cb3-28a68545e802 | -11.81346 | -44.92828 | 2025-08-03 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bb9a9504-e674-309e-8165-4c68279167af | -12.63435 | -44.51415 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 3d1a6f16-dfbb-3d6f-8ef4-c924c1b0858f | -12.61582 | -44.49605 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8d13cef9-5dc1-3f5d-9c79-618d98a6a3c9 | -11.93404 | -44.95712 | 2025-08-03 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 00b2373c-1087-395b-93ce-43f0a0281d2d | -12.03192 | -44.82847 | 2025-08-03 00:07:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f6982a46-6082-3b6c-8e49-b71aedef6a56 | -12.03463 | -44.02749 | 2025-08-03 00:07:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 106d458c-c6a0-3156-a753-e026c11803ee | -12.63273 | -44.50087 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 22f84f5c-790c-36f0-8593-81828a153013 | -12.67513 | -44.49533 | 2025-08-03 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| ac17ac51-343a-34e4-99fc-9da726ac6374 | -7.7597 | -45.11132 | 2025-08-03 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dc02d58b-0ccd-32c9-8f41-34d67380d458 | -8.00753 | -43.21487 | 2025-08-03 00:09:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 08e9a5cd-dab1-30e3-9df8-c9853f6f49ae | -8.33557 | -46.91319 | 2025-08-03 00:09:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d32486bf-e0d9-3866-802d-5e8d46b9213e | -7.11381 | -43.47891 | 2025-08-03 00:09:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 32f49fa4-a4e0-3da6-8d14-9da23b189319 | -4.56216 | -44.19711 | 2025-08-03 00:09:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| ca24d7d6-b22f-38a7-9542-4b8ad2a6953e | -8.31887 | -42.86485 | 2025-08-03 00:09:00 | TERRA_M-M | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 54d5d93e-3023-38f1-9953-191ee4dabc1e | -7.97428 | -45.10773 | 2025-08-03 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 30aed8c5-930f-3ac4-8d0f-cf0eb7427b9b | -3.78745 | -40.9966 | 2025-08-03 00:09:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 0748b8bc-0f2d-3a2b-89e3-addb1ba18f72 | -8.03019 | -43.11683 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 09d7db51-aa83-3cfc-b3ab-241ba93bef3c | -2.28702 | -47.86786 | 2025-08-03 00:09:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c96fea96-02c7-34a2-9c8a-d52b40751c8e | -3.78876 | -41.00583 | 2025-08-03 00:09:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b346a089-3792-3a89-bc7a-9b6ffe6d509d | -8.01017 | -43.16512 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 835.1 |
| 905bd354-2441-31a1-9cd8-10b0ad922393 | -7.87931 | -45.53599 | 2025-08-03 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 790f629b-2799-3ca0-92ff-d527174a935b | -7.12194 | -44.07753 | 2025-08-03 00:09:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 69578b03-727b-38d1-b3b7-7d86a34e0401 | -8.0049 | -43.19541 | 2025-08-03 00:09:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| 0aeba0a3-8933-3b0e-99e5-fb9db55bf3fb | -7.35445 | -44.66342 | 2025-08-03 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 40e65321-8d52-3515-9e8c-99bccfaa51ba | -6.52536 | -42.80434 | 2025-08-03 00:09:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 62db785f-afae-38b6-b8cc-2f6026efded7 | -6.20273 | -43.75465 | 2025-08-03 00:09:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fcde50bb-4985-3d61-810c-00c4581b6d86 | -7.12439 | -43.48739 | 2025-08-03 00:09:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| d0f6720d-3325-3d85-b21f-959f9090fa58 | -7.56561 | -46.28198 | 2025-08-03 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 3f473606-94c5-32a1-8d53-5448790e3fbd | -4.76847 | -45.32965 | 2025-08-03 00:09:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7a53c1c0-7261-3dd6-b700-e3b60d660c20 | -8.02592 | -43.14324 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 796e341a-a1fc-3ba6-9754-7732b4abe160 | -8.01542 | -43.1349 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 2b55c660-8c0b-3288-9513-5acc2e2a340d | -4.31246 | -48.11998 | 2025-08-03 00:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 54dc8d23-73e2-36b4-92c1-72e1995a6b50 | -6.56499 | -43.36531 | 2025-08-03 00:09:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 98e285e8-6a37-31f2-93c2-829104fc81a6 | -7.96396 | -45.10918 | 2025-08-03 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |


[Clique aqui para ver as próximas entradas](README2.md)
