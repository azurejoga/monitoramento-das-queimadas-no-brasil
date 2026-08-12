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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c439db7-b153-3c87-881d-f1f257172ed2 | -16.10221 | -49.8854 | 2026-08-12 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 19bf82ea-599c-3982-9063-23feb8cb391d | -14.33883 | -54.04574 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 09b07ddb-158f-3552-88f2-d70e0b8a2118 | -11.69134 | -44.15792 | 2026-08-12 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c27e89be-8b25-3a8d-a2ff-2217e322d3eb | -13.65819 | -46.24015 | 2026-08-12 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88e29762-47df-311c-a884-60dc2f3da18b | -13.54035 | -46.27393 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85674963-2b7e-36f4-82dd-3310488a04c1 | -9.37762 | -47.44125 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99b62220-e970-3443-84d3-1c7d32066b37 | -11.93321 | -47.35864 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| add9fed7-4136-3b42-8ce8-cf052e8a2a32 | -20.45552 | -47.534 | 2026-08-12 04:17:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91d6e3b4-ddaa-3831-a969-14ff3504be72 | -10.7085 | -47.90042 | 2026-08-12 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15e6ecfa-635c-3589-b32c-4f91368bfc85 | -11.60771 | -54.66468 | 2026-08-12 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 549072ae-f56c-3d2d-acbe-9b6abba3d8af | -11.4634 | -44.5526 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d68e14b7-9c29-3d0f-80ff-8c498ad8cb81 | -16.72158 | -46.39994 | 2026-08-12 04:17:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e62d89e4-eebc-3fa1-96fe-ffe5bf805b76 | -9.37689 | -47.44566 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d53dd59d-05c2-3c5f-9011-dec40b52fea7 | -13.30105 | -49.69911 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0cfbf205-3a81-31b1-9c18-dc5c46b90eb6 | -15.30128 | -48.88118 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f7d5cfa-7d85-306d-a03f-0fd8da4b2d6b | -13.57201 | -46.25994 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7f8458fe-f111-3e9b-a69a-3527b1a39dda | -10.84396 | -50.34997 | 2026-08-12 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac0c7eee-d88e-3eea-9456-a4120e79d3ed | -9.92948 | -49.26474 | 2026-08-12 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8d655fc-911a-3b82-a66c-47f6741aa073 | -10.36776 | -46.38938 | 2026-08-12 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfa9a8d8-1dfe-30d3-bbab-9c818b5324bb | -13.53519 | -46.28444 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db4fd30b-da95-3964-a41c-ee704ffa4504 | -16.10815 | -49.88464 | 2026-08-12 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3fcaccce-8a17-3fa2-8fca-0c35d743cc1d | -9.36436 | -47.45262 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87d7689a-e4db-3bcd-a819-79edb616a9b7 | -9.135 | -46.38515 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e858a9d8-9936-3639-acde-7b92bf0fb648 | -12.85852 | -52.04524 | 2026-08-12 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c2397cc5-e188-348f-9ea7-e231517755ac | -11.96264 | -47.31305 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83d98f5d-fff9-3f68-88d3-87ffb22ca7c8 | -11.8251 | -51.83388 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 87c8a036-6428-3f22-b867-20694c7168a1 | -10.36618 | -46.37716 | 2026-08-12 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9939ec4d-6875-36f8-9404-fb502d913650 | -13.88735 | -53.8306 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ebc6f27-7afc-3613-8549-9c53bfcee138 | -14.51586 | -49.29158 | 2026-08-12 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 647a2455-9165-39a1-9397-90f880b59991 | -12.17872 | -50.16256 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57c7305c-31c3-3cd2-831b-6f37b2858dd2 | -15.00131 | -46.60352 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0046a00c-45a8-37f6-8304-4647be64e2e2 | -11.8357 | -51.88265 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8952aedf-fd39-3dc5-b360-e73f71d56bac | -10.22406 | -45.93018 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cb7cf27a-9c9d-37ff-ae66-9a32d6d88438 | -9.34736 | -47.48602 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e4d993b8-3867-3f85-a46e-14fd9e892c69 | -15.52541 | -45.85925 | 2026-08-12 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bff147bf-b762-37ed-9c4e-f4bdefc5f009 | -11.95353 | -46.33474 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2d57e12-bd98-3158-b491-11d7154a8acf | -15.51935 | -45.85454 | 2026-08-12 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a202a4e-e4ee-386b-ba29-090e4a1821fa | -9.92541 | -49.26401 | 2026-08-12 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa742ca3-ac4b-3f8a-a724-8f7415a9e12f | -11.9463 | -46.35738 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 45fe50c0-b6d6-340f-901d-b60122e11b58 | -10.63895 | -47.49013 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b52b7aa2-7159-3c93-a3ac-5a06bb50bf15 | -11.03102 | -45.67126 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b184c1c6-4ad8-3aab-9f9d-ba96bc25c316 | -14.03167 | -53.59473 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9a16914-948d-3ab2-a216-0fa5664100ce | -14.28892 | -45.29033 | 2026-08-12 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9fd1e44-0cab-3492-865a-e5fdc03ffc62 | -11.46947 | -44.55717 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9b254cfa-c667-3e88-800e-c2e983141c48 | -11.95842 | -47.31656 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86a2df68-f63d-356f-be51-6a590c1cac42 | -13.57874 | -46.26111 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06f2c4bf-51cf-3edd-8625-8ce7723932e0 | -14.58777 | -46.75207 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0536eb1-270b-3cc3-baa0-1f4e34c491ea | -14.58993 | -46.76014 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93ee7705-7de9-3814-9bd3-43e8c78a13b9 | -11.89144 | -45.83473 | 2026-08-12 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 510608c5-74e0-33ef-ba7b-9aff66b5ed29 | -15.06196 | -45.327 | 2026-08-12 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b6c1787-23c8-3dec-a9b7-94520e572159 | -14.33372 | -54.04441 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bfa744db-c37d-3f24-ac1a-a0286283cf5e | -13.53579 | -46.28075 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32bdfb07-5600-308a-97c7-784e49dcdc47 | -10.10546 | -46.20509 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ea53084-df64-39c7-bff4-8dca9f24c782 | -13.84052 | -53.78749 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67b8fad6-c29c-3774-a88a-3ed648ad574a | -13.8411 | -53.78446 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09823c5d-d391-3d00-a1cd-97cd2198b770 | -9.6274 | -48.32996 | 2026-08-12 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3226b5d-a3b3-34c2-b72d-66db5e84007f | -9.13658 | -46.39751 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ee72533d-7a7a-3582-8efd-9b074cbcae26 | -11.49373 | -54.60407 | 2026-08-12 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2365462-3cf6-3238-99c2-95eb424972dd | -16.10692 | -49.88113 | 2026-08-12 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 204b3968-2f7a-3798-ab35-a2c123df7446 | -11.46671 | -44.55313 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9fa7671d-4718-3459-bf15-a5699611130c | -13.89809 | -53.80296 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b964f1e-9892-3dfd-8242-ff6f437ac9e0 | -11.46544 | -46.61059 | 2026-08-12 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3471548-dcb0-3b04-b625-367057c87e62 | -13.54709 | -46.27507 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e9db5f30-73db-3d3d-9807-7c33815d278c | -11.95008 | -46.33437 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b38e3a1e-121b-3c72-a890-3a77f0e9468c | -13.27894 | -49.67128 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bbd80ad7-bda3-37c3-a8a6-2d49ebf518ca | -10.22003 | -45.93341 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 35.4 |
| bd6d3c0b-98b3-3513-8c11-bb84f95a23fd | -13.87133 | -53.83062 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32473b8a-a52d-3c62-a39f-7bc74d7d80c5 | -11.98145 | -46.37857 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4086471d-21f1-3bfe-923e-fbde25c96279 | -14.44503 | -52.26053 | 2026-08-12 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2c87e7a-5fb4-327e-a713-1369da51ddd7 | -11.95812 | -46.37097 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf05d318-abd1-36a3-a77e-8eb4ef689cc4 | -12.72753 | -48.44502 | 2026-08-12 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e99539d-61aa-3c61-a6e3-328dcf012773 | -11.78309 | -51.8521 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 70800bee-f48c-3683-9532-d3f1955f30de | -13.53916 | -46.28131 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29f92934-bf26-32bb-807b-f25986367bfa | -11.46616 | -44.55664 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 945572fa-9030-31a6-bad9-37329458f162 | -13.53123 | -46.28756 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d871a0b-a3ad-3440-b983-0b587e342e2f | -11.94972 | -46.35795 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e691275-b7c5-3568-afe2-98316a10bc86 | -13.27986 | -49.666 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c91295d5-86bf-3e07-8c1b-b0aee40f160c | -11.4623 | -44.55962 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9460cac7-6e0d-358b-9df4-528cd8fe0728 | -11.98179 | -46.39812 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bf2c342b-8985-363f-89be-a29201050019 | -13.83994 | -53.7905 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21fc5c04-78ba-3a06-be27-29f35492610d | -15.05865 | -45.32645 | 2026-08-12 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab058768-0959-3441-88a5-c87ea8952cf8 | -8.88138 | -50.17826 | 2026-08-12 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a40da5e-6b79-3898-a0f7-79e5a47be80a | -13.78002 | -43.17912 | 2026-08-12 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d4c713a4-b506-3fed-adad-6b16959895fa | -9.47925 | -47.82995 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d18984e-710d-359a-8ac1-0f34c1c2053b | -9.0267 | -47.4731 | 2026-08-12 04:17:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c22300e-a00b-31d7-a542-ef44be561dc7 | -16.10726 | -49.88957 | 2026-08-12 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c55d6527-7507-3bf0-8a1c-e32b933657b0 | -14.28673 | -45.28268 | 2026-08-12 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c82716c5-3811-3c34-8362-103a1fea9119 | -14.0356 | -53.60147 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d4b3e4b8-bdbd-385e-9592-96827fb0c01c | -15.28197 | -48.86611 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f5c1333-d139-32e6-91b5-a642d961b7a0 | -13.8571 | -53.82159 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb432601-15fd-384e-8fe5-45283c609fcb | -10.42275 | -46.32734 | 2026-08-12 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 802d4e67-b13b-3d8b-9b9a-1c733bdb5e74 | -10.71287 | -47.91969 | 2026-08-12 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db2e5292-02b5-35dd-a747-a50b5a76e1ec | -16.26071 | -49.42204 | 2026-08-12 04:17:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f5877516-5d8c-396a-8bd2-50c775c6ccd1 | -11.98488 | -46.37909 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3d2cccf1-303b-3947-8c5c-3de7a6cdb33d | -14.99362 | -46.58693 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 117bbcc9-75e8-32fd-bca5-eed9b0e5624a | -12.16276 | -50.13182 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eca29716-845f-35fe-aa98-0de87a052920 | -13.43523 | -57.04808 | 2026-08-12 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11477920-fe7f-3635-810c-c93fdf31f580 | -12.57444 | -39.1822 | 2026-08-12 04:17:00 | NOAA-21 | CABACEIRAS DO PARAGUAÇU | BAHIA | Brasil | 2904852 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ce945b6c-bf96-3c72-aaf0-d1386ec94083 | -13.57323 | -46.25251 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 564c9877-8ab1-3555-831e-1fc7d2514e68 | -22.27282 | -48.66161 | 2026-08-12 04:17:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
