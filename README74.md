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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7973c24-18d7-3bfb-8a43-83e5b95dcf65 | -3.1972 | -50.5592 | 2026-10-08 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5c013ef8-4aa1-39b5-8e4c-6e61d7150c0b | -6.6317 | -43.73 | 2026-10-08 04:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7a0d621c-e686-38d5-98e7-8b137b9b63fd | -8.6107 | -67.0301 | 2026-10-08 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a1288f7d-1124-39e4-aa8f-f82884257500 | -2.7797 | -54.0736 | 2026-10-08 04:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 862fc2de-2c0a-3840-b194-cdfa42535165 | -3.1697 | -58.6244 | 2026-10-08 04:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 1e0bf23f-0a11-3fd0-b1df-3f0c58f476ed | -8.6291 | -67.0296 | 2026-10-08 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5202256d-f50d-3330-9a99-edcea471ebcf | -3.1114 | -53.7839 | 2026-10-08 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 4397fda4-29d3-3283-93b9-fac767cee243 | -8.6292 | -67.0111 | 2026-10-08 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e52e1afa-302e-323c-a123-34969c9193b3 | -4.3473 | -43.779 | 2026-10-08 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| f66744ae-7180-3993-826e-5a61699d30ee | -3.1115 | -53.7637 | 2026-10-08 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 5c1fb931-7cec-3e57-b437-784bd262f736 | -5.6932 | -53.487 | 2026-10-08 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e8d9ce2b-96cf-33cb-acaf-de9772239430 | -3.1602 | -50.5812 | 2026-10-08 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 16c7c627-d0eb-3161-b8a2-e634e6e17640 | -8.7228 | -45.1812 | 2026-10-08 04:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| cf3335f6-9a22-3f30-b712-feb75c7646ef | -10.434 | -47.2601 | 2026-10-08 04:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a59611d6-8736-33ad-8a90-75a56b545181 | -3.5861 | -54.6741 | 2026-10-08 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| ea81ef3f-7695-3ef5-a423-03d33aae927e | -5.6934 | -53.4667 | 2026-10-08 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b02959e8-edda-3b9b-8094-5de1fe0ca14e | -3.1973 | -50.5382 | 2026-10-08 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c324e8be-efed-3dfa-98c2-fdc93e3caddb | -1.5306 | -54.5359 | 2026-10-08 04:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 3db7ac77-a063-3486-9421-209d7089bf19 | -6.1431 | -47.9214 | 2026-10-08 04:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 1f490791-25e7-3278-8a5d-9972dcd2b4fe | -8.6107 | -67.0116 | 2026-10-08 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 04f679d0-25aa-3696-9953-1d49afd1295d | -3.5862 | -54.6541 | 2026-10-08 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b2fa8575-b8c9-38a0-a34e-15f2adbf0aba | -13.1668 | -43.2673 | 2026-10-08 04:20:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 9b2bf47e-60d4-3c7b-a98b-3c92d623093e | -3.531 | -54.6557 | 2026-10-08 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e4357ec4-db71-38b1-b612-080c3f594b8e | -1.5489 | -54.5556 | 2026-10-08 04:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| f94e751e-a44e-347a-980a-56698bf130ed | -2.4987 | -56.1659 | 2026-10-08 04:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| fd1c3224-626f-3769-9836-1fdfa8045404 | -8.6107 | -67.0116 | 2026-10-08 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 104e4a8e-5ca3-3ca9-9a94-6581c6007bc2 | -5.6932 | -53.487 | 2026-10-08 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 4885da33-443c-3027-89d6-cff0a2717e85 | -3.1114 | -53.7839 | 2026-10-08 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| be0069d4-3400-37c5-80c1-c477607dcaf6 | -2.7797 | -54.0736 | 2026-10-08 04:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| bad1a4a2-4970-395b-acf6-3427890ee224 | -5.7376 | -45.1533 | 2026-10-08 04:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| ce4ea503-5226-37a7-834b-cc1fff4328f7 | -10.4151 | -47.2623 | 2026-10-08 04:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 5763f066-85df-39b6-9e3a-9b969621ce4b | -8.7228 | -45.1812 | 2026-10-08 04:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| c40b69b3-40c6-3db0-883d-db2426d5a793 | -1.5306 | -54.5359 | 2026-10-08 04:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ac5ad37b-d95c-3a40-b1e2-9c0dfe146434 | -3.11 | -54.1862 | 2026-10-08 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8fb07db3-02f8-3212-957f-b88a2025c922 | -10.4147 | -47.2846 | 2026-10-08 04:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 7fe0bd22-807b-3795-a86c-a96ce492bdba | -8.6291 | -67.0296 | 2026-10-08 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 338434de-ede4-344c-b893-9276c3228b92 | -1.5306 | -54.5558 | 2026-10-08 04:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| ba4ec9f9-1a14-360e-bb8e-7608806fd5d4 | -3.1101 | -54.1661 | 2026-10-08 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| b136c278-7900-31bb-b165-94a7ac3973cc | -3.5861 | -54.6741 | 2026-10-08 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 3b056632-6816-3d3f-b4fa-089b7f16661c | -3.1786 | -50.6016 | 2026-10-08 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 794cc25e-58ae-3326-a6d7-47aa18f90b1b | -11.3937 | -46.6922 | 2026-10-08 04:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| c56d63e6-7cae-34d8-8884-18a5e0aa9b98 | -3.0913 | -54.287 | 2026-10-08 04:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 04b64a7f-c89c-3e29-8d4b-21f45c622a23 | -5.7117 | -53.4862 | 2026-10-08 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 57b901ab-ca0c-3cb5-bd93-6189d23d64b4 | -5.8599 | -53.4586 | 2026-10-08 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a3fc565e-9fcf-33c2-ade7-a48b10515659 | -8.6107 | -67.0301 | 2026-10-08 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 86ea67b5-4e57-3498-9225-c0758823e08a | -3.1972 | -50.5592 | 2026-10-08 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a5c0ed33-831a-34af-8e37-be9098e8b1fe | -1.5306 | -54.5359 | 2026-10-08 04:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 909696db-5a1e-38b5-87be-9b23a9e42f78 | -3.0913 | -54.287 | 2026-10-08 04:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ac0837d6-05b0-30d9-8891-d3dc66a8e987 | -3.1972 | -50.5592 | 2026-10-08 04:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9cd74914-0583-361a-9fc4-1fec01a58f16 | -1.5489 | -54.5556 | 2026-10-08 04:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 86d11b8c-1eb8-3bbb-89dc-a396cd9dbeb3 | -5.8599 | -53.4586 | 2026-10-08 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| bc9e24a2-0de7-3698-8173-e8113f4c345b | -5.6932 | -53.487 | 2026-10-08 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 8a1676a5-5f72-3fe0-9053-5cf17c377dae | -8.6107 | -67.0301 | 2026-10-08 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 9abf6c0d-457d-3a77-adaf-d470c21b167e | -5.7117 | -53.4862 | 2026-10-08 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 088a0498-c494-3105-8207-a944c27d57fb | -9.0592 | -65.9209 | 2026-10-08 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 4a156866-ac7f-37ef-ad91-19105176f0cf | -3.5493 | -54.6752 | 2026-10-08 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 6861f711-6d7c-3d66-b1e2-f6465c732b30 | -3.5861 | -54.6741 | 2026-10-08 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| afe1f874-974e-3532-865b-82801bdfb803 | -3.1787 | -50.5807 | 2026-10-08 04:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| d5c9488c-e08c-3d63-b245-ae53b6f0d706 | -3.1101 | -54.1661 | 2026-10-08 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 30301d17-b8b9-3063-b72d-2dc74494213c | -8.6471 | -67.1774 | 2026-10-08 04:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 37449951-740e-35e6-831d-fd83b4809dac | -8.6107 | -67.0116 | 2026-10-08 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 06771bdb-619a-3e20-b9f4-21f7ae979937 | -3.1786 | -50.6016 | 2026-10-08 04:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1acb9d95-2617-382a-9816-9e3456b989dc | -2.4987 | -56.1659 | 2026-10-08 04:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| deb928d9-6d97-308b-8c1c-7cd446e1a7dd | -8.6291 | -67.0296 | 2026-10-08 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 12102403-6b03-321b-96c8-f173d875d84d | -3.11 | -54.1862 | 2026-10-08 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d9a9b421-7967-3a14-b89e-95caec597368 | -1.5306 | -54.5558 | 2026-10-08 04:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 165.5 |
| aabd5577-97ce-3b65-b0c8-8e41801731fc | -3.1114 | -53.7839 | 2026-10-08 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| bbc6a106-7c6c-363a-93b9-2d98950d927f | -2.7797 | -54.0736 | 2026-10-08 04:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6e46639f-558a-376e-8872-43a66004a50d | -3.16432 | -50.59219 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b225f87c-1e7f-32e7-937c-21f0cb0c9981 | -3.29267 | -49.13017 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf0163cc-aa6d-39b2-bf14-3f7ed21da798 | 2.43415 | -50.81957 | 2026-10-08 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 72079227-cdbe-3407-9bbf-06246b400c1b | -3.2347 | -46.95822 | 2026-10-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c6586c9-651e-3921-b4b8-bbe6680156e5 | -1.8263 | -55.03436 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 208b2ae9-f158-3c4e-a186-08c987e41dcd | -3.28129 | -50.01995 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b644dd96-9795-3f41-95a8-61bd50ed5c7e | -1.52883 | -54.55328 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33fb1a91-2dbf-31a5-8619-26df49e4923e | -2.99437 | -51.05155 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eecfef5b-ef4c-3350-a997-9f51f988ce4d | -0.42355 | -51.73108 | 2026-10-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f384aa8-4a27-3cd1-aeee-9f4eaca06b23 | -1.28282 | -54.55922 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52c37fe5-5a02-365e-b73b-18f3f3ba3be1 | -1.12737 | -49.18866 | 2026-10-08 04:44:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af2aa5f2-71f2-3541-88de-1b7849f40145 | -3.13297 | -49.2438 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c480e1bd-29a8-3869-a62c-613a066219b8 | -1.47153 | -54.6387 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 212170f2-3c28-3c27-9133-4f289fb6f0cb | -3.1996 | -50.56618 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 318f4772-5685-3005-b72d-e2ffb0040b64 | -1.46271 | -53.23912 | 2026-10-08 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 999cb1c0-5989-3b78-9473-b1c5676474ac | -0.08532 | -49.47814 | 2026-10-08 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c8d2f35-cefd-35dd-90bc-2a8a4c0ba347 | -1.11309 | -47.73395 | 2026-10-08 04:44:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11901b5d-279e-3304-a5ef-6ce20900e627 | -1.82651 | -54.93753 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a6d4e64-a6bc-385a-bb70-f7ef7aea4598 | -1.75522 | -56.19333 | 2026-10-08 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 492b7b10-18eb-3ec4-9776-b815a5699eb7 | -2.08583 | -54.56573 | 2026-10-08 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 53dda952-636b-3757-8afc-14ceb264ea49 | -3.29603 | -49.13069 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32e895e4-3328-3654-8673-558dff4ae952 | 0.44628 | -60.53752 | 2026-10-08 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbb8dcb3-f7e4-3f86-9ac9-b1b0eb11bec3 | -3.27855 | -50.40639 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0201fc26-e75b-34a3-8106-a45f533a72c7 | 1.34773 | -50.83236 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 547afbd1-8117-3b8b-a9a5-598eaf4555c1 | 1.69525 | -55.62295 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6da95030-29c2-3201-97c8-0e9077f24118 | 1.68846 | -55.63689 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e3680f6-bbd7-37ad-92cb-7fa05c52c8f7 | -0.4179 | -51.72271 | 2026-10-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5696d751-2921-3f02-8956-a62cc1eb5895 | -2.05402 | -56.38413 | 2026-10-08 04:44:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ac4ca990-0b22-381f-a691-09ab88ffa4ac | 0.58077 | -50.2086 | 2026-10-08 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e1160d8-adc4-3115-ab06-f2d906e81216 | -1.33178 | -55.43102 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eaf496dc-699c-3a9c-b7ac-812feec10502 | -2.7847 | -51.67233 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 257b585b-2f88-3121-96c6-22b52f2666f6 | -3.19461 | -50.55489 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README75.md)
