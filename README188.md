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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 002e67d9-e5e9-3d4c-80c8-ae5b1b0354f3 | -4.36778 | -54.75531 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d26bd49-d07c-3ee9-89d4-1e7a971f79de | -3.97134 | -56.11886 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2725bef-0641-35ef-99d4-7516dbd9dad6 | -7.38416 | -55.21374 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37b0d428-1aea-32f3-bf21-96afef26ce27 | -3.26586 | -54.05959 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1dfdc664-0ac5-3177-93c7-63db1cae35b9 | -3.28659 | -54.01482 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a941b4a-a3c4-3fa8-af24-f7ff13487133 | -3.20029 | -50.55337 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 72faa3f8-0ace-3956-a259-2673f0d6884c | -6.1607 | -52.65999 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5533e231-7062-3705-b288-89777c38a026 | -3.01509 | -54.08323 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 044eb034-e04d-3976-836d-841cc13f6894 | -5.23375 | -56.01366 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68bb0f99-4411-3334-88e0-ba31b794e5e4 | -3.00793 | -54.05852 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a30fab36-d974-34d7-bca8-10bd8e3b2d7a | -3.6381 | -60.62559 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf712314-8024-3b4a-9c7b-df52e257f211 | -3.05503 | -53.96327 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| a37552d6-28ed-306f-ac90-11b9b8eea01a | -3.71613 | -54.23243 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76969ec8-b309-346e-bbda-faa273fc33d8 | -3.32415 | -50.18357 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7c7bc51c-0975-3e9d-bbd0-e9145fd894ec | -3.11994 | -53.7913 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 32f30f6a-58ee-3477-9d34-7607a2c12efe | -3.5909 | -54.67827 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b113181b-b40c-3f0f-a507-5c6607ccdfe6 | -2.03723 | -54.48838 | 2026-10-08 05:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 619d9f41-26ab-36b6-83ea-96a211cf0c4f | -3.72717 | -54.66064 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7abb4146-cfee-3de3-8d6d-2def40d01606 | -3.16103 | -61.08098 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2843983-eeb0-3c22-98d9-8c027b259263 | -3.02985 | -54.23532 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9699431-ac99-3381-8171-530fc58a41e3 | -2.50558 | -56.14685 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8090870c-c3b6-3bc0-b833-226a6087a560 | -3.57162 | -54.48772 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0df20874-01ff-3428-be0a-cab6b52e0289 | -3.05995 | -54.21057 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 516fcd51-daaf-310c-b013-a5a99d837da4 | -3.74277 | -59.44532 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39816582-e6c4-30ef-819b-bc23ebd946f7 | -3.03868 | -54.10676 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5b250a8-4c70-3b07-84c7-4a4e964f03d7 | -3.05069 | -53.95574 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| e76175ac-ef28-3cc6-915b-c9077dabc66c | -3.54904 | -59.47708 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7524073a-eefa-3a2a-b03a-634036ec7820 | -2.93137 | -56.58875 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 179761cf-9f58-3f80-9bde-6686ee051000 | -2.71643 | -57.46815 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93e73187-ff10-3059-b06a-eb9d8da7ad09 | -3.52847 | -59.37955 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5be9e62-ac75-3a5b-84c2-0f990eb610fb | -3.51922 | -54.66506 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c5f9372-8177-3cc9-8ac9-3d66b41a33b5 | -3.86292 | -50.41232 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cc069213-efc8-3a27-8db1-b9dc5923b906 | -5.27086 | -55.95672 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc11fb0f-8d06-33a5-bdb3-a6a2732641a6 | -3.47371 | -59.5854 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e13d333-f307-3da9-8d5c-db6d7b8dd2d2 | -4.06393 | -59.83022 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 743e43ca-6843-3eed-a5a5-5fb62bf7de40 | -3.65011 | -54.06504 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d895ada6-d660-360f-bcad-478084e6ca6d | -3.0031 | -54.05441 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b854c51-b20d-3618-99ff-6dcadb311856 | -3.0199 | -54.08734 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c558eb91-8411-3e28-8f38-158838cf35d2 | -3.11378 | -54.17523 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e2ca4290-bd03-3f6b-823b-f1be9b9e06d1 | -3.47438 | -59.58101 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c13b95d-1735-3fd1-a79a-cb55f11cf0b9 | -2.76445 | -54.10751 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4d7d2db-3548-397b-9cbc-b81e98035f25 | -2.48347 | -56.13859 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4db070fe-4214-3171-8ccc-85e96b09386d | -2.76205 | -54.08729 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f6f940a-704b-31fe-8598-180e072ab0ff | -3.52483 | -54.66267 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5d7ebd4-ffeb-3483-bb78-489446f4dec8 | -2.988 | -54.11932 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 496ce27a-c341-3c9d-a3e3-6664e5f3100e | -3.16417 | -54.72735 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 554cad69-9ed8-3277-b23a-9c193f099c40 | -5.30048 | -60.08348 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e5da08f-c2d3-32d1-a310-82fe63afc192 | -5.29273 | -60.10901 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60b12b5f-7f4f-34e0-9dab-3c4ef4c6db08 | -4.10901 | -60.71434 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acac8677-7454-3b5b-a803-581a742f93e5 | -2.03894 | -54.48856 | 2026-10-08 05:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a323f2f9-5757-3153-852b-c8af7769d8ff | -4.34654 | -55.12937 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9da860a-bd8d-3119-8a49-c5ec4adc8ddf | -3.10848 | -54.17455 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd6d9361-3026-3956-8309-2f4db600d77b | -3.8767 | -55.99695 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6d2793f9-fee7-3a56-8a6e-a9e4d8bd6f23 | -1.82425 | -55.04221 | 2026-10-08 05:42:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6abe0634-eeda-3a78-887e-ed37b0862f19 | -2.87937 | -54.88129 | 2026-10-08 05:42:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed02ea37-f88c-3ba8-8bc7-f245a919c492 | -3.326 | -50.17958 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98850ef2-0817-3641-b70c-75a311bacd60 | -2.58553 | -56.17569 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d160733-86fd-3991-8da3-6199292568e8 | -3.08149 | -54.24687 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d9edb4b-806c-302f-a69d-fca60e2577f0 | -4.11913 | -59.8873 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f881bf5b-f8c5-367d-9ffe-fef4720774a8 | -3.58944 | -61.63505 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c973c667-6854-3fce-8ac8-34f2163071e7 | -3.95801 | -56.11178 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb231382-13af-3db9-97c4-20558b66ba98 | -3.00684 | -54.10204 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b82374e5-fc0e-31b4-a92a-ccbe95e66432 | -6.15069 | -52.6473 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17063129-6863-31c8-92bb-be174a6f9b96 | -5.8758 | -50.10036 | 2026-10-08 05:42:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 89c8b308-20e2-307b-9090-c61526968c8e | -3.04433 | -53.96154 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8e13654a-d2f2-374a-9f54-35e7652a1865 | -3.3009 | -54.67191 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4f8d734-32de-382c-97b3-1635509d2aac | -3.52092 | -54.6732 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcf8a439-1ebc-35b0-b136-138e86c50058 | -3.48681 | -54.62043 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcf45571-6115-3980-bff4-c6e9a8c08ff7 | -3.09032 | -53.94768 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a149558f-e635-31c2-9313-4376467ae710 | -3.02693 | -53.93139 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2825d8d9-9266-3c28-b55e-18f6263b4c7b | -2.76733 | -54.08812 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5b863fb-11b9-35c2-b5c8-74a3e775e27c | -3.29336 | -54.08082 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08d63a45-b94d-3711-859d-2941f74a8552 | -3.00917 | -54.12263 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1b764827-fc00-3858-9644-1fee5f151174 | -3.57042 | -59.46204 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1069506-96e6-3c04-a726-3c8735e29e0b | -6.7255 | -55.06205 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c20aac7-8dfb-35a1-893a-cb515d5b33b1 | -6.0538 | -59.94773 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cfd8812-dc09-3630-8f76-fa6e5e66a09c | -2.88728 | -54.18275 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f6a5d83-86bd-368f-8a4f-a4cba52f92e7 | -3.03664 | -53.93985 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39b5f3c5-e1d2-3e75-924b-289c88d5473a | -3.65923 | -60.62882 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38383495-724e-3943-a0e6-a694a4da4f58 | -2.58308 | -56.16104 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8ac5da3-0cb0-3347-b2cc-b47ccc106dc1 | -3.13893 | -54.36271 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4641fb5-fc4f-349c-bce7-7ade49f9b131 | -3.72196 | -54.22972 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7135401e-99d9-39c1-acea-182b7dbec790 | -3.77561 | -59.25907 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 211c162f-43df-347d-a75d-a3622117ca55 | -3.01165 | -54.10612 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a7c29f5c-badb-3f70-be1b-6b5ab6f7d69d | -3.51594 | -54.53265 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07d20046-f73c-3577-b558-3789c77ec124 | -3.54127 | -59.50328 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ba628c0-5674-34b4-bf50-a91373db8fce | -3.06043 | -54.20734 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b13563dd-51ea-3d7e-bf15-3b71b9f73ec3 | -3.00251 | -54.0947 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 026c4f15-7a5d-3a93-b98a-ee5f7820fae0 | -4.66022 | -56.21812 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4d7e6fe-d6a1-3f16-bf63-c42ea2ab74aa | -3.52328 | -54.65779 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26342fc4-3510-3971-86aa-68cc3a967114 | -3.28957 | -54.01173 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d165b483-3ff4-32ae-a287-dfc0dc35e6d7 | -3.58326 | -59.52787 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 888159ee-78e0-3bd3-879b-48650a5f58d8 | -3.03153 | -54.08228 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0a37e03-bfb6-3756-a785-1263059937dc | -4.92832 | -55.86477 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7b88af5-b1ff-3c9c-b42a-f0d1fc1ef58f | -5.91053 | -53.88634 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d17fe55f-78ed-3752-9eb5-2a9e2c7c4ccd | -3.06854 | -59.27649 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a6d8f06-29c0-30bf-ac96-549d66fd001d | -3.26969 | -54.07031 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a9b0be4-6932-3695-ae2b-1a1864afcee3 | -2.7254 | -57.4656 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b6609c90-19ad-3ef1-8d63-b9654dfbcfd2 | -7.89856 | -54.71899 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0dd00536-16c4-3e0c-b942-0eb1e0f778e6 | -3.09721 | -54.2853 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README189.md)
