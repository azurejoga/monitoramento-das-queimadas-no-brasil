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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acccf8fd-6e54-34d4-86f0-3b64a798d06d | -3.10531 | -54.17009 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 913af51e-b97f-3d3c-b78b-7123db4836a4 | -3.10524 | -54.14855 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1434853e-fd34-341d-baf4-8e9a21a66399 | -3.10368 | -54.18055 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c31c8e8-688c-3efc-8cfa-012869c6e67b | -3.10307 | -54.16257 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7882447c-c707-37dc-8aa8-ba646fa13017 | -3.10231 | -54.14817 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 435be554-9107-38fd-902c-51038c20f1a8 | -3.10144 | -54.17306 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56c829ad-b977-3c78-a4a0-fbada1b96900 | -3.10121 | -54.15517 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fc8de77-06b8-30b1-ba03-1aeae311dc26 | -3.09844 | -54.15116 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 790f3174-64c3-3f30-ba2c-0fe111de83c4 | -3.09789 | -54.15465 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ab073b8-9440-32f3-8b8e-8b3f9907ef67 | -3.09734 | -54.15816 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f435a56c-1aca-34a1-9dc5-8fbbc8b11a5d | -3.09511 | -54.15065 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 460656c7-247d-39b8-a4eb-07d2f27c31ea | -3.09013 | -54.16063 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60f50639-9388-36ec-9694-67a0f37aa91a | -3.08129 | -54.17358 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0528ccda-1c81-3c11-b0c6-2d1313b7b68e | -3.07796 | -54.17306 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60c7c0c0-4c96-3680-bb0d-abec3cd84a87 | -3.04586 | -54.18237 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f91faed-0128-3dcd-93a5-facff4c2061d | -2.99662 | -54.1066 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbd28e3a-5972-3af2-bb37-ff02b55a7d63 | -2.99219 | -54.11307 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fe551e5-c0b1-3858-a396-3576529c4f09 | -2.95128 | -54.15672 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4096c3ed-0231-3569-bff1-98335dad9361 | -2.94088 | -54.20147 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7b82430-867d-3c24-8172-cc7948fc7b44 | -2.93843 | -53.911 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdf72ce0-b781-3c1f-b3d7-d059c25e6cf8 | -2.93789 | -53.91451 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 627def53-7c2b-386d-b2e6-258680da100a | -2.93734 | -53.91802 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e56c9f5-3d0b-3d9e-9257-289b694e13f6 | -2.93509 | -53.91048 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b420dde-e9f2-317e-b26e-478fbfeb7d57 | -2.93423 | -54.20044 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c50e7095-834b-3cec-851b-8414de18845f | -2.9288 | -54.23516 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9b1612e-c2a1-372e-9ec3-64109adde71b | -2.89196 | -53.99442 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11f56974-8e88-3eee-abd8-9b441c0359f2 | -2.83864 | -53.98618 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ef2e5ac-d398-3d65-ab76-b58cbb372a0d | -2.83164 | -54.27044 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbd2247c-dda8-395c-ad7c-817f07e68a74 | -2.79629 | -54.10486 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60bb1fbc-a96b-3ef6-8a8a-4d519733f732 | -2.75981 | -54.0346 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ad46cde-2d32-3257-a744-a85af8fa6e18 | -2.75926 | -54.0381 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 839455d3-0d17-3c4f-b5c8-457195dd83d5 | -3.59391 | -53.78717 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 294c2e4f-99e3-3ad4-bf5c-afbdde51cae1 | -3.59335 | -53.7907 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7086b1f3-623d-31b6-b35f-e9d8fc2879bd | -3.59056 | -53.78661 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f29a229-33f0-3873-9aee-113e7cd4b8cb | -3.58329 | -53.78907 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ab29a6d-4175-328d-82f0-608533767fc1 | -3.2692 | -53.71191 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4605d005-89c9-3563-8e99-7ba3010e0115 | -3.26528 | -53.71495 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f349fed1-ff6a-3118-ae64-464b491508a3 | -3.26192 | -53.71444 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56959241-cb8e-380a-8fc9-4b078fd65d83 | -3.12172 | -53.71856 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 542c0f5d-b7ce-3555-b150-a5aa753e6eb4 | -3.12116 | -53.72211 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c9ee231-6d7a-3838-afed-b74bce930c78 | -3.11781 | -53.7216 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fc2b814-ee4d-3244-a4aa-4cc2ce4c8a7c | -3.11054 | -53.72411 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c93af7d9-e342-3ea9-87f9-6a73d4b0ad44 | -3.10999 | -53.72767 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4fac542-092c-3113-91b9-424c19d2836e | -3.10888 | -53.73478 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f09908c7-c8a6-3bd9-9c76-f4f4ac8091c2 | -3.10608 | -53.73071 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a03f9b77-2d1e-30f5-86fb-61919552359b | -3.10327 | -53.72663 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 819bcf19-ee95-38ad-9896-4c18f5bf74e5 | -3.10047 | -53.72256 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7e8db82c-d747-39e0-94b6-8558fb86b55e | -3.09992 | -53.72612 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fac9311-db04-3b04-8591-bf6feda9404a | -3.09376 | -53.72153 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fb93c66-e3c7-3219-bf99-809f81983609 | -3.08061 | -53.82821 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ef8c01f-bc50-38e0-b8ab-137725508c26 | -3.07726 | -53.82769 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ad1be93-a7a3-3b3c-85c6-3c9e45214e52 | -3.07616 | -53.83474 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d12444e7-9019-3b23-98fa-3d08e2c5936c | -3.07446 | -53.82364 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 444944ca-b69b-3ca9-a6ab-a609713b5950 | -3.07166 | -53.81961 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a66fc20-c284-3cd5-b77e-aad4fc8ea8db | -3.06776 | -53.82261 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 640935a8-8b63-3e30-9f2b-b374a633cdbf | -2.65763 | -54.62132 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f3d4fdc-602f-3723-990d-86c995d0ff83 | -2.65709 | -54.62476 | 2024-10-25 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 352e70e6-1f8b-3274-b7cf-b21e75034755 | -2.60945 | -54.53989 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 083463c3-8e77-3f38-b3c5-5f9687579a2d | -2.5792 | -54.01712 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60b21681-6d74-3a63-af3a-7c3627aa0c9b | -2.5731 | -54.0126 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b15689be-836f-39d8-b507-a82e7f2b7a91 | -2.56922 | -54.01558 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f7ee89-f8aa-3486-afe3-4f94a631172d | -2.56867 | -54.01906 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba15b82a-3ddc-3eca-bf2b-c3fe474686dc | -2.56535 | -54.01855 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d71a4bb7-f174-3ac1-9389-61313a9ff1a7 | -2.5648 | -54.02203 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f61c8ad6-6292-3113-8faf-debfbea6ac05 | -2.56312 | -54.01106 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c174ef54-8e53-371c-bcba-8a51e18ededb | -2.56257 | -54.01455 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54819c92-e2b6-3c39-849c-1e45a5c4cee7 | -2.56202 | -54.01804 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f263a27a-fe07-3537-8901-d903f63dd4f8 | -2.50197 | -54.14054 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3e6d628-b46a-3937-a008-ab6422dedbc9 | -2.50124 | -54.68847 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 675c0930-acf9-3cf7-bf2e-6aa761f6a735 | -2.49865 | -54.14003 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49ef48d0-ad63-3a72-a4a3-53069e9101c2 | -2.49811 | -54.1435 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bf88b66-27be-3260-bcc5-9d3db78570c9 | -2.49533 | -54.13951 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd4f7a58-68ce-3bf3-817f-24901f523c05 | -2.49479 | -54.14299 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13ea73ff-fd60-3c5f-b933-7a7ef07794a1 | -2.49147 | -54.14247 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f238990-0d05-3cd9-a12d-76bdeb6e3873 | -2.42192 | -53.89243 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2ee3e9a-7545-3dd0-a6b1-520af2c2bda8 | -2.41005 | -53.81517 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04d7af61-62b3-3dba-be3b-7894ebaba7b3 | -2.37065 | -54.35048 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97efc0fa-32c2-3dd4-b221-ef92016601d5 | -2.36396 | -54.32824 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28ac0011-cd49-3a12-bb53-6669e94ec93a | -2.33316 | -54.35174 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc30abf6-d6a1-38fb-90a1-85259461b9fd | -2.17037 | -54.47823 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b88a67f6-cd35-3e9a-bf03-88ca78b4a6e5 | -2.16706 | -54.47772 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0744c843-1154-3e7d-a861-d8fddb78351c | -2.15565 | -54.52876 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a9768f5-6c87-34f1-bb7b-736479a6fa6e | -2.15457 | -54.92583 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b820c39e-a9d9-3514-be85-142154ad9a7e | -2.15403 | -54.92926 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 62e16027-3654-3f0f-be47-0a3d7cb495b8 | -2.14292 | -54.8924 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8fd788e-0db0-3ee6-ae2b-67e6bc7d46d8 | -2.12033 | -54.83957 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37f1fcc9-b309-3f84-aea3-d5de7db94fd4 | -3.6839 | -54.55533 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ebf58f-c333-3c6f-a3e6-900740ca2f85 | -3.65353 | -54.74875 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab4e8da5-dc8e-3e2a-99ac-f4450458b25b | -3.65022 | -54.74823 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2d29f8c-7090-3dea-9cbb-d9b0accde837 | -3.64925 | -54.7975 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8eb06c1-ec24-3032-a659-c3bd825c45cf | -3.64649 | -54.79355 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd674794-6a36-3d03-8ecb-aeb6d6c115b9 | -3.64595 | -54.79699 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 866ccd54-2a41-311b-b0ff-3e83bc042ad4 | -3.64225 | -55.27523 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e247ed2-e2b1-3965-9d08-7356d0ed67b5 | -3.64011 | -54.68309 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab6adab0-c1e8-3a6e-9721-edce66637f17 | -3.63895 | -55.27472 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71969f55-96f6-3b0c-ba95-8493d127012c | -3.6368 | -54.68258 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96f1e82b-d99e-3684-ad1a-dad3ecb48f31 | -3.63626 | -54.68604 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8236f0bf-1440-30b7-8cbc-b6a9a5dc10b6 | -3.6335 | -54.68206 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7bc29d7-2072-359d-8011-c40ddae24919 | -4.35331 | -55.03072 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0dbb596-aeb2-39fc-b7c5-678a5491fdd2 | -4.30065 | -55.08602 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README93.md)
