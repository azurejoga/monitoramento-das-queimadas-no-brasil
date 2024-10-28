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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b2ba752-e2cc-3763-8dff-6f43e780722d | -3.59825 | -49.35984 | 2024-10-28 05:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e317fd32-0ca5-3b02-bf96-25bf8ab41663 | -3.50138 | -49.9446 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e6bcd31-ff48-381f-ac0f-b70bcdb9e1b2 | -3.49632 | -49.9398 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b06e8af4-ee4f-35d8-9744-e0572dfc9865 | -3.44067 | -50.08755 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb29e3af-df78-3d6f-9610-a8b5613a03ee | -3.44013 | -50.09133 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e44df4-a72d-3a34-a180-6d213a54062f | -3.36648 | -49.53096 | 2024-10-28 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c79bfd80-ebd1-3462-8bae-d1ca93308280 | -3.36589 | -49.53495 | 2024-10-28 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76481dc0-3bd8-3c26-9742-b9f34e1964d1 | -3.33862 | -50.09355 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48791eb8-f5aa-3be5-8fa6-15dbe1b90e11 | -3.33523 | -50.09068 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1de4045-35b5-3f05-bac8-74ee84efee5c | -3.33468 | -50.09432 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b151e80e-6d83-3476-8c50-4c52c61e4a42 | -3.33303 | -50.09288 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc97f1b6-d92a-3833-9d07-adf2484eb1d5 | -3.33227 | -49.91975 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0704e906-5d33-39df-b7c8-74b8e41aa30f | -3.33171 | -49.92352 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5173238a-97ad-3334-b36f-7ea9d2c194a2 | -3.32664 | -49.91894 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa2703ed-83bc-36dd-bb86-6c89a5d7fd26 | -3.32608 | -49.9227 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80fb0554-6002-39f6-9894-f9ae7cd6d511 | -3.27093 | -50.02488 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ff558ca-78f0-36f8-b3f8-0e152126c145 | -3.22604 | -50.17918 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5e70b01-d917-39ca-b746-677308ee0b77 | -3.22594 | -50.17829 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b42f0aa6-988d-3a1d-a944-b7ccaba2c5c9 | -3.22104 | -50.17491 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df860e90-301c-3c97-a0f1-625520ea6c12 | -3.22092 | -50.17397 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef031637-cd36-3d3c-903b-4e229f4f81b3 | -3.22049 | -50.1785 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3feb930a-7015-31e6-a61a-a4f6e55a18e8 | -3.2204 | -50.17756 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78ab6392-97b5-3156-add0-3b99f805c4b1 | -3.21644 | -50.16586 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69459ca3-ac3e-3ab0-9173-3209813d2e04 | -3.05334 | -49.48586 | 2024-10-28 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| de46d7e8-3d0a-3efe-81c0-799724fd8538 | -3.05274 | -49.48991 | 2024-10-28 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 583f5095-90bf-364b-812a-535287fd8a14 | -3.05214 | -49.49396 | 2024-10-28 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ca81213-9724-3725-b785-fe64a0102a25 | -3.05155 | -49.49795 | 2024-10-28 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ab882c6-f606-398b-a72a-27568059607e | -3.04697 | -49.48909 | 2024-10-28 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d3ff947-9aa4-357a-aab8-010358eda382 | -3.04637 | -49.49311 | 2024-10-28 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a9acb85c-9db6-374f-aafe-e6e0b427492c | -3.04578 | -49.4971 | 2024-10-28 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1c8aa0ea-e716-336d-95bb-103df704dedf | -3.04522 | -49.50093 | 2024-10-28 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3584023c-ef59-380d-b07e-aadc5e959ca3 | -2.93212 | -49.54876 | 2024-10-28 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 325f5539-e70f-3965-b106-3cb671e501c6 | -2.88625 | -49.50126 | 2024-10-28 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 053a0890-4b4d-3117-b208-30587cecf300 | -2.88567 | -49.50523 | 2024-10-28 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27a3b88f-0eb2-3ef9-916a-3978f5ebebac | -3.43428 | -50.25027 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e726d68-b26c-3634-92b8-9eb01fa3a6bc | -3.43396 | -50.25274 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0c2ed02-c2d3-3130-b89e-8fe2dd7f3817 | -3.43376 | -50.25384 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52c9a715-7560-307f-b0b1-5e70e01238f7 | -3.31827 | -50.23508 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de531674-edbb-39d8-889b-898aa7f1e34d | -3.31775 | -50.23871 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5177207-f720-3db6-95f6-708c4262daa9 | -3.2553 | -50.36078 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37b0c53c-3330-312a-93a4-2adb8e154c3e | -3.24984 | -50.35999 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41611e8c-e5d3-3ff4-a3bc-a78083a3a5d1 | -3.20925 | -50.21584 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 190f1944-421c-38dc-9e5f-7a6167da5ed4 | -3.20905 | -50.21674 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d29b187-813a-3e48-a9b4-a7e4856c5178 | -3.20872 | -50.21954 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ea7113a-9712-33a3-a3a8-268eb3e08bea | -3.20848 | -50.22049 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b531695b-784a-39c4-b20c-49f1cf626ee5 | -3.17737 | -50.38895 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b61e1261-d459-3f0d-8355-0f3bc4cc61bf | -3.17685 | -50.39241 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8eeb99ba-bd6a-32d0-ad2a-d91492372e5d | -3.17633 | -50.39586 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce3600e7-cd50-3822-a939-5aabf51e4d98 | -3.17193 | -50.38813 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd46f599-c1d9-31d1-9a82-3394ab929eda | -3.17141 | -50.39159 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31037d7b-d600-36e0-948e-b97c962a2a45 | -3.1665 | -50.38727 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c95787b-4ed7-3cb7-9c54-4c8e5aaf2788 | -3.16598 | -50.39074 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c43b1b87-1e1c-3f12-bc5a-863c1c7401bf | -3.15508 | -50.46312 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4ae984a-bde9-3790-b61c-934a87ba66ec | -3.1507 | -50.45543 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5862c19-8348-3e5e-a755-53c7fb616b4f | -3.15018 | -50.45888 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6557a05-4428-30af-a194-a2b16260f4d4 | -3.14966 | -50.46231 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a31dd431-5b82-3cbe-8853-de46dfb17e3d | -3.13277 | -50.3143 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecbe134f-6f37-36b4-8b49-161b91c76cbc | -3.12217 | -50.34837 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f6908e0-cc9b-3822-90e9-a5adfb469f69 | -3.12167 | -50.35179 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3de9113e-756b-30e0-bb7b-91596ca9dc5f | -3.12116 | -50.35525 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ae9da7e-ce62-3112-bb14-749f1bf3abd8 | -3.11671 | -50.34759 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1c6b5f9-59f4-3fdd-a586-128f5939e1fb | -3.1162 | -50.35104 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba2d2b96-7d75-30f7-8e9d-1948065f18b2 | -3.1157 | -50.3545 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed34b220-0fad-360e-9d00-faf976c0b3a4 | -4.74831 | -50.82446 | 2024-10-28 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 508ef062-dd7d-35bf-815e-ab06f9dd79b2 | -4.74782 | -50.8279 | 2024-10-28 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 782c176b-d930-3cbb-8e20-c4d563f7b4b2 | -4.73732 | -49.3918 | 2024-10-28 05:23:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5aec7758-d151-390f-afa0-731bd07b463a | -4.7367 | -49.39618 | 2024-10-28 05:23:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7c727f5-b84b-39ff-b5ba-8029c625eb39 | -4.73503 | -49.38976 | 2024-10-28 05:23:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7cd97c10-d479-3c1d-9bac-e2d61aac5faa | -4.73437 | -49.3942 | 2024-10-28 05:23:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f3c452ae-6961-3b1f-817c-b798c91de681 | -4.73134 | -49.39112 | 2024-10-28 05:23:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af28f8c8-a62f-332f-bd07-8242d39745c9 | -4.73071 | -49.39564 | 2024-10-28 05:23:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33b0c62f-d662-3cb7-b06d-e9d8310958d0 | -4.72906 | -49.38903 | 2024-10-28 05:23:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e44a39b3-11bb-3ac1-b758-0cd52ece2df5 | -4.72839 | -49.39357 | 2024-10-28 05:23:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b6792410-9c7e-3e2a-a9ce-3f4140dfee35 | -4.72539 | -49.39028 | 2024-10-28 05:23:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22f03808-4bac-337f-a16a-3aae4d0edf7e | -4.70167 | -49.60354 | 2024-10-28 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43a7bced-d7ec-3b69-b805-7cca0a37fb55 | -4.70107 | -49.6078 | 2024-10-28 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4c8614b-5b10-31d7-848c-22dca7defa59 | -4.38587 | -49.75385 | 2024-10-28 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b9735e3-fdf3-3e35-8859-7af969d7fc16 | -4.3853 | -49.75778 | 2024-10-28 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9be8fd5d-3911-3b0d-bf59-4737b707f63d | -4.11652 | -49.26056 | 2024-10-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea387455-8384-38f5-ad09-e41b2fb93a12 | -4.11352 | -49.25742 | 2024-10-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f80e805-6126-3c03-8978-016c8d13f914 | -4.11291 | -49.26173 | 2024-10-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3e71065-4580-332c-ac35-2b787088f5a5 | -4.11057 | -49.25974 | 2024-10-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f5618f7-a1b3-35db-8cab-c20ddafc7d1a | -4.06865 | -50.01962 | 2024-10-28 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f71dee35-ef75-3220-b74f-862168c8f4ea | -4.06809 | -50.02346 | 2024-10-28 05:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94281b06-9332-3809-81c2-cd561a30de34 | -4.06752 | -50.02733 | 2024-10-28 05:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 858ffb20-dc7b-3cb5-9795-f5672a3ae824 | -4.06695 | -50.03117 | 2024-10-28 05:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97919109-1084-3825-819c-d7de91a96121 | -4.06241 | -50.02282 | 2024-10-28 05:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 167c4b36-208b-395d-b2b0-32ca511cceff | -3.99274 | -49.98523 | 2024-10-28 05:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 624af006-4475-32e0-b947-dd1d907f41d9 | -3.99219 | -49.98912 | 2024-10-28 05:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b203e48e-dc90-3f14-9de5-c7feff57db1a | -3.99051 | -49.9866 | 2024-10-28 05:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 142b3cc0-c00a-3217-9ac7-d1d4a5e92055 | -4.12141 | -50.50201 | 2024-10-28 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1367415-e624-3143-84f7-c9e3fce64c4a | -4.12089 | -50.5055 | 2024-10-28 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd2f7b01-3d01-354f-8d17-223773cc531b | -3.67474 | -50.29514 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f77c7fb8-ab5d-3f21-affb-337fd6d0339a | -3.67421 | -50.29878 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c42527db-a85e-3f54-9354-f255a234ae46 | -3.66923 | -50.2943 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3b0777b-4fb5-38c5-abf8-5c1e741012d5 | -6.21361 | -50.85271 | 2024-10-28 05:23:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff2e8c01-670c-3af4-ae85-3bc5c6244e0b | -6.21309 | -50.85633 | 2024-10-28 05:23:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c94641b4-5594-3e8c-a8a7-9980b23e74d5 | -12.59949 | -52.45215 | 2024-10-28 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3d213d3-53e7-3320-9876-d6517518499b | -12.59905 | -52.45567 | 2024-10-28 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f8a2c23-4be6-368f-8074-a308e05415be | -3.03489 | -51.46313 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README80.md)
