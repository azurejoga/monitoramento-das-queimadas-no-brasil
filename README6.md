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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7719a50-5268-3ebb-8c71-95e19c0d0487 | 0.47471 | -60.33252 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3a559a9-b236-3d10-a3a2-3808042aa8a7 | 3.03565 | -60.81913 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fffd4f72-6ecf-347d-b0a6-00e38ed91898 | 0.66782 | -60.30339 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 230ee403-098f-374e-be7f-e7a751047f8c | 3.03908 | -60.8114 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa95985f-d68a-320a-9852-50583c6ad115 | 3.28758 | -60.72689 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1a744d8-2756-347d-85ec-c7425ebddd37 | 1.50896 | -59.91847 | 2026-03-05 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 898f0901-3273-3a5f-a2b0-1a3433be0304 | 1.08183 | -59.25114 | 2026-03-05 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c659742-7817-3f24-9990-f60b14cfebdb | 2.69783 | -60.68977 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df5fc03f-db82-353f-af13-589091fb33c5 | 3.03203 | -60.81252 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eee31854-21ef-3b45-b37f-81b1b2984ef8 | 3.06885 | -60.63801 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9341da7a-7ddc-3ec5-abb7-fbb8514c0222 | 0.76882 | -59.89307 | 2026-03-05 04:44:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3709cb23-88e8-3c55-9dcc-907aedf8cc75 | 2.69182 | -60.69746 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d1f16b2-e068-32d1-a415-aab01caec914 | 2.96801 | -61.09723 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c8837aa-5f69-3907-b607-80e4d67b7bfc | 3.0296 | -60.82688 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 94a86818-44c3-36c5-8e3a-4cdb03159a06 | 3.06791 | -60.63145 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19f4f6e0-a436-32ee-84d9-c95171cb6b90 | 2.69961 | -60.68771 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b56e3d12-d0a9-3680-892f-73d28e692b24 | 2.78164 | -60.34992 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 606dc52b-2f4a-3cb7-b460-556feee691b9 | 2.6988 | -60.69638 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40e0df9f-198f-390c-bf66-ba4c5ed99e49 | 2.72281 | -60.66585 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8baadf8a-2fe9-3e87-ad9d-e8918e5d13ee | 1.11253 | -59.20088 | 2026-03-05 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0abc4a43-954b-35f4-bbd3-57040be3963d | 1.51448 | -59.91092 | 2026-03-05 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e3a82d5c-b20e-3ef4-a98d-3a7c1570e636 | 2.96084 | -61.09834 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 213e051a-9a7a-338f-974b-ac87befc54f1 | 2.95982 | -61.09131 | 2026-03-05 04:44:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4416975-5d12-35f9-a171-e893f130263b | 2.69364 | -60.69532 | 2026-03-05 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c8f6bb09-b74f-35a3-89a0-e563841f25b3 | 3.28351 | -60.74808 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b415f27-7c95-3e5d-a755-420b9bd89ff5 | 3.03462 | -60.8124 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5dccde02-3255-3b79-b8e5-37d431ce5fba | 0.47381 | -60.32687 | 2026-03-05 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efbe2025-e8e5-325c-8b80-4d717d41bbd9 | 3.04006 | -60.81813 | 2026-03-05 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c946dcd-48f0-35d0-90ce-f2c86d813683 | -17.57706 | -53.07218 | 2026-03-05 04:48:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a611be0b-53b4-3077-83d4-f693d6a95bc2 | -17.52605 | -53.69835 | 2026-03-05 04:48:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fd152e5-e868-39a6-8b3a-d0b8ffcff47c | -17.58041 | -53.07277 | 2026-03-05 04:48:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 18d12e18-4ee5-3916-ac0a-2b9e8d06048f | -16.5864 | -57.8095 | 2026-03-05 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2907e4f1-59cd-374d-9c49-c4c4207ec7c5 | -17.52542 | -53.70216 | 2026-03-05 04:48:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91d77aa6-ed8b-3f5a-b864-9b6338f3d804 | -15.07898 | -57.78404 | 2026-03-05 04:48:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1692e90d-4e5e-3398-bd97-3aa961841714 | -16.58719 | -57.80534 | 2026-03-05 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 73d00bc0-3209-3fc3-8d50-d522e0924f0b | -18.89871 | -54.72446 | 2026-03-05 04:48:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0611f15f-4db3-3d26-9af6-5c0257658730 | -15.07575 | -57.78162 | 2026-03-05 04:48:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ab20616-3d21-30d8-864f-b6a27d16cd26 | -17.52945 | -53.69898 | 2026-03-05 04:48:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26d135b4-b5b4-35fe-9547-9d8a4f78ec71 | -18.86372 | -51.6385 | 2026-03-05 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7de995d-e53d-3eee-957d-4e526a0e9a08 | -17.874 | -55.25253 | 2026-03-05 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1defe302-a123-3aa4-b062-27b6c82b6428 | -16.58722 | -57.80984 | 2026-03-05 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 69cabbf9-69ce-3eee-b8ed-690957a9e32c | -15.07465 | -57.78313 | 2026-03-05 04:48:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1988a2a-f658-38f1-9cee-2afc3aa0b9b3 | -16.59061 | -57.81039 | 2026-03-05 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 111090e8-2536-3952-a725-882fe3b9f38a | 2.7817 | -60.3148 | 2026-03-05 04:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8c7f55f8-f281-3802-a5b0-76c41ddf3257 | 0.0455 | -60.9799 | 2026-03-05 04:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 37e8b713-ef88-3e4c-ba16-6c9a81e63ea8 | 2.7816 | -60.3528 | 2026-03-05 04:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d25d0e0a-a9bf-3db3-b15d-d7618a245749 | 2.7816 | -60.3338 | 2026-03-05 04:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 743b4f0d-dafd-3e65-b6ea-a2c524858e90 | -25.17553 | -49.39861 | 2026-03-05 04:50:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6c500478-6780-3c45-829f-2c125d691d1d | -22.92525 | -48.61156 | 2026-03-05 04:50:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 656042db-2af2-3c6a-98f7-55a014d4610c | -23.08134 | -55.49662 | 2026-03-05 04:50:00 | NPP-375D | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1ef9e3d4-ba6e-3103-8aae-1f55841f18c1 | -24.2791 | -49.7154 | 2026-03-05 04:50:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec5fd46f-94f3-3f4e-98bb-012d57897428 | -21.78087 | -49.83932 | 2026-03-05 04:50:00 | NPP-375D | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 519eace1-2561-3a78-8d8e-eb2544b9b9e6 | -20.93735 | -48.71162 | 2026-03-05 04:50:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bb99d812-645c-3fd5-bb9e-3d4334e84c95 | -19.90598 | -49.41671 | 2026-03-05 04:50:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9236454e-26b4-37f0-80d6-3406b9509410 | -22.9222 | -48.60984 | 2026-03-05 04:50:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0a24763-31d3-3f8c-9325-f34a861f0f98 | -22.60914 | -47.46696 | 2026-03-05 04:50:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80138ccf-2484-39e3-bb6b-61c78abe318b | -20.91727 | -50.53385 | 2026-03-05 04:50:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9a2db07d-982f-3d61-9241-c92390dfd34b | -19.9066 | -49.41236 | 2026-03-05 04:50:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9c65374d-7159-361c-8793-866c9e5af3a6 | -20.75228 | -50.53318 | 2026-03-05 04:50:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1429a66b-7e0f-37e1-9ea1-419c800dd6c2 | -22.77655 | -55.39369 | 2026-03-05 04:50:00 | NPP-375D | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 225553bd-696f-3f3f-82ba-ff4d424f9beb | -21.23292 | -48.52523 | 2026-03-05 04:50:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b88b404-35c8-38d6-8751-40e6143d8850 | -19.90237 | -49.41614 | 2026-03-05 04:50:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f871158a-734f-323d-bc21-056fc0fa2476 | -19.90298 | -49.41179 | 2026-03-05 04:50:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fdf071b1-8d77-3ffb-b624-eaeb5771858d | -21.09076 | -49.22422 | 2026-03-05 04:50:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 03237ea5-3765-37c8-bb0a-beb39c18e833 | -22.91506 | -48.6034 | 2026-03-05 04:50:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 220abfa9-9ddc-3434-ad2d-39eb2905a53b | -22.96653 | -49.91097 | 2026-03-05 04:50:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e42ae750-3697-35eb-8e20-d71051b3421e | -21.4765 | -48.69269 | 2026-03-05 04:50:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ac40087-8aab-3fd0-b1f6-50212618ee09 | -22.92611 | -48.6104 | 2026-03-05 04:50:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42cdc4c4-5e81-3db2-b5a2-bbef4bd2b505 | -21.0914 | -49.21959 | 2026-03-05 04:50:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 988791a4-1e88-3661-beb5-59d144b5eca0 | -25.01844 | -49.29246 | 2026-03-05 04:50:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 92b3de43-1f55-3563-8653-0883cceb711f | -20.94114 | -48.71225 | 2026-03-05 04:50:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a8215dbb-87aa-3698-9f6d-d8cd6b92c5df | -21.22125 | -49.48676 | 2026-03-05 04:50:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6919c29e-1f1a-3157-a724-b42c582a945d | -22.03943 | -55.99808 | 2026-03-05 04:50:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 882b4561-d4bb-3295-97ac-caa41ca4cde2 | -21.30187 | -48.59648 | 2026-03-05 04:50:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 035da7d1-b327-39cd-984a-539a590ff051 | -21.70017 | -47.16877 | 2026-03-05 04:50:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b7ca22db-5a1f-3a8c-bf0e-c4f835258560 | -20.94048 | -48.71711 | 2026-03-05 04:50:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9a6e4c7c-807e-32a2-8cfb-9b524850a352 | -22.77723 | -55.3897 | 2026-03-05 04:50:00 | NPP-375D | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c07e65cd-118b-3d0a-b4c8-def22e323da8 | -29.6741 | -49.97393 | 2026-03-05 04:53:00 | NPP-375D | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 00037b6c-9369-3688-b659-9d9f8c68451a | -30.26187 | -56.60324 | 2026-03-05 04:53:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 1370bfef-1a0d-3892-bef0-98554100c514 | 0.0455 | -60.9799 | 2026-03-05 05:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 3c79eb84-ac87-39a4-9ad0-95b3905803d9 | 2.7816 | -60.3528 | 2026-03-05 05:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 4e473030-1286-3599-b4ff-4c225661b85d | 2.7816 | -60.3338 | 2026-03-05 05:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 6ff93dd9-63f0-38f9-92e6-8d1edb50732f | 0.30208 | -60.45153 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c5cc244-2436-3256-9215-29b1597e6687 | 0.03735 | -60.9765 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2729322-81fc-3792-86b5-b94efb93ac06 | 1.17626 | -60.36741 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2080377f-0dbe-3ba4-97af-be654b12efcd | 3.0224 | -60.64108 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15aa23a6-36d3-362e-9826-f7d5c1ae8aef | 0.04249 | -60.98019 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7554c69-db01-3a1c-8a8c-faf167fefad6 | 3.06798 | -60.63409 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d263d45c-44f0-376a-9ea8-a95a69cd9478 | 2.98886 | -61.0387 | 2026-03-05 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| caa22e51-3fdb-3f68-85eb-e4485e75bb7c | 3.28375 | -60.72568 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37cde33b-9ac8-3671-8a4a-09bd931b588d | 4.95179 | -60.28199 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6215b0d7-6aff-3d1a-8d08-ccf4f8b17bc4 | 1.36326 | -60.38023 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32ac14ad-175e-3af6-b5a5-57eab983ee0c | 1.14628 | -60.89505 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08933758-38a8-3ab2-9526-32e9f58464df | 3.50873 | -61.90579 | 2026-03-05 05:03:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a148889-96ff-3c74-9f3c-7727102c7768 | 0.66533 | -60.30659 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a60c172f-83e1-3da9-9c8b-6a504495d6d4 | 0.30704 | -60.45491 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc94839f-f1a5-3e61-8685-1d475c0aa0b9 | 3.18988 | -60.56775 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd093c60-3621-37ae-81c4-7e5dcd6678da | 0.47322 | -60.33149 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61178e14-9c5d-303a-ad99-66ea4ad9c605 | 4.96767 | -60.26321 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41492f9a-c820-367f-a0c9-47d968cea642 | 2.66397 | -60.41061 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
