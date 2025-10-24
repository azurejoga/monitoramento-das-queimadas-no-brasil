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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa6aa1f9-81e0-38da-8946-97792189a852 | 0.3589 | -50.9414 | 2025-10-24 13:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c3a7802c-e32a-3f58-b3bc-8d2c0675fb77 | -22.4723 | -51.6082 | 2025-10-24 13:20:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 391.6 |
| be2f9bef-7606-3d80-aa30-11d25c36c403 | -11.0222 | -49.8383 | 2025-10-24 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 2c3a7b3c-23f3-30db-92db-49c5300f0c91 | -12.7786 | -47.3752 | 2025-10-24 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 8497c503-20e0-306e-aa6e-2627f5159669 | -14.3792 | -51.5255 | 2025-10-24 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 86ef08ae-bf8e-3602-bb18-9d5010dac858 | -12.8328 | -50.9552 | 2025-10-24 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 2dba2091-8963-3515-89a2-4c4f553749e5 | -11.0219 | -49.8598 | 2025-10-24 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 69d5fa15-4fa5-3961-9485-37718f944cfc | -14.7456 | -46.6096 | 2025-10-24 13:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 91897d7c-ba36-392a-b7ad-000771efebba | -12.067 | -46.4189 | 2025-10-24 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| c85be62d-52ca-3fad-88d8-4ec44eb031bf | -10.8854 | -50.1325 | 2025-10-24 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4a628e6e-7e55-36fd-afba-e2a851af5024 | -19.0323 | -57.5174 | 2025-10-24 13:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 65dddd71-ea84-3c25-80bf-69885ec013c1 | -10.9044 | -50.1304 | 2025-10-24 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 208c9651-b1e2-38c5-9a29-566f40ba5f0a | -12.1696 | -49.4211 | 2025-10-24 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1d24696c-4082-3985-bc5b-60af3bec5748 | -12.8331 | -50.9338 | 2025-10-24 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| af4e14a8-966b-3fa6-a712-3c03a0bde112 | -11.1583 | -49.6073 | 2025-10-24 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 76ad4678-ba7d-3c28-a673-2ccfab811e8a | -12.0862 | -46.4162 | 2025-10-24 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 01e7f0d3-5ccd-3a71-9099-8e304009252e | -10.8857 | -50.111 | 2025-10-24 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 961419cc-dc0d-3ab5-9405-12fda27552f4 | -13.8958 | -48.3919 | 2025-10-24 13:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| cf0624fd-2670-32c3-a5f8-69482c8b38dc | -14.3792 | -51.5255 | 2025-10-24 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| aa3e3d7d-c5f3-3b1c-951b-e787220e3e01 | -12.067 | -46.4189 | 2025-10-24 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 3f316ff1-649f-32f3-bf4e-c0cdd27b3d31 | -13.3451 | -47.9402 | 2025-10-24 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 5b552d0a-b733-321e-8485-f5c8cdb3bdb5 | -10.9044 | -50.1304 | 2025-10-24 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 64676ad7-fdf4-3a3f-9976-93f79b19520d | -12.1191 | -46.7279 | 2025-10-24 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 3a22d74c-3401-3427-817a-d283f2d9e731 | -10.8854 | -50.1325 | 2025-10-24 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 82807ac9-5167-357a-80d9-3cbcdb3c1fca | -12.1696 | -49.4211 | 2025-10-24 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 26436f5a-880d-3660-b3d7-2e99a6caf92f | -12.0862 | -46.4162 | 2025-10-24 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a27d5fd6-4836-34e7-a1c6-93d38184899e | -12.6471 | -44.1386 | 2025-10-24 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 2f73bb77-67df-368f-8261-671cadf0f23c | -12.7786 | -47.3752 | 2025-10-24 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 5eebeae4-1c13-3232-9036-4b18885c95ac | -19.0319 | -57.5382 | 2025-10-24 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 1d4a7ab6-f95b-33ae-883a-f2994fa55da4 | -13.9151 | -48.3889 | 2025-10-24 13:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 55a67cc4-a4ff-3f3b-8391-97b59bf104e1 | -12.8328 | -50.9552 | 2025-10-24 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 4df2a226-2f84-3636-b6d4-8d9f172525a0 | -22.4729 | -51.5855 | 2025-10-24 13:30:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 363.5 |
| f2ae93e5-a1a2-36e8-a5ca-4e0476744c71 | -13.8962 | -48.3696 | 2025-10-24 13:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 737e11c0-b800-3938-9e7c-4111b35ed6cc | -12.6476 | -44.115 | 2025-10-24 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 023fd73a-177e-30d7-a2b8-d57bda696870 | -12.0478 | -46.4217 | 2025-10-24 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c5155b5e-9d8f-3d87-ae92-aa04f65d1605 | -12.0674 | -46.3962 | 2025-10-24 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0657266d-f8c2-37dc-8443-5ec59068e6ad | -10.8857 | -50.111 | 2025-10-24 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 8aa7cf24-602f-3658-8de3-122a8b1dfb4c | -19.0323 | -57.5174 | 2025-10-24 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 9cbcf77a-ee40-3fe1-b2b1-2a15036d285f | -11.8727 | -50.1277 | 2025-10-24 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ca786308-a543-396e-871c-c680ae331fe2 | -14.7456 | -46.6096 | 2025-10-24 13:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 052f14a9-58f8-30dd-831b-6dc7a55ce4e3 | -10.9047 | -50.109 | 2025-10-24 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| c16db0b2-c679-39fe-b053-e081f999bb5d | -11.0222 | -49.8383 | 2025-10-24 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b8aceb71-b222-3f0f-88a0-d861a14c15a0 | -10.958 | -50.3601 | 2025-10-24 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 59631fb0-9354-3628-a6d7-a56084bdebcc | 0.3589 | -50.9414 | 2025-10-24 13:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 84.2 |
| db1f583b-56bc-31bf-b833-bb8b0abcd210 | -10.9047 | -50.109 | 2025-10-24 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 130587af-16c4-31fb-ad47-ebb6954ae648 | -22.4729 | -51.5855 | 2025-10-24 13:40:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 144.9 |
| ef2db485-81d9-31ba-b662-ff1ccf3e456b | -10.9577 | -50.3815 | 2025-10-24 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c425ac0d-113e-3534-92aa-05ff52ec905a | -10.9387 | -50.3835 | 2025-10-24 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a6bca0f4-2bd4-3182-b8b3-6170defee779 | -12.0862 | -46.4162 | 2025-10-24 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 6773ded4-021a-36a0-b59f-6baeae4a2b29 | -10.8857 | -50.111 | 2025-10-24 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ba918d65-aaf5-35c2-b32d-490b5c6c4564 | -12.8328 | -50.9552 | 2025-10-24 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| e24c400a-d2e2-37ea-a1e4-c9042cded5d9 | -13.8958 | -48.3919 | 2025-10-24 13:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 8fe3fe37-8af3-3e44-bae6-234d2d3c059e | -10.8854 | -50.1325 | 2025-10-24 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 2e25767f-308f-35f9-8186-fc0c9b106194 | -10.9044 | -50.1304 | 2025-10-24 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| fa8e9100-cdb3-3ce7-94b8-029b386deb80 | -19.0323 | -57.5174 | 2025-10-24 13:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 78ecbb6c-97a9-3010-940c-71c0a36546dd | -12.7786 | -47.3752 | 2025-10-24 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 82e6f241-0d8e-3907-8126-41b42412c882 | -14.3792 | -51.5255 | 2025-10-24 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| e063d83d-3458-3e8b-86b1-7541d2a50c03 | -12.067 | -46.4189 | 2025-10-24 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 2daaf3b2-ab2f-3c70-8c9a-0264cc94917d | -13.9151 | -48.3889 | 2025-10-24 13:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| afc70cb9-e6ea-3927-ae97-0cd2ba430d16 | -12.0674 | -46.3962 | 2025-10-24 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 7cc7fabb-83b6-3041-8bef-230d9c8b60c2 | -4.8933 | -43.2349 | 2025-10-24 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| a2c6a2d2-6bc7-360d-a6d0-ed009b834048 | -11.0222 | -49.8383 | 2025-10-24 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 7d529589-4c3f-32ae-a9fd-c3c1a2ffc0dd | -11.1583 | -49.6073 | 2025-10-24 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 443bfc97-bea8-3f7a-a7bf-d563ad6ac5a1 | -14.7456 | -46.6096 | 2025-10-24 13:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d51c4945-81a4-3364-9d4a-167c6ab0ed66 | -12.1696 | -49.4211 | 2025-10-24 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 3a922389-2227-3fb7-844d-570cecb6712a | -14.7045 | -52.8217 | 2025-10-24 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| a6b4ffae-90b9-3db6-89b0-5acab32f4a8c | -19.0319 | -57.5382 | 2025-10-24 13:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 701d5f02-d75a-3989-874b-8ee73384c4fd | -10.8854 | -50.1325 | 2025-10-24 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 08e4e444-205a-3341-bb4f-d48c65f9f85a | -12.1696 | -49.4211 | 2025-10-24 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c03fce5d-2357-3ccf-94c5-1810fc6b7a29 | -12.1003 | -46.708 | 2025-10-24 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| cbb335df-956b-3e95-8492-0070010c6bca | -13.9151 | -48.3889 | 2025-10-24 13:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5fa3d68a-3f3a-35ed-a1e9-9b347988b598 | -11.8727 | -50.1277 | 2025-10-24 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 33d65cd2-3cf9-3a18-985a-3bc6b3b2e350 | -12.9377 | -57.0258 | 2025-10-24 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b387eed6-0c1a-3af2-85cc-bc7b198b06e6 | 0.4141 | -50.9619 | 2025-10-24 13:50:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 29ca5fdb-3eb3-39bf-bb9e-d053f4e2f9ce | -12.1191 | -46.7279 | 2025-10-24 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 34aed2a8-4277-39f0-b58e-b2f48504d066 | -19.0319 | -57.5382 | 2025-10-24 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 8d6ed537-e3fd-3fe8-8312-c8b48b52ff46 | -10.9044 | -50.1304 | 2025-10-24 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 2db96809-757b-3b72-976a-ac8fcb158d36 | -12.8328 | -50.9552 | 2025-10-24 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| f695cb3f-9c2c-386b-a922-e0ecaf6891e5 | -12.0862 | -46.4162 | 2025-10-24 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e9c2edc9-ae0b-38ab-8e22-e7a5560677e4 | -11.1583 | -49.6073 | 2025-10-24 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d2cfea73-76f4-3070-8ced-db9748172bad | -12.0674 | -46.3962 | 2025-10-24 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f29c0fa0-ccdb-31b0-82fa-53d0b520a122 | -12.067 | -46.4189 | 2025-10-24 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 3ed2b5f1-79f8-35cb-ba66-8c8bedc89a91 | -12.7786 | -47.3752 | 2025-10-24 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 6154740e-f028-3220-b65f-87d2e036bfba | -5.6065 | -45.1852 | 2025-10-24 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 47d9d6b8-6e02-3808-8a26-29bbb7185beb | 1.3533 | -50.6833 | 2025-10-24 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 55dc93d7-a4f0-32a4-9fb6-618f944be5c7 | -11.0222 | -49.8383 | 2025-10-24 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b0817944-c0ac-3572-917d-8ba1a0f32338 | -10.8857 | -50.111 | 2025-10-24 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 516e5c31-9ae4-3309-84ef-429d77f1ad36 | -12.0858 | -46.4389 | 2025-10-24 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 8d54ecf8-8103-362f-a077-7cc392c5080c | -10.9047 | -50.109 | 2025-10-24 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| d1947bf1-09e0-31ba-bc6a-79b2a4fd71a9 | -4.9122 | -43.2103 | 2025-10-24 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| af2e9378-8648-34bf-b08b-2f83415cd8c3 | -12.1884 | -49.4404 | 2025-10-24 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 208.7 |
| d27774a3-1774-3975-b70c-ccdade32ccec | -12.8191 | -47.2572 | 2025-10-24 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| aa18e052-1308-3793-8861-4c4ba423e6ed | -13.8958 | -48.3919 | 2025-10-24 13:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| ca828466-21c1-33f3-bf21-0f902d374b80 | -12.1693 | -49.4428 | 2025-10-24 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 457.9 |
| efa0a2a9-729a-39b7-b609-67fc8c2eade2 | -14.3792 | -51.5255 | 2025-10-24 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8f5e4be1-8253-3638-bd68-448a4b43f8aa | -14.7261 | -46.613 | 2025-10-24 13:50:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| b2f8b282-d619-39fb-876e-53e8f8023feb | -14.2727 | -52.1152 | 2025-10-24 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3258cae8-692a-3498-b702-6e406e827e52 | -22.4723 | -51.6082 | 2025-10-24 13:50:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.5 |
| ae51a4a3-0492-360a-a127-8ee2fbb3f3a5 | -17.3353 | -55.0156 | 2025-10-24 14:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| a5806f1d-8f97-3c55-a235-fc6ea96ef4db | -10.8857 | -50.111 | 2025-10-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |


[Clique aqui para ver as próximas entradas](README61.md)
