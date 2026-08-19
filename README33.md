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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1c9cca9-d3e8-3310-9aaa-4c55600f2698 | -6.01424 | -50.19427 | 2026-08-19 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bd543d3-227a-33d8-a9a6-fcfc1812f3e7 | -6.89103 | -56.44181 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e48da48b-bf08-3737-bf13-e8e5f4fbe1a6 | -6.34402 | -54.90278 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e15021ff-2803-3305-bef0-904ca6c82507 | -6.69457 | -58.94568 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d620a4f-0c06-3f0b-86c1-d7eec8c2710e | -6.14197 | -57.8598 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c2e9446-3995-388b-91af-fa9ca8141213 | -7.16886 | -43.10545 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29eba61d-a00a-3c74-8de9-7229736135e3 | -7.64847 | -42.77406 | 2026-08-19 04:38:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 98c782b9-dacb-3470-9ad3-ab2a0a56206c | -6.13583 | -44.91362 | 2026-08-19 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 518f42a1-8b77-30a9-b27d-a0d6fe3247cb | -6.0379 | -57.80729 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04f1445e-35e9-3a3d-a5d3-f9336eb8d318 | -6.79723 | -59.44469 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82088e92-167b-38cf-8ea5-00ecf5fbb2d1 | -6.9917 | -59.05093 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e89c6307-947f-3ea4-921a-ed0fbc7000af | -6.07996 | -57.91769 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b33ecd31-29e5-33c6-a9ba-742eef66dc7e | -3.68153 | -47.65016 | 2026-08-19 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5d3f79fc-ad47-3b1e-af7b-685fe0ce1bc3 | -8.35081 | -44.79094 | 2026-08-19 04:38:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5fb0b0d-eac9-3173-b633-f2a37a487646 | -6.44534 | -52.73416 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 239275bf-86f4-3cff-950c-90d0376b56f2 | -3.05526 | -46.92739 | 2026-08-19 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 912034f1-1a4a-3053-9532-77bf63039417 | -8.10701 | -51.66515 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b88c01b-4706-3386-9c16-516c5b9c836d | -8.17557 | -44.43498 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eed7d965-cdd5-3546-80dd-c7acdba5b5e2 | -5.99968 | -57.86143 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2bf547ce-13e7-3685-a64c-d5b68e62828b | -6.78417 | -59.44723 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e248535-6c7a-34ed-8f3a-cace7ffa6847 | -6.33779 | -54.90902 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0446d897-98d8-3487-8d39-c34b4413f8b3 | -6.14358 | -57.88359 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 073d1fa5-5952-383e-a6a9-a5fa886a8d60 | -7.18675 | -43.45497 | 2026-08-19 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cedf04d8-e1c8-3f1d-9fe4-8491e5346b9f | -6.00386 | -57.8704 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ab164f5a-ea54-3f9c-bfd1-cefd99a0cf02 | -5.43216 | -48.4166 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 83344154-0c36-3de7-ac6c-458849ce439c | -6.34321 | -54.90741 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6220a94d-33fe-3c5c-ace6-3ed4e1a5d09f | -6.7376 | -59.04494 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88b6f35a-788d-373d-89aa-913e1818ce55 | -6.13832 | -57.84782 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43ffd4ff-2bb6-3e9d-92c3-3ee5bfcc294b | -6.34389 | -54.90058 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71f7405b-0f48-3c29-85a0-5a8d06b61cf6 | -6.10168 | -57.86019 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25e6bd6b-45bf-3af9-be0b-b9f69fb8c82a | -5.91537 | -49.26194 | 2026-08-19 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30498e13-e888-3777-9851-578e86412c4b | -6.27385 | -55.9726 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb3aaf1d-7947-32d8-9c9b-1fbb148707f0 | -6.2343 | -43.68757 | 2026-08-19 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d6c2d06-a948-30b0-a400-bd85eb9c3364 | -6.44784 | -52.71915 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17c7b4be-8da5-3867-a6ef-65e852c9a142 | -5.92397 | -43.61872 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd571a81-e4aa-3a23-8af6-91b9e3f4971e | -4.43247 | -46.13682 | 2026-08-19 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ecb5b8e-a38e-361a-aae3-7e5615c77d86 | -6.08485 | -57.92268 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 10fb99d4-3795-3369-80db-6fc12347a348 | -7.09972 | -55.45247 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d59af1d-95c8-3c15-88a0-25f2ce6863ed | -6.88338 | -59.05411 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7af6f307-5237-3fd3-bd29-e9fbe73907ba | -6.44617 | -52.72916 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f476efa1-3284-32c8-88d2-7d631063f637 | -6.69374 | -58.9501 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd539880-5e96-37d7-8e68-3ece11968e0d | -7.53603 | -55.59891 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd4847b9-7c21-3d1f-aa50-0ca5edb7551f | -7.94492 | -44.63387 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 687dc1ef-9bcd-3166-84be-7c02298c283b | -6.87558 | -56.41242 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51e8a6e5-710b-3333-bf70-8d191219fbeb | -8.3586 | -46.36362 | 2026-08-19 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35d9eb01-bbec-3730-87ac-8c8bc1576797 | -6.75344 | -59.16181 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6eafd45a-e242-310a-94d0-1455a20012d7 | -9.11689 | -46.04143 | 2026-08-19 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9b48bb5-17e5-38b0-aaa4-4383f811931b | -6.40506 | -46.63369 | 2026-08-19 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80f3c393-3e0a-35fb-8b8f-115bea2d8a0e | -6.26717 | -43.27686 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f3cce0a1-92e4-3631-b791-5fa83a0c07b1 | -3.09616 | -61.22423 | 2026-08-19 04:38:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6efa57cf-6aa5-39bf-b3f3-2400425e428b | -6.69755 | -58.94379 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 47dcec75-6bff-33d5-9571-02b468da51b3 | -6.08615 | -57.91532 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 62073002-40d9-32bb-b902-c775e4b6315a | -2.8242 | -52.29763 | 2026-08-19 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b66deb1-e7b8-33db-925d-7cb084fa70d8 | -6.03855 | -57.80353 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70b3ed57-238b-3966-8cec-05c8ea488e1d | -6.89154 | -56.43894 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a1660e5-8f93-37b8-b493-7062419b7175 | -5.90855 | -43.61642 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 38f245f8-20ad-350a-812e-62b185479d70 | -6.30498 | -55.71206 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dced0205-1517-37d3-a789-362668a2a766 | -5.85225 | -57.53933 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cae89cf2-1976-3ece-bc3f-4c7ce6a45336 | -6.78941 | -59.45305 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8f52316-edf0-3efa-b4bc-b91c464604d3 | -6.69599 | -58.95256 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8267d68e-a6ad-3c5b-a1cc-2b1ea8189a87 | -8.49408 | -48.81809 | 2026-08-19 04:38:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59c09841-0ed5-3ede-a73f-4efb70869bd7 | -7.09884 | -55.45736 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02acb1ee-a293-3024-8403-b52f4eeb9bc0 | -8.08245 | -44.35826 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af185c99-c753-301f-8579-c8caf6853134 | -6.6886 | -58.94488 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70bb9c43-2736-326a-82b6-3d4e4e7edc62 | -8.5432 | -47.3849 | 2026-08-19 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6dd322d-a3a1-353b-bb00-ab579b3cb0f4 | -6.74818 | -59.15663 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23d60bb0-0896-3e2e-baf2-8d61c7ede47f | -7.24416 | -49.89606 | 2026-08-19 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d9400dd-d0fa-3acc-9f6d-4ea0072266f8 | -7.28586 | -44.07617 | 2026-08-19 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad2708d9-1f87-3e53-aa9c-3f7981f67a66 | -9.11979 | -46.04605 | 2026-08-19 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ba8d697-6cb0-30dd-a0b7-3ae3cf6af68a | -7.01416 | -47.97392 | 2026-08-19 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25237c49-92c6-31e3-b7f4-7d488d97c57a | -6.88666 | -59.03658 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| efc6b287-dfec-3522-8e91-a9027869f2b9 | -6.00525 | -57.86247 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9d3f6737-fd76-3318-8b37-42c5990b2c88 | -4.71104 | -47.15605 | 2026-08-19 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 97b4550d-add3-3ec1-b576-aa99f1cbf049 | -6.00914 | -57.84037 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27fa62ff-4867-3bd8-a8b2-025b0dd85062 | -5.99536 | -57.8533 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87be1b92-a6b2-32ed-b7a2-249c8d242ea6 | -6.35313 | -54.90423 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31a71e1f-a234-3560-a286-55985fccb944 | -5.92638 | -43.62893 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4435fc5-5051-3bbe-8f46-c350e3077922 | -6.90149 | -43.2496 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 908a5694-3c32-3d75-b2cb-240379f0f521 | -6.88604 | -56.44088 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45152e04-1b31-3f76-ab63-c8daedd95caf | -6.88705 | -56.43511 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ac1b6b7-fe41-36dc-a34d-68fa6cf03938 | -6.70491 | -58.93678 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2cd17493-beff-3913-a89e-351e0204b367 | -6.80833 | -59.4537 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8df3ca97-70db-39ff-b431-d3b774710a65 | -7.44902 | -45.14793 | 2026-08-19 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6dc42a2a-926b-35f1-9fe6-b51eb2bc8be4 | -6.69697 | -58.93279 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf043da2-a7f0-3b99-ab32-25247ce2b8f2 | -6.74494 | -59.17462 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86747e65-2b55-3053-b97e-cc349840a167 | -6.0059 | -57.85883 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 07a83a73-4f9e-3453-9010-6ca2350d2442 | -6.76333 | -59.45778 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42ee3d82-d85a-3989-b2c5-404451c67886 | -6.83994 | -44.94902 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6217b1c-f1ae-3b8f-882d-6407dcf9f3bd | -7.10289 | -59.77086 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0049666f-f852-3cdf-82a5-f4d9619a1bf5 | -5.99602 | -57.84955 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74c77b0d-7103-33b2-9514-9092d8e50526 | -4.27813 | -60.85509 | 2026-08-19 04:38:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c91546cb-1072-3829-bacc-2cf89b83ecf9 | -6.8588 | -59.0375 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cdf97ec4-c4e8-3fa2-adcc-d3622919758d | -6.85528 | -59.02319 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 972137ee-d07a-36d4-ac4f-b8953ac5af89 | -8.3638 | -46.3528 | 2026-08-19 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64725358-678d-343e-ac60-5767d616aeca | -6.7677 | -59.15131 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c570ccc1-2f3c-328a-8c46-728876309496 | -4.45716 | -55.45892 | 2026-08-19 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6854c796-b84a-316d-a12d-813863bcc773 | -4.01175 | -48.90582 | 2026-08-19 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5ad5ae8-a93f-37d8-8a3b-a8ee3e64e6d5 | -6.3424 | -54.91202 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5ceff53-e6e5-3932-930d-e058591dfb9b | -6.34156 | -54.91447 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9774ef59-be68-32d2-8352-f3f28452c1c0 | -5.85163 | -57.54286 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README34.md)
