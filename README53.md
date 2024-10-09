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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26b05811-1cb1-3cc2-a6c3-0de09b82206b | -3.9394 | -46.445 | 2024-10-09 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 115.1 |
| d922dec1-22a5-3263-821e-7d0a122e556e | -3.8196 | -41.5979 | 2024-10-09 02:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| c83bf820-3946-3cc4-bc0e-850c5a9f8050 | -6.7614 | -60.0559 | 2024-10-09 02:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 186.4 |
| a9c5664e-6b18-3aea-995a-f11d61721a2d | -6.7615 | -60.0367 | 2024-10-09 02:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 1d1e0914-383b-3620-8cee-97bc947ae184 | -6.7798 | -60.0552 | 2024-10-09 02:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 158.2 |
| e34be342-a1c8-3785-8b52-919889d2206d | -6.7799 | -60.036 | 2024-10-09 02:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d97da777-9710-3c38-b594-7d2e2bb82b10 | -8.4919 | -48.6476 | 2024-10-09 02:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 120.4 |
| df4047d7-cfaf-3d54-b67c-3d43e4072cd6 | -8.4921 | -48.6259 | 2024-10-09 02:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 80.4 |
| cd661744-ccc0-32d2-b675-da6725ebb62f | -10.3655 | -64.8451 | 2024-10-09 02:26:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8f0acaf5-9c92-3cfd-8328-c6e6351fcaa7 | -10.3656 | -64.8262 | 2024-10-09 02:26:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6e98b2a2-1b69-31e5-9252-72f598d688a4 | -10.3894 | -61.2502 | 2024-10-09 02:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 0f20a985-3750-3272-868b-25a339241db7 | -10.3895 | -61.231 | 2024-10-09 02:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d8925975-433f-3d2e-aec0-c8f7558cb63c | -10.3842 | -64.8443 | 2024-10-09 02:26:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 46168e0e-0e37-3854-8274-cd97a6dc1638 | -10.3843 | -64.8255 | 2024-10-09 02:26:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6b2364bd-9be5-37dd-81d7-d2c833bcd958 | -10.4287 | -60.9979 | 2024-10-09 02:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e3d69220-006e-370a-8f5a-cdbb40b28ad8 | -10.6068 | -55.9169 | 2024-10-09 02:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 97e99ffd-4bb8-3520-ad7f-b98fdd3d6b54 | -10.6253 | -55.9355 | 2024-10-09 02:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 6b32fbbc-6daa-3144-9f30-244c602f7a0c | -10.6256 | -55.9154 | 2024-10-09 02:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 04a6de0d-4526-32c8-82ee-cf532f7854ca | -10.6258 | -55.8953 | 2024-10-09 02:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f790953f-8a7a-3176-aa68-696604e514fe | -10.6444 | -55.914 | 2024-10-09 02:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 3341b7c9-07c2-33a2-9d4b-406edfec48a4 | -10.6446 | -55.8938 | 2024-10-09 02:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 1e620f48-8843-3851-be85-73a474d350d1 | -10.8754 | -63.9169 | 2024-10-09 02:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 236e6773-2006-3cc0-a6d3-cbd1086aae0d | -10.8755 | -63.8979 | 2024-10-09 02:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 5ce85095-51c0-3016-85c9-89ae58ae31e1 | -10.8941 | -63.916 | 2024-10-09 02:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1e765d65-b5db-326b-8eb0-d2f5d5b62bf5 | -11.3657 | -51.0189 | 2024-10-09 02:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| ecdf90b4-9111-3293-aad6-34c7cfd65f66 | -11.366 | -50.9977 | 2024-10-09 02:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 582694d7-dcb7-37cc-a030-c4e319ff5521 | -11.5233 | -65.137 | 2024-10-09 02:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 88c185b1-bf66-3eac-ac53-ea97b92ca5fd | -11.6806 | -64.0312 | 2024-10-09 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b159966a-b8a9-3e3d-8de1-76e692d9c9e7 | -11.693 | -65.0163 | 2024-10-09 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 404a5e10-9664-385a-9525-11b784f147a0 | -11.6931 | -64.9974 | 2024-10-09 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ab9bed49-e5c4-3f48-b56e-2163d921d154 | -11.7117 | -65.0155 | 2024-10-09 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 54d5e80f-1adf-3bc0-a1c7-5d8c9b40874b | -11.7119 | -64.9966 | 2024-10-09 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 04992a16-c77b-33e3-b49b-ad0e9ebaad28 | -11.992 | -51.0553 | 2024-10-09 02:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 58f09062-054e-3af1-b27d-49015bf4bcc1 | -11.9923 | -51.034 | 2024-10-09 02:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| a35abb2d-2486-3cb8-bea2-2b41822a70ce | -12.011 | -51.0531 | 2024-10-09 02:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 8e7c4416-bc82-3ddf-a939-839fa289ddf6 | -12.0114 | -51.0318 | 2024-10-09 02:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 77f4001d-bdc1-3745-9c6d-d685af528f6f | -12.6676 | -63.0819 | 2024-10-09 02:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 43d44b9e-fa4b-39c6-943b-45629e53e4b2 | -12.769 | -62.2678 | 2024-10-09 02:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 97f1fb86-bc0c-3869-984f-9d9747ec28dd | -12.8591 | -62.8018 | 2024-10-09 02:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 83284eca-5a64-3290-a2c5-4ad392ef11b9 | -12.878 | -62.8007 | 2024-10-09 02:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 100.8 |
| e9386d84-2728-34dc-b5ef-c60fa7b8369a | -12.9568 | -62.4492 | 2024-10-09 02:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7872002a-f9cb-3a06-aca8-1fc1b86d78cb | -12.9756 | -62.4673 | 2024-10-09 02:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 392f1130-c47a-3d69-924f-26ed07fe6c8c | -13.8764 | -44.5386 | 2024-10-09 02:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f96155c5-ba01-3446-9a36-e7f89ecfcfe8 | -15.5996 | -57.3699 | 2024-10-09 02:26:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 6488f950-1ed0-3e4f-a188-9921d9540630 | -16.4184 | -55.9455 | 2024-10-09 02:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| f7a82c70-36d9-30e5-9b4c-814ff57635f7 | -16.4187 | -55.9248 | 2024-10-09 02:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| b5062071-60e5-338d-9b0a-d8bf299f3215 | -17.0623 | -56.0308 | 2024-10-09 02:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| d5bfb4fa-a54b-3d76-8695-f55216232105 | -17.1467 | -56.8463 | 2024-10-09 02:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| f5f8a662-dba7-3857-acd1-db17fb2410e8 | -17.1588 | -56.1222 | 2024-10-09 02:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| c5fe0118-9c33-3997-a34d-58679fbeb2db | -17.335 | -55.0366 | 2024-10-09 02:26:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 109.6 |
| ec09e3b5-401b-3da7-a4f3-99dc86884f5f | -17.3353 | -55.0156 | 2024-10-09 02:26:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 127.7 |
| c3a04c6e-dbc1-3f57-a91b-6ae51efe174e | -17.3547 | -55.0339 | 2024-10-09 02:26:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 425352b1-d885-37a5-ad74-135338ced9be | -17.3551 | -55.0129 | 2024-10-09 02:26:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 2caf345f-a51e-3bed-be05-29909909c63e | -18.5993 | -57.2629 | 2024-10-09 02:26:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 6759c772-9f36-3bd5-a639-a83ba78da42f | -18.5996 | -57.2422 | 2024-10-09 02:26:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 3e25935a-123a-3fc2-b4ae-468c7dc173d3 | -20.0122 | -42.4541 | 2024-10-09 02:26:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 128.6 |
| 23d4e076-0142-38e5-ba6d-164197232e43 | -20.013 | -42.4287 | 2024-10-09 02:26:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 161.1 |
| 8af7aeec-2a16-3022-9b29-c0af89691c12 | -20.3148 | -48.7121 | 2024-10-09 02:26:58 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 70f6c2f2-1098-32f1-a84f-a9a76a65cbf8 | -20.3346 | -48.7307 | 2024-10-09 02:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 393.3 |
| b0c023cd-77f1-3719-955f-4fbae7f60077 | -20.3352 | -48.7076 | 2024-10-09 02:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 297.7 |
| ba2c2cd3-f5e3-31c7-8e52-2e51968669e8 | -20.3551 | -48.7262 | 2024-10-09 02:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 327.8 |
| 4acb54c1-7498-3e51-9506-585f934d47ec | -20.3557 | -48.7031 | 2024-10-09 02:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 860edc54-8118-3d52-aa41-829a1e847fa8 | -20.3755 | -48.7217 | 2024-10-09 02:26:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7a15eff5-b87a-32d2-810d-b8f381156a80 | -20.7839 | -47.2559 | 2024-10-09 02:27:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5614f522-c58c-328e-a76d-db9fd61ce536 | -20.7846 | -47.2323 | 2024-10-09 02:27:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 857ee6f3-cfc3-34ce-968b-5b798b8d6da1 | -21.0408 | -47.5696 | 2024-10-09 02:27:02 | GOES-16 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 23a773c0-4d8f-3b77-9a5c-dbb88cfe573a | -21.5727 | -46.9659 | 2024-10-09 02:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 93.7 |
| aa266e16-45c0-3e55-9a29-934308430a91 | -21.5656 | -47.8878 | 2024-10-09 02:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 71f6d089-9271-3307-8538-8153ac569714 | -21.5864 | -47.8827 | 2024-10-09 02:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9dbb176c-52bf-35df-b754-6e4d59b748c4 | -21.8172 | -49.1541 | 2024-10-09 02:27:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| 54dba239-09e1-3777-96e6-91cd7114344b | -21.8373 | -49.1726 | 2024-10-09 02:27:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.1 |
| 7b3cbeae-fe9f-36f1-a15a-787a6b8d8223 | -21.838 | -49.1493 | 2024-10-09 02:27:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 212.6 |
| 095aaadb-87cd-343d-936e-9cc59020b8d7 | -22.8137 | -48.4225 | 2024-10-09 02:27:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 14df0802-9ed1-3888-8088-226b6471a68c | -1.11 | -53.6173 | 2024-10-09 02:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 0dc84948-4e44-3feb-9b2c-9e2940806dfc | -1.1284 | -53.6171 | 2024-10-09 02:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2aa5d296-8245-3701-beae-ed9b1904dd3a | -3.8008 | -41.5989 | 2024-10-09 02:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 39b81279-d322-36e3-aab9-1c2ee31fbaa8 | -3.8196 | -41.5979 | 2024-10-09 02:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 6482e754-6a58-3b77-8f5c-2acea15792a3 | -3.9021 | -46.4689 | 2024-10-09 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 54076893-1d80-38ac-87b4-e9fd2ffefe88 | -3.9023 | -46.4467 | 2024-10-09 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 0b71acf0-03fa-33e2-a114-240e4e0df4ee | -3.9208 | -46.4459 | 2024-10-09 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 467627c0-67d0-3068-a201-ed37b2f26b08 | -3.9393 | -46.4672 | 2024-10-09 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| cbe134a2-67ce-30aa-820a-3b7c419ce86d | -3.9394 | -46.445 | 2024-10-09 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| ffc1d4a8-6f43-3b23-8019-b55a5e5baec9 | -7.0016 | -34.9416 | 2024-10-09 02:35:45 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| 5e0d800a-3836-3071-957e-dc331f3e87c6 | -6.7614 | -60.0559 | 2024-10-09 02:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 127.9 |
| b80972b4-719f-32c0-93e8-68c6b6db687e | -6.7615 | -60.0367 | 2024-10-09 02:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| f4f734b5-678d-37cc-91d1-a8b2ca4b2b0b | -6.7797 | -60.0744 | 2024-10-09 02:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 50ae1326-aa0c-34fb-aae2-6793d73c2127 | -6.7798 | -60.0552 | 2024-10-09 02:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 234.3 |
| c7005551-f6ce-3301-abae-d066f0a7d514 | -6.7799 | -60.036 | 2024-10-09 02:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 80565d1b-0729-3b1d-89de-4a52cc253dd5 | -8.4919 | -48.6476 | 2024-10-09 02:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 630d487e-747d-3f26-bb54-0f4d46d0c34e | -8.5107 | -48.6459 | 2024-10-09 02:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d2b90433-615f-3824-8668-599652936b7c | -10.3655 | -64.8451 | 2024-10-09 02:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 7a19cc67-5a51-3c5b-b381-174fa512c1af | -10.3656 | -64.8262 | 2024-10-09 02:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 8441b090-7462-3206-886a-e4f3de402a82 | -10.3894 | -61.2502 | 2024-10-09 02:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| af0c8e28-8e81-36d2-a58d-b8103f416aa7 | -10.3842 | -64.8443 | 2024-10-09 02:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 727fda36-6eda-3024-9e66-c9568601b538 | -10.3843 | -64.8255 | 2024-10-09 02:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 3e826693-6457-32ae-908c-b2e9eba16b5f | -10.6253 | -55.9355 | 2024-10-09 02:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8d4444e0-07f7-3e72-86f9-31038eeea35b | -10.6256 | -55.9154 | 2024-10-09 02:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 7a9869f9-3238-38f4-8605-a5610c51321c | -10.6258 | -55.8953 | 2024-10-09 02:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| da81075c-590b-34de-b5df-9e054aef6029 | -10.6446 | -55.8938 | 2024-10-09 02:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 5e2a958f-eaec-322f-93cb-dcd110388e09 | -10.8567 | -63.9177 | 2024-10-09 02:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |


[Clique aqui para ver as próximas entradas](README54.md)
