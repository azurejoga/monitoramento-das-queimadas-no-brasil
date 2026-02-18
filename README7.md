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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bccb0af-7ed0-3a99-a41f-8159cd875dac | -9.18941 | -63.59354 | 2026-02-18 05:37:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d361a693-fbc1-384e-859a-b5b22063ebdb | -10.671 | -59.37089 | 2026-02-18 05:37:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b628075-aea0-373f-a75d-ec922b011c4e | -10.67512 | -59.3715 | 2026-02-18 05:37:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08ab3795-d324-3cbc-874b-2f98d5a45979 | 2.6724 | -60.1453 | 2026-02-18 05:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 48.4 |
| dc6e9dc0-2cf8-3643-84bf-400c5c9b48cd | -15.4724 | -59.59256 | 2026-02-18 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d56a25ba-d8b9-3a1e-bb90-1b4f27aa83dc | -15.47417 | -59.59014 | 2026-02-18 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21b7bc49-8c10-3856-8e46-52371675994a | -13.49039 | -60.38312 | 2026-02-18 05:40:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53798553-cbc3-3ba3-8ecd-101aba0c6816 | -18.70486 | -54.98563 | 2026-02-18 05:40:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6a838ec-2e76-3eb8-90ce-a6444aa83e96 | -15.46982 | -59.5895 | 2026-02-18 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae0ab722-2e77-350d-a451-a4d8f3301a89 | -15.47851 | -59.59075 | 2026-02-18 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f6f69d9-ee35-3a63-9fd9-10a938ba8609 | 2.6724 | -60.1453 | 2026-02-18 05:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 4a6526d4-5171-3a9f-ac78-5c966059c58c | 4.0587 | -61.1447 | 2026-02-18 06:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c40dfdd7-fbc8-30c1-8ef4-1eb9149e04f3 | 2.91549 | -60.81859 | 2026-02-18 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0882c379-379e-3ce5-b2ff-b1bb8d764e3d | 2.67968 | -60.14863 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 69dbfd00-f522-3dad-a9c3-8d492225d44f | 4.04957 | -61.13964 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 4242d4e4-8bad-376f-8a11-a922a3dadb77 | 3.94898 | -60.20347 | 2026-02-18 06:03:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22417b2d-46c6-3cd5-89fd-b47be5dd2310 | 2.68545 | -60.21517 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 007e06bb-0631-3c0b-a5b5-9a499967c8d8 | 4.05037 | -61.1443 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 21.4 |
| add1e30c-3862-3612-ac83-ca9f045f15aa | 2.68142 | -60.22142 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d5338f4-261f-3bda-a619-0f8ab1f391de | 2.56652 | -61.01347 | 2026-02-18 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d474395-f16b-3dd5-94b3-fb19cd55a63f | 2.92114 | -60.81635 | 2026-02-18 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7675106-3b5f-37f2-98a7-32e93725a311 | 1.44408 | -59.96724 | 2026-02-18 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cbfb491-ec71-37ed-8c69-590f7ad5ee0f | 2.92019 | -60.81787 | 2026-02-18 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13587c0f-795f-34ed-b7a9-b95a05ace272 | 2.91258 | -60.82275 | 2026-02-18 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 146cd42c-e00b-3b78-bb8f-e3971956db02 | 2.68053 | -60.21596 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dee76af3-1376-30a2-8318-e3fb8867e167 | 2.68859 | -60.20348 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae22d102-583b-3831-93ba-02baac41df02 | 4.1922 | -60.45683 | 2026-02-18 06:03:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83c2ea1c-65f4-3e7d-96c1-de480871b680 | 2.67654 | -60.16045 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d651c73f-26ea-38b6-8478-e0f90e8c1095 | 2.68059 | -60.15418 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29b036cf-f231-3919-81c3-fb3fceadfa5f | 4.79157 | -60.67417 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bed4cd2-a21b-3807-a955-a05a3a4728aa | 2.6805 | -60.14557 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03e745ea-bb75-385a-ba60-4cfd6bfb7402 | 4.50073 | -60.64968 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e01fb9c8-5df7-302f-bbcf-0245fcef56f2 | 4.24278 | -59.75354 | 2026-02-18 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5504c211-eecd-36b0-8c5d-ace7daf2fa01 | 2.67385 | -60.1439 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3df3566f-2827-37c1-a627-37d3ff56eb05 | 2.68238 | -60.15661 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39d4ee0a-95d1-39db-9d6c-1e3d340fc64e | 2.9108 | -60.81937 | 2026-02-18 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08b6eca8-bd64-36b1-9f1f-fc2f92bf7baa | 2.92491 | -60.81721 | 2026-02-18 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 159c528c-069a-3936-bb93-3a0fda088598 | 2.66397 | -60.14553 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc330b5e-19b8-3863-a6d1-da9cf6d33220 | 3.68764 | -60.9132 | 2026-02-18 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0e1f774-a3c1-3b6d-9216-c1e8a06b515f | 4.05337 | -61.14119 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 5b86be0c-e8d7-37ae-8205-9211bca173eb | 2.67475 | -60.14944 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cdc0a7b2-359d-3c0e-8bcf-9f4e4c5f5609 | 2.68634 | -60.22064 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d45b961-00af-36ce-8a0c-5ffb6e33784a | 1.44919 | -59.9665 | 2026-02-18 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcff412f-702c-3bb1-a66a-93efa5a1cc92 | 2.68147 | -60.15964 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cfa42e6f-3f5d-37fe-8e95-c8e87676e44b | 4.78699 | -60.67499 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d4a1b9c-5bbf-3775-a432-35fc0bca3674 | 2.67565 | -60.15496 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c466b4c3-0ab0-3dac-94e7-0a856cf3e301 | 4.05261 | -61.13652 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| cca5a3f6-bc64-3d67-b8ba-ad8a811eacd2 | 4.05408 | -61.13889 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 979849fc-063a-3e7e-bcd4-c384c1522e7d | 4.32584 | -61.1976 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37626b10-9338-393c-803b-9cac3536df96 | 2.66891 | -60.14473 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfaff809-e58c-3a62-b8c7-40eaeb3f77e0 | 3.36566 | -61.11511 | 2026-02-18 06:03:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fdf9688-977f-3773-904d-1b09f08c506f | 3.3611 | -61.11588 | 2026-02-18 06:03:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 961ae256-9f74-3b8b-a877-0cadfef5781c | 4.27203 | -60.08457 | 2026-02-18 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddc4426d-201f-3fd2-8735-33fc171cb719 | 4.50149 | -60.64692 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31df1c84-b394-33eb-84ff-445ec6cf07cc | 2.91644 | -60.81708 | 2026-02-18 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5740853c-d7a0-3d33-8603-f153a4ea7e83 | 4.04811 | -61.13728 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| c4a0b339-8399-3231-add5-a9a6a0ca0e2d | 4.04886 | -61.14189 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 7e484638-e5bb-30f3-a0e3-8d4e67235844 | 4.05488 | -61.1436 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ed861c6a-9626-3694-8fc7-45af7954bf98 | 1.44456 | -59.97019 | 2026-02-18 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d39a8ee-3e0d-3829-a3a6-1ede55d5d782 | 4.50228 | -60.65174 | 2026-02-18 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87f0cb2f-2d2d-37eb-a569-1ac6a741a233 | 2.68144 | -60.15111 | 2026-02-18 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e799ba5-2d6e-3f50-b3ba-2b9420ab93d8 | 4.78637 | -60.67208 | 2026-02-18 06:24:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c107647-72cb-334b-b6b1-2863c0661244 | 4.7809 | -60.68116 | 2026-02-18 06:24:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b982d842-72e2-3e96-850a-269317405b82 | 2.6724 | -60.1453 | 2026-02-18 06:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 43.1 |
| f43d803b-e109-35fd-90cc-bd3b374f4a53 | -12.48142 | -43.64268 | 2026-02-18 06:31:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 6e44b4af-f48c-3375-8bd5-b83fee8da14b | -18.96815 | -52.92616 | 2026-02-18 06:33:00 | AQUA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2e5e6b38-4625-32ef-8211-b0c89f60c62d | -18.81144 | -51.60432 | 2026-02-18 06:33:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 980378e6-44a7-3afd-88fa-3302c8ae339f | -11.88984 | -45.28374 | 2026-02-18 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 74557fb9-3ccd-3403-9b58-3499c5b2e655 | -11.89867 | -45.28503 | 2026-02-18 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c14373d7-363f-3a01-864f-8603177348f3 | -11.88853 | -45.29274 | 2026-02-18 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 63fb91fc-7ddf-33e0-b5fd-f7b418719dcd | -13.02223 | -45.04765 | 2026-02-18 11:53:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| f936f0db-9aec-3584-a3a2-467b6796a5dd | -13.55082 | -43.71117 | 2026-02-18 11:53:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a3ab58b8-41e6-365c-b5de-c62cafddaa96 | -16.77804 | -45.81075 | 2026-02-18 11:53:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dabead8c-3d86-398c-8b95-49a152cb0f62 | -14.51728 | -46.93497 | 2026-02-18 11:53:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| aca43401-5da6-3e64-bcbb-e134f943c948 | -17.62268 | -46.66057 | 2026-02-18 11:53:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b6cd07b2-fc04-3d72-b813-cf9f34072457 | -13.54273 | -43.70361 | 2026-02-18 11:53:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 1ff7e1a2-0ce6-3fbb-8c2c-4a08cac177b2 | -15.20427 | -39.95706 | 2026-02-18 11:53:00 | TERRA_M-M | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 63683893-d3fa-39be-aafd-9867e76a12d3 | -17.66045 | -45.56789 | 2026-02-18 11:53:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7db568f3-b2d4-3312-8165-e1dafee92af6 | -13.55211 | -43.70166 | 2026-02-18 11:53:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3e6852b4-63ec-34d1-b4a2-95e2523c3c80 | -12.24179 | -44.24027 | 2026-02-18 11:53:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d42b5a43-218f-3cd4-9acb-fbb2700c7f88 | -16.75813 | -44.02399 | 2026-02-18 11:53:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4a3042c2-f26a-3b92-800b-ac00e9814e73 | -14.40559 | -44.58802 | 2026-02-18 11:53:00 | TERRA_M-M | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| cf3e717d-0931-3b16-bff2-d43bc214faea | -12.24307 | -44.23124 | 2026-02-18 11:53:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c078210f-1121-318a-bdfc-726e9bf595b7 | -14.4043 | -44.59717 | 2026-02-18 11:53:00 | TERRA_M-M | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3336179d-4abd-38c1-a07b-e49afd6122e5 | -12.49174 | -43.64193 | 2026-02-18 11:53:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 76c018c6-f12b-30e7-9a34-6a33506ec5a0 | -14.40687 | -44.57887 | 2026-02-18 11:53:00 | TERRA_M-M | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d960e484-0638-38d0-948c-198ffc59c4dc | -17.81775 | -45.36121 | 2026-02-18 11:53:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 03772edf-1c7e-37a0-b0ec-565c8852f416 | -12.52222 | -44.02028 | 2026-02-18 11:53:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2b4328b9-8a9b-3881-bce6-b6558882aa9d | -12.49044 | -43.65128 | 2026-02-18 11:53:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 63667ecc-2616-30d4-9661-01b1b4c23218 | -16.11877 | -42.2631 | 2026-02-18 11:53:00 | TERRA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 724424f5-32aa-3d91-b169-0ff6bc7477c5 | -17.63153 | -46.66195 | 2026-02-18 11:53:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 9298d4bb-a9cc-362e-ae69-fa920e818ff8 | -13.02095 | -45.05662 | 2026-02-18 11:53:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 0bcf25a5-31ee-3602-8837-067f54e1442c | -18.17724 | -39.75158 | 2026-02-18 11:53:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 41.8 |
| 9682f2f8-4207-39fb-b283-56dad0d60a2d | -17.65915 | -45.57714 | 2026-02-18 11:53:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7cd53e6b-0895-3626-8584-861528ff6b18 | -17.64755 | -46.4279 | 2026-02-18 11:53:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1be43b24-cf00-315a-b626-11bb0947a006 | -16.14539 | -45.13394 | 2026-02-18 11:53:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7d0a4fe-9735-3e5f-8849-b749eb4fde92 | -15.17757 | -45.6442 | 2026-02-18 11:53:00 | TERRA_M-M | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| c4852fb8-d73c-3f68-a63b-6c45770803a9 | -15.09117 | -43.83069 | 2026-02-18 11:53:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b8225b84-2c58-3805-abf5-672b68eeb8ad | -20.46592 | -43.28103 | 2026-02-18 11:55:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 49c9484e-1fb8-3d37-88f8-fcdaa48c9751 | -19.7905 | -42.14664 | 2026-02-18 11:55:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |


[Clique aqui para ver as próximas entradas](README8.md)
