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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bfbcbfa-8fd4-3929-914c-29dc2b2b6f4c | -2.9449 | -54.13 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e27d7738-c996-3c23-b26d-e2d3ef310fda | -3.0917 | -54.1666 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 5392232c-695c-3c1c-a270-18678451b2c0 | 1.86822 | -55.8094 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 440c821a-1b59-3db2-947d-2dbfae006993 | 2.08875 | -50.8816 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b345f116-3d24-384c-9e74-02b8bd7147e2 | 1.87542 | -55.77306 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a5166a4-e23a-3d60-85bb-dc174ce00327 | 1.87295 | -55.79854 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8402e908-6d30-39fb-a1bb-f775e5ee85bd | 1.85723 | -55.82133 | 2026-10-05 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f1b04534-9811-3802-a454-0d0785e90da8 | 1.86196 | -55.8104 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 640a2029-df27-3bad-bd95-848d3c4bd532 | 2.0766 | -50.89267 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41c0dc7c-74fd-32fe-8278-113d04e34fa3 | 2.10443 | -50.74726 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f3216d23-b2c7-3ea6-a61f-bbf82341e723 | 1.89952 | -55.78363 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6283ac77-0afe-39c5-a95e-4b7662205ca0 | 2.00728 | -50.92843 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c1f467c-6f9c-3b3a-afde-94d49cf0615d | 1.85097 | -55.82233 | 2026-10-05 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| da061d9c-59c1-346e-b146-2b657d8fd975 | 0.70289 | -51.43406 | 2026-10-05 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 049a3a1c-4066-3d6f-b2f3-c72800d9ae8f | 1.85022 | -55.81741 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 67ee2ebb-e280-3ac6-8b83-22dff0515e7a | 2.08493 | -50.88678 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d53908db-992e-384b-b377-c1e86d130dba | 1.14037 | -51.33152 | 2026-10-05 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20c2c496-2128-3a98-ae63-c622ea5d4170 | 1.84471 | -55.82331 | 2026-10-05 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65881504-5a30-39bf-9823-987080d60b69 | 1.73023 | -55.64552 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a259f6c-7f4f-3892-83a2-b15ef89a30cd | 2.10202 | -50.74516 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da98a8dd-08ec-3e1b-a668-0bdd1747e30f | 2.10373 | -50.74287 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33bd43ef-c07a-3001-98e0-993a3ca516bd | 1.85571 | -55.8114 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7d332a19-2529-3b29-bb33-504e6425849e | 2.0077 | -50.92635 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aec1bd02-c185-3acc-96d4-2157f9f0bb9a | 1.72406 | -55.64656 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4ddc54b-274a-3ae4-b6d2-6245d10fe905 | 2.08112 | -50.89196 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93200791-bec4-369d-bcc9-94d28c51210c | 2.35075 | -50.75547 | 2026-10-05 04:36:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0feef201-3d0c-3570-a5b5-a3621afca3db | 2.08042 | -50.88747 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70ae3499-39fe-3141-9e3e-0e3c97ddd726 | 1.72553 | -55.65617 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10042e37-0d1a-3897-9c5a-4d09a22f11ee | 1.87371 | -55.80347 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec6230de-9e9e-31b0-8a3b-a8a17f51a76b | 1.89644 | -55.78479 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 496cb19b-7733-3a9a-8b19-8ca803d435ba | 0.6983 | -51.43477 | 2026-10-05 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73565799-7b82-3ec4-a7b5-c97eba313261 | 2.0118 | -50.92773 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b511bbe-1c1b-3e3c-982f-238a759479b3 | 1.90025 | -55.78852 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79d79a3b-9c39-3a5a-be0b-61bf62be21e1 | 2.09326 | -50.8809 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a27f5a66-b8d0-30cc-b05b-e21a56ad29f3 | 1.86993 | -55.77895 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 196e2ac1-7944-3fde-8037-20ab8b5506b9 | 1.73097 | -55.6503 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 94aefa55-b8b6-3faf-8bbe-1c6628393bf1 | 1.85647 | -55.81638 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fe1c12cd-d749-39e5-813e-e01cacb918f2 | 1.7248 | -55.65136 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38e4f6ba-8a43-34e6-9dab-770fc13b8c7e | 2.01222 | -50.92564 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f42a4bba-18fd-3c38-99b6-8614ad9df542 | 2.09396 | -50.88538 | 2026-10-05 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9abf2325-c6d1-3020-aa13-7663db58786b | 1.85171 | -55.82721 | 2026-10-05 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 35332322-368b-3c19-b6c1-d56bab24202e | 1.86746 | -55.80446 | 2026-10-05 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f61b0da0-ec05-37bc-a866-137e71d40580 | -2.81618 | -54.12427 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dfedfb5-0d84-3e59-a043-e4db9a7cda4e | -3.06829 | -49.53868 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b304399-d4ea-331e-849d-7d75106c149d | -2.97708 | -54.0926 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c74df7c-6007-3d9e-a4b3-430ea2ea6306 | -3.28223 | -53.83653 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e0d4077-11a6-3551-bd9d-e4eaff4e5bd6 | -2.95658 | -54.15042 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 74ed3766-febe-3a53-9adc-c15c24625963 | -2.78385 | -54.09304 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b494e619-f563-3e96-ac1e-1d75814b4825 | -3.12204 | -53.71519 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c06535ba-73c7-3067-acff-9d6f9c947dda | -3.16102 | -52.21887 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdb4dfa4-f858-3ad0-857d-9bc21b6ac0be | -2.80731 | -54.11304 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 500ce706-2177-31c0-ac6d-fa47390b3972 | -4.04212 | -50.76239 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5883da85-64c8-330c-92bd-c43abf7221ce | -3.94039 | -47.979 | 2026-10-05 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34440e0e-8e6d-36fe-869e-1e374183d1da | -3.40602 | -51.67183 | 2026-10-05 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6cd49e4-38bc-3239-af16-dc936be15d6a | -4.27648 | -50.27169 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54943d02-169c-3ae8-9dbd-23aea2f620c5 | -2.16378 | -53.66522 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b7eeedd-a1df-33ec-ad24-c2dcd69c5f95 | -2.47033 | -48.03706 | 2026-10-05 04:38:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adeedb5d-3a16-3bd5-b299-31328bb6d8a2 | -6.01043 | -53.51143 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f1a1d562-dd74-344a-8a43-a50681a6ff22 | -6.90831 | -43.66705 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ceeef984-26c0-32ea-9a02-451f5da96d1d | -3.1251 | -53.72768 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58cc6de3-08f6-39c5-bfa9-971e63d8363f | -7.89648 | -44.20036 | 2026-10-05 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a45406bf-3b68-3068-9a87-c4c5aced840e | -3.27497 | -50.39761 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 38542d3f-a19f-3c07-8704-036ee26c5580 | -2.48515 | -56.09295 | 2026-10-05 04:38:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9490f52-ab03-3b7f-b306-a4101c48170d | -3.93933 | -48.43439 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b90a40d5-f2ad-3a08-982a-93f1d3e5cbfb | -6.90775 | -43.67638 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e93d8418-0c58-3741-9212-215e73fa32df | -3.50411 | -54.61729 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fd9eae9-464f-3d9e-b03e-ba17b689b9a7 | -3.27859 | -54.18069 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca44a7bf-f67c-3c2c-9da1-16d4547d5fb3 | -7.89767 | -44.19266 | 2026-10-05 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b32228e-1461-327d-9b1d-48ef35cb4b6a | -6.82015 | -38.52537 | 2026-10-05 04:38:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7dd36471-5a30-367b-a41c-b86ac633d3de | -3.11855 | -53.7356 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97e0570b-8d2a-3f9b-a1d3-42f6125c50d4 | -5.96926 | -41.32415 | 2026-10-05 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1e737fd-72aa-3afc-892d-2440a6e848a8 | -2.95297 | -54.14008 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 540a1fe6-7b11-3310-a0f9-cc38f2a27221 | -3.3011 | -53.84875 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af35b065-3455-39da-90aa-1bb7cb628a21 | -3.0963 | -53.72535 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5fc2c9d9-e651-338b-88b3-f338e93d4b4b | -3.61627 | -54.60211 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| facff3f9-364b-30b1-b889-3d577bb1ea51 | -3.5184 | -54.62991 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2dfa096f-6123-3bbf-9636-6280f68af8ff | -3.07477 | -54.17963 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ecff7d8e-4f1b-3d21-81bd-a6a4e130f2a1 | -1.09838 | -54.11621 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28c09383-bd43-3fb7-b63c-c03f76fea05e | -2.82243 | -54.11886 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b43a2fa7-c7df-39c5-8332-00ab4b4f400a | -3.32439 | -53.8501 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd28226e-85c7-3bc4-a47e-aaf2b606c4ea | -1.98432 | -54.42065 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c6d08ba-e501-3ef0-8900-4ec0693a4da9 | -6.71112 | -45.55435 | 2026-10-05 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17b58968-1a80-3ff5-94a4-2ed864acc370 | -3.10401 | -53.7417 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b5760c07-e20b-326f-ace3-599404520533 | -3.12311 | -53.73937 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad9ffdeb-45d9-3d05-9531-d25e3709f72e | -0.37988 | -52.04307 | 2026-10-05 04:38:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6dc7aa63-7aaf-3b3e-ba40-936cfe0b5aee | -2.78696 | -54.10649 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0287d35f-a48a-30e5-9ecc-52bff472a1a5 | -3.3057 | -53.85255 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75b5498c-0fae-3ac9-afa4-de63c203ced0 | -2.57744 | -51.8691 | 2026-10-05 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a74aa65-232c-37fe-9dd2-6261ebfb1fd8 | -2.8604 | -53.91956 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebe987e8-239c-3e5d-ad88-8c81d82f95a0 | -6.89651 | -43.67873 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e29d0caa-60e1-30d4-ab09-a70fc4f020f4 | -3.1233 | -53.75099 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8381a81-7b05-3ea0-a7eb-58da43b4dfed | -3.98521 | -55.81613 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d4679c5-27bf-3d26-a80d-40a1e72d536b | -1.97309 | -48.91246 | 2026-10-05 04:38:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c4dcfd1-a43b-3022-9222-0d0ff9f42e4e | -6.21822 | -52.68882 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb70aba2-1c7a-3aad-b9bd-0257fe05045e | -2.78591 | -54.11277 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 584fbc2f-5182-3ba6-9b66-e2f4702f558d | -2.85506 | -51.57933 | 2026-10-05 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c2cf02c-ccbd-302b-814e-4d9c0a09db5b | -3.66361 | -54.28329 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8153c27c-1643-32e8-b89c-889c06b13b8b | -3.12235 | -53.75684 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 08211683-d710-3e1d-ad97-476ba04823eb | -3.1105 | -53.73378 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f837c66-5074-33e6-aa1d-06ea0ce638a3 | -3.12253 | -53.71228 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README17.md)
