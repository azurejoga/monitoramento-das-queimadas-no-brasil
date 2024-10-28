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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89bb23e4-bda9-304b-a2a1-495b7da9d993 | -3.9713 | -44.2135 | 2024-10-28 14:25:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 57ab4e4f-d644-328a-8952-998e3259a567 | -3.9525 | -44.2374 | 2024-10-28 14:25:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| a8deef7a-a38c-3ea7-bbfa-78518f47af25 | -4.1639 | -43.2792 | 2024-10-28 14:25:29 | GOES-16 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 29e06d16-9f61-3f51-b23e-8f961f959af2 | -4.8617 | -42.4858 | 2024-10-28 14:25:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| 5208026d-fed8-3924-85bd-089a0e0d1827 | -5.1019 | -42.8932 | 2024-10-28 14:25:35 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| f74928ff-c68e-37c0-98b4-d912efbb58b5 | -6.0421 | -42.6096 | 2024-10-28 14:25:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| afed83b3-3088-3bf5-8543-ae571beed2fe | -6.6767 | -43.0255 | 2024-10-28 14:25:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 704855a5-e8e9-3b70-93fa-9d659aae273f | -7.3909 | -44.7445 | 2024-10-28 14:25:48 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 77cbab1f-e31a-38f9-9557-b12e6ccc432c | -7.3912 | -44.7216 | 2024-10-28 14:25:48 | GOES-16 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 408c8082-a9a8-3db6-b064-6f2422c8ea49 | -7.41 | -44.7198 | 2024-10-28 14:25:48 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 09b797d2-2cba-38cf-82fa-f6f56e1c605c | -9.4319 | -44.5034 | 2024-10-28 14:25:59 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 34410a5f-ff39-35d5-9c3a-b9b75d973d98 | -13.2874 | -53.7248 | 2024-10-28 14:26:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d28db169-aa12-3bc8-a79c-dfe0720523b2 | -13.2877 | -53.704 | 2024-10-28 14:26:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 0adb9cf9-e0cf-381f-aec1-2d19f47e9a78 | -1.0243 | -48.83 | 2024-10-28 14:35:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 7e6368fe-fd3c-3146-86ca-c2301ef2a5ef | -1.0059 | -48.8302 | 2024-10-28 14:35:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| aa88178a-0b3f-34f1-8aaf-8cff69ebfa98 | -1.4396 | -54.0966 | 2024-10-28 14:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 2c0884a4-29b9-399d-b7bd-679752401809 | -1.3932 | -49.0387 | 2024-10-28 14:35:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| bbb8ec55-0280-3341-a63b-64608ab29eec | -1.4944 | -54.2763 | 2024-10-28 14:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4d27525b-0bcf-3d19-9471-8bc303ae1f9c | -1.4213 | -54.0767 | 2024-10-28 14:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 4965f1ca-9533-31c7-aa29-c87435727b99 | -1.4397 | -54.0765 | 2024-10-28 14:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| f74cea96-b0a4-3f0a-bd11-2ee8affd4874 | -1.4213 | -54.0968 | 2024-10-28 14:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 177b41ba-da64-3e37-8db2-39b968cc293f | -1.5262 | -47.2029 | 2024-10-28 14:35:15 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 76118d2f-7012-3aa7-89e0-c41abad30110 | -2.188 | -48.7248 | 2024-10-28 14:35:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| b6bde096-f623-3ee7-b130-7b2298e00794 | -2.1125 | -49.2809 | 2024-10-28 14:35:18 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 32288e62-71eb-39bb-825c-d0096d788016 | -2.0599 | -55.7792 | 2024-10-28 14:35:18 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 3d47660f-a6be-3275-bef6-d4f173f1982e | -2.1126 | -49.2597 | 2024-10-28 14:35:18 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| faf95b84-d67b-317f-b564-a48a66050e2b | -2.3763 | -47.6636 | 2024-10-28 14:35:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| d9b563fd-9007-3ec7-98c3-fffd13f0a191 | -2.3919 | -48.5484 | 2024-10-28 14:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| b33dfb75-55d4-37be-a5bf-fb0ca73006f6 | -2.3055 | -46.6591 | 2024-10-28 14:35:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 434ba6d4-8749-356b-9023-00d1a8053969 | -2.2664 | -53.7221 | 2024-10-28 14:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 159.7 |
| 7ac24a88-4376-3cfa-9a57-3a3f49bf408c | -2.2889 | -46.1063 | 2024-10-28 14:35:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 2d10fc74-f8ff-3630-9c14-621e92f5481f | -2.8515 | -49.2408 | 2024-10-28 14:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| dc2e4bf9-4bc8-3e9c-8d72-a00e2cc92e54 | -3.0734 | -54.167 | 2024-10-28 14:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a4775056-6e6f-360b-8c6f-82212edf1f20 | -3.2065 | -44.386 | 2024-10-28 14:35:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 6bbd200a-8b1e-3994-9236-475fe2455d44 | -3.3704 | -41.621 | 2024-10-28 14:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 6c706cea-e198-3d64-bb71-d40575929c80 | -3.3891 | -41.6201 | 2024-10-28 14:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 122.8 |
| 76fa38e3-a049-375c-ae9f-ad9c06c6fb4b | -3.3352 | -44.6997 | 2024-10-28 14:35:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 316130fa-c9be-3c33-b4c0-068e060567eb | -3.5775 | -44.6436 | 2024-10-28 14:35:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| ff746d1c-664f-3311-9507-5b6aa1059092 | -3.614 | -44.7783 | 2024-10-28 14:35:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 383645cf-858e-3827-a76f-778a1633f225 | -3.9959 | -43.2651 | 2024-10-28 14:35:28 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e9553a75-aeb2-3f6a-8676-14cee30eca93 | -3.8412 | -44.1513 | 2024-10-28 14:35:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 90ada664-9866-387f-aad5-285a899c1a12 | -4.1639 | -43.2792 | 2024-10-28 14:35:29 | GOES-16 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 4a09a110-23e4-3dd1-8559-54bfc85b8700 | -4.4468 | -42.9123 | 2024-10-28 14:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| e26666ff-6b88-3e4a-af03-09c59764bae9 | -4.8619 | -42.4622 | 2024-10-28 14:35:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 6d9862d0-89b6-337c-bd2c-e57240a72c3d | -8.1756 | -43.719 | 2024-10-28 14:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 9cff8fb9-a54e-3d6b-8f12-c0cd487fd3ac | -13.2877 | -53.704 | 2024-10-28 14:36:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9039079b-7d6b-3ead-ac3a-13820448706d | -23.816 | -55.2713 | 2024-10-28 14:37:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 3ad71e7a-cb57-39a3-973c-4cda58573db1 | 3.4526 | -51.2595 | 2024-10-28 14:44:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7970f131-f2f5-3007-aa1e-741e45d2735e | -1.0243 | -48.83 | 2024-10-28 14:45:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| aec4eb5c-e1bd-3a8f-9f6d-b086053a4d10 | -1.0059 | -48.8302 | 2024-10-28 14:45:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d4558ea2-7d9e-3233-a25c-b928bbb65bd9 | -1.4116 | -49.0384 | 2024-10-28 14:45:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| d821773d-1a63-31b5-84e1-e13f11f72107 | -1.3743 | -49.273 | 2024-10-28 14:45:14 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| f3caa1bd-7d54-3a86-8877-bbce851b7fc9 | -1.4396 | -54.0966 | 2024-10-28 14:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| f347aa84-f695-3c04-ab72-d4143bff7eb2 | -1.4213 | -54.0767 | 2024-10-28 14:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| cfd19b78-bcf4-3666-ab18-ef146e56a592 | -1.4397 | -54.0765 | 2024-10-28 14:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 143.3 |
| c18b40c6-7a8f-398f-a1cf-e4ddfaf9094e | -1.8415 | -54.9901 | 2024-10-28 14:45:16 | GOES-16 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| a0eb57ea-9daa-3d6a-a3a8-f3bb24611c4b | -2.038 | -49.537 | 2024-10-28 14:45:17 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 849d61bf-98b6-367f-92fe-e07e898313c3 | -2.1125 | -49.2809 | 2024-10-28 14:45:18 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 91f94c67-898f-392b-a91e-bdebd6c83bc0 | -2.3578 | -47.6641 | 2024-10-28 14:45:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| de8d67cc-e302-352f-bca0-9871aae89afd | -2.2664 | -53.7221 | 2024-10-28 14:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| de6b3316-a901-381e-aad1-7ced95049b5c | -2.2348 | -45.6172 | 2024-10-28 14:45:19 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| f540479d-5808-36da-b789-c7723953724d | -2.4104 | -48.5265 | 2024-10-28 14:45:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 6b49ad8f-b6c7-30d0-9e5c-832274602ec0 | -3.0734 | -54.167 | 2024-10-28 14:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 824dfa44-c0e1-3679-808e-8c779dbf80c0 | -3.1281 | -54.266 | 2024-10-28 14:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1cd7467e-c256-3810-b285-73dd5e58783f | -3.3891 | -41.6201 | 2024-10-28 14:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 370205a8-d6f7-397c-a110-b4021570d100 | -3.5775 | -44.6436 | 2024-10-28 14:45:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 76df5495-b4c7-3932-9e28-7bab44331839 | -3.614 | -44.7783 | 2024-10-28 14:45:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| bb928cd1-a197-3483-b680-b51beec8818c | -3.7091 | -44.4324 | 2024-10-28 14:45:27 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0686ff53-8a6e-3404-860a-7a71ff903bf2 | -3.9961 | -43.2418 | 2024-10-28 14:45:28 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4d92b1d4-8bb2-3d48-9378-a05ee10c6027 | -3.9959 | -43.2651 | 2024-10-28 14:45:28 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| df89f725-6e7c-3c0f-99e9-7d8c71d4a9b4 | -4.3839 | -43.8923 | 2024-10-28 14:45:31 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 4c19e542-c400-3dcc-b412-c9b440c41330 | -4.384 | -43.8693 | 2024-10-28 14:45:31 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 18bb4b6c-8e75-382b-9506-af0a995bdaa0 | -4.4025 | -43.8913 | 2024-10-28 14:45:31 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f4f0ed27-adf1-3c88-a001-abba3bdf7d54 | -4.8619 | -42.4622 | 2024-10-28 14:45:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 159.9 |
| ceeed8fd-99f8-32bb-b4da-e94a57789090 | -4.9498 | -43.1845 | 2024-10-28 14:45:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| b17589fa-3cc0-3cdf-bca3-0c10f2b3b70d | -4.9496 | -43.2078 | 2024-10-28 14:45:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| eb7373e2-2189-38ce-aebc-1003b3c55cd4 | -5.9419 | -43.2754 | 2024-10-28 14:45:39 | GOES-16 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 5cb6a28a-14d4-359f-8fbe-9d63e618dceb | -6.7881 | -50.889 | 2024-10-28 14:45:45 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 54fd6e7f-6111-32f1-8c54-bbfd4b7ebbf7 | -7.41 | -44.7198 | 2024-10-28 14:45:48 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| fbaebbd9-f62a-3dc5-a695-76839860a66a | -7.8907 | -45.4256 | 2024-10-28 14:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 786f592f-e680-3cab-a3be-ba5e50dd7fd1 | -8.1759 | -43.6957 | 2024-10-28 14:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3f1de194-15d6-3a49-8dc8-9d12774279e3 | -9.4323 | -44.4803 | 2024-10-28 14:45:59 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 34d48b50-fe1e-3880-9d03-21c3c9040888 | -11.4193 | -45.1643 | 2024-10-28 14:46:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 1682b72c-1564-3884-9f89-561fe632a8b2 | -11.4197 | -45.1412 | 2024-10-28 14:46:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| da65571a-755e-3f9d-ba10-85b7d5af07ae | -13.2874 | -53.7248 | 2024-10-28 14:46:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 12700675-27ac-3b4c-b955-3554d9a06d32 | -13.2877 | -53.704 | 2024-10-28 14:46:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |


