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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65abb2e3-bfb2-39ae-81dd-4bfb5d016e81 | -3.10786 | -54.16139 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21146841-8889-3f83-b307-c2d8dbacd6d2 | -2.01631 | -56.8956 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67de39d9-e9a0-369e-9e4a-2d0c6e1bc832 | -2.60132 | -57.57407 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e1300fc-4baf-3545-ba58-5a20743e7b3b | -3.0833 | -54.27596 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f88feceb-903a-3cd3-8344-d59c0dd6b336 | -8.70037 | -45.21843 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 651ea5e0-b919-3f08-a64c-676214eb4e10 | -4.44382 | -54.97849 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 669b581c-f595-329b-898b-ddd960e9284f | -4.30135 | -50.78238 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f0c1af5-ac95-3ea3-98fd-97478fc2690b | -3.05054 | -53.93962 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f58265d-7b7c-3a39-9303-21ef4874791d | -3.50526 | -54.6692 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2fa0021-7b16-388b-9259-e558069c516a | -6.12221 | -53.0555 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9ba6a0e-515d-32e1-899d-610871ada317 | -7.45676 | -46.8379 | 2026-10-07 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc6c453f-20c7-36f5-9ffa-5abc692d0a85 | -3.44351 | -49.25632 | 2026-10-07 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b821a05-7c27-37c2-b8dc-3ff51766bc16 | -3.09776 | -54.2925 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2c572e2-ad27-3a1f-a0b4-5624e261efd4 | -2.03698 | -55.63894 | 2026-10-07 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57f1c8a5-6d96-3a03-950d-8a82ef64dd3b | -3.54313 | -54.64656 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4ed16996-3e13-339b-a339-9b20ced86e6f | -3.27281 | -54.0646 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d3a304d0-e8d0-3e0b-ba64-4f6af2207fd6 | -3.50734 | -54.63409 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9284f3b3-60d3-38c9-96f4-6396c1adde90 | -3.88592 | -52.21162 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86fe9647-c2b3-3387-ad5f-2ba2abfd7192 | -3.2983 | -54.07198 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 583f8036-c134-39ff-9ab8-e86a10d6bf27 | -2.99518 | -54.05411 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3f033ef-b9d7-3c4d-8f6d-8a33dc33dd15 | -3.47115 | -50.34698 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5310b406-3283-3d48-9d60-fbc00a1c7846 | -6.12576 | -53.05603 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45d98133-acf9-3055-a331-f520b9ffbd54 | -2.32645 | -57.98464 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a72ccc60-0b7d-3eaa-a438-946352f29d64 | -3.51738 | -58.75786 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d29d7d31-6324-305d-82da-34e0d7e95cce | -3.09605 | -53.73486 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2916251-9d45-3eb0-831c-fa33fb4f0a28 | -3.22013 | -53.96223 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55832bae-a7f1-369f-9101-38faa968ba53 | -2.59512 | -57.54554 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3830f93-6af8-3ad1-b46b-015e502ebda7 | -1.20333 | -49.038 | 2026-10-07 05:04:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de49afe3-db5e-325d-8465-7aa75903f98b | -2.89698 | -54.16149 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ece0d41b-4ccf-3be8-b632-dcfd7116290a | -3.60323 | -55.30758 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c257714d-f802-3089-85e7-4b9ef54df238 | -3.68101 | -55.94323 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d8901e4-8297-327c-9e7a-8761adf87519 | -3.30246 | -57.00411 | 2026-10-07 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c84578fe-7b74-3285-90b2-e4028f84c88f | -3.59355 | -54.56199 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 50357d9b-c1cd-38ee-8bc5-719645baa1f3 | -1.2829 | -56.98158 | 2026-10-07 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 862900a9-bfcc-3f07-83ab-15eff451e451 | -6.15316 | -51.73666 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2ff8aec-b881-3e45-91e6-f086e1528725 | -4.46186 | -54.97429 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83c4780c-51d3-3f37-97ca-d50002b1ce56 | -3.27441 | -54.03228 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f70da216-d185-30c1-b29d-8328288f8bbe | -6.40884 | -52.71673 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f7bd66c-a96b-3d2f-8a1d-93590838e3fc | -2.47003 | -56.06896 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b31e01b9-a4e4-3365-9904-38e78310a5cc | -3.06435 | -54.24438 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 820c06da-3b4f-39ca-95cd-32528288ec37 | -3.29659 | -54.06086 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6bc92096-199d-3a09-9c4d-74d12e1a489c | -3.7216 | -55.46349 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 042caa34-4a68-3cfd-9bc9-bc95be4d7064 | -3.56973 | -57.80383 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d44c7b7c-7b4a-396b-975a-8ddcfa9cf2b8 | -5.07947 | -56.29113 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36436cf6-be90-319a-8c3f-dc8327b6b2be | -2.88466 | -54.13089 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3512c419-edcb-3c0a-be6d-55f0d950aba7 | -3.00027 | -54.24169 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89235bc1-deae-3908-bba4-12041ab55603 | -3.02417 | -53.8883 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b49cfabb-05cf-3d1f-b7fd-2602b47c0597 | -5.6832 | -53.49745 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00ab7fbd-38c1-3f71-aee8-c0a6632be9f2 | -4.30879 | -54.79761 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78b7738a-b63e-308f-917b-47c02aab5719 | -2.91289 | -54.10289 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc4dff27-7a8c-3bba-8470-9bccafd528a0 | -4.14601 | -54.027 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53b2e394-40ef-35d7-8b4e-f1380dcf0f70 | -3.15192 | -50.44331 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f562f882-8b57-3a9d-a7a8-981de00a3f82 | -2.42742 | -56.53601 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95c09f06-0b48-38ff-9cfd-8b4adea18be0 | -2.77283 | -54.08447 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e56ad1bd-0926-3e2b-b5df-f9fc735da882 | -3.10452 | -54.16088 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a15c7423-b2c3-387a-a27f-d2dc3821ce9f | -3.05826 | -54.15381 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 431519d6-ab1a-3ded-a663-dbb640ad0c5f | -3.58692 | -54.56097 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05b61b9c-c1c2-32a5-ab3f-baaa1a969e6e | -3.07827 | -54.26445 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08e4b09a-48be-345b-857c-abef381e70a9 | -3.06102 | -54.24386 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1464cbe-3db1-3dce-aecb-5749e7ae1993 | -3.2288 | -53.88347 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60070e34-93f1-36b2-b301-57ebf51a291e | -3.22181 | -54.30472 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69b81750-e37b-322b-b7ee-5975692c569f | -3.09661 | -53.73127 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcbfaccb-5506-3158-9c91-6c97673d13c4 | -3.09995 | -53.70972 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c08fbd07-5d3c-32e5-9b05-2ba627f01eba | -3.55039 | -59.48088 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a81a650-7e46-3863-a81b-b86700795029 | -3.3842 | -58.19965 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 927a9617-bb5c-3a47-8a4d-3a1efa61719c | -3.67426 | -54.54592 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abf6aa7f-44e4-3fbd-bedf-354cedff119b | -3.04896 | -54.21338 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89175d84-61b0-30f0-a35a-b878501fb914 | -3.65927 | -60.63037 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 325416a3-628c-3b0f-9a73-049ded293912 | -3.27949 | -54.06562 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 42c1b6a0-e118-3a08-a1bd-ee2250474522 | -2.56941 | -50.68056 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72092e63-1b3b-3496-9579-552535846604 | -3.13451 | -54.36237 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e62db00-ec1d-38b4-b75d-55619e04ebda | -3.4921 | -50.09488 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e1d9af9-6559-3c67-ad21-2915f2b192d1 | -2.52642 | -58.09668 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 123c5a3c-903a-306c-9a05-fd9a67c11412 | -6.92167 | -43.66871 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 72ab6b4e-77e7-3907-9407-662517e694e8 | -3.50449 | -54.60883 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f42f9e8-3f6d-3efe-beff-bb7852691023 | -3.02752 | -53.88882 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac454551-a8b6-339d-842c-2668cc1b757c | -6.00094 | -53.50457 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e7d9158a-2321-361d-9fc1-5ebe2c9038b1 | -3.56503 | -54.48279 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 917446e5-e6f3-375d-8ca0-79e507b1d08b | -3.30096 | -42.28033 | 2026-10-07 05:04:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b341029-b1b7-373b-951c-f720cc0cbd43 | -2.9413 | -54.1396 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 580dbe9f-e1c1-36fe-bf5a-2122c022739c | -3.73931 | -51.21719 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d88c980e-b214-3914-b37c-215fa2562b04 | -3.96657 | -56.11916 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1e696a8-ce24-3cd5-8c31-588ad607802f | -3.28372 | -59.2088 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd85890d-2724-3ada-91f2-a9c7646e7109 | -4.84001 | -45.79488 | 2026-10-07 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 219ba390-f996-332b-98b8-baf642d97daf | -3.1084 | -54.15786 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 023ffc51-9a98-37c7-82b2-3afa4c26fae9 | -6.08133 | -53.88046 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b78ce3f6-6e2e-3851-80d1-5263213d2dc5 | -3.03824 | -53.93046 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c28c8acd-98cf-3b70-9d2b-5988d12efdd3 | -3.28838 | -54.05253 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ccccfc3c-c2c3-38b5-9c4b-7393aaac0074 | -2.93093 | -54.20613 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df14850f-18c4-34ef-8592-eedfa8794ed2 | -3.0082 | -54.12455 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c99ec840-f859-32ad-b503-7d8d6f27f414 | -3.02813 | -53.9071 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 70171ed0-6202-371f-9796-9bfe09f6ba10 | -3.2767 | -54.06159 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 853f1dc3-f5ae-3116-a1cb-8e18bcdaddaa | -3.09098 | -53.72306 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53130c8d-fb27-3265-9736-596f0a2ddd66 | -8.70651 | -45.21913 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a4e6ff61-f7ee-3934-9336-0109986fe9a3 | -1.51169 | -54.81842 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0a47ab8-f769-326b-beb1-a5f6a3fd32ed | -6.21281 | -52.83403 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f322710-4f04-341a-b5c2-2e704765d7e3 | -7.27865 | -46.14914 | 2026-10-07 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 64de25e2-ecc8-334c-b179-db610426607a | -7.89628 | -49.83698 | 2026-10-07 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e0fb701-9a0c-382a-afb9-8249dc25d442 | -3.84753 | -55.98664 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 946d485e-1991-35a5-8d88-50eb76aa4681 | -1.47748 | -54.77813 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README71.md)
