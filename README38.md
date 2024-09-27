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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 447d543f-a45b-36b7-8c7f-cf4ae64b7bf8 | -10.6452 | -45.8635 | 2024-09-27 01:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 04499766-058a-3d34-8172-949f7bc42b14 | -10.6639 | -45.8838 | 2024-09-27 01:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 05a6d874-bc29-38cd-b394-76e1edc87766 | -10.6643 | -45.861 | 2024-09-27 01:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| dacf5b3c-9bd8-347c-98bb-65ff2b167de1 | -10.9264 | -54.2692 | 2024-09-27 01:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 254.3 |
| b89971bf-0ff3-3826-b164-3f5771393739 | -10.9267 | -54.2488 | 2024-09-27 01:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 266.4 |
| e69378ac-4ab6-30e4-9df1-f7adf5f606a8 | -10.9453 | -54.2676 | 2024-09-27 01:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 0cf31e47-ed52-30fc-9831-0ea6fb6b1ffe | -10.9456 | -54.2471 | 2024-09-27 01:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 41a92daa-92ed-3906-953b-671ba1bf9415 | -11.1219 | -50.8328 | 2024-09-27 01:36:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d6d01e4f-10a9-3fbd-a781-cdad6a53090a | -11.1409 | -50.8307 | 2024-09-27 01:36:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ee0d9741-1fdc-3410-894e-ab5689808f32 | -11.2034 | -54.7752 | 2024-09-27 01:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6ee98fca-980d-39e9-975d-eee75e4e0a77 | -11.2036 | -54.7548 | 2024-09-27 01:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9a054cee-46b5-3137-a381-bc712cd1cbff | -12.1863 | -50.7981 | 2024-09-27 01:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| eb6a34ee-978b-3d47-87d6-9aa7b256e40a | -12.1866 | -50.7767 | 2024-09-27 01:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 13c2c7d2-78f3-3c56-bb24-72486ab475b2 | -12.2053 | -50.7959 | 2024-09-27 01:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 43ea3af3-97c8-3641-ad7d-b17b4b433617 | -12.2057 | -50.7745 | 2024-09-27 01:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| d9581d00-64b0-3f02-961c-ad111a160b6a | -12.6636 | -54.6782 | 2024-09-27 01:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 939974e8-f308-35a4-b1c3-17ef829f41fc | -12.6824 | -54.6968 | 2024-09-27 01:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 97116e03-11f2-3633-9382-d3fbc5cfb2ad | -12.6826 | -54.6763 | 2024-09-27 01:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| fd18dc74-2fc1-3a40-8bba-115205916065 | -12.844 | -54.0215 | 2024-09-27 01:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| f04a13e0-9c94-3088-8c9b-2e11038557ad | -12.8628 | -54.0402 | 2024-09-27 01:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 9bc38154-3b44-3976-952c-683e23c136a4 | -12.8631 | -54.0195 | 2024-09-27 01:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 95eb264d-6b31-33ff-a03a-1252849e7d73 | -12.8634 | -53.9988 | 2024-09-27 01:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| ec980ff5-868d-32c6-95d0-7bbad1010f24 | -13.4413 | -44.0267 | 2024-09-27 01:36:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 1850a8da-c7e4-3d52-b0be-869b33da9dcc | -14.7109 | -45.5096 | 2024-09-27 01:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 5b1785ab-f5d3-3f04-9fe4-33ce7828f4f1 | -14.7114 | -45.4863 | 2024-09-27 01:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 37029c14-b0ac-393b-9c4a-8dda2120741f | -14.73 | -45.5294 | 2024-09-27 01:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1e23d52f-81cb-3e0e-bbab-001fae925e5c | -14.7305 | -45.5061 | 2024-09-27 01:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 405.0 |
| 1b943bc1-a864-3860-a449-5b6f951a3fc8 | -14.731 | -45.4827 | 2024-09-27 01:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 49a9c7b3-3b56-3d67-980f-00c044016bb7 | -16.8367 | -47.7348 | 2024-09-27 01:36:40 | GOES-16 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| ec3fc583-b877-3f14-a5c5-c530f259e63e | -18.4052 | -51.9684 | 2024-09-27 01:36:49 | GOES-16 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d70a6301-55a4-3d1c-a1d8-566d6ba14147 | -18.5944 | -48.9816 | 2024-09-27 01:36:50 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| af12c873-fdfc-3bd3-9585-2a377f1cf1fe | -19.1077 | -43.4466 | 2024-09-27 01:36:51 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| de08d2a5-418a-343e-8943-8f8ad4e60557 | -19.3773 | -42.5809 | 2024-09-27 01:36:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| d33d0ac5-827f-3736-95c3-fc9130a84b6e | -19.6136 | -42.8159 | 2024-09-27 01:36:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| 1f46ae02-5e55-3aa4-910b-736692add0e8 | -21.0986 | -49.1347 | 2024-09-27 01:37:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.7 |
| 4b18ef61-7f79-3895-b320-63b216dd2f05 | -21.4123 | -42.9778 | 2024-09-27 01:37:03 | GOES-16 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| 25d1cc09-3938-3708-9aa9-c0812744ed58 | -22.7433 | -44.8035 | 2024-09-27 01:37:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.3 |
| baf95084-ef8a-3b62-9543-818e809bb151 | -22.7442 | -44.7785 | 2024-09-27 01:37:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.8 |
| 0f814f82-d353-3033-8f36-2210c938bb57 | -22.7645 | -44.7973 | 2024-09-27 01:37:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.9 |
| 4e0c4eff-a484-3732-adaf-fc9259cff80d | -22.7653 | -44.7723 | 2024-09-27 01:37:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.1 |
| 3ad091ce-e89f-346a-bb59-d8ce605513d1 | -23.5816 | -47.3408 | 2024-09-27 01:37:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.0 |
| 31701bd4-db81-39b3-86dc-707db22ff229 | -2.6783 | -57.6087 | 2024-09-27 01:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 4e79ca78-7793-311d-b20f-dbba006b8a65 | -2.6783 | -57.5893 | 2024-09-27 01:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 8eb528a1-0c11-3790-a4ff-06c04935b21e | -2.8611 | -51.6699 | 2024-09-27 01:45:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 70fb240f-3ef4-3869-9a50-be09b008eef2 | -2.8795 | -51.6695 | 2024-09-27 01:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 567830d2-1e80-3f99-9ca1-57dd7233774c | -3.0107 | -51.0652 | 2024-09-27 01:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 766fa84e-ac1d-303a-b8cd-4cbc2a7a80fb | -3.2136 | -46.7843 | 2024-09-27 01:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 82b11138-7398-313b-a66b-1ea09e79f563 | -6.8927 | -59.6475 | 2024-09-27 01:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| eaf56cdc-7214-3f0b-9903-18eb6196f2e5 | -7.0912 | -46.4412 | 2024-09-27 01:45:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 8d0abc44-7398-3e0a-b72b-131666348680 | -7.2006 | -60.6706 | 2024-09-27 01:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 02352e1f-a9ac-33f8-9e97-28411073bc36 | -7.2905 | -61.106 | 2024-09-27 01:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| b254b8d4-1e45-3be5-8523-e42db435c1ac | -7.2906 | -61.0869 | 2024-09-27 01:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| daf67379-0763-3d76-9189-fda47ac385a5 | -7.3089 | -61.1053 | 2024-09-27 01:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c6852667-9d7c-3017-8291-d643d612824f | -7.309 | -61.0862 | 2024-09-27 01:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 3b4cb277-e050-3e32-96df-677455a4645f | -7.327 | -61.1808 | 2024-09-27 01:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 2e627e53-b002-306f-a6ea-45de1df8b28d | -7.5289 | -61.3825 | 2024-09-27 01:45:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 15a2e4c7-8e04-37ca-8a18-34e13bfe8a41 | -7.7515 | -61.2023 | 2024-09-27 01:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ffb8f8d1-0d89-315f-99a6-a0b14f59f013 | -7.7516 | -61.1832 | 2024-09-27 01:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 620d0ce5-b2ee-3089-ae67-49f0ac09c39b | -7.77 | -61.2015 | 2024-09-27 01:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| f3984b36-eb87-3b51-9bd6-0cde55eb7792 | -7.7701 | -61.1825 | 2024-09-27 01:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 190.8 |
| 9f3632f3-f3a6-32f8-99ea-46fd83b499fe | -7.8156 | -54.7252 | 2024-09-27 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| ae6bd2c1-9cbd-3a97-b531-d8511b2a8315 | -7.7885 | -61.2008 | 2024-09-27 01:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 154.7 |
| e5393b0c-6051-3455-a684-14d47db1ee4d | -7.7886 | -61.1817 | 2024-09-27 01:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 215.7 |
| fa24dc98-57a5-3e71-a399-9793364d0df4 | -7.9174 | -61.2909 | 2024-09-27 01:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 088a35f7-fb6f-33a2-81c7-91a420be34ea | -7.9175 | -61.2718 | 2024-09-27 01:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 429415cf-102a-3066-9763-32d2a1bd5bac | -7.9359 | -61.2901 | 2024-09-27 01:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| af7af41e-1a86-39b6-b5e8-531826e3e266 | -7.936 | -61.271 | 2024-09-27 01:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| adf2d41f-2d10-3552-9c61-3463f2b9d4ae | -8.1394 | -61.2817 | 2024-09-27 01:45:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 02449dfc-9334-32eb-a3d3-039e49953c0d | -8.556 | -49.6112 | 2024-09-27 01:45:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| e708777b-93fe-3d4a-9749-871c44709546 | -8.61 | -63.1415 | 2024-09-27 01:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 1d619858-f580-303d-8c20-3d2d21d56f90 | -8.6101 | -63.1226 | 2024-09-27 01:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 50634418-33e8-309a-86ae-5546d44baa23 | -8.6285 | -63.1408 | 2024-09-27 01:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 187.7 |
| a092f4e8-19f5-3095-a1bf-438b532e0639 | -8.6286 | -63.1219 | 2024-09-27 01:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 277.3 |
| 2b3ae8c7-d70e-3b26-9406-8b4097216d90 | -8.6287 | -63.103 | 2024-09-27 01:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f09c84a1-050b-3048-9055-6c745f0cee37 | -8.7032 | -66.9907 | 2024-09-27 01:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 53c059f1-42a8-35e5-9b70-1faf2869c795 | -8.7931 | -67.6921 | 2024-09-27 01:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 04d05fe8-6e5b-35a6-90a7-418ba686701b | -8.7932 | -67.6736 | 2024-09-27 01:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6debd919-1c7c-32a5-9064-17be6f5abece | -8.8116 | -67.6917 | 2024-09-27 01:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 154.8 |
| a363c3e8-cbbb-36b1-a76b-3eca8a2784e0 | -8.8117 | -67.6732 | 2024-09-27 01:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 166.6 |
| e901005d-0bae-3c4b-99af-021504b25301 | -8.8302 | -67.6728 | 2024-09-27 01:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 3c91d052-d35f-3b58-aaaf-5535228ebe49 | -9.086 | -61.1245 | 2024-09-27 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 740be20a-a121-3279-b6bf-dddc6eac04cb | -9.1029 | -61.3726 | 2024-09-27 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| cbcbd088-5b56-3797-8270-7cf426e9d81c | -9.103 | -61.3534 | 2024-09-27 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5ae3ec6c-e2f3-3c3b-9a93-c6fba2197f1b | -9.1215 | -61.3717 | 2024-09-27 01:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 85470b84-7990-3d93-afa2-51b2d26d69fe | -9.1216 | -61.3526 | 2024-09-27 01:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 56255417-281c-35f2-916d-96e986c910fa | -9.1616 | -68.1643 | 2024-09-27 01:45:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8ce4f601-cb11-3451-9bf3-c2b790a63a00 | -9.5829 | -50.137 | 2024-09-27 01:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| fb70cb83-d810-3dd0-bf93-a3e805f18114 | -9.6018 | -50.1352 | 2024-09-27 01:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 7320ca74-d81a-3dd3-9245-3f6896b6959e | -10.3672 | -53.7858 | 2024-09-27 01:46:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 141.9 |
| b50662a2-357d-3fe3-b0fc-4a9379d1e047 | -10.6449 | -45.8862 | 2024-09-27 01:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| abfc3c01-f842-3baf-bbaf-b9842cf87166 | -10.6452 | -45.8635 | 2024-09-27 01:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1952a256-4136-38dd-a24f-7f364cf5f20b | -10.6639 | -45.8838 | 2024-09-27 01:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b7839bea-a89e-3f26-9254-92062c6e9384 | -10.6643 | -45.861 | 2024-09-27 01:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| db55a57e-0950-39d5-8100-d51cd49425d2 | -10.7211 | -51.0869 | 2024-09-27 01:46:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| f6a60484-0b78-3bf6-a010-507ca9cbe71b | -10.9078 | -54.2504 | 2024-09-27 01:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| dc0a1e23-0ff9-3707-beff-6f04e3440576 | -10.9264 | -54.2692 | 2024-09-27 01:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 221.9 |
| f0790001-879f-39da-9a95-9243e8f5ea08 | -10.9267 | -54.2488 | 2024-09-27 01:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 260.0 |
| f70bffc3-64d3-3b8a-9c3f-2eac6884a533 | -10.9453 | -54.2676 | 2024-09-27 01:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| d3bed0e9-9244-3484-ae53-c569690d3ad0 | -10.9456 | -54.2471 | 2024-09-27 01:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 4a4d3b75-844e-31cf-8277-a7e7081cc6cc | -11.1219 | -50.8328 | 2024-09-27 01:46:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |


[Clique aqui para ver as próximas entradas](README39.md)
