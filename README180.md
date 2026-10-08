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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ead4de9-ef14-329d-8fbf-d9612e36f6a8 | -3.01474 | -54.04935 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc391ce1-4a10-3cd5-bffc-1d83010e5ce9 | -4.05893 | -59.83832 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bca9ab24-0c95-3953-a81b-b51f31b053e9 | -3.08624 | -54.28692 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50b7594f-0b23-3442-944e-439aaf5f122f | -3.0002 | -57.76016 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90aabed7-ae21-31bd-85fe-41a69cca9fa6 | -3.44566 | -56.93707 | 2026-10-08 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34481617-d70b-3066-9f6f-e3363ad5de04 | -2.9011 | -56.66938 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eb89468-b280-3fe6-92e5-cf6f8d5bb965 | -3.50366 | -54.64839 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 608ebfad-ed03-3eaa-8b4f-9d9fd69adc39 | -3.35029 | -50.48783 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 144ea941-1b4e-3647-892c-dc22b71ca0a3 | -3.59631 | -54.57195 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7cd55bb-d2a1-308a-9e16-3aba27f324f8 | -6.50832 | -55.38054 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d5871bd-b3e6-3cdd-ac68-9e911e2a29a7 | -3.56699 | -54.66218 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93aa8014-a5e7-3099-9f2f-067bce70999e | -3.26355 | -54.03881 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2518850e-7d74-3674-8a67-fddfbaca79b8 | -3.52185 | -59.32294 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f20560ba-ffa6-34d0-9c85-9219a3ed7b74 | -3.29081 | -54.03941 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b58305f-8587-3d47-b1aa-3d3ecb047a5a | -3.51072 | -54.53202 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c37dd40-d39d-313a-bf39-2c5970eda88b | -3.29288 | -54.04673 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c07be51b-fdb7-3873-9a0f-06d254a5e3c6 | -3.07959 | -54.29552 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 497f0eb0-e4b6-32be-ae43-b73c89fb0674 | -3.68239 | -55.95288 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57eb72df-7f40-3612-941c-c9602bc72c51 | -3.39825 | -60.84055 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20cdd6bb-47c4-3337-b6a1-6023e2660a7c | -2.93763 | -54.17066 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd99d6b9-a0be-3756-be92-84e226cf9a8d | -3.24896 | -56.81058 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc7c4ee7-2323-35bc-8745-fb443a3d420a | -2.80006 | -54.08636 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a11b9e6-ce55-3dbc-a703-3f407a56236f | -3.58152 | -54.67068 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09620dc3-7c8a-3199-8575-4f2eff345994 | -2.85672 | -59.11835 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 731ccef9-7ff3-3f5e-9288-fbcbb01bdada | -2.9977 | -54.09061 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7b64a311-a1b5-3c62-a6c4-e492cc40dc5b | -3.36929 | -58.20221 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a577ad5-cd03-3680-a872-daa12232a176 | -3.03027 | -53.94572 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d449d3a9-6ed9-3cf2-a742-fe1d1b9b7d7c | -7.87575 | -54.97444 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0bcdf77-ae26-31d3-86bd-5aa5aa64f06d | -3.54484 | -60.20638 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4005b67-95fa-302c-bddb-bb3bc885c29a | -3.48921 | -59.58326 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d6472cf-04c9-334f-a441-6827101412ca | -3.47068 | -59.58044 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbf9ffd6-ebe0-3ca4-9078-f3d784756036 | -3.53892 | -54.67418 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc32639b-61e4-39d8-8bf9-6c378b86e0f2 | -3.20526 | -50.56598 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf0cd0d3-b96c-3b85-94fc-78cd593ca8af | -3.85229 | -58.90002 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 856bd8cc-8670-35e4-99ee-bf27ea8f8eba | -3.17437 | -50.59106 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8aa2db80-fa2c-3ee9-a1b9-907dfcc75a63 | -2.76348 | -54.11401 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d2e3aee-de20-34d0-ba37-7fa56e0e6e20 | -3.85821 | -55.98225 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8ea0297-81fa-34d6-8134-09c5d6ff3d80 | -2.98509 | -54.13884 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 169243da-27d5-3b80-be7b-4251c5c58ccc | -5.29218 | -60.10752 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c430893d-9fa8-3674-9377-d97e3084279b | -3.07485 | -54.2914 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39025181-8a37-380b-9049-6454a587f3dc | -3.05156 | -54.26756 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aab7f0f9-d27b-330f-8115-0c9806435498 | -3.73858 | -59.47227 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8fc26ca-5ca4-3543-a568-b294bee51485 | -3.08079 | -53.95687 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 59571b14-221b-385b-8e2a-339d675c5154 | -2.58624 | -56.17104 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06b3a546-e2d2-3d71-971e-347b4bb3968d | -2.58064 | -56.14634 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f068c33-5767-3249-8077-7d65f213df34 | -7.87038 | -54.97365 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 219bac58-848d-3bbf-9d3a-183759d8826c | -3.5582 | -59.49219 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1660784-2a64-3a2b-9753-04e8e84fee57 | -7.20623 | -55.1043 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24b76be5-ba47-323f-a36c-f0230af9540a | -3.58105 | -54.67377 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 34aab084-3320-332b-8b3d-ca52d5588047 | -2.77603 | -54.06603 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60ddcd5e-895a-321a-b15b-e51248dd71d6 | -3.09915 | -54.27242 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db342ee7-bc03-39d3-a940-3c7c763653a0 | -3.51082 | -59.95028 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d61080c8-a68e-36cf-b2ec-547812e60a86 | -2.9905 | -54.06596 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2aa4d710-4a68-3cf5-830f-3cf0300d6e48 | -3.11476 | -54.16874 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0e192adf-7467-3b0e-b8f9-a82ce82eb386 | -3.85272 | -55.98653 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd480924-ebfb-300b-a31c-f7afba5106c1 | -5.29955 | -60.10864 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6de7aede-3c9c-3a02-bce5-b1f437ec9448 | -3.24454 | -56.80993 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54327128-2247-3c23-8984-6e510914360a | -3.51766 | -54.66012 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fd47572-4d96-3b9c-be1d-6687cb51b36c | -3.51545 | -54.53585 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61f3f8b6-cccf-3cc4-9231-1d0a0711a2d1 | -3.54835 | -54.6815 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f73b176e-6a5c-3c12-a9fb-12efb59803cf | -3.69328 | -55.49096 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a65de67-1485-36d3-ab4f-7102ef553438 | -2.79957 | -54.08963 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0041408f-4b9a-3577-9caa-65fffbc84bf4 | -2.7885 | -54.09125 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f3da7db-ad9f-3c38-bad0-1e7fc14509bf | -3.29627 | -54.06095 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2a6cfcd-93c6-3892-8f4a-a154320d3516 | -3.54878 | -50.09716 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8524010-edf6-30d7-91c1-c1ddbc7c0ba9 | -7.2216 | -55.10994 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a02356df-b236-32e0-a13a-03a7ec041579 | -3.289 | -54.03584 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d403f351-42d5-3e83-80b5-e123addeed49 | -2.15372 | -59.22693 | 2026-10-08 05:42:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cfc3e340-3e37-3d17-939a-9dd79ff238fa | -3.93012 | -50.34275 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0bb5c3d1-31b1-3ba2-9241-74ef63ba2bb2 | -3.03103 | -54.08558 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0721b9aa-49e3-3fbc-b9cf-ac231e92fba4 | -3.11172 | -53.77254 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5f8e977-d1a3-3c53-9638-70acc68e2945 | -3.66214 | -60.6333 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8519235c-8016-3048-b940-35456400a7a8 | -6.23472 | -52.85782 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c899c5d0-1d6a-314b-a92f-5450a77f4cd7 | -2.72121 | -57.46496 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d62a1ffd-65a6-34d8-b59a-c9d9dae530c9 | -3.06958 | -54.25465 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54a5562e-5572-3b50-a3ab-2c31e9a274cc | -3.5876 | -54.66521 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03c324fe-b141-3da8-8056-c2105bf9ac83 | -2.84268 | -54.12607 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f567f05-4d94-334a-8dc1-3c600c856cfa | -3.27603 | -54.06456 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d594a788-bd01-3e13-9972-86c575c47459 | -3.31456 | -57.48757 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e30de465-1882-3d30-8580-dd69aec68230 | -3.49149 | -54.62434 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06ba642a-056d-3bc5-ab7e-6c02836b5de6 | -3.01957 | -54.05343 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0341961-117a-3b89-bd9d-52fc8d445332 | -2.78997 | -54.08147 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 032b4d59-14b8-34d9-8d9f-88fa7edbcdf0 | -3.05476 | -53.92886 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63878bf4-0151-3ee8-826b-048591088f33 | -3.59065 | -54.57432 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa29d5a8-b6ec-3fd7-9874-a79e3312e52b | -3.2842 | -54.011 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa0fbc8c-6a68-3817-9a4c-ebbcae13e6fa | -3.19655 | -50.55475 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4f98013-e360-364b-b046-020ee9f95836 | -5.29652 | -60.10374 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fe30380-b922-3b4b-9ad2-e02632fb01d6 | -3.28558 | -54.05939 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8361b88-e8fe-3867-b5a4-a61350549295 | -3.66169 | -60.61307 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef52d760-b7f7-3e1a-9c2b-257670ed5454 | -7.22491 | -55.16435 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87f8106d-3517-3d5d-b36e-ddf55a8b9537 | -3.10125 | -54.18668 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ef9689b5-eab0-330c-8be6-9e6a1acf5e92 | -4.77188 | -55.72353 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2f9723c-84da-3105-b76e-22a46bdfa785 | -3.29841 | -54.06108 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 492a0dc8-a401-31c1-85a2-b9b1c57c01ec | -3.65543 | -54.28519 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78de8650-ae6c-387f-bcd9-4a2c7f6f698b | -2.93136 | -54.17634 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 627195bf-446e-3fc9-9657-564d9c4d3c37 | -3.2998 | -54.01653 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9e5a9f9-006c-3b7d-a149-7bafd01a583b | -3.08244 | -54.27644 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 590646bf-3e7a-3433-90aa-87d7a92e504f | -2.89969 | -54.02773 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8d19da1-6848-3ca2-baeb-5a620139eeb8 | -3.9573 | -56.11668 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c817c739-8488-3aa0-856f-b4676eeb5418 | -3.1939 | -50.57208 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README181.md)
