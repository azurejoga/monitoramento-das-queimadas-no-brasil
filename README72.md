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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 002976cf-620a-32f7-ab92-dc172ef7938b | -3.91866 | -51.23103 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 165e64a1-e57e-3223-95b7-81e72584bae6 | -3.88949 | -51.94006 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f404ce-ee74-34cb-909c-23b6b988273a | -3.88666 | -51.93591 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfad3589-3722-39df-be0e-e1413e16b452 | -3.87823 | -51.96806 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 515b700e-394e-3424-bce3-7d0064856f52 | -3.87655 | -51.97892 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cace0eab-faef-35ce-a3d6-dafdfcfef169 | -3.87484 | -51.96754 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91bb24b9-467d-3a67-850b-e94cfa3174c6 | -3.85241 | -51.36154 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbc07cf1-4951-388b-a739-db6392728311 | -3.85183 | -51.36533 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f418d6f5-7429-3455-bee3-790200f07ae9 | -3.8282 | -51.4043 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a89fb87f-0872-32d4-ab2a-1d3eaeeace6b | -3.82763 | -51.40807 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce7f5144-e37c-378d-9fd3-851faa8fb791 | -3.81639 | -52.25645 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27d74b91-c5c5-3354-85eb-12bf0aecd71a | -3.78589 | -51.31661 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c03a51c1-ecdb-37da-a26f-7632f3d67ca3 | -3.78531 | -51.3204 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 51b563e1-01e2-3f9c-bb83-b822e0dab0c5 | -3.78472 | -51.32417 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 1eb0de7a-ead7-314c-acc0-77d57ebd4948 | -3.78243 | -51.3161 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3772b6d9-7aeb-30e9-93bf-8c69fb99578a | -3.78185 | -51.31987 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 316a5c7b-a0f6-30b4-ad7f-d7858e8c0df8 | -3.78126 | -51.32364 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 64afc138-6c6a-37e0-991e-9e83f6dcddca | -3.77897 | -51.3156 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68088734-4366-352b-a916-544d5a4f7ecd | -3.77839 | -51.31936 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4e8c9a2-4eb4-3767-a06d-3fe943e475ec | -3.7778 | -51.32313 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d36569af-6433-363b-b6cf-ccee0c5e6e48 | -3.77639 | -51.85592 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c2615cd-cfac-3c72-8e81-9da94855e8ac | -3.77528 | -51.88558 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91f88946-bb2a-33a6-be0d-9191e1f798f5 | -3.77493 | -51.31884 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 119f7204-7b93-32a6-9dd1-ff2140756efd | -3.77434 | -51.32263 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1699efdc-6de9-34a4-b3fb-6eb167fcf6ec | -3.77133 | -51.88871 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9a24079-813e-3377-9636-915f5c74d54f | -3.76958 | -51.83247 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5633eec-65a8-336e-ac20-c4f3e46a7ed5 | -3.70012 | -51.0761 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3919d7e8-0494-39e3-8b6e-eca9556181f4 | -3.69779 | -51.22945 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd70e31a-15b0-32cd-b0bd-cd411591b5c5 | -3.69458 | -51.15826 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4b602e-504a-37ba-ab79-285fb01c17b9 | -3.69373 | -51.07117 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc45bd14-3b0a-3c31-be1c-bc201bca5a5d | -3.69008 | -51.11813 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5c319d2-ed13-3460-b2cc-a686c4912738 | -3.68675 | -51.0701 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71206a09-ee3c-39fc-a6d7-37f1985c5f93 | -3.6866 | -51.11757 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd210001-6248-3b29-8283-6aba2a19c25d | -3.68615 | -51.07397 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1917a17-9c29-3f51-a26e-d90c03e653bf | -3.68326 | -51.06954 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35890b4f-f5ae-3039-abff-97951498fdd7 | -3.68266 | -51.07343 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2203a190-3536-31ae-ab4a-d01abe03cc14 | -3.67917 | -51.07288 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0064820-7ff0-3269-ba45-138ef55544ff | -3.6753 | -52.11753 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce597cb9-9a21-3bfe-9a65-5ae17055eafa | -3.64727 | -52.12056 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5135457-d7f0-3d04-929f-e302d5c75249 | -3.62246 | -52.03589 | 2024-10-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a71debd-d4a7-3dfc-a523-9e30efb377f0 | -4.65755 | -50.95266 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0bdd886-187d-378e-b1e9-e3a9a3b15444 | -4.65694 | -50.95668 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78c0baf9-9d89-3593-9404-2e68190a7008 | -4.654 | -50.9521 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94209784-55d9-3ace-bdb9-547504e8334a | -4.65339 | -50.95613 | 2024-10-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b32a63e-e164-3a2e-b6dd-39459e220350 | -4.12848 | -50.83528 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a04d1d4c-c5ce-3043-b6b7-7d63226a9bc2 | -4.12787 | -50.83927 | 2024-10-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51be8e2c-f4dc-32f4-9823-1a6fe075d9d0 | -5.60801 | -51.15753 | 2024-10-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85ee7531-e278-3b03-932c-16f341e50097 | -5.59633 | -51.70474 | 2024-10-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6e14dbf-5ea8-322f-8f94-368f70074244 | -8.47964 | -53.23948 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1700717-6d9d-3420-877b-ee22b7c3f158 | -17.55285 | -42.2987 | 2024-10-12 04:59:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2d658f58-3c22-35d6-b285-d01ea55fa9df | -17.55147 | -42.30793 | 2024-10-12 04:59:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5e62cc45-9363-37d0-bf14-0a883c65a0ef | -12.27138 | -54.0 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f009d70-f0f6-335f-98a8-e9e938d03c93 | -12.27082 | -54.00367 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b2627b7-2dfe-3843-a2d9-bcbf55270156 | -12.2669 | -54.00679 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64ef7814-a504-3536-bcf2-7fb5f21b66d9 | -12.26297 | -54.00991 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f89673d-f622-338e-b1e3-c107dd22608d | -12.26292 | -53.98735 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c39c665-5b86-3f6f-b265-c2b45c7273f0 | -12.26242 | -54.01356 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7de72c10-75b8-330c-9d37-83989f29494f | -12.25905 | -54.01302 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58f559d2-2d57-3534-9e97-e56d59986b06 | -12.74751 | -54.00129 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 372d11e8-499c-3894-af7c-f97d298406cd | -12.6855 | -53.99909 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8a68bcb-3536-36fc-9f1f-9090914f2607 | -12.65961 | -54.01021 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9ba7e64-a5e2-360e-877b-fd05c34b3d99 | -12.65229 | -54.01284 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f14ccb4-700a-398a-9e74-5f586780e3b9 | -12.82426 | -53.51584 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b0d14a4-3440-317b-9bbc-64ec041a49e0 | -12.8237 | -53.49614 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f335524-e304-3fd9-82dd-2267c9a7f173 | -12.82369 | -53.51966 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58ab6576-3462-3c5a-8525-756ce5d7e3cf | -12.82312 | -53.52348 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d76b8332-6fbf-37cc-8c4b-c3498c520714 | -12.82255 | -53.50382 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed3b7b21-5b9f-37ee-b8b6-f2c671618250 | -12.82198 | -53.48406 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a040bfb9-8e30-3d02-90fd-44b54a4e1c69 | -12.82197 | -53.50765 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40884722-4c21-3ec6-87ef-e89b4b6c54d8 | -12.82141 | -53.48791 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 445a5015-3586-3dd7-8bbf-454f09ec0c9c | -12.8214 | -53.51147 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f0367ca-30ea-3068-a3e6-868da702bb4c | -12.82083 | -53.49175 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8364d103-0326-3d47-b240-08bf0012ef9d | -12.82082 | -53.5153 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34097915-82be-36b0-9fe3-eee528a0368c | -12.82026 | -53.49559 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc7c08ed-82cb-39e5-83a1-278f365b124d | -12.82025 | -53.51912 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69bfcae8-f285-3e04-ba3d-873eaed8a64e | -12.81968 | -53.52294 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2352e606-7571-3494-9fb7-8f8fbf49907c | -12.81968 | -53.49944 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6380cf82-e3a0-3606-bbb2-28a37077b1d3 | -12.8191 | -53.50328 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75c2da4a-485b-3d8d-bd10-2fb9ee7a0159 | -12.81854 | -53.48352 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae138dd7-0c35-3c5d-b9f5-052dfabe3ace | -12.81853 | -53.50711 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4395624a-7790-316e-ad4c-689b6dbbc1a4 | -12.81796 | -53.51094 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0751276-faae-3de0-9c3a-96a205bedd05 | -12.81796 | -53.48736 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d839fe9-07cc-3417-acfe-5d941a81fc4b | -12.81738 | -53.51476 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 916c8b2b-c881-339b-8563-7ebe19e46f90 | -12.81681 | -53.51857 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acf135e3-93c8-3a4a-a947-4d09d5c367c7 | -12.81681 | -53.49505 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 85e6647f-38c7-3f1f-b9a1-90bfe66676fa | -12.81624 | -53.52239 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 019cf21d-8c6b-3e4f-a08c-d901b4c356e2 | -12.81624 | -53.49889 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 03565025-6481-3e83-8c39-137d77a697ee | -12.81566 | -53.50273 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 17d08190-901e-3c36-a3f5-9ef7e2baefc5 | -12.81509 | -53.50657 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d8d0671-e2fe-3a96-b779-fda99a570281 | -12.81452 | -53.51039 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8c6a9c34-00a6-3a8e-bb81-84cba2f48b3d | -12.81394 | -53.51421 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c7aba9d8-a4a8-356b-996d-22e760421863 | -12.81337 | -53.51803 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7aad311f-e54a-3e3d-8ee7-efcd885df2b0 | -12.81337 | -53.49451 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1452fe00-2ca3-3cd6-8f33-d44c4d9d7218 | -12.8128 | -53.52185 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7a28b2f1-9dd1-38c5-9805-092bab3e6e69 | -12.81222 | -53.50219 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a7efd4b-0488-3ae2-9efc-23daf87849de | -12.81165 | -53.50602 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 48c3a1cd-73cb-37a7-b067-35259b3bec21 | -12.81108 | -53.50985 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5a95571c-6136-34e2-9c9d-5c36c2fa5d61 | -12.81051 | -53.51367 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5b61fffc-892f-3322-8127-c5c1960ddc53 | -12.81051 | -53.49012 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a37378b8-d3be-30a1-9853-bc700109f8a3 | -12.80993 | -53.51749 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README73.md)
