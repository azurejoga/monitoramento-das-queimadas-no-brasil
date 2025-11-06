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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a91bc6a-f2a3-3033-8532-0333587ac16e | -4.58396 | -43.33745 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 019db8bf-84b6-3ed5-abc2-78dad3fdecfb | -3.98507 | -47.30184 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29196036-5289-3bf6-adda-fc0511a029e7 | -2.78632 | -50.31776 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1a5b61d2-48aa-3f8c-be0a-456ffc6c3231 | -1.96927 | -52.10732 | 2025-11-06 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e35b56d2-5575-3a7d-b1a3-604a10bc5f8c | -1.65348 | -45.55586 | 2025-11-06 04:44:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dce4d47-755d-3a46-8c87-f90d44d822b1 | -2.69374 | -51.90087 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72725f96-870b-3dd5-ae91-23e3fcdc175e | -4.21103 | -48.39907 | 2025-11-06 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57d8a873-28eb-3608-a3d4-42300aa1f483 | -1.63921 | -55.17165 | 2025-11-06 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcb59bc4-fcf9-3e7b-b958-bb3c617f1e6a | -7.95279 | -40.33392 | 2025-11-06 04:44:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 599fec05-8628-3eaf-aa24-769f18584ed1 | -3.59254 | -55.40691 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7104b91b-74b1-3931-b137-f9ddacdd211c | -2.98701 | -52.82475 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c50dfb94-94f5-3cd7-bc71-7bc562e5d729 | -4.04443 | -46.99677 | 2025-11-06 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba60fa21-bc0f-32e2-b740-cf52f8f8e2d0 | -3.92831 | -47.69666 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5f387fa0-b825-30cf-89fb-065eb42a28e5 | -3.41243 | -50.83654 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58434db8-99a0-3583-a405-0ddace70fd12 | -3.25223 | -50.66658 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6898aeee-97e0-3fae-9494-ebbfebdf1a12 | -3.01892 | -51.19638 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 990fc8c4-20e4-3c67-a27f-2bbed8a43586 | -4.87435 | -56.08965 | 2025-11-06 04:44:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f539be8b-d71e-358f-abc1-833068773412 | -2.99054 | -52.82532 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1272fd49-a24a-3ea6-af13-8cb57d2bef81 | -3.933 | -47.68937 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d244d294-a182-36bf-a1c9-38b7b98844eb | -4.58151 | -43.32217 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c79ba4f3-0b36-32d7-96c0-0bdde9c319f7 | -3.00668 | -49.5617 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 416cc85f-9b68-3905-bf27-fa81857d5adb | -4.45972 | -43.22346 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0cce6e3-bc19-3cd7-a8ad-1ebb759c6f17 | -6.20185 | -43.27172 | 2025-11-06 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea36b631-ae93-3dc8-9c4a-f3501a168c30 | -1.6252 | -54.71276 | 2025-11-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 726aaae5-645f-322e-b8c3-e8cb5ed9d821 | -5.75843 | -40.81738 | 2025-11-06 04:44:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9701c332-ff94-3b0b-90ca-1593edb50026 | -6.21437 | -57.77134 | 2025-11-06 04:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e63e506-c7e3-3fcc-8adb-0338720cee1b | -4.61523 | -50.76173 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2977ade2-2fbe-323c-8a6c-0d4af5258998 | -3.7204 | -51.69214 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ec09455-e97b-314c-b5cb-ca77971431b8 | 0.42557 | -60.4912 | 2025-11-06 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4084c64b-5560-31b4-be99-8520a2cc875e | -3.7076 | -51.6204 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9ee4a4d-4efc-3fa2-8085-3f7ef5b4d559 | -2.99117 | -52.8213 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 921b7afe-7b76-3872-bdce-e06ea41450da | -3.80824 | -55.44206 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3b09a47-460b-3527-8612-9f8c9625fcec | -3.10907 | -51.20727 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eb4d27b-8972-34ad-8a75-0c69409557cd | -5.15098 | -41.24769 | 2025-11-06 04:44:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| df3c54dc-afcf-33f3-9e24-97a813e45cf5 | -4.67471 | -50.44705 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c92846dd-0af6-3294-9cab-011396a843fa | -3.86978 | -48.33648 | 2025-11-06 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29da9284-86c0-3299-8572-f0fb86886a04 | -5.2457 | -44.39063 | 2025-11-06 04:44:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7966b2d3-c539-33bf-a3c4-a9aebf1c47af | -5.33553 | -43.03305 | 2025-11-06 04:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d764713-c5bd-36b0-bec9-75b536a435a9 | -4.59987 | -49.55427 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a443650-ade6-3d1f-9772-d836a861f968 | -2.69432 | -51.89717 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5a783d9-5efc-356d-ac90-decf9986c5c1 | -1.64256 | -53.71827 | 2025-11-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 483c746d-75f0-3008-9650-d977cf8599e4 | -4.18739 | -52.09467 | 2025-11-06 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 730015a9-bfa8-3270-b431-068ecd752842 | -3.47046 | -53.23143 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8a7dec5-90fd-39e0-bebe-a41efaa31eca | -3.0118 | -51.39447 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef17706e-c585-309c-9d58-3d956e4de2dc | -2.78686 | -50.31433 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35c3a2a3-8a17-3aeb-9f00-c27531a4fd4b | -5.37182 | -44.73677 | 2025-11-06 04:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c01b07d5-ca3e-322d-a1b9-f30478f04479 | -3.93254 | -40.92617 | 2025-11-06 04:44:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9c5b7abc-7bce-3913-9717-0b2ddd086ea3 | -3.23966 | -53.26838 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c99c46b4-46ac-3278-b121-940f0f77c761 | -4.00068 | -55.46626 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e70ff502-ae33-31e6-a046-ff6af0f3d8d6 | -2.26763 | -53.55375 | 2025-11-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27e82ce7-44ce-383d-a5a2-c62f81fd2a5b | -4.80106 | -45.73841 | 2025-11-06 04:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34424dc5-b64b-38e5-ad22-02b316d837b9 | -1.14328 | -48.09814 | 2025-11-06 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1856bf07-44f4-325a-8f09-650e7987e6e6 | -4.36422 | -48.65855 | 2025-11-06 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05d670f9-5190-3c3c-bed9-f958f4f5e58e | -4.38896 | -49.77423 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41b09e6c-3d96-38cd-86f9-a6339bb4dd3d | -3.98413 | -47.30104 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a422c97-6709-3f53-a042-91709c483df7 | -3.82828 | -49.81359 | 2025-11-06 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2979f83-eb0e-32aa-977d-260f97d4df88 | -3.89623 | -55.87743 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be668f2b-702a-345f-859e-dd0f537b835d | -3.75173 | -45.08733 | 2025-11-06 04:44:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c47d14a-8aaf-3183-8595-550fb31cf623 | -3.98832 | -47.29745 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1c9f4dc-d3a4-3ab7-b5b4-b3e237fa5133 | -3.58788 | -55.40984 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 349f8132-c6be-315a-9165-334890832eaa | -3.86772 | -52.60384 | 2025-11-06 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6f749e76-e1ba-3462-b323-ddf6c8b86fe3 | -3.92364 | -47.70388 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5059bf7f-aab1-3531-9289-c2fef360f190 | -5.6517 | -43.01337 | 2025-11-06 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5908988-d7a4-35e6-b3c0-46025dbc52ff | -4.04144 | -46.99187 | 2025-11-06 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4dc04b2a-7b48-36d0-9bfa-62ecb053de97 | -2.78302 | -50.31725 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09088417-3a14-33cb-a1dd-db23c35c4150 | -6.62133 | -55.02007 | 2025-11-06 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f61dd3c9-2e3b-3c95-93b2-b8d8debcaf1e | -1.64633 | -53.71883 | 2025-11-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 957d7875-0481-375b-9d67-a077687eb04d | -6.12096 | -57.70936 | 2025-11-06 04:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9a99db5-c87f-3631-9f4f-ddcdb3cb9009 | -4.0 | -55.46892 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48b42e3b-f4c8-3216-b9b6-a05d96eb8b5f | -1.14385 | -48.09455 | 2025-11-06 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c6a6525-1059-3077-af4c-ec145f2fac03 | -2.61961 | -49.2289 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9cc91e47-3682-3750-a98c-d5f51af70319 | -4.71745 | -46.43122 | 2025-11-06 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ba56606-71c1-3158-a491-85da44e47ed5 | -4.58319 | -43.33513 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f75fc840-a908-3e4f-9e95-d7701d4b34b6 | -3.93123 | -47.70108 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78674a45-e0cb-3406-b8a5-77dce37f2601 | -3.24055 | -52.91948 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e85f1dc-a8c6-33b0-a996-3187d551613c | -4.54052 | -46.44676 | 2025-11-06 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 294b2c80-8449-385d-ab8c-73219f5472c2 | -5.46114 | -44.69266 | 2025-11-06 04:44:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55666937-ce15-3fc9-ace3-c285619208e7 | -6.52471 | -55.0404 | 2025-11-06 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e83ebb86-a56a-3c20-a914-0603d4a8bdfa | -3.59196 | -55.41044 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d766d6ca-d1d5-3fe4-91b7-23bba967c528 | -5.75793 | -40.82097 | 2025-11-06 04:44:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2adac1b7-8ebb-37a1-bccc-bbccbc0f0093 | -5.15491 | -41.25879 | 2025-11-06 04:44:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| acc75c71-d092-3771-99ac-ed13cbf8277c | -4.4959 | -45.92489 | 2025-11-06 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d54a29b-9094-3cf4-b36d-08a0bf3aa25f | -3.38263 | -49.22254 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49b99259-a628-32cc-8278-4595748bad2c | -3.02534 | -51.38972 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cae0485-f333-308f-b60b-0d5097ac47c9 | -3.74309 | -52.17261 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9f719ef-e62c-3e56-87ec-905c362425ff | -2.6301 | -49.22697 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3857d248-a7a8-3af8-afc7-59edeae6cd9a | -2.92817 | -49.16955 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f30d8123-92d1-35c6-a83c-a9192f9a2774 | -3.43516 | -51.51582 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3616fae8-9edc-32b8-b8d7-2117d7590ae8 | -3.98571 | -47.29774 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56dabd4a-dfc5-38be-9098-07a25ec37ff1 | -2.93254 | -51.30953 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 534c724e-ad59-3776-8ab8-6a762883c1a3 | -3.04275 | -51.1317 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da1ec314-1e78-3d96-bb0b-f6fe9815e183 | -3.41625 | -52.77199 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c40ff19-09ea-3161-a4e1-0d9b87b86ade | -3.83727 | -51.75075 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70938b33-48c3-34cc-96fe-0283e1a22016 | -4.54121 | -46.44226 | 2025-11-06 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a11ecc37-149b-352b-8f41-df4323748726 | -6.23447 | -44.30636 | 2025-11-06 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e3b4b7c-ce95-3a04-99ed-8b80ef54618b | -4.58078 | -43.32704 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 092c79f6-246a-3600-b5c5-cb21bca57a3e | -3.25641 | -51.20144 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bba1f71e-a21e-3cfa-99e2-97cc8aa995cf | -4.77399 | -49.52789 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d91d86c-c7cb-355c-8404-32b5bb01cbbc | -3.50518 | -51.54473 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 956eb63b-58bd-3362-86be-6c8a445e85cd | -4.87846 | -47.5442 | 2025-11-06 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README18.md)
