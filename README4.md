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
| 88b6e2e7-31da-3aa5-abea-bfc773b12960 | 1.27723 | -60.32042 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2bf6e67-8dd8-3b35-8a8b-f691ec40527a | 2.0219 | -61.09535 | 2026-04-12 04:51:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 559f4eb3-d2e2-3501-983e-6a2a6e89fa4b | 2.37552 | -60.95697 | 2026-04-12 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30dd2924-ba0b-3cd1-8be4-75a99fff0429 | 1.38158 | -60.66116 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c0118c9-1e0f-3b64-95c7-f7bf21120da6 | 2.37093 | -60.96589 | 2026-04-12 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7d041fe-d6bb-36a1-b6b0-a21d97ae4922 | 1.21747 | -60.44603 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64003209-f3c3-327c-b4c5-08d5340fba56 | 1.28375 | -60.32653 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f8def86b-48e0-3e3c-bf6b-6197de94ee07 | 2.54006 | -60.35146 | 2026-04-12 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3d73407-f106-3341-afaa-2d3bd7c555e5 | 1.37541 | -60.65826 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e09532dd-0856-329e-8655-e71472e7d17a | 2.0347 | -61.10158 | 2026-04-12 04:51:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2324f837-7da6-3c37-8dea-fb932f6e0de0 | 1.381 | -60.65749 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8af5336-3242-3ffa-bba5-7c053b6e9c10 | 2.6752 | -61.17583 | 2026-04-12 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3a170cc-69df-31b2-b6a1-220673d58456 | 1.28212 | -60.31606 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa758ddf-6c8e-389f-9158-2b0a9ad99a0b | 1.37659 | -60.66566 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d13961c-0e23-3232-9a35-fe4473eefef2 | 1.21809 | -60.44534 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08891902-8e93-377d-884d-a247c97a257f | 1.37566 | -60.66854 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f9ef207-b49c-3bb4-8d83-2fce60662a6e | 2.0283 | -61.09846 | 2026-04-12 04:51:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2dd1fb64-1506-3947-a454-cd4061578785 | 1.35662 | -60.68387 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b39b35f-647b-38fb-825d-dc8770f0f687 | 1.28267 | -60.31955 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ad2d6a3-5694-3cb5-a592-0cc35154665f | -1.60083 | -50.01243 | 2026-04-12 04:51:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0b3f4d7-b323-30e5-b02d-23b66a992a7f | 0.42557 | -60.50655 | 2026-04-12 04:51:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e8fb57e-f5ec-311e-bb81-e8b7f178eb33 | 1.27669 | -60.31692 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fad4bf6b-898e-32f0-8f83-819626e33a1e | 2.02769 | -61.09446 | 2026-04-12 04:51:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 69d66c2b-4b52-332f-b38f-9b7cb10fc815 | 0.43155 | -60.50915 | 2026-04-12 04:51:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 230f3297-4406-30ce-80e8-f226fd70e7d9 | 2.02891 | -61.10252 | 2026-04-12 04:51:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94fe471c-60c1-32fa-9e94-571e665919b1 | 1.37509 | -60.6648 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 967376ac-b443-338c-89b0-6b184a4cf8e2 | 2.37465 | -60.95686 | 2026-04-12 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d79395f8-9c11-3f92-8fca-d17f8c08674b | 1.3543 | -60.66911 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d93525-1774-3a42-a749-013698db4e02 | 1.36172 | -60.68976 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0908f4d-8307-3550-be16-66a81515ab8c | 1.38458 | -60.65209 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adf1fb8b-4d47-38b5-8862-517b26a3c4e9 | 2.03408 | -61.09754 | 2026-04-12 04:51:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bdba36b8-0c71-3cf9-a3ed-6052723be878 | 2.5345 | -60.35229 | 2026-04-12 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08d47fd1-2d59-3195-949f-ac5415af5cad | 2.37012 | -60.96573 | 2026-04-12 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb4bc493-d843-3b51-acbd-da724caff603 | 1.37483 | -60.6546 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1031cf70-3935-3b70-9055-55a0527f2c03 | 2.37527 | -60.96083 | 2026-04-12 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58c80135-45d6-313b-90a9-3a0617beff1f | 1.37956 | -60.6566 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15b0d8ee-f70c-3ee8-8c86-62d74b025df8 | -12.97996 | -54.68122 | 2026-04-12 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 708a3891-df65-338e-ac0a-63e724e2dc6f | -12.51917 | -43.68513 | 2026-04-12 04:55:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50bd7689-0244-32c2-bc84-bca7852a0c5c | -12.98327 | -54.68177 | 2026-04-12 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14a0676d-bbbe-3f58-a993-c5b543e55d1f | -11.20396 | -56.87459 | 2026-04-12 04:55:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2457b4cc-a846-3c6a-be22-123bdf9113cb | -12.97939 | -54.68476 | 2026-04-12 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0b99df0-13e5-369c-bb88-8570bb8fcfa2 | -11.20254 | -56.883 | 2026-04-12 04:55:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc7971e9-d8c5-3cda-a83b-022f1a70720d | -15.28154 | -43.07012 | 2026-04-12 04:55:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a44adad8-354b-3a09-99f6-5d776f2b8b16 | -12.5187 | -43.6892 | 2026-04-12 04:55:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac0c9932-e64c-32c2-a88f-e39e27db038f | -15.37986 | -52.75447 | 2026-04-12 04:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e7db2ba-525e-302a-b739-e596bb6b66b2 | -12.97276 | -54.68366 | 2026-04-12 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7af6f45f-f2a8-3951-a180-e4714e00b0cb | -12.51731 | -43.68946 | 2026-04-12 04:55:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f732e19-5b7d-3784-9b35-bee9ec6854c1 | -11.60147 | -55.32635 | 2026-04-12 04:55:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bff6cb5-3fd6-347f-8289-d595d8d0a6d9 | -12.97219 | -54.6872 | 2026-04-12 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06d3f29f-8bff-3ca5-b084-7112efc0c507 | -14.82741 | -53.21822 | 2026-04-12 04:55:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c21f226-1181-305a-8412-210284c555de | -12.5178 | -43.68541 | 2026-04-12 04:55:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 387bf86a-0f41-3d02-b3ff-4d682f1670d8 | -15.28205 | -43.06525 | 2026-04-12 04:55:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5940ca23-31df-3143-9478-da8b7220a4c8 | -11.20325 | -56.8788 | 2026-04-12 04:55:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b3fa9fc-9b12-3bad-9e11-1ff720ddecaf | -15.37699 | -52.75021 | 2026-04-12 04:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ebe2e35-0afe-3e71-86af-4c3a40ea4342 | -11.60484 | -55.32692 | 2026-04-12 04:55:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c661316b-01d6-3947-b2ea-496d0891c22d | -12.97607 | -54.68421 | 2026-04-12 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 250a457c-97c1-3272-a3c1-70c4beab07ef | -20.09404 | -57.21663 | 2026-04-12 04:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1411cb52-34e1-30bb-be39-29d88695a316 | -23.40726 | -46.35187 | 2026-04-12 04:57:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9fbf7792-9228-336a-9248-3b1053054e94 | -23.40761 | -46.34797 | 2026-04-12 04:57:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f690ae1e-c095-3d1c-aa5a-591cc9849c2e | -22.26765 | -48.50056 | 2026-04-12 04:57:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c44a680-0eb6-3f9f-afc1-7f30985f57f8 | -18.78732 | -51.93398 | 2026-04-12 04:57:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94962a43-5f84-32fb-a434-e39a5484721c | 1.2781 | -60.31846 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f7c1db43-c1ef-3bad-a929-dae3611b500c | 2.67157 | -61.17568 | 2026-04-12 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e7e91ab-76c2-3fb4-8487-24c76cbf32f8 | 2.03081 | -61.09745 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| eb68a759-619c-32f4-a391-f5e0b53d4b29 | 2.38269 | -61.45753 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49a65667-c11e-3820-8805-37b5dd65b14b | 1.35352 | -60.68573 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc5248c1-942a-3042-9f49-3d05d0619c14 | 1.8949 | -61.26033 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f0e91f9-45a8-36a6-8b11-bf36b05ef2df | 1.2817 | -60.31789 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 724a85f1-05cd-3c17-91ee-4d492d7a9ce0 | 1.27682 | -60.31019 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c55bbed5-0afd-3a55-8e60-175652995302 | 1.36929 | -60.67103 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8d928a1-164e-3085-88be-d7e51525fe37 | 2.33633 | -61.47917 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d723409d-9988-38e0-9965-f32e959d8359 | 1.28594 | -60.32145 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e220377f-a579-35ad-b172-fe377a49181a | 1.27386 | -60.3149 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 581ec535-0d5a-3822-b7ad-a2d1f995d38a | 1.30631 | -60.6632 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0f521dd-072a-3c4d-a795-5a138e7e0b11 | 2.02046 | -61.09907 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 87d85d11-e586-3984-aced-064acf65be46 | 2.02451 | -61.10231 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dde028b8-38d5-3886-91c1-d027e449cad0 | 1.37509 | -60.66196 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ae05a5c-3f00-3630-9fb8-f5a28bfcb677 | 2.02332 | -61.09475 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e18b463f-f739-3630-bf8f-9c3f4aebb1d4 | 2.01583 | -61.09207 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd87589d-7b09-312a-8310-f0f0a521801a | 2.03485 | -61.10068 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fda78029-3f65-3128-9e4f-a239b38ea6eb | 2.10488 | -61.2555 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e0018c3-39db-3b47-a04e-bcaf5e8277aa | 1.28298 | -60.32615 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa93ebfb-c086-3115-825a-0afe4bfbdc29 | 1.28442 | -60.32346 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 588fb0a6-5553-3c6c-8193-887d4d158b20 | 1.28376 | -60.31933 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76359927-7fe8-3e1f-850b-8d4246f4e866 | 2.02677 | -61.0942 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c35c52f8-7484-38b2-a346-7c0cf8d1d909 | 1.2745 | -60.31903 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62784d92-1b15-36bc-8b4d-d0c18650f2e8 | 1.35768 | -60.68913 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d02906f1-5688-3e60-a202-b325bd7a0692 | 1.2853 | -60.31732 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16015d84-d827-3a64-9511-bbd87e2216ba | 2.01927 | -61.09151 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af4a269d-c043-32a1-8d1e-1e1ee7f62015 | 2.02736 | -61.09799 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 088251fa-be93-3e48-b786-5548ee44e1a2 | 2.53698 | -60.35056 | 2026-04-12 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2cfa1e3a-d7ac-3b99-abc8-84086b2f787d | 1.35098 | -60.66985 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40ddba05-6b10-382f-80bb-a9b0aaa1d399 | 2.01642 | -61.09584 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1d0aadc5-f7a3-3080-987c-285607919533 | 1.16276 | -60.67237 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 482799dd-0b9c-300c-99cc-b22c2bcf1019 | 1.30923 | -60.65865 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b8f9bc0-a4e8-3e10-acaf-2d2cc29039f2 | 1.37863 | -60.6614 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d2e5538-e4e0-3cf5-95c8-b6b79ea209cf | 1.27257 | -60.3066 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83a04b8a-af19-33f1-9955-c9bd99f22e77 | 1.35415 | -60.6897 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4a3560c-793a-38a0-9b74-1e57d43feb97 | 1.35705 | -60.68517 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4089e703-f855-36c8-9559-15e5e6b2b710 | 1.37383 | -60.65399 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README5.md)
