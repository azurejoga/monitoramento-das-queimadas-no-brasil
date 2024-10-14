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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5006396c-4c87-3e2f-837b-639510e8b2ca | -12.4952 | -44.330399 | 2024-10-14 00:36:25 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9b1612-e2f6-3c25-acf7-125150bd0ce0 | -12.4967 | -44.337399 | 2024-10-14 00:36:25 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e085f3d9-cb5c-3fbf-834d-1f26628e4ce4 | -12.2873 | -43.825401 | 2024-10-14 00:36:27 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 622a068b-9088-3135-9e2f-e47ce26878bd | -12.2889 | -43.8325 | 2024-10-14 00:36:27 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f78f6183-50f3-3d83-b04e-d01d0d4a980a | -12.0891 | -43.188499 | 2024-10-14 00:36:28 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5f34f064-a318-3d93-90a5-89140424f381 | -12.0907 | -43.195801 | 2024-10-14 00:36:28 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 517f3eed-2319-32d2-bedc-577b4500b4ad | -12.0972 | -43.178902 | 2024-10-14 00:36:28 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2ea37fb4-fc8d-341a-a14d-ecebd94aabd3 | -12.0989 | -43.186199 | 2024-10-14 00:36:28 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 76c89e97-cea4-3fac-8520-1c627a26fdb9 | -12.1005 | -43.193401 | 2024-10-14 00:36:28 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 37c97a49-392f-3563-9cf3-67a39413a3a1 | -11.1748 | -39.9142 | 2024-10-14 00:36:30 | METOP-C | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a686489b-6268-3e6e-8456-f55a030b6ea4 | -11.1795 | -39.891201 | 2024-10-14 00:36:30 | METOP-C | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4061e6e2-4e15-3382-9389-b6aae81fa1e7 | -11.182 | -39.901501 | 2024-10-14 00:36:30 | METOP-C | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 811a8cb2-d3b6-3c37-ae00-9fc47969c6b0 | -11.1845 | -39.9118 | 2024-10-14 00:36:30 | METOP-C | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 20c5b000-5e04-3b5d-be99-b11e0fbacb10 | -11.1698 | -39.8936 | 2024-10-14 00:36:30 | METOP-C | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ba453f2a-6cda-303f-90db-51dc54feee31 | -11.1723 | -39.9039 | 2024-10-14 00:36:30 | METOP-C | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| de177eb8-0d65-398d-904f-3c3577ee26da | -11.9133 | -43.321201 | 2024-10-14 00:36:31 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9eef65db-b37a-3c71-add6-9aafe8174e84 | -11.915 | -43.3284 | 2024-10-14 00:36:31 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 172cf51b-e48b-30f6-9379-b0a631ed5729 | -11.8974 | -43.879299 | 2024-10-14 00:36:33 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c14b6fc-ae68-38e1-9bff-1ea99570f1c0 | -11.899 | -43.886398 | 2024-10-14 00:36:33 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f9051e9-4cf4-38ed-8da1-39a22336bb37 | -11.8876 | -43.881599 | 2024-10-14 00:36:34 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39962f28-8f26-38df-b049-41223b08fd5a | -11.8892 | -43.888699 | 2024-10-14 00:36:34 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43f612a8-de30-3f24-8fe4-60d3461fa118 | -11.8908 | -43.895699 | 2024-10-14 00:36:34 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a548774-ba38-3771-906b-dcfdc0669356 | -11.8778 | -43.8839 | 2024-10-14 00:36:34 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f6f75b75-62dc-335b-90f8-249cacf59505 | -11.8794 | -43.8909 | 2024-10-14 00:36:34 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b152f594-648d-3f21-bee3-8efa436a0bd5 | -12.9275 | -49.253101 | 2024-10-14 00:36:36 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16d0047a-b1c7-3e3e-b7dc-3e4bc7afe4de | -12.9177 | -49.2551 | 2024-10-14 00:36:36 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7f29957-22c9-3afa-b511-e1b7a6d0443c | -11.4898 | -43.230598 | 2024-10-14 00:36:38 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1d66630c-22f0-3cd6-b456-af03decb83f8 | -11.3491 | -43.202499 | 2024-10-14 00:36:40 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cb1d64cf-2499-37bd-a750-42acdd027a9c | -13.135 | -51.681198 | 2024-10-14 00:36:40 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbe3d093-76bb-3694-8b49-37e8de9a7a4b | -10.593 | -40.2836 | 2024-10-14 00:36:41 | METOP-C | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5f66b766-b94c-35f7-83f7-04d4f4180f13 | -11.4634 | -43.921101 | 2024-10-14 00:36:41 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76dad35a-8838-31ca-b13c-c890529a1a3d | -11.4667 | -43.9352 | 2024-10-14 00:36:41 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 19211e49-5f50-3ca7-b1da-37ee8fcc72cc | -13.1223 | -51.668098 | 2024-10-14 00:36:41 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 53f04257-9a1d-32d2-87d7-7e083a0e80be | -13.1253 | -51.683201 | 2024-10-14 00:36:41 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e46894fe-42c7-3edd-bcbe-65b63c1d39ee | -13.1283 | -51.6982 | 2024-10-14 00:36:41 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 923456a3-c4d9-307a-babc-bed94998679f | -13.1155 | -51.685101 | 2024-10-14 00:36:41 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0276182e-dae3-3f82-8de5-5f7df0ee3193 | -17.0001 | -57.4381 | 2024-10-14 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| be018273-6d02-3a3f-8f0d-1d2fda85a202 | -17.0004 | -57.4176 | 2024-10-14 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 846ae5bc-090f-3963-875f-c3fd2cdfdda9 | -17.0197 | -57.4358 | 2024-10-14 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 86b4432f-ea6c-354f-afc1-0ff994ab3c2e | -17.02 | -57.4153 | 2024-10-14 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| a559c07c-fd3b-35cb-8414-7b71093a71e4 | -17.0823 | -56.0076 | 2024-10-14 00:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 5c0e2f67-77ab-31e4-aa0f-c5d422d5a027 | -17.0826 | -55.9868 | 2024-10-14 00:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 35bcfa85-ccd4-3034-9dfd-c41fc982f481 | -17.1267 | -56.8693 | 2024-10-14 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 9e40f791-633f-3e54-8788-f9603f1ff241 | -17.1271 | -56.8486 | 2024-10-14 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| a7ca597f-2a74-38bf-98a8-361084a66771 | -17.1464 | -56.8669 | 2024-10-14 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 8e66da2f-0979-367d-9752-7893abc8a1cd | -17.1467 | -56.8463 | 2024-10-14 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| fbfd606d-bf35-3d02-8a32-7918243f1436 | -17.1957 | -57.4562 | 2024-10-14 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| ac5a4950-fa18-3332-96f9-5265dce30b79 | -17.196 | -57.4357 | 2024-10-14 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| d9f782ad-b00a-3935-9961-b86c5bc3895e | -11.1081 | -43.320301 | 2024-10-14 00:36:44 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 48524c77-8c89-375d-adcc-a5c2a39d1fe8 | -11.1098 | -43.327599 | 2024-10-14 00:36:44 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4d7e6710-b9cc-34ae-8f94-d9d566e91794 | -11.1114 | -43.334801 | 2024-10-14 00:36:44 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6dc8b964-b8a3-3b85-97a9-68c4226bafcb | -11.1 | -43.329899 | 2024-10-14 00:36:44 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d568ae57-6516-3319-bb17-05ff54149dc2 | -11.1016 | -43.337101 | 2024-10-14 00:36:44 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 00b744d2-089e-36b2-8512-4ea1e306d856 | -11.9796 | -47.531502 | 2024-10-14 00:36:45 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0732952c-6586-38e1-ab7a-143fbe8bbf27 | -17.6471 | -56.3084 | 2024-10-14 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| c31c22e9-1f30-3d7a-b17f-0db58383c8b4 | -17.6474 | -56.2876 | 2024-10-14 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 42e5802e-bb2b-3096-a05e-2f3cb21e5d85 | -17.6876 | -56.2409 | 2024-10-14 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 9e3f05a2-5ea9-3f57-9281-f439e7febed9 | -17.7264 | -56.2774 | 2024-10-14 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| befe1f8e-1755-3c54-a4ba-aacbdc7d759c | -11.1024 | -44.461399 | 2024-10-14 00:36:48 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e6c3a87-1413-362a-abd7-342ed6a3f98e | -11.104 | -44.4683 | 2024-10-14 00:36:48 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f4ac843c-b715-30a5-bc12-ec53b8c1ddf2 | -18.2559 | -56.4988 | 2024-10-14 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.6 |
| 6ddefb55-e352-30ed-9584-47a3beff2c69 | -18.2562 | -56.478 | 2024-10-14 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| d40bf876-36b7-34f7-b71a-d0d5cd6bcdf5 | -12.324 | -50.231899 | 2024-10-14 00:36:49 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14c9c1bf-f84f-3a59-9ef4-526e2fabc1b0 | -12.3069 | -50.247601 | 2024-10-14 00:36:49 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7141349b-af18-3d04-b3d6-fbb4f3e9c52a | -12.8657 | -53.510502 | 2024-10-14 00:36:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a7400c4-e912-3a58-8f6b-330ec31f178b | -12.8696 | -53.530399 | 2024-10-14 00:36:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91148608-6841-38e1-920a-903e7e28f1c8 | -10.4853 | -42.423599 | 2024-10-14 00:36:51 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c41dbefa-d0f7-38cc-b5f5-18eafd3f0f0c | -10.4871 | -42.4314 | 2024-10-14 00:36:51 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 501ed027-894b-31ca-9ce8-99aed9be3b42 | -10.489 | -42.439201 | 2024-10-14 00:36:51 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6388f7fe-7cd4-3566-91d8-24bb5c6d72dc | -10.4908 | -42.446999 | 2024-10-14 00:36:51 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| eeada40c-394d-37cc-aa8b-4cc6f4397407 | -10.4774 | -42.433701 | 2024-10-14 00:36:51 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ff53f23d-a1a1-3afa-9e08-0e319cebdf15 | -10.4793 | -42.441502 | 2024-10-14 00:36:51 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8a6fff5a-a400-3d93-8575-61ce237c1d17 | -10.9649 | -44.536999 | 2024-10-14 00:36:51 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 67a28c55-f932-349c-9fd1-81b9733a1f8a | -10.9665 | -44.543999 | 2024-10-14 00:36:51 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77abfd24-fc36-3fcf-82b4-c5bc0e18c57b | -19.0724 | -48.3148 | 2024-10-14 00:36:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4a2ebe69-b0fe-380b-b8c5-2c3219f068ff | -11.7377 | -48.361401 | 2024-10-14 00:36:52 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b8ca6e1-c970-3e47-b15d-55e5500fdc91 | -11.7396 | -48.3703 | 2024-10-14 00:36:52 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2897757a-dc4c-3b3f-8fc0-dbd51c8cc8c7 | -10.9299 | -44.654701 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c812c7ff-498e-3e1e-8860-c9328840afcc | -10.9315 | -44.661701 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 404da488-195d-3239-a78b-dec869bc3ca2 | -10.9182 | -44.693901 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4456131-1889-3857-8d09-da3b0c92bea8 | -10.9198 | -44.700901 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9d01d8b-e370-391c-b8f6-d62c693b1912 | -10.9214 | -44.707802 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c586709-8a41-3ac4-a7f3-0539e7e5f6c2 | -10.9069 | -44.689301 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87a1a485-deff-33a1-a217-2acfec94031f | -10.9084 | -44.696201 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 766c782a-617a-36e8-bb42-7a4367ab75db | -10.91 | -44.703201 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff9fd7a2-4be4-33f8-b02f-9cdf873f95a6 | -10.9116 | -44.710098 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe619089-148f-30d6-9eb1-5893f05a70e1 | -10.9429 | -44.666401 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ed0b61f-807b-3155-a628-18fb1baa23d2 | -10.9445 | -44.673302 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea5fe44-6f5f-33ee-bf61-4ad10777e8c9 | -10.9461 | -44.680199 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00c17229-9dd2-3d7b-ac37-8bc32647a3ea | -10.9476 | -44.687199 | 2024-10-14 00:36:52 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 342226f5-651d-38a7-9121-0add10811d69 | -11.0308 | -45.282299 | 2024-10-14 00:36:53 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15789519-6d0a-3ffc-a46c-34a86cc5819c | -10.8986 | -44.698399 | 2024-10-14 00:36:53 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e362294a-088a-3d5b-8073-9a6970455331 | -10.9002 | -44.705399 | 2024-10-14 00:36:53 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca8a4f42-c24e-37dc-8c5a-9d9b1fe00bbc | -10.6668 | -44.4958 | 2024-10-14 00:36:56 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 216dce97-73e0-363b-9ad7-65390a58f033 | -10.6684 | -44.5028 | 2024-10-14 00:36:56 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a03ee8ad-4963-34c7-8388-3f1967364cf0 | -10.295 | -43.4193 | 2024-10-14 00:36:58 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05743def-61e4-3ac1-b072-261b670666a0 | -10.2967 | -43.426498 | 2024-10-14 00:36:58 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f4adbf7-3d9b-3253-860a-c4208aa937c8 | -11.2068 | -47.846901 | 2024-10-14 00:36:59 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65306f9f-69a0-31e3-840d-c01aa57c1542 | -11.2085 | -47.855099 | 2024-10-14 00:36:59 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3a08873-09ce-32ae-9b28-81d9a793cd03 | -11.197 | -47.848999 | 2024-10-14 00:36:59 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
