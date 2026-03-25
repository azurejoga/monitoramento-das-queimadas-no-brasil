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
| 345cd806-91a6-3dca-a777-65106ed76f70 | 0.4101 | -60.5253 | 2026-03-25 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d09a9a9e-21b4-3886-8ea6-9f5dabbe1876 | 2.7065 | -61.3573 | 2026-03-25 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 5017fec8-bd7c-31f7-beb9-f5024555b176 | 0.8297 | -59.9161 | 2026-03-25 00:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d0775e13-d321-3710-90a2-d761328f36ed | 1.9238 | -60.2879 | 2026-03-25 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| faf633f6-f079-3a97-b155-cd9943bc7c4f | 2.743 | -61.3568 | 2026-03-25 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 02401fb3-9b1c-315b-a4b9-ad373fdec454 | 1.9411 | -60.8943 | 2026-03-25 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 29e22aa8-262e-3edc-a5cd-db1a4ff64aa0 | 1.9056 | -60.2691 | 2026-03-25 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 13024d33-f356-3b03-8002-8d94e98c02ce | 0.4465 | -60.5252 | 2026-03-25 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b4e88fb0-0390-393f-a437-3a5032e082f5 | 0.7566 | -60.2396 | 2026-03-25 00:00:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 5f2bef71-3b33-33b2-aa86-f8fbfe1c3993 | 1.9593 | -60.913 | 2026-03-25 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 176bf1d7-3b5e-348a-9be4-ba2cffffb84b | 1.9055 | -60.2881 | 2026-03-25 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 26d311ed-3579-3e67-b049-2d6ca7dc8df9 | 0.4283 | -60.5063 | 2026-03-25 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 5a825733-9b6e-39bc-8abe-69e87cfa1640 | 2.032 | -61.1013 | 2026-03-25 00:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 3cae5262-d8cd-3a56-a665-8b9e9f55d720 | 0.4466 | -60.5063 | 2026-03-25 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d6c8949b-100a-3e70-a033-f2e2f3c15304 | 2.7247 | -61.3571 | 2026-03-25 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 165.7 |
| d5151c84-701e-31dc-9110-1ff5d7acd342 | 1.9238 | -60.2689 | 2026-03-25 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 5be3b14a-cb4c-3612-bf13-63cb067de018 | 2.7248 | -61.3382 | 2026-03-25 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 2261d94d-7575-3eb5-871d-c470be262da4 | 2.7065 | -61.3384 | 2026-03-25 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| af6f7b02-98f5-3dce-bcbc-95c05d92ed85 | 0.4283 | -60.5253 | 2026-03-25 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 4ef9d5db-9e38-3b9b-b641-3de64d486588 | 0.4101 | -60.5064 | 2026-03-25 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c8eb2c7c-7f47-3ca3-a615-2a74aaa3af0d | 1.9411 | -60.9132 | 2026-03-25 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 211.3 |
| 65226c2f-9340-34df-bc19-1ba03c22d836 | 0.8301 | -59.3628 | 2026-03-25 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 219.6 |
| f14b4596-d291-3305-909a-1d0dd743cc1e | 2.032 | -61.1013 | 2026-03-25 00:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 93.0 |
| dd933362-3e30-317e-bb29-30b4938419d4 | 1.9593 | -60.913 | 2026-03-25 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.0 |
| e78f725b-d18a-38a5-9fdb-d50752aa6b0e | 0.8119 | -59.3438 | 2026-03-25 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 267.7 |
| 09c108bc-f986-3fd2-95c8-7509f9d16c55 | 0.7752 | -59.5732 | 2026-03-25 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 84.6 |
| b94b0676-3aeb-3828-8266-61dd3ee680fd | 0.8297 | -59.9161 | 2026-03-25 00:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| cf5d9c4a-01b1-3153-b7f3-c4a3042b7a13 | 2.7247 | -61.3759 | 2026-03-25 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 3704871c-46e7-31b6-bcfd-bcfc147db252 | 2.7248 | -61.3382 | 2026-03-25 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 46ae923d-73c8-3884-af16-4de33db66674 | 0.8119 | -59.382 | 2026-03-25 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 6ac72945-dc0b-3f7b-9677-38464f522f19 | 1.9594 | -60.8941 | 2026-03-25 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 7a1fc71e-f222-31d2-ad33-a44f56d32342 | 0.7566 | -60.2396 | 2026-03-25 00:10:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 136e09f2-aa69-3065-baab-420b8289e320 | 3.0177 | -60.8991 | 2026-03-25 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 14ca7c0d-312c-314e-a8e0-f7bb51e912da | 1.9411 | -60.9132 | 2026-03-25 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 1a3486dc-d86c-35b5-8f88-13d1809bf47e | 2.7065 | -61.3384 | 2026-03-25 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ee621832-35df-3037-888c-8c1cfbd6dc6e | 0.8119 | -59.3629 | 2026-03-25 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 349.1 |
| bc5b3bdc-6ccb-3789-ab24-686a145b7995 | 0.8301 | -59.3437 | 2026-03-25 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 115.6 |
| b9b594e1-56d1-319b-8061-51b6853b0831 | 1.9411 | -60.8943 | 2026-03-25 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 58bd8515-8527-3fbb-a991-cbfedd0d3ad7 | 2.7247 | -61.3571 | 2026-03-25 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 113.1 |
| e121fe46-7379-3f1b-8b09-0936641526db | 0.8119 | -59.3246 | 2026-03-25 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 499fcb3b-e69a-3b29-8538-d776a3a553d8 | 2.7065 | -61.3573 | 2026-03-25 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 112.6 |
| cd56471b-248e-30df-89b2-64e0fd6d16c9 | 1.9055 | -60.2881 | 2026-03-25 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 57465e8c-d460-3810-ae9a-ef7fb88943af | 1.9593 | -60.913 | 2026-03-25 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.4 |
| d78ce896-63fd-3491-9a4c-bf80575da562 | 1.9411 | -60.9132 | 2026-03-25 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 145.2 |
| c909cc1a-3cd0-3a37-a668-d87b170a3c55 | 1.9411 | -60.8943 | 2026-03-25 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 3f501ecd-89c8-37a5-a2f8-ec68e72cb060 | 1.9238 | -60.2689 | 2026-03-25 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d1d59262-9340-3304-9320-2039bd6b9983 | 0.7566 | -60.2396 | 2026-03-25 00:20:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 90.5 |
| ba1599b8-9f5a-3e16-bdb1-0d8e19f0394a | 1.9056 | -60.2691 | 2026-03-25 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| bff390d1-0e26-32a6-bce1-c6697bbe4455 | 2.032 | -61.1013 | 2026-03-25 00:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 70ccfbe5-6147-3686-be16-dccc4f2934e2 | 0.8301 | -59.3437 | 2026-03-25 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 5a1a0371-4f65-3536-bb9d-2d05e245f802 | 1.9411 | -60.8943 | 2026-03-25 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 38f8efc2-6ed3-3c26-b5f6-d38bc5cf4260 | 0.8301 | -59.3628 | 2026-03-25 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 227.1 |
| 4fff8967-59c5-3ec7-98e1-0b36ee76af5f | 0.8301 | -59.3819 | 2026-03-25 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c521d8ba-a5e7-364d-9693-f6f4ffe6799b | 0.8119 | -59.3438 | 2026-03-25 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 216.7 |
| ef65b95b-5113-3981-82e9-9766494598b6 | 2.7065 | -61.3573 | 2026-03-25 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6c5f59df-e6ca-301e-a86b-d9cdd8168930 | 1.9593 | -60.913 | 2026-03-25 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 4a6b9519-4b38-367f-bc5f-d6c2e4cc86fb | 0.7566 | -60.2396 | 2026-03-25 00:30:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 88.1 |
| ffdcd25e-2480-3a30-83db-5dbb73942c52 | 0.8119 | -59.382 | 2026-03-25 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 143eac5f-a723-3d0a-a01d-38fe1476ce52 | 1.9411 | -60.9132 | 2026-03-25 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 69522adf-1d57-3207-b8d4-4357fd948bb8 | 0.8119 | -59.3629 | 2026-03-25 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 317.9 |
| d9fc37e1-6338-33b3-aefc-a999167742f5 | 2.032 | -61.1013 | 2026-03-25 00:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 86e47271-761e-3615-bfa2-cbc10edb10d4 | 1.9593 | -60.913 | 2026-03-25 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1a21e3b1-2be2-3356-95c5-0f82575f1a0e | 0.8301 | -59.3628 | 2026-03-25 00:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 466104a0-3245-39e2-bcba-f8f2c47dff26 | 0.8119 | -59.382 | 2026-03-25 00:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 9ed165fa-f81c-3684-9911-701acf7d4c8a | 0.8301 | -59.3437 | 2026-03-25 00:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 31aa57b0-f301-3467-bc34-3572bc5a8711 | 1.9411 | -60.9132 | 2026-03-25 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 6d294b52-7ae8-34ed-9706-77f563e4164b | 0.8119 | -59.3629 | 2026-03-25 00:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 288.5 |
| fe166d6a-3f19-3089-a029-a4fac51025e4 | 3.8389 | -61.2816 | 2026-03-25 00:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| af1592ac-e06f-3143-b662-0233dae89e1d | 0.8119 | -59.3438 | 2026-03-25 00:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 190.4 |
| 6a677f23-c3d4-3a53-9dff-c16114fb271d | 1.9411 | -60.8943 | 2026-03-25 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2dea5443-493c-3e43-b51a-48611e364002 | 0.8301 | -59.3819 | 2026-03-25 00:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 960a0cdd-d0be-3ba0-b633-209c7d5346e3 | 1.9411 | -60.9132 | 2026-03-25 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 880a29fd-b7b7-38ab-9e4d-a4343e1e2cc0 | 0.7566 | -60.2396 | 2026-03-25 00:50:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 630f65e5-1791-388e-98f2-068b83574c48 | 0.8119 | -59.3438 | 2026-03-25 00:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 168.7 |
| 42cd77f3-02b1-32fc-8c11-fb483d03743a | 1.9411 | -60.8943 | 2026-03-25 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.3 |
| df0d3e9a-b8ae-3c92-a480-36040041c0ae | 0.8301 | -59.3628 | 2026-03-25 00:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 179.0 |
| 4479e815-6476-3907-ac76-18423b302eff | 0.8301 | -59.3437 | 2026-03-25 00:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e2ceb59e-0220-3383-9999-aea4199a10ab | 1.9593 | -60.913 | 2026-03-25 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.7 |
| f865a7c0-c948-37b2-811f-319b9a29f4d8 | 0.8119 | -59.382 | 2026-03-25 00:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 95.1 |
| e430f779-aa78-3c37-b520-ae1c337b1ee6 | 2.7247 | -61.3571 | 2026-03-25 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b2d6ff03-b1e8-3a0d-b1cb-7124c06234b0 | 2.032 | -61.1013 | 2026-03-25 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a6e8ab80-27d6-3e7f-9fbd-d3caebb60903 | 2.7065 | -61.3573 | 2026-03-25 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| cc31788f-ca0f-3d3a-a6ce-d1b704131a27 | 0.8119 | -59.3629 | 2026-03-25 00:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 243.6 |
| eb79c5a8-b0de-3a0c-a019-9b8fccfd72e1 | 2.7247 | -61.3571 | 2026-03-25 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 70a57a9f-e269-392f-b286-8d929e5c0625 | 1.9411 | -60.8943 | 2026-03-25 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.9 |
| edfb0489-cfd5-396a-b5a5-2a39d33449ef | 1.9238 | -60.2879 | 2026-03-25 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| fcb777d7-3426-3e41-a188-9c0e989a8104 | 1.9055 | -60.2881 | 2026-03-25 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0fd72c5d-9a5e-3a21-92da-0e141fc81c42 | 2.7065 | -61.3573 | 2026-03-25 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 62facf46-f49b-30f5-8b1d-381fa039ced6 | 2.032 | -61.1013 | 2026-03-25 01:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 82.9 |
| ce3400c0-6726-3489-ba8e-61e34ee31d86 | 1.9411 | -60.9132 | 2026-03-25 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 5dfa85b9-8749-3b57-b3fa-e74c9a725d5e | 3.22478 | -61.23785 | 2026-03-25 01:05:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ca425a4c-713a-3ec3-aa0e-23544929102b | 2.89149 | -61.32017 | 2026-03-25 01:05:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ec9e71f6-c1a9-3005-9be2-4b0004eb5b44 | 2.03498 | -61.11237 | 2026-03-25 01:05:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0dfda35b-59b9-371d-a537-a463816487fa | 0.81086 | -59.37735 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 2df8d2bc-c9ab-309b-a951-8d843a9ca9d8 | 2.95803 | -61.30832 | 2026-03-25 01:05:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 1ffb45e1-918a-38e5-81b4-775f3e4410a6 | 0.97513 | -59.38102 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a8d3ef8d-8147-362b-aaca-1c3d0ad3eab8 | 1.94475 | -60.90026 | 2026-03-25 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 2ed66d9d-ad6f-33bd-a3e8-3e6ccbd9ac96 | 0.94655 | -60.32138 | 2026-03-25 01:05:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 20.3 |
| cf585e2f-0c6d-350c-91c0-105b04b09956 | 1.90925 | -60.28145 | 2026-03-25 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 0859a329-9e7b-394b-9e7f-807a943918fd | 2.70249 | -61.35478 | 2026-03-25 01:05:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 31.5 |


[Clique aqui para ver as próximas entradas](README2.md)
