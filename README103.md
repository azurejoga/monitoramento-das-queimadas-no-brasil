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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64e767f4-b3b7-3957-888d-672cda3c3cf7 | -3.33121 | -53.21953 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7c4277b-f880-393a-b902-b5b44c01ac98 | -3.33052 | -53.22427 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27c01dcb-a844-38a6-b24f-01b3f4866d46 | -3.32748 | -53.00228 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2ba8e60-f9af-3033-af95-423dd2cbd005 | -3.32673 | -53.00725 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81633e68-296b-38d5-bba9-5c520240badb | -3.32403 | -53.0054 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afce1872-7aba-342f-a192-6d2cb1a45b31 | -2.98536 | -52.90314 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e67650b4-702f-3998-b13d-79cc8e347fc3 | -2.98462 | -52.90813 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 8e9dde87-4dc8-3ede-a1a5-b9f476595b65 | -2.98388 | -52.91311 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c08f561c-5bbf-3507-bcfb-d4f4c8567035 | -2.97914 | -52.90199 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 75cfba68-6dd6-327f-b0c3-c7caeee22097 | -2.97838 | -52.90712 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9f2b625b-46b1-3af8-9f7a-04d3af4694c5 | -2.97762 | -52.91225 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d51087bb-78ac-33ea-b0d0-6788f0d0dbda | -2.97287 | -52.90113 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8d682d24-64aa-3644-8d0c-4e7b7555170b | -2.97211 | -52.90627 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e7352020-09dd-3b0a-bf88-3bd9b881ee82 | -2.97136 | -52.91133 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e23fd1e5-6810-3e27-8b4a-8bcb22c92b58 | -2.96658 | -52.90039 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2eb98b93-0b13-3392-8512-225cbb4fec24 | -2.96582 | -52.90555 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 03b3930e-36d2-324b-9f2a-f4efabeeda53 | -2.96505 | -52.91075 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 12367047-9c67-3f4d-bfa5-bb7d362a51ae | -2.96031 | -52.89957 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 60a4b29b-a909-37a0-afe3-db300148c062 | -2.95956 | -52.90468 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8cc75503-3ba0-388a-8ccb-dd1735da3e91 | -2.95879 | -52.90988 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 00901a60-0218-3969-9121-e915ae5bbc8e | -2.85365 | -52.90741 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c43d579-821c-36a1-ac9f-aa8d1d7aa9f1 | -2.84924 | -52.93729 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e75f3c43-a576-3b07-bd5d-04cd4aa61ac1 | -2.84743 | -52.90632 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 635e3e5a-32ee-360b-973b-0ba3567f0198 | -2.84302 | -52.93627 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 710b33d7-822b-3dee-bf75-f5f6e88b1270 | -2.78382 | -52.48188 | 2024-10-11 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c18f94f7-bb63-38ed-a0fc-0393484693c8 | -2.78313 | -52.48148 | 2024-10-11 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ac80b08a-8575-354b-ad51-94b0a819faa5 | -2.78306 | -52.48709 | 2024-10-11 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9ac93879-445a-35ea-a96e-84d511ad7605 | -2.78233 | -52.48668 | 2024-10-11 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1e442623-b2fa-3748-9506-8ee3f724bcc7 | -2.77742 | -52.48092 | 2024-10-11 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d62b08a2-6715-35f3-a003-7fed8af7d2e1 | -2.77672 | -52.48053 | 2024-10-11 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7b51044f-8f81-3b2f-bbd8-bbc3e20dcb29 | -2.77666 | -52.48614 | 2024-10-11 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d95e07ac-cff6-3e17-99a3-1c26421604cd | -2.77593 | -52.48574 | 2024-10-11 05:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0f8642c5-d177-3b69-a850-a78df8a9183c | -2.8423 | -53.32091 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33999199-d473-343b-b5ae-d43549bf74a4 | -2.83622 | -53.32001 | 2024-10-11 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8c46fd2-35f6-3a1c-87c7-09c4e8843f06 | -2.68195 | -53.34784 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7d6d698-9ab2-33d3-bc15-652499dc32b1 | -2.67724 | -53.33781 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82838f66-51d5-316c-ad49-708fbddb2b09 | -2.67657 | -53.34236 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96dab820-32fe-311e-95e2-c47c95d12996 | -2.6759 | -53.3469 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3bbbb7cc-fd2f-3e70-b4dd-e4134081bf0e | -2.67523 | -53.35143 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cee98ada-891d-3b47-9db4-fd6097153c2d | -2.67051 | -53.34142 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ffa0a5f-31c9-37f6-aa71-0dcae952020d | -2.66984 | -53.34596 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30af2693-5fe5-391e-820f-b4813ce402c4 | -2.66918 | -53.35049 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c95e5c5b-6291-3019-89ce-d39a38240e47 | -2.66851 | -53.35501 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 20b593e3-5d2a-3905-ab93-c3b9bc53e6c4 | -2.66379 | -53.34504 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed5a49f0-0ce2-3ec6-8c20-b1ef8bffc549 | -2.66339 | -53.3438 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f542c2b8-98c8-388d-986d-635a82c45eb4 | -2.66312 | -53.34957 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d9efdb59-db79-3c84-b46e-15ee488f12d9 | -2.66269 | -53.34833 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5408aedb-e370-3c53-8c1b-8c06a2dbd202 | -2.66245 | -53.35411 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2d204ea8-9af7-3dd8-bdd3-b4305edc7f5a | -2.66199 | -53.35286 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 39ef1155-0998-3d77-aafb-9ce7635379b3 | -2.6613 | -53.35733 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2d067cdf-b7cb-398b-bfcc-7cd10761c94b | -2.65773 | -53.3441 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 04c025a2-0a9b-3ed2-93b0-39fd9e390b36 | -2.65707 | -53.34864 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 21325ab8-a21d-3f37-bbe6-70396717baf1 | -2.65664 | -53.34741 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b5572a54-b738-32cc-a02c-ba706abba673 | -2.6564 | -53.3532 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9dde16ed-a96a-3c79-87d2-0d91df8d2eb3 | -2.65594 | -53.35195 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 750ef826-a923-31a7-b0ff-3d837b483568 | -2.65525 | -53.35643 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9bb33c6a-8e6b-3a23-9c2b-5238eece8211 | -2.65101 | -53.3477 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 513ace22-b3ba-3e2b-9a20-d26380e578af | -2.65059 | -53.34648 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cde9d58-a8f5-387d-a015-616491c93a44 | -2.65035 | -53.35225 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a030c9d3-cd5a-3f8c-b4f5-4391c3de708d | -2.64989 | -53.35101 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86408fd9-3837-302b-94c4-9eb408b37770 | -3.83375 | -53.5857 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 631d795d-7654-3433-891c-5a7002023d55 | -3.8277 | -53.58464 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73f19ba9-373d-3ed6-a300-46deafdfc6db | -1.59334 | -53.34561 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f50e921-65f2-3d54-9be1-2630194da5b8 | -1.58918 | -53.34694 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9de29f5-cfba-3af9-a693-fe6f823d55a5 | -1.58735 | -53.34484 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c726a8bb-fbe7-3cca-8b68-f5be7af49600 | -1.17628 | -53.38507 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e93d947-fbde-3497-b7b0-e8b2ed186466 | -1.17563 | -53.38929 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2f4c7b1-c160-3a3f-a597-2da086694334 | -1.17434 | -53.39775 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6875e95-00ca-3121-90af-340b69313973 | -1.1737 | -53.40193 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83e4dd25-5037-3b46-b8a2-99297cf98a9c | -1.16841 | -53.39697 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f05a892-0aae-37d1-9532-6e50856b2b67 | -1.16547 | -53.39479 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0a2767a-b6ff-38ef-b873-b2fe2769c9f1 | -1.16481 | -53.39895 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4efba6e-0b62-3e43-a1ad-025fade27f5f | -1.16415 | -53.4031 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 210154dc-a126-3f53-8cf2-04aa614596b0 | -1.1625 | -53.39609 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 314ad1e5-d487-3c9b-9c62-283251168496 | -1.16187 | -53.40028 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5527c6b-3a4c-3917-9863-bbe8f1e93355 | -1.16123 | -53.40448 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3770ed0-7a43-3312-a24c-bac383f52a75 | -1.1589 | -53.3981 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56cff5aa-4a31-34d8-9211-9676ea6ddf04 | -1.15822 | -53.40235 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6098d763-60c4-394d-b2fe-791d9853414e | -1.1566 | -53.39518 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 415b4f7f-97b2-3891-bc5c-42ea4e529ddf | -1.15595 | -53.39945 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83963225-6ae5-37cd-aac6-92ce92f31ecc | -1.15299 | -53.39723 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4409fed-d589-3248-9dbf-60570585c2ae | -1.12684 | -53.63699 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f04a1d6d-835a-3672-8676-99c9c97c1335 | -1.12619 | -53.64101 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec29aa65-036a-3700-8691-60112ed5192c | -1.12561 | -53.63897 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba50a7ef-1f32-3e10-a955-a0768b66c5b2 | -1.12537 | -53.44219 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d358587d-9f0a-3765-9bd9-cfa10acef830 | -1.12501 | -53.6429 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60bd767d-6280-388f-bf88-73df7bba0cfe | -1.12476 | -53.4463 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8557ac5-9963-3159-b41a-c5162c81be8e | -1.11254 | -53.61454 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccf83451-23b9-33c2-a001-3500a2ee3846 | -1.11182 | -53.61905 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07529518-e9ef-392d-90ae-f68e57e9fd2d | -1.11117 | -53.61645 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41e4d1d2-4236-3318-96c5-74d1988068f1 | -1.02362 | -53.7282 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cb38bef-89ce-37de-b3a8-fad351d7f786 | -1.02294 | -53.73262 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e32532e4-4666-3c93-9230-002309569930 | -1.01779 | -53.72772 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2e8e3eb-ace4-3152-a45f-d333cabf2074 | -0.94122 | -53.72145 | 2024-10-11 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 923dada4-4357-3c34-a59c-e108751ba9ef | -1.5722 | -54.76219 | 2024-10-11 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f762f9d3-2f0d-3cd8-bac7-edb958017ce2 | -1.56678 | -54.76133 | 2024-10-11 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a691335-6860-3f6b-89a7-2685a5f0a605 | -1.25782 | -54.68473 | 2024-10-11 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2432ec2-dfa0-352a-8eb4-406ae0b2d129 | -1.25237 | -54.68401 | 2024-10-11 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07054800-c4c6-3b60-b84e-6cbab29f47a3 | -1.19593 | -54.10838 | 2024-10-11 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61ceef11-e5e3-3d01-815f-95f537887e4e | -1.19079 | -54.10429 | 2024-10-11 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README104.md)
