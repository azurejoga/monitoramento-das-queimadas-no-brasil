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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efafb232-6a47-36fe-b1aa-48b0aca8815a | -10.81077 | -44.30364 | 2026-06-06 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7f060c3-f8a0-3c08-b0f0-40d8162ed88d | -8.93149 | -45.67947 | 2026-06-06 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 113f28b1-6f0d-32e8-bbc1-6bae9e3bfb98 | -6.43831 | -44.58344 | 2026-06-06 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7b0627d-3534-33d1-b7e4-507614b753a7 | -9.89856 | -47.48234 | 2026-06-06 04:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f67dbf27-6184-3f84-8627-ee2d4a62cbc4 | -6.85374 | -44.96515 | 2026-06-06 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1809e8e7-ba71-3fff-8a73-efefe1994c73 | -9.68963 | -47.0444 | 2026-06-06 04:23:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b2206f8-db6d-3168-bb02-d35ce93bc7b9 | -12.00613 | -45.34996 | 2026-06-06 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27dd5d77-caad-302d-9435-89b1787554a2 | -11.11906 | -45.13942 | 2026-06-06 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e46aff5-ea5e-30f4-ae88-7ff2b3bdadf8 | -6.04994 | -47.89051 | 2026-06-06 04:23:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ba7ec374-8b36-3bf6-a6dc-79a778472c22 | -10.94533 | -46.93649 | 2026-06-06 04:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ee23539-bcaf-3bf2-9e81-44a3334427b1 | -6.44435 | -44.56667 | 2026-06-06 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44316208-2b11-3c1f-a34e-edfc9cec9dcd | -10.52035 | -43.63955 | 2026-06-06 04:23:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47a4c34c-fe43-34d2-847d-ca647b9b4012 | -7.09879 | -46.94383 | 2026-06-06 04:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f92e7b5-8a7f-3cd5-ac0a-06086ebe8184 | -11.00401 | -54.31405 | 2026-06-06 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94a534f4-b051-387d-9f2b-c42eb4cd9e38 | -11.00532 | -54.31672 | 2026-06-06 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbc1da67-d2f1-3d00-8df9-e92ed2bc91cc | -8.46136 | -47.00061 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e019dcba-3e76-360f-874b-86decff2095c | -9.36903 | -50.53807 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fd055ab-3605-3842-91a0-40e0990f16c0 | -6.43886 | -44.57998 | 2026-06-06 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30358161-0be1-31f3-ac3c-234277315213 | -8.40914 | -46.87052 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97a0b16a-5b5a-3017-8fce-41f2a36e63e8 | -7.3513 | -49.83477 | 2026-06-06 04:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a44324f-9d74-3438-a5a8-38a81e2fd5d6 | -6.04637 | -47.89269 | 2026-06-06 04:23:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a5fbdba-83a3-35fb-9956-dc843aee76ff | -9.67447 | -44.541 | 2026-06-06 04:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb14f030-5658-3cae-a1b0-092aa065310f | -6.44766 | -44.5672 | 2026-06-06 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8974d70-adbd-37d5-bc0e-e99548e080f0 | -6.05 | -47.89328 | 2026-06-06 04:23:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e6e46338-96ac-36a1-949e-93149517a0c4 | -7.2717 | -46.80972 | 2026-06-06 04:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72606e03-edd5-305b-9c14-36d72c7239f3 | -8.40574 | -46.86996 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d058523-d983-3108-a586-dfbc1f400b24 | -10.04071 | -48.27394 | 2026-06-06 04:23:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b7736ae-c606-3c86-b0d3-722d928b6c3f | -12.06797 | -48.42908 | 2026-06-06 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca49720d-2ab2-390b-8776-07e57ca03675 | -9.89918 | -47.47857 | 2026-06-06 04:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1c76a73-405a-343e-9cbe-d5faf5c84bae | -8.41232 | -46.89372 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a5e54a3-4079-36a2-b1ca-ddda5894a19f | -8.92256 | -46.8594 | 2026-06-06 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a522550-f6e1-3299-ab9a-8a1f178d502d | -8.93978 | -45.67008 | 2026-06-06 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c328aa52-12fc-3fd0-b167-c2801746d0ce | -9.16871 | -58.07052 | 2026-06-06 04:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 056a25b3-127c-3fbd-a0ca-10ce9571bfd3 | -11.46914 | -47.98462 | 2026-06-06 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d4faaa30-146c-30b4-8d73-89fd0645b7e3 | -7.15587 | -44.05961 | 2026-06-06 04:23:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bebd2260-db92-3e93-b612-06c83c309b9c | -6.99394 | -42.77819 | 2026-06-06 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad05a5ea-5d5e-3250-b899-0fe0ffac32eb | -8.79454 | -46.61506 | 2026-06-06 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cbac039-237b-3092-9a3f-0d31fefebb66 | -9.08038 | -50.61127 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fc92b5f-7e84-314c-b125-2de594e04fde | -9.07974 | -50.61494 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39d3f102-2112-327d-b077-ae43c1170ab7 | -6.98877 | -42.88087 | 2026-06-06 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6be055dc-1fb7-35b8-97ea-dffdf164894e | -7.00014 | -43.86269 | 2026-06-06 04:23:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 688f7258-949b-3fc3-b243-cedf658bd6b8 | -11.99627 | -47.76471 | 2026-06-06 04:23:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3421dcad-7707-3f56-ab60-ec8ae78d6ede | -10.94198 | -46.93595 | 2026-06-06 04:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7d2d43f1-afe1-38e0-860c-2ea65a16f296 | -10.00317 | -48.6736 | 2026-06-06 04:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d22f12f2-df70-32da-ac0d-971b1feb9b6a | -6.72625 | -44.37436 | 2026-06-06 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d48535a-9e27-3831-8dcc-b63232178594 | -10.18869 | -52.65061 | 2026-06-06 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ab0b1c0-1369-31c1-85b5-b607bb6a1f46 | -8.42034 | -46.88734 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f4c31f7-6b72-3818-b8ec-f306e3dd43a6 | -6.98102 | -46.74147 | 2026-06-06 04:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 37cd7315-fabc-3020-95e7-df23f37cc097 | -6.04631 | -47.88992 | 2026-06-06 04:23:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e9d2cda8-56d4-3a9a-a50b-2310f828d4a5 | -8.39637 | -46.84207 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cfaeabc-a142-3a7d-8abb-1350b137836c | -6.04926 | -47.89471 | 2026-06-06 04:23:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 78a41f6d-a623-3d32-bfbc-46c5bbe4c832 | -6.44545 | -44.55976 | 2026-06-06 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e63ed21f-0e57-3d4b-9109-ec78b31c813f | -11.07637 | -48.25888 | 2026-06-06 04:23:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a1f8f6c-fe05-3f52-aa09-55e555038459 | -6.98477 | -42.88408 | 2026-06-06 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 36739f99-64a2-3f4f-8f5c-742d832547c6 | -6.43777 | -44.58689 | 2026-06-06 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 892f48a9-7820-3c3c-8bc3-e4884163581b | -11.03913 | -44.32038 | 2026-06-06 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e09373f7-7bd3-3e1d-8024-7e5c160f4ee3 | -11.01022 | -54.30899 | 2026-06-06 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53584a3e-a855-3d53-ab99-caf602961da0 | -11.01149 | -54.31164 | 2026-06-06 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7c83dd7-8332-3d98-9713-78974cb64f3f | -10.50958 | -51.94106 | 2026-06-06 04:23:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d942156-6267-3203-93e5-b2b28eec3ae6 | -6.99276 | -42.87766 | 2026-06-06 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8399f3fe-faea-3a55-9950-1759b8c9f93a | -6.72348 | -44.37038 | 2026-06-06 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66048668-c812-3fa5-9cc3-24ee075939f5 | -8.86946 | -50.18776 | 2026-06-06 04:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cafbf1a-8620-3fdc-925b-8a09b34d7b6c | -9.9026 | -47.47916 | 2026-06-06 04:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a4d6414-d227-3cce-8d13-fdb6e93b3c73 | -13.40122 | -46.60476 | 2026-06-06 04:25:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb1b0ff8-ad0c-3db5-b529-3efa5b935cda | -14.37899 | -45.56422 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ebc3375-2089-31a4-88d1-a10d81de7061 | -12.51126 | -46.30538 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1faffc5d-51a7-3ead-8656-60e4607ef657 | -14.22149 | -45.7927 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f1e28624-3ae4-339b-b109-59c13b29aee9 | -12.49886 | -54.73773 | 2026-06-06 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f6ace28-0ebc-3023-ba91-3fb3d59ba399 | -11.55055 | -52.79071 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b105436f-c518-342a-9fd4-01e0e4184a95 | -17.3056 | -42.64752 | 2026-06-06 04:25:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce8c09d2-3485-3e0d-848c-d379588f5e47 | -14.22703 | -45.80094 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87338eca-5b64-308a-a257-96fc0586f04e | -11.55873 | -52.79715 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd1a063f-d014-34b9-8134-1682e954d76a | -12.77139 | -59.01002 | 2026-06-06 04:25:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9eede5ed-e4ec-3bd8-bcb4-c4fc4d274136 | -15.31509 | -41.89735 | 2026-06-06 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ee904646-4671-3620-9d56-f385402fc445 | -11.54883 | -52.8001 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07292590-d91c-392f-8e0d-ace34dec98e3 | -14.62519 | -54.458 | 2026-06-06 04:25:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71ea5adf-1e3a-3413-8945-a8ed1844c18d | -11.05511 | -56.92404 | 2026-06-06 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15aaa891-2cd5-3963-8e44-e878c88b29e5 | -13.49637 | -56.56991 | 2026-06-06 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d881cc66-68f2-3343-92d2-d73e9e300d55 | -17.29853 | -42.64118 | 2026-06-06 04:25:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ac75170-7412-34e4-a3d2-9be32367c7c0 | -14.25051 | -58.44717 | 2026-06-06 04:25:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 05e34b67-f582-3ad3-b336-e22d5c3c1ad5 | -14.39067 | -45.57722 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 692d5382-821d-3e4d-ab76-27a41a8a9c23 | -12.10047 | -52.01117 | 2026-06-06 04:25:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2150c9d5-8669-3df7-9a70-659fc3586fac | -12.80517 | -54.86489 | 2026-06-06 04:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df7bb89d-46cd-3819-9d06-11501422ee7e | -12.50118 | -46.28243 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0eed7def-5323-3510-a065-271eeae08977 | -12.3891 | -48.12831 | 2026-06-06 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58e0b7bf-e209-3c18-90b8-3875955e3b70 | -19.68264 | -43.92613 | 2026-06-06 04:25:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 786002ee-b1b0-37e5-a9b2-240f49e4bb28 | -12.51083 | -46.26551 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 147d2a90-219f-39d2-b029-9a9bb5fc4113 | -16.43143 | -43.72342 | 2026-06-06 04:25:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 188aed11-a656-34d5-b95e-101ddd6056a2 | -15.52708 | -42.66734 | 2026-06-06 04:25:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d1599ddf-39a3-326f-8c25-bff902ede254 | -12.92381 | -47.88854 | 2026-06-06 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb8419b6-400b-37fd-92a9-b9e714762257 | -15.45873 | -55.8603 | 2026-06-06 04:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3006b075-d7e4-36cb-ad15-4ada30870d5d | -12.5056 | -46.27591 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 085273fc-517c-3b99-b466-fd7d73a33094 | -12.50393 | -46.2865 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a76f73d-0543-3130-9400-0f33228fc5d7 | -12.50671 | -46.26884 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7222bbc-6917-3295-ab06-788298b02b6d | -16.60246 | -47.61936 | 2026-06-06 04:25:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59cd6f84-77f4-3f6b-9b2f-05fb562fc366 | -11.72175 | -56.84256 | 2026-06-06 04:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7882ed7-e340-37fd-b6bb-92d42e7d746e | -10.57303 | -57.31813 | 2026-06-06 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d891606-42b3-3943-a28f-a4120cc217cb | -13.49224 | -56.57295 | 2026-06-06 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fab5e37f-1d99-375a-90ab-e72df11265f7 | -13.30356 | -43.76476 | 2026-06-06 04:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cc876d9-037e-3cea-bfbe-e06f85e6cfba | -13.4956 | -56.57368 | 2026-06-06 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README8.md)
