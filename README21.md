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
| fd59add1-3607-359a-9cc8-a3444443caa6 | -3.0582 | -53.2192 | 2024-11-24 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e5d141be-bd24-3f73-a564-60c6db7e3bc1 | -4.0848 | -50.36 | 2024-11-24 01:20:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6b638d93-08dd-3503-88b5-8731a1d2fbac | -3.2929 | -45.7161 | 2024-11-24 01:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7f68731d-12db-30e5-a6c2-b0e4fd8a34a7 | -0.8723 | -52.7686 | 2024-11-24 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 125f1698-d940-3096-97bd-259bda36253a | -5.9557 | -48.0425 | 2024-11-24 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| e2c01628-c4e1-351f-8fbe-ca1be1bfec73 | -1.8238 | -46.6486 | 2024-11-24 01:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 172d9392-0537-3d39-a2ce-42e135243acc | -1.8239 | -46.6265 | 2024-11-24 01:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 8148e2f4-7066-3e73-9146-c252972debcc | -5.9556 | -48.0642 | 2024-11-24 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e8390bc5-b837-3e57-8b33-8de037dcb3bf | -3.1068 | -45.7903 | 2024-11-24 01:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d222445d-1043-37da-b727-5707bfb43936 | -3.8417 | -44.0594 | 2024-11-24 01:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 37b967d0-06c9-326a-a9d3-c34ecf4a3c15 | -2.9229 | -45.3712 | 2024-11-24 01:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 90194157-f0da-364c-ac6f-a237ee4bfac8 | -2.7149 | -46.2713 | 2024-11-24 01:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 832e5f74-93a7-3998-8bf2-d2b26bbce85b | -0.8907 | -52.7685 | 2024-11-24 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 5c264a40-b0bf-3937-ab87-1779f3b6dd58 | -1.3666 | -53.8362 | 2024-11-24 01:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 7007bab0-7012-3cda-9d57-3c075f6eb1ea | -3.2928 | -45.7384 | 2024-11-24 01:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| c34d8781-17b2-3c18-b621-5d5057672ccd | -3.5158 | -53.8333 | 2024-11-24 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7f6b924f-2606-3bb5-a7e8-282cab547c36 | -3.0355 | -49.4476 | 2024-11-24 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 8bf256a2-a5a8-3621-82a7-0342b2c5a5b7 | -4.2419 | -48.7193 | 2024-11-24 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 2bbd5b3e-93e7-3e51-b815-489ec170aca7 | -2.4456 | -49.0816 | 2024-11-24 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ab2b8ba8-cf0d-30d3-8e19-bb131192cb59 | -1.366 | -53.820202 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efecdd74-8b0f-36be-a74e-b5de9ca3197c | -3.2556 | -54.202301 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7028ec69-377d-397d-b2df-0e41733b87a5 | -3.1791 | -54.313999 | 2024-11-24 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87b0b28b-402a-3b15-a108-0daa782a8218 | -3.5168 | -53.826599 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66a653ba-0391-339a-ab6b-f24c380c50d0 | -20.323799 | -48.8074 | 2024-11-24 01:22:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 49804747-d9e2-3dcb-b263-d9b68a1caf44 | -2.5855 | -51.8978 | 2024-11-24 01:22:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76cebe3a-8f69-365f-b607-5e05842ed706 | -1.5234 | -54.186001 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ccef89e-767b-3313-932e-d84500591fef | -0.2481 | -51.6231 | 2024-11-24 01:22:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0509ced9-93bd-379e-9e69-1c8febd2dcf7 | -4.2479 | -48.712399 | 2024-11-24 01:22:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c585b65-1152-3a01-8361-c2e51a603b6e | -0.8918 | -52.7575 | 2024-11-24 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b31f1d69-d37c-35d9-bba6-9005948b5a4e | -1.621 | -55.132801 | 2024-11-24 01:22:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 961de764-9fcb-37e3-a3a4-45b4a9fac451 | -3.2441 | -54.240398 | 2024-11-24 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55e26084-b6d9-35ea-8309-6867921a9ea3 | -3.2316 | -54.231499 | 2024-11-24 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9421e18b-1fa8-3807-96dc-f09a16d01cdb | -2.4533 | -49.091801 | 2024-11-24 01:22:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6524982-3184-3b19-aa90-c6752f5d5b12 | -3.0885 | -54.541698 | 2024-11-24 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f055f2a-d2f4-31de-9da0-e89cae18d1f0 | -2.1851 | -53.632301 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12cfb37b-791b-31cf-b3f8-f51f9d804af0 | -0.8409 | -52.5397 | 2024-11-24 01:22:00 | METOP-C | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f5a117ab-f2d6-3415-b769-eef94f634945 | -2.1718 | -53.793999 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5477fdc2-1aeb-3eb0-9889-836fde6cb619 | -4.2415 | -48.6866 | 2024-11-24 01:22:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb01b7ed-addb-3cef-9653-145aaa33a702 | -3.644 | -52.246201 | 2024-11-24 01:22:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 078a4415-3f41-3446-b5c0-f02768da15fa | -3.2324 | -53.929798 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c875ee5-5b92-3b2b-9061-9f1f9fe6b61a | -21.123899 | -50.581902 | 2024-11-24 01:22:00 | METOP-C | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2068e44-27c0-3e5e-a787-3920f1ad323c | -2.5944 | -54.2356 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 411010f9-5247-3298-8ccb-310315464341 | -2.3022 | -53.867699 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c778faf3-cc4b-3d72-87d9-ec8f27e92d16 | -2.1786 | -53.7794 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa367fc7-1be7-317e-acc0-5bf57d7be4c9 | -2.1689 | -53.781601 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea77d229-724d-3da6-ad88-3c85be9e19e4 | -3.2539 | -54.238201 | 2024-11-24 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01ec83d5-ad48-3c88-85b8-6aecffa704a0 | -2.1815 | -53.791801 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42427e66-3cff-3484-935a-ba3c157f52d2 | -2.0326 | -54.472 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4713ace-f9c4-3a44-99c4-ef1175412660 | -2.6227 | -54.9258 | 2024-11-24 01:22:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 131f6807-fe9f-320b-94c7-fbe549bf2e5c | -3.1915 | -54.3228 | 2024-11-24 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd1cea1-7831-3003-a1d3-088d602970f0 | -3.2966 | -53.852901 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 489cb81e-8174-30e3-b33b-1fe9d7b3fad7 | -3.2687 | -53.821899 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26b5c6bd-34e1-30fe-8248-3dbc60d20c27 | -1.1541 | -53.397099 | 2024-11-24 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6146561-664d-3405-8354-a64cc75e01bf | -1.4669 | -55.178799 | 2024-11-24 01:22:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c289716-2aaf-3bb8-9acd-a5b92b52c0ef | -0.2579 | -51.620899 | 2024-11-24 01:22:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| dd9566de-8403-319c-9913-164eaf678710 | -3.5112 | -53.803101 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19c2ed05-2c3f-3770-8b4a-620f2f7f3138 | -5.9558 | -48.063702 | 2024-11-24 01:22:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b7918d3-d3f9-3e65-b152-cb7df1ebe420 | -3.2496 | -53.264 | 2024-11-24 01:22:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37e50e2d-3550-3b23-9ad8-0e7a49f9e075 | -3.9579 | -50.194302 | 2024-11-24 01:22:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65f4ea8e-e5a1-33fa-aa44-3038c1cdce9b | -1.6172 | -54.411301 | 2024-11-24 01:22:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbb7385d-142c-3f72-963e-e2b980cd5eb0 | -1.1444 | -53.3993 | 2024-11-24 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3a53c1c-4a60-3e88-9f0b-150b0dd6387a | -3.2227 | -53.932098 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72e2e205-24b8-3d89-9f39-ca0052652b57 | -3.2388 | -54.217999 | 2024-11-24 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0952bd64-2b7d-30e0-aa65-fe586fd8e97a | -0.882 | -52.759701 | 2024-11-24 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c59a3c66-d7c9-3433-bf34-0ac890134807 | -3.1041 | -53.996399 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 406dea96-306e-39e8-97fc-44b1f376fbfe | -3.0653 | -53.2244 | 2024-11-24 01:22:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b23be51-8b20-362c-805a-2c2621b937fd | -3.2557 | -53.289902 | 2024-11-24 01:22:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04203d84-657a-346c-bd72-017c025d00f4 | -1.112 | -53.3923 | 2024-11-24 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b19fa1ae-dd60-314e-b0fd-6c1e83a30314 | -1.4268 | -53.377701 | 2024-11-24 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 703756f8-cfb6-3847-9a8f-7d3987262d19 | -1.6074 | -54.413502 | 2024-11-24 01:22:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 022a670d-82e2-33c8-96bf-64c65a0f50f6 | -2.305 | -53.879902 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32ef7145-03e2-39ac-a30c-dcc8c9e50cf9 | -2.5891 | -54.2127 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db8142bd-c54e-36bc-8b6f-7d031c7a3a40 | -1.4526 | -53.400398 | 2024-11-24 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcabada6-1110-3523-a4ee-b1d06c5042b1 | -2.6251 | -54.9361 | 2024-11-24 01:22:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6c67271-3411-37a1-a1ea-d1a24e51d812 | -3.0074 | -52.505402 | 2024-11-24 01:22:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36189ae3-16ef-3745-a3a6-817204bd6820 | -21.3239 | -55.947701 | 2024-11-24 01:22:00 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6698c65b-06b9-31f8-9ff7-b0be2389c310 | -3.2512 | -54.227001 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3da70c38-73cb-349b-8a00-b682dcd0aa4b | -1.6145 | -54.399799 | 2024-11-24 01:22:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfb3075d-63d6-352f-9a00-4817f8f83382 | -1.369 | -53.832901 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d31768b-133c-3c52-89c0-af33a404877c | -1.2294 | -53.675201 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f67666-8c21-3d64-b8ff-5850fa7f10bb | -1.375 | -55.403 | 2024-11-24 01:22:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9289214-4018-360e-80e8-c65b39580d48 | -1.2373 | -51.742199 | 2024-11-24 01:22:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35fd5d1f-3ec4-338c-af03-c52b9d667559 | -3.5266 | -53.824299 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f972003d-4c25-3f1c-9103-1af7ae73a14c | -2.4629 | -49.0895 | 2024-11-24 01:22:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 833ec936-d1cd-31d0-9bf7-a88af4b49530 | -1.3719 | -53.845501 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5228e2c7-55bc-361f-b9c1-73b3913a7049 | -3.2938 | -53.841099 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2958b141-ef27-37bf-bed0-88e882aca709 | -2.1869 | -54.472 | 2024-11-24 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdaa0a95-67af-3909-b2d8-f76194bbea68 | -1.1217 | -53.390099 | 2024-11-24 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b773c1af-37d7-3ea0-81cf-96a1f1a4c6cd | -7.5049 | -63.509102 | 2024-11-24 01:22:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0769ea52-4d00-3f90-938a-2fec9e7bfbab | -4.2511 | -48.6842 | 2024-11-24 01:22:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9789705-1de3-3f6e-a250-b08984da00d2 | -3.0561 | -52.752701 | 2024-11-24 01:22:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c73beae-e055-38e9-99cd-4221dab8a0bd | -1.4148 | -54.469601 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7147dbf6-c214-3747-97e0-4291dd7ca76b | -3.0622 | -53.2113 | 2024-11-24 01:22:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c139c423-cb83-363c-9707-4f593c06310c | -3.091 | -54.552399 | 2024-11-24 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bc49d4c-286e-3b3f-9988-1d9344f5e739 | -3.2414 | -54.229198 | 2024-11-24 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d108865-dd97-3886-ac7e-57fc6278d83f | -3.1817 | -54.3251 | 2024-11-24 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75f4fdba-11b3-3d63-8d1f-c8683fef9c97 | -0.2622 | -51.639599 | 2024-11-24 01:22:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 31e9bf02-7942-3ba9-8593-4029c70dbe28 | -3.1413 | -52.9814 | 2024-11-24 01:22:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 822b1bff-26e0-3ded-9d30-cd797ef9e0f5 | -3.4768 | -51.977402 | 2024-11-24 01:22:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dc61733-5332-3f8d-b1cf-41cf9cffc03f | -1.3726 | -55.393002 | 2024-11-24 01:22:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README22.md)
