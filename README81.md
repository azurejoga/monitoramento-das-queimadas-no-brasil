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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a91e458c-9440-3ef4-8d38-d7741878d5b6 | -12.29558 | -46.7263 | 2024-10-15 12:44:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6f074bb0-f7ed-3de4-9235-30d6d5cdab84 | -12.88445 | -46.92249 | 2024-10-15 12:44:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e5759651-db53-34de-9101-6af7e49d962c | -2.96509 | -46.95584 | 2024-10-15 12:44:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7e766d57-297e-3c2b-bed6-acfbc639c473 | -3.07327 | -44.0859 | 2024-10-15 12:44:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6a048e4e-fa80-38c4-a49b-f8bfe45d5bcf | -3.0747 | -44.07575 | 2024-10-15 12:44:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 00ce6441-6a9d-33d1-9db1-71799c2e946a | -3.35474 | -44.18478 | 2024-10-15 12:44:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| ed2e9f6e-2dae-3026-a099-a97275745aaf | -3.8934 | -44.55019 | 2024-10-15 12:44:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ceca2f73-bcd4-3915-97c7-5854a1718335 | -3.93828 | -46.41564 | 2024-10-15 12:44:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5afdc7ca-b096-381f-a43c-459c0386478b | -3.95345 | -46.43577 | 2024-10-15 12:44:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 42.5 |
| c414c619-6b5d-3050-9f47-3f1ac26f87d2 | -4.22115 | -45.53785 | 2024-10-15 12:44:00 | TERRA_M-T | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f1a7e52a-4679-37cd-86bc-a722f6119153 | -4.29447 | -44.32406 | 2024-10-15 12:44:00 | TERRA_M-T | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8a15da02-2718-37c9-8c79-87ecdb673e87 | -4.54196 | -46.57957 | 2024-10-15 12:44:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 7e726f20-ecf7-370a-be8d-084f8276bb51 | -13.92366 | -42.75005 | 2024-10-15 12:46:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 1356e45e-50af-315a-bef3-703255ec1732 | -14.84034 | -45.18298 | 2024-10-15 12:46:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f1c277fe-dd03-39d3-837e-088a935b7973 | -15.20788 | -42.46802 | 2024-10-15 12:46:00 | TERRA_M-T | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 3f762923-daa5-3387-baa2-faef105efc25 | -19.54518 | -56.97493 | 2024-10-15 12:46:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 6a8ce4a4-c3ee-31ee-a18c-b4a0f5f1a8ed | -19.55425 | -56.99915 | 2024-10-15 12:46:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 1f43c008-815c-3349-8c26-37019adafdf8 | -19.55509 | -56.9839 | 2024-10-15 12:46:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 1160a5ba-feb9-3c4f-837f-6729dbc9d31b | -19.55817 | -56.97758 | 2024-10-15 12:46:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| fa6efe5b-13ba-3e1c-880b-bd388d09658d | -19.6224 | -46.88988 | 2024-10-15 12:46:00 | TERRA_M-T | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 368c2a8d-2f12-3eca-a7d0-8a82e8ca1ae2 | -20.32123 | -44.35456 | 2024-10-15 12:46:00 | TERRA_M-T | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 35c010da-6e39-38cc-bdda-73cfa0f3caf9 | -20.32316 | -44.3364 | 2024-10-15 12:46:00 | TERRA_M-T | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 91bb9b23-714b-324b-84c5-0f4727115082 | -20.32767 | -44.34862 | 2024-10-15 12:46:00 | TERRA_M-T | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| 799ce3c3-a8b6-30dd-9afd-dea57a81d3a7 | -21.45016 | -43.84912 | 2024-10-15 12:46:00 | TERRA_M-T | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| cff29797-deaa-36c9-9ac0-1b5c66a38366 | -12.06774 | -54.75375 | 2024-10-15 12:46:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 39e020a1-ffc5-3958-8c9d-d44cd4a8eb4c | -12.384 | -53.12411 | 2024-10-15 12:46:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| fb03496e-d70b-3786-8397-675e70d18531 | -15.62821 | -59.96044 | 2024-10-15 12:46:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 271cf070-49b9-3e44-9b39-11cf20aec1ba | -16.92492 | -57.8404 | 2024-10-15 12:46:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 60395c26-1dbb-3c6d-ac50-01f9d3756a76 | -17.19808 | -56.68167 | 2024-10-15 12:46:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.6 |
| bd27759e-d24a-35b9-88c7-c1efc8b2830d | -10.2632 | -47.2802 | 2024-10-15 12:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 213.6 |
| fba79447-a2d5-342b-9a6c-0047f4699ece | -11.245 | -44.1924 | 2024-10-15 12:46:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 0d27015f-4177-369d-a850-f5b0ecedd94a | -11.2637 | -44.213 | 2024-10-15 12:46:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 5f0c9976-a6c6-3f0e-b1cc-eebb6600ce79 | -20.26036 | -55.42007 | 2024-10-15 12:49:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 01a73642-8ae3-356b-a62a-c8b6560c0bd5 | -21.96474 | -48.41886 | 2024-10-15 12:49:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 81568c64-5631-3f59-bd19-c7e6644fbccf | -21.96612 | -48.4083 | 2024-10-15 12:49:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1fe9b43f-12dc-3eef-95db-a510f1b2f008 | -23.70482 | -46.61129 | 2024-10-15 12:49:00 | TERRA_M-T | DIADEMA | SÃO PAULO | Brasil | 3513801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| beab6832-04f0-3a67-a89d-167001e864ec | -9.7191 | -46.9419 | 2024-10-15 12:56:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 60186467-eff2-3272-a153-a689dd99522a | -10.0443 | -44.1717 | 2024-10-15 12:56:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| a86e703b-75ac-3973-88ca-6f65684f7012 | -10.0439 | -44.195 | 2024-10-15 12:56:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 6e0a6523-b536-3c84-b62e-c44c6d2650d5 | -10.0629 | -44.1925 | 2024-10-15 12:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| c226e633-f25e-3c97-b5d5-749934c78253 | -10.0626 | -44.2158 | 2024-10-15 12:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ea21c9cd-7e9c-3bc9-a9de-9cd76a18a370 | -10.0355 | -47.3064 | 2024-10-15 12:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| ae822878-f2a7-3453-a904-bc4fe79e5df5 | -10.0816 | -44.2133 | 2024-10-15 12:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 05990ae1-d37f-3d32-8f54-a71ffdae96bb | -10.2632 | -47.2802 | 2024-10-15 12:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 226.3 |
| 8ad2b458-d849-32bb-86a9-9bc56170bc51 | -11.2637 | -44.213 | 2024-10-15 12:56:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 1bc20cec-f1d2-37b6-b553-a27de8a713cb | -11.2641 | -44.1896 | 2024-10-15 12:56:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1c25180c-151c-3dfa-a09c-158bf474cb9b | -11.245 | -44.1924 | 2024-10-15 12:56:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| a1f2e28d-c907-3c8b-8a38-756440711969 | -9.44 | -44.23 | 2024-10-15 13:04:30 | MSG-03 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d0f248ad-de23-3419-a969-f140e6169835 | -9.44 | -44.18 | 2024-10-15 13:04:30 | MSG-03 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e11c7bdf-95c1-3c30-9e70-2f7d10270d2b | -9.47 | -44.19 | 2024-10-15 13:04:30 | MSG-03 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 889ec0d8-64f1-3999-8837-d3b3b10c0f4d | -9.01 | -54.5042 | 2024-10-15 13:05:57 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 0f0f551b-74c3-3ede-86fa-ca1690230ad4 | -9.5185 | -47.8049 | 2024-10-15 13:06:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| e57d6f76-3193-3dca-a80b-51eca7e418ad | -9.7191 | -46.9419 | 2024-10-15 13:06:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 88463dca-cfe5-3947-b76f-62a7ad57b7df | -9.8883 | -47.0119 | 2024-10-15 13:06:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 52f08ca7-28d6-3612-9f47-d58e704af0e6 | -9.9781 | -47.3573 | 2024-10-15 13:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 79249ada-a0d6-32c4-bdd7-46f14e5b24de | -10.0352 | -47.3286 | 2024-10-15 13:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 9b608982-85f7-3f39-bce0-9c3fc568cec0 | -10.0536 | -47.3709 | 2024-10-15 13:06:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 66d22d96-d7b8-3d8f-9f9b-f12ca13abdaa | -10.0355 | -47.3064 | 2024-10-15 13:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 299a9283-9bde-3c9e-a2af-506a50cbfa0f | -10.2632 | -47.2802 | 2024-10-15 13:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 37c3bdc2-2b2a-3056-8038-452375d88f29 | -9.5185 | -47.8049 | 2024-10-15 13:16:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 5d369da3-f704-3648-8511-e88d90899017 | -9.5188 | -47.7828 | 2024-10-15 13:16:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| a1b8bc4f-fe9c-3887-8caa-17c6efc2341c | -9.7191 | -46.9419 | 2024-10-15 13:16:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b13341c3-227b-3fd7-8a56-e47dc6941519 | -9.9777 | -47.3795 | 2024-10-15 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| fc29dfad-479f-32ae-bdc3-12c64fe64466 | -9.9983 | -47.2662 | 2024-10-15 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 68ca7353-70f0-3cb9-b938-894f28635eff | -9.997 | -47.3551 | 2024-10-15 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| efa95368-9d4c-31d2-a136-2d7f5a5fd69b | -9.8883 | -47.0119 | 2024-10-15 13:16:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 675352af-0801-3a51-88bf-46be49bbefb5 | -9.9781 | -47.3573 | 2024-10-15 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 45b8c335-e2e9-3426-8f57-1e30d9474a32 | -10.0163 | -47.3308 | 2024-10-15 13:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 0db7b0a0-2d6f-3d90-8d4d-99c766d42cbe | -10.0166 | -47.3085 | 2024-10-15 13:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 9cfe62ed-13df-3eb7-b304-3c591db24152 | -10.0352 | -47.3286 | 2024-10-15 13:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 19503709-b830-3194-8364-c396590fc678 | -10.0536 | -47.3709 | 2024-10-15 13:16:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| a31bfb55-3969-3268-957a-64b0880b835a | -10.0355 | -47.3064 | 2024-10-15 13:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 10fc0d6f-e9d7-36d2-bcb2-74fe230aab81 | -10.2632 | -47.2802 | 2024-10-15 13:16:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 0be748e4-97a0-3ff5-890a-c876dfd88295 | -11.7753 | -44.5101 | 2024-10-15 13:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| fa4488ba-1081-3dac-9710-f1a219568a8b | -11.7946 | -44.5072 | 2024-10-15 13:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 43be9545-009a-3f14-ba1d-8c7c895b5415 | -12.3552 | -45.3255 | 2024-10-15 13:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 2cbb83c5-864f-309f-8f34-78456483c771 | -9.01 | -54.5042 | 2024-10-15 13:25:57 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 3d68e657-3a61-3026-9a42-b550c9084154 | -9.5185 | -47.8049 | 2024-10-15 13:26:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 999db64e-0869-3d98-9e95-a86d5db0cc6e | -9.5188 | -47.7828 | 2024-10-15 13:26:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 8a79a156-5212-32c6-becc-7d87db8ee7cc | -9.7191 | -46.9419 | 2024-10-15 13:26:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 90a6f971-13b3-333d-833b-f841f28d76de | -10.0439 | -44.195 | 2024-10-15 13:26:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 432a9437-de0d-34a9-971a-4f55e103dec7 | -9.888 | -47.0342 | 2024-10-15 13:26:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 0cccb614-bde9-3630-800a-708480c0d965 | -9.9781 | -47.3573 | 2024-10-15 13:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| faaf0434-fd47-339a-9ef2-e7c6a7c8aab2 | -9.8883 | -47.0119 | 2024-10-15 13:26:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 2296548c-9736-3a9a-890a-6eb0a8266f07 | -9.9793 | -47.2684 | 2024-10-15 13:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| b680c863-0f79-3e1a-8237-7d4aa6188a10 | -9.8694 | -47.0141 | 2024-10-15 13:26:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b8a0b448-c93e-33d0-961a-eb7c0b759c2c | -9.9777 | -47.3795 | 2024-10-15 13:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 5d4db1bf-b348-3c50-a087-d304971072e1 | -10.0443 | -44.1717 | 2024-10-15 13:26:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 628eb846-7fae-3088-ac51-5e85993f2add | -10.0536 | -47.3709 | 2024-10-15 13:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 2bd71425-eb0b-3355-95b0-b76b4a6ddc79 | -10.0166 | -47.3085 | 2024-10-15 13:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 0e8871d7-7b57-37e7-b793-190fdf60e27e | -10.0355 | -47.3064 | 2024-10-15 13:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 156.7 |
| f09096d3-36d0-394d-9f66-9465b693d057 | -10.0542 | -47.3264 | 2024-10-15 13:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 7a342b97-0ffe-3209-a977-eb21012ff13a | -10.0633 | -44.1692 | 2024-10-15 13:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| fb91283b-a4f1-3d83-bdab-69c60ae6180d | -10.0352 | -47.3286 | 2024-10-15 13:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 3687c359-774c-38cf-b801-56db126e770f | -10.0629 | -44.1925 | 2024-10-15 13:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| f825f793-8989-34b2-9f41-00460dd500e8 | -10.0551 | -47.2598 | 2024-10-15 13:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 3f037b00-b957-3c85-8fe6-9a9ddddec7f7 | -10.0548 | -47.282 | 2024-10-15 13:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| c398f458-9869-320c-8ecf-91f4d2e3496e | -10.0163 | -47.3308 | 2024-10-15 13:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 5ef77773-5402-373a-bc3a-770b978f6f1f | -10.0626 | -44.2158 | 2024-10-15 13:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| afa44e5c-8040-3d6d-9ff7-631d69a54435 | -10.0622 | -44.2391 | 2024-10-15 13:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |


[Clique aqui para ver as próximas entradas](README82.md)
