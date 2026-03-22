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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd1f15fb-9cc5-3c48-8996-db943dc44251 | 0.9943 | -59.3619 | 2026-03-22 00:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 70047af4-394e-3cb1-a5ed-798a9956d2c9 | 0.9761 | -59.4002 | 2026-03-22 00:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| dacd3206-9752-3278-a624-fa670a834a4c | 2.6518 | -61.3203 | 2026-03-22 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6c500168-ec59-39c2-8628-373f15a06fcd | 2.6518 | -61.3015 | 2026-03-22 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 194.6 |
| 5a396c20-eb91-3161-92ed-d89eb3e4a82e | 0.9943 | -59.381 | 2026-03-22 00:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 1afd9e3d-c216-30c8-8ba5-8450cf5c854b | 0.9761 | -59.3811 | 2026-03-22 00:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 188.2 |
| d8646ada-1704-3cf9-a116-16ba457eecda | 2.6519 | -61.2826 | 2026-03-22 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b9094c35-7317-3c75-bf1f-b610cbd1006a | 0.9943 | -59.4001 | 2026-03-22 00:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 6a2332f2-0373-3cb3-82b4-5f5f41a7c47b | 2.6518 | -61.3203 | 2026-03-22 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 40a30d4e-29fb-37d8-9b7b-b8c9acc00b23 | 2.6518 | -61.3015 | 2026-03-22 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 206.7 |
| 19f28633-1430-33cc-a495-8b28f60fa45f | 0.9943 | -59.4001 | 2026-03-22 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| fc2f040f-0cde-3eb1-8711-eda9247d138a | 2.6519 | -61.2826 | 2026-03-22 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 9f3033f8-bfdb-356b-82cd-d755c8aece22 | 0.9943 | -59.381 | 2026-03-22 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 183.7 |
| e9beef07-6e8a-3bef-8f0f-5c5e41b80b15 | 0.9761 | -59.362 | 2026-03-22 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| c3d83731-dd2d-36ad-9ad8-57f6cf0f4cca | 0.9761 | -59.4002 | 2026-03-22 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 65d3dfd4-2eea-3ea8-88f0-9615ede61c20 | 0.9943 | -59.3619 | 2026-03-22 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 9ae04955-0e63-3d31-b405-cabac9ffaa1e | 0.9761 | -59.3811 | 2026-03-22 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 9abfa614-4fa6-3854-b11e-da8a7c84999c | 0.9943 | -59.381 | 2026-03-22 00:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 2ecd34a5-8f34-3d3e-af57-7d56b6c6c4e5 | 2.6518 | -61.3015 | 2026-03-22 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 197.2 |
| 0d47beaf-4962-32e0-8568-61bc1a2d95b8 | 2.6519 | -61.2826 | 2026-03-22 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 7c185168-1bd5-33c4-9607-d4bc4c066f65 | 0.9761 | -59.4002 | 2026-03-22 00:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 31682203-f0c0-3317-9476-4c6508bc5e79 | 0.9943 | -59.4001 | 2026-03-22 00:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c766c50d-bc32-3e86-b008-007e74f2b4df | 0.9761 | -59.3811 | 2026-03-22 00:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 09788d53-0cf0-364a-92ce-6026c03235f7 | 2.6336 | -61.3017 | 2026-03-22 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b2c3aa0d-c926-3230-a2c2-1d0e480d5369 | 0.9761 | -59.3811 | 2026-03-22 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 344b45f9-1838-3117-8019-3c0c6eb66139 | 0.9761 | -59.362 | 2026-03-22 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 97908d8f-3035-37cd-91cb-ff136b656358 | 2.6336 | -61.3017 | 2026-03-22 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 7df9a7b4-cafc-326b-a869-cda4e03bec97 | 0.9943 | -59.3619 | 2026-03-22 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 9c1a4e64-68ca-3055-811a-96f1d50c3168 | 2.6519 | -61.2826 | 2026-03-22 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| c5ad0c31-e223-3f56-a64f-b0c70399f2b1 | 2.6518 | -61.3015 | 2026-03-22 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 633e0183-c3ac-33fc-bb7b-28ade8c933d1 | 0.9943 | -59.4001 | 2026-03-22 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 338dbdc5-6df9-3614-b084-203d76ca5801 | 0.9943 | -59.381 | 2026-03-22 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 1da4a1a9-d2b1-3f3e-a828-bd7e04f6cd1d | -22.16504 | -51.36774 | 2026-03-22 00:39:00 | TERRA_M-M | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 21d80009-d0a4-3449-b405-0d729e279228 | 0.9761 | -59.3811 | 2026-03-22 00:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 8541696e-af3a-3695-a48e-0d439608ad9e | 0.9943 | -59.381 | 2026-03-22 00:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 157.7 |
| bb38cc5a-715a-38d3-a35f-22a6e03433e9 | 0.9943 | -59.4001 | 2026-03-22 00:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 0de1f8d7-c4b9-30f4-9190-3adb91d42153 | 2.6518 | -61.3015 | 2026-03-22 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 188.7 |
| 4a18adb8-6e48-3ab9-9501-3fa0d0380e8c | 2.6519 | -61.2826 | 2026-03-22 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 94.0 |
| ca8adfd7-6e99-35af-9792-a78e5d466ab7 | 2.6518 | -61.3203 | 2026-03-22 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 16b3a3e9-8e3c-3e53-bb84-cb7a566d68d6 | -1.55537 | -54.01027 | 2026-03-22 00:43:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e48f9554-e553-3c8f-aecc-11d17beca418 | -1.55926 | -54.00391 | 2026-03-22 00:43:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0a1309d6-9213-3c9b-8271-ce9bccdd89fe | -1.56073 | -54.01422 | 2026-03-22 00:43:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 43f3a24b-20b5-363c-a1d5-aee1ffbad0d3 | 1.48703 | -59.9529 | 2026-03-22 00:45:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae23d8c6-855c-3afc-b755-a3a8832d7a8b | 1.20808 | -59.97379 | 2026-03-22 00:45:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ab21e803-07a2-3123-9ed1-eca5aa914577 | 2.59424 | -60.60074 | 2026-03-22 00:45:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 552383d8-5834-3ab6-a96f-613157092c81 | 2.77752 | -60.31634 | 2026-03-22 00:45:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 97114e12-c463-31e9-9bbd-22efa8d320d8 | 0.9932 | -59.38462 | 2026-03-22 00:45:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 58c25e00-37bc-36a7-a297-37279cb72788 | 0.86335 | -60.25254 | 2026-03-22 00:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9bf9a78e-a491-335d-93dd-1236c911f1c2 | 2.64678 | -61.31687 | 2026-03-22 00:45:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cf31d9cf-b54d-339f-a2d9-b254434d3749 | 0.98229 | -59.39357 | 2026-03-22 00:45:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| dcbf526d-8b71-3978-89b8-51fe93adeba9 | 0.99461 | -59.37442 | 2026-03-22 00:45:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d8d5368f-b64e-3720-b39d-9b34598cc3cb | 3.90715 | -60.93909 | 2026-03-22 00:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f540dfee-fb26-35ee-91fc-af244170ef9e | 1.04265 | -60.36108 | 2026-03-22 00:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 26.2 |
| f7032662-1e16-3276-a787-5ced5c8d9bfd | 2.06555 | -60.21163 | 2026-03-22 00:45:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 137757c9-2a97-34b4-a806-f980db9dc2d3 | 1.64441 | -60.2998 | 2026-03-22 00:45:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7bdc626c-4263-332d-b564-d3f97c7c9e96 | 1.11926 | -60.17808 | 2026-03-22 00:45:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0f49b146-8195-383d-bff0-9eb381585a1d | 0.98513 | -59.37309 | 2026-03-22 00:45:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 19f8a3fd-dbf7-36cb-9202-2654113e0c47 | 0.57508 | -59.90486 | 2026-03-22 00:45:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a85cecb4-562b-3178-8087-524654bb1996 | 2.65221 | -61.27838 | 2026-03-22 00:45:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c9c92de4-d435-3430-9ae5-d3cea782f67d | 2.59506 | -60.59535 | 2026-03-22 00:45:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d01e4492-ca59-3ff6-9a6a-a0f5f3c34e6d | 0.57282 | -59.91005 | 2026-03-22 00:45:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a2ff9958-617c-3458-930b-c3693a764aea | 1.21084 | -59.96938 | 2026-03-22 00:45:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4d355dc8-287d-38d6-97c4-01927aca9ff7 | 1.08486 | -60.34911 | 2026-03-22 00:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0512ea96-6725-37c7-8706-31444be5b9b4 | 1.95221 | -60.58605 | 2026-03-22 00:45:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 46792539-cfaa-3aae-a126-0343a6d193aa | 1.08061 | -59.72876 | 2026-03-22 00:45:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c6276b4e-55a4-3a3d-9a8d-893cc0976b31 | 2.65041 | -61.29117 | 2026-03-22 00:45:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 147.8 |
| f06e17be-b30b-301f-a144-be7f26d9e403 | 1.15916 | -60.33041 | 2026-03-22 00:45:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 351f5551-6ae9-3967-8890-bad29d257730 | 2.04224 | -61.26833 | 2026-03-22 00:45:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f6e97ba3-0812-3de1-a818-213b5949dbc2 | 0.98371 | -59.38331 | 2026-03-22 00:45:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 190.5 |
| e69ce24d-3e24-3a3a-843a-8347bdaae47c | 2.6486 | -61.30397 | 2026-03-22 00:45:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 202.2 |
| cb2fe759-3ca6-374b-a45d-2e7d18764e30 | 2.11932 | -61.21868 | 2026-03-22 00:45:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 22c0b6bb-0dd6-36e3-accc-8f8a6afa0f28 | 1.54828 | -60.25735 | 2026-03-22 00:45:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0358cc47-1ca6-3d37-b2af-ae1d08852ef7 | 0.75179 | -60.54506 | 2026-03-22 00:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c6c82628-e6e8-3901-b4b7-ac6df91aa31b | 2.11751 | -61.23165 | 2026-03-22 00:45:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8a6a21c2-7d13-3849-ad37-3fd4c3b65e6d | 3.22726 | -61.19093 | 2026-03-22 00:45:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5dd9550d-af16-34b8-9335-743536ae5dc6 | 0.99179 | -59.39489 | 2026-03-22 00:45:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 60fe5fca-b7b2-3792-8070-a1c15b879534 | 2.94096 | -60.75182 | 2026-03-22 00:45:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5e6a540-1f80-3815-a3e2-0d85042ce9ee | 1.34471 | -60.02749 | 2026-03-22 00:45:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b85e73a3-14aa-3abe-b26a-7ae4b45d7266 | 1.11766 | -60.18944 | 2026-03-22 00:45:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 83a0827a-d893-31d1-ac85-f108f9c317f4 | 1.95557 | -60.62852 | 2026-03-22 00:45:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a064b763-c96d-3962-bde2-029ced6fe2c8 | 3.22551 | -61.20336 | 2026-03-22 00:45:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1a94414c-ed1a-38d2-a731-fce07b43bfc8 | 0.65907 | -60.60675 | 2026-03-22 00:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1c4bee61-4a19-31a9-a6e2-12a9a03fd434 | 2.94059 | -60.75744 | 2026-03-22 00:45:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f5a4abf6-94eb-3ebe-84d2-87b8bf562707 | 2.03584 | -61.2731 | 2026-03-22 00:45:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b27f7ea6-b899-36e7-aa9c-c851dd402ea9 | 4.39126 | -59.77789 | 2026-03-22 00:48:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac28632b-71d0-3e77-ae0d-ac7e9afd99dc | 4.39267 | -59.76799 | 2026-03-22 00:48:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6cf42aff-8af4-3338-82d2-7836bc919a7a | 2.6336 | -61.2828 | 2026-03-22 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 43a5529c-b427-388f-b12f-2174ec4a6134 | 0.9761 | -59.3811 | 2026-03-22 00:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 133.6 |
| b7a74d15-8f31-3ba6-9b6e-55ca76f54b28 | 2.6336 | -61.3017 | 2026-03-22 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 92e5eb64-dfe3-35ea-99a6-6b2d702fd828 | 2.6518 | -61.3015 | 2026-03-22 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 212.5 |
| c4b5c16f-bdb3-38c7-a042-229d0d62006e | 2.6519 | -61.2826 | 2026-03-22 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 172.5 |
| de60a7bf-a22e-3d43-8402-059f91944b68 | 0.9943 | -59.381 | 2026-03-22 00:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 112.0 |
| b8fef9e1-1421-3dc1-931f-69831e724350 | 2.6336 | -61.3017 | 2026-03-22 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 328df1c0-9377-3c3a-8de4-d91d1fe4318d | 2.6518 | -61.3015 | 2026-03-22 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 237.5 |
| 01044e47-d4dc-363f-823e-a7c3c365d363 | 0.9943 | -59.4001 | 2026-03-22 01:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 1c37754a-2ba2-34fa-8212-8d16a8e94cc7 | 0.9761 | -59.3811 | 2026-03-22 01:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 3811ccb1-73bd-33b6-abaf-690bbda5fb36 | 2.6519 | -61.2826 | 2026-03-22 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 307.8 |
| 1c8cf0c1-5232-3421-84cc-5f230b0fd03d | 2.6336 | -61.2828 | 2026-03-22 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 183.4 |
| c4068ef4-0c7d-3712-9003-5fed879b10ef | 2.6701 | -61.3012 | 2026-03-22 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0c63653e-1032-35e9-9748-dfb81c08bda1 | 2.6701 | -61.2823 | 2026-03-22 01:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |


[Clique aqui para ver as próximas entradas](README2.md)
