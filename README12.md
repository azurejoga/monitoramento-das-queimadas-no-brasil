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
| 918ca41c-7c32-3d47-87db-8d37694b3a6f | -7.61842 | -70.22388 | 2026-09-22 01:00:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1aa8466d-945b-3f28-9211-78e4f043996d | -6.46402 | -59.98799 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 2d8973e7-ec31-3f7f-b7d6-7f16e2ea7f5f | -6.16012 | -57.7166 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f23bbb4c-ee65-3af7-962d-a5b1d00a13d9 | -6.42915 | -59.97879 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| dce0b4f2-cce5-3916-8827-8ef6c14c54cd | -6.36428 | -58.29432 | 2026-09-22 01:00:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 568a5250-90a0-3298-99e4-36532d6a6a35 | -6.62732 | -59.92264 | 2026-09-22 01:00:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 543c58fe-25f3-31a5-b18a-a415c340646f | -5.81173 | -57.75227 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 3e3097a5-119a-3e20-8de3-e2a99016a9e1 | -4.41981 | -55.51532 | 2026-09-22 01:00:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 38bc057c-4728-38a4-b17f-6cada21a19f7 | -7.6957 | -61.5348 | 2026-09-22 01:00:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d61111a5-290f-3ecb-85c2-61f4d0838eb2 | -6.45101 | -59.97561 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2194b25a-4e6f-3fac-86fa-705f10d42213 | -6.11389 | -57.75212 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 54b1cf40-c0ae-3460-97ec-45e821e927a1 | -7.29264 | -59.52254 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1f639a2e-07fa-376a-a322-d7de8d0f0a8b | -6.62941 | -59.93659 | 2026-09-22 01:00:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 87b29a95-1d6b-31fa-9ff9-8ee41ccce92c | -6.1041 | -57.7037 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| c45dc842-0041-3baa-9c1a-d9c39a71f56f | -6.04462 | -57.82733 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 834c9eca-d662-3347-85ff-39ce5f08cd9c | -6.12713 | -57.76531 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 51517dde-a618-31d7-9a42-e2a2df2587c2 | -6.78178 | -63.13877 | 2026-09-22 01:00:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a67d9c8a-0b03-3190-8d82-15e3fb277d78 | -6.45312 | -59.9897 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| aa4e4311-d092-3830-b133-8b0a1580841d | -6.06409 | -57.86709 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| a9db965c-6df2-36f9-b491-de22885adc70 | -7.49553 | -63.89276 | 2026-09-22 01:00:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 49aa74da-bb8d-365c-bd3d-8ebbdcdfbb0b | -5.80855 | -57.73097 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 8b969dc0-06a0-374f-af01-ff4655e6d6ba | -5.80796 | -57.74702 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4d3eff3d-119e-37af-9a90-51da1be7fcf1 | -6.30536 | -60.00967 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e66ade3e-856f-3342-8bfa-0448464c1095 | -7.08708 | -61.08746 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 37da8085-c437-3701-8173-b8f00f42b65a | -6.75798 | -59.1176 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d45a6a6e-ebe6-3b8e-89cd-61a8a15b96c4 | -5.76534 | -56.5215 | 2026-09-22 01:00:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 3bee0b1e-c0bc-33e6-ae1a-f3ad628702c7 | -6.34098 | -59.94688 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 63cd8215-f5ea-37ba-956b-77eb322582d2 | -6.70094 | -59.96822 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 011395df-15c6-30cd-931e-7e57efcc71ef | -7.29053 | -59.51445 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0623d9eb-5070-3039-b92a-c7732a7e3709 | -6.64918 | -59.9193 | 2026-09-22 01:00:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 264.3 |
| 81debdf5-284c-39d4-90b9-95cbbcb994c4 | -6.19898 | -57.79665 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 383819b4-7d34-39da-a50b-83ef089b070c | -4.5018 | -59.55233 | 2026-09-22 01:00:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 85952610-396a-313c-aa7a-e256386d5173 | -6.46608 | -60.00181 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 56aa24e7-1fd0-37db-aed2-8be9f275e18a | -8.79251 | -69.02045 | 2026-09-22 01:00:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 1a0ce191-5d3b-31c2-bcd6-2a56621413ff | -5.82496 | -57.75022 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b31ed679-a046-32c9-a951-8cc3e9ab8bef | -7.72763 | -61.25851 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 107a532a-5157-3295-adb7-f7ccfb35b0d8 | -6.34658 | -59.96907 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2aa0f454-1021-3dce-94a6-2344750fc62a | -6.34448 | -59.95513 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| c454430b-78f0-3d1d-907c-350a7d87f2cb | -5.45236 | -60.15009 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2cfd618a-cc4e-3f81-a21a-cf158f6fe1a7 | -6.91597 | -59.6262 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f6360d07-1238-304d-889d-961d6e4f9345 | -5.93196 | -59.97504 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 08b778c0-85e2-3a79-951c-859c4719d7fe | -6.86446 | -59.90303 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| afd9ed4b-5b8e-36eb-81a3-597038ebc3f4 | -6.7805 | -63.12957 | 2026-09-22 01:00:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf1cde12-99a0-35da-a8b3-30467885c782 | -8.67996 | -70.03557 | 2026-09-22 01:00:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 43117846-2507-37d7-9257-339e5fe9d274 | -6.30805 | -59.95169 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 807e033e-2de4-3ec9-8b62-16e26c6c0aec | -6.86651 | -59.91713 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ed506892-ac85-393f-bf8f-f37b4f6f814a | -4.26659 | -55.43777 | 2026-09-22 01:00:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 786b766d-c9c3-361e-b6c1-fa2431824c2e | -6.353 | -58.28947 | 2026-09-22 01:00:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 7d23dbfb-e273-3cbe-a52b-a7521636d139 | -6.69894 | -59.95436 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 3a27a28d-cc71-3bc6-bf22-8728eebc416c | -6.12546 | -59.96254 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 28f014f3-2338-3e77-a81b-600b4b682d38 | -8.79443 | -69.03604 | 2026-09-22 01:00:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 54695ded-2429-34f3-a7c2-aa782ded703d | -6.7351 | -59.41565 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2141c382-413d-3f87-b803-43eb4366be90 | -6.42524 | -59.9717 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d2dd7bbe-c995-3fd9-af0e-f52f7817402e | -6.61428 | -59.91031 | 2026-09-22 01:00:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 3d1d7ffe-4a90-35f6-9ee6-9f8ce803918e | -8.783 | -68.85066 | 2026-09-22 01:00:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c0143cfe-ba4d-3ab7-8ea4-ff46785b1d62 | -6.63824 | -59.92092 | 2026-09-22 01:00:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 3f68f3df-d8c0-3694-ace5-554c6d903af9 | -6.19587 | -57.77572 | 2026-09-22 01:00:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| caa5dbdd-4511-3820-a5fa-408aaa153318 | -6.71012 | -59.01468 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 19ebcb8a-59b3-3a38-b1b9-e318f8495695 | -6.65124 | -59.93322 | 2026-09-22 01:00:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ba1da32d-3d38-313f-ada4-90dcc0b86900 | -4.50414 | -59.56847 | 2026-09-22 01:00:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 12ed2f61-8170-34cc-af19-9d5ea4035a62 | -6.88024 | -59.85781 | 2026-09-22 01:00:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c67d4c69-fbdb-357b-a9f8-4c51b93c73c0 | -3.60417 | -60.57951 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4985c431-280b-3685-ba73-90171839d32a | -3.14118 | -61.40029 | 2026-09-22 01:02:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dc067a25-1f4e-353d-9163-49efa840e597 | -1.93452 | -56.5994 | 2026-09-22 01:02:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5c962db3-096f-303d-a3e4-466af8c61149 | 0.77876 | -59.19617 | 2026-09-22 01:02:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 924a1759-f2d3-3fb3-a2ed-47ab6f313967 | 1.77376 | -60.24548 | 2026-09-22 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 435f4222-c51c-3d28-bfd7-c296e0d67e70 | -3.04888 | -61.27293 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2e7a18f9-05d8-3e1a-ade3-98257be1370e | -3.34015 | -61.3023 | 2026-09-22 01:02:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5d5baff7-33fa-3a04-a6e9-dd9507414b31 | -3.04706 | -61.26029 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 1dd5a0b1-db3a-3f9a-b367-92a5675309d9 | -3.19162 | -60.43792 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 73b8539d-2642-38cf-87f6-b49b95af7104 | -3.39645 | -59.53568 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 1c535d03-b667-3d6e-abf1-d9b272a4d4c4 | -3.89295 | -60.59017 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 101a933b-be94-34e8-bf8b-cecbfd769f84 | -3.3983 | -61.0671 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 67b2bf8f-d23c-3aaa-8728-0ec4d192114e | -3.06297 | -61.29674 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a4589f35-1e32-3681-8eba-7a964e05dffb | -3.34046 | -59.86864 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| c9db0528-2ca3-3130-b9b6-2498764fe39f | -3.2832 | -57.86975 | 2026-09-22 01:02:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 8eec6c89-87a8-3ed5-be22-e52889a8c822 | -3.79105 | -60.74991 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8cb7e56e-dc15-3c09-b35f-4734c9db4599 | -3.05934 | -61.27146 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2d1c0c10-eab8-3570-a0e7-179a63613e85 | -2.93462 | -57.80247 | 2026-09-22 01:02:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 0deca04c-0c23-344b-8954-81271e07c927 | 1.08254 | -60.68484 | 2026-09-22 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5e7216fc-4251-38fa-aa0e-3ad6aeee0354 | 0.78906 | -59.21923 | 2026-09-22 01:02:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 59a112cd-3c6e-3a73-b8e0-aadbd0c43745 | 1.53506 | -55.89576 | 2026-09-22 01:02:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1fc5059b-c343-3cc6-bfc4-b2116178df18 | -3.77831 | -60.73801 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| abba0d85-6610-3b7f-8c70-b92a9dd88747 | -3.29044 | -57.87424 | 2026-09-22 01:02:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ecd295e5-63f4-3f1a-b938-c647e6a26af8 | -3.22281 | -61.05176 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 553bafce-60c0-3e1f-87fc-dfb25bec3225 | -3.19178 | -60.43143 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e3364914-0110-3d2d-8674-f50fa3279804 | -2.79169 | -59.88722 | 2026-09-22 01:02:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 3e1a1707-18fd-3a57-88f5-cf541233ada8 | -2.87368 | -57.81721 | 2026-09-22 01:02:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 073f3770-4212-36c8-9029-32831b7d4b3b | -3.29691 | -57.86767 | 2026-09-22 01:02:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 3576a840-2009-36dc-9dc5-c64bb73744d0 | -2.41502 | -58.29077 | 2026-09-22 01:02:00 | TERRA_M-M | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| bf939b67-ac0f-3ea2-9e8e-e121e589a94c | 0.79196 | -59.1981 | 2026-09-22 01:02:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 227c22a3-70bc-361d-9d22-93777386529c | -3.48341 | -59.58504 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 588577c5-5914-3e31-997b-57b43f17c870 | -3.39401 | -59.51869 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 49a476b4-5965-39f8-bde7-b53f24cfdb99 | -2.87024 | -57.7934 | 2026-09-22 01:02:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 153f33c9-d019-37df-8361-d182dea9b69b | -2.40366 | -58.27514 | 2026-09-22 01:02:00 | TERRA_M-M | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6629186a-3b46-38a7-9fa5-ba4a637a732f | -2.95707 | -57.71907 | 2026-09-22 01:02:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 82da2106-5ece-3283-9669-f7acee7ffab6 | -3.06116 | -61.28409 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 38f9804c-5d3b-3ab7-8f01-83e32b74d577 | 0.1782 | -60.49759 | 2026-09-22 01:02:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 6534c5d2-3ebb-3aff-bd6b-155dcb06ef8d | -3.69542 | -60.57471 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 00ac386a-aa7a-326f-85a8-24baac7dfd21 | -3.10518 | -60.7174 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |


[Clique aqui para ver as próximas entradas](README13.md)
