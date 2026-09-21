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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83745da2-ff32-3ba8-9106-853414fa390a | -10.80269 | -50.83868 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27363084-bdd6-3e8c-a7f3-8e8ebedc579b | -10.95062 | -54.09365 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb7f4046-bbbf-3c85-99fd-de54c3231d6e | -7.24546 | -55.60423 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bd64f828-21a6-303d-9653-cf5f28d134c2 | -9.82684 | -48.41133 | 2026-09-21 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2372d48-4dfd-3a3c-b36f-007945232ae7 | -10.44427 | -50.2628 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3bb5f6df-8083-341c-aaca-73a360b55b08 | -11.0981 | -48.29355 | 2026-09-21 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b50404f-b735-3e79-91b3-5bf9854c3632 | -6.64928 | -59.96429 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccd7dc3d-6e26-332f-a704-3868044a2f05 | -8.17795 | -54.77549 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c02eaad-cefd-373b-9139-26e4ab0492b0 | -10.14208 | -45.55944 | 2026-09-21 05:06:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1a5b1c3-815d-3330-b81f-b95224c267df | -8.23851 | -56.17357 | 2026-09-21 05:06:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f21865e-cd2f-30ac-8165-5e9d2549718c | -9.46273 | -45.39891 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c8384fa3-aac8-33c5-8050-58d7e318ebac | -11.03329 | -54.14615 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5b36b6c-6a2d-33d5-a1ce-1ca2c6c889c0 | -10.76852 | -50.81493 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27a007d6-83ed-3e73-ae4a-f77cdab4b7d5 | -11.73614 | -54.5547 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cdfeda5-e088-3684-9e51-d219834ca1e6 | -8.7782 | -48.74487 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b5b41c38-8127-33f2-b6aa-bec8ff22572f | -7.87667 | -54.72623 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 787c1b76-96a9-3583-9c3d-146ce17f208c | -11.62788 | -47.77831 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 824ea824-9c31-3486-9467-a44722a3dba8 | -11.25781 | -54.14451 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 925a6447-3558-3027-ab65-9c29b5bc558a | -11.80791 | -49.80686 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 8c5e8451-44dc-3a2c-b2a0-5e62cfe81df0 | -11.10332 | -48.29383 | 2026-09-21 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cfc71ae-7802-3214-a77a-c283afae6de2 | -9.12086 | -58.92261 | 2026-09-21 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b8d149a-792a-328a-ab63-8e1c1ba8988b | -7.58581 | -57.70028 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15181ca0-2c03-3ffb-8a6e-3f73943fe310 | -9.04615 | -61.64166 | 2026-09-21 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49f405e8-c3bd-3b94-8296-e79a3e977218 | -11.04262 | -54.90781 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22c3eb0e-5a8d-3b86-9301-487ae6d6fb67 | -9.2788 | -46.21964 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fec3829-7e95-3be5-acf1-c7d4a93ad3be | -8.61579 | -54.59263 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b76e60e9-247c-363c-86e7-31686fef4756 | -10.4782 | -45.09991 | 2026-09-21 05:06:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c213a617-c5bd-3c11-851a-b5c3c70ce238 | -9.30431 | -62.31478 | 2026-09-21 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d528f15-5fc3-3a63-9a68-3d98b353c34b | -12.22276 | -57.25798 | 2026-09-21 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5cab81c-20e0-36d4-bd2b-eee908bbaedd | -8.92066 | -50.91152 | 2026-09-21 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 233e3b37-e7f9-3fdb-9d13-e04a05eff9b1 | -9.11251 | -60.94758 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21cf7484-4b80-3e71-a59d-e433812c40bc | -9.81957 | -48.30754 | 2026-09-21 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be169e5e-9866-34a6-ba8e-c8bf758fe139 | -9.71951 | -54.82689 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6045ef14-6157-3402-8bcf-1c8ed68a5c64 | -9.53123 | -45.39721 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 682701b6-889d-3d48-b4ef-ab08b759df35 | -9.01301 | -48.15461 | 2026-09-21 05:06:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 601db4b1-3da9-3c77-9605-580931bdf1eb | -9.71701 | -47.10056 | 2026-09-21 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78310e61-c930-302c-bae5-4058aef5b9f9 | -10.68056 | -48.71731 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 82d26e42-1f32-3d77-9cb3-900e891b55d4 | -10.74112 | -50.7897 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee4a2c1e-fa01-3b01-9a07-05c27829d7fb | -11.07954 | -54.02234 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8382bc42-9ac0-3399-ae06-86cbed14a4f9 | -10.62033 | -67.93058 | 2026-09-21 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4789cb1c-8e78-3be0-b19d-946c883ba1e7 | -11.99258 | -58.06911 | 2026-09-21 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7a886b20-211c-38cf-8e5d-f19e86378f30 | -11.98594 | -58.06803 | 2026-09-21 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e237983e-2bde-3831-8f9d-fec654073860 | -9.02885 | -60.36346 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 28d42d79-4de4-3e11-99c0-e13d7a25f013 | -7.5916 | -57.66425 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 190d1902-0383-3db3-aaeb-2951a26cc057 | -9.68169 | -54.3312 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36f10fa5-ee03-36d6-9919-8223177b501d | -9.55882 | -66.05572 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a118fdde-9679-32ad-b380-02cf1c45ba29 | -11.94583 | -46.49993 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd151c9a-a406-3c3d-aa8b-4e7d8ccb0d04 | -9.54456 | -45.3951 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e195c4d3-f243-3fc3-b1c4-55e1c0576004 | -9.8489 | -48.39929 | 2026-09-21 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5ce03fe-c70c-31c6-b4a8-614c933d42de | -8.7935 | -48.74101 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 648086b8-868b-3236-b276-b6397f6a385f | -9.57077 | -66.05087 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 681f7df2-b64a-34ca-8029-5fb23f16b53c | -10.45768 | -50.26472 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 801a1b6a-7075-3d5a-9f99-616748979416 | -9.25929 | -46.18753 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f1360c0-7584-3dcd-944e-c75aa7b930a3 | -8.18512 | -54.72805 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6847274d-bc84-34b9-8b3a-4414cdf48bec | -10.98331 | -50.59445 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4039c787-e2ae-3f25-a422-c4aa1b87d611 | -7.57957 | -57.68409 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d98a1af9-2d13-3a4c-b052-85b613491c30 | -11.47805 | -47.77237 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9436ce4-1173-3d68-84ad-9a80e5a1772a | -9.45561 | -45.40158 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| f8965baa-65ca-3dc7-af18-b162463c1ee2 | -11.75542 | -54.56985 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 678fe98e-c835-3c39-a2f2-b0448a83353a | -11.95066 | -46.50081 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10d6abed-4f0a-3e82-91d9-c829d168f46e | -12.53848 | -50.08235 | 2026-09-21 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7bd3ba56-92ab-39f8-8cbc-3ec473ca2a23 | -10.68004 | -50.73999 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 755a9c1c-d3eb-3a47-8dc1-ebaac1de61ac | -10.87297 | -54.05251 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19d406d6-37bc-37ea-b193-ef3a2e51e94b | -8.79562 | -48.73514 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a8200648-d881-3127-9239-4bb19cc8be66 | -9.57141 | -66.04742 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abdab228-ebab-32a9-b698-b540feef99bb | -12.80032 | -54.05522 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d26b0fa7-0887-3c1a-a2ea-b6481faae351 | -10.55608 | -46.73743 | 2026-09-21 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb104fe0-e54a-3500-8ea1-d2c2c00b37e1 | -9.53062 | -45.40208 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 001fb8dd-9604-3613-89ae-1d3b1d47f714 | -12.42137 | -47.0338 | 2026-09-21 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd624942-0c4a-3aa3-ac20-10023937aeeb | -6.75665 | -59.11611 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e15a82a5-1c73-3dfc-b6a7-62da3a97b46f | -10.38363 | -51.86748 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b242ea84-6b5e-3492-80dc-a142e0557b92 | -11.27684 | -54.13322 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abed1d8e-5acc-3941-9343-0e0ff0315b33 | -11.36558 | -51.43227 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c692699-b5b7-3f27-9e14-680e3bcb42e3 | -10.79655 | -50.75229 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ef21f0b-3666-39ac-8835-e3b59aafb054 | -7.57226 | -57.68662 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1fac909c-f14a-3cb2-a4a2-ce43823f4441 | -13.72755 | -48.79279 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 547ff45b-a7fa-3682-9bd1-f9ec976b659c | -9.55349 | -66.05465 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c06f13c-d6e1-3ce5-abbe-f9bf88fe7caa | -7.32969 | -55.21327 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a70b791-767e-3b9f-93f5-27c08f7a014b | -10.40946 | -50.22868 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| db1611ce-796f-3965-86c5-beb06c1d8c09 | -9.68922 | -54.32836 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d7253fe-73aa-30db-a7c0-89f27836009b | -10.54073 | -54.49144 | 2026-09-21 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f65b7259-727f-3ba5-a37d-aed85bdfd432 | -11.05146 | -46.56666 | 2026-09-21 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 783eac8e-ccaf-3c3a-ab2f-3a5b9dba31c7 | -12.80472 | -54.05392 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be3d8cdc-d152-3cb5-b13f-05aa95bf8aad | -11.10528 | -51.05798 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 581220a1-786d-397c-95ff-664d7943db42 | -9.27998 | -60.62912 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa423a8a-ff61-33cf-b275-71e8b7310975 | -11.80132 | -51.11454 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f8a8d5f-4d8b-356e-baba-dbed8dc3150b | -10.37959 | -48.90144 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cc06058-01d4-306d-91c3-edfc87ccc136 | -10.92002 | -53.95437 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a89f99c5-530a-3028-bbd3-91aeb0b222bb | -9.11012 | -60.94963 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec4e0600-3c18-393f-9945-e4f659815c8f | -11.09936 | -51.06957 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bba88a8-0f71-300a-ab5d-c07561584d57 | -6.79853 | -58.79027 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c1c21df-e4e2-3d08-bb23-b2d867fd4acd | -11.04334 | -54.15181 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27eb8f69-746c-3f31-a0c4-9a1deeda327f | -6.43843 | -59.97113 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0f116924-b401-35d1-b663-3e7ca32c1ce6 | -10.48251 | -51.2853 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3543dea1-32b8-300b-96db-c88abd386dc0 | -10.8111 | -50.77586 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef104fa8-45d1-3349-bdba-0c8e241295e7 | -11.72736 | -54.56556 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe996d0f-ca96-3115-9e24-875218c14a46 | -10.87469 | -53.96445 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0f6c16e-7977-3857-9498-7631222c877f | -11.01967 | -54.13999 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbf5b18d-6df8-33af-809f-540087843d09 | -10.87712 | -54.07418 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e759458b-9081-3b3e-affe-9d45304e49c6 | -11.04924 | -54.16097 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README73.md)
