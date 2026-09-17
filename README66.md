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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 417c1c92-45d5-3f87-9a66-81d1501a1c31 | -9.85746 | -48.3882 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 278886c6-2db4-3a38-8f27-8d292e6289b0 | -3.54229 | -55.47217 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fef5635-8991-396a-be31-ff3a8e673b46 | -3.47321 | -54.69276 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68f30532-1d70-3bb3-8138-d724aff2177e | -2.95613 | -50.31773 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c594643f-f150-3039-856c-20f432850ad8 | -3.47599 | -54.69675 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb0ebfd6-699e-377c-9ac2-0d3a179ecbd5 | -8.49318 | -57.64298 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcdff8b9-cebd-356e-a550-14c05a9ca9b4 | -2.96235 | -52.15712 | 2026-09-17 05:16:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40589771-8107-3b19-bf81-31cd8595d7a7 | -8.86003 | -46.98637 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cc434a6-7819-3366-8fd7-6f58a66c168e | -7.94328 | -44.82811 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 26876a1c-212b-337f-9679-c9affe734e0b | -3.47932 | -54.69727 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7592b49c-8901-3315-9620-f33fc13b04bd | -1.81401 | -54.93434 | 2026-09-17 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 683561af-2063-32d3-abcd-373d26d2119b | -7.0938 | -43.47019 | 2026-09-17 05:16:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1751047-6439-3b38-a8e2-c0297211010e | -6.79506 | -58.79236 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86325d75-5c6f-3540-93b5-1f76ff3a6fd8 | -8.49377 | -57.63934 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fbd69e8-f0e3-35bb-8ae1-f4c89cc07701 | -5.64711 | -44.80636 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63d185f6-3c9e-38ff-8a5d-d86e7f0dfb41 | -7.6527 | -45.84369 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2558ef7-3f5f-3969-9790-1cfb629b53d8 | -6.76204 | -55.84394 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a0b6224-ef40-3dcc-9cb3-5f9be28c7a6d | -3.8133 | -58.89817 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e982675-353b-381c-b61b-0d2b9c46d352 | -9.12368 | -45.73207 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8d92829-dbd5-3768-bc4a-c529161bbec6 | -6.34951 | -51.77771 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d3d575d-ed27-3d4c-82fd-c0237cae3265 | -9.87335 | -48.38409 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0742707d-570c-3356-978e-f0e301aff84d | -9.61557 | -45.35375 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74bd236a-47b9-339a-ad28-7b0a91d6b0e9 | -12.85321 | -44.39452 | 2026-09-17 05:18:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c61eecf-4239-3d2e-86e1-fb26db19d103 | -11.89027 | -43.82358 | 2026-09-17 05:18:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b0f2386-6734-3379-9a8c-6495204416c3 | -14.22443 | -48.5126 | 2026-09-17 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 08ae615e-a874-3599-ad03-7873eb121a0d | -7.79543 | -66.91741 | 2026-09-17 05:18:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39102600-2845-3ba1-b7d6-372f4a5c0b01 | -14.22975 | -48.51304 | 2026-09-17 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdedc91a-3772-33a0-aa1b-a21d24d5f66c | -12.41632 | -48.48353 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 265620e8-5a81-3d11-88aa-be0e2137501d | -14.55555 | -46.60264 | 2026-09-17 05:18:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 652acebf-b6ef-3de0-9f21-b6c8efac7884 | -13.75428 | -48.80083 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f050f43-6fce-3adc-92a1-b47cacba2356 | -13.74854 | -48.80493 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92789e07-785f-35d6-b784-8338f70dddac | -8.64392 | -66.58304 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75b59002-8290-34b4-9dfb-dc509148e49a | -10.57466 | -57.68963 | 2026-09-17 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e73feb7-41f5-3b56-8685-333572d6f834 | -13.37685 | -57.02357 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 743368b6-2aba-3ad3-9cbc-2be28a0b7ecb | -9.0947 | -60.99414 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ffeedcf4-09c5-3fcc-88ef-02305a4102cd | -10.14576 | -61.17867 | 2026-09-17 05:18:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ab4aaa7-7430-3d12-9f47-f2e1b837fa06 | -11.58132 | -46.88693 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ec03b3f-e55a-3f10-b1a4-e941ca68ea3d | -9.09904 | -60.96925 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7365bb38-2911-32c7-b260-36acb298d9f5 | -15.46588 | -53.77913 | 2026-09-17 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baad9e2c-e659-3fed-87c6-1e85b32e4a7c | -10.82309 | -46.17693 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13205677-639e-3c23-960d-8069ac5d6cee | -12.44537 | -50.84069 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2428e7d5-d9d4-3b2c-bf28-f40a21a99c8e | -11.1356 | -49.04496 | 2026-09-17 05:18:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fd21ac0-18b1-3646-b953-6d0e7b7f35bf | -9.86284 | -60.29226 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9111e97e-1a95-3ca5-80ac-97a696d35c06 | -10.81151 | -50.83896 | 2026-09-17 05:18:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b95c062-7957-35ea-82d2-81a8fa861296 | -15.46282 | -52.89365 | 2026-09-17 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61465ffc-3436-30ce-aadf-a9092bebcc68 | -8.64442 | -66.57679 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7934a4d8-dae5-38f2-9a23-df5ef02797ad | -12.41115 | -48.48283 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ff9f3878-16cb-361f-ba43-71603ff1755f | -11.13867 | -49.04081 | 2026-09-17 05:18:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55f25198-2d2a-32a9-b8a8-dc6cf822ab25 | -12.10238 | -57.19466 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c96c2144-9af0-339a-9501-ca87f5145885 | -12.75445 | -52.83751 | 2026-09-17 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 166a9884-c877-38ed-a335-2b1e1d9b58b1 | -9.91055 | -57.06168 | 2026-09-17 05:18:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 222a0a66-c8c0-32d7-90a5-7cf56056531e | -12.44653 | -50.83202 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 15aa5ff8-13d5-3b26-a27f-1ff3317b5ef7 | -12.43447 | -50.82147 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 9a5cd865-4b36-35da-842c-463d43e79e98 | -9.10078 | -60.95931 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1df667d-ffe0-3abd-8115-05d113012b29 | -9.62049 | -61.81817 | 2026-09-17 05:18:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54447116-906f-3a23-9e48-53914f1b8a13 | -11.53108 | -46.86086 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab235115-dd3f-30ed-bd1e-ac9290f4e9b0 | -9.40794 | -62.70784 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e541bf48-09b2-3c24-aa55-c9a3f219f7d4 | -12.75335 | -52.84058 | 2026-09-17 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e590bca1-97e5-34eb-9ff0-a6aad8975fb0 | -15.63765 | -52.73056 | 2026-09-17 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86b60951-d3b4-3c40-b19f-ace81378c2df | -11.61284 | -50.62805 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3966a0ac-fecb-3b26-877b-34e91a4563eb | -12.45768 | -50.74905 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 759ce84c-9018-3cf0-9318-3f14c5faec32 | -11.58701 | -46.88764 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69ab6df6-0886-30dd-8e0f-5ccfdcd75b90 | -9.86132 | -60.29414 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d31587a8-7c8d-3657-a178-a856f39b48f8 | -12.45266 | -50.75282 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9dff1edd-5cc7-3f60-bf07-b5501f887e23 | -12.31219 | -47.9607 | 2026-09-17 05:18:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 477cfc55-0230-307e-aeca-65e00bfe0a6f | -9.09351 | -60.95602 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02e734d2-2fa4-31bf-b2aa-d2b3b25ccc80 | -12.43771 | -50.83077 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 04d267ca-0c69-3adf-b85e-9cd3ddee2584 | -10.83366 | -46.14049 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24c2568d-8436-3937-bfd4-9d5dc503008a | -10.52843 | -57.45232 | 2026-09-17 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60ba879e-dcad-34da-975b-87bc9ff9468e | -10.83265 | -46.14854 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e79fbd9-ee30-33cb-8baf-f194868c02bf | -11.33168 | -46.77093 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 760a10d1-e269-39ce-83fe-433ec1b84b8b | -10.82898 | -46.17775 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1590838d-4b01-3081-a127-a5521c6a658c | -12.41471 | -50.80093 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb57cde6-e3c4-3f25-9411-4b9d70418319 | -8.64298 | -66.58466 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 564fedc0-1b9a-32df-ad2a-f0c7e41bf164 | -11.32461 | -46.77205 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78b96394-a6d6-3e09-8430-c3d1832e35d7 | -10.8359 | -46.17036 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f5a5995-e717-31f9-b016-84c79296b248 | -9.07335 | -61.00394 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8b3dbb1e-a851-3b7c-b801-909f985a571d | -11.31807 | -46.78756 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a37683a-7f8a-3a35-9915-b2debcba3a24 | -12.42123 | -50.8196 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb82a6c3-b127-3542-9550-712e52e07db0 | -11.20836 | -42.82643 | 2026-09-17 05:18:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| cdb388ee-fcdd-3f5b-9d81-fe2722bcc47a | -9.28767 | -60.61994 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60c630bb-4622-3c88-aa6d-4034dc9b2326 | -8.64467 | -66.57912 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0573303-2430-315e-bc31-2e94706ee9fe | -12.11662 | -57.18594 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e5fcd27-710a-3a31-97d1-e024bfe76488 | -12.95263 | -48.61734 | 2026-09-17 05:18:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38ed058c-41cb-3201-aec5-93cba3fc385e | -12.44562 | -50.80531 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92f38556-7078-37f5-bb60-49799899bd95 | -11.80593 | -58.17648 | 2026-09-17 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 7f9bd2f7-0122-32c6-9119-c73a651eecb8 | -11.53574 | -46.88184 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ad355d8-3dd0-3234-866e-34b35e08f6e0 | -12.44212 | -50.83139 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 107934a5-0e1e-3721-9089-b16746ce57a7 | -12.4197 | -50.7972 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f82c4aaf-12a8-3d5c-9b4c-78bcda87eb72 | -10.65595 | -61.75332 | 2026-09-17 05:18:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dde88c79-902b-3ebf-b34d-4b81b88c0067 | -11.89004 | -43.819 | 2026-09-17 05:18:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 990fe48c-712f-3faf-a937-1d607d075556 | -11.8071 | -58.16927 | 2026-09-17 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 3a2e5d3e-2401-33d8-95ae-b444bbafa40f | -11.53055 | -46.86496 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64e82375-423d-3599-8493-5b7defa9be51 | -9.10641 | -60.95011 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cebcffe-38cc-3773-915e-56661dde4aea | -8.87911 | -62.38877 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7d7ae97-2af9-3ba4-8d39-9ef0b2607d87 | -12.11437 | -57.20007 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b409aa0-3c11-3ca8-a571-0e3198ad64de | -12.45858 | -50.77599 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4407767b-7a32-3618-845c-38db403d2073 | -11.88521 | -47.58339 | 2026-09-17 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1cec3fb0-1d4e-3fbd-a3db-3ebdebc7ba16 | -9.09643 | -60.98417 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 412aeb8c-0f70-3abe-bc70-4da02833db4d | -12.43028 | -50.78536 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README67.md)
