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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45df4012-1be7-341a-a9cd-4c8d42cf762d | 1.98951 | -60.88701 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 953c93e0-1972-3d84-9a00-76d4ad6a3845 | 0.96118 | -59.55436 | 2026-03-18 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 366e451d-93e6-3d64-a72a-8079628d521f | 3.2065 | -60.32177 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4279415-87e3-35cf-8f11-83c4565f1ead | 3.41374 | -60.17619 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94475c6c-8b90-3da5-b684-7fbd25ac643d | -16.44528 | -58.17479 | 2026-03-18 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 1abf6947-fe1a-3d97-aa7a-23a551fdb146 | -16.44942 | -58.1809 | 2026-03-18 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| aac3f3c5-402b-3641-8433-69cad3c4f010 | -16.57811 | -57.80434 | 2026-03-18 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8fe9d3ad-7d64-326d-915f-26bd645fc60c | -16.4501 | -58.17542 | 2026-03-18 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| ea095aca-e559-3373-a482-c12ff9dee8fe | -16.44899 | -58.17654 | 2026-03-18 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| fdfe23b0-48d5-3993-917e-d652de83ee1f | -16.5831 | -57.8031 | 2026-03-18 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 99970899-bea3-3b87-9340-6ac376c07944 | -16.57815 | -57.80239 | 2026-03-18 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 610b8f32-2645-3946-84e8-c4892410c877 | -16.45381 | -58.17722 | 2026-03-18 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 89440ad1-f168-3991-bd37-baa43b1492c1 | -15.77645 | -59.67239 | 2026-03-18 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eab13265-9ef1-3e99-addf-8d998a38f257 | -16.44963 | -58.17105 | 2026-03-18 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8f374f27-19b4-3ba1-bc61-caea69ee86a8 | -21.97743 | -54.62778 | 2026-03-18 05:46:00 | NPP-375D | DOURADINA | MATO GROSSO DO SUL | Brasil | 5003504 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eb539ec7-1ef3-3c39-b3ba-c97c9dcce021 | -21.98388 | -54.62847 | 2026-03-18 05:46:00 | NPP-375D | DOURADINA | MATO GROSSO DO SUL | Brasil | 5003504 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1340c98c-83a2-3885-825b-e2bb5dfb43a7 | 3.08079 | -60.766 | 2026-03-18 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdd652c3-b85a-39a6-a927-735ab899f202 | 3.41134 | -60.17796 | 2026-03-18 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 69e596bd-458d-3f66-9491-1686cc9ccd63 | 3.73741 | -60.75595 | 2026-03-18 05:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1ca6d6f-34e5-3878-8057-a8d25a2d6913 | 3.20395 | -60.3204 | 2026-03-18 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44db2aaa-2388-3dd6-95d4-20fce52d193a | 1.87846 | -61.23143 | 2026-03-18 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b3c9faf-a723-375b-9b61-e524d41085c8 | 3.0604 | -60.75916 | 2026-03-18 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c812e88b-d02f-3bb9-9b7c-55803e8c6291 | 3.20308 | -60.31512 | 2026-03-18 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e524b51-2406-315d-82df-a5b292a1a0c6 | 3.06122 | -60.76413 | 2026-03-18 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c33aa90-7bd0-3d59-b9cb-c2c6767edceb | 3.20479 | -60.14403 | 2026-03-18 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 140af784-7805-32fc-a4e1-abe1f63afd70 | 1.87769 | -61.22662 | 2026-03-18 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e31491a-3629-33fe-b308-abbe449f9152 | 3.07998 | -60.76104 | 2026-03-18 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 329b8aed-6850-392e-96b8-d9787d0a7223 | 3.40738 | -60.18412 | 2026-03-18 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 651496be-3921-36da-91b0-44fc59bc6d44 | 3.20483 | -60.32567 | 2026-03-18 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b57d6091-4c94-3923-8b28-71bfbaeefc00 | 3.4162 | -60.17715 | 2026-03-18 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c97d097-699b-3fa7-a992-6ccccbdf5f17 | 3.05653 | -60.76489 | 2026-03-18 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08d8743a-e12c-3b21-b488-913940a30c4b | 3.78556 | -61.301 | 2026-03-18 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ca7d31b-859e-3c37-ae7d-952cd6aac82f | 3.42105 | -60.17632 | 2026-03-18 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 460ed2c5-9126-309c-905a-183d609ac09c | 2.44103 | -60.24684 | 2026-03-18 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dffff3b-c8de-371e-a742-c259bd85570d | 2.4401 | -60.24118 | 2026-03-18 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cab9767-d92c-34a3-ae2b-31e5a9811417 | 0.96472 | -59.55288 | 2026-03-18 06:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 925722a7-6340-37b4-8bf3-acd2432f47fd | 0.77408 | -59.87292 | 2026-03-18 06:01:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c15670d-23ff-3ebf-b492-24ce883ab9ec | 0.96418 | -59.54963 | 2026-03-18 06:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38836b42-a86e-3110-bdfd-81c25a2ef93f | 0.77358 | -59.86982 | 2026-03-18 06:01:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84c9556b-8c0c-31a0-b2ef-1c6ce1a91317 | 1.07862 | -60.68134 | 2026-03-18 06:01:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27c83327-afdc-320e-bd28-5aa3ba031159 | 0.96483 | -59.55064 | 2026-03-18 06:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d93cca3-a242-3d35-a36e-299aff566c3a | 0.96364 | -59.54639 | 2026-03-18 06:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d97110c-8719-3811-9d5f-d2f4d1fcebfe | 0.96432 | -59.5474 | 2026-03-18 06:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82054bc0-bb1f-3416-bd00-9c7ee877dacd | 0.7684 | -59.87063 | 2026-03-18 06:01:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ea1bfd8-6d55-3259-b6e4-e6486bbd526d | 1.0795 | -60.68671 | 2026-03-18 06:01:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb99dc4e-e536-3c3e-af7d-2b894cd72347 | -16.4507 | -58.17882 | 2026-03-18 06:05:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 2b0549d9-35ec-349c-a532-82f057b23ac6 | -16.45299 | -58.17795 | 2026-03-18 06:05:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 326102b2-49b3-38c5-a328-e873d937626e | -16.44349 | -58.1781 | 2026-03-18 06:05:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 315d07e7-e631-372c-a373-733287bcc3fd | -3.94232 | -40.64306 | 2026-03-18 12:06:00 | TERRA_M-T | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 1fd6278e-9099-350c-999f-cb5a0a67aa52 | -3.1699 | -41.14053 | 2026-03-18 12:06:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| d996eede-1b1b-3446-b758-5698c7d4ca6f | -3.90164 | -42.23114 | 2026-03-18 12:06:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 0b317244-5e86-352e-b320-9ba18aecb656 | -7.95082 | -44.48516 | 2026-03-18 12:06:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 622e44fd-37bc-3910-b59a-eef25f412cc0 | -10.09208 | -44.96449 | 2026-03-18 12:08:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 23f1ae97-e376-3415-8cea-2126e2925af2 | -9.12535 | -45.09005 | 2026-03-18 12:08:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5b77cffe-0f47-3107-91ee-ab19d9bd9b98 | -25.04663 | -51.19517 | 2026-03-18 12:12:00 | TERRA_M-T | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 957b2649-0ae0-3460-83a4-5bbf897a5b87 | 3.932 | -60.6926 | 2026-03-18 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| be19164b-414f-382b-9b73-d2beaef69ddf | 3.9695 | -60.4067 | 2026-03-18 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |


