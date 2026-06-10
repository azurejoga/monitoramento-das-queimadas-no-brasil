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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fa8ab6d-df81-390f-ad13-6f3fbb6a0abc | -18.59092 | -46.58297 | 2026-06-10 03:57:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9067f48-9683-30ee-996a-01b8b3403b46 | -17.4332 | -43.82061 | 2026-06-10 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2b7ac2b8-1dd0-3730-8722-b4cde22e171f | -14.40079 | -45.55814 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e00bc814-f082-3039-8ff7-e1b8d255796d | -16.81267 | -41.86067 | 2026-06-10 03:57:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 29ee8f6e-a28e-35e2-bd3f-2540bda1a347 | -14.3701 | -45.56416 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0aeb5a6-c0d9-39f3-a33b-01a883238588 | -12.0549 | -49.76727 | 2026-06-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddfd8ab7-e934-3aca-a678-72786b6222d8 | -17.45253 | -47.17998 | 2026-06-10 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0be7c14b-bd58-3655-a686-153e13fc6172 | -18.15784 | -42.6516 | 2026-06-10 03:57:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 3f0b7cb6-5fa9-388b-b589-07b2fd63c31e | -14.35446 | -45.53397 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dd1fa49-c5e0-30b3-9488-ae34e3e4ef3d | -17.45089 | -47.18854 | 2026-06-10 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78d1e615-3ffb-3636-8245-807ccbabb075 | -14.6484 | -47.99449 | 2026-06-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1319688b-78a4-3cfa-b32c-cbc893cd2074 | -14.36195 | -45.53925 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb6ba805-c077-3e04-93d3-ad74f03d2e05 | -18.90723 | -41.94112 | 2026-06-10 03:57:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 00bae932-f8a2-396f-870d-a7367f7f9c26 | -14.64776 | -47.99673 | 2026-06-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f5c9f6a-0f25-3991-833c-326c755f3428 | -14.37079 | -45.56038 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d6d7db4-c843-386f-b2d9-c23c55d9306b | -15.18203 | -43.85226 | 2026-06-10 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b271e94d-5267-3c86-ac5d-d350a4e39cf5 | -14.36601 | -45.5634 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9753b486-8f77-3b3f-8e65-e3888af5d414 | -14.69494 | -48.31221 | 2026-06-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dad13f0-073f-3249-ae7b-c48eb3554dc4 | -13.95884 | -46.19437 | 2026-06-10 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 77e251b5-f3ba-3d45-9ce3-f12bee3122e1 | -14.41311 | -45.58382 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92c3bfaf-ed13-3263-b1fb-81cb870cbfdd | -15.75319 | -43.3077 | 2026-06-10 03:57:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f4a195f-84c6-3081-a4ea-1f6c91ec35bb | -17.4552 | -47.18941 | 2026-06-10 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da5f53f1-53e0-33d4-bcb9-8ad6dcc13eb0 | -15.43188 | -46.34003 | 2026-06-10 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d17df1dc-c4c4-3ec5-bce4-cf8c18465d2b | -13.51467 | -47.81586 | 2026-06-10 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b8a3f62-824f-3501-bc81-939d021a5585 | -15.47414 | -40.05825 | 2026-06-10 03:57:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2f8d683d-ffe6-3df1-8920-003a58a077f4 | -14.03257 | -42.15932 | 2026-06-10 03:57:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| adfaa4f7-b7a8-3b47-a3d7-2f6a4ada5f50 | -13.76687 | -47.10973 | 2026-06-10 03:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f51255d-dc53-3cdc-9015-320c1afd9cd2 | -17.42326 | -43.81449 | 2026-06-10 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a988556-3f33-364b-a2d9-5577522c4ce0 | -14.41379 | -45.58004 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e28a06a9-de1b-33c8-971f-459ee62422e1 | -14.36672 | -45.53622 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 642c3f6b-efc9-3726-8cc0-e9de5edfa260 | -14.40487 | -45.55894 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16016cc4-6095-3894-944c-e3e01738c3dd | -15.17762 | -43.85604 | 2026-06-10 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93b81922-b1a6-3145-816f-474c3d41912a | -17.42682 | -43.81512 | 2026-06-10 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c51d0038-1695-3760-a0dd-7f179fff7632 | -15.17837 | -43.85159 | 2026-06-10 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ace5ffa-bf12-3e23-af8a-ac8c303480a4 | -14.35038 | -45.53321 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0c74b04-b0cc-3cce-a069-4019d7a00de9 | -15.43966 | -41.37734 | 2026-06-10 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9be724b1-eeee-3ed0-974c-630bd37e08b8 | -14.63243 | -47.97412 | 2026-06-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bda5191-5a3d-35ce-8985-0875c8a2d1c5 | -14.40012 | -45.56189 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64d857c6-9ebd-3657-bd83-1afa9208b8f2 | -15.52337 | -42.62605 | 2026-06-10 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0cab951-d3fb-3dba-b19d-f622d2547a64 | -17.79606 | -44.5707 | 2026-06-10 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c90f690-395c-3d82-b398-0bf55151369d | -16.15368 | -39.23265 | 2026-06-10 03:57:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0f460f14-bf17-3810-92e5-e4ca43b457ad | -19.69522 | -44.92793 | 2026-06-10 03:57:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 310f4815-c6c2-3c0f-8baa-d720d274a241 | -14.62245 | -48.00074 | 2026-06-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad051e06-f6bc-32d6-aeb4-2f8a1c51c992 | -14.41788 | -45.58081 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2681d0d8-f585-32e9-81b6-171d87f81378 | -20.75397 | -41.88804 | 2026-06-10 03:57:00 | NOAA-21 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bb5f98ba-4051-31a7-968d-095c7f47215c | -13.75569 | -47.11871 | 2026-06-10 03:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 971e3303-aa72-3d6c-8ca4-e69de444a486 | -13.59029 | -46.54897 | 2026-06-10 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a265c5e6-f10d-3a63-a271-b0ac98dd8486 | -18.45198 | -40.34951 | 2026-06-10 03:57:00 | NOAA-21 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ab724a4-8381-3243-b464-c3a185176689 | -14.3667 | -45.55962 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3736258-4481-372a-9460-d9cb103f4607 | -17.42398 | -43.81031 | 2026-06-10 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d4702383-753e-398e-a557-afa6451badad | -14.37489 | -45.56112 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5f42f9c-1850-345c-b65f-2d3cf69a4161 | -15.18118 | -43.85492 | 2026-06-10 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 93e3b83e-86fd-337f-9fe5-aa7d2b5c4663 | -17.42753 | -43.81095 | 2026-06-10 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 57ed056b-c560-3915-8cda-79c7ecc47e6b | -14.69978 | -48.31329 | 2026-06-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f82d9625-693e-3e9f-a2b4-3f5ce14a6225 | -17.79182 | -42.56369 | 2026-06-10 03:57:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c64ac0f4-ba0e-367b-8fdb-2596f37c7fcd | -14.69392 | -48.31738 | 2026-06-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20457ed8-c636-3336-b8f7-76f2752f9531 | -15.52616 | -42.63058 | 2026-06-10 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 71bafc37-a451-3284-875b-7d717a1931f3 | -13.9596 | -46.19018 | 2026-06-10 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1c159b47-c6a9-315a-97f3-76b35bf4dfcc | -16.81238 | -43.66561 | 2026-06-10 03:57:00 | NOAA-21 | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21d69b90-54aa-37c9-a140-eb801cdac5ef | -18.4553 | -40.35007 | 2026-06-10 03:57:00 | NOAA-21 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fdee2c97-84c1-3ac5-8427-424b5fdfccb0 | -14.3742 | -45.5649 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bdc8b10-9c5c-3d92-a07a-e14194ae9c6e | -14.36604 | -45.54 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a19b199-117b-3a2d-ab30-74abace337c8 | -14.69639 | -48.31672 | 2026-06-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df3354ce-acf7-39aa-a12c-9b4cfe5e4d53 | -19.26431 | -49.41828 | 2026-06-10 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1fb260a-19de-3b4e-8df1-4408f5d781ac | -19.6955 | -44.92541 | 2026-06-10 03:57:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8955ab57-bdea-3c28-95d3-dcd0d4d2cb9f | -15.18128 | -43.85671 | 2026-06-10 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb557b3f-4dec-3324-90c3-27ddaf830606 | -13.26906 | -45.57563 | 2026-06-10 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7864ebac-60a9-3ca7-bb7a-2f687d21c793 | -12.05567 | -49.76338 | 2026-06-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00bbbf94-3c06-33a4-bed4-2c0e0583c6cf | -14.39944 | -45.56565 | 2026-06-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 784fb3c4-c60c-343a-bc73-c6e0c2e49395 | -14.6314 | -47.97959 | 2026-06-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 872cdf34-0459-3cd4-bc12-340c8ec07202 | -15.17472 | -43.85093 | 2026-06-10 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6db4dbca-6992-3812-980d-a8c14d12f338 | -18.37212 | -39.95692 | 2026-06-10 03:57:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0a46a409-d8ab-33e4-bf2a-50e91335659a | -9.3234 | -45.4787 | 2026-06-10 04:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| cbe177c1-c0e1-3cb6-9056-56e8c618ddb5 | -9.3045 | -45.4809 | 2026-06-10 04:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.5 |
| e8475a60-9998-36cf-8dfd-f9b670b8db5f | -9.3048 | -45.4581 | 2026-06-10 04:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| fd1973d8-48da-33fb-af0a-ed98995d45bd | -22.04098 | -47.01048 | 2026-06-10 04:00:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb3fcfd9-54db-3583-ab10-88a2427a8221 | -19.96459 | -54.3439 | 2026-06-10 04:00:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de29c788-931d-3497-bc88-6100a4016038 | -21.31835 | -48.54109 | 2026-06-10 04:00:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5199e36d-39fa-3177-b486-2f966b4a7a22 | -22.13297 | -47.7042 | 2026-06-10 04:00:00 | NOAA-21 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81382717-cc77-3170-afa4-226dcf130c8a | -23.56327 | -47.51108 | 2026-06-10 04:00:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| b6cfee04-0b1d-377a-90cf-c28fafc9b8a5 | -22.38306 | -49.79122 | 2026-06-10 04:00:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2229c3db-0836-3ced-aaea-fc690036e321 | -22.45136 | -47.14974 | 2026-06-10 04:00:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b03056b-ded4-3e8f-b799-028dd27d1306 | -22.03971 | -47.01217 | 2026-06-10 04:00:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c929d12-a8de-3239-b169-0b6d606b21ac | -23.31561 | -47.19139 | 2026-06-10 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e364a9d1-f22b-34ad-b7cf-4447c3c7b589 | -23.31477 | -47.19473 | 2026-06-10 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8d54d1a5-d885-30d4-ace0-10c9f5dc0e78 | -21.32315 | -48.54025 | 2026-06-10 04:00:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7a8d0f6-e8bf-3118-9d47-06f514678454 | -19.96293 | -54.34489 | 2026-06-10 04:00:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa88299e-7e4b-392c-914c-65791aa85df4 | -22.38082 | -49.79282 | 2026-06-10 04:00:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ea1a4102-a396-3f5a-abc4-5b773804cff0 | -22.04073 | -47.00683 | 2026-06-10 04:00:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a56740a8-397d-37a1-a9e9-fba13952418b | -21.3188 | -48.53925 | 2026-06-10 04:00:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72a7044a-a16f-3feb-8b49-10f9aa58474d | -9.3234 | -45.4787 | 2026-06-10 04:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 72feb303-8692-33a8-b24a-478e5cf2e1ed | -9.3048 | -45.4581 | 2026-06-10 04:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 356020de-ceed-3f83-8789-46462666466f | -9.3045 | -45.4809 | 2026-06-10 04:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.6 |
| e7de1979-d217-3638-9f83-d279d5b66c54 | -9.3234 | -45.4787 | 2026-06-10 04:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 2d468aab-1ab6-362d-a8bc-ddfb325d9e60 | -9.3048 | -45.4581 | 2026-06-10 04:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| fc5865b1-87b6-373e-b14f-b97bf6dd1ea2 | -9.3045 | -45.4809 | 2026-06-10 04:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| e8917798-e99d-3d6c-8a86-7c0ea11c6772 | -3.50577 | -48.03585 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c1a0fa1c-b793-3be0-8c13-ac5c67bc7215 | -3.49825 | -48.03726 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48092b0f-1c45-3aa5-8006-c603f7dbcd80 | -3.502 | -48.0353 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58d05528-54bf-311c-bcc2-c8c2067dd1e3 | -3.49749 | -48.04186 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README6.md)
