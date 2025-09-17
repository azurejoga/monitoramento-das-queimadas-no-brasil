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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6904ba75-8d99-315d-b497-6cd48316fb0b | -8.6885 | -46.3823 | 2025-09-17 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a71c03e7-9171-3777-b292-5c1c1e7ffb37 | -8.9533 | -46.3099 | 2025-09-17 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1b5c1ef4-f341-38ed-963a-8b9698f66f11 | -12.7102 | -47.9872 | 2025-09-17 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 7c2c865c-084d-3fd4-beb4-a51a8cd324d3 | -12.7106 | -47.9649 | 2025-09-17 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 74302377-554c-375d-94bb-114c384bb78b | -8.9449 | -45.521 | 2025-09-17 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 75fac6dd-84ea-3d18-be45-30298c54946b | -9.1239 | -44.862 | 2025-09-17 12:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 27ce4c26-3434-37ef-83cf-085e3b713f00 | -8.9725 | -46.2854 | 2025-09-17 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| eb546455-b4c3-34aa-97e6-b696848ce144 | -10.6921 | -46.513 | 2025-09-17 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 0a31541d-04fb-3a50-91e5-78349503a36c | -9.1236 | -44.8849 | 2025-09-17 12:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 153.9 |
| fe6747d4-e183-37f5-97dc-d0e486a24e37 | -12.0047 | -46.6989 | 2025-09-17 12:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 89a21e37-270a-3efa-a3a8-b638a10452bb | -8.6887 | -46.3599 | 2025-09-17 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| ef7713ff-087f-311f-8b66-50404628b226 | -8.9725 | -46.2854 | 2025-09-17 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 434600b4-e3fc-332c-ae9e-3d8ee32bc036 | -8.9533 | -46.3099 | 2025-09-17 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 02250120-9cb4-3e5e-a859-991d12e6bfa1 | -8.6885 | -46.3823 | 2025-09-17 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 269e3262-63cf-3138-a985-e59b8fc75e1d | -8.9536 | -46.2874 | 2025-09-17 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 2b184a4b-7c45-3555-9d12-e8ec53821623 | -8.6313 | -46.4329 | 2025-09-17 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 45a8d6ad-cda9-3cae-bb32-bedfa4d43325 | -6.6129 | -45.584 | 2025-09-17 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 89ef394c-5ddb-3ca4-b7be-955103d78014 | -7.6574 | -44.4667 | 2025-09-17 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 154.4 |
| fb0c6278-ebc5-3843-8e32-31166d1b588d | -12.6825 | -45.2977 | 2025-09-17 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| acee7ac4-1ac1-3bb4-9c3e-b37243058674 | -8.9917 | -46.2609 | 2025-09-17 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 189.1 |
| ac843cb4-9971-38d9-9cf3-075633510182 | -15.8417 | -59.4799 | 2025-09-17 12:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 7c10855e-a596-3e12-a113-8e7be768289c | -13.9653 | -44.921 | 2025-09-17 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| be17815f-2aad-3261-b12d-72c1e5c31372 | -8.631 | -46.4553 | 2025-09-17 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a19fa8aa-4d29-3627-9b51-e2c1085b3353 | -8.6699 | -46.3618 | 2025-09-17 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 75eaf733-a5cb-31a6-b786-a8659579e84d | -7.6763 | -44.4649 | 2025-09-17 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 869a3e49-7ca6-3a93-bdac-24a25d2a371f | -8.6882 | -46.4047 | 2025-09-17 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 88032d49-17bf-312d-a07f-55e33dc279e3 | -7.6572 | -44.4897 | 2025-09-17 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 87c90616-fa0a-3bc1-aab2-01e65ad4047d | -12.729 | -48.0068 | 2025-09-17 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| dd50ad09-f0a9-3641-bb15-2f25cd5f0a84 | -9.0478 | -44.8936 | 2025-09-17 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 13b7768c-f4c3-38fe-82eb-c8c1985f9d6e | -8.9728 | -46.263 | 2025-09-17 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 15309f74-8b4f-3981-91cd-b917f3ff597f | -8.8958 | -47.8683 | 2025-09-17 12:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 529d0c9c-04e8-3b3a-b4f6-6d14c9fcf9d5 | -12.7106 | -47.9649 | 2025-09-17 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 62274b64-bdc0-32ef-bd64-4880788c2ec9 | -12.0047 | -46.6989 | 2025-09-17 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 0c2376eb-abd7-3800-81b7-02d28e88f0d8 | -9.1239 | -44.862 | 2025-09-17 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 015e48d8-8399-35ce-9d6f-06211f98492a | -9.1236 | -44.8849 | 2025-09-17 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 1f192596-a3b5-3655-89a2-dc46d1abbb6c | -8.6313 | -46.4329 | 2025-09-17 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f859afa7-f135-3040-8db0-bade2f7184e5 | -9.0478 | -44.8936 | 2025-09-17 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 16d7569b-5efe-3cc9-8a96-2a9d82441e84 | -12.6825 | -45.2977 | 2025-09-17 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 2f6a7000-6caa-30b4-92e8-e387ed5b60a8 | -9.1187 | -48.1091 | 2025-09-17 12:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| a5b9a614-bac2-30f0-82d2-9cc77ecf8fcc | -8.9725 | -46.2854 | 2025-09-17 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 204.4 |
| dd826e37-22fc-3e52-a067-db3626e946f6 | -11.1919 | -47.3896 | 2025-09-17 12:20:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 1cb1438c-8b29-3eee-a87e-271359d2d3ea | -7.5807 | -44.589 | 2025-09-17 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b92d636d-1542-39fc-9de1-8afa91b53262 | -8.9731 | -46.2405 | 2025-09-17 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 1a7d867f-0f86-3fcb-9848-9c3e1fb2dd60 | -5.4897 | -39.426 | 2025-09-17 12:20:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 5ce9a33f-0a26-3ade-8755-7362e864c644 | -12.0047 | -46.6989 | 2025-09-17 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 03251a0b-3f00-324b-82b5-02ce6b771c4c | -8.9533 | -46.3099 | 2025-09-17 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 9d032f98-a97a-3c85-b255-e2efc33cfc40 | -8.5609 | -47.5712 | 2025-09-17 12:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ead3257b-4ee9-3cd3-92be-5b9d8fed00c2 | -8.6882 | -46.4047 | 2025-09-17 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 14d696b2-2290-32b2-a348-ccc7b959e290 | -12.0051 | -46.6763 | 2025-09-17 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 0da0dbf6-23ef-35a2-9dfb-354ac7c67318 | -9.1376 | -48.1072 | 2025-09-17 12:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 8094a1ff-9645-35f5-ae52-d98e511f42b3 | -8.6885 | -46.3823 | 2025-09-17 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 7bfec666-f4c7-3d2e-a369-a4eeb4376091 | -8.9449 | -45.521 | 2025-09-17 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9e598d08-2ec6-3406-ad33-f679e2e3d366 | -8.9728 | -46.263 | 2025-09-17 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 0a25205d-c829-348c-ad80-82b591c3d78c | -8.631 | -46.4553 | 2025-09-17 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 94524437-a1a2-30c6-9ca9-8779812806e1 | -8.9536 | -46.2874 | 2025-09-17 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 827d6bfb-85e3-3f10-87d4-e593358bc1c6 | -6.8734 | -43.9636 | 2025-09-17 12:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| ed318cf6-5a1d-38dc-af3c-97f572f1fa96 | -8.4467 | -47.692 | 2025-09-17 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 223.6 |
| ba5b2311-4e3f-3274-9f22-f836e222ea7e | -12.7106 | -47.9649 | 2025-09-17 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ae6bd162-8f3c-3c4a-9f76-17dc0e789941 | -6.6129 | -45.584 | 2025-09-17 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 60494d0c-25b7-37ec-aaee-2f4f21f674fe | -8.992 | -46.2385 | 2025-09-17 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 943a1efb-6fc4-3c31-8e91-ce200d17f80f | -12.7294 | -47.9845 | 2025-09-17 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 0094ed10-6f78-31fe-be11-2607ee4a6df7 | -7.581 | -44.566 | 2025-09-17 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 98497142-5700-39ed-b7a5-81717308cae6 | -8.4279 | -47.6937 | 2025-09-17 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 8f24cb4d-1bf9-3a75-82d4-977346d1d4f1 | -8.8958 | -47.8683 | 2025-09-17 12:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c398260c-70b0-30f9-88f1-7378416d1b3f | -8.9917 | -46.2609 | 2025-09-17 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 505.0 |
| 5b02417a-89ce-3bd4-aa48-6e3109861c32 | -8.6887 | -46.3599 | 2025-09-17 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| cf30cda0-6d3c-3478-bff4-754c0d96d69d | -15.8417 | -59.4799 | 2025-09-17 12:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 44931b36-9dca-3e6c-ad99-d7b319f4eca5 | -12.729 | -48.0068 | 2025-09-17 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 642b6c41-2340-3fcb-80fb-c82497dd7b0b | -9.1236 | -44.8849 | 2025-09-17 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 874657a6-a553-3d2c-857c-b2309394ca77 | -9.1239 | -44.862 | 2025-09-17 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| ffadd28d-0903-331f-ac2a-82e65ad7b0c0 | -12.4259 | -47.8046 | 2025-09-17 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| aba3d150-0351-3597-827e-f6c16861c064 | -13.9653 | -44.921 | 2025-09-17 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 31117600-28aa-3587-9c7a-a8e33cfe2079 | -6.6129 | -45.584 | 2025-09-17 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 8411cc21-f07d-3fe0-b627-1d6c39762cf8 | -9.1187 | -48.1091 | 2025-09-17 12:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3c1c77f4-ad2a-33d0-9532-dd990c941311 | -8.9533 | -46.3099 | 2025-09-17 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 3b72d5a2-4a3c-3392-81a9-21872954afc4 | -8.5609 | -47.5712 | 2025-09-17 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4f9f3675-d260-3141-9ba5-6b57d3c8a183 | -11.1919 | -47.3896 | 2025-09-17 12:30:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 464c8f68-1977-34df-bf33-49bf397592d8 | -12.6825 | -45.2977 | 2025-09-17 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 214d564e-778a-3721-a8c5-ef6bc9e796f4 | -12.0047 | -46.6989 | 2025-09-17 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 4455317f-c355-3598-864b-d5fa2cce78e0 | -8.4467 | -47.692 | 2025-09-17 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 214c75de-d2ec-338e-b8fa-8e9079a72af8 | -15.8417 | -59.4799 | 2025-09-17 12:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 4f8fd5bc-766c-33d5-90dd-5724973e9a9c | -7.5807 | -44.589 | 2025-09-17 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 067608ba-f19a-3cd5-8e57-17bf51fd63c8 | -8.9917 | -46.2609 | 2025-09-17 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 231.4 |
| f0dd0767-0219-348a-8e95-809c97c20afd | -12.7294 | -47.9845 | 2025-09-17 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| f5016dce-ea0d-3c22-b96d-8f64f61cbbe8 | -7.5996 | -44.5872 | 2025-09-17 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c9e06c73-99a8-36d6-8d0e-b472253f8324 | -8.4137 | -45.7583 | 2025-09-17 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 4a4ad8f5-2a02-3341-a906-149efa5fce44 | -12.7106 | -47.9649 | 2025-09-17 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f275711e-46f9-336d-acf3-418acaf6aa73 | -8.9449 | -45.521 | 2025-09-17 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 5805544c-3a1e-3fcb-bc3c-0b7c0e63d0cf | -6.6127 | -45.6066 | 2025-09-17 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| feb82cc9-25ae-3392-bd63-9d9219aaac1d | -8.6882 | -46.4047 | 2025-09-17 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f42ba4a2-3036-3f4c-9bf9-3371cc08a02a | -8.9728 | -46.263 | 2025-09-17 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 5e2f2de3-6661-36b4-b5bc-5c85838fdcdf | -8.9167 | -46.224 | 2025-09-17 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| a78d566a-1050-3e9e-978d-fc53853015ee | -9.1239 | -44.862 | 2025-09-17 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 3a7e4cda-5597-3c88-be95-cdfcf5859638 | -7.581 | -44.566 | 2025-09-17 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| b7aa81aa-3c76-383f-9b85-4934c9d3f136 | -7.6574 | -44.4667 | 2025-09-17 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 001d32b2-845c-324b-b062-92cfeef53eb3 | -8.9725 | -46.2854 | 2025-09-17 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 160.9 |
| eff4d1e6-7f69-3c84-936a-6b332141064c | -14.7732 | -45.3354 | 2025-09-17 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 68d3374e-ba3e-3b70-9cee-5479325cefa5 | -9.1236 | -44.8849 | 2025-09-17 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 64eaf250-12ac-3043-b370-652165abb605 | -12.729 | -48.0068 | 2025-09-17 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| f9472a89-7005-3823-be74-d7148b02e162 | -8.9445 | -45.5438 | 2025-09-17 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |


[Clique aqui para ver as próximas entradas](README58.md)
