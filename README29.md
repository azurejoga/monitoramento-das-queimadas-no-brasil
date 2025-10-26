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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7283076-f86c-3b0b-8713-8dfb56db3bd5 | -17.42825 | -46.88111 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1c7a8b3-1135-3085-bd24-06b8701e2902 | -15.82392 | -53.58604 | 2025-10-26 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6201db9b-9584-33e0-9d64-108485ebd6f1 | -15.83006 | -53.58682 | 2025-10-26 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05113427-ca32-3118-b9db-dc648e7b5047 | -17.42352 | -46.8853 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c16f1544-efb3-3ec4-8df2-6db2dc31a48c | -21.75863 | -50.04618 | 2025-10-26 04:04:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 1b62f72c-351c-33cb-81bc-403cbb282e25 | -21.76326 | -50.04008 | 2025-10-26 04:04:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| ead48052-26ce-3a7f-ad94-875f11e56ebf | -23.23477 | -50.79109 | 2025-10-26 04:04:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2d8179ca-25fb-3e5c-bf7f-310845a4fd8c | -17.41955 | -46.73093 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe4efb70-e346-31d2-b349-7fe2702c63eb | -17.37432 | -52.02113 | 2025-10-26 04:04:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6ffdf3e-53c5-343e-a194-f64ff14f26b5 | -17.37672 | -45.51092 | 2025-10-26 04:04:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 865666c0-bf47-31ca-90ae-2314efcad093 | -20.32264 | -46.53922 | 2025-10-26 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f09e655f-4f3b-3d5c-9c8c-c497dc8c9a28 | -23.21586 | -46.91307 | 2025-10-26 04:04:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d092f28c-b5ee-3117-912a-24c8b61f51c4 | -20.32186 | -46.54364 | 2025-10-26 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d63d73c-f80a-3858-aba2-f1b6bdd0cfe5 | -17.38031 | -45.51152 | 2025-10-26 04:04:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3de20dc9-e35b-3deb-acf7-ceff58456cdc | -17.71204 | -43.91673 | 2025-10-26 04:04:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e6e3c3e1-2fcf-3951-aad9-4f4fd223d2a1 | -19.34966 | -45.59634 | 2025-10-26 04:04:00 | NOAA-20 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06951dc2-1ff1-397e-80d3-700f12dcc03b | -18.66089 | -52.0887 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82a0203c-7bb9-3a82-b076-9b1672a671dc | -19.92265 | -44.81636 | 2025-10-26 04:04:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4fea275-fb76-3fb6-ae8a-c8ecbe654802 | -17.84632 | -49.42229 | 2025-10-26 04:04:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 570c146c-e845-3298-bdaa-cc95d46f5ecd | -21.92546 | -46.51641 | 2025-10-26 04:04:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8bc920c7-adb3-3343-9b09-93d79c8f73bb | -23.26621 | -46.39684 | 2025-10-26 04:04:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 69decd54-53af-3ec4-a3fa-526d3f46bf4c | -21.87317 | -42.10231 | 2025-10-26 04:04:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4517a893-95e0-38f8-bfec-9df07b108ba8 | -16.31302 | -50.05384 | 2025-10-26 04:04:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd48b515-1258-368b-a401-f922bcd781a8 | -17.00788 | -55.91107 | 2025-10-26 04:04:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 86e634fa-1b89-3cd6-83f8-d4000a6b242d | -17.32967 | -43.65765 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b79b2531-6693-3e55-85ae-67097d6b59f0 | -17.3196 | -43.65591 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 44abec94-20bf-30ea-91a0-e6de312afeb7 | -17.32907 | -43.66135 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 220db323-862c-3f6a-ad02-02401b144b69 | -17.85235 | -44.11113 | 2025-10-26 04:04:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c88de157-b7f8-3860-918d-5f97c010f038 | -21.76238 | -50.04459 | 2025-10-26 04:04:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 7f80b0af-5c71-3b04-af0f-e7c71ed82907 | -19.68283 | -41.98906 | 2025-10-26 04:04:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 762d40b8-5633-3d90-9404-a101d4014f88 | -21.76151 | -50.04903 | 2025-10-26 04:04:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| d763282b-efc7-3455-947c-e3862bab79a0 | -18.64907 | -52.09308 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f64cdb2-566f-36ab-ba0b-f61b94e746b8 | -18.66161 | -52.08527 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1026dd23-ecf3-3c41-9ffb-0b2fa94fd86e | -17.05587 | -51.53535 | 2025-10-26 04:04:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d160d3a-6bc7-3a17-84df-1cdfc382fe5f | -18.19684 | -42.16546 | 2025-10-26 04:04:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dba935dd-aedb-3e3c-8992-30746774357d | -18.46144 | -47.17389 | 2025-10-26 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ac8fc3e-57b9-39f7-b764-235095814a05 | -17.41194 | -46.72942 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fdcf47c-0d53-3318-84c3-a0a09fdf90aa | -21.45251 | -44.84866 | 2025-10-26 04:04:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1ef0d294-6036-36aa-9e21-d31ef48188ac | -18.04957 | -44.40123 | 2025-10-26 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04bd10c4-b5c6-3747-b61e-2be9eaab9e03 | -17.32082 | -43.60636 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ade2f916-0b5a-3a01-bb8c-045be21fefba | -17.32632 | -43.65707 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6ce0189-7b76-3b0e-bd25-c93626c97d09 | -17.38312 | -45.51656 | 2025-10-26 04:04:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7052b1ec-cb94-367c-b8b2-d07b4f41ae5a | -18.20015 | -42.16604 | 2025-10-26 04:04:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7f84b285-6eb4-3a17-b65d-1741d2bdb425 | -21.75954 | -50.04171 | 2025-10-26 04:04:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| b4ed49f1-aeb4-3f31-816f-3cf10ab63d6a | -22.77205 | -43.39272 | 2025-10-26 04:04:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cfad5c9a-dfaa-34a2-ace9-600b352db45a | -17.319 | -43.65962 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d8716fd3-00b4-3641-a9cd-e0133727bb1f | -19.49253 | -44.27814 | 2025-10-26 04:04:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f616b4ff-ee5c-3554-8ab8-3936dec6df4a | -21.76205 | -50.05156 | 2025-10-26 04:04:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 7d62aef1-0f97-37ee-9ee9-1a0bd920898a | -18.4748 | -47.16597 | 2025-10-26 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a675e79-bd8a-3be1-b363-688854eea028 | -20.34174 | -41.74137 | 2025-10-26 04:04:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 48d16477-4709-315d-bcc7-e3ff1b69830e | -16.60505 | -49.36871 | 2025-10-26 04:04:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eae6403c-9b3a-3220-ad02-667bc03446f4 | -18.62504 | -44.94825 | 2025-10-26 04:04:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 013942e1-9da9-3077-a1bf-7718ab6b7c09 | -17.32296 | -43.65649 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d2616bc4-0572-37aa-8af3-0943eda8fd0c | -21.43445 | -49.59218 | 2025-10-26 04:04:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 39993216-6bde-3949-9c60-0e4ff7433c80 | -19.72247 | -42.13227 | 2025-10-26 04:04:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b2b78c3f-6660-3645-8b34-8c0af2cdcd19 | -23.22947 | -50.7946 | 2025-10-26 04:04:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6225ce60-97f0-3d7b-953b-20ba736ba959 | -17.05214 | -51.52711 | 2025-10-26 04:04:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 117b575d-b021-3e77-994b-1cabebe607df | -17.31564 | -43.65905 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e187ef1-63eb-3669-8f0f-323c4ee48dd0 | -17.31807 | -43.64423 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b31c684-0f24-3b79-b9a5-b24bd8fc1556 | -18.64762 | -52.09994 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51c3c659-7865-3a25-8f74-356e10a74a07 | -17.32021 | -43.61007 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f13d9b3d-44b8-377a-9bdf-e159c02e158c | -17.32478 | -43.64541 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e841467-396b-37ae-85a4-6ff821b42951 | -17.21333 | -47.65537 | 2025-10-26 04:04:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f4be82b-eba9-34cb-85dc-5081e421ab53 | -17.43591 | -46.88272 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b054751-001b-3fbb-8a7e-f46136788654 | -17.31746 | -43.64793 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81dd4269-157c-32a3-8849-25660080f694 | -18.65945 | -52.09553 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b98cbec-a17b-3148-b449-a464b514eed4 | -17.42738 | -46.88594 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b272255c-81ef-372a-8909-700db5a583c8 | -18.64835 | -52.09649 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93e61a97-8d89-3ba9-ad66-cbe8345ed89d | -18.47677 | -44.43039 | 2025-10-26 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e35d9252-4dd4-3219-8f1e-80175d16f8fd | -18.48017 | -44.43099 | 2025-10-26 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 181d8a25-3fa1-3974-a116-91a720a0ffbe | -17.32692 | -43.65337 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 748f9884-d1b4-37f6-8ce3-0f32a7dc9dde | -17.20931 | -47.6545 | 2025-10-26 04:04:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e7d49e1-9d60-341f-99ec-8322e36b133e | -23.04445 | -46.62544 | 2025-10-26 04:04:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f24bfd44-6a60-3b23-88a0-e801a0d0353c | -23.02276 | -46.23341 | 2025-10-26 04:04:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8339d5ee-b40b-306b-ad84-72ca9ed278ae | -17.42527 | -46.87555 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65163ee3-3422-30af-9d3e-8d3f69776487 | -18.14314 | -44.22205 | 2025-10-26 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d68ab801-cbb2-32b6-929c-ce0f792344ba | -19.40371 | -45.86969 | 2025-10-26 04:04:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 444e564c-6ce9-3b88-9393-5752a1ca2ba5 | -17.8482 | -49.42461 | 2025-10-26 04:04:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ece060ea-390c-3d75-84dc-68bbca1cbd58 | -17.42141 | -46.87488 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86b5e84a-5cb3-3b6a-aefa-ea450f3220f0 | -17.37595 | -45.51529 | 2025-10-26 04:04:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b169b134-3def-3edc-8643-d4e9be2197a0 | -23.77195 | -48.14007 | 2025-10-26 04:04:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a26155fd-3426-3e40-a88a-7a35830d8cf2 | -18.47095 | -47.16529 | 2025-10-26 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 951bf3cf-f7b2-342b-8b6a-932864823896 | -17.31685 | -43.65164 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72a8daa5-504c-3adb-bd62-d6508dea50c1 | -19.28623 | -45.81293 | 2025-10-26 04:04:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ebaf4f8-8e7f-3a26-ae4e-b1b9072a960b | -19.95275 | -43.83371 | 2025-10-26 04:04:00 | NOAA-20 | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 87ce05b1-267c-3415-a7e1-818e449bac82 | -17.04688 | -51.5264 | 2025-10-26 04:04:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d0bf1a81-fda9-3216-bc29-caf4be340dab | -19.86051 | -42.18549 | 2025-10-26 04:04:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4bb91516-9917-3af3-aec3-3682d1743535 | -20.85082 | -43.55629 | 2025-10-26 04:04:00 | NOAA-20 | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5fea20ce-6c2c-3564-87aa-58bc6bd0ba20 | -17.32021 | -43.65221 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f190db3e-685c-3eed-a61d-3a2df78617f6 | -28.24144 | -49.10843 | 2025-10-26 04:06:00 | NOAA-20 | BRAÇO DO NORTE | SANTA CATARINA | Brasil | 4202800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f47b1595-5a53-3022-a6b4-4368eacf8c91 | -23.76737 | -50.9035 | 2025-10-26 04:06:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| aee82883-3ed6-37a3-89d9-3145ab817abd | -23.76835 | -50.90174 | 2025-10-26 04:06:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 373ab342-b7ad-3189-867f-6472ec2025f3 | -13.5405 | -43.0077 | 2025-10-26 04:10:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 5af9b2e2-d289-3d4d-9d8a-aa0dddb0c7c8 | -17.3158 | -43.6674 | 2025-10-26 04:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ede8c39b-1cc6-3d62-895e-25e5481f9d39 | -21.771 | -50.0604 | 2025-10-26 04:10:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.5 |
| 0964c73c-9815-3f14-9763-ef538fc8e917 | -6.3864 | -45.7819 | 2025-10-26 04:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 9377e795-d8ec-3ce4-a390-0b6f1cee5df0 | -21.7717 | -50.0374 | 2025-10-26 04:10:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 258.4 |
| a195d6a6-5a1e-3396-a3ea-55fe6564426c | -17.3165 | -43.643 | 2025-10-26 04:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 120.4 |
| b2de3840-f51b-3c04-abe7-0ad006738fde | -21.7509 | -50.042 | 2025-10-26 04:10:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.1 |
| 6c9acfc9-488b-367e-8cf0-ce693da2a5fd | -17.3365 | -43.6383 | 2025-10-26 04:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 97.1 |


[Clique aqui para ver as próximas entradas](README30.md)
