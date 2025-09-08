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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2af9b195-98a0-3c70-b95f-23f90b04b10d | -17.95595 | -42.77206 | 2025-09-08 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6c2d225-fd93-34ea-957a-17ac963db77c | -22.56325 | -54.92049 | 2025-09-08 04:06:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2f25c1a7-0149-36c1-baa7-718bb8529252 | -23.47486 | -49.67965 | 2025-09-08 04:06:00 | NOAA-20 | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 284d732d-8143-3f29-8741-0c73b8ac1a87 | -7.3983 | -61.6346 | 2025-09-08 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 113.4 |
| b0f61b58-ec12-3a2f-a5f2-45f4bb68b2ab | -7.3984 | -61.6156 | 2025-09-08 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| cfdd8983-b8eb-3828-a98b-2bb273ce1c49 | -12.6153 | -56.9742 | 2025-09-08 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 429f4a81-5233-31a2-9815-601292ae6d1d | -12.6343 | -56.9725 | 2025-09-08 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0f48aadf-bd89-3158-a96e-93b1ec344b2b | -7.3983 | -61.6346 | 2025-09-08 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c28e8dc0-c9a3-3939-b347-e323fb9be6ae | -2.7919 | -49.62133 | 2025-09-08 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bcb8a4fb-076c-3dcc-8e05-4116e0126b1b | -2.13996 | -47.70976 | 2025-09-08 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7161e941-c909-3ea8-a033-fb75f3f3a612 | -2.6809 | -51.83433 | 2025-09-08 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99583120-518b-37f1-a3a4-04a79ee7dbb1 | -3.65776 | -43.6437 | 2025-09-08 04:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0160d53f-e1fe-39e8-80f8-c4f4307a7c4a | 0.55023 | -50.80365 | 2025-09-08 04:49:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c259d371-8c02-3bb8-8d87-248b22400971 | -2.91732 | -48.67462 | 2025-09-08 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb7d1a04-8873-3025-9afe-731cd2160d0f | -3.89862 | -38.53938 | 2025-09-08 04:49:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 87b076ce-23b7-3b3f-b3b7-8cc77349d5cc | -2.68036 | -51.83775 | 2025-09-08 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b1ec701-dbf5-33e4-b2e6-362004faa2a4 | -3.31115 | -48.71738 | 2025-09-08 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a49d36f6-3c5f-3455-b8e7-b85d7fa2c926 | -3.59221 | -47.51281 | 2025-09-08 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 339b9c11-6536-313e-9dc8-fb78538b7301 | -2.67706 | -51.83725 | 2025-09-08 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 703e4a5a-fb3a-398c-bd53-eab4b0ddbd67 | -2.33336 | -48.61954 | 2025-09-08 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44fe0281-f51d-307b-9284-69be79570546 | -2.14375 | -47.71037 | 2025-09-08 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a650950-8b0a-3864-8717-12854275751f | 0.54969 | -50.80022 | 2025-09-08 04:49:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6f4e8d0-fd20-37fd-a5cc-f115d57bd593 | -2.96398 | -47.89778 | 2025-09-08 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2355aa34-e79f-3642-9441-30b404662dcd | 0.55353 | -50.80314 | 2025-09-08 04:49:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e52ea19b-1dd4-3d01-881d-c7bde7510bf9 | -1.30531 | -49.41204 | 2025-09-08 04:49:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8584da0-6339-3db8-9710-25646a49a017 | -3.3118 | -48.71315 | 2025-09-08 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2d24e5ab-9acd-3158-bc10-8a8d552150c5 | -3.24809 | -50.8108 | 2025-09-08 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fa5094b2-185f-3e84-90c3-1b6f9c0fef43 | -3.89635 | -38.53615 | 2025-09-08 04:49:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1a0b4f4d-b51a-344b-9b51-9e2c8deabff0 | -3.65264 | -43.64298 | 2025-09-08 04:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfd7aa30-b47d-31d9-8c44-7168e532d70b | -1.29099 | -49.36726 | 2025-09-08 04:49:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d93104cb-11e2-3fcd-bfad-4a0d18490a27 | -3.31478 | -48.71794 | 2025-09-08 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c5d08f8d-9df7-345c-8dca-dd61a6a0df5a | -3.30751 | -48.71682 | 2025-09-08 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72fb4885-7ed2-3d05-b6c2-5bc056f765a6 | -7.3983 | -61.6346 | 2025-09-08 04:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| faf39a38-5343-3fcd-a5f6-59060973be9f | -6.84974 | -52.8512 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 259df93a-b485-3bb3-8d64-5c0f5efdfc6f | -6.6685 | -44.55704 | 2025-09-08 04:51:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c93db19b-33a7-34cb-bfa0-f6f60e8023a6 | -9.7236 | -43.97959 | 2025-09-08 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b893fa0-799e-3241-a0fc-05d968cc2c6e | -10.00445 | -51.6303 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c35264df-75be-3a0b-951d-cb90a0eb5146 | -5.29132 | -47.35623 | 2025-09-08 04:51:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06404942-69ca-311c-a6fc-97459e2f8383 | -8.16244 | -44.84799 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82dd9891-f1da-3e68-b5d6-35ce1e8e521b | -5.21483 | -43.28459 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a91b222-1329-3b2d-9433-50d2e02d53c5 | -5.76393 | -40.95438 | 2025-09-08 04:51:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 55c78f3d-2b59-3a58-a55a-d97cf6574c1a | -7.22782 | -46.20121 | 2025-09-08 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb848353-d8d0-3a2c-afcb-49e25780c6a7 | -6.82309 | -51.88281 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89a63614-ccfd-37f4-8f6e-348ade4020f2 | -6.53258 | -49.50061 | 2025-09-08 04:51:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4f9dd7b-dc96-327f-84df-c6c2d3331fbd | -4.53052 | -54.84462 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 340d4b2c-9a55-34b7-9d08-70a1f6f5847b | -4.80901 | -46.82313 | 2025-09-08 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2ec35e2-7a69-3dad-9399-fec4d06dbb8d | -4.41303 | -47.60693 | 2025-09-08 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 892013bb-cfd1-30b9-a617-45b6834f52a7 | -3.84592 | -49.28975 | 2025-09-08 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92aab521-3731-3729-a865-2ac401781843 | -6.26748 | -52.80827 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efaf137e-adfb-3a9d-b9c8-82f9ee6e8ae4 | -4.99791 | -56.25392 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d51e9a63-78dc-3c91-bc7f-01ef1b628b3f | -6.82931 | -52.805 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48c85e17-c077-3103-9cae-785c5064d9fc | -10.45962 | -53.62991 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ac2b78b-7614-3a9f-9eaa-08ebfa518b97 | -3.5461 | -49.37807 | 2025-09-08 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc7ae765-fee4-3fa7-8fe1-88f97e347713 | -6.21141 | -53.27361 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82cc2764-cd21-3cf0-8740-c7c04a59710d | -3.8171 | -54.11814 | 2025-09-08 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caa1bc9c-01c4-325e-a076-15a6e956009e | -7.68181 | -50.28612 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd529b64-6900-37c0-90c4-8cad2ba3c1bb | -7.74729 | -50.74397 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e12d3848-c4b5-3b23-abaa-fb716d915cab | -9.08316 | -50.44937 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b586f0e7-27d5-398f-a972-cd3c70c865ae | -8.19737 | -50.13025 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 692b0a40-d284-35ef-8b06-3347eda60aec | -3.79309 | -48.87354 | 2025-09-08 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82f8e46a-50d7-35b4-a969-e9e95d201cca | -7.24313 | -44.84566 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f989d47-5edd-3555-90f3-4e6821cf026e | -8.19192 | -50.1423 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9aa48ab-6c50-3713-92f1-9e9c98f986d0 | -10.79088 | -49.71902 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82257532-2969-3837-8a88-f4d3d291d6d2 | -6.40725 | -43.87392 | 2025-09-08 04:51:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc1c8516-52df-3de3-ac93-b0247ebc9af5 | -7.83006 | -45.42455 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e703a026-c1e8-3fd8-96a1-4c0ebe660376 | -9.84713 | -56.0446 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72ca08f7-a2a2-3389-9f3d-fbd720050342 | -6.38438 | -42.60635 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01b55105-64a8-329b-b6f6-0948e9847c13 | -10.46619 | -53.60952 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5740bb73-76dd-3629-8af0-be7086c8052e | -9.20248 | -46.04053 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f37272e0-5022-3c16-ba56-81f9f285317c | -10.16566 | -46.21815 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32671501-5b72-3064-b4de-73b1542bcb22 | -9.33974 | -46.50932 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 684b65c5-f812-3101-8d13-02472ae79101 | -6.91927 | -62.94297 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06c64160-be36-3f68-a8d0-9698e764ab45 | -6.54343 | -54.99213 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b276ae27-3dfc-385e-a9a7-c5b6a3f3b4f4 | -6.81227 | -52.80587 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea18b51f-1bd9-3bfa-90d5-2253cdf79957 | -8.1949 | -50.14679 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49918eec-a625-3102-82e7-eadfc08fab48 | -6.0803 | -43.36393 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db3ddabc-3e5b-3074-81f6-3c9f9eb7cd5d | -6.13775 | -44.25979 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c91881a-99ed-308c-bcba-6c8f394788f4 | -9.20515 | -46.05609 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17c8e255-86b6-3dcf-be6f-ae63b2275b88 | -5.87224 | -44.17755 | 2025-09-08 04:51:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccb3fe29-d6c7-34c0-b3f3-1cabc2dc0576 | -5.88542 | -43.9681 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fb7b9309-041c-395e-b36a-958e4c41fcda | -8.03396 | -43.81465 | 2025-09-08 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a5453c0a-8416-38d0-8b17-ac61fb9903d2 | -10.0045 | -51.6533 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5454e05-2bd5-3db3-bb70-7ace94c58f96 | -6.54282 | -54.99591 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bf974b3-89f3-3f02-965d-97ede952f157 | -5.78567 | -45.62941 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5315d337-ead3-3e2e-bdba-ca4145c8acaa | -8.98365 | -44.93111 | 2025-09-08 04:51:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8753d0d-3089-37fe-aa76-00a6716fd5cd | -10.46565 | -53.613 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abec2769-81f4-3320-91f3-a293136ff436 | -6.83207 | -52.80896 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc321b50-e7c2-3c48-bf55-5270c4e9f43d | -6.80824 | -50.85695 | 2025-09-08 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c64d06-18fb-3eeb-ab32-c2fb3ad8b920 | -4.7357 | -55.72165 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5faed5fb-465b-3c21-8256-4df6c04908bd | -7.66456 | -47.94694 | 2025-09-08 04:51:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da7fb3c0-25b9-3246-a51b-74bd8c4b1d42 | -9.95366 | -51.19452 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1aca654e-2ca3-3648-8b5b-186a53a3bec9 | -5.94606 | -45.75222 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8793dfa-246c-32d0-bddb-b3625382a240 | -7.90117 | -61.78336 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 16321d2f-2420-35e9-943a-d1a5687341eb | -9.98061 | -51.67291 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 966c48c2-c2de-33e0-bf99-7e859eb1fbf0 | -4.29299 | -50.5847 | 2025-09-08 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 762dc314-f7be-3b9b-800d-1122699091c2 | -9.78654 | -57.45098 | 2025-09-08 04:51:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c0626e9-509b-3dff-a3e2-decab149dda9 | -7.4037 | -61.62569 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 653a1359-a07e-3c2d-9f99-8453ab8c32fc | -9.84778 | -56.04067 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a50f815-67bc-35a2-9db8-c3c9e046721a | -8.09155 | -54.76147 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ffc0b4a-8469-3bdf-9771-1ed1f8a423aa | -6.81119 | -52.81277 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README51.md)
