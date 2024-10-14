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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47f702f3-e495-3cf6-8ba4-f464c8f77fc5 | -17.94309 | -57.31496 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 076ea3e2-76c7-3008-865b-d1cb08e0139e | -17.94251 | -57.31908 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 3a937923-4e37-3097-bed2-a129f163f5a9 | -17.94192 | -57.29795 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 213.8 |
| 1d27318c-5f14-3204-8190-2dace5af6d4a | -17.94133 | -57.30207 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 9bbf0c0d-285a-3db1-b88d-13530b43c610 | -17.94075 | -57.30619 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| cda91236-0afd-3aa7-8b54-8e3a236306ad | -17.94016 | -57.31031 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 8888dbe1-eeb7-3927-83f4-d03a990735f4 | -17.93958 | -57.31442 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| bfd061aa-9130-3f04-a9a2-5d2600d6eeae | -17.93899 | -57.31852 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fdfd1d17-2499-3f6f-b879-2b8f89b0690c | -17.93898 | -57.29328 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 213.8 |
| bfc91bf9-a9df-3e57-9644-0bae687fb7d1 | -17.93781 | -57.30153 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| f3f00e03-bb1b-36a3-a9d5-c7b75c63b9ea | -17.93723 | -57.30564 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| f5bea820-9b5e-3ab3-b787-9f484dafadcb | -17.93664 | -57.30975 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| def949b2-d5c9-30c1-8840-87568700fb9e | -17.93606 | -57.31387 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 583d2b06-e8f8-3437-9d53-6fbbb094d5f3 | -17.93547 | -57.31798 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 13507192-f757-3e00-9af0-3a840620cb3c | -17.93546 | -57.29273 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 95c6b7ec-b450-37b1-884b-a4b7bfd1d098 | -17.93488 | -57.29685 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| d4e9f224-1cc5-3d73-8299-f996720239f2 | -17.93429 | -57.30098 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| ec2eb929-23e8-3ad3-ab5a-2dd91bb4e9a9 | -17.9337 | -57.30509 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| c3bef324-7a93-3a8a-802f-6e71857ccce4 | -17.93312 | -57.30921 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 702f8dd3-1f39-3727-a451-092ac31aff66 | -17.93254 | -57.31332 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0694788f-6849-3140-b4c9-777ba54fffcb | -17.93195 | -57.31743 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ab462065-4046-3bfd-a489-c8a8a24d763a | -17.93194 | -57.29218 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 18c406c1-16e9-36cc-aba0-faaef5b08775 | -17.93135 | -57.29631 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| a8e9b51d-11a7-3eec-a570-eacf18f50ad4 | -17.93077 | -57.30042 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 8ff18d80-4fca-3188-b10c-356f97b5581e | -17.93018 | -57.30455 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| d6321fae-6cf9-366c-b90f-f25446a9f90f | -17.9296 | -57.30866 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5823cfef-bc93-31fd-8dde-5c32fcc68bdd | -17.92902 | -57.31277 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e0f5dbde-88cf-361d-b893-86eddafe4e78 | -17.92842 | -57.29164 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 9bb11928-f054-36aa-9a67-6b09b6e5021f | -17.92785 | -57.32099 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1013b4e3-2d0c-370f-99db-ff518e7475cf | -17.92783 | -57.29576 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 9b7b9d8d-7bfd-3883-9337-65868e2c4178 | -17.92725 | -57.29988 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| a6bb6ce2-fa50-3d7e-b8dc-668b3de6d26a | -17.92666 | -57.304 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| d6ef8982-7b52-382e-8791-015ec888772f | -17.92608 | -57.30811 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bf795a36-c2e3-39ac-a45e-05852875baa7 | -17.9255 | -57.31222 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 79707648-daf1-3a5c-a0da-b7f593c32850 | -17.92491 | -57.31633 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1c9dc8a2-9519-3c58-8866-ff395f74ea4e | -17.92489 | -57.29109 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 42b579db-37d7-36b2-b4a6-06769091db00 | -17.92431 | -57.29521 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 1cbdea26-3f7a-380e-bebe-5e9b0a647f63 | -17.92373 | -57.29933 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 70fe59d7-2e67-3567-8839-05a129330391 | -17.92314 | -57.30345 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 8ec017a2-495a-363a-b38a-68c210a1268e | -17.92256 | -57.30756 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2610370a-327c-3540-8f5e-ea5e4ba87eca | -17.92198 | -57.31167 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8c428038-ae04-3cd8-b3bd-58316118a3d5 | -17.92139 | -57.31578 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9d29a689-1453-3637-95a3-5fa6035e5bf4 | -17.92137 | -57.29054 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 262.2 |
| acb565c7-fa8f-36b1-ba1d-cf382644edbf | -17.92079 | -57.29466 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 262.2 |
| 1f70b451-aef1-3760-88ac-0a31059905ad | -17.9202 | -57.29878 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.3 |
| bbb5f34a-45fc-3a80-8e58-7030f7513de9 | -17.91959 | -57.27762 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9671443a-57e4-339e-abda-d492f92edbdd | -17.91846 | -57.31112 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| de7674e0-975e-3c40-932a-391f549653fa | -17.91787 | -57.31524 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 171eb458-670b-375d-87a0-48b16d2c1055 | -17.91729 | -57.31935 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d12641d4-5e92-36ef-a92e-461c1bea4940 | -17.91726 | -57.29411 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 262.2 |
| d841eff7-e2c3-3fce-8313-b50b82d7e8a7 | -17.91668 | -57.29823 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.3 |
| a3ba333a-e8b9-3298-aa71-24109687ed65 | -17.91552 | -57.30646 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0e19c59d-7316-355a-9c15-bb884f006194 | -17.91549 | -57.2812 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 05e0fb95-1b55-3b39-a51e-0c99e96ca288 | -17.91435 | -57.31469 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 27cbe6ec-3513-3df7-8b8a-db6ab4d2c068 | -17.91377 | -57.3188 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6e2fb42c-8c60-3291-b06c-4d6ecbce11ce | -17.91374 | -57.29356 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 389.1 |
| 8957796a-8658-3601-a0a5-ab51d1dd2c61 | -17.91316 | -57.29768 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.9 |
| a63b5c00-65da-387f-a0ae-3fbb112a7360 | -19.12802 | -57.70472 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fb75f3a7-0515-3537-8270-085a13d09375 | -19.12742 | -57.70881 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 3fee9039-c07e-3529-abef-ec8743f7ad34 | -19.12683 | -57.7129 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| a9abeb3a-a628-3f9d-a19a-c7da9e541a36 | -19.12392 | -57.70827 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ccfc39c7-1153-3403-8156-cae733fed3c4 | -15.60715 | -59.39727 | 2024-10-14 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8687fc29-820f-3949-9d11-57c19f2f4e89 | -15.60384 | -59.39671 | 2024-10-14 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58e2086e-3576-3bfb-be49-eaebc3ce137e | -15.60328 | -59.40028 | 2024-10-14 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 708d7f96-2e4a-3a38-9cd3-93c40d82fe8e | -15.60272 | -59.40384 | 2024-10-14 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca054b83-2d17-328d-9660-567e7696b292 | -15.59941 | -59.40329 | 2024-10-14 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbf67e7b-0a03-37a1-947f-46c6d95c9352 | -21.56411 | -48.01366 | 2024-10-14 05:12:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5f50d40-513c-3f82-8199-cb4955525a1f | -21.55761 | -48.01301 | 2024-10-14 05:12:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc28846b-d9cf-3079-b7d4-634472df7dfa | -21.55714 | -48.01881 | 2024-10-14 05:12:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38592016-0147-3c7e-936f-b3101a6f46df | -21.55668 | -48.02461 | 2024-10-14 05:12:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b5075dc-0b6c-365e-bd27-4a1e352eec8a | -18.59495 | -50.22534 | 2024-10-14 05:12:00 | NOAA-20 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d6f05130-278a-358b-9524-867e5b076723 | -18.58907 | -50.22847 | 2024-10-14 05:12:00 | NOAA-20 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 394463e3-95ac-3885-b3ee-ea280062e27e | -18.02156 | -53.68059 | 2024-10-14 05:12:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d9bed2e-fa44-342c-9e12-60ad58d5fb38 | -16.74956 | -52.84275 | 2024-10-14 05:12:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2ae343e-fff8-35d0-a75e-dfdfd7359c9f | -18.02589 | -53.68123 | 2024-10-14 05:12:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a2dd6d1-5e77-3292-aa18-7a422c188e9c | -17.63927 | -56.29 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c8963a0b-ce73-3efb-a76b-f0941b2e8fc0 | -16.41175 | -55.92855 | 2024-10-14 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e924da7c-7a62-3dbe-9f29-1d69c41d739b | -17.65351 | -56.24113 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4c4a4edd-e1e6-31d6-979e-18c04f30e240 | -17.65288 | -56.24567 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 962a301a-a008-3baa-981e-623d0c7fc520 | -17.65277 | -56.30127 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1679fa7e-3073-3c0d-9a1c-f851df1ce499 | -17.65226 | -56.25024 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 204e8edf-b49c-352e-be58-e4facc53a4af | -17.65214 | -56.3058 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 489ab1c0-2b37-334b-a306-047eca931456 | -17.65163 | -56.25479 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 976c3427-878e-3f8a-a7f8-94cde083bb42 | -17.65152 | -56.31033 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 55509eeb-91ca-383d-9210-0f027c028dce | -17.64971 | -56.2962 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6558d6cf-0d75-3fb4-aaac-0da87ea3fdca | -17.64908 | -56.30072 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a8ef2d2f-3d22-38a9-bed4-5aed106bfbbc | -17.64846 | -56.30524 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| dd910807-6fe6-3d69-a688-c8b0c9faec6e | -17.64794 | -56.25423 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4e45a74a-2a30-3d35-bf1b-c6ad4c2cce97 | -17.64784 | -56.30977 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 81594227-0fd4-364d-a1f2-7721524312cf | -17.64664 | -56.29112 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 55b580ae-f3ce-352f-8878-ab1f3c78e4fa | -17.64602 | -56.29565 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4c9b3445-2f21-3768-8ffc-ec09682c35bd | -17.6454 | -56.30017 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 56f68507-1504-3902-98a7-4f31bf78200f | -17.64478 | -56.30468 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 882fac8c-19ae-3c12-95bd-6e6da15a4592 | -17.64296 | -56.29056 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 185f3eae-52c5-38a5-b6a6-8225a5891418 | -17.64234 | -56.29509 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ccaf4d59-3378-3d38-89e9-ab15c24743d8 | -17.64172 | -56.29961 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0d570037-07da-35bf-8188-4344136d0ae1 | -17.63989 | -56.28547 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bf56b35b-2f5e-3257-b5a8-ed3a26fd115f | -17.63865 | -56.29453 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| eed6c990-8ef2-36aa-a9a9-d99121657a36 | -17.63803 | -56.29906 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 031c87ed-02a0-30fa-822f-933fce543378 | -17.27486 | -56.73795 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |


[Clique aqui para ver as próximas entradas](README122.md)
