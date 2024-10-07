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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf242031-2758-3546-8009-b965166b1380 | -7.63328 | -42.51428 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cec0dfdc-2583-3459-8dcb-e014b25b4850 | -7.63271 | -42.51748 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 82ee1f4e-7aae-3061-a081-d6e39e5e1f4c | -7.63215 | -42.52068 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64bb82b4-a284-36fb-8d28-1ca405d0f1e5 | -7.62753 | -42.51648 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3697c44b-5839-3e42-a0ba-7bd476a71e44 | -7.62696 | -42.51968 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 83541149-1889-31a1-a1c7-9692c48b82a5 | -7.6264 | -42.52287 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 7bb2191f-c9ad-3949-9b20-b4e4eba5e25e | -7.62178 | -42.51867 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 933de3f3-723c-3ea6-a41c-684726d48f11 | -7.6166 | -42.51764 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 027ee9ca-cc2d-30fe-8143-513e5342be4b | -7.61604 | -42.52081 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 79639ab4-3925-34bc-9cb6-0c4cb171c905 | -8.2001 | -43.70322 | 2024-10-07 03:36:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7658eef-a160-3aa3-afcf-8ec41ddafef3 | -8.19944 | -43.70678 | 2024-10-07 03:36:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d407a70-8d65-31b4-b0e8-9017c9a1c592 | -8.19877 | -43.71035 | 2024-10-07 03:36:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05aa89a4-88f3-395e-804d-331136dc243e | -9.96028 | -44.10266 | 2024-10-07 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbf3d7c1-de06-3c73-a037-cde0fd022455 | -9.95931 | -44.10196 | 2024-10-07 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 455d380a-c376-3c46-8b14-d8f01db1ba5c | -9.95792 | -44.10923 | 2024-10-07 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27fdf162-9782-375a-af05-6926e837620f | -9.95477 | -44.10144 | 2024-10-07 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dec4afd1-8acd-30bd-9cd2-be6b5572727a | -9.95409 | -44.10513 | 2024-10-07 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ed33779-8cf5-303d-bb7f-eedd49efc463 | -9.95341 | -44.10883 | 2024-10-07 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 495105ac-47f5-3566-8117-4f50c3f560a0 | -9.9531 | -44.10443 | 2024-10-07 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a236937-203e-3e91-a401-17a0163abf7b | -9.95239 | -44.10814 | 2024-10-07 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a91dca9-c14f-31dd-8519-654ecebfb1c5 | -11.75334 | -44.4985 | 2024-10-07 03:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0940cef7-faa2-3c76-9f10-4254c3a697fb | -11.75263 | -44.50217 | 2024-10-07 03:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| aab861e7-7078-3dd0-a4b4-bfa6bc746a6c | -11.75121 | -44.50948 | 2024-10-07 03:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7efae361-cd0f-369d-b9c5-83b5c24cdfd6 | -11.74909 | -44.52046 | 2024-10-07 03:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fa1d0e4-183e-394a-9542-3cf19e931dd4 | -11.74784 | -44.49739 | 2024-10-07 03:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 32bea914-961f-3b75-834c-d7af42f502ec | -11.74713 | -44.50104 | 2024-10-07 03:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9c3c5cad-36a7-330b-8516-5dc0e3133e72 | -11.74572 | -44.50836 | 2024-10-07 03:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 637c1a1b-4321-3fde-873a-0ee41e8c7dce | -11.74093 | -44.50358 | 2024-10-07 03:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faa45302-129d-3898-9dd2-b76875d9e971 | -7.24345 | -44.94032 | 2024-10-07 03:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4638277a-b780-3d2a-b9d0-af380d83f2d0 | -7.23777 | -44.9375 | 2024-10-07 03:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7166cb4-47f8-32e3-b9c3-efa481c986b5 | -7.23734 | -44.93921 | 2024-10-07 03:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0492972-6541-357d-8e7a-4ec258b97b73 | -7.23692 | -44.94225 | 2024-10-07 03:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f747602-4251-38e9-8688-90088a45c00c | -10.29394 | -45.4362 | 2024-10-07 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b3c5234-4b96-33b5-8d7b-6029b08721ed | -10.28257 | -45.43076 | 2024-10-07 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56fef803-aa63-39eb-9f02-39a267dfe6c0 | -10.27641 | -45.43053 | 2024-10-07 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db61c718-ef8b-36ec-8435-a033e74efc91 | -10.27507 | -45.50164 | 2024-10-07 03:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70978f14-8caf-3891-bdc6-c889984059a2 | -10.27221 | -45.48421 | 2024-10-07 03:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 693fab30-9978-36d0-94ee-a3763c72256f | -10.26986 | -45.49632 | 2024-10-07 03:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d00b43bb-f705-3bcb-8651-97a9cbde2a1e | -10.26902 | -45.50062 | 2024-10-07 03:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 986d60e2-cdad-3e3c-9f05-cada883ddf8b | -10.26818 | -45.50498 | 2024-10-07 03:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d5e67b95-4594-3535-a7a7-a9ef8e136893 | -10.2668 | -45.47999 | 2024-10-07 03:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d2a34fd-73fa-3f49-a774-5a6a86758575 | -10.05603 | -45.30064 | 2024-10-07 03:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a35dc1a-8454-3252-92ed-ab91d9e86130 | -10.05447 | -45.29866 | 2024-10-07 03:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 969ec47b-6ab2-393d-9c03-12fe459e1c86 | -10.05358 | -45.30335 | 2024-10-07 03:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25a7950c-3a33-3dac-9a24-9713c4ed08fb | -9.47893 | -47.59394 | 2024-10-07 03:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2cd3772-973d-3329-9566-0032ddda52cf | -9.47204 | -47.59255 | 2024-10-07 03:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e76648b5-13db-35f8-8171-ed7950597ae1 | -11.63676 | -48.44516 | 2024-10-07 03:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a39d290b-c809-3494-9dc3-5006760a1b35 | -11.63531 | -48.45192 | 2024-10-07 03:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc9260a0-8e1e-3b32-9306-75379eba59ea | -11.63119 | -48.44685 | 2024-10-07 03:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 37f35d92-7dab-37b1-ac0a-959272063300 | -10.8754 | -63.9169 | 2024-10-07 03:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 550ec4a5-4849-30f9-a2a8-a20642653899 | -10.8755 | -63.8979 | 2024-10-07 03:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 51c82072-1234-3a6a-966b-f1da169dd5ae | -11.7566 | -44.4897 | 2024-10-07 03:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 669f13c0-3740-3443-aba2-a98c46a56391 | -12.1274 | -50.9118 | 2024-10-07 03:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 09a54b9e-4116-3179-8cb0-463786e2a7b3 | -12.1277 | -50.8904 | 2024-10-07 03:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 5c313754-236a-33a9-845a-631f11bd7538 | -12.1468 | -50.8882 | 2024-10-07 03:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| fce0e036-bb79-3ffe-afee-6e131421956d | -12.1899 | -50.5623 | 2024-10-07 03:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 79c41e24-f91c-333e-9707-3664b272fdcc | -12.1902 | -50.5409 | 2024-10-07 03:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 08ba6ff2-4514-387d-bcf5-4a2716c944ba | -12.209 | -50.5601 | 2024-10-07 03:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b22d49d6-7178-3d59-b6bc-b304a7f47764 | -12.2093 | -50.5386 | 2024-10-07 03:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0f35e87e-d9d3-3889-a84f-da8e4c4d3b3f | -13.7342 | -60.6471 | 2024-10-07 03:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b46d55af-865f-36cc-b1ae-231bbdcbe1ca | -16.527 | -57.7161 | 2024-10-07 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| e2a665fc-635d-3cdf-9806-712ad86f3358 | -16.5267 | -57.7365 | 2024-10-07 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 7f3fe476-f0d7-37dc-bcd9-41908886edd2 | -16.5075 | -57.7183 | 2024-10-07 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 136a28ae-0cbe-366b-a157-25327d36c44d | -16.4161 | -57.3211 | 2024-10-07 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| a7ce8172-f660-36db-9301-cada934cd0f5 | -16.4164 | -57.3006 | 2024-10-07 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 20f7f173-f0d6-3e56-a12f-fb831e37d093 | -16.4362 | -57.278 | 2024-10-07 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 59ebacfe-972f-3cb8-82ad-2618af90a58d | -16.4365 | -57.2575 | 2024-10-07 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| da04afa0-3a58-37de-adc2-13b5e7f4d250 | -16.4877 | -57.7408 | 2024-10-07 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| f996e85c-65ce-33cf-87c6-1b920877cb8b | -16.5072 | -57.7387 | 2024-10-07 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.7 |
| 01d2de4c-27c0-3c29-82b6-13e97625e052 | -17.0881 | -56.8328 | 2024-10-07 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| b6f15f6c-3573-3133-b6f3-e994453aa390 | -17.0319 | -56.6749 | 2024-10-07 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 430a408e-93a6-390b-9b17-5d68a75cfbfd | -17.0123 | -56.6773 | 2024-10-07 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 62cbe158-6866-36da-a697-15da4e9bee1e | -17.1278 | -56.8074 | 2024-10-07 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.0 |
| 6d600ee7-b540-3d29-9a88-3e43d0e15469 | -17.1274 | -56.828 | 2024-10-07 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.4 |
| ef4a9c1a-0b06-3b6a-943e-d5bebfb97a64 | -17.1081 | -56.8098 | 2024-10-07 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.6 |
| dbdf83f4-6f4e-3bc8-b524-76d7f5bf7fee | -17.1078 | -56.8304 | 2024-10-07 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| 80396baa-9937-3935-b5ad-720ab35f9053 | -17.012 | -56.698 | 2024-10-07 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 0978aedc-fe01-3760-a1a2-d98c0daf16bc | -17.1584 | -57.3377 | 2024-10-07 03:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 1cc529f3-9427-37a5-b757-6b378fa591ab | -17.1581 | -57.3582 | 2024-10-07 03:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| ad428a1d-83c3-3b6f-aaff-639baa010731 | -17.1777 | -57.3559 | 2024-10-07 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| b7ddb1ac-4cbb-3737-b446-e99337e07164 | -18.4718 | -53.5134 | 2024-10-07 03:36:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c53c7755-e43d-39c8-87df-4f04b20e8a4f | -18.7379 | -57.2864 | 2024-10-07 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 91d3f5ef-9a00-3459-92b5-e41c16e38331 | -18.6391 | -57.2578 | 2024-10-07 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| bb64f4cf-7b89-3859-9ce4-6494a41d7ede | -18.659 | -57.2552 | 2024-10-07 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.6 |
| ee3c9726-ec10-3b90-b2c5-8743450cdee9 | -18.7176 | -57.3097 | 2024-10-07 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| b19ba9b7-358c-30fc-8842-89266551c5af | -18.718 | -57.289 | 2024-10-07 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| d254a93f-d867-3c16-9ef6-e9a8c56ca3b6 | -18.7375 | -57.3071 | 2024-10-07 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 7284c4be-dbbd-322f-aa6b-d05dc93176ee | -20.4443 | -47.7109 | 2024-10-07 03:36:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 250.9 |
| 67336bf5-645a-39d8-b424-6aa99d59cb33 | -20.4449 | -47.6875 | 2024-10-07 03:36:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 347.8 |
| d4a6fc86-3b42-3887-8476-78ecd61556e4 | -20.4456 | -47.664 | 2024-10-07 03:36:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 574b726a-794b-3073-981d-ca70185a793f | -20.4648 | -47.7062 | 2024-10-07 03:36:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 9df68405-e7c9-38a9-a102-084b1aa5a22a | -20.4655 | -47.6827 | 2024-10-07 03:36:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 245.3 |
| 7c7541e2-aede-31d8-833f-edabf83b3b8c | -20.4661 | -47.6592 | 2024-10-07 03:36:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 114.0 |
| bad63525-8b6c-35ee-9a2f-4146cd35252c | -20.5848 | -48.5137 | 2024-10-07 03:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 78c3ac7a-5cb2-343e-8a6f-af41ddf7303b | -20.5855 | -48.4904 | 2024-10-07 03:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 181.5 |
| bca01f7e-95ab-3c70-8994-da51e5ebf1ef | -20.6053 | -48.509 | 2024-10-07 03:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 02ce9c78-76e0-3adb-9798-077e7251ad2c | -20.606 | -48.4858 | 2024-10-07 03:37:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 343.6 |
| 16835441-5395-32af-82b6-13ad5cde3adc | -20.7621 | -49.4841 | 2024-10-07 03:37:01 | GOES-16 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 144.3 |
| b483f20f-71a6-31d1-bf62-2414842ded9c | -20.7627 | -49.4611 | 2024-10-07 03:37:01 | GOES-16 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fd1af27d-2168-3827-a32a-d2ef6bd466d0 | -21.3274 | -47.5939 | 2024-10-07 03:37:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 80.4 |


[Clique aqui para ver as próximas entradas](README44.md)
