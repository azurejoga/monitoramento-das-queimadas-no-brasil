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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf04f767-17a1-3ecb-a914-4ec01628800f | -10.7542 | -46.1894 | 2024-10-05 01:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| f09d940f-4ed5-395b-81a9-0dfc081ad91b | -10.5757 | -64.0248 | 2024-10-05 01:06:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 25676cbe-aeea-3e20-b93c-714ed0aa6455 | -10.5943 | -64.024 | 2024-10-05 01:06:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 54767dab-1797-39d0-9df6-f4208b8a7ce1 | -11.0966 | -54.2336 | 2024-10-05 01:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d15b27ea-7cc0-3024-9582-573f1333cbd6 | -11.1155 | -54.2319 | 2024-10-05 01:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 01db3f8b-2822-3ddf-a7ad-f12d1fdb9c2d | -11.1158 | -54.2114 | 2024-10-05 01:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1e1c14cc-5897-3a00-9380-77d942d868ca | -20.7799 | -47.7393 | 2024-10-05 01:06:15 | METOP-B | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb10c1e-1f0f-30da-b635-4b285e9313eb | -20.783001 | -47.751701 | 2024-10-05 01:06:15 | METOP-B | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a89f0656-4f4b-38c4-9977-90e75cbe4f66 | -20.7862 | -47.764 | 2024-10-05 01:06:15 | METOP-B | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1bd1a8d7-266c-34bb-80e7-f0d20b0e4628 | -20.770201 | -47.7421 | 2024-10-05 01:06:16 | METOP-B | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ca5c0b56-5e28-366d-bc91-9bd543f94334 | -20.7733 | -47.754501 | 2024-10-05 01:06:16 | METOP-B | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bc6bc443-6435-3520-baf4-9d4956d1f6b8 | -20.776501 | -47.7668 | 2024-10-05 01:06:16 | METOP-B | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e62173ea-40e5-353e-876b-8fa474ba32bd | -20.7605 | -47.7449 | 2024-10-05 01:06:16 | METOP-B | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 982ada6e-318b-36cd-a7c0-7da4bff59775 | -20.763599 | -47.757301 | 2024-10-05 01:06:16 | METOP-B | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c02fbf25-29c0-30a6-95ab-b31840f172aa | -20.750799 | -47.7477 | 2024-10-05 01:06:16 | METOP-B | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 91e6b5b6-4287-347c-9264-cf9e927af5ed | -20.9198 | -48.999901 | 2024-10-05 01:06:18 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57703d96-340b-3b53-9116-10228fd38020 | -20.9224 | -49.010399 | 2024-10-05 01:06:18 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d128622-6313-3f4b-aa75-920f4a5b353c | -20.9249 | -49.020802 | 2024-10-05 01:06:18 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 12f6a5c4-5683-36f6-97bb-93d0dbec1cf2 | -20.912701 | -49.013199 | 2024-10-05 01:06:18 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7bde7cc5-8b04-3584-b9e8-2ef6e8f1cb52 | -13.3976 | -61.957 | 2024-10-05 01:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 183.3 |
| 6c5eb113-7bfd-323d-8c9e-4f34f2bc5683 | -13.3978 | -61.9376 | 2024-10-05 01:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| de441485-6f58-324e-b8ae-8fd712d8bebc | -18.860201 | -43.582298 | 2024-10-05 01:06:28 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f59e331-5d72-32b8-b123-f5f0c80357c1 | -18.8507 | -43.5853 | 2024-10-05 01:06:28 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb42f52d-19f1-3a30-a7bd-0489fec956e2 | -18.841101 | -43.588299 | 2024-10-05 01:06:29 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4820f333-19ad-3506-8332-a6e4c1709c27 | -20.5877 | -51.374699 | 2024-10-05 01:06:33 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b43501e2-8255-30da-a1fa-376b5ecc1663 | -20.5896 | -51.3829 | 2024-10-05 01:06:33 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad38b6d4-e209-3ffb-8a6d-4abe9e3456ec | -20.576099 | -51.369099 | 2024-10-05 01:06:33 | METOP-B | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3d807074-ee86-30f9-84ba-beb995ac0ef0 | -20.577999 | -51.3773 | 2024-10-05 01:06:33 | METOP-B | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f994194d-769f-32a2-9ae3-d9a173339dfb | -20.579901 | -51.385502 | 2024-10-05 01:06:33 | METOP-B | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8000530e-283c-36f4-bb92-2dfa827a62ab | -20.581699 | -51.3936 | 2024-10-05 01:06:33 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 767af651-bb23-3221-b340-d7c7c4dadae5 | -20.570101 | -51.388 | 2024-10-05 01:06:33 | METOP-B | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 75af4f0b-c985-3ce6-bdc3-61a65a91edee | -20.571899 | -51.396099 | 2024-10-05 01:06:33 | METOP-B | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f452807-2af6-35d9-8160-b696cac0fbff | -15.7484 | -49.9365 | 2024-10-05 01:06:34 | GOES-16 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 9ed967a5-41cd-32ff-94f3-346707c8c5db | -15.768 | -49.9334 | 2024-10-05 01:06:34 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 35e9b450-e7df-3e06-ad42-d4cfee5c13dd | -15.5597 | -57.4553 | 2024-10-05 01:06:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 8fb4f08e-56cb-3eb0-b82b-c979f97898ea | -15.5791 | -57.4532 | 2024-10-05 01:06:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 0039065f-8b6f-36d1-afdd-52bf6b888c1d | -15.7151 | -57.4184 | 2024-10-05 01:06:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c78b940c-c84f-34fd-a4a7-6598bf1cc7a2 | -15.7346 | -57.4164 | 2024-10-05 01:06:35 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a60e196f-547c-3146-a4ba-2f45678cb16c | -16.0897 | -50.452 | 2024-10-05 01:06:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6fc9197a-372b-3609-872b-4f5ead6801ca | -19.137899 | -46.618099 | 2024-10-05 01:06:37 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 97089d16-3ad0-3d70-83dc-b1ed1d978cb4 | -19.124201 | -46.605499 | 2024-10-05 01:06:37 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b4cd8164-9ec9-3ab3-80ea-0cc5ccaf7e27 | -19.1283 | -46.620899 | 2024-10-05 01:06:37 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ce8933ee-7b50-3819-bc5c-1860a1ac3e31 | -19.035999 | -46.428699 | 2024-10-05 01:06:38 | METOP-B | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c8c4cf42-3491-3f04-b3df-5836f34d863b | -16.4155 | -57.3619 | 2024-10-05 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| aef2d699-8664-3ee8-8e55-6fd56ca22f9c | -16.554 | -57.2237 | 2024-10-05 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 172.6 |
| 930afcf9-d4c8-3a7d-b899-b6c4c9b428b5 | -16.5544 | -57.2032 | 2024-10-05 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| d9d502bd-4dda-3b1f-a9fb-259456b3473e | -16.5742 | -57.1805 | 2024-10-05 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 189.8 |
| ef32310c-9bf3-3b71-8fb7-a4cd3038ffeb | -16.5745 | -57.16 | 2024-10-05 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 178.7 |
| 4ba27b41-c56b-3d24-819b-177ce297e458 | -16.5935 | -57.1988 | 2024-10-05 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| e5ab8609-f873-3eab-8a67-b3a3ee04203a | -16.6598 | -55.5219 | 2024-10-05 01:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| baf16820-66fd-34d2-9b33-2fbe083a0df2 | -16.6871 | -57.4536 | 2024-10-05 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 1e131f2f-d3d6-3a4d-a3af-ec1fc353a9df | -16.7647 | -57.4856 | 2024-10-05 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 161.4 |
| f285f871-8ddc-3cb1-9703-84f2af55581d | -16.765 | -57.4652 | 2024-10-05 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 9b6862ad-066c-36cf-b80a-2bdbbcf736bb | -16.7843 | -57.4834 | 2024-10-05 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.4 |
| 5772eef6-b2be-3e81-9a41-b01813cda726 | -17.3866 | -40.4602 | 2024-10-05 01:06:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 120.5 |
| 01071b89-c59c-33ad-89a6-c01412c1272b | -17.3873 | -40.4343 | 2024-10-05 01:06:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| bfb7e805-a5e0-3fdd-922a-5fd662b597fe | -17.4067 | -40.4548 | 2024-10-05 01:06:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 261.9 |
| 0c4d4818-b371-3751-bdd7-912f25a74225 | -17.4075 | -40.4289 | 2024-10-05 01:06:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 144.7 |
| 0110178a-5b0d-3b3d-ac38-c03a0d0c2f3d | -17.4269 | -40.4494 | 2024-10-05 01:06:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.0 |
| f7778e24-af47-346d-bdd9-29f157d32bb7 | -17.0695 | -56.7733 | 2024-10-05 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 13791168-0920-3446-bb78-42ae3c395c04 | -17.0888 | -56.7915 | 2024-10-05 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 833e5f85-6490-3406-8b28-114081cf4bad | -17.0892 | -56.7709 | 2024-10-05 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |
| bc6c41ac-66e5-386a-8959-0e548939ed08 | -17.1085 | -56.7892 | 2024-10-05 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| 0e866a17-3837-340a-a26a-eca26589dd48 | -17.1178 | -57.4244 | 2024-10-05 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.1 |
| f072504e-021c-3177-b175-e9b4038ca2a3 | -17.1182 | -57.4039 | 2024-10-05 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 186.7 |
| 77ba4e56-70d2-326d-b37a-2ade3a27df74 | -17.1185 | -57.3834 | 2024-10-05 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.0 |
| c5d64c24-43a5-3d10-aa35-0c893010a6ff | -17.1375 | -57.4221 | 2024-10-05 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 198.9 |
| 27ef92f1-0c90-34ad-b147-224a10eb3f51 | -17.1378 | -57.4016 | 2024-10-05 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 235.8 |
| d51b7bbf-a346-3b75-9dd1-06a1c5804a36 | -17.1381 | -57.381 | 2024-10-05 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 134e8b22-6434-3503-8540-d8b881bb2745 | -19.121099 | -48.2001 | 2024-10-05 01:06:44 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0582a196-2ee2-3a9f-956a-735fcb506d00 | -19.124201 | -48.212399 | 2024-10-05 01:06:44 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e088e7f8-d95e-3042-8744-7d8782b8d1d1 | -19.1273 | -48.224602 | 2024-10-05 01:06:44 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 691f6f0b-9e78-36ea-bd39-7e8ae7c84990 | -19.0854 | -48.223202 | 2024-10-05 01:06:45 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 279e51c7-2cc6-30a8-8bfc-498ecf36bd78 | -19.088499 | -48.2355 | 2024-10-05 01:06:45 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4a9cc820-5071-34a6-aac7-5c54cb90324b | -19.075701 | -48.226002 | 2024-10-05 01:06:45 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a3d335af-7704-32a4-a0e2-39dd881efc05 | -19.0788 | -48.238201 | 2024-10-05 01:06:45 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc5bcc6-a226-318a-a1a3-9dbb159ea6b8 | -19.0819 | -48.2505 | 2024-10-05 01:06:45 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9f7d7ab-a25e-3034-849b-c094ab18edc5 | -18.2985 | -54.2231 | 2024-10-05 01:06:48 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ffe47ffa-9a0a-3978-b422-fabbc9490f09 | -18.8606 | -43.6084 | 2024-10-05 01:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| a35565b0-bbcd-336a-941a-00f4c56144d9 | -18.8613 | -43.5837 | 2024-10-05 01:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| 98f361c3-0d6a-3ea1-8ab2-f47a0a3d1d1a | -18.8809 | -43.6032 | 2024-10-05 01:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.0 |
| 0090e87e-530b-3582-a07e-0a7470f17ae8 | -18.8816 | -43.5785 | 2024-10-05 01:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.3 |
| eae343a2-d7ca-341b-8b91-d69ad7da9609 | -18.6582 | -57.2967 | 2024-10-05 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| f1ec8454-54d1-3289-83ef-5ad41d5db207 | -18.6586 | -57.2759 | 2024-10-05 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| bff8b7a1-c4c6-37a4-89b6-8f5162eaff84 | -18.6782 | -57.2941 | 2024-10-05 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.6 |
| f570967e-f322-3da0-b794-92912e55b78c | -18.6785 | -57.2734 | 2024-10-05 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.7 |
| 39310d20-2fb4-35e8-9bcd-7aa44c82b72d | -18.6981 | -57.2915 | 2024-10-05 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 56d2928c-4c8b-38e0-8321-72191d14faaa | -19.0944 | -48.2415 | 2024-10-05 01:06:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 511518d8-ce17-36f1-acfd-6473ce2c4f2c | -19.1348 | -48.2329 | 2024-10-05 01:06:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9f74214b-3375-3189-b06c-5b540ab4c411 | -19.1354 | -48.2098 | 2024-10-05 01:06:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 74d9b994-e596-339b-a284-059706ca6563 | -20.5904 | -51.3907 | 2024-10-05 01:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.1 |
| 9948f027-3f13-3c74-add1-4a239c5c32c7 | -20.7895 | -47.77 | 2024-10-05 01:07:01 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 91.0 |
| b39c33c1-08f5-3790-8a67-a2859fb3a4b7 | -20.7901 | -47.7465 | 2024-10-05 01:07:01 | GOES-16 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 100.3 |
| ab1dd870-c8a8-306e-9703-eff937319e7e | -19.665899 | -56.438 | 2024-10-05 01:07:06 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0413f9cd-4e65-3138-8f06-ae72660f5469 | -19.6675 | -56.4459 | 2024-10-05 01:07:06 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f405f5f7-6aa8-3b26-8e9c-0d3aff2703d6 | -19.656099 | -56.440201 | 2024-10-05 01:07:06 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 01029de6-a61e-3f9e-901f-c9f4bf3e370c | -19.6577 | -56.448101 | 2024-10-05 01:07:06 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bdd68e4c-088a-338d-8c91-29d882e0d96e | -19.659401 | -56.4561 | 2024-10-05 01:07:06 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 155b9359-7bfe-31ef-bb12-465fa3729bfc | -19.643 | -56.476398 | 2024-10-05 01:07:06 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5f1dbe56-8dc7-386a-8bb8-310f81465868 | -19.644699 | -56.484402 | 2024-10-05 01:07:06 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README16.md)
