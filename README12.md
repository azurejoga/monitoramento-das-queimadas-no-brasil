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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85b7c48a-a610-3a72-b71b-2c476993fcfa | -3.08066 | -51.11021 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7aa90928-d397-3792-a217-06e52ad9b8cf | -3.08002 | -54.18125 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1a9e3299-a20a-3236-9eff-73248b76ec43 | -3.07943 | -51.10143 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 92a6650d-7c56-3c6a-b133-e95edc352663 | -3.07853 | -54.17024 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 7c3c5f04-7b1a-3fd8-b50a-d97bf3ff230c | -3.07704 | -54.15923 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3baff8bd-9769-3f5f-b0a7-cc3a25fd6c18 | -3.0762 | -51.27204 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0b7afc21-2743-32d9-9942-c77f3fc61971 | -3.07259 | -53.24076 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 04222fa6-3042-321e-8b87-0ab03873dfc2 | -3.07004 | -50.50293 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40ff5647-332d-3fd4-9345-cac0d1f66f93 | -3.0687 | -53.28159 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 27c5a37b-c992-3b2b-8191-b60e736c2006 | -3.06735 | -53.27174 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c85df8c-1cfa-3f51-953c-5681d6eb7bb2 | -3.06327 | -53.24207 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ca4a4dc2-98ad-3043-abf9-7fd01587bc94 | -3.06192 | -53.23228 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 34aa2c34-b6b3-3077-b7b4-e0cad294c402 | -3.05935 | -53.28285 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6d7b0b0f-021d-3404-91c3-9d9e411ea175 | -3.058 | -53.27302 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 49a3ecc1-dc00-3146-8898-7b329274386b | -3.05444 | -51.05122 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 924b76ef-4527-319c-bd18-60a98733b1ca | -3.05394 | -53.24338 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c1008507-5a63-38b9-8a5d-0ec4fb4dbe57 | -3.05383 | -50.38699 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0f386db2-85da-337e-8590-891be7f5bebf | -3.04194 | -51.02611 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1ec79e96-71c5-3211-a346-07491f2e91a0 | -3.0284 | -50.39973 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ab9d097-df71-361d-b77e-17469ba9e504 | -3.02762 | -53.86758 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a85cffaf-45f0-3159-884f-8e14d68f9dc7 | -3.0219 | -54.35659 | 2024-10-21 01:05:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ba534d1a-e1e8-343e-8982-dcc677c3d9fa | -3.02034 | -54.34509 | 2024-10-21 01:05:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| a30e88ea-1816-33f9-beec-14ddcbbcb160 | -3.00076 | -53.06156 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 96d432e5-284b-3829-a7dc-2d6f1d99ddaa | -2.99944 | -53.05188 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 4726b207-c2b9-3261-a64b-d23a943b0c71 | -2.99812 | -53.04215 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 335fc24e-94b0-37c3-97b7-f86c76738c40 | -2.99299 | -53.05859 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 0ef65515-a3ca-3cf8-8bbe-7e4b463a9225 | -2.99163 | -53.04885 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| f9f58162-05c0-35d4-a447-ed2b29891dfa | -2.99027 | -53.03916 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c225ea7b-5334-3697-ba99-e2ce303f5bb7 | -2.99011 | -51.05772 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 89a805a4-62f0-323e-ac17-e6c6a7fbc53f | -2.98644 | -51.03136 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cfd0b9a2-9aaa-3379-99e3-d5f31303a505 | -2.98124 | -52.8496 | 2024-10-21 01:05:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5e7ee251-3e3b-3d66-a205-e46d325576e9 | -2.97319 | -47.99391 | 2024-10-21 01:05:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| c33cddc9-da2b-3644-861c-869f4d34e126 | -2.96321 | -47.99534 | 2024-10-21 01:05:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| c38b8603-a09e-32f8-acaf-288b1dffa1c4 | -2.96278 | -50.52406 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9f960c1a-c26f-3c99-a4ad-8d005f75d2b8 | -2.96158 | -47.98399 | 2024-10-21 01:05:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4536cfc2-c566-3897-9121-e6ae6ff46adb | -2.96153 | -50.51516 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f90368f2-e329-351b-9e5e-37c0232a1f43 | -2.95316 | -52.90761 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9abc8fd5-7c80-30a2-9fc6-c05da625fd9c | -2.95113 | -51.03635 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ffda6b92-b625-3518-92e5-a0bbf43eb651 | -2.94738 | -49.56048 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 777370f9-d5a9-3055-a52a-eaea10311afb | -2.91857 | -52.45913 | 2024-10-21 01:05:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f1d81785-697c-3b05-9464-303df28eb853 | -2.91731 | -52.4499 | 2024-10-21 01:05:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9440d648-f873-3053-8246-b50f1fcb9c3d | -2.91393 | -45.22562 | 2024-10-21 01:05:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| fe014213-66f1-33b4-84c4-1d082896516c | -2.91119 | -45.20731 | 2024-10-21 01:05:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| fdb49b5c-75fe-3ffd-aea9-9b5cd3d8e17e | -2.90912 | -45.21425 | 2024-10-21 01:05:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d259374e-e463-3d3d-b083-376f28bbc388 | -2.90652 | -45.19594 | 2024-10-21 01:05:00 | TERRA_M-M | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 6635710f-e74b-39e8-84e8-0b0a9313074d | -2.90154 | -45.22744 | 2024-10-21 01:05:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 9f1dc4f7-ebe7-333b-be55-dfc04613b60e | -2.89878 | -45.20912 | 2024-10-21 01:05:00 | TERRA_M-M | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 185.2 |
| 5c8d1e13-acef-3caf-9bbe-b133ee1ba1b8 | -2.89671 | -45.21608 | 2024-10-21 01:05:00 | TERRA_M-M | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6dc64a40-8d1d-3e92-919f-82c1e03477d6 | -2.89603 | -45.19081 | 2024-10-21 01:05:00 | TERRA_M-M | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 8ab4a0e8-0f21-36ed-8436-c569e37cae6a | -2.8941 | -45.19774 | 2024-10-21 01:05:00 | TERRA_M-M | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d327430c-2cf4-3349-b6c9-3b463425c094 | -2.89088 | -49.49101 | 2024-10-21 01:05:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bdcb79c4-63f4-33a4-bf90-868578b841d4 | -2.88953 | -49.48147 | 2024-10-21 01:05:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ecaeb78e-c9d9-3bba-8cc0-c480911a1048 | -2.85963 | -45.47782 | 2024-10-21 01:05:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 0dfbae28-d9ef-3c7e-9e97-af867a939075 | -2.85812 | -51.28822 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5ae5dfa6-af0c-3bf8-8ef1-00898905bfeb | -2.85703 | -45.46035 | 2024-10-21 01:05:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 00496e85-7503-3429-9d56-e35828b6a0b7 | -2.85551 | -45.4839 | 2024-10-21 01:05:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 33.5 |
| f65e2568-c74e-3511-9667-b7157a3264fb | -2.8549 | -53.34362 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 11935a93-d6f4-393d-b605-0756327d48a7 | -2.85356 | -53.33367 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 5661abc6-b349-3eb3-bdd3-3c4ec5c7f204 | -2.85304 | -45.46639 | 2024-10-21 01:05:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 151f9fe2-072e-36aa-a50f-2f9f58175eec | -2.85221 | -53.32376 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 462d179c-154f-36eb-a38c-a89ab9449d0d | -2.8493 | -51.28947 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 53511811-cee4-3160-80ea-28f82366ef5c | -2.84814 | -53.34034 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| f0a7b2f6-9e1c-3225-b56b-7676b0c3f621 | -2.84675 | -53.33043 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 8e20de83-1bb9-366a-9e64-b5836efa184f | -2.84419 | -50.46541 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d7104e58-3b16-3362-bc94-f32013bde437 | -2.84294 | -50.45649 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b0984750-bf95-366a-add4-b2e9fdd70a42 | -2.8388 | -53.34166 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| bf14dcce-e7cd-3080-950e-91eeb84083dd | -2.83741 | -53.33173 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d1a4d29d-8e8f-35b0-bc6e-f14f37b1c8c6 | -2.83713 | -53.98877 | 2024-10-21 01:05:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 93a06d71-0686-3da6-b700-33e9dd0a6970 | -2.83563 | -53.97804 | 2024-10-21 01:05:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 650b1a39-ea62-3aca-a120-936c2f0ae0e4 | -2.83087 | -53.16653 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 87046ad8-64be-38f3-90f7-56626504237c | -2.82825 | -53.00943 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 5b981a43-7b22-3602-8db3-8dbfd13196f6 | -2.82695 | -52.99995 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| f8d2c534-6095-3483-be59-87f3f427d1c8 | -2.81905 | -53.01072 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5f34626d-5b57-38b4-84f8-8634e26ad820 | -2.81876 | -51.34491 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 0259a16b-1b92-31eb-bc29-6c0e568c099b | -2.81774 | -53.0012 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b5944d49-2fb9-339f-9434-2ec2fbc71ad8 | -2.80994 | -51.34615 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d86607e2-7f56-3812-ac0b-2b3b895b4860 | -2.80732 | -45.79355 | 2024-10-21 01:05:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1d4ae9f2-9306-378f-8c0d-b27429e63b9c | -2.80356 | -51.36497 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 2d4621c7-a38b-30fb-86b4-5bfdf8e4008c | -2.80164 | -45.78783 | 2024-10-21 01:05:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 4a7450ad-2db9-3a59-adb1-637d19ed37ed | -2.79595 | -51.375 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5a0972de-6ec4-3c9e-9802-74f94d694b30 | -2.79473 | -51.36621 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| e50f20df-7e5d-3c4f-a883-89dcd352913c | -2.79351 | -51.35743 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8f6bda7f-f3e2-3e9d-8d88-d57a0885deb9 | -2.78198 | -49.30633 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 80beb8b7-a9cb-3018-badd-39fb34ccb161 | -2.7806 | -49.2966 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| eb52d155-9a3c-3321-855e-4fdcf60d3b59 | -2.77272 | -49.30764 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 07e7758e-4a08-3252-a8ff-78a28e3a09e2 | -2.77133 | -49.29792 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e73e26da-4516-3bca-9ce5-189d386bb744 | -2.76995 | -49.28817 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 07b197bd-d6f0-322e-9149-bab1820b29ce | -2.76252 | -49.36837 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a8d803fc-ede6-312f-8b3c-3f36f97633c1 | -2.76114 | -49.35872 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f3c001a4-24d0-3b94-bcbc-58a453a05629 | -2.73798 | -53.21185 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4976d0b0-01ac-3eb1-b103-73d293ef26d5 | -2.73627 | -49.36862 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b0c6183d-2e5c-378e-93cf-4ff67070aee0 | -2.72192 | -54.77894 | 2024-10-21 01:05:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ef4e743f-9f31-3e68-9c64-caa35d73dac0 | -2.72027 | -54.76687 | 2024-10-21 01:05:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 53f78737-8c8b-3d9a-a84b-c8a98a95eb4e | -2.68983 | -52.06952 | 2024-10-21 01:05:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 58d3de19-0d0b-34a5-9adf-5ebb8cc072a0 | -2.66794 | -49.40399 | 2024-10-21 01:05:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b4e1e421-c144-3631-99cc-fdbb3e5fb96f | -2.64785 | -49.98892 | 2024-10-21 01:05:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7062816e-f019-3d6f-bdc5-29204e473ead | -2.63883 | -49.99021 | 2024-10-21 01:05:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d97e8e9a-3be6-31df-8cd1-ef26a4cad87f | -2.62792 | -48.52519 | 2024-10-21 01:05:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 790414c8-4553-3e0f-afd6-9a5a0bee6b83 | -2.56564 | -54.02265 | 2024-10-21 01:05:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e84ce81b-3cd3-34e0-84e0-16ebd5197169 | -2.56414 | -54.01194 | 2024-10-21 01:05:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |


[Clique aqui para ver as próximas entradas](README13.md)
