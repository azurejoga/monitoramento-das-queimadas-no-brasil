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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01f4bab9-8b59-3327-ab00-8dfe4bd9fe53 | -3.30865 | -50.15774 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bcdddc1-c030-3a36-965e-383734de8244 | 1.26014 | -51.26909 | 2025-11-10 05:37:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42f10de7-3c97-3b5a-853c-68fad63dc2e0 | -5.153 | -50.87567 | 2025-11-10 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5627384e-4409-3b6f-9fff-b7b0add44baf | -3.14998 | -54.98726 | 2025-11-10 05:37:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4c86fad-b6fc-3df2-859d-a04d112b5291 | -3.59317 | -55.4607 | 2025-11-10 05:37:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5370d461-87ab-3bd9-9541-13fe464760c2 | -2.64508 | -54.81698 | 2025-11-10 05:37:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b06ab143-27f5-3a0a-b803-f166278fb342 | -4.20879 | -50.62763 | 2025-11-10 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fd018b61-8ffb-3f61-afe4-40f74a78725f | -4.20129 | -50.6321 | 2025-11-10 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4d4cd039-a785-3d0e-881e-19a0a5edb450 | -2.93654 | -57.77197 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0442928f-6139-35c2-a818-a92b212d268f | -3.59718 | -55.46687 | 2025-11-10 05:37:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22956359-5fac-31a6-ba92-13cfcd57e272 | -2.94063 | -57.77259 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 383e482f-a8c1-3397-abea-29b7d1bb74eb | -3.33442 | -49.92648 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd66396f-bd92-3417-8a78-2583874000b6 | -3.10626 | -50.19641 | 2025-11-10 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67e9c2ee-d1d0-32c9-8fc5-8f23e5bf7f17 | -3.32751 | -49.92553 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25f78d51-1c81-32a2-8c3a-ba785cf5c71b | -3.59637 | -55.47219 | 2025-11-10 05:37:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e206c37-3554-3dcb-a69b-ad32d7c888c1 | -3.10543 | -50.20222 | 2025-11-10 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8019d2fe-cc58-319b-acc5-388a8d97d75f | -3.10338 | -50.20215 | 2025-11-10 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd7b887c-4efa-3fbe-b9ac-0235aa2e5021 | -3.92326 | -59.12292 | 2025-11-10 05:37:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26756621-0a57-3ef4-a4e3-b606842fe4c4 | -2.90247 | -56.95957 | 2025-11-10 05:37:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3edc14b4-ad0b-31f0-b4a6-2a07a3556cdc | -2.94359 | -57.78044 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f7f7c8-fbed-3d33-a48d-f5057d5cd9be | -1.63536 | -53.67562 | 2025-11-10 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 195286e1-6bf5-3c4d-9982-9a9a1a9bd2b2 | -2.59983 | -49.22882 | 2025-11-10 05:37:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dad8ae84-edf8-3081-866e-f06290a0fbd7 | -3.31653 | -50.10215 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66db748a-0595-312b-9c54-18bf7ce19815 | -3.31535 | -50.10261 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7fff3dd-97c9-32a0-a383-503d931eb594 | -2.60693 | -49.23004 | 2025-11-10 05:37:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7a341ece-78aa-3dde-ab12-43394aeb7eb8 | -3.11107 | -50.19711 | 2025-11-10 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43ddccd7-da68-3e7d-a30d-5d00713ce015 | -2.60793 | -49.2231 | 2025-11-10 05:37:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c0c1fb4-13b1-34c9-9d99-ad3e895c4010 | -3.31742 | -50.09586 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a2967d4-0bf3-3748-ba48-7a3042fa81dd | -3.21984 | -61.22725 | 2025-11-10 05:37:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce0e90e5-1d0d-3d7a-955d-a9f7f9321bd0 | -1.63328 | -53.67498 | 2025-11-10 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c80ec30e-25b4-3010-811a-402b147014be | -4.20214 | -50.62627 | 2025-11-10 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0d890fba-3b08-3843-9810-1f796960efad | -3.16564 | -60.67337 | 2025-11-10 05:37:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 521f4c60-61a1-3f15-93a4-e6197cb50d54 | -5.14633 | -50.87455 | 2025-11-10 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4d87410-6781-3ee0-b1bf-ae75790ef5e1 | -4.27154 | -59.65182 | 2025-11-10 05:37:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1414f96-cfd0-3f68-83b5-973d6536b7d6 | -2.87255 | -54.10852 | 2025-11-10 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17c7a4eb-c9de-3708-8d8c-fa3504a2aca8 | -4.20994 | -50.63596 | 2025-11-10 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 6fc74b3b-e72f-39be-8ac7-eca1b183b378 | -1.76612 | -55.03185 | 2025-11-10 05:37:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2702b501-388f-3aa9-b9e6-d6136ed80c4e | -3.80275 | -51.09312 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39275598-096a-352b-83b6-8925f5c009a7 | -3.59236 | -55.46601 | 2025-11-10 05:37:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cb45a20-6ba3-3a5a-b2a9-554d412e0177 | -4.4913 | -44.5513 | 2025-11-10 05:40:00 | GOES-19 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 8f20b8f1-4c7d-3f4c-9547-7bcd832fa200 | -4.2128 | -50.6273 | 2025-11-10 05:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3a1fce6e-fe3a-3099-92a5-c2db6ad98bd4 | -10.61508 | -52.18003 | 2025-11-10 05:40:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a550f1ca-a813-3a87-883a-1cc26f37079d | -8.52345 | -55.02697 | 2025-11-10 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b001175-0b99-3914-9d6b-6ca12448d94a | -4.29759 | -60.95382 | 2025-11-10 05:40:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 771dc916-6400-32d1-9dc3-d283623cdd87 | -4.29351 | -60.95711 | 2025-11-10 05:40:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d88a4038-66cf-3ff5-a448-f808db2c3f43 | -4.28944 | -60.96041 | 2025-11-10 05:40:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e80c5db-86b0-3a6c-ab83-fe5af66957a3 | -7.79417 | -55.03059 | 2025-11-10 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de8abd34-3fa9-3d34-91f3-aa2e13b90c3a | -7.79461 | -55.02735 | 2025-11-10 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30742812-2718-3c73-b76d-e9cfbb00a966 | -18.47773 | -53.40553 | 2025-11-10 05:42:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8d46fec3-d910-3f2b-a07c-daedf70b4bde | -18.48083 | -53.4053 | 2025-11-10 05:42:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 198427b5-1c31-3044-92e5-03b031bc0e22 | -18.47412 | -53.40447 | 2025-11-10 05:42:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c6961bdb-882b-364f-9b3e-40227047f7fa | -18.48449 | -53.4058 | 2025-11-10 05:42:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 38ef3b46-cb05-3959-a52b-9c64a16d0692 | -18.19442 | -56.69851 | 2025-11-10 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 6fa197f0-9284-31df-9ffc-1b72bc32b1f2 | -18.51413 | -53.48845 | 2025-11-10 05:42:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51e2e755-13be-30d4-a60d-5ef250cec655 | -18.19481 | -56.69485 | 2025-11-10 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| d1f4a24b-9718-3fce-8958-013ef6932fb2 | -4.2128 | -50.6273 | 2025-11-10 05:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c48e1bd0-a683-3464-9af2-664e4ba0ea7a | -4.293 | -60.959 | 2025-11-10 05:59:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3adaed7c-cd81-3736-8e49-ab52931aa637 | -4.2986 | -60.95667 | 2025-11-10 05:59:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f93ec67a-4a49-392d-ad00-df93863d6282 | -4.29345 | -60.95592 | 2025-11-10 05:59:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0baed547-0252-37a4-9e03-bc782c99d5e7 | -4.1943 | -50.6281 | 2025-11-10 06:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0ffca60b-9c19-3161-ab22-b8d6cf06204d | -2.94088 | -57.77946 | 2025-11-10 06:01:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3ef8a04-f242-3484-b8c1-efc4d13ec3a5 | -2.83732 | -49.51146 | 2025-11-10 06:24:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| defb16f3-9860-3742-af0b-8d09e322f942 | -3.59528 | -55.46681 | 2025-11-10 06:24:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f114f93f-61b4-3677-be5e-f161dbdcf657 | -3.33083 | -49.92115 | 2025-11-10 06:24:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2489b233-c243-304e-99ed-ad109e067533 | -4.20446 | -50.62654 | 2025-11-10 06:24:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 10e2705b-b250-3da4-9590-7ac757f34f9f | -3.10508 | -50.19733 | 2025-11-10 06:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1b731989-5d97-30d5-b160-e71222faed63 | -4.20311 | -50.63554 | 2025-11-10 06:24:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| d523c0a1-6add-3545-ab78-6f5783c4c703 | -3.45127 | -50.47644 | 2025-11-10 06:24:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 03471b0e-2168-34b7-9854-fd3ffb2b353c | -3.85756 | -51.40495 | 2025-11-10 06:24:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4af81212-044d-3a09-914e-e9a6fdc6ad2b | -4.74915 | -49.4939 | 2025-11-10 06:24:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| ca0af397-99bb-390c-aa09-c1a00e320a5d | -1.76684 | -55.02302 | 2025-11-10 06:24:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4161910b-ff6c-3225-b804-ba65f3fbed75 | -3.0964 | -50.31694 | 2025-11-10 06:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d2a1427c-02b0-3ba6-81a1-15baf332c229 | -2.60286 | -49.22009 | 2025-11-10 06:24:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f8b9514e-bb36-362d-b9b4-da5044176c10 | -3.47844 | -49.92049 | 2025-11-10 06:24:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4b9b6a86-666b-338c-8ff3-6988a0f2013e | -3.28032 | -51.11638 | 2025-11-10 06:24:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| acc1b93f-f79e-3eba-a6e1-4e1ff0fe4d97 | -3.85625 | -51.4137 | 2025-11-10 06:24:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 72d43f5c-1188-3325-90f3-c0b4c1e3cc2c | -9.13055 | -50.0764 | 2025-11-10 06:24:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1afdc3de-b559-3cad-bbc7-568edd267909 | -4.10758 | -47.27261 | 2025-11-10 06:24:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 12a6cdaa-f154-32c6-8760-c7d7e5cd473c | -3.47702 | -49.92991 | 2025-11-10 06:24:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c836997a-014f-3dcf-aa34-4a4f67a9d321 | -3.10644 | -50.18819 | 2025-11-10 06:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 55dbf717-24b6-3b09-bc10-54bf726b065f | -9.12903 | -50.08707 | 2025-11-10 06:24:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4db15032-dca1-31c6-8415-a6cd8f3f20e0 | -10.61599 | -52.17803 | 2025-11-10 06:24:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 28cf8a4e-7948-3e4b-a709-a509450d63ca | -2.6014 | -49.22998 | 2025-11-10 06:24:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8567f264-7583-3af1-b4b1-6e72fb2c44a2 | -4.74768 | -49.50407 | 2025-11-10 06:24:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 4af639de-342f-3ee4-9333-121d5c8a657a | -3.31362 | -50.09925 | 2025-11-10 06:24:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9cb0588b-0a85-3095-b716-e98f1d5c0b14 | -7.88311 | -48.39607 | 2025-11-10 06:24:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9ff2d426-acda-3ea9-b2b4-fc5989370ff3 | -7.88494 | -48.38286 | 2025-11-10 06:24:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 57011c7a-f3da-36ce-913e-9ab9523396c7 | -18.47492 | -53.40229 | 2025-11-10 06:26:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 3dcbca1f-c5a3-3a05-8035-0ccd13ec6c3e | -4.86662 | -42.53886 | 2025-11-10 11:57:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| f3591309-3f06-3e4c-af2c-bd32acea3c8c | -5.71992 | -42.19232 | 2025-11-10 11:57:00 | TERRA_M-M | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| c726874e-b521-3456-a1d0-d96e4ac5fda1 | -3.2483 | -41.14053 | 2025-11-10 11:57:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| abc624e2-9ad9-3d21-b4a7-3898d2c04dac | -6.1693 | -38.34141 | 2025-11-10 11:57:00 | TERRA_M-M | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 0c5d6c7a-a8ed-39cc-8456-fa27826d6e89 | -6.36794 | -41.06438 | 2025-11-10 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| f9eea76f-78a6-3d1f-bb82-cd73969a3006 | -2.91259 | -40.45298 | 2025-11-10 11:57:00 | TERRA_M-M | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 33088047-dafe-3bd1-9e56-afe392328f0e | -4.75573 | -42.60624 | 2025-11-10 11:57:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| edc08bc4-5790-359f-967e-d58d739b16d5 | -3.92102 | -43.14826 | 2025-11-10 11:57:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1f37ada8-d8a9-358c-aff7-dd8f98fb87b0 | -7.44367 | -37.34056 | 2025-11-10 11:57:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 0d50fe31-6af5-3263-83e0-4ceb1af07ee1 | -4.75699 | -42.59748 | 2025-11-10 11:57:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 35d030e9-6af6-3455-932e-bdb0c4035593 | -7.44593 | -37.32249 | 2025-11-10 11:57:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 0b73b70c-175d-34c7-b943-3e67f5b5964f | -4.4134 | -43.12215 | 2025-11-10 11:57:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README20.md)
