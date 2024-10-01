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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bf3264c-4b8c-3a28-b951-4ed531de5563 | -16.6443 | -57.26015 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 91f2be70-509e-38d7-9aa4-597145053b76 | -16.64264 | -57.27105 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2ab6eb79-bbd5-3a48-895a-6a2cb3aacef2 | -16.64209 | -57.25234 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 858386b7-21c7-31b2-a26e-a578c76ee608 | -16.64042 | -57.26324 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6158c1a8-946a-3c60-ac55-bdf32ba1720e | -16.63765 | -57.25906 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 9b771f5e-6527-3242-9c96-8b3584c6dfda | -16.63709 | -57.26269 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a881cd2b-de69-3b3f-8219-0962e9994811 | -16.63654 | -57.26632 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8f5ff747-35e2-3611-9abe-1c6bf2042597 | -16.63598 | -57.26996 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c899a43d-7e8d-3963-a09c-c1a695ed0519 | -16.66926 | -57.25308 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 30fcedd8-24c9-3a00-9df6-1fa3d0b517da | -16.66705 | -57.24526 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 529b2cb7-6c92-3327-9c57-0b15959c4e77 | -16.66538 | -57.25616 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 43618c1a-bbda-3b32-acfe-a58b553616df | -16.66316 | -57.24835 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1d24cf5a-f398-3095-8391-0269cd45b93e | -16.66095 | -57.24053 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fb8c6b19-9fef-3762-829a-ff5b4c24abf8 | -16.66039 | -57.24417 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| c072f2d3-b2bc-3a52-9864-ea591fdb94fd | -16.65872 | -57.25507 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b2572eb0-20d1-3470-8061-06e52146d5f8 | -16.65817 | -57.25871 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1aa40a46-c932-3525-a9a1-d80b7e2e1604 | -16.65762 | -57.23999 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bafe1122-0e67-3803-bb42-b0e5e8b310b3 | -16.65761 | -57.26234 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f9ece358-e40a-3a4d-93b3-c4b7763cbd19 | -16.65706 | -57.24362 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 27af2d7a-3593-3619-b654-dc082607c769 | -16.65704 | -57.28832 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f3a6287b-6006-3a85-8348-5f77dc514e1f | -16.65651 | -57.24726 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 8051716d-e47d-37af-8209-090f1fed0f54 | -16.65539 | -57.25452 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b0a3a8f6-a539-3059-ade2-057f4756b3d3 | -16.65484 | -57.25816 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a066aad4-76ed-3f42-b9c0-dcdcd62199b9 | -16.65484 | -57.23581 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 206aea90-03a7-3d1d-beac-d0a20fede8d2 | -16.65428 | -57.26179 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 46c1775b-a306-37ac-b0af-bc95980c29e3 | -16.65427 | -57.28414 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| db637f85-4173-38fa-929f-75282005a359 | -16.65373 | -57.24307 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 055e1c20-89b5-390b-b04e-e7fb1663a4d0 | -16.65372 | -57.28777 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7c3daa2b-2e00-3e19-a4f6-1bb02020bfe2 | -16.65318 | -57.24671 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| e0c5665c-68d6-3760-ba5d-d48a799265bd | -16.65207 | -57.23163 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0c9920b3-17ba-3410-95fc-c5eb5dd5a8aa | -16.65151 | -57.25761 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c432e326-24a8-3ded-8c90-4a10d4464401 | -16.65096 | -57.2389 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 79895c9c-2fcc-3750-b433-a843b5ed23b3 | -16.65039 | -57.28722 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2b52d80a-6588-3166-a409-a8b6276a53a0 | -16.64985 | -57.26851 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6c93b8b3-94d9-3e8a-b3e7-aaeb936a0272 | -16.64985 | -57.24617 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| a5fb2bb3-c5ac-33f4-a2c9-0adb837cf3f1 | -16.64984 | -57.29086 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4168dd59-d5ec-31cd-b53d-a874d8e42aff | -16.64928 | -57.29449 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d6178e95-f5d9-3962-a65e-377723463d04 | -16.64874 | -57.23108 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2382343b-769d-34c4-b845-a95ca13a8903 | -16.64819 | -57.25706 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 51332e2b-cec2-3abf-854d-1f128374c13e | -16.64818 | -57.27941 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fa310c3a-2db7-343b-914b-64d70cc780fa | -16.64763 | -57.23835 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 7f4f44c1-ec92-3720-92c4-c4c970e3642a | -16.64652 | -57.26797 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 35fe163e-69e5-3f36-9271-bb1e5ef56252 | -16.64597 | -57.24925 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 2de7777d-4c36-3eef-a410-cfc168d7f0c6 | -16.64541 | -57.25289 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| ad322d43-8de6-30a7-be51-d393c9cc09da | -16.64486 | -57.25652 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5fa07593-c943-3e30-a36c-3bf707ba9246 | -16.64486 | -57.23417 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| a719673c-ab0e-3b2c-b9d6-e5f8db52d05e | -16.64431 | -57.2378 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 3301ecc3-be56-357b-812e-aa470d1c01c6 | -16.64375 | -57.26378 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ce0732ee-7568-3bc1-b663-b698f8e48c15 | -16.64374 | -57.28613 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d30c5307-d59c-3e09-81ae-35fc9ed77d38 | -16.64319 | -57.26742 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 14bbd776-a804-32af-a97a-1828616e1440 | -16.64264 | -57.24871 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 326a3d95-e136-38cf-a0f7-fafaba605c62 | -16.64153 | -57.25597 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 808f357f-ec09-3edf-a2aa-55cefa751903 | -16.64098 | -57.25961 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1cffcb11-1915-37cb-a9b8-a480dad78a20 | -16.63987 | -57.26687 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c6fadb1e-2641-34ab-8b7a-8db2aa38efd4 | -16.63931 | -57.2705 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9bb2082b-57b4-3bea-bde2-08553658fd1c | -16.63876 | -57.25179 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 161.3 |
| 23eb09f6-4f9a-30e0-897e-742f797977bf | -16.6382 | -57.25543 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| fec46e78-1f59-3857-bfc0-e3161d879e0d | -16.66816 | -57.23799 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d8cc5292-32a3-3f76-90d9-5661b38551f0 | -16.6676 | -57.24163 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ec84ec6a-4a33-3805-bc4d-0e6b0c3aa828 | -16.66483 | -57.23745 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9f377556-2c8c-336a-bdcb-29d517db2de9 | -16.66427 | -57.24108 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 61f466a4-fcb6-3413-8143-7e45b02453af | -16.66372 | -57.24472 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 673cedee-836a-38cf-a01f-60c7991667aa | -16.6615 | -57.2369 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a3c9fa2c-7434-3b8c-9c0f-30a087b73342 | -16.65983 | -57.2478 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 2812abe1-7549-30e8-9e09-bcc100fb5415 | -16.65817 | -57.23636 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 37070a14-4a08-30fc-a7b3-972059ab5498 | -16.6554 | -57.23217 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 365d2154-8edd-34fa-aaf6-e78be473f810 | -16.65429 | -57.23944 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 9a25c844-aa91-3fc5-a554-eb97d1a98b51 | -16.65152 | -57.23526 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.1 |
| b9a47ba2-f373-3e84-ac41-649f4388ea22 | -16.6504 | -57.24253 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| cba57918-462c-35bd-b417-c3539f6e12bc | -16.64708 | -57.24198 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 308.5 |
| 049ee1d2-e14a-33fc-940a-29e084d58a07 | -16.64652 | -57.24562 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 308.5 |
| d7edb730-5a09-37be-9777-5541a8062aaf | -16.6432 | -57.24507 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 308.5 |
| dc3ef145-338c-3523-bcdd-d22e6d20f682 | -16.64153 | -57.23362 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c1e2f576-88af-3b94-bab7-8269cc28624c | -16.64098 | -57.23726 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| adc175e2-4a04-3e2c-94ae-1d5e1da0ecc8 | -16.64042 | -57.24089 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.7 |
| 6ab341cc-9c96-34f4-9518-4b8805e7a29b | -17.08392 | -56.71521 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fc284ff3-1df5-3c9b-b139-6ad9426ff335 | -17.08335 | -56.71896 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 40cf4eb8-7c6e-3a53-91d5-db4d5afdeab6 | -17.08279 | -56.72271 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fcd1dc80-5cdd-3fa9-8b22-e74ccea3f61e | -17.08223 | -56.72644 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3066e630-d7fb-3acf-9864-225f1963cfba | -17.08222 | -56.74945 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fbebcb82-2955-373a-be96-d7bbde303309 | -17.08167 | -56.73019 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3807daf1-c538-35e8-8c1c-47eb5b5c4c6e | -17.0811 | -56.73394 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b90f191d-b2af-3fb1-beb9-119ad9f739d3 | -17.08109 | -56.75693 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fcdbcdec-a50a-35ca-9f35-759f0cb00f5c | -17.08055 | -56.71467 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8bdf5c5f-1e1e-3820-b160-38eba1f733ff | -17.08054 | -56.73768 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0e124201-d83d-3c2c-80a6-6741b9342835 | -17.07998 | -56.71842 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0635901b-d075-3b7e-a2a7-5d97ac605973 | -17.07997 | -56.74142 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 90b8dc4a-9d9f-3d5a-a7fc-f40bb2d5e1cb | -17.07942 | -56.72216 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5b521bd4-65ce-3760-9c91-1142880bd28f | -17.07941 | -56.74517 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b588e5fa-0421-3397-9190-eb04b4ffe1b4 | -17.07886 | -56.7259 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7d1afd99-8ca9-325f-bfd3-90f16e71b837 | -17.07885 | -56.74891 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c1884ab3-2447-3630-bc52-1cf747004495 | -17.07829 | -56.72965 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 651394cd-341a-3e90-ac2d-8339bc8acf4b | -17.07773 | -56.73339 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f3b88228-b7ea-37b0-958a-7ced32f0ad87 | -17.07772 | -56.75639 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4c1e136b-64d9-339c-a933-53f14231a9a4 | -17.07717 | -56.73713 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| e59c1744-f5a9-3189-b03d-83f50df19caa | -17.07717 | -56.71412 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a1b0bd64-fa3d-3457-ba16-eb792068e3cb | -17.07661 | -56.71787 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ba0c844a-c793-3e07-87ef-ee579597051b | -17.07605 | -56.72161 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3bbcefd4-708a-39dc-8cf1-88d4c32ad5dc | -17.07604 | -56.74462 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 83c0629a-7dc9-3c61-a199-863c1492187f | -17.07549 | -56.72536 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README123.md)
