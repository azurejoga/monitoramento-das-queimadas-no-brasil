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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85146fd0-9b58-3c08-b466-0187e460572d | -6.24074 | -47.76232 | 2026-08-17 05:16:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50d004f2-7389-336b-8eba-94442bbc4c2e | -7.37337 | -55.51004 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59256023-4bec-3814-8d3b-9d68af7227d4 | -6.62302 | -59.0623 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07b75d3a-e62c-331e-9270-6bf3a78a704f | -7.06667 | -56.65594 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5f5f47f-779f-3e75-9fc6-5e2e10202436 | -6.76846 | -59.7656 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07fed69e-7839-3216-9d92-f60b76bf54fa | -10.47661 | -50.36791 | 2026-08-17 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 574d2d9c-2aca-3403-889e-682d6b7802ca | -6.54078 | -58.49881 | 2026-08-17 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa084f00-6a59-3332-b006-03a016dcb65b | -8.95267 | -60.52945 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02967196-5a69-36f4-8f55-355aa0e8220e | -8.52238 | -54.91383 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7fa3862-66af-3c45-bb51-4e94657aa8bb | -8.63657 | -54.72675 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afdf8dfa-1d99-3a88-b2c7-b900c5658edc | -6.85086 | -58.97731 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e07e185-a382-3908-ac06-0d523510985d | -9.49235 | -51.60604 | 2026-08-17 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0e37f45-1094-313f-8e64-cdabcd96b05f | -7.3639 | -55.48974 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b04e447-aa75-341a-ac0d-d30c85ead030 | -6.84735 | -59.10577 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e200da2-0372-3f5f-9717-e8d7390937a9 | -6.82972 | -56.45235 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f81b6fee-68e7-3c4e-a8ee-12aa6a093c3a | -6.98637 | -59.04716 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 719cd8a4-9822-382d-ad43-455932c1ff59 | -6.12029 | -57.72561 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ff89ce0-4cbb-32cb-a9b1-ef95f7c3be1c | -7.37896 | -55.48423 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebddbeb1-5dcd-3db8-9bb1-1fe3a2fd39ee | -7.36212 | -55.50125 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecf08d46-2feb-329c-9815-e7df665e6c80 | -6.95635 | -59.298 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72a163b5-1e99-3b78-8b57-e1d43573a9c8 | -7.837 | -61.34536 | 2026-08-17 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41fcb7d9-ad3b-3926-bc23-d9412d707222 | -6.81967 | -56.45075 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f051da4-ad36-3561-8cda-6ca7a8ed4215 | -6.62814 | -59.05201 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d4cdef5-52a1-35d0-ba93-759ffb17690e | -10.50382 | -50.00719 | 2026-08-17 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4619b8c-3886-36d0-8be6-f620fab0464a | -10.50342 | -50.0102 | 2026-08-17 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8acb0af-e8e8-307e-895a-a94cd861a665 | -6.84925 | -56.43716 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82343af3-721a-3b90-aca8-91076914ed01 | -6.83864 | -56.43914 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a76b9a49-8382-30e1-a3ed-8979afe8ab8b | -8.09917 | -51.66069 | 2026-08-17 05:16:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55fe9eff-7667-310f-8e95-41d3fa80e421 | -9.21023 | -59.67525 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a822a2b-6a37-3573-8a66-fa0f7a8e2ce2 | -6.60053 | -58.97765 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1554a66d-2c3b-3cd4-9b79-0e499c2e2632 | -6.97743 | -59.03836 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44ba54e6-a35c-38db-9bdc-c520ca5fd724 | -7.39593 | -55.47824 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6c3dfb4-cbb9-3a58-8f20-ef0622dd2737 | -9.59381 | -57.01461 | 2026-08-17 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63681845-71f2-31ec-af9a-900e5af9a880 | -7.43009 | -60.02925 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ec1822c-c45c-3374-b458-552ec3dade06 | -6.83252 | -56.45644 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f2b1ac6-ea7b-30d9-b7f4-b6603373352d | -9.17591 | -59.67329 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eee8f2a6-3386-37ce-bfb3-8850dd400992 | -6.78328 | -59.45794 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8641ceb4-7118-35e3-a616-99cbf9222c29 | -11.1025 | -47.29202 | 2026-08-17 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4714ec68-994d-36f3-8444-cddab9a2934a | -6.86321 | -56.41371 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 303c6061-04ce-32e6-9add-aef29f0fb753 | -8.95583 | -60.59794 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49a27be1-3a44-385f-98d8-814bb27c943a | -7.50056 | -60.07629 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b1c1b488-3e92-3108-a37d-5fc513259e60 | -6.65612 | -58.96432 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b007d2b-d9bd-3be8-811b-374419af0bec | -6.71678 | -58.93004 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0f03030-8664-3dbe-b9ab-7e285ba532e1 | -6.97449 | -56.46347 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b8dc3c9-b742-3bb2-ae75-2cad473fd787 | -6.70892 | -58.9361 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ac0c00c-d9eb-35c8-9526-56b9a0e2faf3 | -8.26827 | -57.35196 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b32ff408-865c-3cec-a9a9-83e6b2bd5e2e | -8.89883 | -60.55241 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a55293cb-97d1-3cf6-b2ca-f0adbecb0b19 | -8.96847 | -60.52012 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68b52d75-1a35-3cd3-a601-a2aa589f5c5e | -7.422 | -60.021 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6794617d-10ea-3e03-b470-ea73feabd69d | -7.88376 | -61.79581 | 2026-08-17 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f60b5519-86e3-3470-a6cc-f3c19744155d | -6.6567 | -58.96071 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf1e374e-cdae-37cf-9fb6-ec20a093eafb | -6.64998 | -58.95963 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9dc1ae77-1978-30b2-8eaa-0491392f98b9 | -9.29963 | -56.81079 | 2026-08-17 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85982eb8-515e-3e01-9d7d-ecec762ea1e8 | -8.89874 | -60.59638 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 09cb9022-cd8c-35c2-8a49-e097b68b7381 | -6.89107 | -59.00588 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e716e20c-327e-3033-bcbb-f1d85ab26cb3 | -7.07056 | -56.65297 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 218c5f20-670e-31c0-a50b-413d5ebdd769 | -6.98915 | -59.05128 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ec851de-d5da-3ed3-8fb6-657a365e0920 | -8.95109 | -60.51723 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 653d40e2-8b49-378e-a61c-af835a9174c7 | -9.303 | -56.81134 | 2026-08-17 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ae01a3c-25f5-3358-959e-d829a05333db | -8.59604 | -54.69849 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e050f568-42ef-30c7-b765-94c8ef866750 | -8.02814 | -55.14514 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b8a73dc-2ce5-3aea-920e-454ecba948c2 | -7.55023 | -61.37678 | 2026-08-17 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12399c27-765c-372b-8d6e-599b9b17713c | -8.95615 | -60.53003 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1995ebe0-0749-31f0-9eab-3cb9c9501014 | -7.61845 | -60.94696 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 030aed93-f6c2-36f9-b256-044029da38d6 | -7.3803 | -55.51115 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31b5802a-9206-34e1-b819-d8d93f29f469 | -6.10485 | -57.71607 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e047939-d9a3-3e20-ae8e-6f88c3dfa61c | -8.02046 | -55.14798 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07a169bb-6912-3872-a451-85ffed42bfa8 | -11.10311 | -47.28711 | 2026-08-17 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fe683f1-6c14-368e-85da-c535ce067fd5 | -6.62684 | -59.08142 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c212778-da27-30ee-8b72-3d22a75bf3db | -8.95742 | -60.56614 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb1ceb94-a3fe-3e8d-8c8c-d015910c638e | -8.95647 | -60.59403 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6902fb38-d03e-3bb1-ba1f-3caaf54c851a | -8.74794 | -62.90777 | 2026-08-17 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef99d9e7-40fa-36d1-b2ba-29435bb9ebc3 | -8.965 | -60.51954 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 021f804e-5635-3bb7-ad48-201e4a612519 | -8.90287 | -60.59307 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd7f1239-970a-3f9b-b1a1-c34ba7117f3c | -7.3465 | -59.59729 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7521746b-07b1-397e-861f-f77d6305a738 | -9.37019 | -57.36007 | 2026-08-17 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5aa1e82c-615d-3a12-92f6-676ae9dc7a6e | -6.71228 | -58.93666 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4d35a73-3044-3279-8989-3443f27f776b | -6.97465 | -59.03423 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a69d76f-d161-384f-bf42-65593c8bf63c | -6.86712 | -56.41066 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69a143d4-864d-3fe9-95fa-ecdd18fe9454 | -8.90516 | -60.55745 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9c1c311-14d3-34d0-ac8d-e2f496ca8b5d | -6.6011 | -58.97407 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af668250-8e57-3c3b-9e33-e24a34e6d4f0 | -6.62587 | -58.9594 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 0acde2cc-062e-377a-a397-e8aaa5da336c | -6.62522 | -59.07005 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e19f27c-4477-3a31-9b19-05416aa8bfad | -6.10597 | -57.73042 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c8b26365-6e5e-3b81-bec8-3ab7be7fe261 | -8.9552 | -60.51393 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51c5ec12-93ec-341f-926d-be2520320869 | -8.94885 | -60.59678 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22b5d93d-bf1a-3aa3-a271-2717a9488b3d | -6.6472 | -58.95549 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a946228d-3e82-3305-a174-80ff63bd3396 | -6.68822 | -59.06546 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 749a1028-7cfe-3bd8-8285-e5e8f04a301f | -6.70556 | -58.93555 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2433e52b-262d-3e7d-b940-b8ba94bbb9cd | -6.71171 | -58.94024 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8330ceae-b8a4-3b06-b00f-ac0a125059f7 | -8.96761 | -60.53442 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45fc88d2-0eef-3e0f-8cc9-758aa48a1139 | -7.37683 | -55.48707 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 495cac9c-5153-3b68-ac59-261ba9d132fe | -8.94982 | -60.56888 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1e7ae82-0793-30f1-bc77-858fa0866efb | -7.3431 | -59.59673 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86c57af6-2549-3c57-a5fa-f03c629c2143 | -8.68013 | -54.76242 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a015439f-98a0-3a45-b619-53e94f430864 | -9.19059 | -59.66822 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e98de6b2-d9cb-3fff-92fe-91f6dfe18c89 | -8.95171 | -60.60126 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d6b35e9-1fa2-396d-bf7a-168a81e5a548 | -6.09714 | -57.72194 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 352a65e4-8500-34fb-8017-4aa2517fd020 | -8.95266 | -60.57338 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85f1a558-f933-3bfe-9d55-d0bb015ef8fb | -6.83464 | -58.97104 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |


[Clique aqui para ver as próximas entradas](README48.md)
