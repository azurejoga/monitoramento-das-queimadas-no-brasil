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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fade9c59-45f3-3836-973d-adb4eb620cd2 | -20.60063 | -47.82858 | 2025-09-08 05:14:00 | AQUA_M-M | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 7636a4e5-5ad7-3a01-aaee-a16ce5305169 | -18.02969 | -47.09793 | 2025-09-08 05:14:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 979db109-8621-347e-9d53-a49305714359 | -20.59447 | -47.85922 | 2025-09-08 05:14:00 | AQUA_M-M | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 7188b83a-3dcc-3d47-9a45-8603950b8aed | -18.14599 | -43.39224 | 2025-09-08 05:14:00 | AQUA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| dcd72843-72f2-3e70-a288-133d09890fc4 | 0.54878 | -50.80183 | 2025-09-08 05:16:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8af7d247-21c9-38fe-bdf4-c65fbf8872eb | -2.14147 | -47.711 | 2025-09-08 05:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67e22e55-90b8-332a-8d69-ef699fa14ff1 | -2.13568 | -47.7122 | 2025-09-08 05:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3efe89a-5279-3f03-9313-d45330733beb | -2.13571 | -47.71002 | 2025-09-08 05:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 073c98e8-e6e7-3bc4-be5c-e78577e67e77 | -4.48949 | -54.82322 | 2025-09-08 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2fb9105f-7d10-37ed-b5b6-fd2c86401b6e | -4.42767 | -55.16617 | 2025-09-08 05:18:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16aab3f6-c2d4-3994-bfeb-00b037e497eb | -4.26966 | -48.18918 | 2025-09-08 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 677fe716-65da-3281-96c3-f818094d891a | -5.8106 | -45.65535 | 2025-09-08 05:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f55634a8-81f5-3912-ae49-b67e75327185 | -4.73468 | -55.71929 | 2025-09-08 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0161e656-b365-3259-8c17-3b1d5bc1b2e7 | -5.56105 | -52.16581 | 2025-09-08 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db581068-fa3e-39ea-bc86-8c08f4bb2f01 | -4.4281 | -55.16803 | 2025-09-08 05:18:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b21d0f1-a4a6-39bb-b754-5937618459af | -4.42875 | -55.16385 | 2025-09-08 05:18:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 590d1a57-5273-3b74-b7f8-1cc6dde530ab | -2.9183 | -48.67325 | 2025-09-08 05:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 555da383-a3c9-3ed0-ada7-39ddf4cb82a9 | -3.30147 | -54.91175 | 2025-09-08 05:18:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07ec0d11-db27-3dcf-8c8f-65280b7f75e0 | -5.10371 | -56.14902 | 2025-09-08 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b00885d2-c0f4-3d90-b6d3-37ea0dda2fcf | -4.73407 | -55.72329 | 2025-09-08 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc89cfcd-7e39-3767-a2ff-ca936d5b1bd3 | -5.77965 | -45.63122 | 2025-09-08 05:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0de4b991-8fe9-3d9e-8219-6f16a7bf2692 | -3.82049 | -54.11479 | 2025-09-08 05:18:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 001ddb5a-0b0c-325b-bd52-ca934f650c72 | -6.53653 | -44.79858 | 2025-09-08 05:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29cc327d-c60a-3daf-a84e-9572fe0c6fc9 | -4.27025 | -48.18513 | 2025-09-08 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0447dd8d-845d-37bc-a830-45212740ebd6 | -5.78053 | -45.62483 | 2025-09-08 05:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c4601f8-5a04-3e45-946f-e0cbcbe34df6 | -4.99366 | -56.25229 | 2025-09-08 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7a1942b-65a1-335d-aad8-744835e92ee2 | -3.2084 | -54.95897 | 2025-09-08 05:18:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5cef621b-4606-3a3c-830a-dbf7aee5f55e | -3.24907 | -50.81284 | 2025-09-08 05:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30638b5c-507a-3d46-a551-2139ed6e9ecd | -4.99656 | -56.25665 | 2025-09-08 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43c8cc9a-0755-3282-ac3f-f8be621492fd | -4.52902 | -54.84517 | 2025-09-08 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b116cc0b-5aad-3312-96a7-7494538cbad4 | -5.80537 | -45.64893 | 2025-09-08 05:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a99e88ef-68c6-3c4f-8ee3-14d07f476ff7 | -2.67882 | -51.83693 | 2025-09-08 05:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51d48da3-72a4-3102-9c79-dc917ed4e6d2 | -4.42726 | -55.51072 | 2025-09-08 05:18:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8c7a065-3637-3fa3-a050-b80526427e43 | -6.53787 | -45.87413 | 2025-09-08 05:18:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 637ea43c-3a31-36d5-98ec-fbbe074843c3 | -5.4597 | -51.41789 | 2025-09-08 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a33586e-3075-3e96-91f9-493b8ec16246 | -3.31041 | -48.71657 | 2025-09-08 05:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1b37663c-2ffd-34e5-ba36-a269a387fd7b | -3.24431 | -50.81211 | 2025-09-08 05:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa9009e4-550a-3246-b2bc-23cf1312f65b | -3.7922 | -48.87677 | 2025-09-08 05:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a957e3c6-2b18-34e0-a474-0b4f535a6f41 | -5.81142 | -45.64914 | 2025-09-08 05:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f7f3434-6111-32a4-8284-3b0c240a4b03 | -3.54341 | -49.37693 | 2025-09-08 05:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17a48d2c-47df-3cb8-89e2-36dcab2b675b | -5.81226 | -45.65006 | 2025-09-08 05:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7f19dc3-8cf4-32cd-958a-29aa78e2a129 | -4.47502 | -48.11808 | 2025-09-08 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 653c4b32-8bc2-34a9-813d-7960908377d7 | -5.00924 | -56.03564 | 2025-09-08 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c6e3137-0817-3804-a6ad-5c438fb00930 | -6.53755 | -44.79093 | 2025-09-08 05:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c8699a0-18ff-3a98-b8d1-21ee9a2e2dec | -3.32771 | -54.91145 | 2025-09-08 05:18:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b6bb8aa-1804-317b-a91c-287ced8f7dbe | -4.43134 | -55.16665 | 2025-09-08 05:18:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6f2b393-1087-34f0-9cb7-07f3f918c3bc | -3.7927 | -48.87335 | 2025-09-08 05:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4381d841-0c10-3522-812b-95678606d8ee | -4.99306 | -56.25613 | 2025-09-08 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9a31e920-b1ca-3000-8371-7ce7bd25609f | -3.54293 | -49.38017 | 2025-09-08 05:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c89b415-5b39-3c38-9146-94baefb7e349 | -3.81978 | -54.11938 | 2025-09-08 05:18:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c4953db-6515-35a0-82ca-0d37bd25bc65 | -3.32837 | -54.90718 | 2025-09-08 05:18:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f965d5e2-44e4-315f-840f-8c0abe1725bc | -4.49006 | -54.82562 | 2025-09-08 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fce14e8-b1c5-32ff-99f2-0a759bbf48d1 | -6.53704 | -45.88015 | 2025-09-08 05:18:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efb6e5ce-4153-3b19-87cc-48e6c4d44046 | -4.23539 | -53.55226 | 2025-09-08 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e73599b-0f80-3c4f-90f1-42f30fae61a7 | -3.52704 | -52.86734 | 2025-09-08 05:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 344c6945-0f36-30a5-af03-6cd7e4e4e8a3 | -3.30988 | -48.72012 | 2025-09-08 05:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 15179e5a-ac20-31ea-a3d6-a0f0e8790fc8 | -12.6153 | -56.9742 | 2025-09-08 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0455c703-0f4e-3c7b-9c71-5bf6df060a30 | -7.3983 | -61.6346 | 2025-09-08 05:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 335391a7-862c-3164-8f59-40a3aa313bb2 | -11.2007 | -54.9992 | 2025-09-08 05:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 0f2d484b-8cc8-362f-8d64-46873e7f21a5 | -12.6343 | -56.9725 | 2025-09-08 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8eaac8f5-a74b-3cc2-8ea7-8250b8dc99d6 | -9.47124 | -60.48721 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b55231db-5872-3229-8be2-a7294aa5c3b5 | -7.75268 | -50.72298 | 2025-09-08 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6fa62e0-191c-365d-9f42-8d6249d49283 | -11.03358 | -45.95836 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 04dbb400-9a38-33eb-b598-c25b913c0797 | -9.45982 | -56.05123 | 2025-09-08 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10dbb702-cb3f-3d40-85b3-00271f12a6ea | -10.50636 | -61.30207 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9fbf3ce-bd7a-353b-9b20-c933dc03324d | -6.86974 | -47.91286 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 52ccf6da-5764-3944-bb4d-dd5ca1d311fe | -6.63823 | -53.36348 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1420f173-11bf-3bfb-90f5-4d6b60ec96f3 | -6.27035 | -53.43262 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77e645e5-6c19-3860-9d28-a73a2bb25f95 | -9.47736 | -60.49186 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3ed4f97-ed0a-309b-8f04-a752481cbfdc | -12.19474 | -53.91731 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0c86d32-d217-3141-b9ee-c2fbb3bc48a2 | -10.46589 | -53.63377 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50f87c84-be19-3df2-8155-48793e8e9611 | -10.46951 | -53.6063 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de02d256-9d1e-3b38-ad55-0d29c5ba4c37 | -9.30117 | -66.61076 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8643082-1d5c-35d2-9ef5-83cf1240c95b | -11.1958 | -55.00023 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bef0652f-b329-37c9-a7d4-6524853dc800 | -10.17103 | -61.12785 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af4abc55-7498-361c-aef7-f1c286ea3ef1 | -9.57557 | -57.74243 | 2025-09-08 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f32b6bc-0a75-32e7-8e25-be076c2801d7 | -7.22288 | -46.20451 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0e7954ed-a04e-3cba-b268-5bfccaf7bd1c | -5.83632 | -52.20472 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 531482f1-7f3e-325b-b268-81f2ed438e10 | -8.20594 | -50.13867 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e21025d-09dc-3e8f-a9b5-85c1372d6d2d | -6.62981 | -53.36225 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c931c17-2d0f-30f6-a7b5-1930eb5c990b | -10.47326 | -53.61327 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 688efcbb-16a0-3fa1-b763-5ca34e2fad07 | -10.46838 | -53.61478 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f672e3db-2428-33b5-9e78-fc85017697af | -11.03593 | -45.94917 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 41d90794-947c-31b8-a486-4045fbb0196e | -10.25273 | -59.38346 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c46c4b0-fe46-336a-930c-a26d59c213e1 | -6.95625 | -62.93581 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2da154bf-3b5b-3601-9b51-eb20a4af578a | -10.00215 | -51.62775 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58272b9e-037c-36e3-9441-be273fb0e6ef | -6.63039 | -53.35838 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67026f1d-b56d-3784-ba79-6361dc9ad8f5 | -8.18851 | -50.14623 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37402b38-213f-3127-8d8b-c009c03b4383 | -10.46888 | -53.61263 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c475e9e4-b546-38a7-bbf3-4c647d5e37a0 | -8.9241 | -45.81156 | 2025-09-08 05:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 597966ef-2b1e-3ee7-9e4f-55533134e695 | -12.81853 | -52.94236 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ffae036-41ab-31df-bd67-4af80a5e5196 | -9.90991 | -67.01415 | 2025-09-08 05:21:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0661ad5-0109-3134-abc2-9bcf6826f159 | -6.96831 | -62.93315 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f82fc574-36ef-370e-ac15-dc37a953112f | -6.8704 | -47.91089 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 73c1cc4e-f0fa-3b08-9988-2eb12da519d3 | -9.16999 | -59.36575 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 754cac1d-6a79-3107-be4b-a170e7374830 | -9.84786 | -53.29521 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8620f60b-7697-35bb-9c82-b77b0bb2eac5 | -9.14864 | -46.06984 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18feb80c-76f6-3a32-a89f-4523bfb950ba | -8.96989 | -62.96354 | 2025-09-08 05:21:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24b180e7-7c20-3a7c-9d34-55c6a8d12462 | -9.20749 | -46.03857 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 972c47e2-2d83-3225-9ffd-b0035d3d736d | -9.37694 | -65.93922 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README77.md)
