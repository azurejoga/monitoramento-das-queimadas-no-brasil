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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0efff27-7380-3dc1-bdda-27ba627b7e3e | -2.86999 | -51.4732 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f9e0fd8-968a-354d-ad06-7b53c3635d0c | -1.61174 | -54.52666 | 2025-11-15 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecd42792-face-329d-9b68-f3e11337e93e | -3.47625 | -50.03614 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 457ed921-ee72-3bbc-bd7f-ef7e02fe8df9 | -4.35326 | -46.49405 | 2025-11-15 05:16:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3deb1c38-7e6b-3e98-afe3-2bcf33973657 | -7.9519 | -54.84305 | 2025-11-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74a619a9-0ea4-30c8-9883-1222b9dae779 | -2.88251 | -54.23768 | 2025-11-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 400e8a28-f58e-36cd-8b30-9e65df42b3d1 | -1.83108 | -53.79179 | 2025-11-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b0c7f21-834e-37f0-b331-2d3895e14e4c | -7.87796 | -48.40179 | 2025-11-15 05:16:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 915c6716-134e-39b0-8387-2b3dcb27bfd4 | -4.05774 | -46.42155 | 2025-11-15 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49fb16d8-aa3a-3782-81b1-5183b91cba77 | -3.86275 | -49.13479 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90b81d2c-8c99-3c5c-be94-17cb3cb16125 | -2.86931 | -51.47765 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed1885d2-a859-3092-8037-a77ad652b1ad | -2.85774 | -51.28227 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee39e43f-c39a-3189-939d-82b7d74ec1cd | -4.78942 | -48.67276 | 2025-11-15 05:16:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 202f9c41-af42-36a3-b9dc-1b82a8787db3 | -6.32763 | -47.26192 | 2025-11-15 05:16:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6056a7a2-4ec9-3334-ba70-534b1432ea60 | -3.245 | -50.37448 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b66712c3-ac85-34f5-9665-f71c319c935b | -4.27559 | -46.84192 | 2025-11-15 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ad87fd1-0bc9-3965-922d-a0781ec40b44 | -2.87243 | -51.47556 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac9345d4-b5d5-3626-bbcf-49fe20a05e5d | -2.92113 | -52.51492 | 2025-11-15 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b0d6875-927e-3ecd-a4a3-a2334ae68a29 | -2.68202 | -49.86244 | 2025-11-15 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e8a037a-ea62-3a44-8291-373cec6ef151 | -4.87004 | -47.38295 | 2025-11-15 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbfa889a-6d37-32f9-8767-d620b0078066 | -3.19719 | -51.375 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7376ea7-8768-3d68-98ba-7155cbd5d677 | -4.38781 | -49.65304 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61a32330-f4b1-3ba6-a9e2-5d41b3ebc897 | -3.45426 | -53.50802 | 2025-11-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62f242ef-28b6-3e7b-ad0f-e9ac6c417d8f | -3.6231 | -55.43624 | 2025-11-15 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fd768fb-6805-359e-b12b-cdf0b7f7fced | -4.22555 | -51.20251 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7de35cca-4f34-38d5-8576-79c96d9eaf54 | -7.06019 | -48.32179 | 2025-11-15 05:16:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c57bf6b9-2650-3a2b-869e-2bda5bc2ce8a | -3.53323 | -50.87355 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b079d8f3-245f-320f-a0a8-4fe3aac60fc7 | -6.82056 | -48.82685 | 2025-11-15 05:16:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f2515c6-be64-38e0-9c7f-17eb169ee8b4 | -9.12187 | -50.30633 | 2025-11-15 05:16:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49491431-9c88-3fa0-9542-8bfca72af7cb | -4.01365 | -48.80492 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5a7e4da-e6eb-3c6b-9a91-9d1c6a02983f | -8.32259 | -45.40621 | 2025-11-15 05:16:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c35e3aa-3796-3e90-be8f-4659dd450ee9 | -9.81366 | -48.84402 | 2025-11-15 05:16:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53a7fee8-9aa8-3efc-8c73-573988efb655 | -3.23646 | -51.51516 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf1be97a-e477-3da1-88e1-70aaf05704d8 | -3.47279 | -45.6504 | 2025-11-15 05:16:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11fe59bc-bf8b-3813-9287-f12bd3827fca | -3.07792 | -53.28888 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 446a282a-f824-3596-9921-67a2edba6be2 | -2.68164 | -49.86188 | 2025-11-15 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c90d020c-e230-30f9-85a0-574fdb6ef6a8 | -3.77742 | -54.47515 | 2025-11-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba480ddb-33a2-3ad9-af20-f20eb0d3bbc8 | -9.1295 | -47.12481 | 2025-11-15 05:16:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55573af2-c4e8-310a-a190-cc372c69a922 | -3.52935 | -56.31752 | 2025-11-15 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b39b9c95-cad3-32c3-abaa-54e7a2ccee7e | -3.52852 | -50.87282 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0038d474-fa4b-30fe-b9b9-48a835dab703 | -8.32341 | -45.39949 | 2025-11-15 05:16:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85cd88bc-80e3-31ae-bbc7-978688d9a20a | -1.83486 | -53.79237 | 2025-11-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bc38572-5d9c-3a49-97d9-c50aad086f3d | -1.62184 | -54.71241 | 2025-11-15 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0eeb5271-b296-3df6-97c3-aae32d324438 | -6.15472 | -48.04214 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e5d4b0eb-8fff-3cb6-a94f-b65cec3ebf7c | -4.64506 | -47.95089 | 2025-11-15 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71eee5bf-9b30-3f2d-ab48-0a34c3755857 | -2.68161 | -49.86527 | 2025-11-15 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f77bbe9-f167-39d1-8482-a766fd870caf | -3.01183 | -49.43546 | 2025-11-15 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2223aba5-4f63-3ca1-9063-47f2e6dbf7b9 | -1.83415 | -53.79697 | 2025-11-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a48b67cc-9237-31ce-8fff-aecc782f4d62 | -3.16927 | -45.21502 | 2025-11-15 05:16:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e7206d82-a0f9-386a-95eb-ed8394936d8d | -6.1503 | -48.04682 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6702447e-333f-3945-86ea-5ec600f6803c | -7.87624 | -48.41483 | 2025-11-15 05:16:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b1cb2187-791f-3135-89fc-f4a99ddf0e30 | -3.2003 | -51.37405 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1715f50-f327-325b-b373-30950888ac52 | -3.14772 | -45.3912 | 2025-11-15 05:16:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 93fd8557-99ca-308e-81e6-015428b76b92 | -1.99988 | -57.07072 | 2025-11-15 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebd8dd87-bdf7-3340-96a2-987d626b8618 | -2.98984 | -52.82343 | 2025-11-15 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d668e493-492f-34e6-b4b0-ac20cd5cce78 | -6.16002 | -48.04773 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 17f61838-48f8-33d5-a11b-b40972bfcaee | -4.18278 | -50.42186 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fbd71a2-7c3d-3940-9498-f93fcc80ef93 | -9.70373 | -48.87127 | 2025-11-15 05:16:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e86c66ae-db14-3937-a134-1245604d0806 | -9.09465 | -47.78642 | 2025-11-15 05:16:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f558b271-3473-3afb-8174-8f364072474c | -4.25265 | -48.20398 | 2025-11-15 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| faf64cf7-106f-37ca-a824-568f7233906a | -3.15154 | -50.26604 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b46cc85-718f-3ffd-add7-2f04702769ca | -2.86553 | -51.4725 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83e60020-5923-32b7-9ba9-adaf244fb97e | -2.97284 | -51.53668 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c2b4d94-dd9c-3e75-9c9d-269f0662f101 | -3.43617 | -56.31065 | 2025-11-15 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72c74488-6233-3846-8b39-8b9a7c8ceda8 | -7.42637 | -45.23333 | 2025-11-15 05:16:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6fe7338-cc98-3873-a307-15d50b1ad897 | -3.5278 | -50.87776 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e842c5e-ee18-3c19-9730-bf3d01e8b2ea | -4.34961 | -46.49051 | 2025-11-15 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 945ce9d3-f2d8-333d-bb74-6e91f09d8712 | -7.88507 | -48.39373 | 2025-11-15 05:16:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4b8bbe7f-4a83-364a-af04-a94cd5647042 | -9.35394 | -50.74238 | 2025-11-15 05:16:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09d49a56-34ce-3e6c-bb24-0b48551e868b | -7.87681 | -48.41051 | 2025-11-15 05:16:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b197d651-1155-332a-9d07-b23e1ca2365f | -6.60414 | -50.06812 | 2025-11-15 05:16:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc9003b0-be63-35b9-9b71-19dfd261f9db | -2.42309 | -55.34755 | 2025-11-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85ebc87c-086c-359d-bc65-61af2c8feff6 | -3.53442 | -52.99793 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f3aab58-cf08-3a66-992d-5cf1eb0db7f8 | -2.69368 | -49.8525 | 2025-11-15 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d638cd54-6257-3bbf-b051-e3badddc052e | -7.21999 | -47.97571 | 2025-11-15 05:16:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7d54926-fb5c-3a43-b2e5-b6a49ca4b1ae | -5.58644 | -47.10015 | 2025-11-15 05:16:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4ad578d6-b709-3e60-ad6e-056bb332fe05 | -9.71819 | -48.8995 | 2025-11-15 05:16:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e50e7f9b-3018-3828-bc98-ed760630f434 | -4.68344 | -45.851 | 2025-11-15 05:16:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 706abb82-6e34-3c88-b7e7-774dadd35e07 | -7.88334 | -48.40683 | 2025-11-15 05:16:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 18cd7c0b-76c7-3a0a-9a86-4e8d6739439f | -2.97114 | -51.53925 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cbdf95a-e2d2-3b1e-bd6b-9849bd2696c1 | -1.83343 | -53.80156 | 2025-11-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2003457e-3442-3f81-83e2-92a6de5e3985 | -3.19903 | -53.01315 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5f98fbc-9667-3d99-8f8c-2718c3b1e5a4 | -5.12783 | -55.97578 | 2025-11-15 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a54dd53-e275-32a8-bfa0-8097b6f6ac04 | -4.2015 | -48.56167 | 2025-11-15 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66e660a3-371e-3154-a1f1-d5c9b1db14a0 | -2.88731 | -54.85474 | 2025-11-15 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 723b1858-2913-3bba-b071-e8c156ac76a9 | -3.01698 | -49.43629 | 2025-11-15 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a1264c8-086b-3114-965b-30fef131a871 | -9.49397 | -47.27885 | 2025-11-15 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e38e17af-dab7-3b6f-948e-a3d9e89e3190 | -2.88352 | -54.24086 | 2025-11-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58ea540e-198f-374a-8c5d-8bf5dca5f6cb | -6.1634 | -48.03968 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 351e7be3-a929-3828-ae07-8e91449b0b02 | -3.37598 | -50.13178 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63c87638-f782-3eed-9e51-29e93bfc6217 | -2.95238 | -45.15302 | 2025-11-15 05:16:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 3e708678-1285-359d-9911-72e62373086b | -3.67481 | -51.68771 | 2025-11-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d4f3fc3-0907-351b-8281-47c1c770b6f6 | -8.32898 | -45.41342 | 2025-11-15 05:16:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cec5b9ec-547b-3e86-aa6c-2e85a7c5b4d1 | -3.28065 | -51.54313 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39d084fb-2af1-3d7e-8639-1c46e70c129c | -6.17255 | -48.04439 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a9b1e50-5d55-333c-978a-d91a500943a7 | -1.90379 | -56.48482 | 2025-11-15 05:16:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a07d8617-996c-3676-ba08-0b1b62cdffd6 | -9.92986 | -47.83751 | 2025-11-15 05:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efb80195-a115-3007-a535-52a35d37cec9 | -4.46842 | -50.54107 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5be77895-7e6c-3560-86ef-9550e4cad673 | -7.87739 | -48.40614 | 2025-11-15 05:16:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 51056ae0-359d-3c41-825d-1cddeadeb3fe | -9.71875 | -48.89499 | 2025-11-15 05:16:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README53.md)
