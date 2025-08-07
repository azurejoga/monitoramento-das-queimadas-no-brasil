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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6e739c8-890c-366d-8982-6af9724e07e7 | -8.92014 | -60.56332 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0159b3e-fee7-3e71-b2eb-f956de6e3381 | -9.93775 | -60.50138 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abb7e2c5-e512-3fcd-b03b-54d662242c94 | -8.91965 | -60.54489 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9370c38c-66f5-3700-af50-a24242ef12c7 | -11.75505 | -48.18435 | 2025-08-07 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2b558080-9ae5-36df-9dc7-cd0b753fed90 | -12.37701 | -47.04397 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6737869-5eb7-32f0-9895-ebf47d584e68 | -8.92342 | -60.58589 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de7c22fb-cbf1-3b8f-9f09-0d88bc2f921e | -8.90662 | -60.58315 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f7d4853-4ab2-3821-bd63-93bda86b212d | -11.75278 | -48.18356 | 2025-08-07 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b99365db-33bb-3db9-b1a9-9c38315abdce | -8.9167 | -60.5848 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 199115d6-1b15-3a96-9d45-b852c532623b | -8.92358 | -60.54186 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0884bd6b-fa6e-36b7-b6a4-a885f1373352 | -8.923 | -60.54544 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67b8c4f8-7e2f-346f-954f-ba4ae736dfd1 | -8.90498 | -60.57189 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfeb38a4-576e-3405-a131-175e03382634 | -8.92474 | -60.73711 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 0724fe7e-4cae-3f5f-9664-934d9409b937 | -9.93596 | -60.45773 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f72547ed-6f8a-32b4-9298-b429884cf727 | -10.70169 | -48.86928 | 2025-08-07 05:21:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd17e589-ab70-3669-b8c8-d587af5e1b15 | -13.07619 | -56.85713 | 2025-08-07 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fad15e5-5d65-3fc7-8023-91d19acc3526 | -7.40924 | -60.01379 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3a51f470-9343-38b8-87a0-3483ec38ac34 | -9.93889 | -60.4943 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6febad5-1d53-3338-b3f3-f63fa588d5ed | -9.94345 | -60.46595 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eea4a8e5-5e9d-34c5-8f00-2379ccb3d5f5 | -10.70002 | -48.87245 | 2025-08-07 05:21:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c97cfbf-1e74-3191-b237-5821daec39db | -8.90834 | -60.57243 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84c0dbd9-b0ec-3f2e-b7ca-bc98c38e4e07 | -8.92178 | -60.57462 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 970b5988-2bb1-3ccf-bcd8-a76ac18b38b0 | -9.70758 | -61.2942 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 548194bc-2ee5-3312-8e24-d6158f671ca4 | -13.71646 | -53.86113 | 2025-08-07 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e7a730a4-7904-37fa-abcd-f7ceace9f8c0 | -9.94068 | -60.46186 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2508488-d51f-38f7-9e77-a179655db6a6 | -12.52454 | -47.15145 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7212efa-baa4-374a-ad12-f823b70e4ae9 | -19.85044 | -49.07981 | 2025-08-07 05:23:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b2235b4-fe88-38c5-bf17-957f0071050c | -19.8454 | -49.07949 | 2025-08-07 05:23:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbf461f6-d384-32be-b37d-00f616b0d978 | -20.43867 | -51.98959 | 2025-08-07 05:23:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2765ecd-4839-3d76-b340-c936464ffe85 | -19.85203 | -49.0798 | 2025-08-07 05:23:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60f08a32-56c3-358b-bf2b-2fa43525ad6e | -19.84433 | -49.07314 | 2025-08-07 05:23:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36b6dad1-6363-3b2e-b90c-dc04f82415d7 | -17.11118 | -49.14445 | 2025-08-07 05:23:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 798857f3-6fd9-3266-9b52-79a0eaa8ed81 | -19.84382 | -49.07934 | 2025-08-07 05:23:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b5348cd-e59d-3d42-9d58-f25facdeae5f | -19.47314 | -55.40971 | 2025-08-07 05:23:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c98b9046-f4f1-3323-96ec-26068e189c86 | -19.84595 | -49.07325 | 2025-08-07 05:23:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bad7558-d3cb-33f1-8757-4b4fe19bb23d | -21.3945 | -50.3026 | 2025-08-07 05:30:00 | GOES-19 | COROADOS | SÃO PAULO | Brasil | 3512506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.9 |
| 7d0b8a01-9a1c-3379-93dd-8c4067bc4ecc | -10.6438 | -44.7645 | 2025-08-07 05:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| af3e83ab-4658-3da4-8cdd-3697a036212d | -21.3951 | -50.2797 | 2025-08-07 05:30:00 | GOES-19 | COROADOS | SÃO PAULO | Brasil | 3512506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.6 |
| 579aecf8-37e8-3786-88c0-a9b71871c40e | -8.9213 | -60.7489 | 2025-08-07 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| baec3a55-3fea-3483-9cf2-7dd2b7173997 | -10.625 | -44.7439 | 2025-08-07 05:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 184502e0-d0f6-3545-a6d8-637bc467d2e0 | -7.4074 | -60.0108 | 2025-08-07 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 484e61ba-a18c-36ec-9c45-fb776750596c | -8.9215 | -60.7297 | 2025-08-07 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| af092c61-b90e-34bf-8223-65f509f77413 | -10.6441 | -44.7413 | 2025-08-07 05:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 141.7 |
| f8530ec3-f529-3112-9edc-32b72e9418d9 | -8.9399 | -60.7481 | 2025-08-07 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 52cabce7-1faa-3358-a4dd-9076ab89b6ee | -8.9213 | -60.7489 | 2025-08-07 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 1a59f0a8-e6b6-380e-a14a-5d0130663b98 | -10.625 | -44.7439 | 2025-08-07 05:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 7255823c-3ea6-360f-a806-a6ce61cc1a28 | -10.6438 | -44.7645 | 2025-08-07 05:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 591a193b-68b4-306f-9c47-b9e53d137ddb | -7.4074 | -60.0108 | 2025-08-07 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4a106e20-e2cd-315d-bd57-ae7b8408257a | -10.6441 | -44.7413 | 2025-08-07 05:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 0cc3d075-4e5a-38b1-921c-f64b179f3c97 | -10.6247 | -44.767 | 2025-08-07 05:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 7b85c73c-2e2d-341c-86ee-15bd97417e13 | -8.91984 | -60.76472 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5678dc9b-9733-301a-90f4-10becaabc9c4 | -8.90882 | -60.57486 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed1e78d2-ad8d-3c36-8425-e9fc250ae1d7 | -9.94511 | -60.46761 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ad8bc6a-e5ad-3e56-8ab7-b270170ec591 | -9.94182 | -60.49114 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43da659b-5059-3ff0-a081-cd28f3387097 | -9.65314 | -67.25224 | 2025-08-07 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e57817e-c981-30d1-a278-12937618b4d8 | -9.93776 | -60.45857 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0baf505-dfd6-3ba9-bbe1-c05a26acb37a | -8.90586 | -60.5493 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 310eb905-acd2-3d80-811c-cf9d2ec568dd | -8.91783 | -60.74955 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6b33ed46-767d-3ed2-96ae-fe6292d9a69c | -8.90641 | -60.54556 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc1b9899-091e-32f3-a532-fd76b3633be2 | -9.93651 | -60.49841 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8574707f-d106-3e63-8bf9-9a65d25605f9 | -8.90343 | -60.59481 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa2e00df-7f1d-34d3-b51d-0e3f6dfd7346 | -10.05576 | -64.99842 | 2025-08-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c746648-e0f5-3925-92f6-3049764b7916 | -8.91413 | -60.55051 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aff4e6c-04fd-3f1b-bb2c-342c7cd3325c | -8.90569 | -60.59743 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb1e0995-ed4b-37be-9e22-f511a88354fc | -8.92165 | -60.6036 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5917d7d-cfa0-3d58-9003-af5d7d74a529 | -7.40039 | -60.01067 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 0282476f-bb6e-36ed-9241-a686ca71bfc0 | -8.90453 | -60.58731 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69e82199-8930-388e-a17d-5e515062a7c6 | -8.91603 | -60.58359 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ded8d423-ef29-30ef-998e-3317b4b1d5f3 | -8.91607 | -60.56607 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a72ccf48-5dca-310d-97f7-9e8c71fff3e5 | -8.91659 | -60.54927 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d314f32-dc20-38d6-a256-ac7cc1d34487 | -9.94198 | -60.45917 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a173bacf-274d-3339-a449-3483e7108497 | -6.76032 | -59.48276 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31bff3e3-deab-3ae9-9d93-4ce9d60b938e | -8.92124 | -60.54613 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cf040a0-0ac4-348a-a1ea-925adb45b8a9 | -9.94127 | -60.49508 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5530b7a0-8a86-3066-81b1-c0d7990d8812 | -9.92877 | -60.46135 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d05a96c3-3dc1-3f44-b7a2-8e73f1c92471 | -9.70826 | -61.2943 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6d7e3e1-9f5c-3436-b768-d456503a7b4d | -9.94456 | -60.47152 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a44fb77-22f0-315e-bd93-a1adff51840b | -8.91089 | -60.55993 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de16f8ed-1cae-3b55-b32f-7132fca9280f | -8.92191 | -60.75011 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1fb6df8d-3355-3956-8783-7217681d8abb | -7.4124 | -60.01643 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29d41fbe-9d8f-333d-bef0-76b0c8de10ab | -8.91443 | -60.57724 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 144e6888-a8dd-342b-8fbe-99f3ea658a65 | -9.93962 | -60.50688 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e0d6ddf-42ea-3c3b-9ed6-d059c2c8946e | -9.93541 | -60.5063 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d6ddfc93-a768-3bd7-a88b-ea7cbb65eb71 | -9.93285 | -60.49391 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 032e1478-d110-3a51-9900-022b78658bb5 | -8.91881 | -60.54739 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| deb6caee-ce35-351e-8c73-a7eb8c07614d | -9.92863 | -60.49334 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69c4fa81-9a8f-3e15-b5f6-b103dff5c40d | -8.91248 | -60.56176 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bfc7eed-2fa5-309b-a6cf-374dd9c46081 | -8.90835 | -60.56115 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de4b4622-9310-39e3-baeb-5249357ba7ac | -8.91502 | -60.56054 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f162409f-7cf8-3e50-8655-19e57b28cc08 | -8.9168 | -60.75684 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ea55ea61-8696-3ca9-acdd-239c0450b372 | -5.87589 | -57.75257 | 2025-08-07 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2afbcde4-4dd8-395b-a352-5f97147ac4d9 | -8.92217 | -60.59984 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0f3306f-5592-3788-920d-d1d9919f9a62 | -8.92072 | -60.54988 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 727d6f56-b84d-34ee-9500-f67e349d35eb | -7.43334 | -60.01959 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b3cc06a-d925-3d47-b095-7b065e27b145 | -8.91245 | -60.54867 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60892406-aad8-3014-b44e-75792b644c33 | -9.9398 | -60.47484 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcf0ba7b-5fb0-3d20-9c77-7a718406be5d | -8.90508 | -60.58356 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8014391-cb9f-3cfe-92f5-6726b5b671e5 | -9.71076 | -61.30525 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9286826-1889-301c-b975-58ee34127762 | -8.90618 | -60.57604 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0ec488d-f369-3811-b2e4-8f84912b16d6 | -7.40931 | -60.00816 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |


[Clique aqui para ver as próximas entradas](README25.md)
