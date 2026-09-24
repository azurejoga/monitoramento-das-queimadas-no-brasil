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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49f8058f-3337-34df-b53f-f0d1fc180355 | -5.25135 | -49.23203 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6d7fc984-2719-360d-bc3e-0df041e391bf | -3.72194 | -54.20543 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 426b1399-a946-3828-b5ff-dcc92d2ea813 | -4.01899 | -52.07488 | 2026-09-24 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f437e8d-0777-3537-9796-2ca6e55f6ee4 | -5.22786 | -49.22492 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b23a46b-9a88-3028-aaf0-fdfecb303a73 | -6.60734 | -59.92377 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3077b418-c241-32f8-9b75-9ed2bdc130d1 | -1.62723 | -54.91812 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bb45baa-ba88-30ad-ac34-666a38351d97 | -3.70593 | -54.19939 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ada7e5f2-ac2f-3ce5-8dae-36ff4c0cc2d3 | -3.47276 | -59.52868 | 2026-09-24 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ff0ca49-6af6-33bd-b078-1ce19e28f3b3 | -6.67299 | -50.95132 | 2026-09-24 05:04:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0b95833-ea0d-3726-ac71-f7de47f4a3c2 | -1.42551 | -54.59245 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c127626-7ee3-3771-bc7f-e06dc286073d | -5.3726 | -56.05422 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61071810-d251-3a80-8d13-fa2c64604c68 | -6.68335 | -55.04673 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a3ef91b-57dc-3073-950d-e5a8b87e9f31 | -8.27953 | -54.77234 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de28108b-41c4-32e5-af78-faee3ef3f213 | -8.17571 | -54.78393 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b08423be-e8e5-35b6-a902-b77de26fc96f | -9.2376 | -47.35187 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a57d5ba-7b1e-397d-b3fe-9372a9991a5a | -5.60234 | -60.20217 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c432a07-3afc-3a87-9455-31866871e88c | -9.26476 | -46.2378 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce85ebc7-0a0d-3711-adbc-42c4da567958 | -1.62838 | -54.91088 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2685f486-7d39-358e-aad2-bff7ef2eb641 | -4.51281 | -54.98027 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 025f8cf5-f069-37e7-b5b9-c8606a5dff99 | -8.20435 | -54.73155 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2dcf8606-4313-38bf-99cb-95bdf35ab64e | -5.81993 | -57.74183 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36300c41-db3e-3798-aa0d-9da9259fc1ed | -3.91446 | -59.66282 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d30a0667-c12a-30b3-a150-65593f050613 | -2.38893 | -48.52064 | 2026-09-24 05:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61f47932-243d-3786-aa48-7ce49f6ed24f | -7.33065 | -55.58896 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fd92970-a751-34d5-a7b7-b0ff45e435b5 | -3.44489 | -50.08083 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff6e4264-7ecf-3833-83b7-bde0f4d8495a | -5.51749 | -50.02898 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2120428-2e9f-39ab-8a43-184185c18ec6 | -6.4471 | -59.9511 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8f0d76c8-a41f-3c18-b5e7-f9b1ae683eda | -7.55466 | -55.01511 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4899fe3f-5a56-3b69-b745-38b287e37e92 | -6.34405 | -57.76945 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4faf28ab-2209-312a-ba85-bbdaba7e2cea | -4.44982 | -55.0317 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c14f4e6-aed6-3677-a55e-e8d5ee008eba | -2.28535 | -56.66956 | 2026-09-24 05:04:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dccb7db2-00bf-3b81-b670-23a4e98c7414 | -5.21984 | -60.05472 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f52db1b-2608-3f07-a175-ca98b4f090cf | -8.26023 | -54.76571 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f36566a5-bae6-310a-8885-a57a2dd87624 | -3.68655 | -60.54917 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 56214afb-05d5-3e29-9a25-58abac995f05 | -5.23304 | -49.29982 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca64390b-4aff-3462-b24e-6217efe3ced0 | -6.33924 | -57.86411 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6dcfd82-5962-30c2-9d21-ca71e00ed6bb | -6.76837 | -63.14614 | 2026-09-24 05:04:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e7d6625-3048-350d-8f34-88506218cff6 | -8.12661 | -54.81522 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb7b0170-64a4-32f1-ae77-1c7d3d5ef1c0 | -4.89155 | -55.97139 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f654e06-b509-3fd1-9a0f-5ad5dc184bca | -3.18178 | -48.01595 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 14156e88-17b5-3760-aa0d-2f546195da8f | -5.85119 | -52.02929 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27e7b19b-b46b-3dd0-9490-0bbc1198a5b8 | -4.03203 | -59.84677 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c7d95a0-0cae-31c0-80c1-cd4c8a4c1f5c | -8.38994 | -46.29551 | 2026-09-24 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 82fc451a-bac6-3583-bad4-0590571804bd | -7.85777 | -54.71157 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c843a7e-2acc-368b-8f7a-222800a1cae5 | -6.71527 | -44.15805 | 2026-09-24 05:04:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 807cf001-9920-3fc5-a2a9-fe7342fbfbc1 | -6.61212 | -59.92067 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cb1966f-c1b9-3f96-8e8a-014ce75e2489 | -3.45535 | -50.08695 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3074a36-4b45-3173-b19f-36e51d98f72f | -3.8497 | -58.66952 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74d3c837-570e-3d12-a908-b741da77b63b | -7.67787 | -45.49019 | 2026-09-24 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f6fa1e8-0e32-32e9-994a-9d456b107066 | -6.62354 | -57.984 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6521f7b5-113a-3a94-bcd0-5b196eb0ad43 | -1.25929 | -56.86278 | 2026-09-24 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2672c476-2326-3f1a-b896-e59b0743c133 | -3.06501 | -49.57631 | 2026-09-24 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04b4ca6e-97ef-3061-a0ef-4e8eddf6bed6 | -2.57261 | -54.74653 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb9949a7-b6d7-3aba-b52c-f700095abaf8 | -9.25764 | -47.34908 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 77b17aa1-741a-35e0-8bdc-f619ec35a546 | -9.26736 | -46.25766 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b68c40c5-76e1-33c3-834f-2c6965c06169 | -4.53058 | -54.97189 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39664179-12a1-3abd-bd22-833a5bce3a2a | -6.27153 | -43.27282 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d72b9ed-e1bf-31c0-80d3-fa60044c0674 | -5.2477 | -55.91707 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 856e98ab-bd70-3bd2-afe5-edf4aede01e2 | -2.9177 | -54.15632 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 426ed043-d7a5-3f37-a0bf-8b31b3d79d28 | -6.54745 | -43.08893 | 2026-09-24 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdbf8fc4-a912-30f0-beba-7f2c4760f766 | -3.71808 | -54.20837 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f3eab38-2461-321e-bbf1-f435896fce74 | -6.61791 | -59.98801 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06c0fa14-5e4a-3049-8c08-8e6283982010 | -2.91825 | -54.15287 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c08685f8-2b3b-3157-a7a1-d2dc1def8c41 | -2.95909 | -54.08884 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0cf12b0-201c-3c7a-b94e-25ec32402601 | -9.17455 | -49.99222 | 2026-09-24 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b241368-d3f0-3d0f-9360-aac06b5986d6 | -5.76892 | -45.09777 | 2026-09-24 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 563ac42d-cf75-3f9b-875f-5dd59efc9bdc | -8.90227 | -45.90989 | 2026-09-24 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c814855a-862e-312f-a7f9-96832385459c | -6.33334 | -59.95703 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04c3a039-7898-3873-ac35-3017593f71cd | -6.13619 | -53.15203 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b9a9767-693b-3ea3-bda6-456b718527a9 | -4.13613 | -56.32682 | 2026-09-24 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ade41acf-0a5b-3fb7-bce4-f6542f3fbe75 | -5.86435 | -60.16056 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 468e9648-feca-39ce-83f1-8fa2ffe59dd8 | -7.34431 | -54.94915 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f4e8441-89a2-345b-9a22-10e566f954b1 | -5.22051 | -60.05066 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60c80643-40fa-37ca-853a-5dd5c138d7d6 | -5.98858 | -44.42988 | 2026-09-24 05:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b06017f5-325a-31fd-9a39-c38df1c301ea | -7.33343 | -55.59302 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 997c65a9-8cce-3b89-bb6e-17bccd03c315 | -8.27732 | -54.76487 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30903cd8-6f62-3d46-b591-03051ecb29fd | -5.40971 | -60.21752 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e59ed399-82f1-3dfd-87d8-5fc3379d5b70 | -2.82891 | -46.70503 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88194ab0-03f3-38c8-b7d4-9e7f6181559e | -4.99138 | -45.5554 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e126cc8c-646e-3840-b3fd-3f5457ac23a6 | -6.1765 | -53.28916 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78630db4-7935-356e-9c50-8b34f5d83af3 | -6.12049 | -57.76212 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2843b13-6b50-3be4-b77b-ecbfb110acb1 | -6.6765 | -58.55673 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cf71d70-c6bd-3d77-96c8-d97f69d3f1ca | -4.44705 | -55.0276 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f59b6761-0e93-3557-a0b2-d78c2ce413f2 | -6.69651 | -59.96197 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5354bd36-e54f-3a44-bf04-3fec08c6a837 | -8.27456 | -54.76087 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e44a0ba-010a-3e91-af00-a5208997de0b | -6.21084 | -47.49778 | 2026-09-24 05:04:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f619f9e-8d58-3463-acf4-01c8ae4c6513 | -6.66969 | -58.55085 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a010c2b-46d5-3870-ad3d-d907a9d92ae6 | -6.61451 | -43.73227 | 2026-09-24 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af3b9160-5a69-3f89-bbc4-7c06c96ae2cc | -4.44648 | -55.03115 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe79502d-eb22-3315-9399-96be17eb5b32 | -8.59131 | -54.62585 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdab3bf9-a788-34b5-98d7-42e02544c1fe | -3.00958 | -51.53568 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 857dacc9-9790-3425-b7dd-a83b01b34d0c | -5.83681 | -52.0077 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 23c3c72f-33b7-3641-ab3e-86e0dae58080 | -8.92966 | -45.94762 | 2026-09-24 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6d84d6b-1109-3257-bcc6-98fdb877f771 | -2.93521 | -57.91978 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c89ad06a-4f81-35ec-9818-01355b61f3ac | -4.99783 | -45.54685 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 70834d31-2d89-3d08-9941-da1e72fb51f6 | -4.44082 | -55.06645 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82491ec7-a3b2-37a8-b82d-f4f1b504a04a | -8.20711 | -54.73555 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05981a2f-2ef6-3e49-8046-bb9860d25842 | -6.23424 | -60.02729 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b15d244-a8a6-3a3f-895a-4705bc32df9c | -5.84705 | -49.87859 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faf948d6-850a-30c1-9eb6-2433e53c9d6c | -6.44293 | -59.95044 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README62.md)
