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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b3e247e-d05b-321e-889a-28f967229be5 | -9.0842 | -61.3925 | 2024-10-10 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| a8e9a8df-bcff-306f-adc9-a6a6e48e1d98 | -9.122 | -61.2951 | 2024-10-10 03:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 62832ff8-2d63-309a-a6b4-217ea19d8dac | -9.1221 | -61.276 | 2024-10-10 03:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 180.6 |
| ed9f43cc-9495-3757-8676-88ebb86308a9 | -10.178 | -36.4313 | 2024-10-10 03:36:03 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.5 |
| 5a205650-3271-3f07-802f-1d5a5118ab60 | -10.4287 | -60.9979 | 2024-10-10 03:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| dcc90caf-1a09-3887-af46-0f136bf09617 | -11.0254 | -57.2237 | 2024-10-10 03:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 8236bf88-7309-3ca9-a40a-3ba6550ab7bd | -11.0256 | -57.2038 | 2024-10-10 03:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 5c0de8ef-e669-3167-9262-9e26acbc2c56 | -11.0443 | -57.2222 | 2024-10-10 03:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4795b69e-b523-3bdd-9db7-6c1539ed9213 | -11.0445 | -57.2023 | 2024-10-10 03:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d0fc2f21-8d49-3f0f-be80-224d98f7ecbe | -12.2893 | -43.7258 | 2024-10-10 03:36:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 1a02b9fd-cc64-3388-b01a-98d1f1cd7202 | -12.3065 | -59.1838 | 2024-10-10 03:36:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 3a30ff40-b4e9-3ec0-86d7-58f828ba6db4 | -12.9921 | -62.7554 | 2024-10-10 03:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ddb055ea-8a4d-3a15-a828-dd4e12f6c956 | -13.8374 | -44.5455 | 2024-10-10 03:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| c01cdd88-4b19-36ad-a781-1717c8687573 | -13.8379 | -44.522 | 2024-10-10 03:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 172.6 |
| bec06ec1-b164-3d77-a6de-9c2968b962a8 | -13.8569 | -44.5421 | 2024-10-10 03:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b12fc6ea-9115-3f51-80c2-a87c7ad5882d | -13.8574 | -44.5185 | 2024-10-10 03:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 287.4 |
| a51ea814-c400-3f99-98ee-6af586073cfe | -13.8579 | -44.4949 | 2024-10-10 03:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 904a77db-bf63-302b-adae-dcdec5d44f65 | -13.8769 | -44.515 | 2024-10-10 03:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 63b979ca-a159-3755-8ccf-33ad3deeb44e | -2.6532 | -53.3708 | 2024-10-10 03:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d934cb07-c119-3f25-8074-1600453d01b8 | -2.6533 | -53.3506 | 2024-10-10 03:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 00dc3e7a-7052-321f-9b5f-60e2a0a36949 | -2.6716 | -53.3704 | 2024-10-10 03:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 55fee879-1d75-3c49-9b3c-e55e1e235bf0 | -2.6716 | -53.3502 | 2024-10-10 03:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 295.0 |
| d3564a84-b101-39e0-a3d9-3fe524a5f2a4 | -2.6717 | -53.3299 | 2024-10-10 03:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c2deddeb-69f6-3d45-a3f0-98c32e1ac907 | -2.69 | -53.3497 | 2024-10-10 03:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| cad242b2-052b-32dc-a52e-d61ec0d994e4 | -3.9103 | -48.3466 | 2024-10-10 03:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 20691e5f-cb74-30ed-814b-c80a5989cfec | -4.0814 | -51.0292 | 2024-10-10 03:45:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 30fff9cd-ddbf-3661-8659-ecb7de1a061a | -4.0961 | -48.2739 | 2024-10-10 03:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 209ae3ae-b7e7-384a-b1ef-e5ad8ea11cf4 | -4.0962 | -48.2523 | 2024-10-10 03:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 3a6d1d63-8e50-348c-8697-3aea31f3dd21 | -4.1146 | -48.2731 | 2024-10-10 03:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 05eb007a-7b78-3098-9499-69288426a84e | -4.1148 | -48.2515 | 2024-10-10 03:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 3d1eae90-5d74-3702-85a6-73a13989edd9 | -6.7654 | -59.3252 | 2024-10-10 03:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| e8d06476-b35a-35cb-a1eb-d02be6eef982 | -6.7839 | -59.3245 | 2024-10-10 03:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5214f773-9b35-37a6-b01c-06c29a0441fb | -8.1478 | -42.9481 | 2024-10-10 03:45:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 2cb4d1e7-6129-3af6-9c2b-0695ba37a713 | -9.0084 | -61.6253 | 2024-10-10 03:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ecad9a84-b383-3bcc-8ae1-80be3d4d0f19 | -9.027 | -61.6244 | 2024-10-10 03:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| cb118054-17f9-361c-aee1-9162d30cca04 | -9.0656 | -61.3934 | 2024-10-10 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c57d2941-f7da-36d6-a2cf-1e3f0f1c5fb9 | -9.0841 | -61.4117 | 2024-10-10 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5ed2a9fd-54b2-30f8-b3bf-64583dd11f3c | -9.0842 | -61.3925 | 2024-10-10 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| f0946891-bff9-3a83-8c4c-9a124a73698e | -9.1035 | -61.2769 | 2024-10-10 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 5cb602c1-3991-3945-95b4-3a811436580c | -9.122 | -61.2951 | 2024-10-10 03:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| a04100c5-0c22-3f83-943b-5eaf8e216e19 | -9.1221 | -61.276 | 2024-10-10 03:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 40b15f62-3ab4-34e0-806d-d8f88e9f65b8 | -10.4287 | -60.9979 | 2024-10-10 03:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 7a2deb86-f4b1-3b97-8881-bf0849a0fbad | -11.0254 | -57.2237 | 2024-10-10 03:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 969f3b61-c77d-3e6d-a468-6a7fa80c2877 | -11.0256 | -57.2038 | 2024-10-10 03:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| fec57270-0f61-357a-b1aa-e25e28fc5c69 | -11.0443 | -57.2222 | 2024-10-10 03:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| b7564bae-41ca-36d3-b8b5-69cef81e0e27 | -11.0445 | -57.2023 | 2024-10-10 03:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 80fb350b-696b-3486-b41d-c66e70165bd8 | -11.277 | -60.4067 | 2024-10-10 03:46:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a9360224-d1c6-3c38-a898-6d2f4de6e596 | -12.2893 | -43.7258 | 2024-10-10 03:46:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 8f086440-36a0-38bd-b90e-f4939a58351c | -13.8379 | -44.522 | 2024-10-10 03:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| e1b3d7fe-a97b-38ca-838b-880c34c192bc | -13.8384 | -44.4984 | 2024-10-10 03:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a85dda03-6800-3f84-ad51-4d4c7ae18b1d | -13.8569 | -44.5421 | 2024-10-10 03:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 03a7cab7-0a7f-3ffb-b6a9-86d811e3b626 | -13.8574 | -44.5185 | 2024-10-10 03:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 308.9 |
| 8876a8e1-d821-361b-b813-662902acd9b3 | -13.8579 | -44.4949 | 2024-10-10 03:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| dc951872-4c47-33d1-8920-bb87dccba85e | -13.8769 | -44.515 | 2024-10-10 03:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 78bcf0dd-bd16-3603-bc7b-9103b638fe29 | -14.8177 | -50.7974 | 2024-10-10 03:46:30 | GOES-16 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 651f1dd3-c0b8-38e5-876c-147876786d11 | -5.07131 | -37.71534 | 2024-10-10 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 920c7d86-050e-32c2-b060-482ed37f4e23 | -3.48001 | -39.53407 | 2024-10-10 03:53:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa019e0a-4b4e-33aa-9e6c-fb7ee4c310f1 | -3.45897 | -39.15514 | 2024-10-10 03:53:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 72dc1dd8-994b-3241-b305-65e33b45f845 | -4.05301 | -40.48988 | 2024-10-10 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1fcc806f-d699-3f91-af85-05b227d75de4 | -4.05229 | -40.49055 | 2024-10-10 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 40c40a4f-c66f-31ae-96dd-64495be2efef | -4.04716 | -40.40912 | 2024-10-10 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6cba1673-c455-31f1-83ef-b1021bbd6319 | -4.04428 | -40.40462 | 2024-10-10 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 110fdccc-b48d-3110-94f7-a1d35dca610f | -4.0414 | -40.40013 | 2024-10-10 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e682aef-ad25-36bd-aa53-cc95e6e4100f | -4.02863 | -40.3901 | 2024-10-10 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dcde1f96-90cc-34e4-900f-cfb30b68ec3f | -3.96272 | -41.48214 | 2024-10-10 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c479ab04-660c-3b8c-9cf7-9e20bc480ee2 | -3.95689 | -40.72523 | 2024-10-10 03:53:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1767cbf5-85ea-3866-b74f-a4921c6db7f5 | -3.88825 | -41.03674 | 2024-10-10 03:53:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 721e90b2-006e-3d21-af06-47efe0802ecf | -3.88757 | -41.04095 | 2024-10-10 03:53:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 013f995b-a57d-32d8-8504-b7ea8a007185 | -3.36463 | -42.88759 | 2024-10-10 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78c308dd-4c4c-39fb-83da-4de25aaea764 | -4.71713 | -42.94491 | 2024-10-10 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e58b221a-c44a-3cf7-91c0-cbb841fa9ede | -4.71657 | -42.94839 | 2024-10-10 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7ac4af2-8bd4-3644-945b-2534e9965d29 | -4.44427 | -42.90668 | 2024-10-10 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 770e1fff-78b2-38aa-b02b-2d2db8981c0d | -4.44025 | -42.90606 | 2024-10-10 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79a1dec6-7de1-3645-8988-470cffb785de | -3.53885 | -43.93968 | 2024-10-10 03:53:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9966deb7-d8fc-3a6a-8901-3cecae894d16 | -3.30168 | -43.50822 | 2024-10-10 03:53:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f13320e-b37e-3237-bc8f-15ed58059bb3 | -3.30103 | -43.51219 | 2024-10-10 03:53:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a7f0536-bc99-31f6-9fef-2168f1085dee | -3.46012 | -44.27833 | 2024-10-10 03:53:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e98991cd-3b66-3e32-a0e9-66db5e9dd883 | -3.45938 | -44.28279 | 2024-10-10 03:53:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55a1ba3e-48bd-36a0-b9b4-ebb48c67801d | -3.55637 | -44.37946 | 2024-10-10 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b56f6ee-69ec-39b1-81a5-e507379f03a1 | -4.49659 | -43.84286 | 2024-10-10 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| efa3d458-6c3b-3475-9e18-0f9e9783deee | -4.40635 | -43.52148 | 2024-10-10 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 346feca7-c76b-3779-9281-c62dac761df2 | -4.39737 | -43.52391 | 2024-10-10 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afdc663a-a2eb-3704-a6f0-1ca4e839bec6 | -4.39319 | -43.52318 | 2024-10-10 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20965b7a-de11-3c8a-9c5d-adbb04f77b4b | -4.36398 | -43.57005 | 2024-10-10 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e2720e3-afcf-3e66-8fc9-8c06cb61380d | -4.36361 | -43.54617 | 2024-10-10 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dbd02fc-38f8-3e7c-a032-36531673cff5 | -4.28334 | -43.14472 | 2024-10-10 03:53:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d60591e9-0278-34c3-a6f0-be8ad967e952 | -4.02852 | -43.39429 | 2024-10-10 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5385a9e8-facd-3977-b720-411f69fb89ff | -4.02695 | -43.23555 | 2024-10-10 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62d03fea-c107-3805-ad14-46b96dd32843 | -4.2931 | -44.38484 | 2024-10-10 03:53:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ecd63d1-1285-38fd-b0bd-624930fccf9a | -4.29196 | -44.38438 | 2024-10-10 03:53:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e18133aa-44ee-39c1-bb73-e530ed041379 | -4.29118 | -44.41598 | 2024-10-10 03:53:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36db667c-6e68-33bd-bea4-60be27098bb9 | -4.28865 | -44.38414 | 2024-10-10 03:53:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc87e6a4-4d25-3bb3-ab2f-2057bf3ea049 | -4.28751 | -44.38367 | 2024-10-10 03:53:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6320c7a-f6c0-38d7-861c-32557f4dd5e0 | -4.28348 | -44.38783 | 2024-10-10 03:53:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b658f42-9da3-3ca3-9a7b-83679780f2b4 | -4.28232 | -44.38736 | 2024-10-10 03:53:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3426fec-5ef8-30ee-8c74-06e5922622b8 | -4.04609 | -44.26257 | 2024-10-10 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7639265-f109-33ef-a92a-a78d3c977e3d | -3.78897 | -44.36823 | 2024-10-10 03:53:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25303940-7c2e-3108-9a06-aabe2b4dcdfb | -1.48325 | -46.89808 | 2024-10-10 03:53:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97a146a2-6460-3105-841d-0b71c07c8452 | -4.28443 | -45.47066 | 2024-10-10 03:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dddac203-44d0-33dd-a08b-5050190f13e3 | -4.27963 | -45.46991 | 2024-10-10 03:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README40.md)
