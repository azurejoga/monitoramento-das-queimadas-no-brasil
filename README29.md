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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc9c66a2-f839-35b0-9ede-802e900e426a | -4.17943 | -49.86586 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0898f82a-54f7-315c-8306-4a81c9e8d78b | -3.2599 | -51.17749 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 125e481c-dc8e-396c-ae17-460ed37e935e | -3.45946 | -50.54794 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 23398dc8-f66d-3574-a011-c9df2100dd2d | -2.88151 | -51.81151 | 2025-11-26 05:37:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c5a16cc-0d18-3357-9c0b-875c2aaf72cc | -3.22204 | -50.58481 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd7f59ea-addc-3a46-90fc-7d995fd663a3 | -3.20705 | -50.22258 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 800dd872-f0d4-3670-9d2e-88907e495679 | -4.17243 | -49.86483 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22d4fc80-be87-3bad-8a52-a3ce5bfecbad | -4.17708 | -49.87141 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 751a34ea-be68-3362-bcf4-6c88d87fe9d7 | -3.21979 | -50.58463 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1ec2a5c-aadc-3da2-8794-375adc143b44 | -3.32666 | -50.27132 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f145fd0-4e17-35ff-bc2b-29375a51a60e | -3.22118 | -50.59055 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d33d8552-79e8-3f4d-9002-946892db7311 | -3.02258 | -51.03573 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 392fd390-b260-3e65-bc91-9b36c1dacbfe | -3.45746 | -50.54209 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9c91e1e-7144-38c7-9a51-60151bdd3138 | -4.17749 | -49.87918 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4efa2edb-4268-39e9-9f95-0168a24ab4b1 | 3.82565 | -59.95366 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fab79cff-c63a-30ac-b73b-a74d29db66ba | -3.33429 | -50.26647 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf11b3c9-e565-39ab-b24e-9e911969e624 | -1.11034 | -54.13633 | 2025-11-26 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7be2a5a2-e7a8-3028-81d8-a2a8a216658d | -2.94046 | -49.36085 | 2025-11-26 05:37:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7f93ed2e-5d5d-30e0-8a80-4df7554192b4 | -3.02981 | -51.0314 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ee5cb86-938b-355f-a40e-0ad678181482 | 4.15312 | -59.94783 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdacb7bb-aedf-373e-8524-7b61c958dfe2 | -3.48949 | -50.43937 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 433c4b5d-2bf0-32e0-8566-90214c72e625 | -2.94147 | -49.35402 | 2025-11-26 05:37:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d597a19d-24a4-303b-b2e5-aed20e126108 | -3.45663 | -50.54792 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c128cd6-2237-3f29-bea3-7b137c0a6186 | -3.32754 | -50.26529 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16e05d7b-0c39-3ff7-ae50-d43d309d8f77 | -3.32307 | -49.71811 | 2025-11-26 05:37:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ce9a858-5ee5-37c0-872c-15a33f0bd5af | -4.1719 | -49.85721 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 909c5ca2-7273-3d1d-a2be-d2242056c773 | -3.26593 | -51.17498 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75b8a7b3-816a-32cc-93d3-bedc06d63a4a | -1.10818 | -54.13604 | 2025-11-26 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afa716d8-53b9-3eb0-93b4-80a797d83318 | -3.13701 | -49.40529 | 2025-11-26 05:37:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49e3d67a-3803-3092-b5c8-df4c1d196d81 | -3.45366 | -50.54118 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51cb3adf-c406-37b9-99f3-2db37652ea85 | -3.25954 | -51.17392 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2d18ccb-b93b-37b6-9fc4-c658630d08b2 | -3.26065 | -51.17231 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9e7d335b-b6c5-3660-9a47-0169de59155c | 3.09994 | -60.77087 | 2025-11-26 05:37:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67f79413-6108-3a3d-9c90-915e4510aceb | -2.33298 | -60.06536 | 2025-11-26 05:37:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fef4017c-8cea-3b0a-8076-dce0a2151193 | -3.2324 | -51.18049 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55e26df6-72b2-3c2e-9b1b-e539b0a9e84d | -2.89817 | -50.49738 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b72e07b-7185-377c-b6ae-fdb4e862648d | -4.1789 | -49.85829 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a44c36e1-cf34-33fe-aae9-71694e9686ee | -4.17339 | -49.85826 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cddc8b1-b3ee-33ac-87b6-3ea1ec388110 | 4.23269 | -60.12154 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc4e32e7-1a75-352e-b0a2-153f0cd56e60 | -4.17613 | -49.8782 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 468af3f5-b6fa-302b-b322-3ceb655bf324 | 4.15426 | -59.95496 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 425b9a07-9e35-3df9-9216-f25340351a01 | 3.09938 | -60.76738 | 2025-11-26 05:37:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d95b58b3-1404-3c72-a754-85336d38b801 | -1.38483 | -55.34196 | 2025-11-26 05:37:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| decd1594-66b7-3f05-aca8-910a10545dce | 3.10327 | -60.77034 | 2025-11-26 05:37:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9846bc39-84f3-34c3-9a17-eacec0d9977f | 4.22596 | -60.12253 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e0e9090-1e91-3568-a63d-a8d64e44af11 | -2.87676 | -51.80131 | 2025-11-26 05:37:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0681bd0f-2ef2-3290-a5df-cf10a44c1663 | -3.208 | -50.21604 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edb4b99a-7585-31dd-a6c9-4b0b4b4ba982 | 0.95252 | -60.45808 | 2025-11-26 05:37:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36afeb14-dd67-3492-a9ee-89fdca598f02 | -2.88763 | -51.81239 | 2025-11-26 05:37:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73f49477-1442-3f9a-8360-457c6fcccf93 | -2.87608 | -51.80595 | 2025-11-26 05:37:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe61007c-11df-37dd-871e-8ba019a1c55c | -4.17006 | -49.87047 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0bbdfc0c-7b11-36ba-a764-80f8e2ce2917 | -2.74909 | -51.90147 | 2025-11-26 05:37:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40d81060-3aa2-34e1-955b-ff60e314b26e | -2.88219 | -51.80689 | 2025-11-26 05:37:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd910224-36ca-34fc-bc62-88dfa02abe96 | 4.15544 | -59.96222 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ada2a1c-294f-3432-abc5-77b94616d820 | -4.17848 | -49.87239 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0901c260-48e5-312f-983e-d7430a3f5055 | -3.48512 | -50.44465 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fffdf4be-4a8a-3287-bd05-faa749d1bdaa | -3.2068 | -50.21643 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa776f84-f32c-342c-9fb1-3b2018d52657 | -4.16912 | -49.87725 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d4d27941-e8c7-30fe-9c75-18f601a5d5d9 | 4.22653 | -60.12605 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a29b2241-9ef6-302f-80e5-342e7c6a6498 | 0.84512 | -59.82092 | 2025-11-26 05:37:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a1569d9c-f0ae-3ae4-8841-f03580e4c338 | -2.33037 | -60.06628 | 2025-11-26 05:37:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 834690a8-832a-3b59-91e1-3e55a38b63ed | -3.48865 | -50.44497 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21bd113b-48e3-3146-8693-63856f65639b | -2.74843 | -51.90593 | 2025-11-26 05:37:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d332c6b3-4f96-3786-befb-3dfefe276808 | -3.12994 | -49.40409 | 2025-11-26 05:37:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 324f46a3-6f8b-34a3-a927-2cf8fda82fc6 | -1.36556 | -55.24627 | 2025-11-26 05:37:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb8128b0-388b-30a9-bb6f-4e2b37e9295e | 4.15485 | -59.9586 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3cfbee5-bb2d-3a15-825e-adce771d0d65 | -3.48592 | -50.43905 | 2025-11-26 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d348db1b-2d39-3096-a3b4-58965cab80b3 | 4.22989 | -60.12557 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d0c3adb-77c8-33aa-a898-5a90dab32654 | -1.30643 | -55.43496 | 2025-11-26 05:37:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66d63033-c83b-347f-a409-677ceb573841 | 4.22933 | -60.12208 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 652ad922-61b7-309c-be13-77271ac4e1c5 | -3.44997 | -50.54686 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21d4f91b-c362-327a-aef0-7dd80ba88cc6 | 4.15254 | -59.94425 | 2025-11-26 05:37:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8134f61e-d10f-3b29-9b80-8245c0f00ea4 | -4.17799 | -49.86487 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e99e5bc-63e5-31b0-ad6f-91b859a82347 | 0.84572 | -59.8247 | 2025-11-26 05:37:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 195e6ec5-0c07-3c90-ba0e-e515dc09f0a6 | -4.18039 | -49.85929 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 067f288d-fbe5-3b09-b16e-d54409d8044f | -3.13092 | -49.39739 | 2025-11-26 05:37:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac43399a-2929-3771-9585-7fe4de923cfb | -3.46034 | -50.54206 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54913851-e5c7-3341-8b7a-58824384d137 | -2.88832 | -51.80774 | 2025-11-26 05:37:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84d474dd-5c54-3b37-86b5-de60d937b884 | -3.45279 | -50.54699 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11cd000a-ba2d-3381-b64c-d765e3cd0494 | -4.17047 | -49.87827 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 574a04be-8f5e-3707-965d-058640406119 | -3.20582 | -50.22286 | 2025-11-26 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58145ff5-f93c-3642-a9c6-df568eeb57cd | 2.74158 | -60.72679 | 2025-11-26 05:37:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6de403c4-6045-3b25-80a1-dede87ca1d28 | 3.10032 | -60.77276 | 2025-11-26 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f759ff11-4d41-316d-965d-dc89cde9591e | 4.23211 | -60.1255 | 2025-11-26 05:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c764b457-19a9-3d1f-911c-d68b42b7c4c4 | 3.10499 | -60.772 | 2025-11-26 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38300387-9a6f-3318-b424-27e6e128066a | 3.1042 | -60.76709 | 2025-11-26 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4d1cbc22-3121-3289-a1a0-dcb7763e1bd4 | 4.22728 | -60.12604 | 2025-11-26 05:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50964c78-d646-33a4-8b96-e17f40bb2ebd | 3.1025 | -60.77034 | 2025-11-26 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3d1a1db9-e71d-3c0b-875c-639d4d0c3e88 | -3.32722 | -50.26399 | 2025-11-26 06:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| dd7b3351-837d-34bf-a1b7-3a230268b6d1 | -2.88157 | -51.80146 | 2025-11-26 06:48:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 41a64398-52e8-3ca8-a513-d19ea8e6e280 | 3.10265 | -60.76611 | 2025-11-26 06:48:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3af85a04-da35-3dca-a9d4-47a9ab621c6e | -2.92521 | -48.22154 | 2025-11-26 06:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 3213b0a4-1c60-387f-8cda-b1a3692ace80 | -2.91702 | -48.22819 | 2025-11-26 06:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| f754a11e-179e-34e6-bf78-30060c9dce4f | 3.66033 | -51.29977 | 2025-11-26 12:33:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9fb98d55-e20e-3da5-bd50-687775de60e5 | -3.56109 | -42.40006 | 2025-11-26 12:36:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 46.8 |
| 4217664c-2c2b-310a-84da-638bc761428a | -4.16781 | -43.73112 | 2025-11-26 12:36:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| d1142038-9553-3b76-9f6f-f4547f8c71e5 | -4.17196 | -43.69985 | 2025-11-26 12:36:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| f62b50a0-e7ca-3878-a927-1695c22c69b1 | -3.9931 | -45.44776 | 2025-11-26 12:36:00 | TERRA_M-T | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 3ff6bfc3-bfa9-35c3-8d3f-0fa4f417ca91 | -3.95915 | -42.15549 | 2025-11-26 12:36:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| b13a2491-0535-3fc9-b93f-8cc525a17641 | -4.01637 | -46.49924 | 2025-11-26 12:36:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |


[Clique aqui para ver as próximas entradas](README30.md)
