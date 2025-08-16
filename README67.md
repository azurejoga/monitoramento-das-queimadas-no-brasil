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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cb80732-8410-3de1-bbd4-166dbc956f30 | -9.5113 | -60.54141 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 716ce5c2-3c58-3219-9ef8-edf40593aeae | -8.05728 | -70.58202 | 2025-08-16 05:50:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1fe4b7d-269e-358b-81f9-07b036dae59c | -9.1685 | -59.65269 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb9316ee-0a36-308b-a7e9-86080cc049ba | -7.53322 | -61.32885 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| deb332cc-bf6a-3f44-9901-ba1aacdb73d9 | -7.4393 | -60.02971 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96b2b1fd-116a-3cea-b8cb-6548d6d45ad4 | -7.87944 | -61.81996 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4a7f5a9-4097-3e02-bfea-bb4cb769901e | -8.99133 | -60.49445 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 4f26cb3c-b160-3212-be41-c3aef249f5ca | -8.56044 | -63.91849 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a76aba0-00f8-321c-bdaf-0307ca44df23 | -7.62895 | -63.32098 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a385d14-3d5f-3405-a7d4-2a58ed2c7933 | -9.15172 | -59.66678 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b1c48e2-fc01-3e2b-a6c3-a8f86197a26b | -7.66896 | -63.30871 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a29525f3-72af-3c66-bfa5-24fd0f7cf665 | -8.98229 | -60.55641 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20f0b701-0642-3ed4-85aa-54f2e304a9fb | -7.91185 | -61.74165 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd649eb6-eabc-3536-a6c2-37224df9497c | -8.11247 | -61.19138 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1303aaf-387a-3c8c-b995-3090ffef5c57 | -8.98705 | -60.56027 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1180c76-7886-38a6-bea9-52936b3c6940 | -6.14508 | -57.93305 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5873d1fe-9224-3d87-bbe9-bb5036eced2f | -7.04741 | -59.62037 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93ef3bbe-f88d-3876-a133-f7e25c8738d6 | -7.4518 | -59.9388 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bef4f4a-15e8-3b66-a859-073b1056061d | -7.44234 | -60.01878 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85c7a5c2-3dea-32fd-9fdc-95e5758dd808 | -7.87533 | -61.81935 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b8ec62e-59a5-3533-ad02-9d49acb19c3c | -7.92065 | -61.73919 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2bc55f0b-8c80-3005-ba6b-21b37b3ee800 | -7.52706 | -61.31178 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42b36ee1-d411-30fa-9ca9-98bde63ffa90 | -8.55486 | -63.93076 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02791f2b-eff9-3403-9fdc-ba59c02c1c8f | -9.15585 | -59.67276 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dd73744-e41d-377a-bb42-dfc337fb365e | -9.16511 | -59.64127 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9ebaf2b3-6c4c-3adf-a203-8bc945eb87bb | -6.93139 | -59.54547 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4cb1bfd-34d4-393f-b0a8-fb3663f28f7e | -7.05143 | -59.6259 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7a17851-c9bc-3a8b-be79-b5218adf248e | -8.55057 | -63.93447 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 597f2618-b7ab-3b9e-8b30-ebb23835082b | -8.98295 | -60.55178 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9ad1405-1a02-3d89-9633-4ebf4ede5120 | -7.52225 | -61.31512 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d93c17b-a464-3d5c-8fc4-8e6ca1c8eab9 | -8.66405 | -62.45897 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f8153ce-4dd1-3cf5-8593-574a604735f5 | -9.1767 | -59.66503 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b87688c-6872-38e7-99db-243399f93d6c | -8.09956 | -61.18951 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf4e965b-ab4c-3deb-b8f6-d8c60bb20401 | -8.98422 | -60.51256 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b99a2f60-fec9-3210-a413-ff246561aa8b | -9.16775 | -59.65812 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7240744b-7e9c-361d-8b7e-c30bfb8db95e | -9.21945 | -59.66067 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efc725d8-96a8-3e13-9257-9d08f5ca66db | -9.20736 | -59.65815 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 674b345b-dd9a-35b8-be7e-590b73875bb9 | -8.89588 | -60.7434 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1353e5fc-dee4-393d-9fb9-34f544521506 | -7.94796 | -61.75449 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15ed41e9-fb49-392d-848c-ce3ab502ea50 | -7.61531 | -63.33047 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f2ef6b4-26de-338d-b80a-f9cedf18c7e8 | -6.13984 | -57.93243 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56028b9a-cafb-335c-8f17-7e086613b13d | -8.98427 | -60.54259 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 091c09d3-855a-391c-9ec8-ea202bf40c18 | -9.17409 | -59.64798 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab33a5b3-d6e2-37d1-9fb6-146ebade45f0 | -7.90196 | -61.75161 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12f0e0ae-c895-39c7-9271-c25647a9ab4f | -6.14462 | -57.93624 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 338b833d-121a-36b8-b4af-d4de588860b2 | -6.93611 | -59.54623 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 824606b5-8d05-36c0-86e4-882cd87f1314 | -6.65838 | -58.81923 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a214f09d-ea3b-3fdb-927b-8ea3d52102e7 | -7.95208 | -61.75512 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa44e21a-0dc1-33e9-ad38-3e9725adfd53 | -7.91687 | -63.51272 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5823077-dc12-395f-9eb8-2918fc53b73f | -7.28298 | -64.69463 | 2025-08-16 05:50:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d011e3fd-4a44-395e-8bdb-95d65b78e878 | -7.81252 | -61.32936 | 2025-08-16 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0989bb5-b90f-3e7c-91fc-8d5379a5746f | -9.51264 | -60.53196 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b48cf12e-76ef-39ff-a868-dba17c3a3093 | -6.65761 | -58.82483 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1938017-388e-322d-bfd8-4a4505b50d0d | -7.95322 | -63.21086 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2adb9ba6-63e6-3baa-ad11-d7ab7bbb49b2 | -8.99069 | -60.49913 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b479190a-61da-3e21-856c-5f0f9f6ed259 | -9.1666 | -59.63037 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 99081042-f996-3602-a05c-6d785adb47b4 | -6.13459 | -57.93184 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e885e4ba-fe58-31d2-9111-1affdb999556 | -8.99483 | -60.50138 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 16bf7b2a-135c-3f62-a542-c8cae19aaa82 | -6.69805 | -58.82498 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1c8ade7-b76b-3037-a0ef-183b3889acb8 | -9.00247 | -60.51529 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29071baa-5ff1-3250-afa0-8fa7400c137a | -7.43405 | -60.03368 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a0db11a-3618-33aa-afb2-582a00b8029e | -6.65751 | -58.8182 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24d36f62-2ad9-3ebd-9b4b-750c7e312eea | -9.15611 | -59.63456 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 726ce4fa-03d6-3bc6-9f23-69befd0e7d41 | -7.503 | -63.82193 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 78db7606-e250-3c82-aa15-04b460c05060 | -6.93996 | -59.65332 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed626ee0-a169-3746-a19d-969308049bc8 | -8.98438 | -60.54573 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dbd90c7b-fd27-329e-9375-63cfabe65e26 | -7.56288 | -61.42009 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fc88f47-aa5b-3fda-a5a6-2660597ca31b | -8.99526 | -60.49983 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb300944-984d-3f4c-955d-159936635ef4 | -8.98162 | -60.56105 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0697a2df-2662-367b-bbe7-72036ea0dfc7 | -7.92784 | -61.74781 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 427af09e-472d-35a8-bdb5-cea445943526 | -7.45558 | -59.92768 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25e4812f-a836-3520-a3a6-9ea39c27c00a | -8.99855 | -60.50988 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17994757-04b2-3904-befb-b1e883cd6468 | -7.62457 | -63.32488 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fd3aaf0-ea00-3f6b-9dc9-416f7b1b7f8e | -9.50931 | -60.54913 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 136850a0-9528-3f68-ad03-31d7479b71ea | -8.11306 | -61.18733 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f6a4bf6-0918-34a8-92ad-69bac07f055c | -6.66825 | -58.81398 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51227731-b8f4-32f8-80b0-9f627f01b255 | -7.43173 | -60.02691 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f5c1788-214c-345b-8732-0e341039f5c1 | -9.15512 | -59.67808 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 568cfeb4-ca8e-31d5-a476-6fd67d017e65 | -8.96954 | -61.68278 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 70555229-d3f6-3ae2-beb0-162fdc05cf46 | -8.99349 | -60.51074 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dcc95390-58f8-3020-8031-b714174d382f | -7.9483 | -63.21713 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46db7eee-e0b3-3623-969e-5cfeeac99ee1 | -9.50471 | -60.54852 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a19e9f7-1340-37fb-8c54-6e275eee413e | -7.45314 | -59.92902 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ff26280-339b-39c2-92d7-ea227366cb4b | -8.4126 | -67.74229 | 2025-08-16 05:50:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27d21a97-6d49-398c-a772-90b8f2909af3 | -7.44164 | -60.02357 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef51e546-3425-37f5-8810-0e4f4bd045f5 | -6.94554 | -59.54784 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9dc3d784-c9da-3c9a-aae9-517ef6a32e45 | -8.94423 | -62.23935 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86340d3e-3222-31c9-b663-5d89cbc10984 | -9.39431 | -60.54248 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a33bda0-afe9-3566-a96d-237d5339c115 | -8.98187 | -60.56425 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3c33071-fcb7-32e0-be7e-1539185e75a9 | -7.91131 | -61.74535 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd54447b-a27d-3bc5-8833-3598de1c1db6 | -7.91652 | -61.73856 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be98b656-d688-3048-a6a9-aa2e263e65ee | -8.99006 | -60.50382 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6015c1aa-55ce-3118-b1ea-5b9d82f382bb | -7.45487 | -59.93261 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6c2cb2d-7c8d-37c9-9f10-2ff0c09fac17 | -8.11129 | -61.1995 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a4dfc4b-21ff-3ad9-805b-8b34eab165a6 | -7.07717 | -59.24103 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7315d2a5-5a40-3ba2-b1e3-b919529b2112 | -8.99929 | -60.53855 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0b18986d-a033-3016-a456-7e4b9f25520b | -7.42116 | -60.0349 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16640ca9-bf57-3808-95e4-625031fa91ad | -7.59861 | -63.50158 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12986ab0-9648-306e-ba1b-710d0b2afc04 | -8.98096 | -60.56568 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d52eda55-c712-308b-8da5-2e1f0f4ccab9 | -7.61395 | -63.33938 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README68.md)
