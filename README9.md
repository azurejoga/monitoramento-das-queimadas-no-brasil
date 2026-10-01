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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b4876df-e7a4-33dc-9d60-b582ccb10856 | 1.96712 | -50.86915 | 2026-10-01 00:20:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 1862b790-b1d7-33e5-88e1-90cbb70b9d27 | -3.03741 | -53.88598 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5c66565b-ac1c-3428-accd-97a5f47af4d6 | -1.08623 | -54.10934 | 2026-10-01 00:20:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 83e19539-f095-3f2e-bf72-a46556602c94 | -1.85041 | -50.82381 | 2026-10-01 00:20:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 569b0591-6db2-3990-bda5-47f6f35227b0 | -6.64638 | -52.6062 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15de527f-e0a2-3993-a8e5-ac8e9c87e071 | -3.87815 | -50.66273 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 28e0d47e-4fd0-3f68-865d-d7fc252731ce | -6.1398 | -53.06565 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3a7dd9a4-8ceb-3d27-963d-6e9f7baa770b | -7.50777 | -55.04315 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a93b9900-5cb1-3802-b232-3ad738f02046 | -2.49457 | -56.91267 | 2026-10-01 00:20:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0c2fb8c0-49a5-3289-8010-a0a150450b63 | -3.16949 | -54.10815 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3798792d-d024-31d3-9a82-1c96c046c6e0 | -3.22428 | -54.30841 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 120c0634-9435-3909-b8c3-636a24c6e92f | -3.00601 | -51.07208 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9a9281d9-3d92-30a7-9844-ae8533e5354b | -4.05538 | -51.1053 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 44b2216b-c6ae-31fd-b04d-a17877a8834a | -2.9089 | -51.31227 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 41f0d3b4-8d94-35c4-af62-d8c416003ab2 | -3.82551 | -55.80363 | 2026-10-01 00:20:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0cc11a74-9930-3cc0-8f50-c8475d7f8e86 | -2.44133 | -49.21468 | 2026-10-01 00:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d0fe7b69-1b16-3ad8-8546-26dbc4f86b66 | -7.3435 | -55.59858 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 5ea5e163-7caa-3926-850a-414e6fd32206 | -3.68892 | -60.53478 | 2026-10-01 00:20:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e64e9f3b-a427-33c0-b918-7caf4d02b9e8 | -3.06763 | -54.37854 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bff212f7-bebe-306f-9ef1-a1744722d04a | -3.11777 | -50.26449 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 7713ce78-ecd0-34d1-9607-824d6a67e9fc | 1.78801 | -55.65378 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6fc09173-4b56-39cd-9f29-25bf2bf02b3b | -2.93107 | -54.18693 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 80a0790c-e010-30fd-ae67-8ffa9bdce8e8 | -2.89851 | -54.08243 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0ac9aa6a-aa8c-375c-b592-d757483c64c0 | -3.30096 | -53.85838 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 66b7e8b4-d956-3364-9e4a-f10bc9a580c2 | -4.12343 | -53.80651 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 3520bf8e-9cd0-3a8a-bcf0-c7604f70cf1c | -3.7988 | -50.60057 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 972f709d-796b-3820-9d97-fbd986dd66c2 | -3.47929 | -54.69097 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a6a6af68-6481-3f26-949e-ca06b551435e | -5.86808 | -53.49838 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 9df1e56b-7ecb-3e7c-ba75-680450ee5bed | -3.73292 | -54.65487 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a4fab35e-6198-399e-a37e-e2b4e0f42ef5 | -5.75353 | -55.75505 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 67908371-93b8-358f-9540-e508e852e89e | -3.16825 | -54.09923 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 303.8 |
| 24c26ea2-5129-3d80-9b9e-7525485f25fd | -2.99416 | -54.90517 | 2026-10-01 00:20:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 731d5de1-dd99-3a8e-808d-1578a9919f13 | 1.7259 | -55.97499 | 2026-10-01 00:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 16c69eef-8203-38ef-83c1-83f7c6d33b11 | -3.57626 | -51.47639 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| c7d6d3f1-cc5c-3f3f-85e2-68fcc7a3d8ec | -3.86518 | -55.8195 | 2026-10-01 00:20:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 34fe5271-9c52-3fda-b4cd-8edf1029b974 | -5.11703 | -56.01921 | 2026-10-01 00:20:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8e12a07f-4fc0-3a97-9d7a-4d1bb6d21b23 | -4.04283 | -54.22861 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 01ec4657-9e18-34f3-9d57-a2742ef26374 | -3.26727 | -54.27813 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5f2cee09-07c1-30a6-87e5-58daff46397e | -4.16538 | -48.89987 | 2026-10-01 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| ae8848c7-95cf-3ea4-a8c1-310fb16f8084 | -3.2255 | -54.31728 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 38d41fd7-e0f6-34aa-8db6-22777a9bd8f9 | -7.035 | -50.75663 | 2026-10-01 00:20:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 900fb0c8-fcf7-34bb-973f-b6bcbc649bd7 | -3.14927 | -54.0928 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dceb112f-f931-3222-92a9-31ca1c2a3f71 | -2.89953 | -54.15506 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b3fb4af9-62e0-3088-91a8-aeae070c1404 | -1.44826 | -54.45581 | 2026-10-01 00:20:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 014b21dc-b162-31d3-8b3a-54770fbe6b30 | -4.15732 | -48.8946 | 2026-10-01 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 8ee24926-0f63-3525-aed8-102ec3b39dcc | -4.30711 | -50.78553 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 4d40286f-54d3-372b-b7af-4b890e016c9d | -3.01916 | -53.89476 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ab548cec-c90c-3cfa-a984-8414bb86ec56 | -6.01997 | -49.57556 | 2026-10-01 00:20:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ff5d86c3-4180-3b96-8d24-420f52bb4f2c | -3.1067 | -50.26609 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 878543a8-97d3-32ba-b286-ac8d09458970 | -6.13202 | -53.27715 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7fb12d02-2d2c-3627-ac31-d090181abe19 | -5.86684 | -53.48949 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a2488d1a-0e5a-36b7-b424-ab5ee1fef063 | -6.69997 | -55.05621 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 91809d8c-2d48-3c1a-946a-cf7719747131 | -3.01149 | -54.23311 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| abd785ef-9c96-388a-8c26-4a1515bb9855 | -2.9106 | -51.32441 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 30a61be6-4e6a-37c1-8b5d-4b6711ed0e40 | -2.98824 | -51.02314 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 6825f44c-cf86-3d92-972a-57d5b2bb9b5e | -7.04163 | -50.73193 | 2026-10-01 00:20:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 596758b8-6383-3a9f-8e14-cb3ee8c47cf8 | -7.55256 | -55.03096 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 831a919e-954b-3a4c-999b-45614479e340 | -2.9323 | -54.19582 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8bf88b2a-4f23-3d14-bb05-1e2bf8dce1d0 | -4.27217 | -50.76487 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 614.3 |
| 40c426df-a0c4-3701-a70e-d8dc54c78222 | -3.79908 | -51.02346 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 9d592e00-5a29-38a5-a270-5acbe7ead0ac | -3.25838 | -48.77451 | 2026-10-01 00:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a381ba1f-2b6a-30a6-9bd1-f436424531a9 | -6.16048 | -57.70267 | 2026-10-01 00:20:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 42786e44-554a-3f17-bb75-31349d3a73f3 | -3.69127 | -60.55247 | 2026-10-01 00:20:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 78ae2cf2-1963-3932-8715-52bbb99ade7d | -4.3035 | -50.76018 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 98c375d5-803a-36cd-957a-566d53ebd6d8 | 1.96926 | -50.85357 | 2026-10-01 00:20:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 61bf1f47-d274-3dba-bf66-c4fad7f7e2be | -3.27178 | -50.70015 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| da2006f9-d802-3fff-bf85-37baea5b8968 | -3.14759 | -53.75382 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b6aa7d64-0b73-3abd-bfc6-df306376b412 | -4.04525 | -54.24616 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 52ce460c-2955-3925-a092-5ae50eb7528b | -5.85991 | -57.74932 | 2026-10-01 00:20:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7b847187-8308-37e5-8db8-87bb21f9d244 | -7.71887 | -54.76488 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cb10f059-c41e-37fe-85eb-a2031d7ae309 | -5.96932 | -55.37875 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8e4734b6-5b77-33ea-badd-33be87cdd569 | -3.95644 | -49.06749 | 2026-10-01 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 43287852-67bd-353c-8eb6-fb1fe13a03dd | -5.8716 | -57.75987 | 2026-10-01 00:20:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 50ce7de4-4e1a-32bf-ac56-816480e3d294 | -3.5624 | -51.4631 | 2026-10-01 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| c909e1e9-1f17-3bcf-9907-24eab813a4a0 | 3.2742 | -60.6105 | 2026-10-01 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 139.0 |
| d20bb587-5ae5-3d7b-a80e-02add9de9c1a | -7.108 | -43.1497 | 2026-10-01 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.5 |
| 7f547ac4-538b-3782-b319-fb7116186a22 | -5.9993 | -49.566 | 2026-10-01 00:30:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 4e60c9bb-deb2-34da-ba2a-7a37eabadf84 | 3.2924 | -60.6101 | 2026-10-01 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 9a578886-3c3a-3413-ae94-bb31f5ead3d8 | -11.791 | -50.5021 | 2026-10-01 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| bb5d84d9-ba62-3df3-9aa3-7576228a48a8 | -9.0047 | -65.6801 | 2026-10-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 3a8e849c-c537-3bfb-8916-4226c0017232 | -5.7355 | -43.2916 | 2026-10-01 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 247f5943-a6dc-3eb1-bd40-414d0dcee2af | -4.1667 | -48.894 | 2026-10-01 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 8c52d9ae-0632-3db2-9acc-cde45e6bb13d | -8.986 | -65.718 | 2026-10-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| afcde683-dc0b-39bd-a2be-daa52c0de484 | -6.0179 | -49.5648 | 2026-10-01 00:30:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| d0e8a0d9-c01d-305c-b01c-8f49a1e7072c | -3.1572 | -51.3515 | 2026-10-01 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| eda6fea3-e91b-3041-8665-1e1bbca7cb62 | -12.8552 | -44.3389 | 2026-10-01 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 2ec58563-d0d4-3e81-a1c5-9dd99bf619b5 | -10.7853 | -50.5279 | 2026-10-01 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 291acdbe-4979-3083-8ea2-1f42707aff86 | -13.0772 | -51.224 | 2026-10-01 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| cd98f6e8-9828-38ab-9b04-a936cc0225b9 | -13.6671 | -53.9314 | 2026-10-01 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| ce6849bd-f3fe-324c-8459-56dbb8fd74fc | -8.5738 | -66.994 | 2026-10-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| b0dfa98f-daa8-35a4-a07b-143b4397d988 | -13.6479 | -53.9336 | 2026-10-01 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| cee05305-5da9-35a7-ad6c-52465e798735 | -7.1269 | -43.1479 | 2026-10-01 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 77c2107a-792c-3101-b822-f587671c5eb6 | -3.1061 | -50.2686 | 2026-10-01 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| f5dc6e08-1391-3e74-9f50-52a883425683 | -13.0776 | -51.2027 | 2026-10-01 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 20c7a850-70a8-37e7-8415-7f06628c803e | -8.9861 | -65.6993 | 2026-10-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 9ceb550a-f08f-3276-8500-d435ad044b00 | -3.5623 | -51.4838 | 2026-10-01 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 198.0 |
| ff4bbebf-d496-3854-99fb-26e71d4831dd | -13.0584 | -51.205 | 2026-10-01 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| ffa89403-3006-3a35-80ce-3b6b041bbe2b | -6.9317 | -59.2798 | 2026-10-01 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 22f8da38-1f6f-3997-8823-a17030d7cebb | -14.9721 | -49.8165 | 2026-10-01 00:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| c117d203-5bdd-3157-b29f-7d19ddc7ef85 | -3.1245 | -50.289 | 2026-10-01 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |


[Clique aqui para ver as próximas entradas](README10.md)
