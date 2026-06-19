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
| 25669f1e-dd73-3e0f-8fc3-52445124cf70 | -13.96581 | -47.37729 | 2026-06-19 03:42:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3e15ec1-2fcd-31cd-ba00-4fed8b9e26cf | -12.86498 | -44.37306 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 70814160-ac96-32b7-a700-d9b2e13212c6 | -12.87087 | -44.37087 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 922813c7-da45-3329-8dea-32e9f138c9a2 | -11.3667 | -46.30969 | 2026-06-19 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0f35450-37c5-398a-b496-6816b14bec5f | -10.98151 | -47.74496 | 2026-06-19 03:42:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d591cb72-72a6-3992-89b2-b448610be1d6 | -13.32341 | -45.1772 | 2026-06-19 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cd73492-83f5-379f-9fe0-61d3e976a97d | -17.9955 | -43.25926 | 2026-06-19 03:42:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 562da005-f9f5-36b8-b4d5-fb6c00767747 | -12.83873 | -44.36765 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 25986b10-2cd2-3f1e-b6d6-81c95ea3e228 | -13.32414 | -45.17356 | 2026-06-19 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f3e523b-1556-3da7-82ca-e8ed01b1cc7e | -12.28192 | -42.66351 | 2026-06-19 03:42:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12454e9a-9de9-398d-966c-54e1f399533a | -13.31615 | -45.15646 | 2026-06-19 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b80d6bd-30e3-3e3c-aab6-180c6cefac76 | -13.31542 | -45.1601 | 2026-06-19 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c89f45c4-cd41-381d-8433-42ba61fd25a2 | -12.41319 | -43.82125 | 2026-06-19 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d71d0a10-2304-3a2a-83c4-d71fba284511 | -12.44368 | -44.75479 | 2026-06-19 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce19c176-9a56-3686-a4d0-2d647e8ffbc9 | -10.98027 | -47.75103 | 2026-06-19 03:42:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f08423df-f881-35fa-b52e-3abe6529fae0 | -12.86563 | -44.36974 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d9ee32f5-84af-3947-ae01-9a0b0b52e3e9 | -12.87546 | -44.37535 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 42720cc9-9c0c-34c0-bad1-fc8ea289465a | -12.13279 | -48.2639 | 2026-06-19 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e6914964-ec46-3278-8224-a22770e95ee2 | -12.78922 | -44.508 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bd5f0c8-4ff1-3854-96c4-3e92bee9b79f | -17.31374 | -43.64694 | 2026-06-19 03:42:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f062c71-0344-3d4f-bee9-7e15541bfb15 | -16.02345 | -43.42757 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1b551a09-26cb-3203-b58d-8cfcf719fdee | -11.32966 | -48.00384 | 2026-06-19 03:42:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9774d8f-518e-3b8b-89ae-dc0d9484f40b | -13.9647 | -47.38253 | 2026-06-19 03:42:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63c49ef9-df72-3573-bc59-6dce3b42a505 | -12.83807 | -44.37101 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4abf1668-bf24-3354-9103-1f4139b823b7 | -12.87407 | -44.35427 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b7b62e0-c53d-35b6-904a-29f9bad96af1 | -12.83282 | -44.36994 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a56f0db5-21c1-35af-8033-b5abd0d0abfe | -11.33642 | -48.00512 | 2026-06-19 03:42:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 530337fe-a43a-321a-8862-b114188682fd | -13.32088 | -45.16135 | 2026-06-19 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40d24ebc-35f0-3e3f-a3f7-607725812ef7 | -12.87215 | -44.36423 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bfeccb8-b659-3eff-abb3-d410d2af777f | -12.78391 | -44.5069 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6873d42e-651a-3c8e-86ac-d4b8d1cc1a25 | -12.40751 | -43.8232 | 2026-06-19 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 58b02455-0c7a-3de6-a392-ce593790af21 | -12.50026 | -43.76686 | 2026-06-19 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5c2aeb33-f00c-3397-9cda-15ff992b81d7 | -16.02533 | -43.42841 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 14b50e02-6f55-37be-8799-593d97227e59 | -12.78324 | -44.51033 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bc5a733-cb48-3ee3-98da-28d3581105a7 | -12.494 | -43.77194 | 2026-06-19 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ccae9863-5f3c-3af1-8bfc-f60ae9b78e02 | -12.78989 | -44.50458 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8df44809-64a3-313d-9069-13e0452db6e4 | -15.35963 | -43.66765 | 2026-06-19 03:42:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86058696-dafd-3f5b-927b-e8c24e09993a | -16.03202 | -43.41908 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 16d912fc-9359-3c7e-8779-36e908c34fa1 | -12.49459 | -43.76888 | 2026-06-19 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec98226f-0293-3901-b792-2e3d8ef7b36a | -12.87482 | -44.37868 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| bc0f157c-b062-348a-ad1c-9f789259806a | -17.31936 | -43.64282 | 2026-06-19 03:42:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4f6eddad-d550-3b0b-a8d2-407e7682b3df | -13.31469 | -45.16373 | 2026-06-19 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1107daef-6a46-3213-acec-46ffa81bd413 | -17.10847 | -49.75742 | 2026-06-19 03:45:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7878eb55-270d-39fd-a502-957dd527a07c | -22.80577 | -49.34144 | 2026-06-19 03:45:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8388bacf-39e1-31f8-9ab6-473905f045c9 | -21.22388 | -44.14705 | 2026-06-19 03:45:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| cb935f16-b077-3b3c-8a78-b69aed7af023 | -18.82434 | -39.92812 | 2026-06-19 03:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 493d9ac0-fa73-3d12-8b05-0fe3570dee87 | -18.82609 | -51.47216 | 2026-06-19 03:45:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21f4d1a6-d34a-3ae1-94ba-71ab96284458 | -18.8305 | -51.47505 | 2026-06-19 03:45:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3425682c-83e2-3ff9-b538-493d418f1b84 | -21.22577 | -44.14577 | 2026-06-19 03:45:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f18cbfa6-f212-3bdd-9a1f-286364dd8986 | -22.78304 | -49.34441 | 2026-06-19 03:45:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 561ab844-b8dc-3573-aa0f-2a5015fe2fc1 | -22.79998 | -49.33962 | 2026-06-19 03:45:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e460eef4-a871-35dc-aa08-04e747d4927d | -18.70077 | -40.24196 | 2026-06-19 03:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e9eea9df-5a56-3e07-bfb3-60e10200a26c | -18.87663 | -40.03691 | 2026-06-19 03:45:00 | NOAA-20 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 504bd2f5-2f31-3269-b826-4cb657fb8fad | -17.10984 | -49.75147 | 2026-06-19 03:45:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4c0c574-dbc2-3c88-ab58-72ec17cb032b | -22.78192 | -49.34916 | 2026-06-19 03:45:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1ed15ee-3ee5-3308-a302-3d8a9012a542 | -18.8235 | -51.47281 | 2026-06-19 03:45:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b0213d4-dd62-3f36-97cb-9f55f30e216c | -22.6985 | -43.36295 | 2026-06-19 03:45:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0a83e702-ea59-304d-a8dc-e6cbbff6b361 | -20.87736 | -43.76682 | 2026-06-19 03:45:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 61a9e0d1-21c3-3350-a212-1634ced98671 | -22.80258 | -49.34068 | 2026-06-19 03:45:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12cd5e9f-828d-3280-8a48-64b8e4e29af8 | -22.34343 | -41.78277 | 2026-06-19 03:45:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fecc4db9-65d1-34e6-a286-73f1bd3776f7 | -22.78079 | -49.35396 | 2026-06-19 03:45:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48d31e21-855b-323b-a961-6171bd84147e | -22.78885 | -49.34617 | 2026-06-19 03:45:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea4b5f45-dd0b-3c65-93ab-d6797f991b41 | -12.8736 | -44.3828 | 2026-06-19 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e12dc3c4-c5da-3de6-aeb5-e1f14fccb243 | -12.8741 | -44.3593 | 2026-06-19 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 45477062-6fbd-31dd-945d-04fae1477e28 | -16.0342 | -43.4224 | 2026-06-19 03:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 4c0df812-31b9-3a3c-8b83-88c8d0ab3ffc | -12.8741 | -44.3593 | 2026-06-19 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| d7c0960c-41b3-3c8d-98ae-30d594486c10 | -12.8736 | -44.3828 | 2026-06-19 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| b4cb7988-c984-3fd9-a1f0-caa5fe283651 | -16.0342 | -43.4224 | 2026-06-19 04:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 9327a332-019c-3723-b835-cde03495efbd | -12.8741 | -44.3593 | 2026-06-19 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 8e92a2b2-0fd4-38bd-acb5-67002a079627 | -12.8736 | -44.3828 | 2026-06-19 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 392a5610-9fd7-3013-b544-00e9ed9d0653 | -16.0342 | -43.4224 | 2026-06-19 04:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 3f4059f5-fe53-3954-960e-2a1095372bb7 | -12.8741 | -44.3593 | 2026-06-19 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 60161847-e377-35a9-87ae-eea89d1582c5 | -16.0342 | -43.4224 | 2026-06-19 04:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e58d0790-9fe8-39a2-ac63-5fd8369dc21b | -12.8736 | -44.3828 | 2026-06-19 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 1a18f0ca-ee73-3671-9df4-45b8794172b2 | -4.35484 | -47.76458 | 2026-06-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cec5f280-a190-34d5-967d-fddc3985ec3e | -7.00412 | -43.86738 | 2026-06-19 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6855ed5-4cc4-3355-96af-631c674c50e0 | -7.3573 | -49.85899 | 2026-06-19 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7ca22c9-ed00-3454-b616-c0f1b0e8d520 | -3.51444 | -48.0342 | 2026-06-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e8ab827-3628-37f3-936e-c396130418a4 | -5.61246 | -37.53153 | 2026-06-19 04:25:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 459001b1-03aa-3592-8ef2-123aeb35c293 | -7.36097 | -49.85957 | 2026-06-19 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bbb8eb2-796f-3194-98e0-3eb3e63ea461 | -3.51382 | -48.0381 | 2026-06-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa0024a8-efec-38e1-9a31-c2c3e20ddb56 | -3.82032 | -50.63355 | 2026-06-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ed58adc-c26d-336e-916f-7513d09cd474 | -7.13475 | -45.88158 | 2026-06-19 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32bce23c-ce62-354d-95df-8b1baf775e70 | -7.72026 | -44.16427 | 2026-06-19 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3af175c-da6c-3eb3-934a-d1e7da7826a0 | -7.80448 | -46.45438 | 2026-06-19 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c1e78c4-a416-3ff0-84f0-0e015274853b | -6.64935 | -43.91743 | 2026-06-19 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 34a11a9d-316c-3cb5-8a7d-9282d5bca414 | -3.50745 | -48.03316 | 2026-06-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4764320-0037-39cc-b844-df31a719d494 | -7.36026 | -49.86388 | 2026-06-19 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8afcfd8-6637-3dd1-9af0-2e9f97615893 | -5.84606 | -47.19893 | 2026-06-19 04:25:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1b57fe3-53bf-3a6f-9c62-fb18bea7540f | -3.85304 | -54.22452 | 2026-06-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 858fb797-c695-346b-b32e-b1f400d69e83 | -4.23554 | -49.18065 | 2026-06-19 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48d91114-fa54-3a3e-aa74-f49bf8655b27 | -6.90649 | -42.84341 | 2026-06-19 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 15db2c9c-0d08-3065-8bf5-2b2bcf4f7a70 | -6.62923 | -38.73308 | 2026-06-19 04:25:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 50fa360d-6842-3d25-b7a3-3eeeee58e15d | -2.31453 | -47.18402 | 2026-06-19 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5d0bb7c-b16b-34b1-be1b-a26fe9372183 | -7.3566 | -49.86329 | 2026-06-19 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76358b08-e3a8-3f6e-be6e-69b4ed8d1ea9 | -4.23692 | -49.17202 | 2026-06-19 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 757f19e7-97b7-3cec-8aa2-62bbd34f1cfd | -7.79788 | -46.45335 | 2026-06-19 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 08be0398-86be-3b78-a29d-cde40d720c26 | -5.82782 | -45.07227 | 2026-06-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| baae02ef-81f0-3e27-9463-f7a38c7b7371 | -7.13145 | -45.88108 | 2026-06-19 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5912e653-973e-3d82-ac4b-eb5109670252 | -6.64646 | -43.91312 | 2026-06-19 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README4.md)
