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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d73c74c-572c-3451-aa07-60f5850bf5d7 | -16.52593 | -57.24854 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 79559c83-631a-3c8e-bdee-69d62a043276 | -16.52528 | -57.2532 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 55473438-3721-31db-b2d1-0fc9734be4b9 | -16.52281 | -57.24331 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d860debf-819a-3507-88cb-45caa5b7cad0 | -16.52216 | -57.24798 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b5b8f9d2-098e-3e7b-a9d4-85da24d5594b | -17.17266 | -57.34893 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| fcf7ac2f-ce58-356d-80fc-eafea721c219 | -17.16759 | -57.35779 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| be926d31-0f0f-3c61-be06-053f717fb753 | -17.16512 | -57.34779 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.0 |
| d1d5d32d-2186-337e-af73-c9a3417b1e46 | -17.16422 | -57.41 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b17330a4-1a47-3e6c-b709-519bad0026dd | -17.1607 | -57.35194 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 29b8b693-95b6-396d-a5c0-b1d6ed93e113 | -17.15981 | -57.41412 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6e9368a4-6a00-3bab-a402-144ca6c7faa9 | -17.15693 | -57.35138 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| c89cbaa9-dc67-35a2-8aa5-50c3630f7f2c | -17.15606 | -57.41357 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f35afa47-feb3-39fc-a690-12daaa1cb76c | -17.15445 | -57.3414 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| a49d269b-671f-3eda-b817-04fd32afdddb | -17.1538 | -57.3461 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| b2c04fe1-f5ec-34a3-8778-8de022be1313 | -17.15316 | -57.35082 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 08e9b688-c499-3ae8-993e-c37e340eff98 | -17.14498 | -57.35441 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e19d5f6c-c943-3b34-954e-337c39231c7a | -17.13175 | -57.36685 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d9dda9cd-fed6-3206-aac3-d37c02a42fea | -17.12671 | -57.37569 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c0113889-e0b6-308f-b707-cce05cfecd38 | -17.11664 | -57.39333 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 9919fae3-1aa9-3ef2-bf40-cd339bcab84f | -17.11605 | -57.3693 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9975459c-1a7a-329c-9853-1aba1c656722 | -17.11225 | -57.39745 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2ff6731e-7841-33b8-ac10-7b0ed17c2e17 | -17.11165 | -57.37344 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 811df19d-50d4-3f90-bc77-04519336bc43 | -17.11039 | -57.38283 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 23317853-256d-3a7f-821e-510ce62057a7 | -17.10975 | -57.38752 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2e841154-1830-3a49-b798-ab1009845898 | -17.10849 | -57.39688 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| eb4543e4-97c5-383d-9e01-c8e0df96fe8a | -17.10659 | -57.41093 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 79392f8e-c8fb-31fc-8992-8a3a93c6f247 | -17.1041 | -57.40101 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9b777138-3b5c-3993-a2aa-cb796f21d7d0 | -17.10389 | -57.3988 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ecda84b6-b45c-3e78-a25c-d38423f5de17 | -17.10346 | -57.40569 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0a17a395-b1f6-3a4e-a3bf-67d367a3c9f4 | -17.10342 | -57.37483 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| b9764174-f704-3490-9410-d1f09a61c537 | -17.10323 | -57.40347 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4fc40328-5d15-3065-9b77-a0de6ae98cae | -17.10286 | -57.3817 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 7366f056-779d-3f5d-b6a9-ebc7727f9bf5 | -17.10223 | -57.38639 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 0eff34c5-f149-389a-a2db-9c85cc97b542 | -17.1022 | -57.41504 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5fff7b67-5a72-3813-9344-830c8989f5b7 | -17.10034 | -57.40045 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 116827e2-34f6-3ac6-acc9-f96980dfaf74 | -17.09908 | -57.4098 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 8b6e1fab-efad-3f00-bb0f-f2f89054b77d | -17.099 | -57.37896 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2585b58d-7d60-3c6f-a4d5-05c7c44ea70c | -17.09882 | -57.40758 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e5bc3a50-8774-3790-b982-6bd66d788066 | -17.09769 | -57.38832 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d3d1f202-3bde-35aa-9dff-4be176381068 | -17.09658 | -57.39989 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3ae34ea4-dd92-39d6-b7aa-f09be67c0431 | -17.09506 | -57.40702 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7ced17d0-a47e-315b-b5cb-f1bad90ab9d9 | -17.09375 | -57.41635 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 62dfb3b4-0b49-363f-a1f6-c125e95be50b | -17.09157 | -57.40867 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c34551c8-eb52-34ec-a9d7-c7c6d25f7a05 | -17.08999 | -57.41579 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1a0648ce-be00-388a-80f3-1e4d3ea331e7 | -17.08624 | -57.41523 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 882ea22d-caba-3142-a8e2-ae179a1b3bb8 | -16.82049 | -57.3659 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 926a2b62-2ea7-3f71-a2d1-2609ce8bbc38 | -16.81985 | -57.37055 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| f6afe0e5-8331-3f8b-a852-618181b26b91 | -16.81921 | -57.3752 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 79feecab-6d57-3606-8643-3b88336c7fb3 | -16.81858 | -57.37984 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f95bd936-c212-3497-a271-1d8751bf803d | -16.81794 | -57.3845 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 644b9a09-3aae-3850-8d4a-51cfb69fa136 | -16.81666 | -57.39378 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| a898d2dc-e932-3117-acd7-454d572c4cdb | -16.81419 | -57.38393 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 237e367f-fdc4-320e-b962-6618bb93f759 | -16.81355 | -57.38857 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4ad87d39-2139-3d19-ae9a-7ec3dda8a01f | -16.81292 | -57.39322 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f1a82695-6011-36cc-a008-3050f5203714 | -16.81228 | -57.39786 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fb2e0014-4c25-3cb7-ae71-7fa679947a89 | -16.81164 | -57.40249 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ecf6bc56-5578-376d-8b3c-7530e46025c0 | -16.80542 | -57.39209 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8f97e1df-6fc2-31d0-869d-272bdaf1bf4d | -16.80352 | -57.406 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a8e8150b-5897-3798-ac7d-9efb062ab8b3 | -16.80041 | -57.40081 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0dae70e3-8698-38ad-8776-a4336b9ca655 | -16.79978 | -57.40544 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 717c0c7d-0c9d-369c-9599-202c96e6f17c | -16.79667 | -57.40025 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 505d3c3d-7071-30da-be72-5495e66b5a5e | -16.7923 | -57.40431 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 18c3c4ef-5cf7-3100-9f17-e8cd3fd9e9ab | -16.78418 | -57.40782 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| d6c61ffe-22ad-382b-b068-cae0f553ede1 | -16.78355 | -57.41245 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ea3d7d16-429c-3394-8a34-65aba661b34d | -16.79162 | -57.43724 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4993bdf3-9f7d-3b36-a9a2-3f00d356d49b | -16.79099 | -57.44185 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e2aaa08b-a554-361b-9076-874b71fe6b4e | -16.78662 | -57.44589 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 73b4cc28-a6c6-31c9-9ce0-1439e3b941d2 | -16.78595 | -57.47866 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 0cc40250-bb87-3d98-aee3-2e1885bdb1ad | -16.7854 | -57.42688 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 3df0e07a-a389-30da-94d9-ebbea07ef2d7 | -16.78167 | -57.42632 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| e46c5658-2fea-32a4-9028-06cd74740c3e | -16.78104 | -57.43093 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 9cf3bca6-a895-3f7f-8378-98114148b177 | -16.78041 | -57.43555 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c3ce1c26-92a7-3d02-b09d-9c920da1ed2f | -16.77909 | -57.50102 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5a7ff40f-48d1-3d51-ba69-046ed9c3bf5a | -16.77846 | -57.5056 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8f0e1fc9-331e-3954-8adb-ca7a821e13e3 | -16.7779 | -57.45399 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ffb6a764-2f62-3d39-b52c-79830c723137 | -16.77728 | -57.4586 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 559c4dde-53d9-3e1e-bdf8-b9a7d7f208bf | -16.77537 | -57.50045 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3e2cc732-97bd-3a00-ac68-c2225849935f | -16.77477 | -57.47699 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 628321e7-0f70-3352-9577-8aba10b1fa73 | -16.77474 | -57.50503 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 57806c9b-a0ef-3a8c-acc1-5c66d1b19ff4 | -16.77414 | -57.48158 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6db94f1e-c2ce-380d-8034-131ac5a7cf92 | -16.77165 | -57.49989 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 37205502-4dad-3a67-abba-d898910e6033 | -16.77104 | -57.47643 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4316ae36-e53d-3692-8274-d79235770d8c | -16.77058 | -57.47438 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a1c124a1-30b9-304f-bdf5-9791fd7aacb4 | -16.77042 | -57.48101 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 9b6f2259-8353-3aa5-b9b9-728db21b0d72 | -16.76993 | -57.47897 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2c70926c-f65a-35c7-a25e-373dcb411b77 | -16.76928 | -57.48354 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| f15b133e-7835-35ff-b51f-c876ec1e9edc | -16.76855 | -57.49476 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| aabb69b9-a1e3-32a3-9b58-39d02dc4a005 | -16.76797 | -57.4927 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 193e854b-97c9-321e-9cf3-ddc5bf7ad44f | -16.76792 | -57.49934 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 0da185d3-53a2-30c5-b1f1-a52ef2d831a9 | -16.7675 | -57.46924 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 93a73cc8-8724-3a06-8d98-4d156d21ee61 | -16.76732 | -57.49726 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 836601a9-e4ec-3ab5-952b-f2b9451c8823 | -16.76669 | -57.48045 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7bc12bf9-14ac-304d-a164-13c51a55a1e5 | -16.76482 | -57.4942 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6f790fa7-b664-386f-9378-91c1cb03b264 | -16.7642 | -57.49878 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 8e0f8bae-3f66-33fa-9170-3e85ed4f3cc9 | -16.7636 | -57.49671 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 47266cc4-d7e7-32b7-8862-da8972fd0f3f | -16.7611 | -57.46556 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8d3d1c01-dc6f-3a7f-9fce-e6ce7ab7c873 | -16.7607 | -57.46354 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d73803c0-966a-34d2-a793-2d4ffcf8744a | -16.70287 | -57.46891 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d201813b-1c03-32f0-9de4-eaa48cc42902 | -16.70041 | -57.45918 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 220bfd02-2b09-3e80-b936-1a08de924f6f | -16.69359 | -57.45347 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README119.md)
