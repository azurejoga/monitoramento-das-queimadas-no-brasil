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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b19a7fc1-b483-352d-abe7-70bc0de12048 | -7.23038 | -44.65062 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57a790dc-1bf8-363b-8a55-d3e0b4ad55d3 | -8.90646 | -62.42805 | 2025-08-08 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcdb4fff-66e9-3735-bbce-78100a55cb4f | -9.24885 | -58.75965 | 2025-08-08 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f6685b4-4542-304a-9504-066038c5a19e | -7.25192 | -44.65839 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ac8cd62-1f99-33dd-8418-97928ce85f23 | -5.00667 | -56.03882 | 2025-08-08 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 229b6918-8ebb-36a1-9ac4-80fe8ed8917b | -9.47252 | -57.8462 | 2025-08-08 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1994da6-b79a-3919-9998-423778d07df7 | -7.0486 | -59.18138 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 93d651d2-46cb-3531-a12a-ce2062c1412e | -7.11001 | -44.22339 | 2025-08-08 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6946092b-8122-3e0a-b7a3-9f69001accfc | -9.65212 | -43.85442 | 2025-08-08 04:59:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c3c0a185-9111-324c-91e0-f7e0b915edb6 | -6.09832 | -52.25182 | 2025-08-08 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c681f572-9b32-3124-8e3c-db1687e2e974 | -7.04801 | -59.18483 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 50c98d08-0c9d-32dd-8966-7f5cad02a4d4 | -6.96928 | -42.86979 | 2025-08-08 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 59cdc0aa-8a0f-3f39-b778-bc5939ccf3c4 | -7.89995 | -45.33616 | 2025-08-08 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 548a6b8a-9876-3ea2-a20c-095efb1ee044 | -10.83329 | -49.37459 | 2025-08-08 04:59:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a0e4dd6-9638-307a-a2a9-879fe9ef0f81 | -7.38933 | -44.24448 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6fb289c-03a5-35fc-a13f-5f80c76e0033 | -7.25351 | -44.33373 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e1f56d3-81da-30f4-ac95-0b980b576fe2 | -11.74786 | -44.94771 | 2025-08-08 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de6a6b2b-4f15-3040-95d8-e2a3101e4e26 | -7.89372 | -45.34198 | 2025-08-08 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bb09067-cc82-31a2-8d9f-93a2b373851f | -6.81181 | -44.76386 | 2025-08-08 04:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9b24218-47a5-3bba-a5c9-eb8b9dff79ee | -7.22538 | -44.6553 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b082752a-470f-3ce6-be4f-6da2005cd2c5 | -10.4354 | -44.34565 | 2025-08-08 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70baf785-8506-3ba5-b8c6-17bf35d17f24 | -7.37172 | -44.64542 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d85e9b12-b873-3ea6-a770-3324c5e42aae | -7.37777 | -44.64257 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ce1135e8-8c6c-3302-8e66-1a809595be55 | -11.02577 | -45.07225 | 2025-08-08 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eff5e4f4-9aa3-30aa-b80d-018c7e76ee18 | -11.73874 | -47.50974 | 2025-08-08 04:59:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2418b8b2-8d2d-3896-8c02-c98694712dfe | -7.59877 | -55.20014 | 2025-08-08 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 057a1669-0697-3774-88a6-0319f76150f1 | -11.0691 | -48.35727 | 2025-08-08 04:59:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e99c7fbf-dab1-3e6a-9ace-7a97b71187f4 | -8.9113 | -62.42885 | 2025-08-08 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf1100c9-8408-3f11-ac46-8feaa8c32fd5 | -8.92255 | -60.75708 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e74a860-f013-3812-8fbd-5fc4329bee38 | -7.24688 | -44.65392 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11fdd42b-bac7-32f7-85e7-41e1db1acbca | -10.43169 | -44.35455 | 2025-08-08 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e60345b8-32d9-3257-a886-4be42579282a | -9.31852 | -62.64849 | 2025-08-08 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cc7f851-2e69-3935-b944-772636d8a610 | -7.40056 | -60.00014 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9def6cd7-ccb1-360d-b3ae-7e1f9bcc3ca9 | -8.92899 | -60.74543 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50fb89a8-3091-395c-8719-4711b3a112a1 | -7.59934 | -55.19662 | 2025-08-08 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6204202-f622-3416-a914-55e6526a4a22 | -8.5283 | -43.30848 | 2025-08-08 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b1c5bcf-b620-3c4e-956f-f7611f195219 | -11.15727 | -49.70163 | 2025-08-08 04:59:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0b528f8-0515-3182-a769-b0e03ede997c | -7.37072 | -44.65273 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3418f088-e1a5-350c-8c48-65dc0e885990 | -8.90634 | -60.5445 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c62d6ab-41d3-3ae6-8e34-72fbb1e5743b | -8.9297 | -60.74127 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abbfc5d6-7dcf-335c-90bb-0fba10d38360 | -7.91976 | -45.54714 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83d0e123-a855-37e9-a25f-0f24eb44fced | -7.15322 | -44.07822 | 2025-08-08 04:59:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a852eb5-6fa2-3d58-b1b6-6ba20edad816 | -7.25091 | -44.66579 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4fb7aebf-65ad-39b9-a19d-3144c5324346 | -7.26349 | -44.31725 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dd7c5fb-110c-3405-8eae-45ff88799929 | -7.06879 | -59.15984 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7a016280-c8fa-3676-b8a6-5659a70c4ae9 | -7.05025 | -59.19588 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f421be57-02fe-3615-bd2b-2ef794db683e | -7.0434 | -59.18765 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fc267e22-165b-3c6d-a1d9-2343acbb4475 | -7.04252 | -59.1866 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f953356-b576-3fbe-a50c-c490fbae1e53 | -7.3731 | -44.6546 | 2025-08-08 05:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c8aa11b9-fc63-3053-8d8a-5eb40524e90c | -20.0613 | -47.5897 | 2025-08-08 05:00:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 64.0 |
| a013186f-6c21-3f4c-866e-fe6a13ef5dc7 | -12.55343 | -47.14318 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae93c2e5-9de3-38d2-927b-6d114e22f470 | -9.92478 | -60.48832 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 527a4a8d-091e-3066-b10c-afc038194c80 | -12.30768 | -50.01197 | 2025-08-08 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d008f92-c9f4-3738-8be3-fe7cd6098277 | -12.52519 | -47.12222 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32eadbf1-ceb1-3bc3-9cf4-11d1daddba21 | -16.72118 | -49.13155 | 2025-08-08 05:01:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65ae7b8f-615a-3b93-9012-2073e27881d9 | -9.93463 | -60.506 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77d95781-ad4a-3e82-b2e7-8e9151e41a3c | -12.3082 | -50.00819 | 2025-08-08 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2de79dff-8a38-3e61-bd16-4baad5a8e845 | -16.7218 | -49.12653 | 2025-08-08 05:01:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 202f62de-ba77-394d-b7ee-0d350b9ed0f1 | -9.7082 | -61.28714 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66a00841-d836-339f-89cd-e652e76e699f | -12.53505 | -47.13382 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 77d2ac71-d85f-3305-be42-c563092c6d45 | -9.93814 | -60.5106 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1701fd74-d76d-3b83-b406-610b06a9c8d6 | -9.93292 | -60.46612 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca17d8d9-e11a-349a-bffa-324c97574380 | -12.52314 | -47.1067 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8f81970-35ef-3a9b-99ec-64d874d47286 | -12.52753 | -47.1451 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 407c0ee5-c0a1-34c3-901e-1676e1e0e020 | -15.55144 | -43.27415 | 2025-08-08 05:01:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| be8f80fe-6c0d-3758-b00d-d41e8fb2805f | -9.9388 | -60.50677 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0090eaa8-18aa-3aa5-a237-7f6a2b89cd5d | -9.92894 | -60.4891 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fab402b-6f55-31fb-b7db-73f4e23be909 | -11.03672 | -55.37626 | 2025-08-08 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 257890d1-b39c-3f3d-a97a-cdf1a06e4bb2 | -14.35816 | -51.10447 | 2025-08-08 05:01:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9cd3534-90be-3d62-957c-b1a69bb9d88f | -9.70586 | -61.30643 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 201a6643-c3a0-3f9c-af8c-40a30c5ff30e | -9.93946 | -60.50293 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd937616-d065-31b6-8e0a-b51a68f99903 | -13.05871 | -56.85358 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca987bea-7cd4-3502-82a8-fa282420e093 | -12.55902 | -47.13951 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3dc4cd41-b072-38c7-93b5-d06f5ce5bb74 | -12.57651 | -47.16375 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bb76ea1-a115-305f-b5bc-06be4ba09cf8 | -12.72372 | -46.37401 | 2025-08-08 05:01:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cab0452-ce83-3491-8a15-4982bc5d1e09 | -9.93839 | -60.45925 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 372d6a19-73d9-3fc1-83f0-ec72ff268fdc | -13.00107 | -47.49545 | 2025-08-08 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc5a28ee-1713-3481-aabd-c6edb486f5c3 | -11.74686 | -47.50306 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e44b403-f9d0-3e00-b202-053014459bdd | -14.36212 | -51.10514 | 2025-08-08 05:01:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 765a1f55-ce63-34c2-9ed6-445564310383 | -11.74138 | -47.50714 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a2f1b413-040d-3c3f-b6cf-fa7095cc5e0e | -9.71527 | -62.40441 | 2025-08-08 05:01:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 20d8dd58-c6ed-37d9-a9ae-5770a6da4e6e | -18.91191 | -47.55618 | 2025-08-08 05:01:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35d85726-c848-3bee-bd64-ed210ac67e59 | -12.61979 | -48.10722 | 2025-08-08 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 873899ba-6470-374a-bf97-67e18949981e | -12.55975 | -47.13366 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d72265f-f10e-3c1e-bfe7-100979c10f9a | -11.76211 | -47.50006 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5084b714-245f-3246-8fcb-909634085120 | -13.05021 | -56.86337 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0208e7ae-d8a8-37ad-a8f7-23945513f069 | -11.74978 | -47.50143 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fb43e91-9177-3062-9d26-c341e171230d | -12.54514 | -47.13523 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2fa126ff-b6f7-37f6-a488-7e40d5512dc3 | -9.9211 | -60.46 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b43e67d8-17c0-3bfd-b426-0e5ba420706d | -12.53932 | -47.14042 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c47acfb-f62f-3b68-82d8-40fa7f77e793 | -9.93595 | -60.49835 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee2a6650-23d3-326a-864a-0056b1ce7945 | -12.49171 | -47.50182 | 2025-08-08 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c42a082-13f5-35b6-9aa3-7263c97d7da5 | -19.12522 | -43.51487 | 2025-08-08 05:01:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8035a06f-29d6-34b3-bc6a-64649b9c7fdd | -11.75168 | -47.5041 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cebd51eb-772d-3ef4-b034-4c2535399348 | -12.52483 | -47.12517 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8aa2b6cb-7551-390a-be43-309607defcb2 | -12.09627 | -44.72968 | 2025-08-08 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d52f09d-b324-3176-a5e3-429722785adc | -12.33944 | -46.06176 | 2025-08-08 05:01:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f69ebb53-ece6-3c46-8ce5-23d4562218bd | -12.72085 | -46.37655 | 2025-08-08 05:01:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3746daa-22c3-3ebb-b61d-b25bb751ff78 | -9.70947 | -61.30531 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecda1477-3c7a-35d6-ae88-6c87c86213e7 | -11.1928 | -51.43718 | 2025-08-08 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README21.md)
