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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| debb959b-5ecb-380a-a718-f2581a26a657 | -2.85185 | -53.32352 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82859a7a-5701-3b61-91ff-95c439c4b1f4 | -2.85042 | -53.33216 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3e9d0d9e-b4f2-3799-962e-402ae9e2d3a7 | -2.84971 | -53.3365 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5dfbf62d-f505-3416-9710-456c8f6c0920 | -2.84899 | -53.34087 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b175e848-59a2-33bc-a67a-956cf531451e | -4.13493 | -53.49846 | 2024-10-20 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f1003d7-7e6d-36a7-9d93-86269ab6b74e | -4.13422 | -53.50273 | 2024-10-20 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f830144c-c0b9-38d5-9934-cfadf36d1b9c | -4.12555 | -53.66496 | 2024-10-20 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ceebfc2-487f-318e-ba91-eb6f8fc51774 | -4.06627 | -53.77299 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ddfc84a-a537-3eea-8ccb-14e4ecfa5c36 | -4.06179 | -53.77221 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f2f06e6-232b-3b6f-a3c9-8470fd9f704e | -4.06102 | -53.77679 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecae44c8-cb88-3744-805c-4e5699c68c42 | -3.76874 | -53.40464 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7392a4eb-618f-3f61-b6f9-158cddc0e190 | -3.76806 | -53.40888 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de84ad09-1371-3c6d-be99-5b9efec6b921 | -3.76737 | -53.41311 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cb73094-fe4c-32a2-b6fe-38c927531a38 | -3.57215 | -53.75515 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 46f39970-b86b-32b0-9478-a8c9131682af | -3.57123 | -53.53796 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5dc44b46-8771-37a9-8f1c-d7681b64e44e | -3.57051 | -53.54232 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e44e1dcd-00f3-3726-a066-7aa1681b2758 | -3.56906 | -53.74574 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 70b3f1e4-4af2-33a9-8622-684adac0248f | -3.56836 | -53.75 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 477b06cb-0780-3ebd-8abf-0a27b06e56d1 | -3.56822 | -53.52864 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| df527416-28c3-39a8-bb63-b9d280193631 | -3.56765 | -53.75435 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f8c021b9-4575-3c5d-965e-a4b673a6a24b | -3.56677 | -53.53732 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a45c8ab-6da8-33d1-b1ad-23bb8b897359 | -3.56458 | -53.74479 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65d5fe99-6b53-374a-98fe-54ef616a47c4 | -3.56387 | -53.74913 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d9f536f-f6f1-3682-9738-c6c61f5191ff | -3.90351 | -52.38697 | 2024-10-20 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2123fdc8-89c3-3383-9d14-16b26b171a7e | -3.71998 | -52.29095 | 2024-10-20 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc3846c2-d39f-35fb-8216-5a869424e749 | -3.59321 | -54.66454 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2be83e6c-242d-3c92-aab7-535cede52c99 | -3.5906 | -54.68003 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 222216e1-e369-3979-8087-033c8052f918 | -3.58973 | -54.68519 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0e45c2e-b3ef-3545-a2ef-b5d51fb47c0a | -3.58951 | -54.66205 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a442bdf-c790-3826-9908-df7258dc8920 | -3.58701 | -54.6776 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 087ffbab-d764-386e-9458-66842e5ca495 | -3.58618 | -54.68277 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a239a633-9d12-3d64-b666-868d5f1f5875 | -3.5858 | -54.67918 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d4c4bec4-2f0d-34c4-8afa-7c21e0215d6d | -3.55182 | -53.9939 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12a864e8-be58-3eb0-bd48-01a5c0814dd3 | -3.49666 | -54.45234 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35fb8b49-c66d-3313-b03f-5d2495bd6dbd | -3.49591 | -54.45621 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e006f17-8698-3e06-9bf7-ca517af81f06 | -3.49581 | -54.45733 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2050b04-4029-3254-b7b4-2f869ad96b89 | -3.49116 | -54.45546 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ccdeacc-b675-309b-9ba2-3dd2e8f4efb4 | -3.49106 | -54.45659 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0ee2712-c72b-3d20-afb8-8e67eb717dec | -3.44098 | -54.14693 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e8cf2fd-edc0-3cce-a9b8-53fe499b4540 | -3.44015 | -54.15179 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ab84bad-795b-3929-97fe-79923facc75c | -3.43794 | -54.14804 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d3e39be-a2a7-3a8d-bb47-555e60b72e0b | -3.43716 | -54.15293 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6452ec5a-1dc9-3b63-a40c-1c30c7a2abd2 | -3.43332 | -54.14714 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bbdeca8-3e84-3f99-9b96-756f5f6fbf45 | -3.42869 | -54.14624 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 142e5a48-0763-396a-b3e3-08709901cdbc | -3.35438 | -54.74567 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48c290f7-430a-3d9e-8cfa-19627a359717 | -3.34956 | -54.7447 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdc1c0d8-3660-3078-aed9-cfe30dc7399a | -3.32958 | -54.18375 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa8de32d-2802-30a1-9f66-795ac3e3ad39 | -3.2768 | -54.15476 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6400c624-40df-3938-9819-632a40d8a22a | -3.27501 | -53.70786 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62259f1c-8b9b-3120-8c4f-a2f4913ba52a | -3.27295 | -54.14905 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e7519fe-fa1a-3e7f-ad2f-8c790377a15c | -3.27211 | -54.15416 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25cc177a-ecd2-3356-bc92-92aa1539a569 | -3.27049 | -53.70708 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cadb520-8b0e-3a18-b765-7288b18619cb | -3.26826 | -54.14845 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d04c745-4944-3858-a425-03acb9489b79 | -3.26743 | -54.15348 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 745804a5-d142-33f1-8899-17b35baeb865 | -2.75779 | -54.03738 | 2024-10-20 04:32:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 655dd276-1042-3271-b12d-649ba2c1139f | -2.71743 | -53.99215 | 2024-10-20 04:32:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcd18faf-0ba3-33d4-942b-c1f69df47281 | -2.71353 | -53.98693 | 2024-10-20 04:32:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b8f7bac-242e-3448-9cfa-ef10f95e784d | -2.71272 | -53.99171 | 2024-10-20 04:32:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63f6ed2c-1dde-3691-b2e6-22781930bfda | -3.15443 | -54.36068 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f0dae8f-0452-39d5-b757-e6066cd706ad | -3.15051 | -54.3549 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0df91a9-b389-3986-ac17-0dcb6a36ea32 | -3.1497 | -54.35982 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| db9c2199-9f33-3b5a-af3b-7428e2dd09c9 | -3.14888 | -54.36481 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0ebd61c9-eb8c-36c4-bc82-88bc88ec84a1 | -3.14659 | -54.3491 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31034bfa-8f47-3296-a47b-159196074651 | -3.14578 | -54.35403 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5576beb4-18d1-3ee5-8c0d-339167401111 | -3.14497 | -54.35895 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 44b58b25-d063-3db6-b11b-887a2c9c4857 | -3.14416 | -54.36391 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b7b023f1-720b-31ff-a513-f2c1341b1b9e | -3.14106 | -54.35312 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fb4f82c-2baa-3be4-90c9-e553d3bd842e | -3.14024 | -54.35809 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52656f5e-df32-3ec7-adfc-3aa2571edc41 | -3.13942 | -54.36308 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41c3f745-0319-3884-83dc-34f48b411da2 | -3.13634 | -54.35222 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b217a59-8210-3b6c-bc9e-122e9a41401a | -3.13552 | -54.35722 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e76e84f-cc5a-3862-ad3f-57c5794b00ca | -3.13469 | -54.36224 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0028fbf0-01c1-32a0-b09e-873f75f8ad6b | -3.13162 | -54.35134 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 62f948aa-c50d-3c6f-a952-865860cc054c | -3.13079 | -54.35637 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 25a44f04-4b7b-3d3c-ad80-1d9144dfe2c1 | -3.0886 | -54.43377 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00ce7d84-f308-3ca2-8c93-34c3a10641a4 | -3.08849 | -54.43773 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c8121a2-774e-3447-ad8d-8d4b65779105 | -3.08456 | -54.43169 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e625c1b4-7138-3787-a49a-16ed9e0f7694 | -3.08383 | -54.43301 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1c445c2-3a6e-35bc-939f-87b143ebf99d | -3.08372 | -54.43695 | 2024-10-20 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a082a0e9-1757-3c84-9585-1a75ede8fabc | -3.02266 | -54.04342 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30d9cb8b-c6f9-393e-8e45-788540491aa3 | -3.02184 | -54.04824 | 2024-10-20 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7fe822c-9084-3ca4-a1db-d3f30228ed4c | -3.02019 | -54.04079 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f239e31c-48d8-3fea-a145-799682233379 | -3.01941 | -54.04562 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdeadd31-c789-3059-955c-14074a2d4359 | -2.9529 | -54.15981 | 2024-10-20 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1b0706a-535a-36aa-8057-9c9869cfe565 | -2.94848 | -53.70294 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5ba9e89-3690-3cb0-b6e5-9f21695cfe08 | -2.94822 | -54.15898 | 2024-10-20 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e05d287-d6ca-3c9b-be98-8c997fc50df5 | -2.94774 | -53.70752 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1719e301-11fa-3161-8dda-b9d17c86512b | -4.07926 | -54.11649 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8b541d9-d273-3fed-84a9-5ac07cc289bc | -4.07467 | -54.11573 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b9e4cc2-1bde-3150-8790-d0827ef408c5 | -4.05427 | -54.51412 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58880168-9937-30b1-8477-4d26a721141c | -4.05289 | -53.88022 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4602f192-601a-3a15-b4d6-e4a498bb6a39 | -3.83706 | -53.99384 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8f9efaa-824b-3071-9607-53d978f55ee5 | -3.69795 | -54.06989 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 290c29de-26db-3992-890f-b6c10b035771 | -3.68871 | -54.21062 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6de5d7d6-113e-331a-b550-81cf9db5129b | -3.68405 | -54.20988 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4117c46a-641c-3792-a913-f82f29a74cf6 | -3.68325 | -54.21468 | 2024-10-20 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee912ec5-7676-34a6-8782-8b010550355a | -3.6269 | -54.66976 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 97ef42cd-9d44-3f5a-bb54-8b4d7a00462d | -3.62604 | -54.67499 | 2024-10-20 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b1652f1b-ebe1-3443-ad25-86c5b3968074 | -3.48922 | -55.43439 | 2024-10-20 04:32:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b61fd017-ba37-3fa6-bae9-1a24a90b733e | -3.48415 | -55.4335 | 2024-10-20 04:32:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README40.md)
