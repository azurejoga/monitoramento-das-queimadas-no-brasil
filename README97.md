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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b3a7575-4c2d-3a5a-836f-18c8803c4d49 | -3.1726 | -58.62645 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da2f7bab-4711-3e20-8eaa-d8b637527c5b | -6.4542 | -55.49884 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35e63d79-29e6-3f28-9f7a-1c6dee50ee32 | -7.05829 | -40.96461 | 2026-10-10 05:04:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4c87a845-66a7-34fc-a775-ffbc04e59562 | -6.85633 | -52.84004 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dedc2f4d-fbdb-3e2b-992c-0d69e927a7b5 | -3.02309 | -54.04483 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbeb1dda-0613-3de4-b7bf-9e80a25feb66 | -2.74982 | -54.09692 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 288f5bd8-33b6-33f7-9cb7-aa26d33ba9de | -4.68526 | -48.52198 | 2026-10-10 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea52b603-45bd-393a-8870-ce8943b1978c | -7.19114 | -55.16335 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a91c7897-b758-34ce-b9cc-69065ede4385 | -3.25592 | -54.67657 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0600162-4f54-35b9-b2c1-7fcf9fbf51cb | -6.08817 | -53.50209 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 753524c3-d5c7-3557-974c-4d91aed8bcec | -2.2398 | -51.92753 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d43d7cb2-e8c8-390d-a065-6eeddaa6faf5 | -3.07627 | -53.96821 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfc76fa9-b0a7-3c5d-a480-44720a51deef | -6.45755 | -55.49937 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eacd9822-453b-34f9-a465-63c303e026ec | -4.59315 | -55.72747 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 21c6c52d-ddf3-3e62-838f-02da95d87ee1 | -3.10656 | -53.94827 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0213faca-2996-3a13-8722-4c356257edb0 | -4.58462 | -54.95088 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6b4622f8-9c46-3c85-9101-e68935736cc5 | -4.12946 | -50.83135 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 020d75b9-7059-3e00-88c9-a071f7516aa1 | -5.96493 | -55.37341 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06d10057-d246-3fea-b5e1-d2ce485c10bc | -1.10392 | -54.16878 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f1afdd7-bace-3db4-a167-6fab91f42f4d | -3.66396 | -57.01075 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79cbbb41-7581-3f50-8c4c-23eefacbcaf8 | -2.48265 | -56.16851 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 451f3053-caa2-3a67-9b5b-261fe6ea0ede | -3.51589 | -54.59877 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff43bcbb-214c-30ea-99b5-18bddeffac6b | -6.12632 | -55.70215 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff98a100-3767-34f3-b80b-a9ffcd5d25a9 | -7.56468 | -45.64357 | 2026-10-10 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60aa1f1b-ba50-374d-af9b-dbbd170051b1 | -4.50684 | -54.99324 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 177fd168-e115-364c-81b0-78803a1e03d7 | -3.20578 | -53.85821 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37e904b0-dbe1-366c-a095-08468cb4b7a3 | -2.48916 | -58.07962 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4963f616-183d-3b21-bb5d-7115a7e5bbcc | -3.69788 | -57.07674 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbd37050-6d91-3af8-8124-6c997ae55cd5 | -3.11019 | -53.79732 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| baf1d598-25b7-3799-b8f0-effbf0def141 | -6.12584 | -55.68364 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc55b950-b845-31ee-b996-8615e8a11c4d | -1.26237 | -55.75603 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 392c2544-c378-33de-b5b2-66175c2585cb | -4.11825 | -54.03817 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ea32b74-a190-3af1-be97-39fb32bcb571 | -3.10574 | -50.31315 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b3167f5-e333-321e-a568-09476ca80518 | -1.20943 | -55.65985 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 273fde4a-28c3-30bc-9e0e-0d28492eb09a | -3.56245 | -54.69217 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6bfe74fe-36a0-37d5-9e2e-d36e4b834d5d | -7.19499 | -55.18188 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb752003-aeb2-3ee8-8530-a3c4e6de53db | -2.47404 | -56.08647 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfa0986b-d428-35c5-b1fb-a027d6cebed1 | -4.32095 | -54.90244 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8249fa5-d7ce-3543-ab1c-8aa7b41f11dc | -2.61459 | -51.70601 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 111f48b0-5abf-3c1c-88ab-2ea767171f6f | -2.55792 | -58.02672 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4d64127-9909-3385-9bdf-751c9c72b53c | -3.03758 | -54.14618 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae94e3c7-acd7-3fa3-9a1b-59cddc552162 | -3.00086 | -53.90718 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80bc5949-1780-3419-8628-e12c280a6f61 | -4.31089 | -55.34483 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28ae3992-4842-34ef-b8ae-fa5a4e42c569 | -3.57189 | -54.69727 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 430ddc28-ca2f-3ad7-98c8-711d6014de4b | -3.37728 | -44.48637 | 2026-10-10 05:04:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5191462a-27b4-3d7b-bfdb-32f9ceda2637 | -2.52001 | -58.08652 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff735220-1445-3ecb-b700-fe6ca6614bf0 | -3.11539 | -53.95671 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb7f3de0-a8f2-3286-9155-675d15ea7c72 | -2.95751 | -54.13714 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 905165a4-7c3c-32d2-af09-1708fee84219 | -7.08484 | -52.67488 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7092bec6-5696-39d7-81ae-120a1adc7aaf | -4.60826 | -49.20539 | 2026-10-10 05:04:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a54be78-b1a7-323f-af57-49b9a4c78174 | -6.44495 | -55.28398 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 411d4dbf-c78e-3451-afc4-79b5466cfe64 | -7.02569 | -47.66232 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 528df857-238b-36d0-a0f2-106d680f0b2a | -6.37134 | -55.16797 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1466613a-0e87-3890-bd7d-c5bdb4ea404b | -3.12559 | -54.17042 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a473e8f7-ddbb-31bb-8ab0-efb0f8d88249 | -3.51944 | -59.94754 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24bb17eb-109d-3650-af64-2dd3e4f9e028 | -6.4234 | -55.20502 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 622bbfa1-7cc9-39e2-bb6a-23f5079f0c0a | -5.79385 | -53.79829 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de6ae9ce-cfbc-3094-a0fa-988dc35ffa41 | -2.99379 | -57.7599 | 2026-10-10 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56d360b8-d1ab-358a-a27a-c4f88d11fb0a | -3.98633 | -59.36369 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| adfa5e84-69fa-397b-a2c5-677369613bfa | -3.24626 | -54.03029 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e77214ab-ba9f-3ad7-9199-72b08c17442d | -3.43425 | -54.53643 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5f5da53-b672-31e2-88d4-8d4caead4260 | -3.00249 | -54.77357 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abd2e91e-ceb7-3fc4-9d61-693f9c7ca757 | -7.08984 | -55.73197 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 378ac01f-f0e0-3df5-8753-4d434e4935ac | -6.48404 | -55.96704 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff4d5909-3755-34ba-9938-e24103e5fc61 | -6.53355 | -54.9187 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e6cf774-9eed-3173-b9e4-a40d86c0eb1c | -5.38485 | -56.06031 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96b5358a-dff1-3340-97c7-9fe01c3a4dd3 | -2.42821 | -55.99118 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ea7d894-3164-373c-b56b-88059c721697 | -4.4014 | -49.78106 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 660de03d-945c-397a-a84e-96cbeedf5fe0 | -4.19143 | -59.40868 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81bedae3-15fe-3d44-90e7-6021bfd4bfb5 | -2.41829 | -57.99702 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f870e858-03ac-3d11-907a-335ef08046ea | -3.26229 | -54.05753 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0524d3b4-7529-3b3c-acb7-c25535364ab8 | -4.1625 | -54.33821 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c25367f1-7995-30ac-bc65-5d8780591c45 | -6.80514 | -52.78395 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed125e36-ee94-3b9a-963c-a17d02fc22e1 | -2.86702 | -54.17244 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 661d4ffb-e7d0-3627-953d-e8e870ca53ed | -3.20083 | -53.868 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdb6b3c7-86cf-393d-9b66-0732b1f75dcb | -5.74734 | -45.13249 | 2026-10-10 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a7aff70f-7f5c-3f42-bece-eee216fe6e84 | -3.31243 | -54.68175 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca1ceef9-0598-3060-91ee-b7728e2db348 | -3.02062 | -57.78008 | 2026-10-10 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6570842a-524e-36ae-b6ff-7fc0d515e38e | -7.18571 | -52.63343 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e093247f-7b24-357a-970c-5ac28855c9c9 | -2.98979 | -51.04648 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6123341b-097e-3ff8-a556-825260ddb4fc | -6.38288 | -55.22366 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ade2a0ff-1c67-3c8d-b35b-a01db98d53f7 | -5.79661 | -53.80227 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efcb5919-95db-36e9-9461-3e0d29d39227 | -3.38955 | -44.47775 | 2026-10-10 05:04:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cce8732-cfa0-3a02-9f0d-d4b98f3fdbff | -4.0973 | -54.02076 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb9f184f-5b94-3ce8-bd9e-5c63ccb571ef | -7.0592 | -40.9576 | 2026-10-10 05:04:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6db83b2e-b69a-3241-b81f-cc76b88f9761 | -3.21756 | -48.81587 | 2026-10-10 05:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fa024f8-3bbc-337f-bb49-1091994fbcd6 | -5.95998 | -55.34007 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc212005-f9b6-3726-9601-649e86cb9f9d | -4.31324 | -54.80049 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1cb0b37-b6a0-3793-88b9-8295f1342098 | -3.29796 | -54.68667 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d9c4518-e607-37f4-a862-31d4ccd5a399 | -4.12676 | -46.86724 | 2026-10-10 05:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 675fb3e0-dbe5-3e51-b842-f5b1b9bf7276 | -3.57666 | -58.63161 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2de88e65-9e52-39a1-8945-e10a2d6f094c | -3.31555 | -54.17246 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2055673e-30c8-3425-95a0-a7b7cd5171ce | -3.25815 | -54.66251 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52bb394f-2356-3ed9-a815-4d6a556b502c | -3.94762 | -58.83945 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9a54182-4f6f-31d2-8c83-6080fca03c1b | -1.4381 | -52.83282 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8598f68c-efd9-367f-803b-010f4c4fed75 | -3.04332 | -54.26036 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9559fd4-b57a-398b-9449-73242851989c | -3.77593 | -58.58981 | 2026-10-10 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c589006f-490f-37df-b59e-894f2709a64f | -6.44407 | -55.03283 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 153883a1-36d4-3cfa-9765-519d9a2eff4c | -2.92607 | -54.12148 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a653cee-2e8c-3124-b744-b995877189cb | -3.71942 | -54.21855 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README98.md)
