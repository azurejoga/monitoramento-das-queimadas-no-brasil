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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1e5f049-10fe-3162-a0c3-70d48381d546 | -3.49298 | -42.15035 | 2025-10-24 12:17:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 79e17d22-ea0d-32a4-97c3-68a62aade912 | -7.10419 | -47.75243 | 2025-10-24 12:17:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f93a8b5d-08ac-37d0-b125-a8151d4bfb00 | -6.81154 | -45.44566 | 2025-10-24 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c32b7491-73dc-3329-ac9c-f834aea3da0c | -2.92642 | -48.30045 | 2025-10-24 12:17:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 74f63d98-79e6-320b-abc0-e22f2f19337f | -7.35976 | -45.02205 | 2025-10-24 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0ae3948e-90a8-37e0-b897-48ff26ca0b30 | -6.85962 | -42.79994 | 2025-10-24 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 9b0ec670-2005-329a-828a-b9c2fab18eaa | -6.01594 | -48.1192 | 2025-10-24 12:17:00 | TERRA_M-T | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5b04375c-f724-3b1f-b437-af4876332ed1 | -5.60464 | -45.19381 | 2025-10-24 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 281e8610-72e5-3b2b-9343-bb60558a498b | -3.67499 | -45.85733 | 2025-10-24 12:17:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e42727c5-1df6-3128-8bb5-c561b6dcd473 | -4.45768 | -43.23484 | 2025-10-24 12:17:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7080e813-5d26-3a60-9d42-61383256d18a | -7.64406 | -42.3032 | 2025-10-24 12:17:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 38ed4f30-5496-3a96-a736-dcf1fd465900 | -4.85219 | -48.57692 | 2025-10-24 12:17:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5adc989d-f91f-32b3-abd5-ea301df916b1 | -3.02819 | -49.44478 | 2025-10-24 12:17:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| d9c36ed4-1e6e-32c0-a854-f53bc5b66277 | -3.81584 | -47.57884 | 2025-10-24 12:17:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d114137a-6ac3-3701-91f0-74da7862c89b | -3.42477 | -44.82848 | 2025-10-24 12:17:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 675965d2-cbc2-3934-8763-7146c906c58c | -3.42618 | -44.81858 | 2025-10-24 12:17:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 7b1d616f-ed10-356b-8441-e90bf928c0bb | -3.64023 | -43.15926 | 2025-10-24 12:17:00 | TERRA_M-T | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 38d8f4bd-41d8-3335-b9f1-b96250fa5954 | -7.05887 | -47.22036 | 2025-10-24 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2b93875f-2f20-33f8-b5e9-4802fac23d8e | -2.26245 | -47.8485 | 2025-10-24 12:17:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| afcb760e-9671-31c8-995d-92a3e391c8f5 | -3.81712 | -47.57 | 2025-10-24 12:17:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4ff58a87-62cc-305e-8863-3aa1346562ae | -6.84974 | -45.16946 | 2025-10-24 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 35c8b7d9-cc47-3e23-b749-4d46f86e9d3b | -4.48342 | -49.01866 | 2025-10-24 12:17:00 | TERRA_M-T | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 63618362-9bd7-3839-b33f-0f21af96474c | -2.47776 | -49.22359 | 2025-10-24 12:17:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 1f350d46-580d-3293-b7a0-2c03a516bd4b | -4.85556 | -47.84717 | 2025-10-24 12:17:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6f0ba27d-fed7-3a37-9c88-d0c0d1233544 | -4.85684 | -47.83829 | 2025-10-24 12:17:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 655985d9-e84f-3eb5-b204-87f371965207 | -6.54386 | -41.69282 | 2025-10-24 12:17:00 | TERRA_M-T | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| b6120612-890b-3dcd-bd57-5b1fac10727f | -2.77223 | -48.59969 | 2025-10-24 12:17:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a74a2f0f-e0e3-35af-9d8d-14fa0acae945 | -6.93057 | -45.0371 | 2025-10-24 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4b8716ea-3742-36d9-81a3-f7ed99db1f3a | -4.52142 | -46.58487 | 2025-10-24 12:17:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 942b02ef-f8f3-31dd-a1ae-dc028bb101e6 | -4.85355 | -48.56771 | 2025-10-24 12:17:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 135c7e8e-8a74-3348-9479-72739224c9f2 | -7.65019 | -42.2977 | 2025-10-24 12:17:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 3b933e15-c394-30a0-8f3f-00ecf343ee04 | -3.43982 | -46.34227 | 2025-10-24 12:17:00 | TERRA_M-T | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 926975e3-d2a2-3527-967b-9f37916c19e0 | -5.8728 | -38.22544 | 2025-10-24 12:17:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 44.5 |
| a9d58180-ad38-3d91-a99f-bcd2b25a9418 | -2.47625 | -49.2339 | 2025-10-24 12:17:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| ad4d0777-e01f-3c8c-ae95-e112ef3572ce | -4.85205 | -46.72778 | 2025-10-24 12:17:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5e666bd0-60d0-30e9-abc3-0f3521d63054 | -4.24652 | -48.55172 | 2025-10-24 12:17:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5b6adc33-2932-30ae-811b-6950782896bb | -5.77479 | -49.2678 | 2025-10-24 12:17:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2a763686-c1bf-392f-8661-eb02c03d5c9c | -6.1107 | -48.10243 | 2025-10-24 12:17:00 | TERRA_M-T | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 2b1e5956-4384-3d14-ae39-c1cde35cacae | -1.12829 | -48.85648 | 2025-10-24 12:17:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a62103cc-2598-36d4-89ff-f681bbdcb9f8 | -3.80838 | -42.84591 | 2025-10-24 12:17:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| f39363d8-4eae-34e4-b93f-9d5147c47780 | -3.14955 | -50.16251 | 2025-10-24 12:17:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9fca0de6-9829-35e5-87cc-7c566903a56a | -7.01161 | -46.7145 | 2025-10-24 12:17:00 | TERRA_M-T | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6331b04a-6f30-3174-8ee8-09ccabd66221 | -6.84724 | -45.32678 | 2025-10-24 12:17:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 50705d94-f0d9-3e73-a227-c1b6eaa08b82 | -5.86538 | -38.22961 | 2025-10-24 12:17:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 62.3 |
| f8c365d8-d0ce-351d-90d9-c4838540d6b1 | -4.76252 | -47.14845 | 2025-10-24 12:17:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 390c021f-1c16-34b8-b289-e844365383bc | -6.54062 | -41.68656 | 2025-10-24 12:17:00 | TERRA_M-T | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 80e2f98e-cb64-3459-a08c-622ef8594744 | -3.52035 | -45.12249 | 2025-10-24 12:17:00 | TERRA_M-T | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3f351c7c-539d-3de4-9594-73652afef28d | -7.01032 | -46.72356 | 2025-10-24 12:17:00 | TERRA_M-T | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ae01edf0-2fd1-3f10-8425-52a1a3135cb6 | -2.57256 | -48.96774 | 2025-10-24 12:17:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5988e9cc-86be-326e-a2ce-320a293ace9b | -3.68624 | -42.58826 | 2025-10-24 12:17:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 04d0cdb7-dc79-34a5-b637-32a505f0c509 | -6.94426 | -44.03263 | 2025-10-24 12:17:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b7ae28b1-a0cb-3a5b-b9bb-669ec0e49c74 | -5.61109 | -45.19094 | 2025-10-24 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 39d0a5c2-d23b-34b8-9919-8634e158b72f | -3.99696 | -43.75404 | 2025-10-24 12:17:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1a2be14b-5662-3199-a3d8-02f664021720 | -2.27141 | -47.84977 | 2025-10-24 12:17:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| fa72ff69-022b-3255-8929-dc7ec1575f49 | -3.22522 | -49.35812 | 2025-10-24 12:17:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 04578d7c-9d56-377d-9438-16b3653f9e4a | -5.86849 | -38.25885 | 2025-10-24 12:17:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 106.9 |
| a78df9ac-75c1-354c-95ed-d9fd07620315 | -2.87385 | -45.26172 | 2025-10-24 12:17:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3119dee5-2cda-31e6-97e5-d2e4b86c88e3 | -6.18539 | -44.85866 | 2025-10-24 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c11fc4e5-8ece-37d9-a857-6719ee29c4c5 | -1.24285 | -47.49972 | 2025-10-24 12:17:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 71103d7e-84ea-3b2c-8be6-a5d380d9baec | -5.60606 | -45.18378 | 2025-10-24 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 34add352-1760-35c2-bc6b-be6913c6d16f | -3.67371 | -45.86641 | 2025-10-24 12:17:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b381f24c-9f06-386e-be75-1a50211fedb9 | -3.80363 | -43.30755 | 2025-10-24 12:17:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3b3ea149-283d-36a4-acf9-5000e08ac7e4 | -4.46818 | -43.23625 | 2025-10-24 12:17:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 787f297c-3ec3-3984-b61e-edf3b8f4b67d | -4.82786 | -47.78901 | 2025-10-24 12:17:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| dadd37de-c31e-3b89-b755-8e03cb238573 | -5.62317 | -46.42924 | 2025-10-24 12:17:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b178f536-9bc7-344b-b571-5c2112fab277 | -3.81234 | -42.85244 | 2025-10-24 12:17:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 9e15de9d-b790-3d25-999d-aedd222eaa30 | -6.2451 | -46.39518 | 2025-10-24 12:17:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 92b9b953-0ef0-3c59-baf8-35f201a0ff14 | -13.53976 | -47.55016 | 2025-10-24 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9f872e47-0694-3d14-ada9-c540010d7520 | -12.81179 | -48.66819 | 2025-10-24 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e66e7dca-d839-3203-80f7-b08ca98ef90c | -9.25015 | -46.46145 | 2025-10-24 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4a85a392-aa0a-3718-83d0-a3cb0a095bd2 | -11.33358 | -47.64371 | 2025-10-24 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 43a6b627-0f1f-379f-8d2e-e847254fa967 | -9.26978 | -46.45443 | 2025-10-24 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| c2298d81-6138-3a4a-8aad-a5f7901849a3 | -13.90091 | -48.39444 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 86c347e7-8f82-3d62-becd-d9b51523ae8e | -15.36053 | -42.90143 | 2025-10-24 12:19:00 | TERRA_M-T | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bbc068cb-ce8b-3629-9072-97819e607c62 | -8.73146 | -49.69103 | 2025-10-24 12:19:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 18049320-9b39-3c2c-be0a-6c55405749e3 | -10.48337 | -50.20317 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 056edd3b-f760-3d5a-bf15-95ec42530099 | -13.30393 | -47.45809 | 2025-10-24 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bf402b38-b7ff-3651-bdfb-f04be0195f91 | -10.48194 | -50.21286 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 014e748f-a7d6-37ff-9b53-a96742331094 | -7.28895 | -46.96476 | 2025-10-24 12:19:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 94d6149d-204b-3a04-8f48-3182ac313add | -10.04564 | -47.10386 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 08b910cb-4efc-3417-a3eb-2f98a6f72883 | -15.83781 | -49.1029 | 2025-10-24 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d8f1eb06-fda4-368c-bb38-04c614d4bf7d | -10.8987 | -47.98251 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0e319e91-d3bc-3a18-87b1-3405a378958e | -15.03749 | -43.34486 | 2025-10-24 12:19:00 | TERRA_M-T | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 6ec2d815-69ae-3691-aecf-fe68356ce235 | -11.36503 | -45.94922 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 70685ce9-7c18-39b0-be1f-afe25d4c05cd | -11.37317 | -45.96136 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| b883b2dc-87a3-38e4-918f-382ea638c05c | -9.24881 | -46.47109 | 2025-10-24 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f240ad1e-dad2-3a7e-8fb6-e3c98456f324 | -13.54107 | -47.54062 | 2025-10-24 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| de4aa458-c486-3835-b717-0660d96a3684 | -15.13919 | -43.78146 | 2025-10-24 12:19:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 36.6 |
| e391af4e-0f59-36a4-8ecb-4b9a42902bea | -9.20316 | -44.5417 | 2025-10-24 12:19:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ec003063-0dd7-3037-a7ae-2c3c058794bf | -12.06817 | -46.4045 | 2025-10-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 10ca811e-0728-3fce-8e5f-e43d366e60d4 | -9.85112 | -48.27454 | 2025-10-24 12:19:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e33ed29b-8eac-33b6-b4ea-c23255bd0825 | -12.18449 | -49.42984 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a6e457e7-100f-355d-8616-c63c1e5a8886 | -10.03504 | -51.61571 | 2025-10-24 12:19:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 0564ea35-ccd8-39b8-8581-09d94c87a22a | -16.25594 | -49.21447 | 2025-10-24 12:19:00 | TERRA_M-T | OURO VERDE DE GOIÁS | GOIÁS | Brasil | 5215405 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 17aebc2d-1118-3f9f-ad97-6493be43025e | -13.32816 | -43.09178 | 2025-10-24 12:19:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 0fe1a60e-b1c0-323f-9761-72a3f0c78dae | -12.07399 | -46.40129 | 2025-10-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d6d65517-d0f6-38f3-a524-1f48de6b8f3a | -15.03234 | -43.35628 | 2025-10-24 12:19:00 | TERRA_M-T | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 42.6 |
| fc35ab6f-cd15-3afc-8b37-33167fc6f5dc | -7.78748 | -46.63886 | 2025-10-24 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1e50b9c8-07e9-3aaf-a49f-c90271a2971a | -11.1344 | -47.4248 | 2025-10-24 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6d0bdbd2-cd19-3cd3-9749-9468dc48ceb4 | -9.5997 | -46.92895 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |


[Clique aqui para ver as próximas entradas](README56.md)
