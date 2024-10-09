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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdf9767d-e332-33c9-8e0d-bf72f9431fff | -21.572 | -46.9898 | 2024-10-09 01:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 6090b58d-76ab-3bc1-b130-6099554080af | -21.5727 | -46.9659 | 2024-10-09 01:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 81379ca3-97aa-3fba-9de2-f5fc65f6e877 | -21.5928 | -46.9845 | 2024-10-09 01:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e9ac9e6a-cb5a-3b8a-bee3-2f019f7e46c3 | -21.5864 | -47.8827 | 2024-10-09 01:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5373d67d-9031-3dea-b51c-0a9bb9312a2d | -10.5934 | -64.499001 | 2024-10-09 01:27:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 062a6c33-d476-3b26-81cb-30471ff6429e | -10.5953 | -64.508102 | 2024-10-09 01:27:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 182717e9-1a28-3480-b3f1-06c04b23cf2a | -10.5662 | -64.467201 | 2024-10-09 01:27:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab29f97-cbd7-3282-af44-310ba9ce04ea | -10.5681 | -64.476196 | 2024-10-09 01:27:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eb0bda45-19cb-37a4-8008-1f90acb9bbfc | -10.092 | -62.5 | 2024-10-09 01:27:06 | METOP-B | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a95cf81-f525-33d8-b3a3-3a0e27ee29f4 | -10.0936 | -62.507401 | 2024-10-09 01:27:06 | METOP-B | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8ba2ce51-f31e-3037-ba2c-0c91f937c1e5 | -10.0822 | -62.502201 | 2024-10-09 01:27:06 | METOP-B | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 195426fd-9f3a-3b74-a8fb-e4b99d9c846b | -10.0838 | -62.509602 | 2024-10-09 01:27:06 | METOP-B | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f870e9de-9422-3585-9f7d-9825c79b7c38 | -8.2924 | -55.0854 | 2024-10-09 01:27:07 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 082b5b20-467f-350d-814c-1a1bdcac2faf | -8.2954 | -55.097698 | 2024-10-09 01:27:07 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50dccbc6-a902-30fe-afda-3b44ae2bb89b | -8.2983 | -55.109901 | 2024-10-09 01:27:07 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4f3d9c9-8bb7-37ae-b166-6836ebfadcc9 | -10.5297 | -65.4132 | 2024-10-09 01:27:09 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ded67585-5a86-3a5f-992c-5ebf4a78edc0 | -10.1473 | -63.655998 | 2024-10-09 01:27:09 | METOP-B | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b23fbb2-36f4-37f8-81e0-39afb4d78c1f | -10.1358 | -63.650002 | 2024-10-09 01:27:09 | METOP-B | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ca759c4a-e07c-3289-ac12-8ebcde7fa7e1 | -10.1375 | -63.6581 | 2024-10-09 01:27:09 | METOP-B | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e934a6d2-cc38-3d83-8efa-14e704a96bcc | -10.1393 | -63.666199 | 2024-10-09 01:27:09 | METOP-B | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e911b306-f6c0-33f1-9ab0-08cf3df71abd | -10.3833 | -64.812897 | 2024-10-09 01:27:09 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01bf2458-485a-3d40-a6d4-7ca885cf7b8e | -10.3715 | -64.805603 | 2024-10-09 01:27:09 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7274aabc-dab2-328f-a5f2-7be72c129ce2 | -10.3735 | -64.815002 | 2024-10-09 01:27:09 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 446a7e31-9674-3854-8072-4bf66aa7c42e | -10.3755 | -64.824303 | 2024-10-09 01:27:09 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8d81130d-7954-35eb-82c7-37bee4509b52 | -10.0338 | -63.4622 | 2024-10-09 01:27:10 | METOP-B | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 84057393-15fa-3d4c-80ac-299ac2a33d3b | -10.0355 | -63.4702 | 2024-10-09 01:27:10 | METOP-B | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9160b29d-3067-3ffd-9c3e-a396e248b956 | -22.8137 | -48.4225 | 2024-10-09 01:27:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5ab2a59e-84f7-393f-b964-8012ce5722b8 | -9.7453 | -62.324699 | 2024-10-09 01:27:11 | METOP-B | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 439fbd52-1712-391f-ab60-61b86eb4a8f1 | -9.7469 | -62.331902 | 2024-10-09 01:27:11 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1903d0a0-3a84-3a83-acc9-dac4531607ba | -9.7517 | -62.3536 | 2024-10-09 01:27:11 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a368c9d7-04ca-366d-ab9a-f01ab788c981 | -9.7533 | -62.360802 | 2024-10-09 01:27:11 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec7c3a3-6adb-386d-bb48-2319abe78c7e | -9.6868 | -62.292198 | 2024-10-09 01:27:12 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9dd8ccb-de05-39ee-8096-e5a2a07c127d | -10.0973 | -64.815399 | 2024-10-09 01:27:14 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 517a0d85-5d99-3327-ad32-be148d7dcdb4 | -10.0993 | -64.8246 | 2024-10-09 01:27:14 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 097ee4f2-10eb-38fa-9640-5b5154417221 | -9.0469 | -60.435101 | 2024-10-09 01:27:15 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d28affcf-80eb-3f66-9c3b-c61bb8719b07 | -9.0484 | -60.442101 | 2024-10-09 01:27:15 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20ad7614-f79a-370a-9120-9db4b30c9e28 | -9.05 | -60.449001 | 2024-10-09 01:27:15 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50b72049-6ee5-3586-af48-1d8bee1e8820 | -9.9935 | -64.760399 | 2024-10-09 01:27:15 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27fdb70c-d5f6-3ae7-8c8b-86b836a2c96f | -9.795 | -63.877701 | 2024-10-09 01:27:15 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b016faea-974b-3e50-bbc2-79decb187f4d | -9.021 | -60.4119 | 2024-10-09 01:27:16 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 467252bc-0ceb-335b-bea9-5676a7a9b091 | -9.0226 | -60.4188 | 2024-10-09 01:27:16 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7f19425-d5b3-3959-a507-2a1773a3590c | -9.3977 | -62.333599 | 2024-10-09 01:27:16 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9897585e-c8a1-37f2-9d17-522f37e6b327 | -9.5261 | -62.9198 | 2024-10-09 01:27:16 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 58c65e07-2e8b-3043-8928-852930cf3720 | -9.0082 | -60.720699 | 2024-10-09 01:27:17 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a7edfb6-dea3-3e1d-9ba6-917b3ce0b560 | -9.0097 | -60.7276 | 2024-10-09 01:27:17 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f478f959-5f6c-3603-9b88-79bfbf9ddf77 | -9.0979 | -61.121101 | 2024-10-09 01:27:17 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02aa72e0-6ce8-32e5-ae0b-9607bfcf8a85 | -9.0995 | -61.127998 | 2024-10-09 01:27:17 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 552f56bf-5221-303f-ba19-b0528ac9c102 | -9.101 | -61.134899 | 2024-10-09 01:27:17 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9946bb7-20a4-38d1-a52a-b304d36e37c7 | -9.0866 | -61.116402 | 2024-10-09 01:27:17 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a0b5168-10a5-3b95-bdff-387d591746c4 | -9.0881 | -61.123299 | 2024-10-09 01:27:17 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb0df789-4ed7-35b6-a92e-2d941fc1bfb4 | -9.1643 | -61.5569 | 2024-10-09 01:27:17 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a3e0fae-9f82-3f3e-b483-016b661b2c2f | -9.1658 | -61.563801 | 2024-10-09 01:27:17 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1d949321-1604-3004-9490-7d84d8d1b11a | -9.1545 | -61.559101 | 2024-10-09 01:27:18 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 73b01851-ae04-3aca-97ac-ad03a09dfce1 | -9.156 | -61.566002 | 2024-10-09 01:27:18 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd7fb9c-96c2-359c-addf-6ac8073be261 | -9.734 | -64.215103 | 2024-10-09 01:27:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6279ffc1-863a-351b-aca1-130b24e1eac8 | -9.0967 | -61.346298 | 2024-10-09 01:27:18 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4bd6fd4-03d3-383f-a329-ac2f63e474d9 | -9.0983 | -61.353199 | 2024-10-09 01:27:18 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cca789ec-a3c0-3794-a437-84fdff124eaf | -9.7242 | -64.217201 | 2024-10-09 01:27:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e75150f0-6417-3cde-9204-a667c4239ce0 | -9.7261 | -64.2258 | 2024-10-09 01:27:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 75dd5b1a-f1d1-3060-8efb-062127e037e7 | -9.0833 | -61.378399 | 2024-10-09 01:27:18 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b84257c1-5d46-36f1-bc8d-d10908e42a89 | -9.0849 | -61.3853 | 2024-10-09 01:27:18 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f64aa74c-00d6-3ccf-beec-e9a80ac3d538 | -9.0689 | -61.359798 | 2024-10-09 01:27:18 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c31d04ef-79bf-3f7d-9fc4-7bac0f6ff331 | -9.0653 | -61.389702 | 2024-10-09 01:27:18 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 349a15ca-543f-3d7c-9c2d-db9c2b6df332 | -9.1764 | -62.262402 | 2024-10-09 01:27:20 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0ebc1b53-cbde-38ee-bdde-ce835ba1d5ab | -9.1779 | -62.2696 | 2024-10-09 01:27:20 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 95766319-ad8d-35a1-9338-d62e2756bff9 | -9.574 | -64.0905 | 2024-10-09 01:27:20 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e1aeb399-a02e-3abe-b2eb-012b6bac3bab | -9.5758 | -64.098801 | 2024-10-09 01:27:20 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 41efc238-3668-3435-b459-2586b5f45a0e | -9.0079 | -61.5481 | 2024-10-09 01:27:20 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 62bc0ebd-3315-3301-ae76-4b71242ceaf5 | -9.3836 | -63.398102 | 2024-10-09 01:27:20 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 560a08e8-6a3f-3f4d-8012-8874fc883a09 | -9.3853 | -63.405899 | 2024-10-09 01:27:20 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ede7f914-b7a8-3119-af8d-136464e73ff6 | -9.5223 | -64.040497 | 2024-10-09 01:27:20 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e567c47d-947d-362b-afbf-9981a73e4018 | -9.4053 | -63.6404 | 2024-10-09 01:27:21 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f2919e9c-0251-3750-be4b-cbba1e503186 | -9.3955 | -63.642502 | 2024-10-09 01:27:21 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8696dcb3-dff4-3761-884d-a5faa2b91fb5 | -9.3661 | -63.7915 | 2024-10-09 01:27:22 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a100234c-7c07-306d-b3e3-631670436ced | -9.3678 | -63.799599 | 2024-10-09 01:27:22 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c9c7538-0dc6-3a28-9cef-49061336fea9 | -8.849 | -61.4818 | 2024-10-09 01:27:22 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc26e6c1-4024-3c14-987c-1095bebd2666 | -9.3563 | -63.793598 | 2024-10-09 01:27:22 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fbb3082a-3377-3f33-af4c-f54202373e93 | -9.358 | -63.801701 | 2024-10-09 01:27:22 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 46cc6698-6f93-30a8-99de-4c3d217c0d34 | -8.8376 | -61.4771 | 2024-10-09 01:27:22 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0bc4bb9-f76d-35c7-8d94-d1af5f1b7cd3 | -8.8392 | -61.484001 | 2024-10-09 01:27:22 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d543c67a-0853-31a9-b01e-607112aec481 | -8.8407 | -61.490898 | 2024-10-09 01:27:22 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6eab5fa1-ef49-32d4-9449-542b46980568 | -9.5815 | -65.231102 | 2024-10-09 01:27:24 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ee8bdc14-fd48-3103-ad01-caba09b7d868 | -9.0573 | -63.220001 | 2024-10-09 01:27:25 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c60d339-4c64-3bbb-9a73-b04a42eab44d | -9.059 | -63.2276 | 2024-10-09 01:27:25 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5193e70e-ba1c-3dcd-af0e-ba9e7e148afa | -9.0475 | -63.222198 | 2024-10-09 01:27:25 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 21964f81-c67b-39f0-8fb8-d5492e0fe644 | -9.0492 | -63.229801 | 2024-10-09 01:27:25 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2fe38f89-21ff-3419-9012-b922c6aa2c11 | -9.0305 | -64.138 | 2024-10-09 01:27:29 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 947cd033-496a-38d7-b295-34a7fc301290 | -6.8702 | -55.2981 | 2024-10-09 01:27:31 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6513133f-17f9-3e90-ada5-11f81a9e2c09 | -5.4294 | -49.522099 | 2024-10-09 01:27:31 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 060b940d-02af-3124-9bd1-71a874866b03 | -5.4376 | -49.554901 | 2024-10-09 01:27:31 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d714b11-572e-3b25-ba71-8f6e02ca96dc | -8.2201 | -61.202599 | 2024-10-09 01:27:31 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 738798f0-b880-3f40-8b26-bcae71ad4a43 | -5.4198 | -49.524601 | 2024-10-09 01:27:32 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6abe249a-c761-38d3-963f-595e79519316 | -5.428 | -49.557301 | 2024-10-09 01:27:32 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b9ca47e-5394-386b-a773-691050ae417f | -9.4361 | -67.073303 | 2024-10-09 01:27:32 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0837e106-4067-3fa9-a714-785ac34b7461 | -8.089 | -61.261002 | 2024-10-09 01:27:34 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fb1c56a-f1c2-39d8-8b3b-04a49008af5c | -7.298 | -59.724998 | 2024-10-09 01:27:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8b4b2e-b9d3-368f-8d36-c98e24f3c68d | -7.2517 | -59.612801 | 2024-10-09 01:27:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3534137f-48dd-3c36-9598-6d2b05e6b813 | -7.2534 | -59.620098 | 2024-10-09 01:27:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8eeeb9-8a5a-3e0d-bd63-f78cfcbcae6b | -7.2419 | -59.615002 | 2024-10-09 01:27:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| beb79303-5f4a-3e83-98a9-4071dbd04ef2 | -7.2436 | -59.622299 | 2024-10-09 01:27:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README46.md)
