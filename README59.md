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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad80ce85-2ad8-3289-8c6b-eb2081b8b4ac | -10.40911 | -53.77688 | 2026-10-01 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6d8ddee-3412-35fb-9f60-077bd460e515 | -8.20105 | -45.49458 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2cb98cf-3874-32b0-aae4-6f688d25a4d0 | -11.78763 | -50.5041 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 86ebee20-d458-33e1-a767-1e0c11ac7292 | -11.16959 | -48.31613 | 2026-10-01 04:34:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 324fcef8-b8d3-3c39-8713-7871a138a9d3 | -7.19117 | -46.50196 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b451ad5-95fc-3db5-bd10-becf6a28a4d7 | -12.50602 | -43.10392 | 2026-10-01 04:34:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f6bf6a58-7497-3189-9c13-a0ec5258dd7a | -11.4297 | -43.41663 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5d3a9f0-15bb-3c58-8be0-99a676519337 | -9.81219 | -44.82316 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a88d95c-0c89-3dcc-8316-b4fd13a7e76a | -7.84876 | -45.81946 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7863f77f-22be-3e33-86b6-569530d7dff7 | -11.41579 | -43.40485 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3f696dbf-7c6c-3548-be19-62fd6749f4af | -8.31478 | -44.16054 | 2026-10-01 04:34:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 391a5550-f38d-3298-8051-45e549413cc1 | -11.3969 | -43.37273 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3a53fc4a-37b0-3157-a671-b5a0cc822d38 | -8.19878 | -45.48696 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd88ee0b-1056-3a1c-9efb-596e113ba260 | -11.1952 | -45.18895 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1af4d3b5-4aed-3580-882f-35a56926f6d5 | -7.45165 | -47.17313 | 2026-10-01 04:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df7cb720-0636-3a0d-bf18-6530b1ff5db2 | -6.69791 | -55.05614 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 028d23a5-c096-35d5-9935-b9feee61da56 | -11.83861 | -44.75343 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0bce09d-bb12-32cc-a2ca-2e9b212e4147 | -10.29682 | -44.65093 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a282e567-ca3c-3bc8-87eb-9678fe710d04 | -8.94482 | -49.786 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ce0a386-5dd3-3843-b418-c5297af51e74 | -12.18979 | -48.43704 | 2026-10-01 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 67ba11d6-bacd-30d8-8d00-68cae58088af | -14.3702 | -44.77656 | 2026-10-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62331b4d-b603-3031-8f0c-cbbb8bf69279 | -7.60543 | -49.5341 | 2026-10-01 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e8f5106-012f-3a4c-bb5e-57f892a58b58 | -9.06488 | -49.87127 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aa44360-cfd3-339c-bf9b-a2200a36275b | -5.86033 | -57.76783 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49568d83-add1-3621-acfc-77d87dcaf584 | -7.78379 | -49.87486 | 2026-10-01 04:34:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad2dc995-9b45-3108-8246-c07e438102a7 | -7.03309 | -50.73277 | 2026-10-01 04:34:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d064cfe2-4364-3cc1-8ead-a80596489d24 | -8.84431 | -50.50514 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 429735b9-6913-30bb-90fd-d32738c9e711 | -10.32519 | -47.45393 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c8999d1-4d37-3882-870e-96630c3bb576 | -9.90073 | -50.16652 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2cd2c93-50f5-35ef-b7d8-c42f24d756f4 | -10.75075 | -50.54299 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2e4043a-4d9e-3fc6-892b-16c4bead7d66 | -7.71584 | -54.80645 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa11c0ff-c5fe-3fd2-a963-856651f0b8fd | -10.77494 | -54.75321 | 2026-10-01 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97596d5f-53ed-3de3-a219-af1e65e78783 | -13.88694 | -44.45483 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcd37bd6-faea-3733-a4f7-e90820f54804 | -9.31417 | -57.71126 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a9b97bb-fa76-37ce-890e-2ac0007a6c41 | -6.66316 | -58.88261 | 2026-10-01 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f5d3ccfb-4382-382b-a2d2-0edf8e83dcb9 | -8.1667 | -47.14137 | 2026-10-01 04:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ff40332-d6a0-3b98-8419-18002b487360 | -12.50895 | -43.10684 | 2026-10-01 04:34:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 23f28a84-37c7-3ced-9209-9818de18408c | -7.50382 | -55.04161 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20326469-7d3a-3751-a96a-90a0f05d9db3 | -11.41191 | -43.48673 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca700d8d-c9df-3b83-bab5-960fd109174f | -11.16673 | -54.11544 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6da1de8e-a508-3cc2-b379-9501a7329e90 | -7.33395 | -54.98449 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15d6c7b0-2073-3124-bed1-18f49b60ea0b | -11.17793 | -45.11404 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 316b6d2c-0a48-397b-b8e5-68b494585be8 | -6.91599 | -51.67677 | 2026-10-01 04:34:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84614b17-9c92-3b56-b49a-e8cfb93a01f0 | -9.79941 | -44.81319 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a5a852c-df84-38db-82bc-f2e8e9ca7350 | -9.90006 | -50.17061 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6cd45a7-31a4-368f-a497-863b7a580df6 | -11.39465 | -43.36976 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ba63ef7-6874-35ca-94c6-95b83a6c270e | -10.8524 | -48.70043 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 432bb42b-04b8-3582-a9c2-fd1e99217729 | -7.55088 | -55.03649 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42e1fb81-0c09-35eb-9f58-4b757594c62f | -7.72276 | -54.79617 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb11a81d-d4c9-3c5d-b608-8beaf9b20276 | -11.17852 | -45.11008 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9c761bc-91b8-3a85-b029-beb73d674c25 | -11.71746 | -43.43459 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a0f5fa7-b114-3a29-a4dd-5b85b9231e4d | -13.67924 | -44.28833 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a47775a-3ba5-3793-939c-284929130fde | -7.49944 | -45.79374 | 2026-10-01 04:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6545e1e3-9ef4-31cc-ac11-ae0e49eaaccd | -11.18489 | -45.11519 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17c24baf-7207-3564-8091-a44870cc5ba0 | -13.53317 | -49.19011 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7ab6c8a-27ac-327e-a8d2-dc0f1e53c6de | -9.11812 | -49.92098 | 2026-10-01 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c19d46b9-232f-3b13-8cb1-7584de4f9a2d | -8.84726 | -50.51007 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a892108-7d1e-30f4-b05d-22eec65e6ee2 | -12.26029 | -54.00065 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13514594-3eba-3621-90a2-ced29304f98e | -7.38545 | -47.01291 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4bd69c1-f0a7-37a0-9298-6bf25cb870b6 | -9.65576 | -45.11826 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 965789b8-63a6-3b06-94c2-9ac38c7090d5 | -13.42993 | -43.81213 | 2026-10-01 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2ab9eda2-a1f4-30dc-9748-a45101df33e6 | -12.37138 | -51.14248 | 2026-10-01 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 369ce187-ef6f-37ba-bf85-81e4337acd02 | -7.34111 | -55.59554 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 333695f7-b4f5-3d41-b9c5-cd082b1277e0 | -12.85673 | -44.33522 | 2026-10-01 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b065a864-2b78-3dbd-b4bf-2add5ef663e8 | -11.51754 | -47.17242 | 2026-10-01 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19ca7622-e0ea-3352-a139-4c3ae0283cbb | -13.33228 | -43.71136 | 2026-10-01 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 569c534d-dc1e-3d4d-8320-dd27fbc653f9 | -8.24486 | -54.6611 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 974a4250-9f18-3948-9e54-fdccbafa6f3d | -10.84847 | -48.70342 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef037fd2-7399-342f-bf66-2d0adcf50a77 | -10.51883 | -57.77503 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a5e2356-c23b-3593-a42b-2369a20c9c3b | -8.88642 | -50.65419 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 766f1a2a-326f-311e-812c-5afbf140aad9 | -12.57832 | -47.16108 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06430c33-0340-35c3-8f1f-13603cf24038 | -8.24147 | -45.43425 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84c68529-9d19-3b40-a6e5-0d4978447a51 | -9.08869 | -45.007 | 2026-10-01 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 8548630f-af79-3c1a-9d94-30ac67612e9a | -9.22648 | -45.84076 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c90e0f0f-d76a-3dd3-af4f-986b473d4af9 | -7.49152 | -54.99436 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b014aab-645f-3e66-88c5-259749bd5ba4 | -5.90937 | -53.49595 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3a7e41ea-e022-37e6-8a59-0c9e87570f66 | -11.223 | -45.19333 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a74667b-7adc-3981-9438-8786475d1203 | -8.79763 | -47.99841 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a6551a9-cd92-31ff-9f57-64107beb1775 | -13.53258 | -49.19374 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad3bc943-ee5d-3f1e-9654-cc7451d9dae6 | -10.7655 | -47.71922 | 2026-10-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 893ed695-c308-319d-a453-82349a5f35fd | -7.95238 | -48.56103 | 2026-10-01 04:34:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07b9041c-5b70-39c4-a374-bb08a99bd182 | -11.46997 | -43.46139 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41728f57-f337-3e6a-83ea-aceda1d038f4 | -8.74256 | -47.8767 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47603f19-8c9f-3092-bd1c-7e9446fb205b | -11.41444 | -43.41437 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 291ffdde-d6a2-3832-9417-1290a454e2ea | -7.38322 | -46.42622 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6694f48b-57a9-3484-b634-5fee7b3a2a34 | -8.19264 | -45.50437 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c5cf8e8-bb60-3993-b7ed-331c3ae998b9 | -12.7119 | -54.06667 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccde98a0-266d-3306-9c6b-90e26e95e2c5 | -11.44292 | -43.43319 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d2bf088-c04a-3efc-9397-46f833d34c76 | -8.20388 | -45.49861 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b12bccc-ccc0-3748-9299-47c67d085e38 | -12.38888 | -54.09634 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b6d5942-503f-31b8-a522-ce6c6bba5d7f | -6.91195 | -51.67606 | 2026-10-01 04:34:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f4ea95b-446a-35c6-a800-7f81b21f69f2 | -11.79977 | -50.51877 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77bc935f-aae3-3e08-a1d1-350dccfd250b | -10.66419 | -50.76435 | 2026-10-01 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 090bf793-7450-326b-b51e-a84f7518b877 | -12.77312 | -54.02271 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c9994d9-451e-3dbe-b401-b97a51d5c199 | -11.71189 | -43.43594 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68b65bb5-0d01-353f-8da0-3efd0f39d8f0 | -7.33944 | -55.60472 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f330f8d5-b98f-3380-b7e3-45da5261068b | -10.32647 | -47.78795 | 2026-10-01 04:34:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d08bdf0b-8e71-399b-8b8e-ad6402904c7f | -11.40404 | -51.02628 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1dfcb0b-ae69-3747-89fe-1b0b17e8a08c | -8.36905 | -45.37954 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50c5b4e6-4548-366d-a11c-0b3a285287b9 | -10.60338 | -48.05239 | 2026-10-01 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README60.md)
