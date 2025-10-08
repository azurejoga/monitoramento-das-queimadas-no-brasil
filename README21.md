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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a50aa097-6292-34b5-88d2-12c20373900b | -14.94385 | -46.79213 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a606ce0e-0532-351d-8c3c-c65a137ad4f8 | -9.54239 | -47.76817 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66ef1faf-ea6a-3c31-8a77-85b57b5a33f6 | -12.98571 | -46.77702 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47bb20d4-fd27-3a80-8a0d-87f7bd3e7397 | -8.53427 | -46.23105 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b91b7df9-e4d7-36b0-89ac-13fa4628ad7f | -11.67344 | -50.96727 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 030f7c60-effc-3a19-b025-43855ed2da5f | -12.39209 | -51.13844 | 2025-10-08 03:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68a4c2a8-f4fe-32a8-8a64-3d9c89afe6ff | -14.38691 | -46.02131 | 2025-10-08 03:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e906969e-3058-307d-8be4-97e798a1b102 | -8.55061 | -46.22998 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00a36a9c-183c-3a1d-9be3-f2bc4dde54f1 | -10.71757 | -44.80109 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff7637b0-8d2b-3c25-974b-db1efa5173a2 | -11.34174 | -44.87924 | 2025-10-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 18f21261-0bc2-36f2-a6f7-30ba7164ca6d | -9.09371 | -47.96064 | 2025-10-08 03:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2e8b1fc-2941-37fd-bad5-58b940c82baf | -3.94668 | -39.02103 | 2025-10-08 03:49:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8a4e6340-aed4-3993-b499-dcfbc7c96a55 | -11.98886 | -46.77269 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1368d086-3f3e-3709-9075-8b85e4942057 | -9.77569 | -48.28599 | 2025-10-08 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a34a2d7c-058c-3361-9ceb-f1b4bb873aa4 | -11.77349 | -45.13441 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 942465dd-4303-3cfc-98a0-1119e694a47a | -8.23365 | -44.18191 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| dcdd0479-e03c-3f02-b9c7-dbc7f461c727 | -3.44147 | -45.59488 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87bcb2b1-67c3-3cf5-b8b4-985c522f8d37 | -11.47075 | -43.4857 | 2025-10-08 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34a1e6a7-254e-37d4-841b-1632730a56a0 | -9.98168 | -48.78467 | 2025-10-08 03:49:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4b553de-15a1-38e0-9fce-048776c72dfe | -12.94666 | -46.8466 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4fbb1401-5522-34bc-a73f-99b9fc2cd33f | -10.68079 | -47.55077 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53159eb7-7750-3a0d-a8d6-a689beef7236 | -8.46673 | -47.2093 | 2025-10-08 03:49:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30c618e1-3439-374d-826a-edc1ef4e8a3c | -14.19553 | -43.66756 | 2025-10-08 03:49:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14ffdc25-426e-3225-9e64-0fee2b814bdd | -13.2882 | -48.48932 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27308a6e-964e-3836-b805-2c1f0bef9196 | -3.85822 | -38.55651 | 2025-10-08 03:49:00 | NOAA-21 | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f54d7281-5f87-3820-bae3-697bc7ccfff7 | -13.25244 | -46.47067 | 2025-10-08 03:49:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc9f26d1-a03d-3b2b-9cd6-e223101db0a5 | -12.01692 | -45.19997 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49da4467-57bc-3ef0-8767-97fc59ad4400 | -9.76088 | -47.69153 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7e98f21-5cb3-3165-94f3-cb1dcf1c7f20 | -8.53955 | -46.23162 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0d1c1e6-e2b0-3194-b18b-1d7f65b0751c | -10.42415 | -48.09572 | 2025-10-08 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6dab0a3c-15f8-3383-b5f0-519108881113 | -13.00945 | -46.78816 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 711c6ab2-c1b1-30a8-a53b-e0fa2111f621 | -14.94283 | -46.79757 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d3e6bb2-1e6d-3a46-af92-8ae132f0a3b7 | -11.87496 | -44.9385 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94230472-7ec7-3b00-b274-be0c851ef413 | -8.47447 | -46.29024 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccc8ff94-4196-3405-a4ec-e97d14a0bf53 | -15.24601 | -46.35622 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be24adce-2147-321d-a584-4f983ed62392 | -8.12354 | -44.77148 | 2025-10-08 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a3b8d4ae-520c-3405-8327-05f26a71f003 | -8.52252 | -46.23256 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8de80a97-a257-3f6e-a205-3a4d7f11a999 | -11.79635 | -45.11296 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fc607c8-7044-3011-b533-dd2ca8d0a8de | -10.47509 | -49.38608 | 2025-10-08 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ab2b176-a61c-32d0-8c04-047ded72e4fe | -14.92824 | -46.78931 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 39f57e1a-b806-3268-a582-948fa76c6d5c | -12.00272 | -46.77205 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 633e3fea-a172-316a-9371-f25cca3d387c | -8.52194 | -46.23582 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78e80a20-fc17-3e57-8e72-1557f76614cf | -11.72453 | -50.94212 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 0bf5573e-c9f2-3236-84b9-56265e10d822 | -9.39571 | -45.95706 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e36fbd92-f1af-38cb-87e2-9e5ba9d869c6 | -13.22648 | -47.18811 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3045201-ceb9-355f-95a1-853e0ea58ace | -14.38785 | -46.01627 | 2025-10-08 03:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5e3a370e-871c-3e35-997f-603f30f65855 | -12.9411 | -46.84847 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 74a7d1b8-6890-3900-8de9-a3e861c75dc7 | -13.28701 | -48.49043 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 212adf88-6c80-3237-87af-842851c9cc95 | -13.0722 | -48.01375 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 717ed5c0-9849-32f1-9a35-337bb6ddb100 | -15.07506 | -46.62256 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 486f6101-d205-3e32-8ef5-0fad82c32ce0 | -13.28365 | -48.47855 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c39b39e-56fd-32fd-9421-b301af3b2d18 | -11.70351 | -50.95508 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 390a8a90-69a3-34a0-8b32-ff624e2774c7 | -13.23118 | -47.19116 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8cb9a8a9-9ad6-324e-ac05-39e894b96a24 | -12.24265 | -43.78334 | 2025-10-08 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce3d21d9-be99-3eb5-9cd9-dc744de3291a | -11.77618 | -45.14543 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 845cd7c3-55d5-3105-816c-48cc11f00dc6 | -13.3713 | -47.55626 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d4ba2608-2115-3274-b37a-8263a3ae3348 | -11.9996 | -46.77158 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c7b3f098-ccc1-3284-9d27-3753897b8b0a | -11.72571 | -50.94744 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| bab6dfa2-1569-3440-888f-30cb068ef52e | -11.73651 | -50.9507 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 5881b9eb-875e-3ae9-b6ec-1f88d373b8a9 | -8.21947 | -44.1551 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d53b149a-1dff-3401-a4ae-681c3883e753 | -13.34329 | -47.55983 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a692b42a-3994-337c-a77a-02a46c83438a | -11.7842 | -38.43034 | 2025-10-08 03:49:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a83f6e97-0459-3c1e-9ee5-3a6564262061 | -14.92301 | -46.7965 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 15021093-8cb3-326d-90fa-74f64043b276 | -13.80438 | -45.79196 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 84c27818-db0b-3000-8a6c-843f1d72a442 | -9.08719 | -47.96351 | 2025-10-08 03:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02f04368-7900-3ab6-8cf5-534836ef2bc4 | -13.73687 | -45.72397 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9fb85fd-d21b-3ae0-b00a-b2b8fa8fd0d0 | -14.95996 | -46.83219 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5bac5f2-1034-38f4-a896-5beb1dfd3ca9 | -14.38596 | -46.02638 | 2025-10-08 03:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a493f245-cbf5-3d07-9c87-1a32eeab6d0b | -13.73777 | -45.71922 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5288cde9-0db3-3649-9cc8-5a00a1b0cf82 | -13.07032 | -47.93612 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ca398de9-1b33-3774-9e2e-3ebbc224e363 | -10.90632 | -47.14 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a02d89c4-3c3b-3eb0-93ad-ec0589e78009 | -14.70541 | -46.01422 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| be003f65-87fe-3cfc-a9c9-a58b501bdef4 | -12.02432 | -45.21123 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| beeab0b7-25db-32ce-bb86-cd407a45471c | -3.98296 | -40.39753 | 2025-10-08 03:49:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c219f499-02f5-3469-af7b-7f62b2ed4a43 | -8.19188 | -43.34423 | 2025-10-08 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| bfe15144-a71d-38ad-8fcd-0c952d4aadc8 | -11.85863 | -44.92581 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fc250d6-ed2a-3e35-a358-5ed7666d2967 | -9.19142 | -47.79715 | 2025-10-08 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86611b40-2966-351a-99b3-411bca0ce421 | -13.28276 | -47.56427 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba3756fa-bf74-3e16-b749-1cf62f3fe312 | -15.3168 | -46.1632 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7cd86147-75f1-3120-b8f5-60b73887b830 | -3.43994 | -45.5946 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58a56856-7c25-3740-8b90-6f4b67acb2a7 | -11.99822 | -46.76808 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fbe005ac-f67d-39da-859a-9317c9b7eccb | -11.87646 | -45.74603 | 2025-10-08 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1de49dd4-39df-39aa-a395-eac19a4b7535 | -11.79382 | -45.04998 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df309fa1-c291-3dff-acc7-05f630bd6be0 | -13.36508 | -47.55922 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e951035-f7f2-38a1-96b1-efb0faac9d6f | -13.79845 | -45.80257 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 033e674f-1459-3426-8f6f-fc7ea34a9dad | -11.68415 | -46.3811 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 082dc3dc-8eb7-328d-8a4c-19202017397d | -13.4652 | -50.40925 | 2025-10-08 03:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dffb504d-948a-346b-8920-9b8d3e686875 | -8.9379 | -46.59918 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63bac044-ed2b-387b-a860-94e3fccb91de | -11.72875 | -50.96651 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 42f9f606-614c-35c1-b336-97109524af02 | -11.71194 | -50.98145 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f356fad8-9d28-3d67-a8a7-8144e078c0da | -14.94706 | -46.79553 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74efcfb0-12b0-3458-8e09-f96f251bce22 | -13.78655 | -45.81524 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ae88aa2-7233-3dc4-9145-5de2f1790f0a | -11.70446 | -46.35513 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a929ad2d-f3b5-32ca-9ce1-17ca203ed403 | -14.70698 | -46.08199 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd2e9e10-1b76-33a8-b3ac-a5fb5f93ab2b | -14.36387 | -47.73178 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1faf4da5-cee1-30ec-b379-f28c99ee29f7 | -8.51859 | -46.28522 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 331b1a9b-8811-3610-bcb4-30c4c8e7a5b2 | -3.28791 | -42.6236 | 2025-10-08 03:49:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98a56360-28dd-39d6-9a6f-914bd750d645 | -8.7856 | -48.00379 | 2025-10-08 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f054e77-12ee-3441-b1a9-c655535ab3cd | -15.08581 | -46.61814 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b30cceb9-55ff-318b-a204-05337eb379a2 | -13.22427 | -47.1859 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README22.md)
