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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43148010-2181-3801-a980-b4b131f247d0 | -3.4003 | -61.2898 | 2026-09-21 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 164e796b-ce2d-3aa0-8a37-b1209a2fb49f | -3.1698 | -58.5859 | 2026-09-21 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| df01166e-fd68-3e8d-8e76-ec408afcc1d4 | -3.4186 | -61.2895 | 2026-09-21 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 39b1faac-fd14-382e-bb49-4ff198428b6e | -5.3645 | -56.0447 | 2026-09-21 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 9ead2933-0eae-3291-94d5-05ed4d9150e0 | -6.4485 | -59.9909 | 2026-09-21 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f1bc079b-c039-322b-b07f-301dec9aaece | -9.977 | -50.248 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0ba22321-533c-37b9-83f7-9c852fd36b1c | -10.8735 | -53.9668 | 2026-09-21 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 1e56a62d-7e8c-3b96-8b0f-3af4f8e944d6 | -10.7466 | -50.5959 | 2026-09-21 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 385a99dc-a1c4-3ae0-818a-3968469ce913 | -8.5984 | -54.6139 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 38851f18-30cc-3e7e-af61-00f456fe3fab | -10.4728 | -51.302 | 2026-09-21 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 212.0 |
| f381843a-d6c2-3490-8572-ed2290631d61 | -8.0894 | -55.331 | 2026-09-21 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0408ae26-3cbf-3331-a281-5c30d9afbc5a | -9.1523 | -49.9853 | 2026-09-21 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 68613635-49ce-372a-aa1e-c935a22d2550 | -5.804 | -53.5223 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a640e40b-948c-38c8-aa09-d5d5f5fa19cf | -10.955 | -50.5738 | 2026-09-21 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 40d6f97e-2a53-3654-96db-6071664fc8d0 | -5.8411 | -53.5002 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d3e5bfcc-9e21-3c21-b15e-dd2155890ef7 | -6.0973 | -53.913 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f4c7d368-7943-3599-bb86-7102cce18835 | -6.7369 | -55.0874 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| dba8fc90-a84a-31d9-8fe1-08de7040c334 | -7.5661 | -61.3239 | 2026-09-21 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b7af752c-77a8-3447-90f3-78fc758b54e6 | -4.4303 | -55.0867 | 2026-09-21 15:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 7e6f3bd9-a5f2-3566-8648-1cfeddc27a6d | -2.9709 | -57.7197 | 2026-09-21 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| a81e245d-0152-3736-bb50-faeb9892328c | -6.737 | -55.0674 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b14a01fa-f927-3e88-93fb-5525465079ac | -8.1688 | -54.7432 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 647e0c7e-6321-3de5-a6c1-a536c4abdbc6 | -6.8058 | -55.8217 | 2026-09-21 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 2c900c2d-cf4d-3da4-ab09-c7105d8dc946 | -6.5761 | -45.5194 | 2026-09-21 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| be26459e-20f7-36e2-9217-12c3d9adc103 | -3.4599 | -59.5209 | 2026-09-21 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4e4bb114-e8c3-3da1-85d5-bdc41e84d1fe | -8.1686 | -54.7634 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8789d5e9-baef-3589-9788-9c09767afe3e | -12.2914 | -50.1633 | 2026-09-21 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| ad33b710-e31f-362d-a809-5497ed1ff597 | -11.8168 | -50.0482 | 2026-09-21 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 6252371b-7722-34b7-af98-694ec49b929f | -9.5593 | -66.0545 | 2026-09-21 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 2960c855-7035-3342-b09d-2a356f5bf3ca | -7.7346 | -49.3799 | 2026-09-21 15:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 92f6ab6c-d2f1-39ea-9898-4c725a17b4c3 | -6.467 | -59.9902 | 2026-09-21 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f3727e0c-a316-39ff-ab6a-5ee56f2c7493 | -6.8263 | -55.5421 | 2026-09-21 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| c29665ed-a59d-32e1-9d2d-3a8e8b5f1cb7 | -8.1876 | -54.7219 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| c5224287-2252-3d56-a6a8-7cf7aedd6fe3 | -9.257 | -46.1873 | 2026-09-21 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5e9b0821-2721-329a-96b6-9c7eb947aedf | -12.5231 | -50.0051 | 2026-09-21 15:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 2f9abac5-d1a4-3f5a-9afd-9171d7970962 | -6.5451 | -44.8643 | 2026-09-21 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 712.6 |
| 4fba6811-22f9-3940-af11-9debfb66b79a | -9.1711 | -49.9835 | 2026-09-21 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| f529ec64-22af-3673-a6de-9a0bd99e18fc | -6.2585 | -41.6617 | 2026-09-21 15:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 169.6 |
| 3ed0baca-b716-3a36-9c82-a0570e212cc1 | -9.2222 | -60.2531 | 2026-09-21 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8f47473c-fb32-36f6-b40c-95ca2d6b29a6 | -3.3823 | -50.4486 | 2026-09-21 15:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 8c4ca0e4-3512-335d-af2f-688722dc4f78 | -6.1653 | -47.5052 | 2026-09-21 15:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a514b865-cb83-3739-abca-f3ee144dd4f2 | -0.803 | -48.6397 | 2026-09-21 15:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 743dbd19-ec5d-3bf2-8791-c31314aa6109 | -8.5982 | -54.6341 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f597e142-7a10-3e7a-90c8-0055b4c8dea4 | -11.801 | -49.8345 | 2026-09-21 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 96c2e6c9-5e34-3825-b9d3-87e32b653684 | -10.3916 | -50.2916 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 3e2bcc79-8260-3429-992d-d0fd1b4682a5 | -6.7485 | -59.0557 | 2026-09-21 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c5ba2bfd-aed0-3f20-ac3c-5a7e18da6f69 | -10.3363 | -50.1905 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 11089756-b0bb-39d6-a5a8-2199e77adc41 | -10.6143 | -50.5884 | 2026-09-21 15:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9861a8a4-cf55-3e22-9b54-b205315e7737 | -10.0898 | -50.2795 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 99dce8d0-36e7-3989-98d5-c8d3b7bc8d4c | -3.5356 | -58.6939 | 2026-09-21 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 02cf5287-541d-30c9-9d1f-05e57ef780ed | -6.183 | -47.6133 | 2026-09-21 15:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 36dd8638-7a88-31d6-9b25-3effaf79f567 | -10.3921 | -50.2488 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 6aca0a2a-10d1-3ea2-b431-4aa03636913b | -3.4828 | -57.9803 | 2026-09-21 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7af2818e-5fd1-32a3-b8cd-ff2300417661 | -6.295 | -57.735 | 2026-09-21 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 8acf7659-8f11-3f22-ab0a-55cf3086e222 | -10.9358 | -50.5972 | 2026-09-21 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| a3c228e8-db2a-303a-be81-a3b59a701ce5 | -10.2979 | -50.2372 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 49f6bd93-c2c9-300b-a35a-b2cd854be176 | -3.753 | -59.419 | 2026-09-21 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 120a41ad-d22b-38dc-8c32-76bbaeaec87c | -6.392 | -45.1948 | 2026-09-21 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| b5794d30-e3bd-3880-ac1f-ff480f0454a9 | -9.5595 | -66.0172 | 2026-09-21 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 901cad48-86c4-3452-ba0a-0298b510c76b | -11.8014 | -49.8129 | 2026-09-21 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 1c154c82-6639-3703-a99a-c06c739c3713 | -9.8307 | -48.451 | 2026-09-21 15:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| c5780e68-1ae4-3423-9020-70c75ad9cab2 | -10.3727 | -50.2936 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 7e9ac41e-b0be-34c2-90a6-55425972321e | -3.1514 | -58.644 | 2026-09-21 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3c6743d8-a62a-3a14-bbd9-ee02492a791a | -6.0462 | -53.2662 | 2026-09-21 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f19f84e8-1cab-399b-b24a-7e460163d2a6 | -4.4112 | -55.2466 | 2026-09-21 15:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 0185e413-3171-3789-a4cc-aaadadca9b0d | -10.4919 | -51.279 | 2026-09-21 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 99aefdf1-cedc-34d2-97cf-235ce609d5c1 | -6.0974 | -53.8928 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| cbe8b6ee-e950-3eca-bca0-322d38b6c617 | -6.5571 | -45.5434 | 2026-09-21 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 218.0 |
| a56c3631-84c1-3a9b-b52d-4d4f6569a837 | -3.6449 | -58.8647 | 2026-09-21 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 14082e7d-68c3-3f9c-90b6-dec9b9e0a30d | -5.6408 | -43.392 | 2026-09-21 15:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 98a1ed7a-d2a2-3cbc-baa4-ae10296bb34d | -10.4664 | -50.3479 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 86c1b28b-a288-330b-a843-c60b71167445 | -10.3549 | -50.2099 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 0accf1b4-9469-33c8-9235-351f89ccca4a | -8.7729 | -44.2568 | 2026-09-21 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 914.8 |
| caf4d651-e904-3de1-b600-3360f01f5731 | -13.203 | -51.7406 | 2026-09-21 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| d600363e-e48f-3b6c-a466-65352d83ce20 | -7.3125 | -54.9359 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 598eded2-2dc4-3994-a273-fbb9a2149443 | -3.6632 | -58.8643 | 2026-09-21 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 57523719-ca66-3611-af4d-f738c557de57 | -6.8264 | -55.5222 | 2026-09-21 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 05c7a7e5-0ebe-381f-9118-1750cb784bea | -1.4302 | -48.9529 | 2026-09-21 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 942c239f-9dc0-3215-b8ce-365fecebf6fd | -6.8448 | -55.5411 | 2026-09-21 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 4f2ff98d-fd53-36d3-92c6-9ed1bce8c1c9 | -11.0804 | -49.7456 | 2026-09-21 15:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 97b3df27-8888-3c92-a63b-c99df5fe8176 | -6.4228 | -55.0233 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| be4adf6c-78bd-3319-9836-cc5599c68686 | -3.1881 | -58.5855 | 2026-09-21 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| deefd8bd-731d-3b32-8551-e2e8898dbe0e | -10.473 | -51.2808 | 2026-09-21 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 467cc466-c467-3b78-95bd-99a29a8857c0 | -8.6169 | -54.6328 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ab7bea35-ec9c-312b-a2ae-8bb8b08b96f3 | -10.9547 | -50.5952 | 2026-09-21 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 224.2 |
| d3caa95a-019b-32c9-b900-74691d736620 | -6.5449 | -44.8871 | 2026-09-21 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 364.9 |
| 371c6f69-ee06-3dd5-ac3f-1c4a93cc3779 | -10.5906 | -53.9918 | 2026-09-21 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| b5ceb024-35df-32d4-89a2-136afef8d33d | -7.3289 | -55.2155 | 2026-09-21 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| a7121079-7423-363e-8c57-f3d53b013735 | -7.2333 | -55.6004 | 2026-09-21 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 7870056f-6de3-3b82-96e4-290c9266b56c | -11.4001 | -44.076 | 2026-09-21 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 275.0 |
| a3ac306f-260b-34a9-9d6b-fa72bbdf6416 | -9.1057 | -60.9511 | 2026-09-21 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 24a3a5d0-263d-3f22-b6cd-f83a9f5a40e6 | -6.5444 | -44.9327 | 2026-09-21 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 3442d217-8ded-31b7-8b79-eeefb8c10100 | -10.6 | -50.2486 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0c27f9c4-f44d-3383-b9ab-26a25a97df96 | -11.7823 | -49.8152 | 2026-09-21 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 71f2deff-6f25-3de1-840a-c00c348b2e26 | -1.4671 | -48.995 | 2026-09-21 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 8da461a2-77fa-3b90-8347-e8cbb15cebb6 | -5.6221 | -43.3934 | 2026-09-21 15:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 6ef24a7c-eae6-35bb-bceb-80e34865beff | -1.1345 | -49.2123 | 2026-09-21 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| dbf1fb14-51cd-3cd7-8e07-5411a507a8df | -6.5634 | -44.9084 | 2026-09-21 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| c6db1de9-6282-37d0-8e9d-9d5e6164fa38 | -9.8689 | -48.4252 | 2026-09-21 15:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 8d4b589e-277a-3b04-a7c1-cd85355d59ac | -10.336 | -50.2119 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |


[Clique aqui para ver as próximas entradas](README143.md)
