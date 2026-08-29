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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a27978b-1f6d-3803-9e7b-576bfb85d5e3 | -6.6317 | -43.73 | 2026-08-29 12:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 99da7586-e56e-344c-9937-58982dbb3922 | -6.7884 | -55.6635 | 2026-08-29 12:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 0b64447e-932d-3b54-bcc6-2d56dc2e15b5 | -13.5991 | -45.772 | 2026-08-29 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6e5339d6-9ad1-33e3-ba85-eca76846dc52 | -12.2093 | -50.5386 | 2026-08-29 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| a609f35e-8643-3909-9480-f70814137e5a | -6.7885 | -55.6436 | 2026-08-29 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 310b3151-643d-3c56-b415-be3cb386553b | -6.6317 | -43.73 | 2026-08-29 12:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 237.6 |
| cfa93911-e498-3622-ab79-7918f7453a02 | -6.7884 | -55.6635 | 2026-08-29 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 09395985-f33b-3aa0-9ee8-f56899ca8e98 | -6.6315 | -43.7533 | 2026-08-29 12:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ce2ff6b4-05ae-3650-bef8-0242a32fe5f8 | -12.9221 | -45.8582 | 2026-08-29 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 84bf8346-83ce-3f37-b076-e30f0d00cf86 | -6.7699 | -55.6644 | 2026-08-29 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5d9dbbb4-dfbf-3723-a132-eec7f606c373 | -6.7885 | -55.6436 | 2026-08-29 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 5b3aa6cb-7e08-3b11-8450-cb491c27fd16 | -11.1726 | -51.2728 | 2026-08-29 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b921013d-4042-3bd0-ac21-9322d2a71a8f | -7.3479 | -55.1544 | 2026-08-29 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 57b46b5d-40a3-3164-9d42-640503f79067 | -7.3478 | -55.1744 | 2026-08-29 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a1c3afaf-baa1-35f0-a791-b61b366ef602 | -13.5991 | -45.772 | 2026-08-29 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0baf1c5f-5aa3-3d13-b777-5b8cac93978d | -6.6129 | -43.7317 | 2026-08-29 12:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| bf2d55d5-662c-396f-b703-ab9e847c1aa7 | -6.7699 | -55.6644 | 2026-08-29 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 6493b89f-9d24-3984-9ba5-22fa9decae08 | -12.9221 | -45.8582 | 2026-08-29 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 19354f9c-9a0d-3d77-be8c-64bbf10ac01d | -6.77 | -55.6445 | 2026-08-29 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 0a069dbd-711e-318f-b078-a68c7bd7caec | -20.941 | -57.5694 | 2026-08-29 12:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 3d4b4b10-4d32-3c1d-8eb4-f356a0f46bf2 | -12.2093 | -50.5386 | 2026-08-29 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f43eb6d7-3e99-3c52-9e39-e3457dfc3ec7 | -6.7884 | -55.6635 | 2026-08-29 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 42e07956-d40b-3a7f-a716-e02637f0b78b | -6.6317 | -43.73 | 2026-08-29 12:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 289.9 |
| 7b04cc8d-8ddd-3dfd-94bb-35a237b16dae | -5.982 | -57.6697 | 2026-08-29 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7a431816-f71c-3887-9524-89344819d2f2 | -6.27639 | -53.14218 | 2026-08-29 12:29:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b23407f3-03be-32a5-93f3-4bd29106a330 | 1.81943 | -56.05208 | 2026-08-29 12:29:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b1c98727-8262-32c8-aaae-4543a027ef18 | -2.82531 | -56.8618 | 2026-08-29 12:29:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 375601e2-36a8-3d0a-9142-af1acba61085 | -2.29987 | -55.24266 | 2026-08-29 12:29:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 90e0b0f3-a366-311a-855a-21abbec86626 | -5.89626 | -57.75883 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| cf772ab4-7e48-3970-a356-41807f9c5415 | -1.36373 | -54.63267 | 2026-08-29 12:29:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 645b62dc-e710-3c8a-aeb2-dda1f0ae41b5 | -5.88616 | -57.76643 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b58b361d-3197-3338-bbe7-bdea55e4122d | -2.2905 | -55.24139 | 2026-08-29 12:29:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 915a1383-d40e-3180-bff4-b795ffa21fbd | -5.14792 | -56.2729 | 2026-08-29 12:29:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 488843f7-5ad3-3931-9ab4-0abd03fa5078 | -3.61352 | -60.53795 | 2026-08-29 12:29:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 15f2cd66-4c03-3e0b-be71-5e283cee2c24 | 2.13331 | -50.9229 | 2026-08-29 12:29:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ef61581b-5ee3-3339-8eaa-d52b0e959865 | -5.97958 | -57.69504 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1c169a14-5f2f-3b00-927f-dcb67a9cc348 | -0.53911 | -51.80571 | 2026-08-29 12:29:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e753e35c-ecab-37eb-9e3d-fb504f886e86 | -3.52733 | -59.03886 | 2026-08-29 12:29:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f97a46d1-b287-30ec-ae2c-c9c115f603c7 | -5.85205 | -57.75269 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d288b22-266e-34a6-9bbc-57e2ec0b5eac | -5.9821 | -57.67729 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 20a66da8-f994-3482-bfa7-d266a078c166 | -2.50019 | -48.35644 | 2026-08-29 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| fe538b27-20a9-39b7-92b0-983b7f68cae5 | -4.97914 | -56.29584 | 2026-08-29 12:29:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f390cbb8-84f5-3ba3-9cc8-9cd8cfb9ca63 | -5.99095 | -57.67853 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2c458a10-53ec-3c95-8cca-e36bbc1a3f71 | -2.9944 | -48.96593 | 2026-08-29 12:29:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 90f42369-3c7d-3569-afdc-85e87b413323 | -3.52868 | -59.0296 | 2026-08-29 12:29:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a29b4a9-3ef3-3358-91ea-37809a6823bf | -2.51339 | -48.33146 | 2026-08-29 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 3a62d30c-5bdb-349b-8c94-cb9f96341e01 | -5.98084 | -57.68618 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| e607d524-736a-372c-9526-57dad9a6cfe5 | -5.88742 | -57.75761 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 1b09f989-04a5-3ea5-9f0d-649ea230819a | -2.99855 | -48.9361 | 2026-08-29 12:29:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 9c388e93-6e5e-35f2-9e64-1347b0f6916d | -5.98969 | -57.68739 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 21290a23-cda1-32e7-abee-9e78087b0f76 | -6.64623 | -53.18877 | 2026-08-29 12:29:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 98721e57-8931-35f8-aa32-2563e57e93d3 | -2.52069 | -48.3258 | 2026-08-29 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 80f514e3-9f0b-3cb8-a54a-ab5b2fb8e010 | -2.99478 | -48.9425 | 2026-08-29 12:29:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| afd37e7e-2756-348d-927d-22096a29ae32 | -5.89753 | -57.74995 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 7d36a621-5050-3ffa-aa07-414034adeb1f | -3.64118 | -60.55294 | 2026-08-29 12:29:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ab73ab0a-bf57-3b87-9ccc-b50cde4d98f3 | -2.50909 | -48.3643 | 2026-08-29 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f144d340-320f-3a81-b142-2b53ba29efb6 | -5.88868 | -57.74876 | 2026-08-29 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bc9c1ce6-b380-3a9f-aed0-69fd14f2b42a | -2.99085 | -48.9724 | 2026-08-29 12:29:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 1ba9c8d9-d751-3b93-907d-d698e53f7803 | 2.13074 | -50.90582 | 2026-08-29 12:29:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5b41c29a-757e-3f6e-a131-2707ded6cdab | -11.211 | -45.0555 | 2026-08-29 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d6415df5-2f78-379a-a583-eef3b0f6c589 | -8.9428 | -63.2797 | 2026-08-29 12:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| dcb17d57-7fb8-39da-b2cc-ef6c4c2d7ce8 | -7.3478 | -55.1744 | 2026-08-29 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| e4dc05c3-abf9-3e09-b3f7-a2d29227b5c8 | -9.971 | -53.9214 | 2026-08-29 12:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 9c07b8ce-b2ab-34fd-bdd7-42239b791f2d | -6.77 | -55.6445 | 2026-08-29 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 9cbaab2d-8b12-3dc2-8e4f-7f1d2ebe11a5 | -6.7885 | -55.6436 | 2026-08-29 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a1cc6caf-14c7-3d5b-b34d-05592de2d6b9 | -12.9221 | -45.8582 | 2026-08-29 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 212.4 |
| d9e7021c-4348-3829-bc9c-b9a5e4a4c54c | -13.5991 | -45.772 | 2026-08-29 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8a6b8572-cd68-3f2c-9f93-d38bf9dfba2f | -6.6315 | -43.7533 | 2026-08-29 12:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 25c2e16e-03c3-3d5d-a4cb-5d3fd8c32fb7 | -11.2302 | -45.0528 | 2026-08-29 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 34abb4f5-0dac-322c-ba9a-0a2a807e057f | -9.9708 | -53.9419 | 2026-08-29 12:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 8d9c821d-e243-34c9-abd1-050bbd6a8f4c | -14.4057 | -50.0537 | 2026-08-29 12:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 64b592c2-93f9-3792-8d3a-0178dc757ab4 | -6.7699 | -55.6644 | 2026-08-29 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| b7afc31e-2950-3e4e-8fef-001662892ea6 | -12.2093 | -50.5386 | 2026-08-29 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f2a50061-532a-3b12-8b76-db42fd19546d | -6.6317 | -43.73 | 2026-08-29 12:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 164.2 |
| c9159463-8753-3d62-ba6e-085e60682517 | -7.3479 | -55.1544 | 2026-08-29 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| cab9352f-8032-3164-b2b2-46bcc9f9a717 | -6.7884 | -55.6635 | 2026-08-29 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 1b0dc7db-b3d8-3474-b0cc-ebfab6cafea2 | -20.941 | -57.5694 | 2026-08-29 12:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| b599cf26-7181-393b-807d-ba603cfe1f1a | -20.9414 | -57.5484 | 2026-08-29 12:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 672b9e7b-2af2-3486-863c-491800e70064 | -12.2284 | -50.5363 | 2026-08-29 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d446f289-f056-37b5-9b3e-1993330fb443 | -6.6129 | -43.7317 | 2026-08-29 12:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8d8ac5f4-5f20-3591-a251-dc72c178713e | -9.61713 | -55.11877 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ac58a409-d0b4-3d32-a6c2-0886e3f20549 | -7.50941 | -55.31139 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 67dff650-8dc2-3985-8cc3-9dc3e9392914 | -9.97694 | -53.92054 | 2026-08-29 12:32:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| d1cf7cc7-2bcd-39cb-a5ad-42f2c74f56ba | -14.17604 | -52.83182 | 2026-08-29 12:32:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 8335dc86-47e6-36f8-872d-5dbb1e5c76de | -6.54935 | -55.23732 | 2026-08-29 12:32:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 826ead28-ac53-3b6a-97d1-c0d8264f760c | -8.53451 | -55.36129 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 177194de-5b4e-3a46-8727-e5cdf0d93c64 | -8.65875 | -49.54609 | 2026-08-29 12:32:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 59b1ea62-bb61-3483-bf8d-ddc9064c2634 | -6.79021 | -55.645 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 2f8edc70-6224-3b58-ac75-c2acff0a1c83 | -9.13032 | -57.57584 | 2026-08-29 12:32:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b524319e-4e56-3621-9749-697176433e62 | -10.87508 | -50.50471 | 2026-08-29 12:32:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 6e712c4c-3994-329c-8a2d-2ca7781bd787 | -10.83232 | -50.49422 | 2026-08-29 12:32:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 3fb6170f-b804-393e-ab22-468c2c1fcc21 | -7.51097 | -55.29998 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 2e03e4b1-2e9d-35bc-aa68-79cf4fe8c8a4 | -11.26934 | -54.02275 | 2026-08-29 12:32:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| f351d942-91fc-3b3e-8d3c-c33e160aec34 | -10.87844 | -50.49942 | 2026-08-29 12:32:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 1af24d5b-945d-31ac-9d89-5831912e6fb8 | -12.88225 | -58.2798 | 2026-08-29 12:32:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 82a69ee3-a40a-391e-8fd0-9898fc3b40f0 | -6.96634 | -55.70282 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| a48e645c-e000-3bf4-9474-efb8368a5676 | -8.53726 | -55.26525 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 81557062-5b64-3f80-84bb-9a04ebe90246 | -6.54784 | -55.24858 | 2026-08-29 12:32:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 51f88f9b-916f-3a89-b359-5720482075bb | -6.60068 | -55.44714 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7b5f511e-7f30-37f1-a396-35bd18d878b6 | -11.02695 | -57.24659 | 2026-08-29 12:32:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README76.md)
