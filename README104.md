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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 204027c4-c7c2-3a12-9c80-1ad0f75fe4d0 | -17.745 | -57.5138 | 2024-10-30 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 4a59c4aa-0142-36ac-bb3d-1f2870af909b | -19.5083 | -56.5989 | 2024-10-30 13:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 7e306c41-d677-3772-a5dd-08c130425d92 | -19.5087 | -56.5779 | 2024-10-30 13:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| e544549d-6fd6-392a-9be6-4d15ee473f10 | -20.255 | -55.4318 | 2024-10-30 13:26:59 | GOES-16 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 5687179e-2133-3376-877f-885b8c16d9d4 | -23.9923 | -54.1106 | 2024-10-30 13:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 124.6 |
| a91b4c04-f16c-3738-a025-c16454c766ff | -3.4076 | -41.6432 | 2024-10-30 13:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 9e4e0d9b-9521-33f8-a19b-6d047c0dabd8 | -3.3891 | -41.6201 | 2024-10-30 13:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 89576fea-7fce-3cb5-a116-e9ca1b8d9f28 | -3.9326 | -41.4957 | 2024-10-30 13:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| d1db0169-6492-3d10-a6a4-b0396b573d0b | -4.2563 | -43.4368 | 2024-10-30 13:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 401.5 |
| e35864a4-42a5-3bb6-9a7e-4ff9b25fe47c | -4.2561 | -43.46 | 2024-10-30 13:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 203.9 |
| a044d84b-c09e-3d8f-a461-ab5955d2c345 | -4.8617 | -42.4858 | 2024-10-30 13:35:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| b8d265d2-4b8c-320f-ac3e-70ea7fc8be70 | -4.8619 | -42.4622 | 2024-10-30 13:35:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| f7f644d4-f348-3350-8a94-8e438c41b192 | -4.9311 | -43.1857 | 2024-10-30 13:35:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 7422ef20-516c-34d9-8717-2ffb6dc9c3f6 | -17.7443 | -57.555 | 2024-10-30 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| dc924ba8-1324-3e27-8f58-cfbe737da773 | -17.7446 | -57.5344 | 2024-10-30 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| fb6e3645-9744-3949-9457-e9cc26787686 | -17.745 | -57.5138 | 2024-10-30 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.0 |
| bb47591f-26d6-3949-b848-55ad3aff7392 | -19.5662 | -56.7164 | 2024-10-30 13:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 18c39cfa-5cba-3fa7-ab88-a3e7b8b83679 | -19.5465 | -56.6983 | 2024-10-30 13:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 7a0b7663-0977-322e-9ec2-60f0af066546 | -19.5866 | -56.6926 | 2024-10-30 13:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 566b1f79-0d20-3f73-ba72-3b157643e707 | -19.6067 | -56.6898 | 2024-10-30 13:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 164.3 |
| 406f52de-c79f-380f-89f7-aeb478d93c17 | -19.6268 | -56.6869 | 2024-10-30 13:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 157.2 |
| 15e58712-7f81-3662-ba20-1d50a90077af | -20.255 | -55.4318 | 2024-10-30 13:36:59 | GOES-16 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 287f6898-7587-3dfa-a3d8-645a5da7d47c | -23.9923 | -54.1106 | 2024-10-30 13:37:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 94.7 |
| c49bbfda-be41-36b0-807a-0a16a8341aa8 | -24.0128 | -54.1286 | 2024-10-30 13:37:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| ee1af4b1-03c2-3671-bda2-4591c247a177 | -3.9326 | -41.4957 | 2024-10-30 13:45:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| eb8ef1f9-4940-31b7-8c26-13c393c33281 | -4.8619 | -42.4622 | 2024-10-30 13:45:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 01f47208-13e9-358b-a79a-bcb6fb5f7bbc | -4.8617 | -42.4858 | 2024-10-30 13:45:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 3b1559ee-74e2-3b4a-8591-9fcceb35f44a | -4.9311 | -43.1857 | 2024-10-30 13:45:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 249f3ec7-0dd1-3b1d-b8aa-f86f2d54e5ac | -6.225 | -41.2548 | 2024-10-30 13:45:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 58c9bc59-7ded-3af7-b4f6-360acb32e250 | -8.2799 | -37.6075 | 2024-10-30 13:45:52 | GOES-16 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 121.3 |
| c7ae1d24-8091-36fc-8618-67e794ea8341 | -17.7868 | -57.3649 | 2024-10-30 13:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 555078c1-9c10-344d-b15c-9ccf23e1f5fc | -19.487 | -56.6647 | 2024-10-30 13:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| d86390e2-df47-3df1-9a3d-a8e39f433678 | -19.4677 | -56.6256 | 2024-10-30 13:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 0bd5d505-8d01-3b6b-b444-a29f89255a09 | -19.4874 | -56.6437 | 2024-10-30 13:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 740ea330-dc20-3582-84e0-8bf74ab62a7f | -19.4878 | -56.6227 | 2024-10-30 13:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 0f87f073-5a2a-3505-9a49-ae2e306422c1 | -20.255 | -55.4318 | 2024-10-30 13:46:59 | GOES-16 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 20e69aec-4e47-315a-a82a-542c5fe3f973 | -24.0128 | -54.1286 | 2024-10-30 13:47:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| 638e34bb-0080-3b4a-ab5b-4473e24f9edd | -24.0123 | -54.151 | 2024-10-30 13:47:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| dc8b57ef-de88-328c-afcb-9cc4fbc13e2e | -23.9923 | -54.1106 | 2024-10-30 13:47:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 121.9 |
| df31a71c-dba0-3eeb-bf81-b8678efe4a63 | -3.9326 | -41.4957 | 2024-10-30 13:55:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 43305054-0b1a-337f-b77e-c7b9a1809f87 | -4.8619 | -42.4622 | 2024-10-30 13:55:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| d7690da2-23ca-3db2-b1a4-b433eb4f7f61 | -4.9311 | -43.1857 | 2024-10-30 13:55:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 4b61124f-448a-3f33-ac4c-39ecf6cc4814 | -6.9782 | -41.3277 | 2024-10-30 13:55:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 0802ce79-bf14-3f1e-a958-9fd0017b785b | -7.8833 | -42.9534 | 2024-10-30 13:55:50 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 734413d5-a8f4-3c94-94e4-fa3353266cff | -7.883 | -42.977 | 2024-10-30 13:55:50 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| a9b60af4-a5b0-35af-8daa-0d7ecd454450 | -19.4677 | -56.6256 | 2024-10-30 13:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| ddba852c-a4d8-3186-9e89-5e483f7c68b2 | -19.5087 | -56.5779 | 2024-10-30 13:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 5577bc43-5753-343c-9fb1-d12a5e96ccd6 | -19.4878 | -56.6227 | 2024-10-30 13:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 88c4e5d5-5cbb-30d7-859d-72acd7ef63af | -19.4874 | -56.6437 | 2024-10-30 13:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 153faab8-7118-3271-9a91-bbcb383fda15 | -23.9923 | -54.1106 | 2024-10-30 13:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 140.6 |
| 8a5856f8-a4fa-32cc-8189-a648f1facdae | -24.0128 | -54.1286 | 2024-10-30 13:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 162b9268-d57b-34aa-90c7-354874b5a0a4 | -24.0123 | -54.151 | 2024-10-30 13:57:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.5 |
| 4fda63d4-f7d2-301f-a037-1567b5b1e6b7 | -3.7767 | -42.4798 | 2024-10-30 14:05:27 | GOES-16 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3ed2bc74-7c22-35b7-8626-a68073546aa2 | -3.9326 | -41.4957 | 2024-10-30 14:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| 1958dd16-879d-326a-aa21-2f3c11852fae | -4.2561 | -43.46 | 2024-10-30 14:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 5fc8a2c4-055e-31c2-b8e4-09a0d2c86f98 | -4.2563 | -43.4368 | 2024-10-30 14:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 424.6 |
| 7abe95c0-0003-34fa-a4ca-ecff65421641 | -4.7626 | -43.1967 | 2024-10-30 14:05:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5b348961-4fe5-3f3b-b145-e5acb53aaf0f | -4.8619 | -42.4622 | 2024-10-30 14:05:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 25f8f251-b54d-3bf6-b0c9-eb9ef2e214e6 | -4.8617 | -42.4858 | 2024-10-30 14:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| cea8c48c-5ddf-3212-8d40-f563c1dcff49 | -4.9311 | -43.1857 | 2024-10-30 14:05:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| a31471b4-a01e-3fe2-ae58-0994194eecfa | -6.2404 | -41.5912 | 2024-10-30 14:05:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 289f3605-321d-327c-92c4-9dc7ff270b41 | -6.2401 | -41.6153 | 2024-10-30 14:05:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 0531f6c3-862e-37ce-be0d-4b35c3d0eb2e | -6.9971 | -41.3258 | 2024-10-30 14:05:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| ca1e07a7-0a30-3824-bf2e-672317d1e06c | -7.3967 | -44.2386 | 2024-10-30 14:05:48 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 633d93cf-dd24-3a32-bdac-b46d527d96ef | -7.883 | -42.977 | 2024-10-30 14:05:50 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 191aff35-28e9-3923-88d1-54e2de72dfd3 | -7.8833 | -42.9534 | 2024-10-30 14:05:50 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 19121498-f4e3-3366-ab0a-8715cbf6daf4 | -7.9019 | -42.9749 | 2024-10-30 14:05:50 | GOES-16 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 170c3142-d83c-34c9-af36-97d11f1ebdb7 | -8.8395 | -40.9171 | 2024-10-30 14:05:56 | GOES-16 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 3fbf5a0b-eb91-3722-81f9-0bd3306a5dbc | -8.9882 | -41.1422 | 2024-10-30 14:05:56 | GOES-16 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 9d074f05-877d-3396-8898-9a8e78df1d80 | -13.7713 | -43.1088 | 2024-10-30 14:06:23 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 132.5 |
| 5506ff3f-28fb-36e5-bbd3-c5b3279713a8 | -14.2727 | -41.6215 | 2024-10-30 14:06:25 | GOES-16 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 145.8 |
| ef586689-84c6-3a8b-8a2f-1ec7a387012f | -14.2531 | -41.6256 | 2024-10-30 14:06:25 | GOES-16 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 137.1 |
| eca55071-f1a4-3381-9da6-5ca3f21ead6a | -19.4886 | -56.5807 | 2024-10-30 14:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 5ed8fe76-615a-3a43-a559-4b6645de72aa | -19.5087 | -56.5779 | 2024-10-30 14:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 40c844a4-07d8-3777-901b-ff64c1abdfff | -19.4674 | -56.6466 | 2024-10-30 14:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.2 |
| 752eff1d-65fb-3ef8-920b-93b0ca389e3b | -19.4878 | -56.6227 | 2024-10-30 14:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 0037fcf8-4fb9-31fe-97f5-1744c9b72643 | -20.255 | -55.4318 | 2024-10-30 14:06:59 | GOES-16 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8aa311ba-61f2-3887-a4e2-e67a22f3eb22 | -22.7959 | -53.5071 | 2024-10-30 14:07:12 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 77.6 |
| f0614e7a-7463-32e7-b688-c9ffe1cc0e10 | -23.9923 | -54.1106 | 2024-10-30 14:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 127.9 |
| fedfa4ed-4fb8-3613-846d-75a81e46ef35 | -24.0123 | -54.151 | 2024-10-30 14:07:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.1 |


