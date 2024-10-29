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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24fbbf22-00c7-3564-8060-80485fe9a0c2 | -2.81547 | -48.44146 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 186a4347-4f57-397a-838e-152396590cb0 | -2.77235 | -48.6946 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6efa900-c881-3155-9bac-55f754118c23 | -2.76636 | -48.71123 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab912585-dff7-3323-93d4-10f5546d096b | -2.76528 | -48.71809 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3030b6c1-4adf-3631-9512-451e3b835f16 | -2.76401 | -48.6617 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 541e4237-f2dd-3dfc-baaa-fbf75d744931 | -2.76252 | -48.71415 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2908c25b-5b9c-3779-856f-ccadad9fa15b | -2.70317 | -48.63467 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e1ef739-fc53-3260-8974-a7ad8284d122 | -2.70263 | -48.63809 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a91c703a-783e-3d93-a934-de53d3e07f3a | -2.69987 | -48.63416 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05c03f8c-7b7f-3597-bdf4-f272e4628637 | -2.69933 | -48.63758 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d16aa58-2c85-32d4-8954-eaa57c58b9d8 | -2.69658 | -48.63364 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 830db9d0-cd9e-31b5-8e13-c05659b7efc9 | -2.69604 | -48.63707 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 064d7f7f-2997-3e59-af53-c1a83d380d06 | -2.6955 | -48.6405 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 481164f4-c24a-3864-bd3b-fafd881bef72 | -2.69496 | -48.64392 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0fc3e43-4e6a-36e0-b540-3b16ca07b7a7 | -2.6922 | -48.63999 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1c5a7bd-af0e-3336-b563-e46735e72205 | -2.69166 | -48.64341 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8f1ea7e-a38c-31d1-a656-b291c8b47861 | -2.69112 | -48.64684 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76ea090c-12d1-3e3b-b90a-a69ac0fb9fd3 | -2.65424 | -48.49003 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1fd1165-e1d6-3a18-af3f-216f6e25bcbb | -2.65262 | -48.50031 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d5bb615-d9fc-3af8-8b9c-2b64bf9b3354 | -2.64932 | -48.4998 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d32b3ecf-ef26-32cc-9a4c-615797b974e8 | -2.63957 | -48.54041 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8110b48-4871-3c86-ab03-aeb46008f570 | -2.62799 | -48.52808 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43e8b52f-4d5e-3a99-a8f5-7b316f4f71b9 | -2.62745 | -48.53151 | 2024-10-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 400c4bb0-990a-3c42-ab2d-3abe142e2833 | -2.31892 | -47.48256 | 2024-10-29 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a5515e7a-3a53-3b39-ac93-3141f825e7a6 | -2.21553 | -47.77282 | 2024-10-29 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab3164c6-39dd-3eac-b13e-0cc1e40a1f81 | -2.19421 | -48.82174 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd4469cd-f929-352e-86f4-d12d717fa3c0 | -2.19367 | -48.82518 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcf3f550-9ca4-37bf-8b0d-ae6ef9b960c8 | -2.19085 | -48.80012 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8213399-3077-384a-8864-06312bc7c1fd | -2.18755 | -48.79961 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afc3fd78-2cfe-3589-8809-e598c160ecde | -2.18533 | -48.79223 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 795a596b-fded-32fd-acf6-7c9fb105de00 | -2.17859 | -48.72362 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3678eff4-21ac-3c88-a8bc-b43d56e6a122 | -2.17806 | -48.72705 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 24f29b22-e18b-3f83-a342-ed464a75dfbd | -2.17529 | -48.72311 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c730415-21ae-356c-9f43-dfce689a8a0a | -2.16188 | -48.83007 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 804eb4c1-026b-32e6-8ab4-89d3d78ab262 | -2.16041 | -48.53822 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72c9989b-5c4a-3b3d-b25b-1bf15c2c1091 | -2.12716 | -48.37868 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56e245ec-e938-3008-bef8-e548a94ee3cb | -3.04836 | -48.01682 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1cad0d2-e87b-37d1-b814-2b4610b5d05f | -3.04505 | -48.01631 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e40e5bb4-46e9-3755-ba62-006f83ff0ab7 | -3.03296 | -48.02859 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b2ee762-e6f9-30a4-b7c8-ae6ec73997e6 | -3.02885 | -47.94649 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef2568b1-8b36-3b3f-906e-bf951307dc48 | -3.02662 | -47.93905 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc649046-13e7-3086-a645-6b0576f6e097 | -3.02329 | -48.11189 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7abee18c-4b2c-3e88-9f52-f727dfef80a2 | -3.01998 | -48.11137 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca6d0514-4449-386c-82d0-71a9f773cccc | -3.01607 | -48.09311 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d7be2ba-7386-3f9f-837d-85fb1095470e | -3.01277 | -48.09259 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9703afc4-53c6-3b44-b3ce-fa3c88509e57 | -3.00892 | -48.09553 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae7b5d1e-ee3c-3996-8bb0-cb57df5aaae6 | -2.99069 | -48.08211 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 672c7cda-d03c-3ec1-a8dd-97a8e0998220 | -2.97408 | -48.05834 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b733fb48-938b-360a-8552-32b4c7c673da | -2.97131 | -48.05437 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5926d744-cc3c-3da0-96c5-b594f7827847 | -2.97077 | -48.05783 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b62fcdf1-6721-32f0-9747-5418242f502c | -2.97023 | -48.06128 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d837ca71-d596-3430-99ba-56d0ea699479 | -2.96969 | -48.06472 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef9addfc-76d8-3165-869f-7b2545e2b79f | -2.96915 | -48.06817 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fecfcd1f-638f-3743-98b7-eff6d65c82d6 | -2.96746 | -48.05731 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e7ba33d-2dd3-3be2-ba03-af536e2756d3 | -2.96692 | -48.06076 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa69362c-4682-3f02-9f2e-ceea83ce06ec | -2.92586 | -47.866 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd4dd249-7c92-3bed-b081-b8aa340c902c | -2.92532 | -47.86947 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7957868-e3d2-3fcc-ba15-dd433fefe564 | -2.91266 | -48.0587 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea14c72b-9979-3a99-b8bc-c8b3b6a65140 | -2.90881 | -48.06164 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ab07ffc-8aaa-3537-b31b-49d0370dcffe | -2.89188 | -48.27755 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e955da90-183e-3dc7-83e4-811ab6b82047 | -2.86912 | -47.90333 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b23e2f7d-27ed-3ef6-850f-053d1a5a08aa | -2.71867 | -47.99334 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61be415b-8b1b-3234-9b0a-857c09a98c5d | -2.7159 | -47.98938 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 183073cb-5a3d-3a6d-9878-914be29a1e45 | -2.71536 | -47.99282 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee5d28af-f424-3040-9efc-de8c902a0521 | -2.70532 | -48.2979 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15ee7d73-5c3a-3ef4-89d9-3f31d1e35c26 | -2.70202 | -48.29739 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a1639b8-5159-333f-ae59-c7f55cbb3978 | -2.66294 | -48.13289 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af4a2f53-663c-38fb-8aed-96dc983334ed | -2.6624 | -48.13633 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f0d656f-f2d8-3a84-95aa-7088439fa64d | -2.66017 | -48.12894 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8f0cfe0-4e1a-3ed6-8435-1dc2c8e3c5e2 | -2.62068 | -48.31629 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a98b3cd-ebf8-3077-a8d0-85211f8f44b0 | -2.62014 | -48.31972 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0ddbc3d-8cdf-3845-958a-720d29e8f66e | -2.61738 | -48.31578 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0225d94-1423-30f1-bd26-1356fb5d400f | -2.61577 | -48.32607 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73f3ed53-2b72-3a58-bd5e-e0a92d51ff5a | -2.61392 | -47.94484 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b49ce9b9-6fdb-315d-8a38-4492f4730539 | -2.61262 | -48.36773 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e92e178-7395-33bb-b1c2-51f41cb9b789 | -2.61247 | -48.32556 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a63fe8b-8613-3a9a-bf51-7f7f3726326f | -2.61208 | -48.37116 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e17e84c-a278-3993-8cf8-bf0a448ecfe7 | -2.61061 | -47.94433 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d48d9f06-f710-38e2-8d34-f3ffe277174b | -2.61007 | -47.94778 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b081b01-b713-385e-8b1b-19b628e0c5d1 | -2.60917 | -48.32505 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f053a2c-13a1-3e32-8db2-63f5b60e1c44 | -2.6073 | -47.94382 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34beaa10-19e9-3078-abb0-5c2c1785e1c7 | -2.60676 | -47.94727 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59b701f4-4c4f-3fc7-b771-d457aedd931f | -2.60272 | -48.21508 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81b1c1c8-52ee-3df7-9891-ecd21a0455f9 | -2.5993 | -48.21051 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4c215dd-35c5-3152-9ea3-8ae93a9667ef | -2.59876 | -48.21395 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dfa2b4e-1364-370d-a399-f869d1622359 | -2.59654 | -48.20657 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be452fe8-b20b-3cb8-90a1-b3e8d36a56f4 | -2.596 | -48.21001 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4d0edfe-fb69-38cb-bcf7-71aa4736c33a | -2.58866 | -48.14905 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdfc0ec6-bdeb-33b8-a1b8-8e53bc7421f9 | -2.58812 | -48.15248 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c20fb6fd-c88c-3667-9994-2fac699c1572 | -2.58536 | -48.14853 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3630ba99-6e43-3797-aaaa-e5274871e090 | -2.58259 | -48.14458 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee736c42-4e7f-3d3e-a3b3-6cc4dcc624ed | -2.58206 | -48.14802 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a35f5a2-a504-3875-bd54-a7afba4ca8a4 | -2.57875 | -48.14751 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d305b1c-cac5-3875-b8db-be5fac3cff10 | -2.57213 | -47.97371 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 287571f5-841b-322c-bff6-0e768f5385bb | -2.51762 | -48.12749 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fe395a5-0150-306d-9e26-3dc1839d26b3 | -2.51708 | -48.13092 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c203f5e-892a-3f38-9fa8-cde887ed8894 | -2.51431 | -48.12698 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3657596f-4bfc-379e-a500-6ce9a49765e1 | -2.5127 | -48.13728 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03a9d07e-c072-3715-b7fe-363867669798 | -2.51223 | -48.31301 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31b655fd-2b5e-3ad9-9f94-056eefa82f0a | -2.50994 | -48.13334 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README41.md)
