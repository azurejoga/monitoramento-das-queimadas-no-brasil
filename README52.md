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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ae8c6dc-9f9d-3e66-a3bf-9ff32dc6be00 | -3.39303 | -41.47339 | 2025-11-14 11:17:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 20c4f33a-9af5-3f28-a1df-352e09eddaf2 | -6.71325 | -42.96767 | 2025-11-14 11:19:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 191.5 |
| a42e102c-94bb-33ad-af2b-4a8ef1c4b267 | -6.46044 | -37.63663 | 2025-11-14 11:19:00 | TERRA_M-M | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 18.2 |
| b416674f-0edb-36d1-9e23-0e777fed840e | -13.5778 | -43.14496 | 2025-11-14 11:19:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 7b18a31d-c105-3123-b84b-984d8e92a5c9 | -5.60669 | -37.8052 | 2025-11-14 11:19:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 0b6b0987-9b95-3ea8-a0b2-8309aef505a7 | -6.85939 | -37.46364 | 2025-11-14 11:19:00 | TERRA_M-M | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 4aebca88-d062-33ff-a078-ed39735da3a1 | -5.60451 | -37.82001 | 2025-11-14 11:19:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 66f0b039-da45-34ee-a54d-be0c1aec5c51 | -13.57796 | -43.13907 | 2025-11-14 11:19:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 38.0 |
| b76619e8-9d7b-3657-af67-f917d7f0e9db | -5.60629 | -37.81126 | 2025-11-14 11:19:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 110.4 |
| 7d405769-f4ea-3142-95fd-18373609627f | -13.67105 | -43.04665 | 2025-11-14 11:19:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 3f062718-4129-30e4-8ea9-4cacf9f66504 | -6.85569 | -37.4563 | 2025-11-14 11:19:00 | TERRA_M-M | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 7482f838-7262-3daa-a3f6-cc1b5b90b3f4 | -13.58291 | -43.11677 | 2025-11-14 11:19:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| af71f527-c254-35d8-87c2-ae610febc068 | -6.71815 | -42.97585 | 2025-11-14 11:19:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 170.4 |
| 788f6410-7bf4-3d12-b32f-e33ddde4e41c | -6.85374 | -37.46947 | 2025-11-14 11:19:00 | TERRA_M-M | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 6d9aaf81-2868-3a4c-b009-dbdfdcd40024 | -3.7473 | -44.2705 | 2025-11-14 12:10:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 100403d6-5de5-364c-9aee-bb1d8f0fefad | -3.7473 | -44.2705 | 2025-11-14 12:20:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 5e583744-6d61-3c13-9870-23645438f45b | -3.7473 | -44.2705 | 2025-11-14 12:30:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 22abec44-11e6-38cc-8e9e-cad89427a121 | -3.7473 | -44.2705 | 2025-11-14 12:40:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 202ad09a-bc94-3609-90fa-4109461a388f | -5.5259 | -43.6794 | 2025-11-14 12:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 2ca4c278-b413-3330-ad4a-ff75fe1c3b5c | -5.0156 | -44.3366 | 2025-11-14 12:50:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| d1f49ada-2c76-3802-aa4e-a6309f51d837 | -5.5447 | -43.678 | 2025-11-14 12:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 7f28d7d7-8f28-3b06-874e-48e6c93d9e26 | -5.7983 | -42.5822 | 2025-11-14 12:50:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 9b4d4e62-5d91-3c63-92be-aa42e7403732 | -1.61212 | -53.21227 | 2025-11-14 12:55:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7af94691-936a-3e01-a5ca-5cf04d9ac1ab | -2.06039 | -56.62014 | 2025-11-14 12:55:00 | TERRA_M-T | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| af64648a-c0ee-3f7f-9b93-b8784927fd37 | -1.90836 | -46.79208 | 2025-11-14 12:55:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 197.6 |
| d1681e15-0f74-37a0-8694-a38decda3844 | -1.91642 | -46.75779 | 2025-11-14 12:55:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 23fbe7a9-bd14-3652-9d05-c2adbd2aa285 | -1.37723 | -55.39584 | 2025-11-14 12:55:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bf029c03-6e5d-3f12-aa46-09884b461c6a | 3.18477 | -60.25226 | 2025-11-14 12:55:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 27.1 |
| a37dd5b2-9c1c-3d20-8cd7-bcb691768603 | 3.18674 | -60.26618 | 2025-11-14 12:55:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 40.4 |
| a4fb6213-1021-3d89-8e84-7dfcaed6cf3f | 3.37775 | -51.31561 | 2025-11-14 12:55:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0f5d7e94-5e11-3586-92d8-e8b9360652f6 | 3.16491 | -60.2691 | 2025-11-14 12:55:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 809bdb90-7cef-3c12-8298-d9e80ba1aab7 | -0.34422 | -51.75646 | 2025-11-14 12:55:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 28.6 |
| b716ac04-b73b-301f-b4b5-e819865ed850 | 1.84862 | -56.06921 | 2025-11-14 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5d18e81b-de94-327b-ae74-7cd4ecf2c632 | 0.11486 | -49.89922 | 2025-11-14 12:55:00 | TERRA_M-T | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 5e644e24-aa92-316a-8f5b-c7f75382467b | 2.16355 | -50.88412 | 2025-11-14 12:55:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 323ca24f-8dee-3c9a-a510-5eed4e239daa | -7.40703 | -48.61811 | 2025-11-14 12:57:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 6ec289eb-901f-34b9-ab69-eacfa282c85e | -6.23321 | -53.56554 | 2025-11-14 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 52aad432-016b-372e-b795-c0ee539f3530 | -5.74526 | -49.03128 | 2025-11-14 12:57:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 444b7fd4-b5f0-3b64-82ab-ef94ed45f27d | -6.16087 | -48.01944 | 2025-11-14 12:57:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f69cd477-86a7-388a-8f6e-1c350e89d2f3 | -7.39388 | -48.65829 | 2025-11-14 12:57:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 2b1e04ef-4aa7-3813-90da-b0dbee583db8 | -7.39793 | -48.6239 | 2025-11-14 12:57:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 72807aed-4803-3eb8-bfdd-7c57da68420a | -10.77363 | -52.20364 | 2025-11-14 12:57:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| b10cbea8-6635-358e-8df1-ab0336578a08 | -6.15621 | -48.05683 | 2025-11-14 12:57:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 138.5 |
| e4d11349-60ee-3408-b58c-fa046eea381f | -5.74906 | -49.00117 | 2025-11-14 12:57:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 2cd33a42-b96c-3535-9052-04ccc5c0902c | -9.96921 | -49.94708 | 2025-11-14 12:57:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 8299a391-aa71-3f86-af13-73b17c7049ca | -5.74863 | -49.0252 | 2025-11-14 12:57:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| c2f4ab7c-1cfd-389c-b7fb-18fddd07ecd6 | -10.8703 | -52.16008 | 2025-11-14 12:57:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| af8011aa-e92e-362c-8d4d-463b0c0005e5 | -6.17283 | -48.05923 | 2025-11-14 12:57:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 687a5718-ae55-3715-aad6-85eda5ea6d87 | -7.4027 | -48.65257 | 2025-11-14 12:57:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 158.2 |
| bc34cd02-4411-37b7-82b2-d604849c3490 | -11.72975 | -48.51788 | 2025-11-14 12:59:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 43cd2fdb-71b1-3f8f-bd8c-9e2a36429564 | -11.85197 | -49.21141 | 2025-11-14 12:59:00 | TERRA_M-T | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 5a1419b2-c571-3d28-a54b-daf72ac278ff | -11.27341 | -53.96292 | 2025-11-14 12:59:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 046a8db3-db8f-3b30-a215-a3e114ade5ea | -15.34907 | -51.6447 | 2025-11-14 12:59:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 39fe18b4-963f-389a-bbb8-9fc3c94234c9 | -13.09731 | -53.47857 | 2025-11-14 12:59:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0cc1fe8c-4e11-360b-a8db-0ee71d9b74b5 | -15.36714 | -52.19703 | 2025-11-14 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 1890bbac-4f06-3989-8453-444be4cfa540 | -15.50689 | -52.38848 | 2025-11-14 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| d5e7bd2d-bc67-3a87-9ba6-6561a6ad7062 | -7.492 | -42.5452 | 2025-11-14 13:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| fe500166-ca8d-3bee-8d27-b7a64fb84fac | -5.6001 | -37.8156 | 2025-11-14 13:00:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 112.1 |
| c65218ac-2181-3c8f-ba35-c744310eb208 | -5.0156 | -44.3366 | 2025-11-14 13:00:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5f688517-c2a5-3e22-8c78-2bec875d86c6 | -7.4728 | -42.5709 | 2025-11-14 13:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 60ebb879-bfd5-341d-b45e-1b9ba23f10f6 | -7.454 | -42.5728 | 2025-11-14 13:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 137381a3-016e-34fa-b41c-a5cbda9f25ac | -3.4792 | -45.6413 | 2025-11-14 13:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 929fea92-d957-3353-8612-38968872e1e9 | -6.6691 | -43.75 | 2025-11-14 13:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 43789143-b064-33de-818b-a1125a6267dd | -4.2715 | -46.8488 | 2025-11-14 13:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1b880529-ebcf-3a6b-bbc9-23131142937a | -7.3373 | -42.8685 | 2025-11-14 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 681f1994-5b5b-3fe1-9aa3-6aa41d6eea95 | -6.0711 | -41.5821 | 2025-11-14 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| b233877e-f7f3-3d3d-87df-482bf374cfad | -7.4728 | -42.5709 | 2025-11-14 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 47bcb654-31a7-3817-8548-ae8a91ed1e56 | -7.829 | -44.2885 | 2025-11-14 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 4d9cef4e-9fb6-341c-bdfb-2ce81b3f0c0c | -7.492 | -42.5452 | 2025-11-14 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 5f7abc02-9bf6-3b56-9aa3-e3e904e4b089 | -6.1608 | -48.0289 | 2025-11-14 13:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| ed5d9ae2-4525-314b-a4e8-9a85622294ed | -7.8479 | -44.2865 | 2025-11-14 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 224.8 |
| a4932c55-7cf0-3280-9316-55d78334d4bb | -7.454 | -42.5728 | 2025-11-14 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 7f26c94b-7f7d-3d0f-8db0-9a7c5cdd3c83 | -3.4656 | -41.3283 | 2025-11-14 13:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| b46758e1-1e40-301b-a8c1-2520240b343f | -3.4654 | -41.3524 | 2025-11-14 13:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 5daff6ca-c4a3-3ef8-aea8-4d8de150b3fb | -7.4728 | -42.5709 | 2025-11-14 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 410e4807-97b9-30aa-854d-0cac8f33e02a | -7.454 | -42.5728 | 2025-11-14 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 44c30993-8cd9-304e-bfa5-8480b979d4c7 | -3.2174 | -42.2471 | 2025-11-14 13:20:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 47b74873-18d2-3227-aaa8-09a79e13112d | -2.0257 | -47.3239 | 2025-11-14 13:20:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 21e2ffee-bd61-3ffe-b2c9-0de7c857fa7a | -6.1608 | -48.0289 | 2025-11-14 13:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 565.4 |
| d0f5b4d5-791f-3316-921d-96509f620d0b | -7.8479 | -44.2865 | 2025-11-14 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| ce652c13-877b-3c0d-b4c9-5cfead0e8759 | -7.3373 | -42.8685 | 2025-11-14 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 6a91e238-4423-30db-bd3b-b67c00e72c57 | -7.492 | -42.5452 | 2025-11-14 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| f77ee447-1bea-37fa-86ba-d22e56b00ac8 | -3.4654 | -41.3524 | 2025-11-14 13:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 638cc022-dec8-32cf-975f-7e261a9db025 | -2.0257 | -47.3239 | 2025-11-14 13:30:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 37f4bd80-e7ba-3b40-8a09-0bf4f1337b63 | -8.6623 | -45.4834 | 2025-11-14 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| f53be342-ab97-3c4b-9425-ba84326eae4e | -6.5609 | -47.1034 | 2025-11-14 13:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 073e689c-01f3-375d-82a7-0c4f9c1289b5 | -3.2174 | -42.2471 | 2025-11-14 13:30:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 48ef19db-7bd5-3c92-b4c9-e4a7364dd2eb | -7.8479 | -44.2865 | 2025-11-14 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 2557357b-8925-387e-b6d3-863622cbe9f0 | -4.2715 | -46.8488 | 2025-11-14 13:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 259.1 |
| e9ddc45a-20ca-373f-b610-71c30a07a597 | -7.4728 | -42.5709 | 2025-11-14 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 117.2 |
| 07a9e480-5e45-313b-b1f0-a06d0305fe67 | -6.1608 | -48.0289 | 2025-11-14 13:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 193.4 |
| b4e7a8aa-ecca-33cc-9c76-b79386de26ec | -4.6311 | -43.2749 | 2025-11-14 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| e346134d-a460-3b5e-bace-d0164020fab9 | -7.454 | -42.5728 | 2025-11-14 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 150.2 |
| 0a0750d5-353c-304b-b279-4ad034ace6fc | -5.0156 | -44.3366 | 2025-11-14 13:30:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a0a625ed-b0f9-3f9e-ada7-07c73ce83087 | -4.2717 | -46.8268 | 2025-11-14 13:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 151.1 |
| c21ee704-846b-3fb4-a75f-9e7a8f337b8f | -7.492 | -42.5452 | 2025-11-14 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| cca03cc2-0817-35e8-8070-b9e15a3317ef | -4.6744 | -45.0409 | 2025-11-14 13:30:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 15f8af7a-e70f-3891-b6a0-d7736206745e | -7.3373 | -42.8685 | 2025-11-14 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 159f4751-544d-31a3-91f9-7e3c2f056a6d | -4.2717 | -46.8268 | 2025-11-14 13:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 111.3 |
| be2d6a8c-eb49-30fb-ac34-70977b97c519 | -4.6744 | -45.0409 | 2025-11-14 13:40:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |


[Clique aqui para ver as próximas entradas](README53.md)
