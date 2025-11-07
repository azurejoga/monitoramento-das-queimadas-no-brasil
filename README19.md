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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86543e26-c926-37f2-bc29-8aef281b4bd0 | -7.41944 | -37.06125 | 2025-11-07 11:38:00 | TERRA_M-M | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 15.3 |
| f17699b7-3902-3e83-98f9-e0c2c079fd96 | -8.22622 | -39.54094 | 2025-11-07 11:38:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 45.7 |
| 4944d229-4bcb-3db8-91a3-cfd7f4fd009f | -7.92327 | -37.61605 | 2025-11-07 11:38:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 24.4 |
| df75efbe-dc1c-3e32-9f04-179e7c22b31f | -8.32717 | -36.37378 | 2025-11-07 11:38:00 | TERRA_M-M | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| bbe145d7-4ada-3540-a688-5d3f61fbc525 | -6.30284 | -37.77415 | 2025-11-07 11:38:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 8e6ad9d2-296d-3fb0-bd8a-4fb24b5f6d69 | -8.46392 | -36.2569 | 2025-11-07 11:38:00 | TERRA_M-M | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e337f878-eab2-392f-99dc-cf28e4fec39f | -8.43229 | -40.40157 | 2025-11-07 11:38:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 11.0 |
| e3d94406-c54e-3d4c-8b44-47bcd65fc7a1 | -8.33644 | -36.37505 | 2025-11-07 11:38:00 | TERRA_M-M | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 4d8a3c2a-e230-3406-9468-869f8957e249 | -10.54309 | -39.29548 | 2025-11-07 11:38:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 9ed948a8-6dc8-36c0-b718-b3c067a80197 | -7.59913 | -38.83943 | 2025-11-07 11:38:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c88103ed-b796-331b-a4f7-66837f1716a3 | -8.92326 | -40.38177 | 2025-11-07 11:38:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e2cdb5b8-39e5-3b58-af97-5bcd596efb84 | -8.22756 | -39.53178 | 2025-11-07 11:38:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 158.4 |
| 7386fad9-ef8f-3830-966e-48517ca32a51 | -8.36085 | -40.31121 | 2025-11-07 11:38:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 78af7f42-7a13-397e-8003-87be258f201e | -10.68089 | -37.07078 | 2025-11-07 11:38:00 | TERRA_M-M | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| aa7a484b-8949-3f13-ac48-b873e9e96775 | -6.58443 | -41.3965 | 2025-11-07 11:38:00 | TERRA_M-M | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 10929dbd-2fd1-30a2-9953-e444bfb78848 | -6.04411 | -37.58482 | 2025-11-07 11:38:00 | TERRA_M-M | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 38092c23-7110-38ed-b26b-b7d42e907806 | -7.20605 | -40.74649 | 2025-11-07 11:38:00 | TERRA_M-M | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 68dd722e-1bdc-399b-b63f-e2d8ae7ae1b9 | -6.57527 | -38.3845 | 2025-11-07 11:38:00 | TERRA_M-M | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 78362e6c-cfe0-327d-88e1-012924134f57 | -8.11737 | -35.5089 | 2025-11-07 11:38:00 | TERRA_M-M | GRAVATÁ | PERNAMBUCO | Brasil | 2606408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| bad62941-b6b2-334a-ae49-a6824381cc00 | -11.27147 | -39.16219 | 2025-11-07 11:38:00 | TERRA_M-M | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 9da2ce1a-9304-3360-9a7d-4025e9e71347 | -7.50959 | -36.35574 | 2025-11-07 11:38:00 | TERRA_M-M | CABACEIRAS | PARAÍBA | Brasil | 2503100 | 25 | 33 | nan | nan | nan | Caatinga | 11.0 |
| a8ad311b-5ff0-36b8-8841-f057dbe5d29b | -6.37477 | -38.30776 | 2025-11-07 11:38:00 | TERRA_M-M | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 108.1 |
| c851c9b2-cc3c-3ee5-833b-bb865d319e91 | -7.69477 | -37.65674 | 2025-11-07 11:38:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| b165f79b-97bf-3929-828a-0c2bc4355eeb | -7.7566 | -37.87045 | 2025-11-07 11:38:00 | TERRA_M-M | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8e4405bf-959a-3590-85a8-9f52f6bc1218 | -6.88294 | -42.85345 | 2025-11-07 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 1b2aca81-8ad4-3b6b-81db-151facaf7f2e | -13.11929 | -42.99848 | 2025-11-07 11:40:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 35.6 |
| 3edf847a-f2bf-3c44-86ca-eee1a7cf24f2 | -13.11698 | -43.00473 | 2025-11-07 11:40:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 70c8fc18-162a-3161-9907-5a25721dd2d1 | -13.11895 | -42.99249 | 2025-11-07 11:40:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 53aab825-16c7-330c-9e1f-704e670bfd98 | -4.5718 | -46.4135 | 2025-11-07 12:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 81237a3c-cbee-3aa8-89f7-dc7f28e1d7eb | -3.5252 | -47.5389 | 2025-11-07 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 745c89d7-80bd-34f2-bc26-2d44bff76b1f | -7.5964 | -38.8294 | 2025-11-07 12:50:00 | GOES-19 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 125.4 |
| f0ab01b2-02b0-3680-af27-f64410788e0e | -7.5964 | -38.8294 | 2025-11-07 13:00:00 | GOES-19 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 100.9 |
| b711aad9-5c1c-3672-888b-b9620c846469 | -5.2738 | -47.146 | 2025-11-07 13:00:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 215.6 |
| 265cebfe-a768-3d13-8e40-544af574e5a0 | -5.255 | -47.1691 | 2025-11-07 13:00:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 326.1 |
| 2129b8a1-2c45-37bc-a11b-90c1b850d585 | -7.7974 | -38.0357 | 2025-11-07 13:00:00 | GOES-19 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 102.7 |
| d6614388-de1c-3528-bf74-0d7e9f841b64 | -5.9234 | -41.3056 | 2025-11-07 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 58b99cf9-cd9f-386c-8500-7bf505abd496 | -5.255 | -47.1691 | 2025-11-07 13:10:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 179.7 |
| 39762edc-60fa-3774-96b3-f109b6ef4865 | -5.2738 | -47.146 | 2025-11-07 13:10:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 230.5 |
| 9b06ca4c-66b1-368a-ba6d-4091b41e430b | -3.0874 | -50.3321 | 2025-11-07 13:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 80a2d21c-93ec-3369-8672-dcffbdab5c99 | -5.255 | -47.1691 | 2025-11-07 13:20:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 2e4083c9-a3e3-3988-9e5e-978ba1d81024 | -3.0874 | -50.3111 | 2025-11-07 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 991f1750-e68f-390d-88b1-3078b42d6d8a | -4.9049 | -41.7696 | 2025-11-07 13:30:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| dadf48e3-2e18-3324-80f6-689fafa8c2b3 | -5.9229 | -41.354 | 2025-11-07 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| a408d16f-2d64-333b-b3e5-f3d1f262d730 | -3.0874 | -50.3321 | 2025-11-07 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| aa4e1796-5ee3-30db-9a8c-1dda15decf16 | -5.255 | -47.1691 | 2025-11-07 13:30:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| ebeba79d-ebfe-38ca-856b-27d278c85b55 | -3.125 | -50.1419 | 2025-11-07 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 959dd4cc-9af1-3bc3-a4ad-71fad3115775 | -6.3333 | -41.703 | 2025-11-07 13:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| fd7fc55e-6cd0-3fa9-a9c8-9ed2d7b05825 | -7.9758 | -37.5448 | 2025-11-07 13:30:00 | GOES-19 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 129.3 |
| 4f287429-42f6-35d7-8856-4c80af371e47 | -6.108 | -41.651 | 2025-11-07 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| 5de74f21-d776-3dbd-a960-45938a7db36b | -3.125 | -50.1419 | 2025-11-07 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 5db77436-dac5-312e-8f1c-3bb2c5e389e5 | -4.5726 | -46.3025 | 2025-11-07 13:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 8d22a0cb-8e72-36fb-9132-38d01aa1f2a5 | -4.9049 | -41.7696 | 2025-11-07 13:40:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| d7cd7e6f-d098-3230-9ce6-e68038e8a222 | -6.1271 | -41.6253 | 2025-11-07 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 18c85bdb-c84a-32e2-a0cf-8fca2f3a194a | -3.0874 | -50.3111 | 2025-11-07 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 9dcc6436-1d54-3bd3-8381-86230c5ba28d | -4.5726 | -46.3025 | 2025-11-07 13:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 6b5047bb-60f5-3b47-bfe7-0b91b2625ca5 | -10.0466 | -39.4239 | 2025-11-07 13:50:00 | GOES-19 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 95.5 |
| f286acbf-7e43-355b-bdab-7e5c76bde6e4 | -6.108 | -41.651 | 2025-11-07 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| a8df368e-4c3c-3aa8-aba5-b43777f02082 | -3.1657 | -45.1143 | 2025-11-07 13:50:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 3b19fa1d-b6fe-321b-bea2-ec8d08770af5 | -1.2822 | -49.1467 | 2025-11-07 13:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| fe6b7197-e7a7-317d-af22-b24e2bb3c47d | -3.125 | -50.1419 | 2025-11-07 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 8afa2c6c-9175-338b-a3f6-6cf681bb7e9b | -4.9049 | -41.7696 | 2025-11-07 13:50:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| 3cff90ae-57e0-3ef6-987b-190795f3184f | -5.1533 | -41.2468 | 2025-11-07 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| e09fd83e-e59f-3b38-a87d-50c1ad4a9078 | -5.1535 | -41.2226 | 2025-11-07 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| b32f7803-9c04-3b0f-a685-bfec0b55dd4d | -5.1533 | -41.2468 | 2025-11-07 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 01f3f271-02d0-3af5-9191-8780002783f3 | -4.9049 | -41.7696 | 2025-11-07 14:00:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 1abff0be-572b-39a4-8eb7-165dfc10fcb5 | -1.3007 | -49.1464 | 2025-11-07 14:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| ccde91c2-40c4-3bdd-837c-e4905437bc1b | -3.125 | -50.1419 | 2025-11-07 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 83d5a540-fc5d-31c3-a13b-f717308a1a28 | -5.1535 | -41.2226 | 2025-11-07 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 81403869-48fb-38a9-8abf-ce3b15733094 | -1.3006 | -49.1677 | 2025-11-07 14:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 791a99cd-b040-3845-b7ff-2b32a00682c9 | -6.4982 | -38.7252 | 2025-11-07 14:00:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 96.6 |
| f1b68412-aeeb-34c5-b3a8-e834dbba8f4f | -3.0874 | -50.3321 | 2025-11-07 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| b4f1b279-9a76-379d-ae62-3c7a973e48bc | -4.9049 | -41.7696 | 2025-11-07 14:10:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| ecff032d-f139-3d2c-b1dc-2ae4cf8f3bde | -3.125 | -50.1419 | 2025-11-07 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 904fca7a-e615-3f0c-ac40-8807fc74c2d4 | -10.0658 | -39.4209 | 2025-11-07 14:10:00 | GOES-19 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 19c27e47-a942-31ea-a463-9434a2c25b5b | -9.5562 | -66.7442 | 2025-11-07 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0d78c5bd-64b2-392a-b6f3-fbb3d03c2cad | -4.6131 | -48.6589 | 2025-11-07 14:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| c7527cdb-d809-39a3-bc29-00e1694bb2cc | -5.6245 | -41.0887 | 2025-11-07 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| cd695006-dc90-36ef-9b40-fbebd634a008 | -3.7674 | -44.0171 | 2025-11-07 14:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 048db29d-d5a1-3dbb-abef-02e19d604fa9 | -5.7775 | -40.8328 | 2025-11-07 14:20:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 7d37a09b-8daa-390d-872c-8070ee4a6c18 | -4.9049 | -41.7696 | 2025-11-07 14:20:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 908a6e31-6ae6-3bc5-b2a3-e9f8df51e0b6 | -5.6243 | -41.113 | 2025-11-07 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| befd7df6-59b3-3b6c-b748-b095d1825825 | -19.0323 | -57.5174 | 2025-11-07 14:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| a0459ebb-b157-307b-8a50-6d2bbef04424 | -3.3465 | -50.1769 | 2025-11-07 14:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 6af1829c-b962-3f3d-a9d8-22216da888a4 | -5.1347 | -41.2241 | 2025-11-07 14:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| a1e947bc-03d2-3669-9b5d-33428ac5edd5 | -4.6131 | -48.6589 | 2025-11-07 14:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 37ac2e65-bedc-3f12-b2bd-b227bc4b3850 | -6.1274 | -41.6013 | 2025-11-07 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 05db4c56-69b7-3e81-a167-3e58e91552e3 | -5.7777 | -40.8084 | 2025-11-07 14:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 98.1 |
| f061c271-ce45-3bbe-b0a4-dc3def4a1059 | -9.5562 | -66.7442 | 2025-11-07 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 2530ca4e-5a69-3e67-b5eb-ef1fef2fc6c4 | -5.6245 | -41.0887 | 2025-11-07 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 4db05ef8-800a-3132-82cd-5b0952b62b02 | -5.1345 | -41.2482 | 2025-11-07 14:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 116.9 |
| 97e70efc-5c03-33bb-bd8b-40b2370e0c47 | -3.6884 | -41.6289 | 2025-11-07 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| cfdcf23a-61f5-346f-9291-a8c2d7050c12 | -5.1962 | -45.1221 | 2025-11-07 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 8cfd0641-fb1c-3503-83b9-558c720a267e | -9.5562 | -66.7442 | 2025-11-07 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 727c71d9-1a20-33bb-9b67-0d5899e5240d | -19.0323 | -57.5174 | 2025-11-07 14:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 867e73f3-a46e-396b-9ca9-5ff39d520714 | -5.6245 | -41.0887 | 2025-11-07 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 44bd2f10-b844-3037-af05-804ca2c0a240 | -3.125 | -50.1419 | 2025-11-07 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 4c2204fb-340f-31de-9ed8-0103844e8092 | -0.3769 | -51.7481 | 2025-11-07 14:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 65.3 |


