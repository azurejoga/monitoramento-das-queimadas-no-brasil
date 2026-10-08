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

## Dados Diários - Página 400

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c3ca005-da29-3dad-b8ed-30aba618983c | -7.4697 | -42.8315 | 2026-10-08 19:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 159.0 |
| 5738e423-1811-3834-807f-2c4f5ff3222e | -6.509 | -55.9554 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 230e9172-5507-3362-9fcb-4c2ce2dc89a1 | -2.9633 | -54.1095 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 7247846e-2d3a-36ba-84e4-c978051de315 | -12.2311 | -44.7661 | 2026-10-08 19:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| fd186d06-89ff-3500-8ce6-3d290b7180c8 | -2.9005 | -56.6685 | 2026-10-08 19:00:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9388568e-00ef-3a56-adad-213aa65879f6 | -5.0575 | -46.1859 | 2026-10-08 19:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 1bf0aaff-2f69-336e-9c57-a6a213e00502 | -6.4032 | -55.1842 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| d10b7d3d-b062-37e4-8d82-792c3760927a | -11.2482 | -46.2604 | 2026-10-08 19:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| f342fb9c-eb7d-3904-b6a3-3db5b59424d7 | -3.1484 | -53.7225 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3b4a5e9f-819c-3a06-8685-a2af70f270d8 | -7.1894 | -44.2811 | 2026-10-08 19:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 84e312ff-4426-34a2-a2bf-a1038073ea3f | -8.2435 | -54.7183 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| cea0cfe7-d520-34d4-86f6-cd84a9b9b7fa | -3.1879 | -58.6433 | 2026-10-08 19:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 75adf713-5b02-3a04-845a-20e37f6d9cd6 | -2.0759 | -56.8784 | 2026-10-08 19:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f56acf4c-9dca-3c8c-8254-4d89739adbc8 | -3.1874 | -58.8358 | 2026-10-08 19:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 57bd917e-7de0-3a03-8924-368779b70b66 | -7.4097 | -44.7427 | 2026-10-08 19:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 1db98a6e-fb8b-3938-b093-fbbaccc7d826 | -1.7681 | -55.0309 | 2026-10-08 19:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 821437f9-dad3-3a6a-a5ea-3405e421eef9 | -2.8712 | -54.1719 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 720b056a-6f14-364d-98d8-c6cc7929ee85 | -6.1617 | -52.6471 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 383a1efc-c7e2-3cdf-ad2a-7307a614297d | -4.0629 | -51.03 | 2026-10-08 19:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 15c43947-d607-32c9-b945-31f3ecaa4562 | -6.3134 | -54.7884 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 94cd1bbd-6c3c-3925-9860-3e7b05d7484c | -2.7613 | -54.0941 | 2026-10-08 19:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 6fda82fa-c36f-32a1-9146-f65e194cdba4 | -2.7152 | -57.472 | 2026-10-08 19:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e8292b37-a7d6-355a-96ab-27b7c93090f3 | -3.2717 | -50.4102 | 2026-10-08 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 32960566-db4e-3fca-bbf5-61bee44cdc1f | -3.2136 | -42.9764 | 2026-10-08 19:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 421.4 |
| e43595a2-5e0b-3bf0-88b0-5a7336ec4952 | -2.8433 | -57.4891 | 2026-10-08 19:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ce8dc9e1-6d3e-3086-81bf-e64640b1a8ef | -14.4591 | -41.1854 | 2026-10-08 19:00:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 159.3 |
| a3d7c01d-e0b2-3768-9655-d2945921bc3a | -2.9447 | -54.1702 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 73c1aa61-0ca5-335f-9326-89a0c6d0170a | -3.1115 | -53.7637 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 1377f425-fefe-35c0-9660-78d2ab6f9350 | -5.8599 | -53.4586 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 9b960b23-cb34-3d39-a097-887436893566 | -2.9449 | -54.13 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dc8d423d-ffa6-346a-b706-07bdc81fb279 | -17.2351 | -39.4926 | 2026-10-08 19:00:00 | GOES-19 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 110.4 |
| c0e1536f-16f1-3217-a2cc-38e23808fa52 | -7.5354 | -42.088 | 2026-10-08 19:00:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| bd131e72-e2e3-365c-814d-97367116e83e | -6.0075 | -53.5122 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 94171406-5da4-3806-afde-998c51809365 | -7.089 | -52.6958 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 224.1 |
| 802e6f13-8b4e-340f-ab02-374b0bc5b232 | -7.2187 | -55.0815 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 603b57fe-7a0e-34cd-af68-844df6859cd6 | -11.619 | -43.6196 | 2026-10-08 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 722.9 |
| a9d82ee3-b863-300f-be8c-08d76d89f904 | -3.314 | -53.6979 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 53ed19b7-ab1a-382f-bd63-86c2d5c6348e | -4.6364 | -50.9437 | 2026-10-08 19:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 180.7 |
| a34d2ded-7f4c-39a6-8faf-4f0f3e0bef76 | -2.0649 | -46.577 | 2026-10-08 19:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6cbc635d-9829-3183-a9f3-77f9a1221f36 | -7.2372 | -55.0805 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 2c27cee2-3d88-3432-aa25-045277484a0e | -2.7517 | -57.5297 | 2026-10-08 19:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 4b35232e-dc32-3048-a147-964d80925a6f | -11.7545 | -43.5512 | 2026-10-08 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 41c23d99-d9f8-3770-9df8-11465a28b751 | -7.4508 | -42.8334 | 2026-10-08 19:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| bcaf5d31-582a-3dd8-b947-4c5f8d9127d3 | -3.8749 | -55.9961 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| de52e793-a856-37dc-ac0e-20e659ea51bd | -15.2541 | -42.3495 | 2026-10-08 19:00:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.0 |
| 7e04c160-46f8-31a1-ba10-e9925c5f3481 | -6.1429 | -47.9432 | 2026-10-08 19:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6d2355e6-0ea3-3e61-ad69-4e1b3fc4f57b | 1.7488 | -55.5663 | 2026-10-08 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| c1c6292a-3ee9-3542-9cc2-1a44ca495cbc | -5.5146 | -42.8399 | 2026-10-08 19:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 740addce-38a2-3b9e-9c4f-0eaa36fbde06 | -8.5921 | -67.0491 | 2026-10-08 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.1 |
| ab0e0cd8-b142-3478-85df-8141077fbb72 | -2.7612 | -54.1142 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 087b316d-3cda-3628-bf0c-2e6468708136 | -6.4567 | -55.4809 | 2026-10-08 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| e868e989-834b-3cf8-b80d-0ab19dc00132 | -3.3142 | -49.1195 | 2026-10-08 19:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 587b3e93-73cb-3806-af6b-2047355b435c | -2.4942 | -58.0768 | 2026-10-08 19:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 0d56ac44-890d-386a-9fd8-05ecbbeaf332 | -8.0764 | -45.6339 | 2026-10-08 19:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b2ef885b-7af0-3d9e-b453-6d632970e17a | -2.5491 | -58.0566 | 2026-10-08 19:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 50be8317-4f9d-3c55-9911-bab7826a8812 | -5.5144 | -42.8634 | 2026-10-08 19:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 91b6841d-95fd-3971-8406-91750e391cb7 | -2.5069 | -47.3771 | 2026-10-08 19:00:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 1bd082aa-b5d3-3b48-9aeb-b23d4b2b4a2b | -3.6603 | -54.512 | 2026-10-08 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 559c1369-a481-3c89-b0b8-5c167f0a9fff | -8.5922 | -67.0306 | 2026-10-08 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| f8498436-b65f-3511-8fc4-31c14000963a | -1.8233 | -54.9307 | 2026-10-08 19:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 59ccf80e-4b75-30c3-aca2-ccb0a12cde39 | -3.0992 | -57.6589 | 2026-10-08 19:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 09754a6f-c646-3fdd-ad74-b3f3aeb6e06f | -9.8442 | -47.4608 | 2026-10-08 19:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 560cfd67-c5a0-3fa8-bcd0-9462e3d7185f | -3.1697 | -58.6244 | 2026-10-08 19:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| b295f75d-6ece-3c5e-8210-34b2d4f5f6b3 | -3.9483 | -56.0138 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| d32cd87b-e0df-3a6b-b154-9ca5a7525a91 | -14.0873 | -43.7671 | 2026-10-08 19:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 3ede2d7e-ecb4-3621-9ad5-56fa74528316 | -9.8439 | -47.483 | 2026-10-08 19:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| eac54a76-6bac-32cb-b4ac-21bf83343eca | -2.9265 | -54.1305 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| d72dc657-e109-35ef-bd72-f0c456a2bf60 | -3.2956 | -49.1415 | 2026-10-08 19:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 438ec615-c1ba-37cc-a87d-e7dd87328f3c | -2.7428 | -54.1146 | 2026-10-08 19:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 338.5 |
| b80ca264-2340-3748-8f8d-6756d49b1c8a | -6.4905 | -55.9563 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 259.8 |
| 70447b57-3372-32e1-8fc8-eafbca482d6f | -8.9302 | -45.2041 | 2026-10-08 19:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 499.1 |
| 2cf42c25-9ecb-30b6-b908-ec4a9f89770c | -5.4958 | -42.8413 | 2026-10-08 19:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| da1f5984-acdc-341f-adf8-c197c59c3f2a | -8.5183 | -67.0139 | 2026-10-08 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 4909bfcf-fbde-366a-932f-0213bdff90af | -3.1602 | -50.5812 | 2026-10-08 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| cbabe3e9-1395-3309-bc00-6dd049e72038 | -3.2533 | -50.3899 | 2026-10-08 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 42b96aee-4fce-3d5a-84ee-ac7e9b727b63 | -1.3264 | -56.398 | 2026-10-08 19:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 897b75cf-14a5-3893-b6a5-881504becb25 | -5.3905 | -44.1968 | 2026-10-08 19:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 866620ab-45c1-3054-b302-e693d2fd27b4 | -8.9305 | -45.1812 | 2026-10-08 19:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1076.6 |
| 47ec15df-36ab-3066-8bb2-25e079b1fea0 | -8.7225 | -46.6693 | 2026-10-08 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| ef7ee8fe-af2a-352b-8102-032e0f3ebc70 | -6.0744 | -43.1478 | 2026-10-08 19:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 207.0 |
| 5455b8fa-ba0f-3bed-a855-f899985b5e0b | -3.0256 | -57.7768 | 2026-10-08 19:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 5b98590a-6948-37af-a5ab-24cb40778ef3 | 1.7672 | -55.5463 | 2026-10-08 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| e4408bfd-0c08-3af1-b042-5d7b31e40100 | -8.3011 | -45.7245 | 2026-10-08 19:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| b7ad6986-9d08-35f3-8b72-b9298238df0a | -6.2348 | -52.7866 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| ff1965c1-86c3-3bc6-85c3-cac7aacb4357 | -11.776 | -45.5495 | 2026-10-08 19:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5552e6ba-d00c-34a2-96e1-90db727dd728 | -7.9086 | -54.7194 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 7be913f3-acd6-349d-b807-2c2b9b3e26d8 | -3.2955 | -53.7185 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 01f71ef7-5414-3308-a313-b22277716a4d | -8.9308 | -45.1584 | 2026-10-08 19:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 506.8 |
| f72a8060-6fa7-308b-bfc0-bea7642b474e | -12.2316 | -44.7427 | 2026-10-08 19:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| d1d2d86e-8f1b-3e67-a508-8a749a55902b | -3.5193 | -58.0376 | 2026-10-08 19:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 4b1e77c2-47c3-38ab-b7a5-704df82a710c | -4.6641 | -56.2281 | 2026-10-08 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 22522d10-8eaf-39f1-a524-dbe6dfe155af | -2.8163 | -54.133 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| c83704ed-59c8-338f-8783-deb2da99fe9f | -3.7809 | -41.7913 | 2026-10-08 19:00:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| deea4d87-1b9a-3beb-8c01-9f170a78a725 | -2.572 | -56.1646 | 2026-10-08 19:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 2d1c0ebe-5de4-3b67-a049-f800bfb0fdd1 | -6.8907 | -45.8988 | 2026-10-08 19:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| f859260b-ee29-30e1-97bc-ec71ca4d8d4a | -2.0576 | -56.8786 | 2026-10-08 19:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| be162906-55c4-37e0-93bf-04236e3fa135 | -11.2478 | -46.2831 | 2026-10-08 19:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| e56e1cff-d3ed-3d7b-b6ba-cf79fcc66fe5 | -15.1057 | -43.6168 | 2026-10-08 19:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 118.9 |
| 178f6d7e-775d-348d-9b32-f14a3914f743 | -6.9331 | -43.6566 | 2026-10-08 19:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 57ae7202-0014-33d6-9824-9098e21d64f3 | -3.8383 | -55.9774 | 2026-10-08 19:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |


[Clique aqui para ver as próximas entradas](README401.md)
