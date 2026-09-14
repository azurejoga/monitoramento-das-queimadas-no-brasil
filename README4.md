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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63a26a49-14ab-3bcf-9251-a4c4c24742e8 | -3.52796 | -59.06647 | 2026-09-14 00:43:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d9561a73-4f5c-3828-9714-4bbed30e99c1 | -5.72706 | -60.23066 | 2026-09-14 00:43:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f1910f0c-485f-3cee-bba3-255e16785b45 | -2.66376 | -57.51994 | 2026-09-14 00:43:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 06b881c6-30a1-347e-a7dd-69d958ada54d | -3.54399 | -54.00143 | 2026-09-14 00:43:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| ae946bce-105c-36ad-a081-19d6dd696b58 | -4.12936 | -60.68025 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| e0c0f45a-d494-39f8-8567-574a77bf7608 | -2.69824 | -57.5495 | 2026-09-14 00:43:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| b2bc346e-8e4b-39d0-a63f-ba2b5a532619 | -3.14479 | -60.63469 | 2026-09-14 00:43:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9904da17-e14f-3bb3-a88b-9e36426cc487 | -3.16666 | -61.18659 | 2026-09-14 00:43:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ffcd87bf-f5cf-322a-b37a-0021f07d59f4 | -4.13056 | -60.68903 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 97edeac0-3b08-37ee-a2ca-b331a65eaaed | -3.35126 | -59.39039 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 19832e72-47b2-34c3-9344-201488dabfcd | -3.16644 | -58.6499 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 2be646ed-8be4-3dd9-bbc0-3d99072c333c | -3.40845 | -58.21829 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cb27ed77-f329-37fa-96a1-fde64c8450c1 | -3.1651 | -58.64022 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 7cbd0234-431d-3c9a-8988-b666c828168f | -3.17586 | -61.12228 | 2026-09-14 00:43:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c67426b4-330c-3499-ba7f-1516d5534ef4 | -3.39105 | -59.40625 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e657bd8a-0780-396c-bf3f-eb28887ef8ab | -4.38899 | -55.20407 | 2026-09-14 00:43:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 22054db2-09c8-3ff6-adfc-f41a01ea2b39 | -2.66698 | -57.54249 | 2026-09-14 00:43:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| bd37c68a-1f92-3442-970d-99a8551d7091 | -3.40702 | -58.20818 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 1522b8cc-ffb3-3609-a74d-27c542d969b0 | -3.06324 | -59.17237 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1dcc09d7-20bb-338d-b6f2-54e4d5a24648 | -3.74001 | -61.74553 | 2026-09-14 00:43:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 66960c95-05ed-30a2-ba0d-a502962b67c7 | -5.08263 | -56.2537 | 2026-09-14 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 72a72d69-8d00-3f20-bc72-2c0b3e821463 | -5.12165 | -55.96303 | 2026-09-14 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 75267306-42c3-3be8-9ab0-66b1353dd5a1 | -3.89391 | -60.58848 | 2026-09-14 00:43:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4d709c98-65b4-3f71-9acf-12f35bea3752 | -3.39232 | -59.41531 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| bacc9679-c8f4-3879-b135-b4ec85fb4351 | -2.99358 | -60.81061 | 2026-09-14 00:43:00 | TERRA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d942b56f-3d76-3012-b5f4-71e7b4e50d32 | -3.80953 | -58.90419 | 2026-09-14 00:43:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e30b467a-e2e4-37aa-a1cb-3538b28b7f72 | -3.37867 | -50.39437 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a3fe1b59-3f29-3f65-ac29-f8ce1816afec | -5.07216 | -56.25518 | 2026-09-14 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8d15a50b-05fb-3627-aa13-530bfa2889a6 | -3.03559 | -59.17272 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5f1a8f40-41f3-30bf-92a3-a21bbf6d4adf | -3.17428 | -61.17652 | 2026-09-14 00:43:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ef17c5ed-07b9-3ade-990d-d027fee0324e | -3.35748 | -59.82827 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2f2c8111-358c-3bc0-a00d-ecd4fcce9d42 | -2.87681 | -50.41505 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 99c2af7e-75b9-30c4-ba89-7410df693e0b | -3.72251 | -58.87458 | 2026-09-14 00:43:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| e00fbc59-e2f8-3c21-8771-d112d0b59ebb | -3.73227 | -61.75594 | 2026-09-14 00:43:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9c3a62cc-82ca-3603-a219-eb79e98ec261 | -2.70766 | -57.61662 | 2026-09-14 00:43:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 83332a35-f56c-3ca0-bfd3-3ad84c68e98d | -2.91126 | -50.40982 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 189.4 |
| 0fe3af3f-e928-3869-bcc0-a834f836a7a3 | -3.31044 | -59.35907 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0b38032e-5a57-34a9-b28c-868d6388f442 | -2.69666 | -57.53824 | 2026-09-14 00:43:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| bb866f09-cfe1-3e9a-b527-9895d0066257 | -3.35624 | -59.8194 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2f6bdf29-5357-39d2-8d64-e4b12fe69781 | -2.89231 | -50.41766 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 177.6 |
| 0ef7fe0e-55b3-33b4-baaa-b48827bce8b9 | -5.13234 | -55.96154 | 2026-09-14 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 3da88ec7-0029-31cc-9af0-cbf5ead5971b | -3.41499 | -58.19673 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 84f7da9f-07f4-3ca0-b67f-c86c36f6ba44 | 2.5801 | -60.29797 | 2026-09-14 00:45:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cba3b184-a410-3784-8797-8cf034d8d838 | 2.31854 | -60.92342 | 2026-09-14 00:45:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 60f238ae-0012-377f-bbd7-78f3ea0f0182 | 2.57882 | -60.30724 | 2026-09-14 00:45:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b922d20a-4b07-3b3d-8e67-9be953607c80 | 4.2803 | -60.94564 | 2026-09-14 00:45:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 808037f3-60e7-3d41-8833-87d93a0405c3 | -13.5598 | -49.912 | 2026-09-14 00:50:00 | GOES-19 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6b0aa780-2308-334d-8866-7478c1c2e284 | -5.1255 | -55.955 | 2026-09-14 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| aad1d495-9419-37ac-a23a-436f3bcf6323 | -4.115 | -60.6886 | 2026-09-14 00:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| d15f58c3-e3f3-30a9-aa68-3be7e1832d5c | -7.1048 | -41.7971 | 2026-09-14 00:50:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 7062cb48-4a59-32f0-9cec-621a00303317 | -14.1861 | -47.3844 | 2026-09-14 00:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6ca13da1-24de-3a42-86eb-b35dc4379635 | -15.8243 | -42.3718 | 2026-09-14 00:50:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 9c361080-fd96-3940-b215-48ffd0842723 | -9.4325 | -50.1299 | 2026-09-14 00:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 234.9 |
| c6833b81-585c-3f57-9f57-f66025150796 | -3.4089 | -58.2142 | 2026-09-14 00:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 31585ede-2328-38bf-9511-8c40d3072ad0 | -4.1333 | -60.6882 | 2026-09-14 00:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| ae748f87-00f6-3dac-87ea-9fa821c8bba1 | -9.4328 | -50.1086 | 2026-09-14 00:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 3d70c431-f1a0-30cd-97de-ad87e69fe9d5 | -12.4901 | -41.4012 | 2026-09-14 00:50:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 4eb5ba7a-632f-3651-91c1-94acfbfd8295 | -6.2831 | -59.9394 | 2026-09-14 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 548f4bd3-b720-3904-8e35-43034745ed79 | -5.2883 | -45.2744 | 2026-09-14 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6b691699-091c-3762-84e0-7a2881c3a22b | -6.8446 | -55.5611 | 2026-09-14 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c388f46f-d92d-32e3-86dd-da4cc6c7fbc0 | -6.3015 | -59.9387 | 2026-09-14 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9d73d0fa-4a3d-3d91-a476-86db901588d1 | -6.5837 | -58.8498 | 2026-09-14 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| f8b94ef3-9f11-3c57-89c5-53fa7cb1e08c | -6.1111 | -57.6645 | 2026-09-14 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f5b57c6a-06df-3505-960e-b701caddea14 | -9.4322 | -50.1513 | 2026-09-14 00:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 43c20271-c31a-3ac6-9a15-ca9e6893aabc | -13.5602 | -49.8902 | 2026-09-14 00:50:00 | GOES-19 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| bfa3d2e8-2a6e-3935-8b1c-a862e15fe945 | -4.1334 | -60.6692 | 2026-09-14 00:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 162ba35a-1f4e-3a9b-a1f7-5bac911a78f0 | -9.4132 | -50.1744 | 2026-09-14 00:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ef4e1713-afa9-3cd8-b6ed-cf2caae84d44 | -6.1109 | -57.684 | 2026-09-14 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| c3e89162-6488-37d8-bc6a-42cd3e95a335 | -11.2265 | -46.4215 | 2026-09-14 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| ec771603-bd0f-3f3c-83a4-06e9df87addb | -4.115 | -60.6886 | 2026-09-14 01:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| fecbcaa7-eceb-36a3-aebd-9d0daa6226d0 | -4.1151 | -60.6696 | 2026-09-14 01:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 74af9a51-3480-3dc4-b63f-8ed44c534325 | -4.1334 | -60.6692 | 2026-09-14 01:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 9874ddb2-2767-33da-9fb8-c1886a67afc4 | -6.2831 | -59.9394 | 2026-09-14 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c4f47a79-36f8-3518-9126-ef94bb1112b9 | -13.5598 | -49.912 | 2026-09-14 01:00:00 | GOES-19 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 50d22fb0-b1dc-3806-a8b0-d54f2f1488d9 | -4.1333 | -60.6882 | 2026-09-14 01:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| bba83727-05f8-3bd2-a82b-c294f3b10372 | -15.8249 | -42.3471 | 2026-09-14 01:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| ce80813b-4b9b-3678-81fb-6435f3042bf4 | -6.1111 | -57.6645 | 2026-09-14 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| aa17936c-bb8d-3ec5-bcc8-cdc99c5690d4 | -5.1255 | -55.955 | 2026-09-14 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 89a2b200-1c2d-3d27-9d89-6c84b9e082a8 | -9.4513 | -50.1282 | 2026-09-14 01:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e4cfc7e0-f7b7-36ac-b79f-8c3f4804780f | -15.8243 | -42.3718 | 2026-09-14 01:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 556382b1-99a0-3f06-a69c-5eb7d23cf8e2 | -6.3015 | -59.9387 | 2026-09-14 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| fc5fe214-c5f6-39e8-b636-605efdd79c41 | -9.4328 | -50.1086 | 2026-09-14 01:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d651c8a6-7294-324a-8151-892e62565126 | -6.5837 | -58.8498 | 2026-09-14 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| bfccfa7a-8cac-3ea2-8474-f2c55e3a541b | -4.8562 | -48.3667 | 2026-09-14 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 43045718-fa41-37bc-b151-ee32fa0539a2 | -6.1109 | -57.684 | 2026-09-14 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| eee355b6-89bf-32ae-9031-f9d6898b486d | -9.4325 | -50.1299 | 2026-09-14 01:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 231.3 |
| 26be58ce-661d-3912-bbc6-bd708e88b5ea | -4.1151 | -60.6696 | 2026-09-14 01:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 9c92b062-f31b-3838-ada7-308799925620 | -6.2831 | -59.9394 | 2026-09-14 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| fbcc73a5-605f-3ade-91ee-63492b016013 | -4.1333 | -60.6882 | 2026-09-14 01:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 89ad2fff-d9cd-3983-9015-6ab5a8fdfb61 | -6.3015 | -59.9387 | 2026-09-14 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f941e772-231a-30e5-80bf-74b8aea96f10 | -5.1255 | -55.955 | 2026-09-14 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| e70a9188-c11f-31f4-90ae-22be259742d2 | -3.728 | -61.7555 | 2026-09-14 01:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 02451e03-55e8-372d-a00f-1043a18dbd75 | -4.1334 | -60.6692 | 2026-09-14 01:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8c2a96ae-7b0c-3805-8d19-870a9b8609a6 | -6.5837 | -58.8498 | 2026-09-14 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 5aea648e-88b6-3fac-b176-78a0a5afbb1d | -9.4328 | -50.1086 | 2026-09-14 01:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| cd6f49aa-1e49-3b40-86d5-3a8cf4aa4fbe | -15.8243 | -42.3718 | 2026-09-14 01:10:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 263a12ff-a0f0-3d63-9499-6b51b0647b62 | -4.8563 | -48.3451 | 2026-09-14 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| e50325f6-9cc4-3b78-acc1-f32b7b31488c | -4.115 | -60.6886 | 2026-09-14 01:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 0e933506-dfc3-3081-81b1-e1c99a6b252a | -6.6927 | -59.1352 | 2026-09-14 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| dfdad7f8-9a5a-33fa-9efa-7d6df2cd396f | -4.8562 | -48.3667 | 2026-09-14 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |


[Clique aqui para ver as próximas entradas](README5.md)
