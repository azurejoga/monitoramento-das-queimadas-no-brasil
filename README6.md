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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09cfda65-fab6-32d2-a14d-774449eb218a | -7.5289 | -61.3825 | 2026-08-26 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 197.5 |
| 30a2530d-91d3-32cc-ab3c-4537720f05c5 | -6.641 | -58.4987 | 2026-08-26 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 59cd90b4-0190-334a-af81-1e15274b40fd | -13.2263 | -51.4826 | 2026-08-26 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c7f6da7c-8cab-3272-80f1-3e783eec91b0 | -7.767 | -44.7543 | 2026-08-26 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 287462cf-32e5-3887-a382-f8083f055ac8 | 2.58 | -60.6973 | 2026-08-26 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 477312b4-6468-3509-8e31-608fe7d2b292 | -13.2469 | -51.3949 | 2026-08-26 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 6c3cbb10-0efb-3bad-b4d9-a07636671b95 | -13.2465 | -51.4162 | 2026-08-26 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| aa641d3f-426e-3e52-8d42-275364fd0589 | -13.2277 | -51.3973 | 2026-08-26 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 84a9c442-1205-3dd2-9dc9-ca344ba2ef85 | -6.6595 | -58.498 | 2026-08-26 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 09b1ce34-d00b-3e19-89a0-d6e95bf40754 | -6.2676 | -53.3768 | 2026-08-26 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 647d17e2-6205-335c-b151-8306e1bc1dfe | -13.2266 | -51.4613 | 2026-08-26 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| eea9d722-aca7-3936-8bca-b6b7c41b14d4 | -7.7481 | -44.7561 | 2026-08-26 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 76c3edd7-9678-38c7-a8f7-9be22df2ec74 | -7.0612 | -59.2358 | 2026-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 0f3adc2a-ec89-3c7f-8060-98875fb4a8cf | -7.5288 | -61.4015 | 2026-08-26 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 409cb724-1551-3d98-ad3a-02c19f85076e | -9.6024 | -55.1078 | 2026-08-26 01:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b1926f8d-239f-358c-b678-3d7264751696 | -7.0797 | -59.2157 | 2026-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 206.8 |
| fc0a2b59-0b17-3239-8dad-fff14c56d92b | -10.7596 | -54.0384 | 2026-08-26 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 257.5 |
| fc4c849d-428d-3a11-9294-5a2fe63590b9 | -10.3727 | -45.0537 | 2026-08-26 01:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 9c244411-79c8-316b-bcb2-91cfedb37328 | -9.0304 | -50.7817 | 2026-08-26 01:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 7f58693e-0e20-396d-8279-f390848e9f1c | -6.6409 | -58.5181 | 2026-08-26 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 218cac94-64d7-3b31-bb00-35b48538127d | -7.5104 | -61.3832 | 2026-08-26 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 47f615f6-ec4f-3445-b384-2a6922a9532e | -6.6226 | -58.4995 | 2026-08-26 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| bed5f636-08e2-34d5-b4b5-3806d3b19a27 | -10.7598 | -54.0179 | 2026-08-26 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 174.3 |
| 44378d7f-c44a-3bbe-9e72-32c47e103a11 | -7.0613 | -59.2165 | 2026-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 199.8 |
| 8c98fea1-e38c-384e-89ee-95136bf5d24b | 2.5983 | -60.697 | 2026-08-26 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 44598584-9e4d-37b0-a26d-09552b536630 | -4.8002 | -43.1709 | 2026-08-26 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e0e326ba-5c2c-3786-9549-3515088eaeed | -7.5105 | -61.3642 | 2026-08-26 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 71f326e1-48ca-34a4-8da9-6e21e4b68e8a | -13.2469 | -51.3949 | 2026-08-26 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 88e59929-349c-3912-9052-fae210a5585b | -9.6024 | -55.1078 | 2026-08-26 02:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5a165ef0-5746-3e09-b917-62135f8000f5 | -7.0612 | -59.2358 | 2026-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.2 |
| e09fcbe0-5111-3c4e-b1c5-a1a29ba4e00d | -10.7784 | -54.0368 | 2026-08-26 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.6 |
| b816f5a8-97d3-3ec7-9556-b787aac3e55c | -15.8797 | -48.3379 | 2026-08-26 02:00:00 | GOES-19 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 736e6f2e-9f3b-3521-9376-15e14d3d050d | -11.0034 | -51.1847 | 2026-08-26 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 3885ec81-bdeb-31d2-b2d5-c0512a1fe7af | -9.0304 | -50.7817 | 2026-08-26 02:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9273f343-3f1f-31b5-8595-bc6b593d48ec | -6.2491 | -53.3778 | 2026-08-26 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 7d218a7c-d7fa-30f9-a584-e5a4dd637262 | -7.5104 | -61.3832 | 2026-08-26 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 11cdc6b6-f693-373d-9b09-75e6a10c9fce | -10.7598 | -54.0179 | 2026-08-26 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 23442990-c789-32d1-841f-ad38b2ed63cb | -13.2277 | -51.3973 | 2026-08-26 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.6 |
| b6df3512-3992-37f9-8f9b-e2eae60fb229 | -13.228 | -51.3759 | 2026-08-26 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ea818b2e-35ff-3309-89be-8a5d065555ea | -7.0797 | -59.2157 | 2026-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 189.9 |
| cd31dca4-e56a-316f-aa6f-47a09d12fd5c | -7.0242 | -59.2374 | 2026-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 3f22349f-4c4a-3111-ae80-f6a385860807 | -10.3918 | -45.0512 | 2026-08-26 02:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5d4f683f-5d3c-343a-8eab-f28445b6bef1 | -6.6226 | -58.4995 | 2026-08-26 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 09ed39ab-14d5-39f9-8ddc-fccbf957a6dd | -4.8002 | -43.1709 | 2026-08-26 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 40b9484a-0270-3af9-93b2-fdae60657e27 | -10.7787 | -54.0163 | 2026-08-26 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2be40e9e-ff9f-3593-8658-7c5f2f4025ea | -10.7596 | -54.0384 | 2026-08-26 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 1d04b91c-dd60-3659-b1d5-c41cf0d1e720 | -13.2465 | -51.4162 | 2026-08-26 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 61be0786-3704-3a36-8374-d3efe4450fe3 | -6.2677 | -53.3565 | 2026-08-26 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a2a51022-3168-3e4b-8430-3ce406c4e7a6 | -6.641 | -58.4987 | 2026-08-26 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 8655a24e-2f35-3a4b-8c3a-86c49147571a | -6.6409 | -58.5181 | 2026-08-26 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 0259f619-4b58-313c-9669-8a0ae0c7e810 | -10.3723 | -45.0767 | 2026-08-26 02:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 093535d5-d932-31b3-8d0e-a457ff77bc02 | -6.6594 | -58.5174 | 2026-08-26 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 2597aa4c-9c01-376b-bc2e-dbf15e24223f | -6.2861 | -53.3758 | 2026-08-26 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6dcc7864-5dd7-34bd-bfa0-1e7a5ea4b3c8 | -7.0243 | -59.2181 | 2026-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 118ae203-3217-3b3c-a62f-596dad68e4cd | -7.0796 | -59.2351 | 2026-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.6 |
| ebd17af2-79b6-347b-aaa6-92d7bc8c038c | -7.0613 | -59.2165 | 2026-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 82a521e9-7cbe-3e64-a745-6d58252a8ceb | -7.767 | -44.7543 | 2026-08-26 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ce55b767-67db-3b8c-acab-a7f2d31190c7 | -6.6595 | -58.498 | 2026-08-26 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| d4882b89-92b9-3b5a-a3ae-c35785415265 | -7.5289 | -61.3825 | 2026-08-26 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 3396736c-7e0e-38f7-ba84-335d6b174256 | 2.58 | -60.6973 | 2026-08-26 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a52594f6-1d9a-3fca-a6c0-b04ec39e683d | -10.3727 | -45.0537 | 2026-08-26 02:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| c75452a1-be52-348e-b192-239810f90f5d | -6.2676 | -53.3768 | 2026-08-26 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 890da052-40fd-3ac4-a2dd-f2a6e71ad307 | -10.3727 | -45.0537 | 2026-08-26 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 65f44a09-2563-38c8-96b3-03fa5d1c0f76 | -10.7784 | -54.0368 | 2026-08-26 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 26978565-c339-31b7-8d41-53669cfc57c1 | -7.0797 | -59.2157 | 2026-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 1431ead1-4577-3aad-a320-e88ceb342cb7 | -6.2676 | -53.3768 | 2026-08-26 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 6153f663-ce3d-3bb9-b324-17e94bdaf383 | -9.0304 | -50.7817 | 2026-08-26 02:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 02e14ec0-ddfb-3a52-bdf3-79532c8cfee0 | -6.6409 | -58.5181 | 2026-08-26 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 8419fe4a-4968-31a3-874a-3b41dbee6326 | -7.0242 | -59.2374 | 2026-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 9cc00e74-f48e-31eb-8d62-71c4e2402884 | -7.529 | -61.3635 | 2026-08-26 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 04296d37-9fcb-3dce-8780-f28e200a89c1 | -6.2677 | -53.3565 | 2026-08-26 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 92701ec2-2f84-3385-aba9-407c97a553bd | -9.6024 | -55.1078 | 2026-08-26 02:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 269d62dc-cf1a-3efa-8230-4f7066b64c72 | -7.0243 | -59.2181 | 2026-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5b169253-4846-3577-b2b8-3fba5785d886 | -7.767 | -44.7543 | 2026-08-26 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 55dcc6c5-17a1-38a0-a147-de021bb58583 | -7.0796 | -59.2351 | 2026-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 55c3b7fd-ae68-3fea-8d9d-e31a26b09ec3 | -7.0613 | -59.2165 | 2026-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 215.4 |
| c4a4c786-e438-326e-a5ae-2654f0e3a5c7 | -6.2491 | -53.3778 | 2026-08-26 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ddff7161-4b28-3274-8219-f8eb17f4bc8e | -7.5288 | -61.4015 | 2026-08-26 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| bc588572-8c2a-3d07-bbd1-d6e1469d8c8d | -10.7596 | -54.0384 | 2026-08-26 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 218.6 |
| 56f8b91d-cf46-3f74-8ff7-46b68b3b4f69 | 2.2333 | -60.7018 | 2026-08-26 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ee7e0053-99ae-322e-b976-d691ad7cd782 | -10.3723 | -45.0767 | 2026-08-26 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c70040cf-4a63-31b7-afa9-e4590f0d07ab | -6.6595 | -58.498 | 2026-08-26 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 024c3dbe-0430-39c1-9711-7caecbd37f56 | -6.641 | -58.4987 | 2026-08-26 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 157.7 |
| bd3baebd-0aac-3501-ad8f-4bfa8e8b16dd | -6.6226 | -58.4995 | 2026-08-26 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 082ae9c5-6b23-3b90-83c7-686deacbe9bc | -7.5289 | -61.3825 | 2026-08-26 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 205.3 |
| a4bbc4dc-c9c3-328c-a0ea-4599dea9c524 | -10.7598 | -54.0179 | 2026-08-26 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 181.3 |
| 1dd0aae3-1058-3c9d-bdcf-08fc2ecc8331 | -10.7787 | -54.0163 | 2026-08-26 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 02578f0d-a49c-3e7d-977d-c29b3f2eb597 | -7.5104 | -61.3832 | 2026-08-26 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 580bf412-a269-3011-b8c6-4760e0e00b72 | 2.5983 | -60.697 | 2026-08-26 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e29a8cd1-279b-3ecc-93e0-707e254d0820 | -7.0612 | -59.2358 | 2026-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 0747651d-f4ba-367a-a63d-6c4e8b5aacf4 | -9.0492 | -50.7801 | 2026-08-26 02:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 956d6651-ef65-3764-abd6-929924cb9c6d | -13.29 | -51.49 | 2026-08-26 02:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43814bcf-00ca-3b80-a29d-16de1476ed88 | -13.26 | -51.48 | 2026-08-26 02:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74f75122-6998-3ff4-bfb4-99b7e0947177 | -6.2677 | -53.3565 | 2026-08-26 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e262d462-9112-381b-914e-ce94bef8d724 | -9.6024 | -55.1078 | 2026-08-26 02:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| fc240479-1243-3eb3-8c36-3624fc603c6a | 1.4734 | -55.9839 | 2026-08-26 02:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 507d09f9-bb5e-3070-a764-a068034154e4 | -6.6409 | -58.5181 | 2026-08-26 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 45069b84-6b7c-36a3-9dcc-0038e4f9d16e | -7.767 | -44.7543 | 2026-08-26 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 66da9926-ced1-31fc-9f95-3c46d07a6892 | -10.3723 | -45.0767 | 2026-08-26 02:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 80b6d5cb-12ad-31ea-98e5-1f8b75f79e72 | 1.4917 | -55.964 | 2026-08-26 02:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |


[Clique aqui para ver as próximas entradas](README7.md)
