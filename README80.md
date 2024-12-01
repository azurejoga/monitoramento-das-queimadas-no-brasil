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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f3cc732-e9f8-3654-b994-65280d8b6baa | -3.03241 | -51.54079 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cb95c38-87c6-3c26-a7d4-39de0b60ffb5 | -2.968 | -53.94283 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d7da71b-8e63-3f2d-bd3b-bfe0a3b06787 | -3.09261 | -53.29224 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a422fb4b-6690-3901-a813-2552c38e27a3 | -1.48146 | -52.67889 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 454ad5ce-21fc-341f-a9e5-ec808ea1337f | -3.14388 | -53.83168 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2be5047-8397-3247-a349-b0a20f84e7a2 | -2.31525 | -53.8522 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bafd1d7b-97c5-30ea-ac2c-4a7333b4d1ed | -2.3324 | -50.673 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6f13b21-2887-3e56-aabb-7758041f0c9b | -1.82176 | -50.90681 | 2024-12-01 05:08:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d8dcc70-92fd-3b8b-b394-371c0de3479b | -3.00434 | -53.23242 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9979c75-5e39-3128-96f0-045b59e4a5d0 | -3.7736 | -51.6192 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 064596ff-4ffe-317c-b78a-7cd56803df9a | -3.10818 | -53.75751 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a0ac81b-beb8-358e-9029-8c7e9159dce7 | -2.37455 | -53.66026 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e71aa28b-12e5-3a89-895c-34ed5aaffc31 | -3.48108 | -50.25119 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0d0dc48-3d30-3c89-b1f0-a59d57a9e78b | -3.46601 | -53.8781 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2174a64c-69b2-3506-8c64-4257d803a4f5 | -2.94437 | -54.42004 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01ed40a3-a0e0-3353-aa98-e6283573e94e | -4.55657 | -45.7247 | 2024-12-01 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ce8179e-e3d5-3911-89b5-81fa5fd7ddcf | -3.25051 | -53.86804 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88ad4060-4528-3b6a-b379-bfdcca87f9f6 | -2.59961 | -54.22263 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aced274f-1d6a-3fc7-bb0b-e3bf65d050da | -2.60703 | -54.28926 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6004fc3-dec9-3071-a0b8-2394ec4b29e7 | -3.15096 | -53.83267 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32dd63c8-a0aa-3b2e-b7c9-4cba13fbb84f | -4.55725 | -45.71995 | 2024-12-01 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09ef97d4-c061-3168-b13d-85893e686da3 | -2.43426 | -53.88448 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e841c4bd-b550-3e04-82e8-dce44e705a27 | -3.10026 | -54.29705 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be0a1e7a-b8d3-34dd-a107-b3c55a613575 | -3.01588 | -53.22986 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8c45e42-2ab7-3812-9ac0-0a4b612e5e01 | -3.40787 | -51.97597 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27d16aaa-549c-31ff-a5f0-01bfd8e3e261 | -3.21874 | -53.63035 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 276458d8-b41b-3142-a4df-de31fafcaca1 | -3.68778 | -51.82445 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3d5a765-45cb-361a-ab09-9f956286f24c | -3.33312 | -53.54665 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e84754da-8788-367d-b6be-1e995fe01637 | -3.47841 | -50.44625 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79e72492-2763-322e-b305-d1aa34157a64 | -4.11502 | -54.41107 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c37e72e2-c1cd-3104-8d27-56e02fb180ea | -2.78057 | -52.866 | 2024-12-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 202ec61c-7e42-3ae9-96a7-72f18a9ce271 | -2.86801 | -54.00366 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffc4dbe4-bd82-3cba-b5a2-3d68dc456626 | -3.32502 | -52.07315 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc50e829-1e09-33e4-88ce-f727eca11cf4 | -2.90224 | -54.17413 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 579c9161-45f0-3eea-82e3-d2ecc5dd17e2 | -2.98748 | -53.88578 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f20f0eb9-e55b-380e-a911-7fefb95b1f8e | -3.17344 | -53.63995 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e37ae11-7130-31c1-89f0-75e6b5eeb79d | -3.13745 | -53.16945 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be11738f-5355-3b97-9191-ae542a22c077 | -2.4479 | -54.005 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1b8db01-96f2-3578-8249-e0bb8cbf819b | -3.18092 | -53.25262 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87a0422d-ddea-3ac8-a9e5-3b1354cfc393 | -2.87143 | -54.02797 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a112507-af66-3125-ba3e-97f917f659f6 | -2.368 | -53.67941 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1d801d5-ffcc-3e94-908e-aacade2c8e59 | -2.8448 | -54.05289 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a828071-f660-3efa-9aad-2b086ff6fa8c | -1.65994 | -55.23214 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8dc6adb-0c18-333a-ab06-501db0e1eac7 | -2.03004 | -55.77315 | 2024-12-01 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4737a4d-52fe-3f97-a67f-ba5e091a23a7 | -3.49876 | -53.83041 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac5e4f2b-448a-300d-9b8d-8ce7c56bef56 | -2.6351 | -46.88009 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a06c49b5-4769-30d3-8214-d72efb3f7b71 | -2.83989 | -54.09409 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 520d87df-82fc-3188-9222-7d4f682fc2db | -2.73673 | -54.0363 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2aa59b3-fcf6-3e1d-8132-afb19552f77b | -3.41607 | -50.1779 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10ddf856-8584-3eee-b0ec-0eb624e9785d | -2.59077 | -53.99152 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68e9c4de-5ec8-3779-980c-6403709f1fb7 | -2.62412 | -46.95526 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 426f16a5-213b-3a15-a697-c1b8d16e3820 | -1.51008 | -52.56779 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8794ecee-123c-34ae-bf34-0880f8c244c9 | -2.10176 | -47.62765 | 2024-12-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b00faec4-4df2-3584-9c1d-034e31bd9fe4 | -3.05933 | -53.67691 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40237cfb-7766-31e8-a404-9111db4c946f | -2.04415 | -54.70934 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66886b46-51b6-344a-81c4-89c4a2939a6a | -2.84405 | -54.04349 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6097bcb-f901-3e6a-a770-729924b19aa6 | -2.77331 | -55.34277 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37cb417e-908a-374e-8a57-adbdb4fb45ef | -1.64034 | -53.86338 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba8bd47-6f5a-3195-97c9-8eecf097eda1 | -2.88628 | -55.22605 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72e0d35f-e146-3212-97da-f9c0d7f6445d | -3.30466 | -51.10921 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 920bb487-ab9a-320c-8109-0ff68b9b443e | -3.11331 | -53.27818 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c26e817d-e6a5-35f9-be3c-f4453add918c | -3.48643 | -53.81629 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6c42d41-970e-3139-886a-88e76c8a93e1 | -3.37987 | -49.85955 | 2024-12-01 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61b0bfcf-6d86-32e4-9797-de0f9d24fc62 | -1.43799 | -53.39851 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef7c6cb0-e5c2-3e1b-9872-5cb003482cc5 | -1.44616 | -54.54157 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 995e047b-70d0-3bf9-b2ef-d03ebdf27a2a | -4.18894 | -50.68774 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b16dc915-9949-3ffe-af4d-3a9d8707d467 | -4.06748 | -51.06371 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8327060c-cae2-3d07-8c2a-d918cfe98504 | -3.41236 | -50.34856 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 102df60a-848d-35e8-862b-3bb8b64eeedb | -2.59426 | -53.99205 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45d75a17-722b-3177-942a-214ffd9250cb | -2.25664 | -53.62653 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 166a59bf-54bf-384d-92b7-04f8e0cafb46 | -3.3061 | -50.49073 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43f2eb51-1a31-3b66-8538-7b9af2f8f193 | -4.2565 | -50.83863 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 621b9e04-57d3-3f63-acb0-3bf6d337853b | -2.7976 | -53.0438 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e910a9ab-e842-371f-bc48-81ba863fced2 | -2.44266 | -53.61777 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb237786-fd42-31cf-966f-ec4fb6fb1b3a | -1.26029 | -53.37802 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc0ab3e0-740b-30c3-9eb9-773095ab4285 | -1.64259 | -52.74829 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3400faa-d906-3545-a76b-fc9686029266 | -2.33181 | -50.67687 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac6d1e59-69c8-3af8-8f1c-d3cf22127026 | -1.63974 | -53.8672 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e5a1c91-1ea8-3c11-9149-ecbbe97d005f | -3.46462 | -50.27065 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 41168b43-2b4a-3527-bc8e-831826771ca3 | -2.4462 | -53.61833 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9e947c2-3243-3833-b5d5-67055f58f369 | -1.20704 | -54.16868 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f283489a-e258-3f24-a63f-d509fba9cb03 | -2.74916 | -51.74994 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| baf0e327-36d3-342e-9ad4-0c5bd5299174 | -3.70361 | -51.06702 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b25cbfa4-f147-37d6-b101-8c1ea2caacb8 | -2.44849 | -53.62688 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20427184-0cc7-3d0d-b064-067b3caa93a6 | -2.44974 | -53.61888 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e500389-32ce-3c1d-9f18-2b66a502b3aa | -3.17701 | -53.64048 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9232cf2-9b7b-3c02-b805-c472535880f1 | -3.87822 | -51.80712 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68ab4bc2-84fc-399a-8113-f6c1dd928420 | -3.14033 | -53.83125 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8229ec2c-2abe-30f5-bedd-03ba94d18cca | -3.46955 | -53.87865 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0200301a-f8bd-3a54-a60e-94cc043f93c5 | -4.26447 | -50.84397 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3d2b9d4-58da-3fb3-8780-09b25e7593dc | -3.53631 | -51.50763 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43341b40-b356-391f-9a06-d4e5e4d81492 | -2.97729 | -53.9007 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2dcfff14-dbbc-3ce3-9482-5613c560f8b7 | -4.39184 | -49.92944 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93a7b4b9-420d-37bc-b3cd-ef19a7b6ed13 | -3.50463 | -53.83932 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e915793d-8eaa-35e5-8ece-a275d85002b4 | -3.59205 | -50.38074 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ee45e57-2c40-3208-a7b2-4bae38f02350 | -3.32435 | -50.21844 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3123f519-14b2-3970-b044-d23726bf11bf | -1.05304 | -55.24564 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cce4bca5-0d5a-3d35-8899-7821c474d852 | -1.59611 | -52.29112 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7e226f4-290d-3670-84db-93f44169dd37 | -4.43995 | -45.36104 | 2024-12-01 05:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f668f6af-1f8d-3a59-898d-654dda5618ae | -1.62213 | -52.6892 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README81.md)
