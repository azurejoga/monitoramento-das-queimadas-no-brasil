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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae570c51-c918-3e45-bbba-90d3df0bf879 | -4.00155 | -51.03062 | 2026-09-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfcaf7b5-525b-3729-b849-9637c1076ac4 | -2.72764 | -57.61866 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| caa13fe6-248f-31cb-b7d8-1519d0385479 | -3.98281 | -56.09225 | 2026-09-10 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c0338c2-a9f2-323d-a20a-263ecc199232 | -5.75808 | -45.09277 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 052e1338-9e8d-3b80-a301-dd00318f22e0 | -9.04041 | -65.41187 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4b52220b-1ba4-3fad-bfe3-d49f14eb73ec | -9.0894 | -59.46832 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a233845f-cc21-35d0-9a48-f0e8faa17be4 | -10.67724 | -45.99085 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e7fd84b-6626-3824-9c12-142cff53320f | -9.22163 | -63.64058 | 2026-09-10 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8edff38d-5de2-3c5d-b39e-99b89851ac98 | -10.86141 | -60.82537 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b6dbc47-c501-3873-9953-d59ae0458e43 | -11.06996 | -54.51272 | 2026-09-10 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83d1ac21-e9e6-3bcb-a54c-bfe074f6325b | -8.88948 | -61.44597 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf3909c9-8822-3043-a7d3-4b79066b7c74 | -8.9961 | -60.58195 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5834bb64-8814-3804-babe-8ffde04a5bcb | -8.90179 | -61.43929 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6f31a0e-1cff-31b4-a65f-9d0a4b63cfed | -10.77271 | -45.96177 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a289518-7590-36ab-bc78-a5c10152a2c2 | -9.92743 | -59.61082 | 2026-09-10 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c763906b-eb54-3490-be8e-ed61f8c91b09 | -8.82376 | -62.48706 | 2026-09-10 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 587d761c-3e79-3f1a-bfb3-fe579b92c570 | -12.35349 | -48.20264 | 2026-09-10 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47f05fee-3ba1-303f-9bc1-119614d375bc | -9.21623 | -63.64742 | 2026-09-10 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6543aea-c2df-346c-9993-8edb5064dffc | -10.4972 | -59.60381 | 2026-09-10 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e60703e-387e-31d6-820d-2e73c4cc0af6 | -12.35428 | -48.20349 | 2026-09-10 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1678e4b-afb9-3194-b41a-2c75f870b589 | -8.36312 | -62.92722 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8b49b1b-02fa-35f3-a6e3-518f5e229841 | -9.15077 | -60.26434 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00933beb-de92-3d8e-8bdc-1d24bf749588 | -8.62743 | -66.50937 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15cb05c4-9149-3c51-82cd-cfdc73835539 | -11.86915 | -44.84785 | 2026-09-10 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d95f6ca-f836-321d-9340-ec5e703116a2 | -10.85669 | -60.8325 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8177a121-86bd-3d45-acbb-63477eea0675 | -9.04506 | -65.4127 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d7b10e2d-a1b2-345e-a97c-dfda473f5149 | -9.14136 | -64.40758 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d392a0f-426c-347f-a588-a25137d25c60 | -10.85543 | -60.84024 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5c63acc-04d8-38e1-a94d-884cbd7a443e | -10.18981 | -68.76945 | 2026-09-10 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08a4d7e0-911a-3493-9e2e-c39b1c4999fd | -10.86487 | -60.82595 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 877b1929-f99d-30d7-84dd-756047b0bf82 | -8.90771 | -62.36275 | 2026-09-10 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffe4dc3a-2c06-33b5-86c8-957ea1372184 | -8.99589 | -65.41929 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53052099-519a-319a-94a9-4bf8ac89af11 | -8.89231 | -61.42895 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efddcee9-d774-3738-baf4-5e72527a3d9f | -10.77202 | -45.96767 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83a365a2-5b7f-3ce4-99c8-49248ca31acd | -10.66998 | -45.99581 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a2a53d6e-b6dd-3c01-acbc-342512d1d036 | -8.06163 | -61.27506 | 2026-09-10 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72c112e0-b237-340c-a35f-e9d250c1ef0b | -8.98812 | -60.57734 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e640b00f-8ad2-37d3-a0c9-163e9bfe1f47 | -8.92449 | -66.85708 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba49ad94-cad0-35e9-98bb-16e3ec94a532 | -8.89301 | -61.42471 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61b76b88-13ca-305a-9e13-0aa9aa915654 | -8.68365 | -62.46127 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0bf0cd1-0e9e-3d1e-a94f-3cf1107e5b3c | -8.35913 | -62.92655 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd1befb3-7214-383a-a17d-ea23d780f680 | -8.2199 | -62.81623 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4eebb5d5-3f77-394a-8265-6293955b6aad | -9.15189 | -60.36161 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aae5afca-9a28-3a8f-acb0-14f383bfd374 | -9.25755 | -60.93221 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcbde7c8-4282-3d24-ac56-1fab4aabd264 | -10.75093 | -60.70515 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f65868-e69d-3a7f-99fe-ccbe0618b6d7 | -8.62611 | -66.51045 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec2d67da-6d2d-38cb-bade-f62093c17548 | -8.76063 | -61.40852 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5344561-62bf-37bf-a546-418060140538 | -9.22448 | -63.64883 | 2026-09-10 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaa3db2c-d08d-32f7-abc1-6901058b7b60 | -9.93078 | -59.61136 | 2026-09-10 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b822fd3-0755-39e8-b426-d766e49d81d8 | -8.6875 | -62.46192 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0dbe6d1-ba10-33f1-9df6-ea515841b62c | -9.20416 | -65.77712 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c19a9e3f-4d68-3a9b-9044-0c961e596cc3 | -10.07626 | -45.48508 | 2026-09-10 05:12:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 383b89d5-cd6b-3aad-86f5-957d1697965e | -9.23742 | -65.59357 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 121ccdfb-6466-3894-807a-b3c5642855aa | -8.90542 | -61.4399 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eaf67aa3-4ee7-30c0-bdb0-c4c287dc12e0 | -10.75438 | -60.70573 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ee99d27-1938-381e-8174-ce8e41e66d24 | -12.35396 | -48.19839 | 2026-09-10 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc919763-4093-3527-b09d-ffb541974b4d | -10.4131 | -57.21912 | 2026-09-10 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10bdcb94-1970-3ec2-ac73-448a392b668a | -10.85606 | -60.83637 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb6938ca-0c0d-34eb-be2f-0866ad905ab6 | -8.98627 | -65.39214 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b676b582-0157-3472-84df-bda8e8d7d9a6 | -10.16047 | -61.59519 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78e5c457-3aa2-3411-a02f-7cef6e945e62 | -8.68448 | -62.45642 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23e92b4d-67c0-32c7-bb51-34b016412f61 | -9.19006 | -59.69217 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12f64235-74fc-3fae-8641-2dac1e8127e9 | -9.08696 | -65.38297 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab8611f5-4db0-36c2-9863-9ca543041c8f | -8.9796 | -60.60805 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df81f9c5-1684-3bbf-a052-21fb493178a7 | -9.92069 | -67.87855 | 2026-09-10 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e54b6fd2-6f4f-3bfe-9e57-87280a982411 | -9.04421 | -65.41763 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f42716f-e11c-3d05-b3da-0796957b0681 | -12.65124 | -47.0939 | 2026-09-10 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c72e84d-759b-3d9f-828e-c200751b24c6 | -8.89745 | -61.44293 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afda456a-5197-3158-a4b7-9a68b5592472 | -8.73224 | -62.38504 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b539362c-7278-3095-9a42-c131c207d919 | -10.7661 | -45.96102 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b572d9b1-5f72-35b3-ba3f-c7ae5d37c10d | -10.86833 | -60.82654 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3da8af64-b453-3b04-acce-238d62aabd68 | -8.89594 | -61.42955 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18c6c069-5c5b-3cb0-91e4-6ca8be90da12 | -8.99448 | -60.58234 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fc29c1c-2737-313e-904d-813f90c0d42f | -8.8916 | -61.43322 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e99c7c5c-550c-30d7-8cd4-5ae6056c8695 | -9.20949 | -64.50671 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eb40c6f-afad-33e6-8e2f-d058f4a99f16 | -8.99326 | -60.5775 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec82f14d-edaa-3ca1-a121-bde82aa580ed | -8.98373 | -60.60469 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cbd11f9-c817-35c6-a3e4-a866d5202c50 | -10.60006 | -60.78706 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7fdbbcf-b982-3760-bfb5-d55ac5f05578 | -8.67979 | -62.46062 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0120e481-8117-3206-8e4b-47ce9a399f87 | -9.1512 | -68.25178 | 2026-09-10 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d685dcc-5e3c-3ba4-ba7e-74dfc43e76a9 | -10.66931 | -46.00154 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a6eae61b-d0b3-3e7f-85f3-1ee84d07fc6d | -11.21737 | -49.93892 | 2026-09-10 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d63a84be-7db1-3421-8d22-22c3bb48840a | -8.98659 | -60.60917 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b6ae1c4-ea8c-3d26-9a70-d115b47033f0 | -10.73307 | -45.91512 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a7cff89-55c1-3aa5-9b43-419fb0fd9661 | -12.77629 | -48.68503 | 2026-09-10 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9448e22-1aa5-3610-ae33-5ce495cf5d7f | -9.04361 | -65.41075 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ca0040c0-9fb5-3cba-b513-a34270d7ab1e | -10.0709 | -45.4724 | 2026-09-10 05:12:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9cdad99f-1c74-32ed-89da-b6a32f3911ec | -9.12448 | -67.84026 | 2026-09-10 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92f068a1-8ed0-346e-8df5-aceff537a69c | -8.99122 | -65.41847 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b261a10-f34c-334c-b46f-d8b94ec75eb9 | -8.89089 | -61.43747 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 872ab817-9bd7-394e-8918-6e95c8d8207a | -10.06459 | -45.4679 | 2026-09-10 05:12:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 261bb7a8-8766-3e40-86e5-f9a905e39873 | -8.15472 | -62.89798 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 374c8913-12ac-3845-8b87-dee374de0b06 | -8.9831 | -60.6086 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a28066db-c7d6-34bf-8454-e7b4fec3bc4a | -8.89523 | -61.43381 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 977f1a71-0370-33dc-8e5a-eb0c05a4bab5 | -9.04887 | -65.41846 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a57a7b7-c293-3f16-9256-d06a22ed742d | -11.41947 | -62.10576 | 2026-09-10 05:12:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f73f820-cbcb-3622-aac5-f65ac69716dc | -8.82763 | -62.48769 | 2026-09-10 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e1d2602-faee-3676-86ba-6b33e742e6f4 | -10.86015 | -60.83307 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0d1d9732-622d-3280-887d-c47d33927e7f | -8.06527 | -61.27565 | 2026-09-10 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f844c72-f4df-3aa6-bbf2-2b4ec927827a | -8.78617 | -63.82685 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README34.md)
