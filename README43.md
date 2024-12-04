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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c67d1ad4-1100-3ee9-ad28-081f83ce60ba | -2.85367 | -54.82584 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 51db6e48-3b0f-3240-8f44-86e1d258f368 | -2.78224 | -55.37055 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52e2f2ff-c563-399e-bd0f-f2815421d51e | -2.9795 | -53.90486 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbf87d90-3912-39b0-9391-b0dfba6c4333 | -1.70402 | -52.62524 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8405af0b-ed67-33b4-b4a3-20d5cd9dd4f6 | -1.75777 | -52.63645 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5bff3af1-3b0c-3b84-8593-10afc8811caa | -2.09633 | -46.5821 | 2024-12-04 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d729998c-2024-3547-9c71-982fc462bed7 | -4.71219 | -47.20176 | 2024-12-04 05:03:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62351718-9a80-3376-9cd4-43a8fc20465d | -3.40093 | -50.22174 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a13ac189-f982-3703-9e7c-0150073b904d | -1.69439 | -52.57279 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e47dd9c-7de2-3d83-82b3-910e91f226a5 | -1.66693 | -53.22571 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8df03b48-ebe4-38c4-a3f7-1ffa30ddc66f | -2.58655 | -53.67659 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 225aa407-6717-3e8d-b519-497f31b85082 | -3.18862 | -54.33458 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ecf79c1-f359-3a81-8904-02e085266a36 | -2.00191 | -54.11502 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 362e4b86-1e0b-38c4-ab3b-77c1d83acf40 | -2.61414 | -54.09126 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fefb3a5c-0ddd-3d22-a451-380de9d515fc | -4.05739 | -46.81561 | 2024-12-04 05:03:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e97c6167-0787-3fde-9e6e-65571c2306af | -2.89698 | -53.97971 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6643e13f-893d-37a4-beb1-b7424eb703ef | -4.0404 | -48.34189 | 2024-12-04 05:03:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49a930ff-321a-36e2-a169-1f62915c22ac | -3.31363 | -50.4393 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c75b0f6c-10eb-36a5-9501-bbf446ae12f9 | -3.25751 | -54.10726 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 016ebb19-08d7-348a-9fcd-717518ad783c | -2.33668 | -53.92947 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00d8d61b-04e6-3500-a1d0-cad68377e496 | -3.25175 | -54.2112 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ddb1ae5-e2d7-3605-9c71-e65128edc919 | -2.63336 | -45.73726 | 2024-12-04 05:03:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 444ac630-9c1d-30b6-959f-e5d59115738f | -2.6973 | -52.91207 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77d30afd-8b22-3b32-8422-b6cfff10ce57 | -2.81688 | -54.05429 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 285bb587-bbd1-3105-9283-1468d1f36dc9 | -3.10085 | -53.29882 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20e6a2f9-785f-381d-a890-14a025ff279c | -2.52114 | -51.81082 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efc31192-e32a-3d52-8a56-02da83d7d235 | -2.96715 | -53.89569 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d467c4c-effa-379f-8321-ec9d8150a189 | -2.45038 | -54.00869 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8047f92b-8940-34ec-aba8-7a0faabd8316 | -3.81786 | -51.99828 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 368d2da9-0a96-3f1c-afe7-98530407e70c | -2.77332 | -54.18454 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2377279f-859b-3f7f-a2e0-b1edf802d166 | -4.27473 | -46.57344 | 2024-12-04 05:03:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 843c2c30-0325-3ceb-a88d-66e01394f7bc | -2.41225 | -53.66454 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fddd478-22a3-345c-a093-a62c0caee172 | -1.05569 | -53.3806 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 699ddd35-36ad-3d48-ade3-2228e43276a9 | -1.75029 | -52.61572 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6df997ee-9f3f-3dd1-8f69-3366b4fa7b90 | -3.06831 | -54.03458 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f7bb195-7296-32d3-a287-c60d09b1b697 | -2.77823 | -55.33125 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13f8e8db-b5c9-3889-8aa8-9a70cd095804 | -2.72996 | -54.17787 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cca76b83-c933-34f1-bd9d-4b806ff9318b | -3.07523 | -53.92296 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d955af3-c664-32a0-82f7-d4f9b61a52ff | -3.29137 | -50.39687 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f24cba1-4406-3644-a5f5-90d40905ed1c | -2.55797 | -53.40579 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06a22d09-bb9b-365c-8386-e2724fed54c8 | -2.84369 | -46.69067 | 2024-12-04 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8952b34e-7ae3-3a0a-acc3-0158a50dd85a | -3.03939 | -54.06644 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 014ebe03-56e0-3f54-bd3a-056c3de2469e | -3.80221 | -52.27254 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e768d11-58a4-3482-b972-cdd6d8d19b5a | -2.19999 | -47.24408 | 2024-12-04 05:03:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8e765d18-b2b1-30d9-a72b-5fc15a49e7ca | -3.9618 | -52.20566 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ac15c09-a548-36e1-a75a-42053aa1f8b2 | -2.87467 | -53.99078 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8e50f85-4983-3d1d-b2be-564b1467d928 | -1.73697 | -52.60974 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68b6d2ba-0fb3-3066-9304-f545dc0867d7 | -3.03203 | -53.42792 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e5cb545-960b-3bb5-819c-3e2616500a26 | -2.46172 | -53.62448 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16096990-ddf3-3b43-9a13-2c39ff942fcf | -2.42092 | -54.02216 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd899ae4-ec10-3a5d-981d-a59a5d44b505 | -3.21893 | -53.12445 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 342bc7b5-5321-3faa-a767-d9f9f3450ce8 | -2.65648 | -54.10488 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d6e66c3-de90-3fcc-a0c7-62b3e599b9eb | -2.41478 | -54.01761 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eccd0fea-fbba-37a6-a832-cf3d18f369d6 | -1.75277 | -52.80661 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6765f27b-290d-3452-83a3-92f2297897da | -3.10543 | -53.2919 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b44cd662-b588-3402-9f73-aec7689832e3 | 3.13993 | -60.27762 | 2024-12-04 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3d0330b-7f5e-377b-8004-bedd1ea7b973 | -1.72563 | -52.48684 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ced5869-0446-3edd-acd2-4caf496bcc13 | -3.13194 | -54.17133 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39167bcb-fb05-308b-adbc-c360adb21365 | -2.79609 | -54.14482 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af489004-3986-3e9d-8d2c-2cb286d15cb4 | -2.78823 | -55.35389 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e80880df-107a-32ae-849b-e989a5e66bc4 | -3.01719 | -54.01622 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 602e2148-d2af-3240-a0e5-1242b0ff48f5 | -3.10351 | -54.05093 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e573713b-3c23-3505-ba76-3fbd21ec9b88 | -2.80928 | -53.05244 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a7f475a-c6cf-3340-9371-3820f9959532 | -2.87187 | -53.98673 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02cc4e57-d695-3c95-ad91-7b0e97cb8843 | -1.47231 | -54.4587 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85aae8b5-9260-3806-bde6-1f73159a0237 | -3.55382 | -50.20036 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bf30fb5-4164-33c1-8002-0f5bdf72849d | -2.63752 | -54.09484 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed2d872e-fe35-3125-ade3-7ff0e8f0d990 | -3.3447 | -51.20695 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 427f353b-64a4-324c-8fc4-1fe19103c964 | -3.25724 | -53.64927 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c4b94142-726c-3810-abe5-9aab7d035479 | -2.87314 | -54.04488 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a5cd675-74a8-359c-ba82-9146aa6eb675 | -2.647 | -54.09986 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 923bf752-f1da-3e38-ad8a-30c271755e93 | -3.13231 | -53.27697 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8710763-5775-3dc8-b89f-b3f9ac405227 | -3.17754 | -54.34001 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 220d45ed-fddc-3776-b49e-3a81e0805ed0 | -3.09028 | -54.11402 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 772c9694-0a93-3e54-9bd1-90523496da9f | -3.10886 | -53.29243 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72fc042b-4102-34c7-b531-521f5f309160 | -2.80753 | -53.06372 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e272514a-6f94-3f81-96f5-61ab306a656c | -3.26628 | -53.6581 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c35171fd-891b-3707-be66-d190877c8c28 | -2.88422 | -54.01763 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 134aa963-c29b-3eb5-874a-016ce62e7e11 | -3.92203 | -52.39114 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18af9857-9d3f-39c7-b7c7-40a4fdc00696 | -1.13931 | -53.05224 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8171754b-cdec-32f1-9292-a28a250b7464 | -2.86352 | -53.99632 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac526c6e-77ab-3230-9c1c-ba7c6c66864d | -1.62231 | -53.53651 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3a6e4c61-4bd8-39a4-a612-5e888d43c92a | -2.93388 | -51.80393 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f48b6b69-2ffe-3311-9334-f70c2002e09d | -3.05088 | -54.49859 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f30836dd-8307-304a-88b2-4c7f2bb60ae2 | -3.26795 | -53.62486 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ba07ef4-055f-34c8-8659-7e8a67093f78 | -3.81694 | -51.66395 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39b4292e-a0f0-33b1-8207-45c39d25864a | -2.62914 | -54.25864 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f4b267-6154-3b96-9d6c-4d2476213baf | -2.03924 | -53.94131 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 36b779fe-d11b-301f-930d-06788f95a59e | -1.82936 | -53.14901 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 933c7063-891c-3238-a07f-cfbd5a3660e2 | -2.84437 | -53.94251 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcf8f383-44b4-3acc-afe8-9afb73ed93f1 | -2.58738 | -51.91844 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb8fd9b5-117c-3f25-a9b0-383a4a63b972 | -2.24931 | -53.63594 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c3a527c-3dbe-3323-a46a-95b911435f79 | -2.88032 | -54.02066 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66d6d877-7dae-334e-b338-a47023d1de1c | -3.09858 | -53.29082 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ceba39d4-213f-3998-a531-74221cb53e01 | -3.95883 | -53.97002 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60e8ed39-3acc-3901-83e5-33ba80bbe68c | -2.63343 | -54.20913 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15424ba1-76f6-33eb-aeaa-a54a1c3de00c | -2.87854 | -53.33004 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4a6d7b0-62fe-3f3f-ae2a-fe8234147c31 | -3.11704 | -54.61937 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f939a347-6199-328a-9b22-000d2138c145 | -2.45331 | -53.63425 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 114d7761-6cf3-3a13-b75e-1c93934506c5 | -2.86043 | -54.08266 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README44.md)
