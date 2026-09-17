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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd13d8d1-c899-36b0-a784-604ff905c4bc | -9.2204 | -60.555401 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48efa5ea-915f-38c6-a18d-4531c1832a20 | -8.423 | -57.644901 | 2026-09-17 01:22:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33428dfb-ad07-3839-895e-e408d8c82e45 | -12.4179 | -50.8307 | 2026-09-17 01:22:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2df0b663-c9aa-3186-b5da-6c81cbc8f2e2 | -8.4297 | -57.673901 | 2026-09-17 01:22:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 517a3bba-ce1f-3e13-909c-a076d2c5ac4b | -11.9193 | -52.496601 | 2026-09-17 01:22:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08d71ded-7c35-37ed-bf08-59b91cc24290 | -10.5234 | -64.976303 | 2026-09-17 01:22:00 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a64072de-aa3c-3e7c-b117-07f91a43a987 | -5.0866 | -55.9604 | 2026-09-17 01:22:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c77a3de6-a1af-3aac-9d2b-589a2573cdcd | -9.5242 | -60.5331 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 631f5735-5175-3a2a-ab53-4f570f82853b | -13.3137 | -57.055302 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc69b60d-5199-348b-9d76-64c2e86a2d65 | 0.8603 | -59.2071 | 2026-09-17 01:22:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7671d5-9afc-3e95-9d24-b9b85f5dd060 | -6.3041 | -58.298599 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 492f2138-5318-369e-bef0-c6bcbb72d581 | -6.2927 | -58.2938 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd04d8d8-f9a5-3acf-bfad-55f305ce6a6d | -9.3339 | -60.372398 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 412d5a6f-76c9-3c02-aba4-b56edae36b07 | -9.3301 | -62.731899 | 2026-09-17 01:22:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6477683b-5ff0-3ffb-baf7-74299d224309 | -7.0478 | -55.139702 | 2026-09-17 01:22:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a0aeffd-3ec7-37a3-b16b-0bbca647ba0a | -2.8318 | -54.177502 | 2026-09-17 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb18efe5-ef84-3983-9d84-b50b8be41a10 | -12.0406 | -57.219601 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70772f69-e44d-3419-8ee0-a43d3d0c92d2 | -11.7385 | -58.197102 | 2026-09-17 01:22:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5dc6878-2c9c-3584-b4b5-ea14ac428964 | -2.6315 | -57.631401 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95a9ad51-f6d6-3840-b31e-64e8749dc2ab | -9.0171 | -61.027901 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8ef7430-831f-3bab-ae7a-eaad70a47f4c | -6.7442 | -59.1782 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e948f11-6b7b-3b98-8947-989fe1727119 | -12.0488 | -57.210098 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40d48d9e-236a-300f-a30f-65abc6cd4351 | -1.282 | -55.857101 | 2026-09-17 01:22:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdf1e3ff-7f27-381f-b45b-a2cb145c864a | -9.3212 | -60.315498 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c1ff272-9424-3c0a-a1af-25cfded15477 | -9.3697 | -60.394402 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52ed292e-9a0b-3b1e-bdca-06b6dac23ac8 | -6.7317 | -58.809799 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a7ab116-10e8-3775-9cfc-9eae129f7816 | -9.0236 | -60.964699 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9957c78-4963-3d45-99d4-cf13b8833a40 | -10.7789 | -46.186401 | 2026-09-17 01:22:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 887b1bd4-0ec4-3a33-867f-f80671be86f9 | -9.017 | -60.981602 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47fdc7b2-1864-36ef-883e-27e19697d63f | -6.7407 | -59.208 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03e7c96d-d82c-3316-99d7-5c8c474b5b02 | -5.0844 | -55.951199 | 2026-09-17 01:22:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 893ef9b6-3b37-382d-8ab2-a894d3d501c7 | -10.8838 | -57.2174 | 2026-09-17 01:22:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e69ed9df-c16f-3101-bce8-9c05748baf2d | -9.0285 | -60.986698 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 763e4fd6-b328-3a49-b879-2cc4c5834088 | -8.5598 | -66.592102 | 2026-09-17 01:22:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8c69136-9157-360c-82d7-9e0edbe92ac3 | -6.6259 | -59.472198 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1739e8e-8259-3c5f-b976-6816d3888847 | -14.4996 | -46.630299 | 2026-09-17 01:22:00 | METOP-C | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bae32722-6ed1-39ed-839d-2144b5bc0840 | -10.7964 | -54.065899 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e14a94da-810e-32fe-8449-2e832f30779e | -9.2086 | -60.641102 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66f5c9bd-1da6-3d5a-9dbe-5c6099917dbb | -6.5097 | -51.117802 | 2026-09-17 01:22:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1afd2e5-f55e-3837-aa64-9f0739719d6e | -8.4132 | -57.647202 | 2026-09-17 01:22:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d63e7d54-e5e4-3f91-bc20-cf30772b238e | -3.4072 | -54.740501 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc2aa573-80ef-347c-bb06-d9c98e61abc6 | -16.2285 | -58.373901 | 2026-09-17 01:22:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 02e5e94d-05a4-34db-a9c9-3923a45c93fd | -10.7573 | -54.118198 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b2be45f-959e-3242-9594-75ece6ad929a | -2.6217 | -57.633598 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae1f8ed-f122-3cf2-b9d8-94ebb58653fe | -12.414 | -50.815399 | 2026-09-17 01:22:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6762c753-0ea9-3251-9865-01f1ef159b5e | -3.2651 | -59.838699 | 2026-09-17 01:22:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d152364-bb9a-3f04-ad75-64876d70ca70 | -14.1647 | -48.540699 | 2026-09-17 01:22:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 80e51f14-57e2-36aa-86bb-4a4500d68b30 | -9.0268 | -60.979401 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8abefc62-c386-36e0-89a9-fb7b2a9f33b4 | -9.3228 | -60.322601 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5796c785-f2be-3d17-84f1-0fc071172414 | -15.3974 | -52.91 | 2026-09-17 01:22:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fb289bca-5c65-30b4-98f4-ba5f4b07fb09 | -6.7375 | -59.194199 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8475216c-d1e2-32cc-a043-10df8b6ce258 | -2.6236 | -57.641701 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ceb6ba63-0e8f-3041-96fc-9bd09c646ecb | -3.0608 | -59.041 | 2026-09-17 01:22:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d18e503e-0876-310f-96ce-9b1ae47aa4b7 | -9.6877 | -60.481602 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf20821d-4183-3a5a-ad8f-b15afa57c4c8 | -10.3239 | -58.325298 | 2026-09-17 01:22:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab0bdb53-c8bd-3ccc-b411-694a31c31df3 | -3.399 | -54.705601 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8414d406-7277-32b0-b710-761c14c3c037 | -10.5034 | -57.714401 | 2026-09-17 01:22:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad98903-4dbb-3438-9a91-d54e6d6fa2aa | -9.0203 | -60.9963 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e078e5a-89d6-3300-891d-11a012c0a43d | -9.0154 | -61.020599 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa592c21-fafe-38e7-8446-6fc8ff55e6e0 | -15.3988 | -53.803398 | 2026-09-17 01:22:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b678bc7f-46e7-37a6-93d4-022773f68879 | -6.6107 | -58.866501 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 957c98f9-bb93-3891-8822-4db0f619e9f0 | -12.4276 | -50.828201 | 2026-09-17 01:22:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b39425f0-b198-3f83-a6c0-ffa8207c2bda | -9.2102 | -60.6483 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 494730da-646a-3e0b-8951-6c1010fb8325 | -9.3114 | -60.317699 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70900964-e96e-3523-90c5-d44af8d82da5 | -15.3999 | -52.9203 | 2026-09-17 01:22:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b6808fcb-5c3d-3e70-9f73-df0d417cdfbc | -1.5471 | -55.582199 | 2026-09-17 01:22:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6059cb35-a531-3953-a8ab-440e0772e980 | -9.3323 | -60.365299 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 665638ca-b934-3080-bc6c-613fc651fac4 | -10.3255 | -58.332298 | 2026-09-17 01:22:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e50f0332-9507-33fe-84c2-c49a0becf546 | -1.5446 | -55.571301 | 2026-09-17 01:22:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6a9a11b-6d2b-3088-8d1c-4cf54c58ac69 | -12.0683 | -57.205502 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e529e356-0614-3ca3-90e0-257b508f7cc6 | -13.3201 | -57.0387 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bcd31189-631b-3b5c-aa7f-67d28fa317c4 | -10.7793 | -54.123402 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71d2836a-e2b4-3966-b74c-ecaa4386d1c4 | -9.0187 | -60.988899 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42f37578-0fa4-31d6-b240-dd0690901adc | -9.313 | -60.324799 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e5f26be-bfb3-35e5-9ac3-46eed9c2e0e5 | -2.618 | -57.617401 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cc9485f6-9d37-361d-8b6c-48ade4660fa9 | -6.8628 | -63.040798 | 2026-09-17 01:22:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5c83991-a678-30b9-bf2a-c20372e19088 | -3.4142 | -54.7267 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bdb014e-de81-3a86-90bc-85b032cbe856 | -3.4087 | -54.7034 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c113e790-e4c4-3402-acba-58d9edbe9ac9 | -10.8073 | -61.409302 | 2026-09-17 01:22:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb8cedbd-6b48-361d-a183-f4e9ff3d1690 | -12.039 | -57.212399 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f3ca473-8d60-35ae-b2dc-7871eec21a7e | -6.8511 | -63.034401 | 2026-09-17 01:22:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 318c08bb-514e-3af8-b3c4-d0f038f8c65a | -9.6975 | -60.479401 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f643592e-40e2-33dd-a561-43a8890ad2ff | -6.6275 | -59.479099 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9de526a-36ae-34f7-9862-fedbb8b66896 | -10.6305 | -54.191601 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be515bbf-bcea-33f7-aff6-ec47586b961b | -10.7768 | -54.1134 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d58f96e-8b66-33a4-aa59-9ac90e8d8c24 | -3.4045 | -54.728901 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18e59bca-c7eb-3db9-a1dd-3dc7a38a0753 | -3.0592 | -59.033901 | 2026-09-17 01:22:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5a21510-955a-3137-8284-d8be503c25cd | -3.424 | -54.7244 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b063dd9f-ac3b-392e-ba7f-c9da6b40d730 | -8.8094 | -62.414902 | 2026-09-17 01:22:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| afc9c9da-33cb-3208-8f8e-acbfb00e6269 | -9.207 | -60.6339 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12528f70-ef32-3d3f-a91b-f7f1baa8ddf9 | -8.4199 | -57.676201 | 2026-09-17 01:22:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 403d82f5-2750-3e6e-b19a-d3001fcd377f | -6.7705 | -62.902199 | 2026-09-17 01:22:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05a2b3dd-9775-396e-8647-ea4aa8b401ad | -2.4093 | -54.6964 | 2026-09-17 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77b9fbea-6ba0-3426-8872-16abf019194f | -9.0073 | -61.030102 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 488d21bf-9b3d-36a6-9a3b-a51186bf6e05 | -9.5144 | -60.535301 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bdeaa04e-ec44-3040-b365-b0461e7a2255 | -9.3398 | -62.729801 | 2026-09-17 01:22:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23a1dd17-46fa-35c1-beb4-ce02fe115138 | -3.4115 | -54.715 | 2026-09-17 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb7e6560-fecc-31bb-9ac7-1a8618e7795a | -10.7598 | -54.128201 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 928af5fa-210a-39c4-ba7e-d476e856e688 | -9.1051 | -58.319099 | 2026-09-17 01:22:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4597ab61-1158-3c6e-8317-5e965e78c36d | -21.390499 | -48.705502 | 2026-09-17 01:22:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README11.md)
