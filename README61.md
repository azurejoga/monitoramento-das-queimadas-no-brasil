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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6646db0b-1c38-3b11-8321-7fb4794d58f8 | -5.84741 | -53.5619 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02ddf609-95a0-342a-b712-1bfa36800291 | -11.02069 | -48.33325 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27bf8038-d9a6-31e9-8ddb-5a1f83600935 | -13.38559 | -49.44574 | 2026-09-20 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab08c899-af55-3aef-b85a-f6acdff90cc6 | -11.01949 | -54.1404 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4949327-d144-3042-9725-b2a0ce7a89fe | -5.85853 | -51.93678 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66564537-c9fb-3375-8632-3301a823c8a5 | -9.72759 | -46.09077 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed6283ca-87d9-3747-9a1e-0fe19ea032b4 | -9.93454 | -53.98681 | 2026-09-20 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55e18e3f-ec2b-33e2-adbf-64a0f87cd85f | -8.36454 | -47.21351 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a0dcdcf-e058-3c28-a28e-4f847d5c19fd | -9.35422 | -50.09115 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 276a1843-8910-3413-b6df-6adad33aa4f0 | -7.41944 | -44.7004 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ac6d754-0cf0-3ccb-9bcf-8909ae4f1148 | -8.7712 | -48.7305 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8be32d9a-4d54-3606-8eb9-3124750cafe4 | -13.88605 | -48.5847 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 457324a0-fc29-3740-95ed-17479c49af02 | -8.76954 | -48.69815 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2ce7af5-0462-363f-859d-0e8e5d44dc4b | -9.26666 | -48.23843 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2de732b5-7694-35a7-bc16-5f4b9ae29e9e | -10.55642 | -46.75579 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e387eaa8-fa46-3822-b715-02c27564c762 | -8.36006 | -47.22015 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbe319ed-a51b-37b8-b047-bcc5d2cb5063 | -10.5575 | -51.36803 | 2026-09-20 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f1bcd5b-bc62-3c51-802e-126028098dfd | -11.01287 | -46.55536 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d08f84d-831f-37f3-ab89-64b035129ce0 | -9.27879 | -48.20448 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ad52c4b-5b05-3560-a2ee-c7c3a4e74a9e | -10.34108 | -45.31175 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0774157d-4af0-3e85-ae31-37d5e98e533a | -7.54912 | -45.44419 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1a59422-b8d5-32c2-8168-87096ffaf4ae | -9.53758 | -55.0897 | 2026-09-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20bfdd95-a1ea-30ab-9e70-e6ad976ff567 | -5.76864 | -57.45932 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf5d57f1-6b99-3050-bb7a-a931379953c3 | -8.34509 | -50.83702 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03728650-ee8c-322b-bad0-d1989dd414d0 | -10.27719 | -50.27573 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01962b29-f78f-3a0b-8186-a305d0be0e80 | -7.49094 | -46.70954 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b18332b-357b-3ca5-b1d2-c2ef5125523f | -11.66284 | -43.41792 | 2026-09-20 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23f931c2-9980-37a4-87ee-87e8c125d636 | -10.8699 | -54.09149 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f1fa658-f217-3832-bbe8-46b709e1d0c0 | -7.00898 | -45.76274 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cb52230-3f78-3651-8d95-53a70c889dc3 | -7.06155 | -47.53215 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81381545-cf06-302d-a41c-83c9c244cc1f | -10.38939 | -51.87259 | 2026-09-20 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7df2930a-dbd6-3a58-9a7e-e17d043b30fc | -13.31963 | -51.79246 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d78300a-f93d-3b12-a51e-d07d6e55d726 | -11.86906 | -47.67386 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c63febb-2a42-3d03-957b-4c8b482681b4 | -11.22199 | -54.08424 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48e60fc7-9ec5-31cc-9b9a-2db91d25e5ff | -9.69182 | -48.34184 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea9fd3c3-7cae-3d7a-bf04-ee34cb0eb3a7 | -7.53412 | -44.93086 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abf2d110-23bb-3a40-bc9f-44e38e24ff0a | -11.10259 | -54.02867 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 98e5964c-b684-3142-94d0-c688a6fae7aa | -12.31402 | -50.72325 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 536289c8-9019-392c-bfb3-ca45a249388c | -8.16862 | -54.75071 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44bf3e85-65d7-37f6-bcd9-7177924947d6 | -13.67419 | -48.57307 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94077f67-ed0a-357a-9044-8b66e4510224 | -7.43551 | -44.69408 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2270cf29-f089-399a-aba0-05a738715d2f | -10.88252 | -54.09008 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c765aeb-94dd-3369-94f4-892c4ac3851f | -9.82777 | -46.3881 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f36e89c-d799-3f34-b647-a7e9d491fcf5 | -11.87359 | -47.667 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cfedd807-d2b2-3ce0-ac86-55b9e15692f5 | -8.30393 | -46.85986 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 755bf55a-4f8f-30bc-aa55-37c14e855601 | -6.12972 | -59.94848 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e99776a-bbeb-363a-8662-b5eead48cb26 | -12.55668 | -47.57166 | 2026-09-20 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd1aca44-d10d-3eda-b4b1-0d177074b5e1 | -7.49432 | -46.71007 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2897340a-f4bf-357a-a282-75bda6267da7 | -7.74146 | -46.71799 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f4bb37d-c705-30cf-8b8f-4c4161349110 | -10.28709 | -50.2143 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad4add1d-49c9-32f7-9444-e5fa5d071603 | -9.25924 | -45.93726 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9d8ed5c-1aca-3d18-870c-91cb67e793dd | -8.18535 | -54.758 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0543fea-8571-3492-a951-f3ad27f4f289 | -7.54649 | -45.38985 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b2bc5d0-2fd6-3e5a-ab4f-5d0ff590a37d | -9.12729 | -45.71204 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0b382c1-4a15-32ec-996e-42ffaf0c79e2 | -5.83746 | -53.54457 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88953fca-30c2-391d-992c-94359e616702 | -5.8347 | -53.55646 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f6b75fc-8f8c-3e81-8384-4c50894377ea | -10.14554 | -48.28494 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7378053-5c57-33e2-bc11-840878f00a77 | -12.99224 | -46.91774 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d918e99-e54b-3a4e-ad63-9123954f4c2a | -6.64728 | -47.7052 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25dd098b-fefd-352f-b0c7-462857327b49 | -7.74487 | -46.74093 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2b8381d-4a01-324c-ac86-ca7f98e300fb | -8.42163 | -54.72363 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34683e8d-5e5e-37da-bfe8-53d58f8484b3 | -9.15676 | -49.98913 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e26abcd-bb43-3eb8-b6c0-2051c0473c3d | -10.30358 | -45.25699 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ae3a969-0bdf-3b57-93b2-9ee7c5e33269 | -11.49134 | -47.78865 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5a66203-3ef8-3a17-80dd-6a9304465316 | -11.02071 | -54.13334 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13ecad07-d1af-3a36-a6e1-0d654659767b | -13.52262 | -48.93968 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31cd2fdf-a0e7-3e06-8f9b-6b6cba2475d4 | -11.97818 | -52.45658 | 2026-09-20 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1045f65-d250-3e20-9478-b14e5fa06f7a | -11.85485 | -46.86674 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f9c3fd7-d1bd-3e1c-87b7-a10663de32ea | -10.92083 | -53.96487 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36d48de0-e796-354f-be6a-c79bd94dba3d | -11.6809 | -54.4484 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afeb2d19-f095-3617-8dd9-c42d24737a59 | -8.75245 | -48.65625 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba05e6f1-4075-343a-8e49-6c3b309bfac8 | -11.72437 | -54.55774 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7641bc93-70a8-303e-af68-325c7c3b89d7 | -6.09623 | -57.62826 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dee09da-4652-3f38-ba6c-75b31f5c5daf | -8.63365 | -47.62016 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22145b1d-02df-379d-acef-8a438424ec27 | -10.20906 | -53.91877 | 2026-09-20 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1af66e3d-babc-3bf5-9b07-56fad2362f5f | -7.59085 | -46.1463 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5e5dcb9-9f7d-3a2f-a834-24d763af806f | -6.64897 | -47.73749 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6986ee88-f857-382d-b684-ffaa71bb56cb | -6.09705 | -57.68644 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58801f84-fb13-3833-b938-e409e280662f | -10.78292 | -50.87867 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ada7cf9-cd9b-36e4-8151-d29e74543b26 | -8.77837 | -48.72808 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17a559d1-5b9e-3c0f-bfe6-ffe44a7cd48a | -9.80988 | -48.32468 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8da057f8-7f5e-35db-a8dc-f831e7132e76 | -11.34112 | -47.35069 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16178e86-c114-377c-8096-2c031e672e9d | -8.43275 | -46.86436 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 382b5f23-b1a2-35e6-8064-2932fd90a11e | -9.72842 | -47.20745 | 2026-09-20 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36454802-7225-34e8-a736-97d3c1f910e1 | -7.5928 | -46.97689 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09eed75b-ae67-3045-9f71-865729259e5d | -8.47934 | -46.85992 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e19477d8-08aa-3a11-8a7b-dd594ee344a5 | -11.88377 | -48.99905 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2027524-6af4-3ec8-a318-613d6f1082d0 | -7.95489 | -45.24035 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0123ec0-6078-3c89-99cd-748b174a3a45 | -10.87478 | -53.99401 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca33044a-067d-348f-bfc5-f4f2728e66e3 | -12.99989 | -46.91465 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e2d2474-e1d3-368b-b8d0-9b6dcc961090 | -9.26453 | -45.95036 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d4f2bfc-dd70-3086-8e32-fbf750209745 | -7.55223 | -45.42389 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b18ae342-61d0-3e26-b38e-aa64f9f9c463 | -7.77275 | -44.83147 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11db4667-5a81-3703-874e-bca49885721c | -7.5875 | -46.73565 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfb2097e-cf42-3f45-9385-e6cf5475ed24 | -12.91373 | -53.89968 | 2026-09-20 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77b167f9-542a-3990-b4db-3ae995026cfc | -8.43618 | -46.84228 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 104635db-be62-3785-8bd7-8e1b1a7b606a | -9.22271 | -43.17682 | 2026-09-20 04:40:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9229a33d-ef21-3271-aad4-a911bc679084 | -12.74978 | -50.02627 | 2026-09-20 04:40:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac4eab12-cef9-31a7-a63c-f6d3ef704b4a | -6.64964 | -50.9261 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e87a3fe8-45cf-3e9e-b161-e2d39bcd15d6 | -8.44657 | -45.86309 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README62.md)
