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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e22747dc-3723-3ab4-835d-aeffb6137e1c | -3.0374 | -53.9268 | 2026-10-07 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 90230770-7239-3ae0-8719-d804ace043c9 | -5.7374 | -45.176 | 2026-10-07 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 18e9e4eb-b304-3815-9efe-27b0047c1149 | -8.2865 | -50.2731 | 2026-10-07 03:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 2833ad47-b974-3976-b8ea-2f0a00c64f9b | -3.1787 | -50.5597 | 2026-10-07 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e3ac4581-184b-35d8-a11e-8cc44ef1abd6 | -3.8566 | -55.9967 | 2026-10-07 03:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| a285e247-2744-3631-987e-dc91b475efea | -3.1115 | -53.7637 | 2026-10-07 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 705fdf9d-3335-3b14-8e36-09dcf94f817c | -8.7225 | -45.204 | 2026-10-07 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| a46f896c-c53a-332f-81fc-50c2d736fcd5 | -8.7039 | -45.1832 | 2026-10-07 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a058a7e8-de57-3767-b757-71ce613647e8 | -3.6579 | -60.6412 | 2026-10-07 03:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e0ad4c8c-91a3-3dd8-bcf7-29ce4dfe9de3 | -3.6206 | -55.2708 | 2026-10-07 03:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a9b50f87-3691-3fd9-bd77-12d8a97fc398 | -2.7796 | -54.0937 | 2026-10-07 03:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 187.0 |
| a0b6e787-f596-3607-b975-b667932463bc | -2.7797 | -54.0736 | 2026-10-07 03:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2cbfa5bc-a78e-39d2-baec-d3cbaedacae7 | -3.658 | -60.6222 | 2026-10-07 03:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 78f4e868-2ffe-3b15-b95e-11d6b225d359 | -3.6205 | -55.2907 | 2026-10-07 03:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 2e12e73e-53d5-3f71-9d52-d97c230b7987 | -1.801 | -57.1161 | 2026-10-07 03:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 02fa3b1f-5a11-35c3-93d2-fe4d0553e706 | -3.531 | -54.6557 | 2026-10-07 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 65d10f71-a1df-3149-a3d3-1ac393f17c56 | -3.658 | -60.6222 | 2026-10-07 03:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a73556e0-b418-3358-9c4d-35731e50fab1 | -2.7612 | -54.1142 | 2026-10-07 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 195.2 |
| 3df97d03-fdc4-3110-95ba-0218ded4d6ca | -5.7187 | -45.1773 | 2026-10-07 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 21aa0bf7-ab3d-3d9f-88c0-3600896408af | -9.1517 | -65.9554 | 2026-10-07 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 07585983-6d10-3207-88a9-8b07c3d9b0d7 | -3.0 | -54.1287 | 2026-10-07 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| fc212bd7-ce88-3022-8f1f-618fbb62b0c3 | -5.7189 | -45.1547 | 2026-10-07 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 31c399d1-20e2-3d73-b6f5-58c132182bf7 | -3.1114 | -53.7839 | 2026-10-07 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5072d982-a9f6-3643-8e0f-71c3345ec193 | -3.1787 | -50.5597 | 2026-10-07 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 22bc55b2-2928-3b84-975e-656d18bb8aec | -5.9647 | -40.9383 | 2026-10-07 03:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 49.3 |
| ba3c11bb-d934-325a-852e-f22878f74925 | -1.801 | -57.1161 | 2026-10-07 03:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 04169115-71fd-36b2-bd79-5d90d0ae58b1 | -5.7374 | -45.176 | 2026-10-07 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ba23f8e4-e4ec-37ac-9b7c-6731fb2a4dff | -2.7796 | -54.1138 | 2026-10-07 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 249.4 |
| a70901ec-1b7c-3850-a9a0-286e1a0494b7 | -3.8567 | -55.9769 | 2026-10-07 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 51393b30-4b8f-3f6e-ab30-e7aa3450db3c | -3.6205 | -55.2907 | 2026-10-07 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3d52193d-41fd-3e4d-8b11-4fd03f865e00 | -8.7225 | -45.204 | 2026-10-07 03:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| c1db806b-45f2-365d-ae67-fd4728f9a41e | -8.7228 | -45.1812 | 2026-10-07 03:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2b44fbf9-736e-33ce-a79b-61c1ad924b24 | -3.0375 | -53.9066 | 2026-10-07 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 426757d8-d6c4-396b-9d36-e8e26833788c | -3.073 | -54.2674 | 2026-10-07 03:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3c8b9bd0-5765-38a6-b383-581b3e1269bf | -3.4762 | -50.0883 | 2026-10-07 03:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 0bdcac93-2590-3e05-ad99-87f9477c62d3 | -3.0374 | -53.9268 | 2026-10-07 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3331153e-aa83-3d1b-9192-f2012cfc0555 | -5.7376 | -45.1533 | 2026-10-07 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 0cd7355a-aa84-369d-be7a-4c4acbb8da71 | -3.6579 | -60.6412 | 2026-10-07 03:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| d2b9d944-0c92-326a-badf-7667a253ac5c | -2.7797 | -54.0736 | 2026-10-07 03:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 533e10a6-36bb-32ed-904f-1d5cc148fe44 | -3.5311 | -54.6357 | 2026-10-07 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 86535305-967b-3b45-987e-8e6a53ecbf6d | -2.7613 | -54.0941 | 2026-10-07 03:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 210.4 |
| cbae0ae8-6630-3bd0-9765-d40186435111 | -8.7036 | -45.2061 | 2026-10-07 03:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 56b06729-a34a-383c-975b-fcd119d3d83e | -2.7796 | -54.0937 | 2026-10-07 03:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 210.4 |
| 32aa9091-ef41-3350-bf21-4339cfdddd1e | -3.1115 | -53.7637 | 2026-10-07 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| b0ff07a4-e6e6-3f2c-9573-b8113c937289 | -3.8566 | -55.9967 | 2026-10-07 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 54f53e86-38ad-3add-b754-7fdf5fe0004a | -3.5126 | -54.6762 | 2026-10-07 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 31bbdf69-29c8-3d4b-9ff1-671ab4504bae | -3.0914 | -54.2669 | 2026-10-07 03:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 27ed3731-8a98-3458-89d9-f021d3519465 | -2.7613 | -54.074 | 2026-10-07 03:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 14b6e57d-3c86-3861-bf4c-e2f82eebef28 | -3.0913 | -54.287 | 2026-10-07 03:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| e7925353-578d-31a5-86fc-8cd576ca8cb3 | -3.5127 | -54.6562 | 2026-10-07 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 3bccda9e-5608-3c44-840c-e1fb34b3a59e | -8.2865 | -50.2731 | 2026-10-07 03:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| afc4fc36-c733-34a7-8491-7ecc84975d75 | -2.9448 | -54.1501 | 2026-10-07 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ee264acd-b253-357d-92a3-35505f7fe4fb | -9.1517 | -65.9554 | 2026-10-07 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9e1dc5c0-b5f8-381a-9a5a-96c0a44ad05e | -5.7376 | -45.1533 | 2026-10-07 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| d2f52dba-f615-3591-a896-40ad71fc87ce | -1.801 | -57.1161 | 2026-10-07 03:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| eb18310d-f9c6-3a03-85e9-19c427ab2cf3 | -2.9448 | -54.1501 | 2026-10-07 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 9f02358d-807a-3903-9276-333904252efd | -3.0375 | -53.9066 | 2026-10-07 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d812570a-4865-3576-8b3c-fb840d9c4ceb | -3.0914 | -54.2669 | 2026-10-07 03:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| eeb4da7d-c47f-37ce-993e-4c2605cb56b3 | -2.7613 | -54.0941 | 2026-10-07 03:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 210.0 |
| 72e838f4-4563-343f-9926-123fc1b8e5ee | -3.0731 | -54.2473 | 2026-10-07 03:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 50f1e73c-240d-3207-8138-2181a1b2930e | -2.7613 | -54.074 | 2026-10-07 03:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 8996c941-c12a-3f8f-bcbd-db19131ab8d8 | -5.7187 | -45.1773 | 2026-10-07 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a206580d-f991-33cd-a838-80e1cabae153 | -3.6579 | -60.6412 | 2026-10-07 03:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b1d4d954-f034-3d82-8165-61620a7f8f7c | -15.2511 | -43.2743 | 2026-10-07 03:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 80.8 |
| bb9bcdf0-9589-3bd7-bc95-316d2c79b723 | -8.7225 | -45.204 | 2026-10-07 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| af3b260a-ba03-3169-8ea9-e14cfb02fb34 | -3.531 | -54.6557 | 2026-10-07 03:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 2dbd88db-c91a-387f-bbc0-47a4d4faefea | -3.0 | -54.1287 | 2026-10-07 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 81206271-0452-3326-b6f1-e18d1a4b6905 | -3.4762 | -50.0883 | 2026-10-07 03:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 352ea345-b1fc-302c-ad84-29cfdd651cd3 | -3.0913 | -54.287 | 2026-10-07 03:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| adc1701f-eb50-3bc4-8194-d700fe313232 | -2.7797 | -54.0736 | 2026-10-07 03:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 27784f20-d939-3666-aa33-5783740901b6 | -3.8566 | -55.9967 | 2026-10-07 03:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 60f092c1-7bb8-3ec3-814c-da850b89c113 | -3.5311 | -54.6357 | 2026-10-07 03:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c2004ca2-95c8-39a3-91fd-6aa8c2bbb91d | -3.073 | -54.2674 | 2026-10-07 03:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 257ca70e-71f5-38a8-aa25-786503138f09 | -5.7189 | -45.1547 | 2026-10-07 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 616eef35-7ed1-37e8-a757-f542a7a24ae0 | -5.7374 | -45.176 | 2026-10-07 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d83ca5b6-866b-3d15-aa8b-145b4d9acd25 | -8.7036 | -45.2061 | 2026-10-07 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 1cf6623a-5eff-304e-89c6-c262fb0435c0 | -2.7796 | -54.1138 | 2026-10-07 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 220.1 |
| 3608c087-29dd-3950-a0e4-4769c709ea97 | -3.8567 | -55.9769 | 2026-10-07 03:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 601faffb-a880-37a8-9400-3eae472b843a | -3.6205 | -55.2907 | 2026-10-07 03:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8d551806-08fb-3e29-a497-3a2f900d8fba | -2.7796 | -54.0937 | 2026-10-07 03:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 205.0 |
| c1ca284b-5035-37d3-9592-485189e2b1a1 | -3.1115 | -53.7637 | 2026-10-07 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c96b7ecc-5bd2-3bf8-ad51-c2a194bd9d5c | -10.4842 | -50.4314 | 2026-10-07 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 31559afa-742e-38f6-b643-3f7e3ec82843 | -2.7612 | -54.1142 | 2026-10-07 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 196.5 |
| 9086ebf4-5312-344e-88aa-de22642740ff | -8.7039 | -45.1832 | 2026-10-07 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 3e779c8a-cb62-39e2-84c4-774bb0af7f36 | -3.1114 | -53.7839 | 2026-10-07 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ea5685c2-1afc-3127-88fb-34abd00ca8d0 | -8.2865 | -50.2731 | 2026-10-07 03:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 3a0f17a6-4b12-338f-96fd-7b04dadbd2c2 | -3.5127 | -54.6562 | 2026-10-07 03:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 231e3475-6fd7-34c2-b70b-c0ae65e348cc | -3.658 | -60.6222 | 2026-10-07 03:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| b3264b88-dc79-307b-b9da-37053e106512 | -3.1787 | -50.5597 | 2026-10-07 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e9599b8b-f55a-375e-9c7b-381c68d9a41b | -2.7796 | -54.0937 | 2026-10-07 04:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 164.8 |
| a869cd2d-be79-3c6a-b5ab-0395d4d5e91c | -3.6205 | -55.2907 | 2026-10-07 04:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9815482e-6b61-3daf-843d-ffb724e2112b | -2.9448 | -54.1501 | 2026-10-07 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4ee1047f-76e3-33f3-a180-b880d4114922 | -8.7036 | -45.2061 | 2026-10-07 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 7a6560f4-f63c-3f64-ae20-5e99360ef4dc | -8.7225 | -45.204 | 2026-10-07 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ab1840eb-9774-32e2-8a5d-8470292cef81 | -3.0914 | -54.2669 | 2026-10-07 04:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d5fd1c89-2bac-3ebb-8fed-2803faa89ef4 | -3.0913 | -54.287 | 2026-10-07 04:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 543aad8a-1cb8-35c9-9b12-440bb53cd82c | -15.2511 | -43.2743 | 2026-10-07 04:00:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 127.6 |
| 967842d0-5fe7-3daf-a93d-173c52f04817 | -3.0375 | -53.9066 | 2026-10-07 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 2b32df0c-aaf5-3d98-acf0-58961f650b11 | -3.658 | -60.6222 | 2026-10-07 04:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| df657a4a-fe76-32f4-9b3b-f3a6080466de | -3.6579 | -60.6412 | 2026-10-07 04:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |


[Clique aqui para ver as próximas entradas](README35.md)
