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
| 8de351a0-0f51-315e-96df-60c7028c398b | -18.97195 | -52.93152 | 2026-02-20 04:14:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ec3dc1ae-00e0-394c-bba0-37f42114a938 | -22.24992 | -47.22746 | 2026-02-20 04:14:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe9c8388-b350-3585-ab24-feb7a53c52c5 | -20.47445 | -50.37226 | 2026-02-20 04:14:00 | NOAA-20 | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6890386a-a42f-383c-a98a-f2f7c925eaef | -20.93699 | -48.65637 | 2026-02-20 04:14:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 365f79fc-136e-3ab4-aec0-b5d75be59070 | -20.98141 | -48.66062 | 2026-02-20 04:14:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 35554509-6b95-3db2-8860-f8ae2bab0d12 | -20.98222 | -48.65606 | 2026-02-20 04:14:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 089eae9e-12d6-3c88-98bb-babede8ce1ad | -22.25041 | -47.22696 | 2026-02-20 04:14:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ef5e98c-28a3-33a5-80fe-b430c858ae47 | -21.63783 | -48.98352 | 2026-02-20 04:14:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66ee6c2a-05ac-3c6c-9df9-90c59dfebc27 | -22.93082 | -48.67771 | 2026-02-20 04:14:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae8c80fa-f1e6-30a8-89c8-480474bba848 | -20.92893 | -48.65932 | 2026-02-20 04:14:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c441eaf1-5f5e-3766-b6b6-ea044c950375 | -22.40167 | -47.10124 | 2026-02-20 04:14:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19cc7394-a689-350e-b7a9-2c7220191718 | -20.93337 | -48.6556 | 2026-02-20 04:14:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 65ac6efe-2523-336a-b659-634c9c41a08f | -20.93174 | -48.66461 | 2026-02-20 04:14:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 40ee8867-63d9-3112-b358-875bbeae3e3e | -20.74131 | -50.53748 | 2026-02-20 04:14:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ced5b65d-1eb3-3bda-81fb-5678c8caf22f | -22.02531 | -49.50451 | 2026-02-20 04:14:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 83fca8ac-f898-3989-9bb8-158824c54e93 | -22.30107 | -47.17611 | 2026-02-20 04:14:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fc928a0-38e2-3668-87e4-477b2570187e | 2.562 | -60.5648 | 2026-02-20 04:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.5 |
| e4ed6d58-eb74-3657-a276-2c39e30f52f3 | 2.562 | -60.5648 | 2026-02-20 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 10886b96-9ef6-3b99-8b80-7c16661ee5f9 | 2.562 | -60.5648 | 2026-02-20 04:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 93.9 |
| c0771020-98f3-3f08-9096-686bc976e6d6 | 2.562 | -60.5648 | 2026-02-20 04:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 4e6ef116-8e3a-3a59-aa40-33629691e1d3 | 2.68016 | -60.22104 | 2026-02-20 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 63f64fc9-fb65-388d-b8e5-de79098a7c0e | 4.07496 | -60.18746 | 2026-02-20 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04a7e54b-17f4-3ef8-bd10-f07451019ead | 4.48354 | -60.56544 | 2026-02-20 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5be1399-ddd5-37f5-99b7-76949bfca9fc | 3.23199 | -61.19625 | 2026-02-20 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f76a94c0-42b6-31bc-9ba4-b33d1916afd0 | 4.47928 | -60.57248 | 2026-02-20 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89dadd0e-a3de-3cb3-8196-8f66992bd056 | 4.48396 | -60.56835 | 2026-02-20 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b45cd2a3-459f-3d99-9eb3-8faaf262209a | 4.84009 | -60.05731 | 2026-02-20 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48fe7175-ea27-3af0-b643-802f5c099ddd | 4.47738 | -60.596 | 2026-02-20 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22538a5a-398b-3c1d-b4c4-f7dbdc37efc6 | 3.23247 | -61.19959 | 2026-02-20 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaf30afb-ca98-3dd3-b1c9-ed859f0f678c | 2.68509 | -60.25434 | 2026-02-20 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85ab3731-c7ff-360b-8db8-19662686d396 | 4.47846 | -60.56682 | 2026-02-20 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c2ad113-a919-3980-acc7-baf5f858ad46 | 2.69002 | -60.25359 | 2026-02-20 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a71c97ec-5b24-38f5-be3a-cd8e782cfb10 | 3.22754 | -61.19717 | 2026-02-20 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 317133de-0795-3de5-98bf-a74327d688a1 | 4.47887 | -60.56964 | 2026-02-20 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 221c34e4-16d9-38b1-9f8c-82cf80bc4dec | 2.7671 | -60.28597 | 2026-02-20 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18917e7e-4d54-37bd-a1be-8fcb77108af0 | 4.47782 | -60.59906 | 2026-02-20 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af43d572-e23e-3359-8df7-2637d4d59f83 | 2.69739 | -60.23542 | 2026-02-20 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef80275a-9b7f-3747-a993-e77fc28d094b | 3.22805 | -61.20051 | 2026-02-20 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb1464ed-669c-37e9-b402-ffb826c499d9 | 2.76587 | -60.28785 | 2026-02-20 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 044171f2-f1ec-3e80-9f98-98cc52ab2952 | 4.05763 | -61.10666 | 2026-02-20 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ceee80e-1bc5-3e30-9df2-43c735c061ec | 2.70231 | -60.23467 | 2026-02-20 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b51f995-d55d-3078-a38d-741d24270ee6 | 2.69329 | -60.24172 | 2026-02-20 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d582b89-3cf5-388f-8303-9b0d38407721 | 4.10721 | -60.64433 | 2026-02-20 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0882a86-e68f-3d61-af53-a86163b9e061 | 4.10768 | -60.64744 | 2026-02-20 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d0d70c9-4860-39c1-a044-0b752621d495 | 1.12849 | -60.52311 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 172980fc-ba53-3ac9-b15e-472088ec6d1f | 1.82493 | -60.8489 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db6ca06b-68d9-340f-bbb8-df41b1756486 | 1.37681 | -60.31429 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 776fccb8-50de-3ba7-9acf-a4450ff3a098 | 0.45331 | -60.4082 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 29f99ac3-e6de-3f52-9050-a9f5ebce6bde | 1.37464 | -60.30759 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47d7f72c-c74b-3d59-9ae5-146aeb90eef8 | 1.36235 | -60.06246 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6931c57c-40a4-3fcc-8574-0af96b3b98cd | 0.4565 | -60.39694 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1668fed6-c1f6-3d2a-8976-5330cdcd1bbe | 1.37869 | -60.30151 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca6b8318-e8d9-306b-83c4-cf9c3de2ff3f | 1.15359 | -60.33163 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2c631852-d148-32a5-a12f-c874d0404dc1 | 2.55616 | -60.56082 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| f38f87d6-0d9f-3c65-9191-26a0a1af67e2 | 1.37544 | -60.31293 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95111beb-8aa0-3755-978c-f1b603f12cd8 | 1.82955 | -60.8452 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 447ee6d5-b21a-3f94-8bf9-3a43fa27e55d | 2.55573 | -60.55793 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f12139df-6c2c-38e5-baf6-cea9006e67e2 | 2.56207 | -60.56592 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c1828377-3ca3-3af5-9d7c-a62426b23e24 | 2.56119 | -60.5601 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 73f03b5e-411c-3c49-92db-ca231bc0506a | 0.93545 | -60.25601 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b414ad17-7527-3382-8cf0-2c755923ba05 | 0.45169 | -60.39767 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 74db2582-18b9-32b2-8335-64efbdd474f1 | 2.53953 | -60.72594 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7714cd54-a99f-39ee-926d-b542232f329d | 0.46131 | -60.39624 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a5247f38-9b91-3a9f-8d19-fc909ec4db1c | 0.47093 | -60.39474 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a629eb66-5c98-3e6f-acf6-add51b02dd6c | 0.98261 | -60.42791 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2ed6512-f3ae-3a23-ad85-d57c96356310 | 0.46694 | -60.40075 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a94fa88-df43-36f2-a60d-3230c7bc2dbf | 0.46213 | -60.4015 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a667cdb5-5185-32b9-b390-231fea81cb35 | 2.54417 | -60.7222 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4c06c0c2-237d-3249-999c-1b7a56228592 | 0.93577 | -60.25817 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 178e0019-a161-3c9c-9a64-8ac66e4f24ef | 1.37597 | -60.30894 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b54a0e79-2a2f-39dd-93d5-53ee12e58a0c | 1.37997 | -60.30288 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 719fa939-46ef-3b01-8165-8cde938ef773 | 2.534 | -60.72372 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dc0edc8-774a-3619-9b5b-3541bc2f0a47 | 1.83 | -60.84814 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 063ab62a-28b5-335c-97e1-b4434c5a2cce | 0.94057 | -60.25745 | 2026-02-20 04:57:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b17e5c0b-328d-36f5-9d27-1e1076cd287f | 1.38029 | -60.31218 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd3f00e4-fc3b-3685-9a22-cfbeaad49d42 | 0.45569 | -60.39169 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bc852a70-4300-3369-8dc4-e7a5e0f8395b | 0.45088 | -60.39242 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d4ef7ab4-0d05-3693-b61d-640e63eab9d7 | 2.5566 | -60.56372 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 07e76ccc-031d-32b5-b6c7-7f6245632a09 | 1.8291 | -60.84223 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f34ff887-44e8-32d0-8588-f5cbdcf82e30 | 1.82448 | -60.84594 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1df1310e-1b3f-330f-8ce4-65fc4fbb66b5 | 2.55704 | -60.56665 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 98ed016d-d4a8-3595-ba90-1bd23231c193 | 1.97688 | -60.69887 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0108b9e7-de05-3368-bc77-086c50f638fa | 2.56076 | -60.55728 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cdc52cbd-8f8a-3521-8f15-cc010450f6a8 | 0.94109 | -60.26057 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f0978807-fe21-31ec-8905-558b441bf8a3 | 2.56163 | -60.56299 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| cef8191e-35bb-34a9-a32d-9ec6d7915438 | 1.82403 | -60.84298 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 904241fe-208a-38a1-963d-a2ef60488d72 | 1.37949 | -60.30683 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ad44645-49fd-3037-bdd9-6c41ff73d740 | 0.47656 | -60.3993 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13bcadc1-c542-31b6-a0f2-44ae9afa95cf | 0.47574 | -60.39404 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f7bfc2d-9d7b-320c-ac73-b76bba11cab9 | 1.3811 | -60.31757 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb840f5f-5495-3f12-a024-b759d9c1b240 | 1.38166 | -60.31356 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84607406-b603-3993-a7c9-85f6ddf18e08 | 0.47174 | -60.39999 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9990ab2c-210a-3ede-a2a5-1927e18ac56f | 0.46612 | -60.39549 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ebf7f952-30bc-393c-8551-e5f5ae5c626b | 0.44769 | -60.40366 | 2026-02-20 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1953c69-5468-3480-b48f-8e0f0a359732 | 1.37513 | -60.30362 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f7a6e76-7ec4-399b-b07f-97dd69dfbcf3 | 1.15443 | -60.33696 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b7a70ad-d5ae-3d74-bb85-9dfa35bfa642 | 1.27733 | -60.41194 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8686ec25-62b1-3f9c-8171-3372f8e2ecf4 | 1.15724 | -60.32922 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f93dfc12-75fe-30ca-aa40-e8d40d3ad036 | 2.53908 | -60.72295 | 2026-02-20 04:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 314b8570-5cf7-3e92-afc7-6b27b8d9894a | 1.27406 | -60.41039 | 2026-02-20 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README5.md)
