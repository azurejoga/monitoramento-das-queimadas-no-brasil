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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92ace99a-c488-307e-9e08-92f3adcd4449 | -5.0938 | -43.8945 | 2024-12-17 04:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 9e6571f7-31ed-3487-982d-30d990d2d526 | -6.9349 | -43.4934 | 2024-12-17 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| bece7b9e-7867-3dc5-a9f6-03a5be08f7b7 | -5.0936 | -43.9176 | 2024-12-17 04:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 77b7152c-8674-31d0-99cf-868108615e4f | -3.2968 | -53.3749 | 2024-12-17 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 2a95261f-736c-3ef4-9736-ee538cd1d690 | -6.9346 | -43.5168 | 2024-12-17 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 8f0ad35a-cabf-3159-a122-b393e956133c | -4.51767 | -47.93885 | 2024-12-17 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50eb8893-0ba3-30b1-b936-e1c9ab798e11 | -5.08586 | -43.90621 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6edec0a0-6f64-3c00-830f-0e3feb81456f | -3.96016 | -46.92549 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be68faf1-bcba-30b9-847f-c7075de16d2f | -4.29887 | -43.89384 | 2024-12-17 04:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 555017ef-5bb5-3a47-bcdb-b7368b82f09d | -4.96822 | -44.96563 | 2024-12-17 04:21:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 24edfa7f-7c5c-321d-872e-ad88f0f9f8e8 | -2.94269 | -54.1792 | 2024-12-17 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d1be7a0-e985-3f7d-bf8b-1ad1283e2b4f | -1.54042 | -53.73428 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36507ade-7250-3b79-ac6b-86473cf6dde6 | -4.97153 | -44.96614 | 2024-12-17 04:21:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1a012b4c-8ed1-3887-a7ef-4e7a8fcf043f | -4.74072 | -37.8017 | 2024-12-17 04:21:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 24b2995e-937e-3ce1-a8f5-168c70f73ffb | -3.2433 | -46.80172 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37190d93-278f-316a-adf8-ee8dc348b7fe | -1.64076 | -45.92435 | 2024-12-17 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c5004d8-fec7-35ea-ba5b-7393d5756054 | -3.30823 | -53.3673 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc72fdbb-12bf-3bf4-982c-bd07a2475742 | -5.2116 | -44.56305 | 2024-12-17 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d064a55-6c6d-32f9-93b0-153b46d7528f | -4.20516 | -44.36255 | 2024-12-17 04:21:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b1da0aa5-0a67-3fc5-b280-1685d37d2808 | -4.00022 | -46.89949 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce3e2a36-fa53-379f-a17c-291cc5c51d05 | -4.36995 | -46.06924 | 2024-12-17 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3584817a-545d-389e-ba0c-0b706db0e6ff | -5.09913 | -43.90824 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| ff8ac644-fc6e-3d5f-ba48-ceab9b320d9c | -4.00875 | -43.24188 | 2024-12-17 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6fb8a3a-5dc5-33cc-90f3-505341aef0f2 | -4.79605 | -43.77915 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d00c97dd-688e-3388-9bd2-fcfc2ade708d | -4.07351 | -47.10048 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebb9fa42-af47-3e42-8a58-9eceb1f064b8 | -3.43986 | -45.60023 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07db5cf3-3884-3020-a94c-798bea9bd23c | -3.85471 | -49.15143 | 2024-12-17 04:21:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3dbb3bd1-ce8e-33b7-a014-d9691e949e96 | -2.94821 | -48.04908 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b872579-c4d3-30b5-beee-7f1017d185f9 | -3.83093 | -46.68411 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bfa15c3-45f6-3685-9c74-ca56c9b66677 | -1.63296 | -45.862 | 2024-12-17 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35880d60-d2c9-38e4-bdac-5114016053c7 | -4.09972 | -46.6666 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bc38abf-c537-3b40-b1e1-6464510f0866 | -1.29608 | -52.83266 | 2024-12-17 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8183218-9fa1-3be2-ad71-a040f7f7ff9d | -4.10466 | -46.70234 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b89dad66-4d30-3099-bfe5-241aeea9ffc3 | -5.09474 | -43.91468 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b3c0c684-c44d-3e67-97a0-42e3a9bd76bf | -4.20932 | -46.48621 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 869736c6-b77b-37b1-bcb4-a63ba6375224 | -4.20954 | -46.48673 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8252676d-4591-3d61-bd3b-1e1b027a2bf2 | -5.26057 | -43.76591 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 927afde5-4881-39cd-b648-65580ef2aa7a | -4.56107 | -43.56086 | 2024-12-17 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a006191-3229-38f7-8eca-712435c4f570 | -4.09343 | -46.72809 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2636a3dc-aa49-3283-9711-d29c428b0f44 | -3.87308 | -47.0378 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e3f9890-96e0-3534-afdf-ce1a51c23d1d | -4.01134 | -46.89723 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01b74f4a-c31a-3517-8a70-da0e4ff46c03 | -4.0346 | -46.90903 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7753005-d6e1-34d8-b560-5de23a4a875a | -2.57674 | -49.41269 | 2024-12-17 04:21:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eef1a34-e481-3c3a-a1b4-73fcb303ec59 | -3.73945 | -50.05539 | 2024-12-17 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1149a83c-1a1a-30f4-8c45-1bae88d3634a | -4.20186 | -44.36203 | 2024-12-17 04:21:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 218372ec-c2c8-303c-88ca-63b315ba30e3 | -4.10701 | -46.62102 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89ba8bd8-e00a-3ea3-aa13-2c6ef13e1096 | -3.03054 | -47.83082 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 414dfc4d-fb13-3f36-9392-c277a95b78e9 | -4.48142 | -48.12009 | 2024-12-17 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7a97c0a5-7e5b-30bc-a9b7-6d702dcbc9bc | -2.24581 | -45.69153 | 2024-12-17 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ae6f27e-abd3-3bcf-b618-f106dda30a22 | -3.83034 | -46.68789 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e52a9bb-820e-37f3-a382-ee5accb21742 | -4.03908 | -47.02203 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dd57629-5f1b-3c6e-9601-ad4b809fda5e | -4.0195 | -46.82288 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7da62ec-d7ec-3973-b22e-2834078a6e7f | -1.29687 | -47.74474 | 2024-12-17 04:21:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 486ff3f4-f58c-3a3a-82b6-01bba7a89966 | -2.05412 | -46.66369 | 2024-12-17 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 237dd55b-a6ee-3dac-ab0e-b8f37080cb07 | -4.04385 | -47.0148 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfab661f-2ab5-3b6c-8014-232b5cc26cd9 | -5.96517 | -41.59587 | 2024-12-17 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ed31e907-a637-3a2b-899c-651c5ab3cab1 | -1.27502 | -53.03275 | 2024-12-17 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b85600db-78b5-337d-8e2a-8ffd2c061ae2 | -3.43544 | -53.9847 | 2024-12-17 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65f743da-07b1-30a6-b18c-8bfa187990ad | -4.68041 | -44.04175 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dba32188-7ed4-39e0-bc9f-4d7dcb184fd6 | -3.99594 | -47.28976 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3af3ee41-b310-3dda-93ad-a7fff38a6701 | -5.11614 | -43.20406 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0e55a09-57ad-3fe4-9e71-6c6bba12d635 | -2.26807 | -48.32868 | 2024-12-17 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4adb49ef-8411-3ede-9f3d-3de88cfbf48c | -2.87928 | -45.251 | 2024-12-17 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 500d695a-71e3-3a1b-ac69-134515c49703 | -3.99672 | -46.89893 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df26afc2-daaa-3d94-8bf6-7f37c031bc19 | -3.96096 | -47.97434 | 2024-12-17 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db2cffe5-b471-34f7-9807-033f2d348395 | -4.17443 | -46.7247 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94e8b029-7eb9-3e4b-91c0-5cbaa09f7b9c | -2.55902 | -47.59371 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2d942e2-1492-310f-b503-f9a32ef1c185 | -3.66981 | -47.12946 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e767ea8-7d2f-372a-bf04-87747991102d | -2.65746 | -45.93169 | 2024-12-17 04:21:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e37e7e1f-5835-3fed-a0f3-dadf8e41096b | -1.46122 | -46.81116 | 2024-12-17 04:21:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6048afb-c9ef-31ab-b03a-ea8191096965 | -5.06257 | -46.39774 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ed46a16-c62f-3b90-b915-1595815cebdf | -2.04043 | -46.50019 | 2024-12-17 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99a805e4-0281-3a3b-b92b-2b12bdcac025 | -3.45999 | -54.04212 | 2024-12-17 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b04e1636-63bd-3014-8fcd-e9f1bf72d696 | -3.02123 | -48.03075 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3e17aba-3eae-3ed1-b1ed-db65d3ae8181 | -3.77277 | -47.14553 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e187de56-09df-3002-b326-a259d4d05f37 | -2.4936 | -47.27443 | 2024-12-17 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79437447-0bed-30f4-95f0-27ce0a368e89 | -4.09627 | -46.73254 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d324097-70b4-30aa-81b2-7916395ac4c3 | -4.07699 | -46.61594 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ee7e641-4d2c-389b-8442-c24e478f60b9 | -4.29941 | -43.89038 | 2024-12-17 04:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f77af11-5123-38d5-8021-025689a25ccb | -4.79874 | -46.40244 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5456bc91-75e6-363a-953c-0f81fa4ecdcd | -4.03025 | -46.86821 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1382a9a-356d-374a-9df4-466d90307f9f | -3.42239 | -43.16598 | 2024-12-17 04:21:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fad93dda-43ba-3735-a6cc-55cecfe1b350 | -2.87314 | -45.24644 | 2024-12-17 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9259c85d-21ed-37e6-8d11-846c3ce770c6 | -2.58086 | -49.41335 | 2024-12-17 04:21:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03ab9ef6-429d-3f26-90e9-5c802a6b14d0 | -3.92672 | -46.9322 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e358425b-8dd3-3bad-9c7e-9c397484bb18 | -5.2954 | -44.93957 | 2024-12-17 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f58ff16-5947-3b5a-949c-89dd837e9244 | -4.05485 | -46.924 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5565b877-5b13-3ef1-92c8-19b372d99d79 | -1.65576 | -45.89605 | 2024-12-17 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9194385f-6171-3a52-b7d7-230e0722d5b0 | -3.16201 | -45.98272 | 2024-12-17 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3b63d5e-fbb4-3027-bedc-ac5904c1e045 | -3.86664 | -47.0328 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e5063b22-042b-382c-b7ca-d598b5cb4faf | -4.06624 | -46.72005 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd9785a9-0e75-3c78-b464-38183c552243 | -3.297 | -53.36885 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b9536e55-6a83-3ec5-9146-f34580ede1e4 | -4.02191 | -46.80762 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c8a6618-f5ed-3dbc-8b47-85b5c27de0f3 | -2.58259 | -49.42881 | 2024-12-17 04:21:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cd8d3fa-58ab-3502-80dc-ce46eb627209 | -1.40477 | -47.47586 | 2024-12-17 04:21:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63380f6f-25db-34b3-802a-c5936ff8f9c7 | -3.29852 | -53.3705 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 91b94791-a063-302c-9cc8-7d40bfc7cbc1 | -5.38925 | -43.65992 | 2024-12-17 04:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a15ba86-8e22-319e-90f8-9cef5f20c745 | -3.07726 | -47.75271 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50a3dde5-eca1-313a-bc3e-b49c17c3d055 | -4.76361 | -46.71042 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| acbf0868-59b5-3447-835a-1a053b98225e | -4.52622 | -44.04977 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
