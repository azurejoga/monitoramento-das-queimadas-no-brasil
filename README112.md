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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcdd6f9b-33df-3a33-9c70-d701e62be4bb | -4.44892 | -55.07579 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a94cd44d-13f5-3878-8948-69dfaf842941 | -4.00387 | -52.08749 | 2026-09-23 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 445a2f23-0984-3719-8698-fc7dea0e3726 | -1.29774 | -55.83735 | 2026-09-23 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65a981e6-be67-3fd2-8132-82f2540fdc1a | -3.15015 | -60.63177 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3456b2a-e125-37e5-850f-f655097945f1 | -3.55897 | -59.95929 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7d4ee4c-4b49-3104-aa35-a6032ce0b312 | -9.55528 | -65.9815 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e222061-1c94-3894-ac69-d56bec4f9a5f | -3.00925 | -54.193 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f560c5fc-1af1-3cac-98c3-947208bf3d4d | -3.7409 | -59.43678 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 271898df-f98d-3c72-8f41-e5cd9d97d38d | -6.18543 | -52.79962 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 765622c1-f947-3091-9124-8e2418f647d8 | -4.4179 | -55.49816 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1a9a21f-781d-3c1c-a74e-948ee32481bc | -8.31073 | -54.76982 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02dc4515-2a3d-3da3-94a9-cd758bca7df2 | -9.16188 | -61.36782 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f1d789d-af48-3d90-9efd-d8b2e7ec0450 | -10.84823 | -56.217 | 2026-09-23 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6df48850-9105-3a4b-9294-c86a399fe926 | -3.90279 | -60.59348 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95e97b1a-96bc-3985-ae37-b8e2e0bd1935 | -11.24524 | -54.12188 | 2026-09-23 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0c5055c-d994-398b-b515-f2eea0a1e963 | -3.10763 | -60.74211 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28c2a945-e04a-3672-b95b-ab7cf55738ec | -3.76199 | -59.47599 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f18d7846-0e36-39ed-823c-b3ed829d7c86 | -3.44012 | -56.49578 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a4c6cb1-f7df-39b7-baf9-830125f9b875 | -3.24463 | -60.80986 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 548c37a0-c36b-33a6-afc9-3b6fa3236864 | -2.54751 | -49.10122 | 2026-09-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ce95ba6-6d10-3285-9dd4-b83fceb872f4 | -10.30375 | -50.50098 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c7f992e3-a06d-353a-88e4-cd0d1efd6b01 | -3.64907 | -55.47943 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eee8eef2-aebd-3005-8842-579a34c1fe50 | -9.33777 | -65.73042 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25e45602-8e67-3c2c-ad5e-f360b894073a | -3.15472 | -57.69022 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28434683-3d0b-3e02-8def-dba62d2e3361 | -3.00686 | -54.18294 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a935070-90a1-313c-ad98-ca87c3db8252 | -9.95166 | -62.22215 | 2026-09-23 05:23:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c1ac60a-3bb3-3a25-ba91-5e71d6afe634 | -4.46182 | -47.92432 | 2026-09-23 05:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45acaa3f-f46a-3bf2-a06a-2690e4ce7d19 | -3.0667 | -59.1688 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3abd78f-7a49-39b5-9dcf-c54a4060f644 | -5.89502 | -52.09565 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4aa3082-5ae0-3573-9af6-f0c4eaec8694 | -3.15075 | -60.62798 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 661c0d9f-df36-302b-8438-f6241c77744f | -5.87553 | -52.1329 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f59ab45a-3134-3979-8bed-27734f42ad58 | -3.13742 | -61.39257 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fce39323-35d8-3de0-80d0-e8092c02fc82 | -3.22539 | -46.94821 | 2026-09-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 641f22be-35ad-3751-ad47-a4d0376f831e | -10.26591 | -49.97924 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c8c7728-f9f0-30ba-8806-b1e5a933a46d | -9.05267 | -65.42331 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89a123df-e0ec-3e9e-b9bd-1bbb2d8fd633 | -9.33846 | -65.72643 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f321dd7a-e29b-3950-90e1-0a8b82053de3 | -8.18303 | -61.19119 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bd316c4-7372-3b5e-81f8-354fbf9b8882 | -5.8024 | -49.15774 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35ef5ffc-001a-3ca4-ab73-e38960a1b53c | -9.25858 | -65.43897 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 100caa88-1163-36be-8c73-4e4a96c6bbb1 | -3.07551 | -58.40609 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6818be58-9f90-34ae-9e72-5d826b7f143d | -2.95658 | -54.08531 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba54578f-d579-3305-bfe1-65144c36608c | -3.06433 | -54.39129 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eab9fda3-6f34-3b62-a17d-1afffe2babbc | -3.8176 | -58.89077 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f617a91-d439-3a80-b498-afb266bbc197 | -4.05397 | -56.3141 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 028cf00b-0139-3538-8727-04011a2fb440 | -10.29218 | -50.54635 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a033a619-8280-3ab7-80d0-9304dcc55a41 | -7.04161 | -62.92821 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c451d315-537d-3b95-92e7-5077397dfb3c | -8.5269 | -67.00809 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5d4a494-dd48-3cec-8002-ae87ffe3d6f7 | -10.2872 | -50.5421 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 524c75c3-b595-399c-b8a2-db3f3e201b9f | -3.73813 | -59.43275 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da4fd7b8-49cd-33bf-b597-8ad7ad2ff640 | -11.63778 | -50.9471 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7738ed52-a193-37d1-bcda-92aa0633978e | -3.18901 | -59.70358 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ffea6c5-bbe6-3ff1-ab3a-3bcd55fdc68d | -3.08308 | -61.1667 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb868114-8a88-3b85-ad9d-474060e87756 | -5.82482 | -52.0301 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e1f846b-1ca3-3d16-932c-426a17435d47 | -9.94219 | -48.47148 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06eca079-5861-3098-9b95-f95320cc46b0 | -10.29696 | -50.5177 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d6096162-720e-3228-921b-423dcabeb38b | -3.60736 | -60.57889 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff08829e-a3e2-36c1-94d9-db2aaf789e63 | -3.00375 | -54.17755 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39665645-529f-3365-a7aa-ed2b1d72fa7f | -3.85887 | -58.82308 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3d9581b7-3ba1-33ff-89df-0f3f4c91890e | -11.00907 | -54.14678 | 2026-09-23 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 772ce439-52fb-3c35-a30c-1f6f4566fc44 | -10.04904 | -50.2165 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f33a712a-ef50-36c9-9066-54b12ab2abec | -3.44699 | -50.61519 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01af6695-5612-3126-ac56-d3d45cda0801 | -3.90756 | -55.8391 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 434faa8e-ac1c-36dd-abc1-1e5a93fe163c | -3.6848 | -60.57534 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 303a6ea8-d8ab-3bcd-92e2-f65e436eef76 | -3.15804 | -57.69073 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d8c393b1-3f47-3fc0-aa7f-708a65cdf13e | -8.91954 | -50.89756 | 2026-09-23 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdbd366e-d9b5-3716-ad69-895db34d5421 | -2.82056 | -49.24144 | 2026-09-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b34898a9-b5e6-3635-84c4-f6d7b0f4a8e7 | -8.23212 | -62.85022 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57ce28b5-8b56-32ed-bfca-f2f03de87fe6 | -8.5244 | -67.01153 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31ab4580-4f46-3393-aefe-9d52c511c9f4 | -3.31178 | -57.85728 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2179eb5-ccef-3b08-b91d-91b0873be1d7 | -4.33772 | -55.65244 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 303d6194-081f-365d-927f-765185b45503 | -11.63552 | -50.94044 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a40e999-2ab4-3098-8772-d2b1e057677c | -2.60573 | -59.75862 | 2026-09-23 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a42c4149-2f2f-3aa3-a390-95045653365a | -8.49299 | -57.60691 | 2026-09-23 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab073878-5595-3bb2-8b58-bccbb7513557 | -3.69607 | -58.88537 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45b4d94d-7cc3-37d8-908b-b2ca842e9c95 | -3.35896 | -58.22551 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b632a0d-9990-31ce-a562-e17537ea7172 | -3.17998 | -61.10313 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 40d704c3-27a3-376c-9bf1-943bc4eeb97e | -3.93154 | -59.32715 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d9b4fc1-a2c5-323c-8ea0-116fd502365f | -10.29238 | -50.50985 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f4ef2541-b48c-301e-bf90-40051ec49dbc | -3.10559 | -60.71042 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b0cc47a-8464-3d85-bfa9-a7842a234d33 | -9.15408 | -59.49161 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af5c60df-97e2-35cc-923f-423b8d4ab811 | -3.88527 | -51.96051 | 2026-09-23 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d05a2056-1220-3f8a-ae98-6e9d60319ca4 | -4.15082 | -60.79379 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5be67b93-bdb9-3300-b22c-57296b909d5a | -3.84927 | -58.66983 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e74eae13-968a-3791-b95e-1be13d7d49de | -3.90207 | -59.72487 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a65acbe-2be8-31d8-b5bd-592bd1a44888 | -10.29416 | -50.49561 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1043f49d-a6dd-3eef-87bd-0c92bf434898 | -3.64784 | -60.60781 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d130623-f961-3c28-a797-911bf964d09a | -2.62761 | -51.70074 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78930364-624d-3850-b153-a71b5f6735fc | -3.73547 | -57.25485 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a595fec-44f9-3e4b-8f7e-fb2e25442b7a | -9.55528 | -65.99352 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99347cce-4503-316e-9a10-bfe70bec8a25 | -10.87212 | -57.17221 | 2026-09-23 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 129a96e0-6950-3fa1-8e46-9c52a89feb69 | -5.80662 | -49.15387 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ffe0f56-7095-32af-b9b4-5746c17f998b | -8.48956 | -57.60638 | 2026-09-23 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfecd4e6-41de-3229-b382-74828ed65f70 | -2.73898 | -51.54617 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa9780fd-e774-357d-a4d5-cd6a074d582c | -10.29473 | -50.53548 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 93181b81-f249-3c9a-9ca5-b554a6bae58b | -3.45981 | -60.25191 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45c05017-33f3-3003-9169-9b21898dc18a | -3.72319 | -60.57768 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b71d815-ed26-361a-a3ef-429dd35c6c94 | -3.88074 | -59.56298 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1276ac5-411b-34bf-8cc7-c0e68ce5d2eb | -7.04013 | -62.937 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| feea340d-f379-3f7f-9369-8b54fb513f16 | -3.37186 | -58.07922 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26d5b829-2dc6-34d9-b9a7-46983f089184 | -10.84512 | -56.21191 | 2026-09-23 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README113.md)
