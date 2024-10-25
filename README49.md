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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9123ec1-9363-3573-83d1-d8c0635a68c1 | -7.27206 | -43.63648 | 2024-10-25 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83dad056-3eff-3e8a-a76e-3b436544c75f | -6.95108 | -42.48019 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 21079aa9-6404-3892-9d19-2bb364a3bf68 | -6.85249 | -42.81694 | 2024-10-25 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d65524b2-3fab-3847-a3e9-a454fc858fe8 | -6.85176 | -42.81483 | 2024-10-25 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f0dc9d16-cb0c-3cc0-9b16-f95341fcb27a | -6.58917 | -42.24616 | 2024-10-25 04:38:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 33263c04-afeb-3ac4-af8a-3f09e60b2aba | -9.35212 | -43.37223 | 2024-10-25 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 13f5a6b6-86be-3184-b282-0cc80d1811c6 | -9.35188 | -43.36573 | 2024-10-25 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95bc5ae8-3f89-394e-b241-8e0691bc02a3 | -9.35574 | -43.37093 | 2024-10-25 04:38:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc22e843-58b4-360b-b2c6-5007af7d1461 | -9.35124 | -43.37029 | 2024-10-25 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c9807cc5-b9a7-3243-9835-e749c65310bc | -9.11114 | -43.19169 | 2024-10-25 04:38:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ab8d13af-4499-377a-9d03-161d200b046c | -9.34544 | -43.37873 | 2024-10-25 04:38:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce229d8b-feb5-348f-9978-1ddf4a1bd9c5 | -10.76291 | -44.26449 | 2024-10-25 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d7713cb-5448-3ee3-9e5b-845b2421d173 | -10.58487 | -44.28669 | 2024-10-25 04:38:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a62a00ea-907e-3d1f-ba28-6141acedd496 | -10.58429 | -44.29082 | 2024-10-25 04:38:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88c2386a-011e-3378-bdb1-c49ada9a7fec | -10.58114 | -44.2819 | 2024-10-25 04:38:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b761208-5959-3534-9ba7-f8e54b06573b | -10.58056 | -44.28609 | 2024-10-25 04:38:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81f01e75-d55d-3647-8140-76aa2ba5fe2f | -10.4752 | -44.21078 | 2024-10-25 04:38:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6aa8cf79-f85f-3823-ac2b-ddc5e7615d80 | -10.76781 | -44.26086 | 2024-10-25 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8f08923-ce9e-37df-bd76-93965677e7ef | -10.76724 | -44.26506 | 2024-10-25 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65525474-28c9-3041-82fb-0eecfe889545 | -3.42171 | -43.16551 | 2024-10-25 04:38:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba3d773c-cc49-3215-b814-9415945d4126 | -5.0784 | -43.82693 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efcf1200-52fa-3f28-9e04-5c164e087e2e | -5.07784 | -43.83059 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec48be16-253a-3200-b82c-6636a9a24cb2 | -5.07429 | -43.82635 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75316ef0-e4f8-3e55-b1a7-544734e16004 | -5.07374 | -43.83 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52d8f79d-b139-3265-8ab6-9929edd47fa2 | -4.36356 | -43.89621 | 2024-10-25 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ad05783-901d-3be0-bf91-9d536dae46c6 | -3.80409 | -43.25876 | 2024-10-25 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ef4d07a5-e084-35a3-82f9-9b26d6fd60f4 | -3.79991 | -43.25811 | 2024-10-25 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 122b98b6-dfdd-3a3c-9764-e845ad35e7b2 | -5.91326 | -43.94872 | 2024-10-25 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc4d10d2-258e-3022-8829-ee0a9fa09bec | -5.82882 | -43.65162 | 2024-10-25 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72670437-9bf0-3fdf-ae89-05d98457d79c | -5.82825 | -43.65545 | 2024-10-25 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| acd4f8e7-afa4-33dc-9ec7-c961c80e7e5b | -5.72369 | -43.77643 | 2024-10-25 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1e37165-9710-3cac-9882-a93bb63039f4 | -5.72314 | -43.78011 | 2024-10-25 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9d9c79a-186c-3c4f-be82-fa1c236da96b | -5.72251 | -43.84081 | 2024-10-25 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0557c4c1-d46b-35e3-b163-c457a074d705 | -5.71954 | -43.77583 | 2024-10-25 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a174327-1c76-3889-83f9-729e3dfc4051 | -5.71899 | -43.77952 | 2024-10-25 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9738d0de-72b4-3a59-94c6-c83e18296a17 | -5.71892 | -43.83653 | 2024-10-25 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae2fb059-22d5-31d9-8537-7f079237ec9d | -5.71837 | -43.84021 | 2024-10-25 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b317b1bf-52f7-32a7-85a2-eada57aac0db | -5.48709 | -43.66233 | 2024-10-25 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c54bb2b-70a1-36c8-b09c-040505ede317 | -6.33648 | -44.80037 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bbe88dc-44c3-31f1-9582-82d9c7869d8d | -6.33254 | -44.7999 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45979c93-ad69-301c-838f-75a376eda90c | -6.28919 | -44.7679 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52d83d8a-195f-36d1-bb2f-106d2c79f88d | -6.25264 | -44.13963 | 2024-10-25 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b78e4d09-30ce-319b-af2b-a48e0551b8bb | -6.19431 | -44.54092 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 423ebd46-3e40-389b-9d19-eb4f96013562 | -6.19357 | -44.54602 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfba4a9d-44de-3165-ad98-28f7b728feda | -6.19261 | -44.52468 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7daab47-bd83-3f1a-875a-b8160556ef5d | -6.18961 | -44.54528 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0b4913f-4bc4-3fa6-85e4-98ef85f890a6 | -6.18736 | -44.52139 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33d3a7ba-dd30-34b0-8998-7f0df64326a8 | -6.18465 | -44.52344 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ec5f5f7-af61-362f-aca1-936c8d59f914 | -6.07082 | -44.62308 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 252f3e92-13a6-3839-8d3b-78e24011c086 | -5.89269 | -44.64452 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa54affe-e056-33bd-823b-fea0076a34ff | -5.89193 | -44.64959 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c17c2ffa-d748-3390-a7f8-0d593ee428b6 | -5.88875 | -44.64392 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e4f204a-56a9-31ee-aafa-802e921c81f2 | -5.888 | -44.64901 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcfd9053-a7f2-3c86-b8d7-a7a4143c2c42 | -5.88407 | -44.64842 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a115577-7f17-3d0a-93cf-bcf2cae2a133 | -5.8205 | -44.88926 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ed7f51a-ac01-3ee3-89e4-20bbaa65354d | -5.81546 | -44.49228 | 2024-10-25 04:38:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5837aea4-af99-3ff6-b47d-773902ecf202 | -5.8115 | -44.49165 | 2024-10-25 04:38:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6d60093-8574-3190-abef-0768f0440976 | -5.81075 | -44.49667 | 2024-10-25 04:38:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e06b1bf-dfce-3a84-b2d5-661aca727503 | -5.70794 | -44.65296 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d253c47-0804-3ea1-94ae-8ebb5105baf4 | -5.62619 | -44.82584 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6d135f1d-e4d3-376c-abf3-1c15d53ec899 | -5.62548 | -44.83064 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2a20f692-adfe-3679-90f5-863068fbb3e2 | -5.62233 | -44.82519 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a9c08cf-2cb4-323a-8d7c-7464400d8b2e | -5.62161 | -44.83 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dac478d-a460-399d-9742-a23c8d4dfa38 | -5.61845 | -44.8246 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c57fc13-e947-3f19-bf55-2bf5bbaf2d06 | -5.57639 | -44.88535 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 32147442-6755-392a-aeb5-169d6d849b6b | -5.57567 | -44.89007 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f5877fe-0d27-32fa-bdd4-694c0619387b | -5.57253 | -44.88478 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 87595883-2adf-3370-9bdf-cb241feb80c8 | -5.56867 | -44.88416 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1227723f-7a6f-3146-9407-b0e348d86ff3 | -5.5109 | -44.82134 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5f6d380-7c79-3674-a919-99b20e9e715e | -5.5102 | -44.8261 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a89b9ce1-6918-31ed-894e-35c4d470d631 | -5.50703 | -44.82073 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64d48774-aee1-3a11-92d5-894816809303 | -5.50633 | -44.8255 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1391e196-bced-3622-ad87-e4788000d0bc | -5.50562 | -44.83028 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62c357f9-8413-3254-b66b-e78b9767dca0 | -5.50246 | -44.82491 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ee4a600-971a-3ae1-ac31-946f93ddc518 | -6.45926 | -44.67219 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f1f15297-12c4-386c-b3ee-fb981dfa93b6 | -6.45849 | -44.67735 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d16f693-d359-36ba-9bce-30af19b8c188 | -6.45774 | -44.68234 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 760c8566-8dc9-36a0-99fe-2b88c25caef0 | -6.45567 | -44.42194 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67f9be8c-902e-3ed3-b856-0e0726c641ea | -6.45455 | -44.67667 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32dc7925-7496-37a1-af8c-8daba84c5630 | -6.45379 | -44.6817 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 516e02f2-92ab-34b0-9ab9-5d7f87d19b8b | -5.11266 | -43.84277 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a114ede-e444-3715-906a-e04d55bb7ae0 | -5.3275 | -44.84357 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e10b7c26-a33e-3d39-9fa3-e5bc6510d875 | -5.28296 | -44.74098 | 2024-10-25 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f08f8f00-834f-37d4-aacc-154a47898c18 | -5.218 | -44.45394 | 2024-10-25 04:38:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af2ddb78-efcc-3aae-a698-775892985118 | -5.21512 | -44.45177 | 2024-10-25 04:38:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9716f7b-e02e-3fb0-b26e-325348ca808e | -5.21405 | -44.45335 | 2024-10-25 04:38:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a67fd230-b64a-3808-b2a5-2c90906adb85 | -5.21104 | -44.23777 | 2024-10-25 04:38:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25f282e5-8ef5-340e-84bc-078f6d1f1777 | -5.06048 | -44.76433 | 2024-10-25 04:38:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e817c5a2-e278-3c46-8aee-065f3a688d58 | -5.05986 | -44.76237 | 2024-10-25 04:38:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea443867-6c18-3b6c-abc6-ee99845563b0 | -5.05661 | -44.76376 | 2024-10-25 04:38:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44ea3afc-282b-3392-b519-55402adb21cd | -5.05599 | -44.76184 | 2024-10-25 04:38:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ae1aad2-c589-3701-b16a-8dcdc0ab3d80 | -7.77655 | -45.15284 | 2024-10-25 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06816956-7038-3247-ab57-6c9ab1ff48e7 | -7.19602 | -44.73623 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d10cd03-7794-3017-9702-41bbd66e0f51 | -7.19526 | -44.74137 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 000eafa2-35bb-3caf-a62c-8836c9dea3bc | -7.19438 | -44.71981 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3769b73-8baa-317e-8dd6-dfd4faf420b8 | -7.19204 | -44.73559 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8832c560-28c1-38b2-9070-b090acb2f2f7 | -7.17737 | -44.99625 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8983445a-dd3f-34d8-96bf-086c076077f2 | -7.17717 | -44.99277 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5576fa7-aa8b-341f-a409-83b1178a5688 | -7.17646 | -44.99768 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af5d5a57-c978-31df-8300-5c24ad152b15 | -7.14374 | -44.84323 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README50.md)
