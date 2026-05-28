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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0535d7eb-dc2b-3574-9b53-2115599cbbe7 | -9.3613 | -45.4744 | 2026-05-28 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| d82defb6-edcf-3396-a758-f0c8eea59312 | -11.591 | -47.4496 | 2026-05-28 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 92fabbb1-378a-343c-acb1-afd9addc7be2 | -11.591 | -47.4496 | 2026-05-28 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| f8a7a066-4549-34a4-8713-7a482415da1b | -13.2186 | -54.5182 | 2026-05-28 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f02118b4-0d73-385f-9a93-7eeb231092eb | -13.2189 | -54.4975 | 2026-05-28 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| d0123090-737f-30cb-935f-b13c89aec888 | -13.2186 | -54.5182 | 2026-05-28 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 9c5ddf9f-4973-33fe-bd63-19c84d22923f | -13.2189 | -54.4975 | 2026-05-28 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| eb2f8cf8-b013-3ecd-836b-684ab4ea9da8 | -11.591 | -47.4496 | 2026-05-28 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 75191420-ed64-3368-8ff8-f0d992b8025a | -13.1998 | -54.4996 | 2026-05-28 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 7cad2065-51ff-3681-9dbf-60a3f7ac89d2 | -13.1995 | -54.5202 | 2026-05-28 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7c515b9f-e3c2-3e2b-aaba-e34c9c4be908 | -11.591 | -47.4496 | 2026-05-28 02:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2fcd62b4-fbf0-37ac-896d-93ab8041e82b | -11.591 | -47.4496 | 2026-05-28 02:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| d735019e-3122-3825-8214-c5ffb51f855f | -11.591 | -47.4496 | 2026-05-28 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0e8f0316-3379-3ebc-bc5c-0c359419930b | -13.2189 | -54.4975 | 2026-05-28 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 082b4254-e8fb-3b7c-8cb8-f0a0b592bd98 | -11.591 | -47.4496 | 2026-05-28 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 645741fd-3e1c-3a59-8414-e67b025dd1a1 | -13.1995 | -54.5202 | 2026-05-28 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ed9df7ee-1ba9-3d7e-a80a-a14c81d324b6 | -13.2186 | -54.5182 | 2026-05-28 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 2462438c-f81c-3e49-bf5a-740a536b7ad6 | -13.1998 | -54.4996 | 2026-05-28 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| f8907511-5e52-3f99-a8b1-5376af03a8a4 | -11.591 | -47.4496 | 2026-05-28 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 11b15f62-ddce-332b-8891-d04c14915cfe | -13.2189 | -54.4975 | 2026-05-28 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| d185b57b-76ff-3236-bac1-c5a2b83c225a | -13.2186 | -54.5182 | 2026-05-28 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 00a34ba8-6bc7-3ab8-be5d-7daab247ed82 | -13.1995 | -54.5202 | 2026-05-28 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| fe5921da-42d9-3a74-bae3-e6b57b0e9088 | -13.1995 | -54.5202 | 2026-05-28 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| cf67dd51-fcfd-395d-9518-89153046b55f | -13.2189 | -54.4975 | 2026-05-28 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| ec715c3c-1f1b-3c75-a483-52085034bdac | -11.591 | -47.4496 | 2026-05-28 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1add47c0-98ab-3ee8-89b5-2f6d29ed6f0d | -13.2186 | -54.5182 | 2026-05-28 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 3933ab2c-cce9-39f3-a041-f1aaf4ed79e2 | -18.76134 | -40.99947 | 2026-05-28 03:02:00 | NOAA-21 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b22f6c22-4799-3cc8-94ae-2ace7b49d738 | -18.76221 | -40.99575 | 2026-05-28 03:02:00 | NOAA-21 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a9179efa-fa39-3e32-a985-4be0b3c3c9a0 | -13.1998 | -54.4996 | 2026-05-28 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1f321564-52ae-37f5-a165-7b7c3c5822cb | -11.591 | -47.4496 | 2026-05-28 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 0d678879-6052-3df5-a4f6-f9ba3f8b02a8 | -13.1995 | -54.5202 | 2026-05-28 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c4d71569-60c2-35c5-a950-6e0d8ff6d39d | -13.2189 | -54.4975 | 2026-05-28 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 76e4de38-86cf-315e-9154-03496d2c8e00 | -13.2186 | -54.5182 | 2026-05-28 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 338e24c1-4267-39b8-9b56-7cc315af2a0b | -13.2186 | -54.5182 | 2026-05-28 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| ac8a6647-8a9a-3e1e-aa43-dc8f48615ff3 | -13.2189 | -54.4975 | 2026-05-28 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 0efd7e30-edf9-3b16-8b59-843736156098 | -11.591 | -47.4496 | 2026-05-28 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 5f632173-6120-3b54-9e13-eba8b52ff71d | -13.2189 | -54.4975 | 2026-05-28 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 626a6769-d425-3b9e-9e8a-1b23269b1cb3 | -13.2186 | -54.5182 | 2026-05-28 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 01e2d12e-7d1e-371b-9cea-60f2223d79cd | -7.00105 | -42.88379 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0e3ff83d-70af-3ea6-a23f-1e54c3735b6b | -7.01036 | -44.99855 | 2026-05-28 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72af93ba-9ac2-358f-9b75-c0f30074bb72 | -2.96272 | -39.92327 | 2026-05-28 03:32:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 94d2c9e7-4ffe-33bb-acb7-1e6134667491 | -7.00205 | -42.87855 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0e9776a0-1a30-3e64-8336-309be845f18f | -6.99366 | -42.88765 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 7228aca4-eed3-3a5b-8700-bbe0269a27e4 | -7.00095 | -42.88211 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e9b007e1-5acd-3c7d-8098-28f459f1c853 | -2.96843 | -39.92426 | 2026-05-28 03:32:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f799657-f9f3-3bff-a7ef-ff9bb6645d92 | -6.99455 | -42.88071 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 7c42d731-660b-3187-8a84-90b66f6a08f3 | -7.00753 | -45.0134 | 2026-05-28 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 480a5d0e-fb07-35f9-ac0c-88b57e7c3556 | -5.95423 | -43.49625 | 2026-05-28 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dbd360fc-1052-3c7f-a84b-8420119272e1 | -5.96097 | -43.49777 | 2026-05-28 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 46add165-9e68-359e-93aa-b7865ba6e7ab | -6.99359 | -42.88594 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f19f9ab9-95d6-3d29-9326-839820a3d8e5 | -5.95449 | -43.49062 | 2026-05-28 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7fc5917c-e5bd-3be0-a3de-3d7f415aef44 | -7.47593 | -36.60742 | 2026-05-28 03:32:00 | NPP-375D | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e7b1b47-884a-332e-9ea9-6936224b7420 | -6.99551 | -42.87547 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b4dfa42f-65db-3929-9dcd-6ff7505e5bba | -6.99999 | -42.88736 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 29f0882e-4cfa-3f39-bb75-26dee1a871d1 | -5.96211 | -43.4916 | 2026-05-28 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5032c5d7-78d8-3974-a5dd-f82aa01a3927 | -6.99565 | -42.87718 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| f8af8d16-097b-38f9-a071-b81abbc2ef8b | -6.99465 | -42.88241 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 243ac7a1-6aa2-3561-8d9e-daa4322a03d1 | -7.00897 | -45.00588 | 2026-05-28 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7badd606-3768-3472-8226-66d220be6ceb | -5.95541 | -43.48995 | 2026-05-28 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 467dda03-b9b8-3f19-a878-0114e6441019 | -5.95335 | -43.49696 | 2026-05-28 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1accee68-e460-3209-956e-67ad7bf4ef38 | -7.00006 | -42.88903 | 2026-05-28 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 823416ca-d4d5-301b-93f0-41ba9c6a4485 | -12.69247 | -44.78859 | 2026-05-28 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b6df5f18-5ded-3a46-93fd-08603a0db71b | -7.00994 | -45.00561 | 2026-05-28 03:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c05558fe-6b30-3211-b8de-e0a195b83895 | -7.01138 | -44.99829 | 2026-05-28 03:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5fee408-7e8a-39bf-ba3a-44129e2adb35 | -9.36162 | -45.46469 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3d35eef-812e-32bd-9f51-187ffc55d79d | -9.49619 | -40.30636 | 2026-05-28 03:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7531a9ac-d868-3ed3-8d5a-a6b6c13f64bd | -9.36017 | -45.47167 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1bef7c7-4557-38b0-8634-0b514c135489 | -9.34266 | -45.47747 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a727b77e-6b07-35de-bfe9-d4ffedb3bd15 | -14.39763 | -43.52205 | 2026-05-28 03:34:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5888b563-5ed7-393d-9c33-0a10896782c4 | -9.13929 | -40.10818 | 2026-05-28 03:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ff76112e-d3e5-320d-84ec-eac7cf2e2d5e | -11.41526 | -37.81706 | 2026-05-28 03:34:00 | NPP-375D | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6bfe342c-0a09-32c2-9925-2c80cfffa26f | -9.13869 | -40.11142 | 2026-05-28 03:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| db12cf5d-8769-30fa-80b2-d734e4f0cedc | -9.49678 | -40.30312 | 2026-05-28 03:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 33cebecc-0bfc-36d2-8c2d-00184820eaf5 | -9.34439 | -45.47562 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7a2adc79-50f7-3598-82d9-cf64880d042c | -9.35124 | -45.47195 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| aa1184d7-6987-380d-934b-81969f8079aa | -10.84736 | -39.31458 | 2026-05-28 03:34:00 | NPP-375D | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d870e44-8cf2-3f37-b99a-c07f491b739e | -7.00847 | -45.01309 | 2026-05-28 03:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5dc7a7f0-e1b6-3cd6-9013-25f4456b28fa | -9.95665 | -37.40482 | 2026-05-28 03:34:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0f68898e-471b-350e-ad46-6aad41ec3e50 | -9.35981 | -45.46652 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1fa579bc-9bbf-3588-9032-eabc690c957f | -9.34586 | -45.46853 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aa7d7e2-6de7-3825-bd23-8410f08acbd1 | -9.35302 | -45.4701 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c179c509-82dd-3434-80aa-62e6b5f7270b | -9.34409 | -45.47037 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 948b3c8c-4082-3a8a-8213-38306db80860 | -9.35266 | -45.46489 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 43aa3e06-f779-3f63-b9aa-bb88c7d4e8aa | -9.35448 | -45.46306 | 2026-05-28 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50418719-cc32-3f8c-a776-964863ec9333 | -18.76065 | -40.99918 | 2026-05-28 03:36:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9da15a7a-fbe5-3637-bcb3-f31fea49d8e7 | -19.08949 | -40.08101 | 2026-05-28 03:36:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0c0085da-e1d8-3fa2-8c56-2ec38fd45716 | -21.42178 | -47.07336 | 2026-05-28 03:38:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b31ab820-564e-3863-aa31-805da0fe92e6 | -21.54242 | -47.04951 | 2026-05-28 03:38:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6ae3890-13ac-3266-8011-f04793dc201c | -21.42443 | -47.06235 | 2026-05-28 03:38:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 386df478-0d5d-364c-a211-e6e4aa12b842 | -21.30048 | -48.59208 | 2026-05-28 03:38:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bef8dabd-8f4f-348c-8361-1c4b6a538964 | -21.55034 | -48.8966 | 2026-05-28 03:38:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77c55fc3-30e1-3374-8362-065372ff8e32 | -21.54171 | -48.90145 | 2026-05-28 03:38:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c33bcd4b-bbfb-3295-a3a9-bedee1e2f462 | -21.42053 | -47.07856 | 2026-05-28 03:38:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d56d295f-7961-3a99-8ed5-b2091697db73 | -21.54374 | -47.04404 | 2026-05-28 03:38:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e023f00-f997-35cb-99c8-121a7a05373c | -21.30218 | -48.58546 | 2026-05-28 03:38:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a4f64ba1-3bda-3f4b-a3e2-43796217e706 | -21.4281 | -47.07497 | 2026-05-28 03:38:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e90b93a-25f8-331a-8b7c-da20b4a4d3ca | -13.2186 | -54.5182 | 2026-05-28 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| dae9221e-d673-3218-a71f-ea5786e8d563 | -11.591 | -47.4496 | 2026-05-28 03:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 393ae74d-52da-3703-93e7-2bf46526f72e | -13.2189 | -54.4975 | 2026-05-28 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| aeca7223-e4c8-30ea-a4ee-9628e89e4b68 | -2.96282 | -39.92326 | 2026-05-28 03:49:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
