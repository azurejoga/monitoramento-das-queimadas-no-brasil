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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a34bcb12-ec78-397f-8e23-43ddd53c83a8 | -6.00954 | -53.4987 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30faba8d-9501-3177-8d33-4c22d5c72d29 | -4.86095 | -42.83294 | 2026-10-08 05:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71478f3a-e17b-3665-840a-ab53551ae1f4 | -3.26912 | -54.0338 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef2f7685-84b9-38bc-a005-f23985ab5dbe | -4.00104 | -51.0174 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b318fab-e054-36f4-96f3-2498b64fc593 | -5.84027 | -50.14316 | 2026-10-08 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5752a9d-a597-3d35-8fc1-6dc983e94f28 | -3.59329 | -54.56778 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc8ff046-5070-3254-bb9b-aeb8ee0c75c4 | -3.09493 | -58.02546 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7114db92-5270-3927-a46f-9736cceff1ba | -2.15695 | -51.98201 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c8641ef-dc92-38ee-b27e-7f228b4041ac | -3.48173 | -55.43613 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d6b930e-550b-348b-946f-329aff45d4f4 | -3.66275 | -54.28221 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 852741e1-f7ec-3507-825f-2b14b13cb980 | -3.47629 | -54.62317 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 573d2c22-fafe-354a-a5af-4920e07564c1 | -6.51481 | -55.384 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2b57fd8-8742-3105-b785-4aa6167fbd04 | -5.04718 | -49.76214 | 2026-10-08 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba9b9c2f-33ed-3deb-a483-8d9a52fd818d | -1.50455 | -54.82426 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77b8f053-2f41-308b-8c52-74ff5694dd5d | -3.1803 | -50.56724 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c7523fd-ab35-31c2-83e0-6e01f28f1e0d | -3.79229 | -50.87109 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0c72272-065d-3eaf-ba9d-cee87f535258 | -2.57186 | -56.16035 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d1a31ea-d316-3cf5-a7ac-f31a91a635ce | -9.06265 | -65.48612 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e7bbb63-7be9-3648-8712-7f141897b1c9 | -3.47512 | -54.63067 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fdba247-e23c-3939-a5bb-aa688832c636 | -4.36468 | -55.05717 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b9ae600-2bbc-3408-8bd4-062769808102 | -10.88301 | -49.14377 | 2026-10-08 05:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe6cdedd-4136-38ab-a5e0-062a3e795beb | -2.46237 | -56.06187 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d639aac-6c2a-35ff-afca-25111c641179 | -6.94348 | -45.28809 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 67dc754f-a707-30d7-ac82-37e5162251f2 | -2.98327 | -54.1071 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88453be1-afe7-38d3-8517-3d730e781ef6 | -5.85081 | -53.55041 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12bd6c5d-1a4d-3a59-bff1-3ed970329050 | -2.98775 | -54.05624 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f608aac5-4209-3715-b0f5-355ef507b099 | -3.44939 | -59.82505 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2483219f-25e8-3edf-8000-76f93906cf2e | -2.48187 | -56.111 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06bc5cf2-ee54-3873-b55d-21b9a492373a | -2.49072 | -56.09821 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41e3eafa-e453-3e6f-96e2-049e4affb897 | -3.91284 | -55.89332 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ac1e3b4f-2faa-345c-ac20-58974328d72a | -3.00731 | -54.1186 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 982a48cd-f128-3a4b-98fe-0ec7ce954071 | -2.88317 | -54.17429 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6c418d1-b88b-38bc-acc0-e12ea02cab6d | -4.43405 | -55.65984 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47583a1d-6329-3743-98a1-a5d7b61fdec2 | -2.83608 | -54.12871 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56f22f10-ee4e-33bb-bab1-006657c1db45 | -7.281 | -46.80346 | 2026-10-08 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c012743-ba7b-3a87-8151-2388330c0f18 | -3.54456 | -55.52561 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e86fd3c8-9e2f-31cb-b986-84ede0fe7cff | -3.16898 | -48.61492 | 2026-10-08 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef32af5b-26e4-3dcf-a46d-365bbff3a87b | -3.02583 | -53.90575 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be7b2685-9d9a-3a42-b316-834693d9871b | -7.22227 | -55.16392 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dcb035e-4ca9-31d3-acdd-da0a9aae340f | -2.92469 | -54.13751 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d64b6b5-62ae-3493-bc05-09ad04922b85 | -3.01331 | -54.07991 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48432800-8a75-3fb1-9261-5629b37687eb | -5.24744 | -50.91372 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36030926-e69d-3c30-b2dd-c365bca4c0f2 | -2.89108 | -54.07697 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fdd5085-22d3-3928-b704-6815dc767f05 | -1.72134 | -55.44381 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9b9ac699-efc3-3dd8-b3cf-b1db7b60460e | -9.12356 | -66.00438 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7486047-d7f9-3ce4-b319-b17320a6cebf | -2.93085 | -54.07521 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08bf0bd1-b89b-348a-a405-a901d3c94d49 | -4.54976 | -54.96817 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9fb926a-c005-3248-9ffe-71cde3c79052 | -2.79893 | -54.09141 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df6b9ee8-b093-324d-827c-21a611927b78 | -5.33525 | -50.98418 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfa335c4-751d-3d11-9378-a3d9a035e7ff | -5.85804 | -57.56059 | 2026-10-08 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a19cebc-70de-3667-a78d-6b72155daafe | -2.85181 | -59.11837 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb056931-b7b2-3593-8108-ecf63474bbff | -3.06142 | -54.25276 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 469288a0-ab96-348d-8d2f-609635e9f7be | -3.0015 | -54.10977 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c3df2f5-4a1d-3023-b45d-60f1c1b21c59 | -3.17007 | -50.46053 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f758db2-d665-396c-9244-ee7a9acbc17e | -3.2822 | -53.83343 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81224ebb-dcd6-32ab-b27a-ff61b4497019 | -2.57633 | -56.17522 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 734c9faa-ae9d-32e1-bd7c-b2f7f09e7d18 | -2.99047 | -54.08824 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d25b838f-cde4-34d8-8175-696a6fab06f9 | -3.17389 | -53.83354 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be4ee7cd-b5f5-3104-8f78-f1d0bed131b0 | -1.82907 | -54.9362 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22cc0f84-4541-378f-bb91-2a1d6d7e7b1b | -3.04766 | -53.90508 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 306fd514-4552-38fc-8e07-82db9580e540 | -2.39703 | -57.23761 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac4c4082-046d-380c-b850-cb2427d94b6a | -3.29979 | -54.02242 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35f29a0a-416f-335d-acf6-67d6aed9cf25 | -3.54709 | -54.66047 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9bebee5-bc15-36bd-bb60-70f0ba414e89 | -3.48117 | -55.43969 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 589a38a7-bd28-3c49-a161-5aa2bf12cee2 | -2.12268 | -54.80109 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb78acc9-f181-3b6a-b340-11e9e5058305 | -3.10606 | -53.76368 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57f8ed27-8888-3e06-8fbd-6308ad3b7380 | -3.07625 | -54.27758 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 227f1e97-edc3-3571-8aa1-b9894bbe6a78 | -3.00261 | -54.12577 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2cbde99-ffd2-3f3a-8ab1-def01fff3898 | -2.85792 | -59.10314 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6af54a45-1f75-3ec1-ad23-795b554ef7a3 | -2.98301 | -54.06345 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3add352f-9ad9-39fd-91fa-7eaa86a5edd9 | -5.86055 | -53.46214 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ddccc38c-7567-3474-8286-bd28bcd8ffdc | -3.11486 | -53.77731 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a954cbf7-055c-3d38-8c2e-f13775d1379d | -3.66236 | -57.09474 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b52d505-661c-3012-b109-c64cef50ebc8 | -3.20193 | -53.95586 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f116fd01-dbca-307a-be37-dd9a0f2b8536 | -3.54996 | -54.66474 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 859bdc69-b3d9-30be-b1e3-4ce3596be166 | -3.00611 | -54.12632 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a8c6cbd3-2c65-3e5a-a13e-ad6e3126767f | -3.79154 | -59.37406 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc320afe-0091-3fb1-9566-8e39da9b6408 | -5.3718 | -56.06617 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 468b10c2-bbdd-3cec-a6da-f23f281f65e7 | -3.3515 | -58.21065 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99218ffc-f622-3ab1-ba49-fd74a05fa4f5 | -3.0821 | -54.26287 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6643a1f1-646d-3e79-9216-3161bcc6ef76 | -11.98768 | -57.61092 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4eff5c4e-0560-3c3b-838d-301504133a2e | -2.80013 | -54.08369 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9123e53b-daa6-3811-9554-4c7e5dc9765d | -3.99486 | -56.25627 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1990572-d979-37ed-8084-c112236f7502 | -5.51916 | -50.02332 | 2026-10-08 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e89de56-7b1c-31ab-a6d1-95bf1bd3cad8 | -6.21228 | -52.86091 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 89dafc71-b25d-34b1-a035-492faed1c4c8 | -3.26607 | -54.05328 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5feca6f6-b1c1-31e4-b328-f255efd39b02 | -3.19952 | -59.04261 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9616b475-1944-3605-aa45-6a98df676acd | -2.82821 | -59.24099 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f37d4332-7c1c-3a4d-aa60-6821bc754b97 | -3.16726 | -50.59441 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a3eb18cd-ccf1-36ad-a979-82043b159bc6 | -2.97916 | -54.11041 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79bcd5fb-4831-3398-924d-9144857df356 | -3.0893 | -53.93977 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 87e1cae6-020b-3e91-952d-07265bcba791 | -8.61485 | -67.05772 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdafc23c-e2f4-3b53-be88-68e9d3148202 | -3.58965 | -54.24016 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8340116e-e6ea-302f-b684-b9b5952364fb | -9.06085 | -65.92677 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe8fe665-00ab-3f81-a082-e22e53a0d6e5 | -2.69488 | -56.54133 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5ab2e16-e850-33a0-a984-83555ec1aeda | -1.71855 | -55.43979 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7fcc19af-5f6d-3f26-93eb-fa3beace2051 | -5.88823 | -57.75116 | 2026-10-08 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e1fbdc6-fe1b-30a2-a1b5-dfd651277d43 | -3.29502 | -54.02975 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13639131-5cc6-3665-904b-203740b34aba | -3.73131 | -53.72416 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a413cbd9-6db6-36c8-8ea9-2e17c020a6c6 | -3.28352 | -54.07996 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README156.md)
