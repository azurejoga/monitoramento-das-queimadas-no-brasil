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
| c67f84e6-ac55-30ce-a47f-bd99349de445 | -6.10014 | -41.78778 | 2024-09-27 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0cbfe4ff-9e6e-3f2e-a50e-136628e35e3b | -5.64791 | -41.24456 | 2024-09-27 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f720e8c8-f533-3b47-8982-e2cd61f61a9a | -5.11157 | -40.81474 | 2024-09-27 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c67b253b-dbf3-38ee-872c-da95a3aaeab6 | -6.89723 | -41.61348 | 2024-09-27 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ee6f8eb-75f7-3548-b650-70e20eceb1ac | -6.78596 | -41.24324 | 2024-09-27 03:47:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9aa561a6-138d-36d0-9b68-697867237177 | -6.77593 | -41.23114 | 2024-09-27 03:47:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dc349d0a-04d3-3c16-9ab5-3ff7377b73ea | -6.90122 | -41.61413 | 2024-09-27 03:47:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1842618-c5f1-3efd-a77a-f7dfbf7dcb7e | -6.89666 | -41.61692 | 2024-09-27 03:47:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f5cb0259-9a6d-3828-9936-eb8a1c62206d | -6.85732 | -41.7042 | 2024-09-27 03:47:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f2aae5b3-bad8-3d4d-af8f-f983225e703f | -6.79146 | -41.2341 | 2024-09-27 03:47:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d19ceeee-9034-31ec-bee8-950a418142b3 | -6.78985 | -41.24397 | 2024-09-27 03:47:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a359ed3c-5021-3ae5-9d47-10ccb3d382ee | -6.78207 | -41.24257 | 2024-09-27 03:47:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| aa84e32b-07a0-37ec-a529-305d7020a961 | -6.78062 | -41.22692 | 2024-09-27 03:47:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cc3e2245-1352-3b34-ab94-0e4bc93e7fef | -7.29175 | -42.02431 | 2024-09-27 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86af7349-4608-316e-b9d5-24167bc3a2e9 | -7.29115 | -42.02791 | 2024-09-27 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7fdf4e50-6e33-34d1-90c6-7e7f7ebfc5d3 | -7.05225 | -42.05862 | 2024-09-27 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 96d46dde-d7b1-3374-a8ea-7571e39bee2b | -8.62808 | -40.98537 | 2024-09-27 03:47:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f4c47e7d-6297-3103-a6d0-a887517e3a16 | -8.29311 | -41.42597 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff5d817a-5f74-3fe4-9cc5-715417234744 | -8.29229 | -41.43077 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8cbf3994-ef4b-345e-9836-2a96c4731134 | -8.29117 | -41.42801 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59d1fc4f-80f4-35e8-8d3f-a00887c4f7ab | -8.62434 | -40.98472 | 2024-09-27 03:47:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aa38d1ed-8fdd-3c24-81a4-254401be18dd | -8.29918 | -41.4369 | 2024-09-27 03:47:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| f51c8e12-20dd-3b84-b1ba-566dd8f12d40 | -8.19146 | -41.43052 | 2024-09-27 03:47:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 09398ab7-8bd7-30d2-8c6f-76169ddd4037 | -3.21371 | -42.68961 | 2024-09-27 03:47:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02d6bc98-b9b6-3579-8311-451b3c415a6c | -4.79656 | -43.04308 | 2024-09-27 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 734e8fe5-5a73-3a30-bc61-3ff42c7c3a7f | -6.40938 | -42.9278 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2d3583d3-438d-3076-9e67-95bc6b685c21 | -6.32935 | -43.16191 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf4c3c5d-0be6-315d-b7be-3649f4bd8ceb | -6.32507 | -43.46491 | 2024-09-27 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cd9c2dc-156b-3f17-99a4-ec5d57424afe | -6.31871 | -42.50079 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| eceac1d1-5002-3836-a80f-45cf8329fc1d | -6.31442 | -42.50025 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7599be1b-57a9-34c3-b850-a077de8505c4 | -6.30029 | -42.506 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| de9fdf8a-7c5d-3fa1-bccb-c08d0f18d0bb | -6.29601 | -42.50537 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a5bf02c9-4d01-3c8d-a8ef-15b06efc1f01 | -6.29532 | -42.50945 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 41795d56-d5bb-3315-9dd2-f4d3d24ba720 | -6.28975 | -42.41373 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9cdff811-b245-3dff-b9cd-8f366b242e83 | -6.28928 | -42.70211 | 2024-09-27 03:47:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 47ed4d90-1bac-3688-b650-8351dcd81a1f | -6.28547 | -42.41321 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 10c19d67-56f2-3414-82de-0fefc485e17c | -6.2363 | -43.31905 | 2024-09-27 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01f202a6-972c-31de-8787-dd10503137f6 | -6.2336 | -43.31684 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53ed000b-c50e-3d41-8d50-cbf0db080324 | -6.33455 | -43.15825 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf1d9293-5137-37a7-8506-b960027d4321 | -6.33381 | -43.16265 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe70ed29-eef3-33ea-a610-2a0cd198bc15 | -6.32729 | -42.50196 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8f5cceaf-72d0-3777-8510-82302d8f0683 | -6.32661 | -42.50599 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a25136b2-38d1-3657-a264-d67dfff9fcb3 | -6.323 | -42.50137 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 89c177a0-b753-31c0-9e77-d9223267b004 | -6.30948 | -42.50352 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8c4cd139-794d-3ecc-bfae-beec8920307e | -6.30524 | -42.50265 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 78d99d6c-b049-3aef-b65f-bc82dc88e4f8 | -6.29959 | -42.51012 | 2024-09-27 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 412e52eb-3f50-31ce-8f0e-de7bb4218d56 | -6.28998 | -42.69796 | 2024-09-27 03:47:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1e84521e-5659-3b77-b884-366e3708e76c | -6.2318 | -43.31818 | 2024-09-27 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6bdd6cc-a949-37d3-b80d-452ca632fd20 | -6.04467 | -43.45467 | 2024-09-27 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95c976e0-7b02-3dd2-898a-09eb3ea96ea0 | -5.94913 | -43.26956 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0bfc2b1a-90cf-3f59-b320-d00baafc40a5 | -5.79292 | -43.27088 | 2024-09-27 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd2c733c-c6e6-35b9-8e06-713403fafc81 | -5.30849 | -43.07948 | 2024-09-27 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52634758-1678-316b-88e0-929b0f6e3e21 | -5.30771 | -43.08399 | 2024-09-27 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2507c77-8976-39bf-b84d-5146d827fc46 | -5.30665 | -43.08152 | 2024-09-27 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d635483-8bf3-358e-944a-9f97fed077ea | -5.30361 | -43.07178 | 2024-09-27 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 117d0b63-b83a-3030-9d19-beb5c5d21fc3 | -5.30023 | -43.07355 | 2024-09-27 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 21200d3f-a823-3d8d-98eb-c3d610524799 | -5.13733 | -42.89365 | 2024-09-27 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5acbe42e-06a9-3192-9cb3-f0279e923d4e | -6.03926 | -43.45883 | 2024-09-27 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe49c26b-0c29-330f-b013-44a56e7fa62a | -5.94836 | -43.27408 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ef692d83-5d32-3a5d-abea-c34098b7938a | -4.1942 | -48.6339 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c48de1fc-23bc-32f4-afc9-9d9c35cac420 | -4.18871 | -48.62642 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9aba8f95-25e0-304b-8792-faf7bdb9e6da | -4.18766 | -48.63243 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f870ded-49f0-3007-ae60-f380bf63ed95 | -6.0071 | -49.33535 | 2024-09-27 03:47:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 684c826a-c0a3-378e-b513-99c139260912 | -6.00602 | -49.34107 | 2024-09-27 03:47:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99c84248-2f27-332d-b2d2-9ac14515d2ee | -6.0033 | -49.33814 | 2024-09-27 03:47:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d201c695-80f5-3f23-99c4-df9f000b5490 | -5.87329 | -48.09837 | 2024-09-27 03:47:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| be8e6840-7984-3189-aec7-14322800ee2f | -5.87247 | -48.10292 | 2024-09-27 03:47:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 83f87cf5-2bfc-373c-ae72-8c54f09e4e5c | -5.8716 | -48.10774 | 2024-09-27 03:47:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 135ffbbb-7c8a-3736-8784-67f818758430 | -5.86617 | -48.10221 | 2024-09-27 03:47:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de985236-20ad-3268-ab8e-52193df752ca | -5.8653 | -48.10701 | 2024-09-27 03:47:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c852c8b-effb-3467-b935-963591a7a1c4 | -5.62617 | -49.15928 | 2024-09-27 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8959bad4-6190-3aa6-b87d-f8bd7ff58eeb | -5.62247 | -49.15882 | 2024-09-27 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ce75a8a-7792-3015-b6b8-74aae7758154 | -5.62144 | -49.16458 | 2024-09-27 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2af20d9c-6809-3c6d-9804-b1ab8927d3bb | -5.61955 | -49.15788 | 2024-09-27 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e50355e6-c545-3caa-80e9-44926be9587b | -5.61848 | -49.16366 | 2024-09-27 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eae8760b-5eb6-3555-aa8c-4c732e1e1fa0 | -5.25742 | -48.88774 | 2024-09-27 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2338a640-7a6b-3c40-9243-511497604dcb | -5.24985 | -48.89212 | 2024-09-27 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed2c88bc-6e12-3376-b4c8-41cb43ef333b | -7.56773 | -49.18851 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 23.7 |
| bf3af21b-898a-350e-bc0f-10030f1784dd | -7.56731 | -49.19118 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 37.9 |
| ba7b8638-7019-3bad-9dfb-552972d34c1b | -7.56666 | -49.19432 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 4b151c6a-7116-37cf-bf1c-ae97d3965bf5 | -7.56622 | -49.1969 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 72b86427-3123-320b-a6f8-49f18d36df78 | -7.56565 | -49.19986 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 5ff51556-39a0-372e-82d9-be87ed25d7ac | -7.56519 | -49.20233 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 11996fc9-20ba-3d07-8b7d-00f3f4f64fbf | -7.56464 | -49.20533 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 9c3e7e6a-d420-30ac-9a96-ebb013e06e02 | -7.56413 | -49.20786 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ddc52661-db41-37e2-a247-633cbbd3c977 | -7.5602 | -49.19302 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 87feb632-0a82-3dd8-8e89-82106b2ca078 | -7.55977 | -49.19561 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 294a561e-f8d4-3635-b690-750e67fb257c | -7.55918 | -49.19858 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 35.8 |
| d7e184ca-d679-35c7-906e-704c4b387e4c | -7.55872 | -49.2011 | 2024-09-27 03:47:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 2f658562-5894-3271-ac01-406feecbd8d1 | -2.79692 | -49.58902 | 2024-09-27 03:47:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a001328-612d-3dbc-9601-840615bab721 | -4.96153 | -49.90642 | 2024-09-27 03:47:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eca01627-38ed-3f6d-b270-247e5bd40c07 | -4.95738 | -49.90278 | 2024-09-27 03:47:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02010dae-2804-3d99-880e-1fb81bb724e5 | -4.95615 | -49.90966 | 2024-09-27 03:47:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c3228cf-94ad-3788-af5c-dc1aeca0c738 | -5.02302 | -43.79563 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 54ba89f1-01ad-3ee3-a4ca-c1085bbb9856 | -4.77564 | -44.6543 | 2024-09-27 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cf373d6-2242-3d48-9bd8-ee362405b438 | -4.77059 | -44.65335 | 2024-09-27 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 740a98c7-9bd6-3045-95d2-d60bb663c7aa | -4.77008 | -44.65638 | 2024-09-27 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2369c06-6de9-38a8-89f0-0b949847ae45 | -6.58714 | -43.61308 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bcfe0c39-58ec-31b0-bac2-669b46baa245 | -5.98948 | -43.97905 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2baafa5a-55be-376c-9d99-85cf23cfe00f | -5.87475 | -43.87365 | 2024-09-27 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README54.md)
