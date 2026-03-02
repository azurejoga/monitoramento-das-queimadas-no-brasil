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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec6419ab-864c-381b-a72d-d1c696fc3d9f | 1.17277 | -60.82547 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdf218e3-b04b-3e14-9b98-a65e39257291 | 4.37602 | -60.61792 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4db944d-3338-36cc-bee5-71de5df787c6 | 2.41941 | -60.25037 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e74898dd-84b0-3d86-af42-82170f8b32b4 | 1.48866 | -59.90907 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07ca4515-419e-3adc-b6b6-50ee4ea19607 | 3.41849 | -60.83658 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1effba25-f42f-30d3-a318-ce4bdb4f71a5 | 1.72175 | -60.29922 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 726a3c0b-c6fe-37fd-95e9-9648c6b56c68 | 3.46625 | -60.79335 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bcac933-018c-3ef1-a36a-a0b8f4264367 | 1.87478 | -60.9142 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faed3af6-bb4f-3ece-af74-0974bc19225b | 4.37381 | -60.62543 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5bc7f5b-bca3-3168-91e1-24801e2f525b | 0.09452 | -60.63109 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a38b8ed-3b5c-37c0-821f-9c308b3a34c7 | 0.69784 | -59.97102 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fe93d45-6c83-32e4-b8a6-c340c2b3b007 | 3.46126 | -60.78342 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84719060-e985-3de9-be7c-4166a6c9ee08 | 2.85184 | -60.84333 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 849f68f1-0281-34a5-aadd-4c24ed6be896 | 0.45137 | -60.39321 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 198cee56-b9d3-390b-af4f-8b213f58d3e5 | 3.4146 | -60.83363 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16554e94-9f5a-303a-bc46-d322585d2c2b | 2.86207 | -60.84889 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 26cbeca9-b658-3879-b04b-c61c58ceb76b | 3.05325 | -60.66851 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54410f17-6d2e-37a2-95d1-6bcd567f40b9 | 2.84906 | -60.84734 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 615c59b6-435b-31d2-8ba8-ca9e6eeaaf48 | 1.45736 | -60.06667 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1afa48a0-5925-3f96-85f2-ae848478e04c | 1.49733 | -59.91918 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d282b1c3-6912-349e-bf0b-1801dfb28536 | 3.46357 | -60.28936 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 214ff26b-9506-358a-9a32-e50290e91c28 | 3.02601 | -60.68354 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cc8eab8-d991-3763-a50b-83159fc3f438 | 0.19062 | -60.44432 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d04129cc-2490-331d-959f-988180414e1a | 3.98717 | -60.09097 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51c2eb59-51be-3254-8676-a09317c48a0e | 2.11804 | -60.19754 | 2026-03-02 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25cb0736-26a8-3ceb-9d78-88b739f1eec6 | 1.11906 | -59.19469 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 594b755d-cbd8-37c3-ba9c-740739562811 | 0.68421 | -59.84081 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56572de3-3072-3d3f-89e5-7596cabb5983 | 3.01152 | -60.7002 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df43bdb8-f006-3220-ab71-24bee6ecda64 | 3.39549 | -59.84257 | 2026-03-02 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f2f50be-d4fa-3654-9cf9-4cae36241046 | 2.84963 | -60.82935 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6bc543e4-79a3-3f4b-95c8-348a5d00f426 | 1.0219 | -60.53754 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89cefbe5-a6ae-3bb1-b5cc-f7aead915440 | 2.11405 | -60.1944 | 2026-03-02 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a204d18-532f-3d5d-a562-be55c86a8ba2 | 3.98997 | -60.08684 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc736e68-d6c6-3ac4-a772-e8f3a9eb30ee | 0.57993 | -59.84107 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62fff028-092e-3c5a-a815-6da1b3a9eeac | 1.49388 | -59.91972 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ee83ef5-7a6f-3785-9685-82175c0231af | 0.45029 | -60.40843 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fcda4b7-1db3-33ed-a049-a5cbea72e53c | 1.0876 | -59.24896 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86460ca2-b05f-3875-b584-e5695841ad49 | 4.25288 | -59.91374 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 248138a2-1b12-323d-961e-cca8f16dae9f | 3.05716 | -60.67149 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7a7a36f-cefc-3a9e-b014-5cce2cdf2c00 | 1.44172 | -59.94714 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d59e16b-b300-3069-9714-0338478dbb7f | 2.11183 | -60.20226 | 2026-03-02 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24497dd7-6b1a-38cf-8ccb-779aee51572a | 0.76152 | -59.89208 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c033a9e8-5dbf-3e12-9b05-ee93a0abce73 | 2.86039 | -60.81694 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b290a79-f7f6-3b7e-acca-ed16cfc1423d | 3.04162 | -60.67389 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8df1f6c4-e479-39f0-a830-fb6a8414ad38 | 0.56591 | -59.90974 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eec3f52-dc33-3ca6-83df-632cab17eed0 | 2.85129 | -60.83983 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c39c6bc-3fca-3f37-b486-786b2816abf7 | 1.45855 | -60.07408 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 364a3368-30f9-35fb-9ffd-bcf6befe8de1 | 4.25568 | -59.90964 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45817f30-59c4-3d4a-927d-8f0a542ef7cb | 4.25848 | -59.90549 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65660b2a-892e-3f5b-8722-d13e62fc53f7 | 1.48818 | -59.92834 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8badce7c-a917-37ff-840d-9757dab60410 | 0.30914 | -60.44502 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47b5005f-6540-347a-8a16-df3bd53a449c | 0.7083 | -59.51659 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbdc453e-54fb-3186-8ab7-129f69ac3177 | 0.47648 | -60.3968 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18b73d39-a606-3225-9169-085380ea4d2b | 1.48592 | -59.93638 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a8f52e-5f05-3775-8cbb-9eb6f63b6184 | 0.19005 | -60.44063 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94e32d50-9bc9-3564-85f5-7955d55c8ea4 | 1.87812 | -60.91366 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b8ff4ce-19e3-38e9-b974-f68f757e9ae8 | 4.0869 | -59.88387 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f4a90f9-c7eb-3544-ae8a-2b6fceddd2e2 | 3.93649 | -60.60125 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62166289-d159-3cf4-be36-52d2792b9276 | 3.02936 | -60.68301 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f70c331-b638-379d-ab9f-85881df1a696 | 3.41793 | -60.83311 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebacf33e-382b-30f1-9604-995ba975b876 | 3.41127 | -60.83415 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25e2281c-303b-3643-bc87-62034689ca3c | 1.75595 | -60.38274 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37a4bda5-41a4-3996-abd2-6553c577dcc9 | 1.47843 | -59.93371 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12265719-6813-3c44-8e3b-14417230e3e8 | 4.08409 | -59.88803 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a03899c5-920c-3ddf-918f-c92088a40288 | 1.50482 | -59.92187 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fb598ad4-635b-36b7-9630-94b0ad1e7f3b | 0.9627 | -59.89639 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 771eadd9-22da-3534-bd45-fb6d3f391913 | 3.42182 | -60.83606 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3738f1b7-1c3d-3725-b908-19979b48adeb | 3.46569 | -60.81129 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8b7f0e0-35ee-381d-8f48-600c8945171b | 0.89646 | -60.09459 | 2026-03-02 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 433e03a2-d895-3111-8dc6-8f6945436bbb | 1.51517 | -59.92031 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 52e9245a-1582-34e4-9545-c6aa5fc0029c | 4.50656 | -60.54446 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12769b11-fee6-3eec-a338-9f4edc45ebec | 1.51288 | -59.92825 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f975d32f-cc5e-3cec-b82e-f3a8011ef870 | 4.44476 | -60.72847 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdaefc91-5dd9-3ce6-8db4-a4955432dd3c | 3.18874 | -60.69011 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc178b08-20d8-3c9a-bad9-c32fa98141dc | 3.46181 | -60.78691 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 702b95fb-ba3b-3369-a426-feea44399ba1 | 1.47379 | -59.92673 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84e5d3c1-f3a3-3fc5-8dbb-fb8a68aca4e4 | 1.49615 | -59.91173 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4812007d-b4c9-3620-981c-4574b142a986 | -18.79305 | -57.62204 | 2026-03-02 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| c708609a-b5d9-36ed-af76-a27d3b6a6695 | -18.79375 | -57.61554 | 2026-03-02 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| cbd18520-db0d-3f66-b926-9c31df33f6de | -18.7986 | -57.61944 | 2026-03-02 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a84dafff-9d44-3008-a2b9-a2a1835cb39a | -18.7993 | -57.61294 | 2026-03-02 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 43ecf842-20df-3bda-a888-00efda8d67ea | -18.7927 | -57.62529 | 2026-03-02 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 117ebd4f-c0a7-30cb-8a9e-9ff4d5587185 | -18.79895 | -57.61619 | 2026-03-02 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e6a8e9fc-3b2c-327a-9e94-4b36e00a11f4 | -18.80415 | -57.61684 | 2026-03-02 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| dcabc5f6-7b32-3e0e-a27a-9deef7978678 | -18.7934 | -57.6188 | 2026-03-02 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b61f7597-a1dc-3743-a535-aa964bcb8849 | 1.5047 | -59.9116 | 2026-03-02 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 7c6d5992-8311-3064-8063-0a936f6d2ee0 | 1.5046 | -59.9306 | 2026-03-02 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a7b9064d-1540-3431-8eec-b89d8dee36aa | 1.4864 | -59.9117 | 2026-03-02 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| c0c001e2-9bdb-3b08-95b3-86651806c6ca | 1.16086 | -60.84191 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8d49038-7cdd-3ba2-ae06-385e0e60448d | 1.4945 | -59.91716 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7eae6cd6-36ee-36d8-b638-d5f1294fab42 | 2.86243 | -60.83089 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e187fdb5-422e-32d8-bd57-9a579303c8d7 | 3.41355 | -60.83574 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bbe47b70-6c2e-35dc-8cf2-3dfd9b78e6c0 | 1.49963 | -59.91645 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2904b8a3-9aa1-3eed-b89f-e9b723d926e4 | 1.51694 | -59.9261 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cca83dfd-125c-3c2f-9b5e-25fc32b4d2d8 | 1.48989 | -59.92101 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a338ac0-4bee-3745-b9a0-754527eb266f | 1.09583 | -60.17878 | 2026-03-02 05:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc9d662e-2613-3928-8b6f-28e6ed4871eb | 3.39749 | -59.83947 | 2026-03-02 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d77d172e-0872-3081-9f91-f6076c91bc08 | 1.49702 | -59.93246 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b347d64-4997-311a-abf5-ff9bd80efc0c | 1.07912 | -59.25571 | 2026-03-02 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ef3880f-3301-38f1-ab0a-3549cec0f440 | 3.02507 | -60.68274 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
