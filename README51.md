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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb82ef86-6701-3a9d-8dcd-59ba04e2c218 | -10.68663 | -68.86085 | 2026-09-27 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6954c30-8a26-3695-97ac-fe4521c51c53 | -11.98618 | -57.60793 | 2026-09-27 05:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deb7a2bb-33f5-3b07-bf0e-43b709dc39b5 | -11.03189 | -54.04586 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0d4de82-57e4-340b-845a-3c4f15ce17d2 | -11.27658 | -54.43656 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2dce81d9-5520-31cc-9f78-505da0cd0fe9 | -9.13117 | -67.84743 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7d9643b-007a-3673-bb11-f3a49c8a10a7 | -10.8113 | -60.726 | 2026-09-27 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5a34257-f39a-30e6-962b-d7101e3e7cea | -9.63946 | -55.13422 | 2026-09-27 05:50:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 870bb590-2656-33a6-b0d6-d56ac385c2b3 | -8.62547 | -54.67379 | 2026-09-27 05:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e446c9e-1edf-33d0-97b2-805ee2f09967 | -10.81861 | -60.73517 | 2026-09-27 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bfaeccb4-969f-3b58-816a-0586b6cab3d3 | -11.27724 | -54.43108 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 466388e6-0a3d-3dfa-adf1-0538221438c0 | -9.64051 | -55.13665 | 2026-09-27 05:50:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e96cd41-3f40-3558-bc9a-059c77b99958 | -10.67949 | -57.63332 | 2026-09-27 05:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a510116d-4748-3045-bdfe-d09dc857ad56 | -12.89014 | -61.71478 | 2026-09-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 754acb62-212f-38b6-91fc-dd7033edf0a0 | -9.28209 | -67.65352 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9227b97-b582-3ae6-b6e4-82aabaccec26 | -12.89728 | -61.72329 | 2026-09-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86315098-2f14-37ab-ba3f-1973a481e94c | -11.01974 | -54.04973 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bdc81e3b-f02a-35b5-b769-b41caa40ff1e | -9.27256 | -67.64822 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dffeef02-f784-36c6-b8aa-eddf9d3ecf93 | -10.8144 | -60.73452 | 2026-09-27 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 42f77a4d-fd17-3f66-b390-3ca34996f453 | -10.40899 | -53.81226 | 2026-09-27 05:50:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36e6881a-84a5-3dec-a071-36cbe2e41ee6 | -11.02772 | -54.03891 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 061a44bc-7036-3760-a1d6-bad2dc4ad3af | -11.27593 | -54.44204 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 17159d59-53b7-38c9-9aa5-96258e61e662 | -12.89829 | -61.71593 | 2026-09-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9322e3e-4e24-3004-8cb8-80e7ee849b1e | -8.63161 | -54.67471 | 2026-09-27 05:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f32b971-bea9-3b6a-91e5-4888775c9fb0 | -8.88874 | -66.87041 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b511cfce-77c8-3657-a6c9-259db509064d | -9.28328 | -67.64624 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc151792-2385-3ec1-9685-a46be481e58c | -8.5973 | -54.65339 | 2026-09-27 05:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c54e9732-1399-3eac-8d45-52e64fa22614 | -9.63888 | -55.13866 | 2026-09-27 05:50:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5011bf6-e902-30c7-916b-7e26636e59a1 | -10.81074 | -60.72995 | 2026-09-27 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6bd16d1-890a-38a4-b668-dd2f27732727 | -9.27872 | -67.65297 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84b37462-4ebc-3ead-9ecd-303baad72cd9 | -11.1639 | -62.86945 | 2026-09-27 05:50:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddd54852-39a8-30db-9b6c-a438da720cf0 | -10.03832 | -62.45731 | 2026-09-27 05:50:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d4e7d04-82c1-3552-a7d3-db8f48fb2e7b | -9.28666 | -67.6468 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab8faa04-1be6-3f33-bd1d-745741e2c313 | -6.93261 | -62.94355 | 2026-09-27 05:50:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1c30c85-825f-3d27-9bc8-2e0f038e0167 | -8.60368 | -63.93085 | 2026-09-27 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b083c93c-b237-3c71-9c14-28385665de1c | -21.28999 | -57.89999 | 2026-09-27 05:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 03eea585-8f4b-341a-828e-cbc414fe8ea7 | -21.29062 | -57.90132 | 2026-09-27 05:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 86e30d8b-906f-3b5f-a7d1-ce905eeefffe | -21.28477 | -57.90071 | 2026-09-27 05:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f231e643-c870-33a7-9f9c-9d02773bdf62 | -8.3679 | -44.13889 | 2026-09-27 05:55:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 5e315c42-32b4-3e0c-9638-fea82204af86 | -8.34758 | -44.20263 | 2026-09-27 05:55:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| c2afa03c-eca6-3df5-9849-620cc078fb38 | -8.36165 | -44.1738 | 2026-09-27 05:55:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 356.9 |
| 12c20880-fb12-3573-9b7c-1c910f9bdf7c | -8.35166 | -44.13599 | 2026-09-27 05:55:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 899cbf67-280b-3245-8b24-19066dd00dfc | -8.34533 | -44.1711 | 2026-09-27 05:55:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 746.6 |
| ee483ba4-b2a6-3d90-9d68-a14d438163e7 | -8.33732 | -44.16479 | 2026-09-27 05:55:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 183750a5-8f4a-36a5-b1a6-4c3626643078 | -8.35968 | -44.13243 | 2026-09-27 05:55:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 302.3 |
| 199e597e-66ea-39c3-9170-9f5d7ae54598 | -8.35365 | -44.16743 | 2026-09-27 05:55:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1233.4 |
| 8f592468-9efe-3ff9-aca6-bffade6998ba | -3.91419 | -43.02808 | 2026-09-27 05:55:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 43183ca2-d656-3fd6-a81b-b54fc6a9f084 | -8.36 | -44.2 | 2026-09-27 06:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cdf8895a-8d5e-3d0a-9d7f-3d0936be60ed | -8.33 | -44.15 | 2026-09-27 06:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 86a7f54a-3428-3e64-8fa8-ac89d50e870f | -8.36 | -44.16 | 2026-09-27 06:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8a1ba316-b810-3915-864f-ea8a24b73789 | -9.28938 | -67.64642 | 2026-09-27 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03fb2e05-83d8-3438-884e-970018825d2a | -9.27514 | -67.65257 | 2026-09-27 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6abeaf24-7252-3c08-99e9-63117ef08d3e | -9.28331 | -67.64553 | 2026-09-27 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1656b57c-b136-371e-b5f6-1b4753f0d0c9 | -7.82009 | -72.8063 | 2026-09-27 06:33:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3d922d8-30d1-37ab-89e6-7bab5d50490a | -9.27612 | -67.65385 | 2026-09-27 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f8fc4d4-66a5-3dca-b56d-47f05819c88f | -9.28275 | -67.65013 | 2026-09-27 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f05195de-4d79-37d6-86a5-813a9c972966 | -9.28219 | -67.65475 | 2026-09-27 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7142d0fb-ca95-3aa5-858e-d37277270b6e | -9.05183 | -66.11005 | 2026-09-27 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ba51c55-0035-3ebe-b9d3-993a83faed5c | -9.04519 | -66.109 | 2026-09-27 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e56e9882-1f53-3d63-9658-5987303f0581 | -9.2812 | -67.65346 | 2026-09-27 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32962912-370d-3173-bdb0-d63104c0cc70 | -9.27668 | -67.64922 | 2026-09-27 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 15297119-aac7-35a3-90f5-272d70e21c5f | -9.27573 | -67.64796 | 2026-09-27 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82bbe67b-7ff3-3d11-85df-cc0077e61f52 | -10.5454 | -69.22964 | 2026-09-27 06:33:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0313d37b-1843-3f35-b12f-3e1562720f79 | -7.82064 | -72.80871 | 2026-09-27 06:33:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b3b862e-b9ae-3962-98de-96badbf021a1 | -9.2818 | -67.64885 | 2026-09-27 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6789ecdc-8583-3a87-a32c-68249be3ba54 | -9.04786 | -66.10991 | 2026-09-27 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a34380c-13e2-3ea2-9fa3-2674499e021e | -8.36 | -44.16 | 2026-09-27 07:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d3a097b-3254-3fd3-9a0d-fdb2647560af | -11.9434 | -50.4844 | 2026-09-27 07:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a26139e2-d49d-3160-a1f1-ff6b30c7b252 | -3.82513 | -55.90364 | 2026-09-27 07:31:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3460c987-335b-37bc-9bf6-7b6be76f19f6 | -3.85884 | -55.80534 | 2026-09-27 07:31:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ddb6aa6b-89ca-397e-ac45-769e15d875e4 | -2.93208 | -56.56905 | 2026-09-27 07:31:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f27ee8fb-2a94-3c23-aa6d-cb6faf3b07ae | -1.04263 | -53.56848 | 2026-09-27 07:31:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2d4101d4-56ba-3bdc-a271-30a31dff4788 | -1.11577 | -57.27468 | 2026-09-27 07:31:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 362e4e8e-497a-3c5d-91ec-60acbde807f6 | 1.65908 | -55.93016 | 2026-09-27 07:31:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d4d3d006-2207-378a-8631-33845a4d9667 | -5.16696 | -56.00304 | 2026-09-27 07:31:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 95dbdf15-00ae-3de1-87e2-f7871b7ee664 | -3.00891 | -54.20725 | 2026-09-27 07:31:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7134004d-607f-3ff8-bb70-86f4b99504a3 | -2.06325 | -56.86755 | 2026-09-27 07:31:00 | AQUA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 355280b8-0596-3139-b05d-844ed1c0b470 | -5.16049 | -56.00676 | 2026-09-27 07:31:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a628dfea-a16e-341d-9230-3a28e60791bb | -3.83448 | -55.90499 | 2026-09-27 07:31:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 88ca89a1-e09b-31af-9cc3-eb077f5d00f7 | -2.67118 | -56.45634 | 2026-09-27 07:31:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 37edbf15-eb10-3e6b-8d00-4fc3361a28ab | -4.48754 | -54.95359 | 2026-09-27 07:31:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 3abf69cc-9f81-38ae-b4df-cb9cd61ce697 | -3.85734 | -55.81549 | 2026-09-27 07:31:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6330c0b1-149b-3672-8892-3ac14fbb0d8e | -2.93069 | -56.57825 | 2026-09-27 07:31:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 561aa223-ebbd-374c-9607-32ac90b33f89 | -4.49952 | -54.9384 | 2026-09-27 07:31:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a337b803-b9a4-3f72-b2d2-5b30b34b7d64 | -3.94745 | -56.08932 | 2026-09-27 07:31:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 246514e4-4b20-3d5f-927f-16da4f55a17f | -4.55973 | -54.94724 | 2026-09-27 07:31:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 060c9358-474c-3085-a6f9-9ba938c85aae | -2.0544 | -56.86626 | 2026-09-27 07:31:00 | AQUA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 27d6fc32-a931-303a-8bf9-23135edeab2f | -4.48783 | -54.94849 | 2026-09-27 07:31:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 06bb0a8c-9b3a-3db5-8c0a-1b8c85edca2a | -4.28958 | -55.25479 | 2026-09-27 07:31:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bc786fe2-804f-3247-840f-b5abc9b37430 | -4.4895 | -54.93684 | 2026-09-27 07:31:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ceb55bb7-75dc-3bf9-832b-bfd45bda62af | -3.2274 | -54.3195 | 2026-09-27 07:31:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d3afe163-3013-37dd-89ef-f4d8fd74fac0 | -4.98009 | -56.15084 | 2026-09-27 07:31:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0b400923-9da6-3f83-a1a3-2ce79353cde1 | -3.19797 | -51.03501 | 2026-09-27 07:31:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 285879ca-ef1c-306f-89ae-086ec9a4a112 | 1.66043 | -55.93912 | 2026-09-27 07:31:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 9f19a1b7-c332-3c77-889d-afae6301b435 | -1.04456 | -53.55548 | 2026-09-27 07:31:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| bb053bcd-551e-33ba-b4bb-6e1966897e90 | -4.54457 | -54.98062 | 2026-09-27 07:31:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 632666ca-50a1-3b80-a863-6e6ff9830818 | -3.20376 | -51.02866 | 2026-09-27 07:31:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 807ea673-2b47-3300-872d-540535da044c | -3.96458 | -59.34291 | 2026-09-27 07:31:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 91243a91-741e-3ebc-90f2-a6d4a8dcfbcd | -4.49785 | -54.95006 | 2026-09-27 07:31:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ec6bdd67-843a-38f1-a130-4457538d9898 | -4.97079 | -56.14906 | 2026-09-27 07:31:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 02a5e366-eb91-32d2-8767-2362ea5224fe | -4.48928 | -54.94195 | 2026-09-27 07:31:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |


[Clique aqui para ver as próximas entradas](README52.md)
