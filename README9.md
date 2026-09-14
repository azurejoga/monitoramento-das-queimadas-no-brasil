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
| 7698b4c5-3381-3e34-be0d-a8a128563883 | -2.92844 | -50.41061 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ac8a7a28-a44c-3d17-a544-96a4bc1a45ee | -2.91474 | -50.45069 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ccbd24ad-fbba-3d40-afa5-2c4d05ba52d3 | -3.79608 | -44.10649 | 2026-09-14 03:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5706f7b-11cf-3540-ad99-4c91740a12b2 | -2.95628 | -50.39209 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a27a6f03-7906-3476-8c1b-b9a58ffd493b | -2.89306 | -50.41693 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 140eaff8-ee94-3f16-b638-fe2804be6af8 | -2.87969 | -50.43453 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 062244f1-fcca-37a2-824e-789ea565d3ef | -2.95042 | -50.40221 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 959da320-9f8d-30e7-a7a8-73974416b379 | -2.96194 | -50.39882 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ea35644e-aec6-3214-8488-c2a9843f68d4 | -2.82593 | -49.235 | 2026-09-14 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76f85e4d-d15a-34cc-a8db-3f88d00f0f09 | -2.76983 | -45.49851 | 2026-09-14 03:53:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09c7d322-e25e-3949-bbe1-4713bf65421a | -2.8922 | -50.40045 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7c53a9b6-f2ac-3c63-a365-1aa598279e1e | -2.93042 | -50.39894 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 305471e7-ac39-3a72-adc6-d28c57b89028 | -2.87666 | -50.43235 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 600faad6-6319-39ab-9ea7-87451362e436 | -2.90174 | -50.40633 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a2d9738b-12ea-30fb-ace6-5c938c571ee0 | -2.89014 | -50.4544 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7844b6f2-5e37-379e-a4ac-4b1a37413a51 | -3.23341 | -43.03759 | 2026-09-14 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65c231f8-abc9-3878-8824-66361a0e7d5c | -2.96758 | -50.40575 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0ab354e-ec4c-325a-8a75-55802d299a88 | -2.9008 | -50.38987 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c65735d3-c683-30f2-ab20-5922ce5524d6 | -2.91042 | -50.39569 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 79136a36-ac80-3eec-9ec1-886ad8450708 | -2.93142 | -50.39308 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| daef76f4-5bbf-3c0b-aa15-dd957cc9a389 | -1.8601 | -47.97716 | 2026-09-14 03:53:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f8ad664e-7559-3a93-be58-61ac5c93a0f7 | -2.88262 | -50.4169 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe6bde2c-fb9f-3e06-b557-0001e1557362 | -2.93509 | -50.4118 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 061f7e36-d32b-3c5b-9af4-ba01c6899959 | -2.88832 | -50.4239 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| b234f903-3981-3551-9d34-8574b3ee9389 | -2.92008 | -50.37928 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 233cdf2d-ea73-378f-be63-39f2cb64de1c | -2.88637 | -50.4159 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 70acd898-3578-35f1-abbf-46cbc358825e | -3.2336 | -43.03394 | 2026-09-14 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5805454-ce80-3329-a455-9108f04de897 | -2.90234 | -50.44279 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 190.5 |
| dd3c146b-de33-38ba-9d53-98552a3fe898 | -2.89887 | -50.40157 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 45edb0a6-6f70-3673-8add-b1c08018563a | -2.87767 | -50.42649 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 749847fa-9327-3822-a689-e8a6343ebcac | -2.9163 | -50.48187 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 53c3317b-a8fe-36cf-b780-b57bb1419ac0 | -2.89402 | -50.43088 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 4582f27a-4a7a-3185-ad08-25238f3a1463 | -2.8911 | -50.44858 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92c7d120-a1c8-3457-8d35-173506375136 | -2.8813 | -50.44525 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c37d4d22-d3ca-39f0-b491-bf963a08de3e | -2.92442 | -50.43417 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 5e4b2135-c7a0-3a3a-9167-6a7a5434a43e | -2.92144 | -50.45172 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| c9e124b5-8a26-3935-ac58-03dde54d43d8 | -2.90337 | -50.43683 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 190.5 |
| f2de23b3-65a3-3e24-97dc-7725318af391 | -2.92542 | -50.42833 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 6f767de2-dea0-3f27-863b-d5aef8aa3bdd | -3.22431 | -50.59259 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d9f3071-6f89-3063-ac45-068d4df9e200 | -3.46532 | -47.46733 | 2026-09-14 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f3393633-eb76-33be-9e9c-8f6389e60556 | -2.89623 | -50.4784 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95ca4929-3e3e-363c-8bf9-a54283130cda | -2.89161 | -50.46527 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b26b52c8-d558-3ec4-8e60-3de3ea8b79f2 | -2.9514 | -50.39639 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f712eafe-7643-3170-a1d9-3dd7a5fdb7fa | -2.92241 | -50.446 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 26d90f13-d401-37bb-98cc-9d6d090819bc | -2.90291 | -50.47966 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 325ef597-ed57-3035-875d-7fdc05e43806 | -2.94248 | -50.44915 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cdca9550-8518-3170-b900-56d5168c6e0f | -2.91943 | -50.4635 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 80d9e1b7-f91b-330c-907d-c9edb72c9521 | -3.24295 | -43.02803 | 2026-09-14 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5812ef67-ee7d-336b-af0d-d76d321c8e71 | -2.92277 | -50.40365 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 159.3 |
| d4f3bc72-37b2-300a-9e85-3a9f8bcd5134 | -2.95709 | -50.40324 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6ef5dd76-794d-3a75-a5f4-f016bfd87478 | -2.95887 | -50.41635 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6a0d3be5-4ee5-35fb-91d7-26e93bed4f90 | -2.90475 | -50.38884 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 261233e9-3861-3baf-a26a-2c2e7f3fda05 | -2.92642 | -50.42246 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2c6e9dd8-8680-3caa-bb0f-a5e8f7ad31c5 | -2.88638 | -50.4356 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| c10f0507-304f-36b1-be3f-2c1e36c34487 | -2.88319 | -50.49643 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a602a1b-1f2d-3a50-af49-c31262bb70bb | -2.92342 | -50.44006 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| c8afac3f-e3b9-33ce-b8b2-86094cd16856 | -2.95323 | -50.40944 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 31c0fc1f-e85f-3048-8dcc-42afa7bb3f0c | -2.96296 | -50.39304 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9490f0a-f5fa-3ee3-bbc4-01fb4b57cdf8 | -2.90503 | -50.46726 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 59ebae13-5828-3558-9a0f-5e75cc59fe5e | -2.89709 | -50.39354 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc76b7f0-8ebf-334c-98fa-1c30556bb437 | -2.9161 | -50.40256 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 159.3 |
| a8255ff2-75ad-3b07-9581-d3d2b11a32db | -2.88226 | -50.5021 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a487e682-27c5-3125-8d8e-5fdc097a0dbe | -2.89809 | -50.38775 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66a83637-1e56-3797-9385-41cb818c74ed | -2.88359 | -50.41106 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ffa09bc-da92-392e-bfa3-f8b8e814d0a1 | -2.88455 | -50.40525 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2895b3ff-9f84-38ad-a805-aa7434fd351b | -2.91243 | -50.38401 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2212716f-89e1-3c9b-8db8-6b06304b38e9 | -2.88493 | -50.46406 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a3573a75-0a02-36bc-be2a-9c2d8fe80d79 | -2.9096 | -50.4808 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| d9549582-5af4-3394-92b6-55e2d69bb9fc | -2.95513 | -50.41489 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 581f02f0-090e-30c6-8f98-6fe76f941484 | -2.8983 | -50.46639 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 19ec4647-c5da-3d72-8285-85dbce19539f | -2.9341 | -50.41761 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4ea62fc8-5ac2-3ef9-931f-bd9788b048a7 | -2.91572 | -50.44492 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 331.7 |
| fc61887c-65d8-3272-9096-d398083b9ef1 | -3.7867 | -44.10927 | 2026-09-14 03:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a644c42-0662-39b5-9f3f-f82e4f603f6d | -2.89021 | -50.51352 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9d0fa33e-6331-3fd9-9aa5-51a0111f95c7 | -2.8979 | -50.40742 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9fe16c31-d69a-3a64-bb31-9419f8c46b9b | -3.59545 | -43.04396 | 2026-09-14 03:53:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c67012a-807c-3a8c-b2bb-14acac27d12c | -2.90667 | -50.49796 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 802b8b6b-d4a9-3060-918a-d23eef7f7014 | -1.85943 | -47.98132 | 2026-09-14 03:53:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 21bdd42e-a358-37c4-9b73-bb1abfde7a3e | -2.88699 | -50.4521 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 219db82e-e359-39eb-af0e-c06db9c54b98 | -2.89221 | -50.50188 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 23f4762c-b637-3533-ba65-1cd5b30a5a0f | -2.90803 | -50.44974 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e234968d-cae3-3dd7-b250-0bd305f8148c | -2.89103 | -50.42869 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| a7c9e49c-2866-39fd-9739-dc409299f202 | -2.93879 | -50.43039 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 93822770-fc73-343d-9244-244cd7d0bb92 | -2.88743 | -50.48956 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0a8b936b-a5d1-3344-b177-b945003b9cd1 | -2.95785 | -50.4222 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f71b9d34-6888-3992-b1ad-89d29eabda9e | -2.93382 | -50.45974 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 775c3951-4adb-3672-a1ca-161d5ba8b797 | -2.89122 | -50.40636 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6fb971c4-fee7-353e-a49b-13e0cd857730 | -2.95611 | -50.40905 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e6dd1c21-84f5-39fb-9a61-cad528f19102 | -3.79541 | -44.11065 | 2026-09-14 03:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a8d5365-227f-362c-8697-44cacabb28fd | -3.74176 | -40.42456 | 2026-09-14 03:53:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 51c36ae7-787f-395d-b9f3-0ebf412fcaac | -2.87773 | -50.44633 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f97101cc-726c-3294-abd2-e79bd522bb05 | -2.89499 | -50.42501 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 89a3c43d-5b4c-3fb0-8b6b-3e17a17ec7be | -2.96475 | -50.39841 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| de5831ba-ddc5-39b9-af31-3a1c8da6bcc9 | -2.91375 | -50.45649 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 293c5051-4499-3699-81bf-61fc925eded2 | -2.92613 | -50.46457 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f5398a22-6242-34dc-a133-db242094fae7 | -2.9378 | -50.43625 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0ad29374-6bdb-351c-b7f0-7e42e92b0451 | -2.92476 | -50.39196 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 34bac5ef-481e-3437-8145-2f2ca31078f9 | -2.90375 | -50.39466 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 55c1451f-1559-3577-9836-e1ea8631a91d | -2.89506 | -50.40531 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bb5c4a8-3567-3357-b954-f18e78387983 | -3.46593 | -47.46381 | 2026-09-14 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README10.md)
