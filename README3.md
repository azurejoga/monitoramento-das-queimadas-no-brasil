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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8281f99-f5a9-3bf2-a8b8-94a49232ce9a | -3.774 | -46.1196 | 2024-11-22 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 1616e855-e31f-36de-850d-d5ee7d7338e0 | -5.9557 | -48.0425 | 2024-11-22 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 5e2c4c82-acfc-3528-aeac-9953add65cb0 | -2.5012 | -49.0162 | 2024-11-22 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d2f43bf4-8fc6-3595-b7bf-12accf684903 | -1.2041 | -51.9478 | 2024-11-22 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 0905d2ae-5092-37d6-9d03-31239e798347 | -5.9556 | -48.0642 | 2024-11-22 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 3beb286f-3d12-3486-8b1c-0af428ba2377 | -1.1287 | -53.3951 | 2024-11-22 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| e913375c-3329-3371-bab8-fdb3ba3173ea | -14.5577 | -54.7412 | 2024-11-22 00:50:00 | GOES-16 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| bf9516f0-5aac-380d-9c9b-7772eefc9599 | -5.9742 | -48.063 | 2024-11-22 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 02a10ecd-aa4f-3367-8bae-43216ea9a44a | -4.1182 | -51.0486 | 2024-11-22 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8196d65a-87be-339b-94b4-9df1f0e4006b | -3.4975 | -53.8137 | 2024-11-22 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| d467a692-4bbb-3770-a5ce-4a21c5d1ec9c | -1.7549 | -52.3913 | 2024-11-22 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| d7fed735-f493-3b79-b276-d8700ae8d957 | -3.4592 | -45.9104 | 2024-11-22 00:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 175.3 |
| bd26345b-95f9-3238-87fa-dbe10460856a | -1.1103 | -53.3953 | 2024-11-22 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 6c33e388-74ae-3502-83e7-0fc6251a818c | -3.8355 | -52.2576 | 2024-11-22 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| de7c310e-7584-38af-88fc-a944f819782b | -3.516 | -53.793 | 2024-11-22 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| ddd15f7d-c562-3201-9fb8-29d130dbe65c | -9.3986 | -35.9196 | 2024-11-22 00:50:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| 7a1d96de-57c2-337d-b547-f3a1c738aa89 | -3.4976 | -53.7935 | 2024-11-22 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 5a6c052a-3b1f-3d4b-8e87-ad0955d794d8 | -3.4778 | -45.9096 | 2024-11-22 00:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 2dbff484-b480-3199-9bc3-6f0b8fc687ee | -1.2041 | -51.9683 | 2024-11-22 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f6e4c503-78cc-38d0-a527-ca6ebdc5b715 | -2.504 | -54.1598 | 2024-11-22 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e9ce2f06-7550-3629-9c49-e3090c457ab7 | -3.4593 | -45.8881 | 2024-11-22 00:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 13705208-8830-3229-b3ff-7547c236026e | -14.558 | -54.7205 | 2024-11-22 00:50:00 | GOES-16 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| f8fdb558-dd2a-3656-b787-999e8ce1867b | -3.1831 | -54.3247 | 2024-11-22 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| ff012376-5011-3e44-b917-2e5faf348262 | -3.7554 | -46.1204 | 2024-11-22 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 0630f033-da39-3ca4-86b9-6dccc4591b31 | -1.1287 | -53.4153 | 2024-11-22 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| f6dbe9f3-d79e-30da-ae95-e62b0b9cfdcf | -3.5159 | -53.8132 | 2024-11-22 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 9bf5ba12-b772-3f03-95bf-feb085d47bfd | -1.1857 | -51.9685 | 2024-11-22 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f1582db6-92fe-3cd8-9420-2233587ef5aa | -5.9744 | -48.0413 | 2024-11-22 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 8709c3f7-b618-33ef-9ec5-8c5d0e469a7e | 1.3819 | -55.9652 | 2024-11-22 00:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| cdbe82c1-0d55-3b7e-9ea8-642a55650db6 | -1.1857 | -51.948 | 2024-11-22 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 62861b25-4447-3b09-81bd-417f3b0da715 | -2.5013 | -48.9949 | 2024-11-22 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| d800477c-0f80-3a47-8c27-35776c970366 | -3.4406 | -45.9111 | 2024-11-22 00:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| dd71ef7f-dd74-3f24-8ba7-aa8c067bdb32 | 1.3636 | -55.9457 | 2024-11-22 00:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 29d59ee8-cf3f-32af-971e-e414fac1f07c | 1.3819 | -55.9455 | 2024-11-22 00:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 91ace4f9-ee43-3144-ac4b-acc7a59c165c | 1.3636 | -55.9654 | 2024-11-22 00:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| c2957ca8-1c27-382e-826d-d7dd67c435c9 | -4.2424 | -48.6334 | 2024-11-22 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 79ae70a9-412e-3085-aee7-acf96cc83dbc | -5.9742 | -48.063 | 2024-11-22 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 2a1ff315-ddba-3f8b-bf5d-52e9330557db | 1.3636 | -55.9654 | 2024-11-22 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| e9eef020-9276-3534-abb4-bf4a9e72de7e | -3.7555 | -46.0982 | 2024-11-22 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 6f61a96c-ce19-3e99-8db1-46f507395cd1 | -1.7549 | -52.3913 | 2024-11-22 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 2abc2e5a-3567-3f96-a624-e83e8a14f6d1 | -2.504 | -54.1598 | 2024-11-22 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| fbc52eb0-fb1c-3de0-876c-a950c461895c | -3.4592 | -45.9104 | 2024-11-22 01:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 1368e260-9ed2-37a3-972e-2a8bbf429295 | -4.2424 | -48.6334 | 2024-11-22 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 1cb1bd59-1a15-3c64-bcda-3eec9a88de6b | -1.1287 | -53.3951 | 2024-11-22 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 66eee972-93f9-3a5a-ac96-1344f7d98817 | -2.5013 | -48.9949 | 2024-11-22 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| d9d226c3-99a2-3409-ba72-a232760555bb | -1.1857 | -51.948 | 2024-11-22 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 5a9eded9-d9df-36d2-9716-786d10a94e50 | -3.1831 | -54.3247 | 2024-11-22 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 1b8c1b44-9719-363d-b558-261d15625a94 | -5.9556 | -48.0642 | 2024-11-22 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 36984350-734f-34ae-96b9-b9c979f654f4 | -1.1103 | -53.3953 | 2024-11-22 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f0eac600-1e1d-3a8c-b82c-8e956496764b | -3.4975 | -53.8137 | 2024-11-22 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 0ed5c6ea-acaa-3c2c-9fe7-a997481c668e | -3.516 | -53.793 | 2024-11-22 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| d7c68496-d265-30a0-a9a6-a59123615baa | -3.5159 | -53.8132 | 2024-11-22 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 2ed1e5f8-8850-3a7b-b287-df1c7a6a2441 | -3.7554 | -46.1204 | 2024-11-22 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 94e062f5-7369-398e-b564-819c3cbe6295 | -3.3338 | -53.3334 | 2024-11-22 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 67db45b9-4913-3b0a-b7e3-6326ca3e695e | -4.2238 | -48.6342 | 2024-11-22 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| bfa3f45f-ea9f-3a1d-a00b-4d5985562255 | -3.3451 | -50.5126 | 2024-11-22 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 8e52c42d-95cc-322f-b94b-efea16ffe1c1 | 1.3819 | -55.9652 | 2024-11-22 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7ca6b362-a60e-3c37-98a0-dd3a171f1118 | -1.2041 | -51.9683 | 2024-11-22 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| d396a241-7081-335e-8fd7-c8e299794589 | -1.7366 | -52.3916 | 2024-11-22 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| a0763c30-73fe-38b1-aaff-52fd6d4b8eb2 | -5.9557 | -48.0425 | 2024-11-22 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| c31e4a49-629c-3119-a305-682d4dd40ad7 | -3.8355 | -52.2576 | 2024-11-22 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 1e8242be-3599-3807-b9b2-df4cb732bfaf | -3.3452 | -50.4917 | 2024-11-22 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| f3ab2dc3-96c9-33c1-9c8d-d8ec0fe5111d | -3.4976 | -53.7935 | 2024-11-22 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| f70c324d-28ce-31ca-85eb-628b4dcf1800 | 1.3819 | -55.9455 | 2024-11-22 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a7351f43-fff4-315f-b1be-3f6fe682f77b | 1.3636 | -55.9457 | 2024-11-22 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 8797179a-e22d-3fd9-af31-3423266f65e8 | -1.1857 | -51.9685 | 2024-11-22 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d1a43b13-69a0-3c3d-a7ea-bcfab285a3b5 | -1.1287 | -53.4153 | 2024-11-22 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 497220e3-6c82-30b6-8091-28148f4843c4 | -3.4778 | -45.9096 | 2024-11-22 01:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| baabc90f-f90c-3391-a176-8a0b5f6b44a2 | -1.2041 | -51.9478 | 2024-11-22 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 058a547a-50a8-3b5b-8b47-b5896a6ba5a2 | -3.23 | -54.19 | 2024-11-22 01:00:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d058bce-d643-3b45-8bdb-fabe08660d8b | -3.23 | -54.25 | 2024-11-22 01:00:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45b5a38f-c468-3b85-9df3-b0f35b8665b9 | -7.21695 | -45.08301 | 2024-11-22 01:04:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 58a279c5-c779-3881-b0b3-375d99c031b9 | -13.23912 | -50.89033 | 2024-11-22 01:04:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ed05544c-02b5-3251-bd19-a0eaf385b059 | -14.1012 | -51.83655 | 2024-11-22 01:04:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 482749f6-2bca-3607-b0ac-3617f446142f | -14.5577 | -54.73852 | 2024-11-22 01:04:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| ae3f0c7a-a8f9-37ff-980e-9c75c1606243 | -9.82338 | -48.16999 | 2024-11-22 01:04:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 47c575e9-7f42-3420-abf6-788abc2fe7b8 | -13.24038 | -50.89959 | 2024-11-22 01:04:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5403fa17-94a2-3894-ba48-0115dba3446b | -7.65209 | -44.51157 | 2024-11-22 01:04:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 320e7cfe-6f7d-3954-81c1-d938732e9d54 | -7.71303 | -45.67559 | 2024-11-22 01:04:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0e27af2e-0821-332a-b51e-f3f7b9462929 | -14.52632 | -50.81824 | 2024-11-22 01:04:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cd9ba2ea-59b0-3330-9735-fc0d33149a14 | -7.71875 | -45.66796 | 2024-11-22 01:04:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5b3814b5-5554-3551-abc6-e156d553fd5d | -7.71049 | -45.65882 | 2024-11-22 01:04:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| cf31d4d7-35a9-37f0-817d-5b0134f6f05f | -14.52505 | -50.80884 | 2024-11-22 01:04:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cabe3975-609d-31d4-988b-0a1054445583 | -14.55584 | -54.72299 | 2024-11-22 01:04:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 3ccee74a-86f4-365f-921f-bae1aa69e745 | -2.45888 | -53.69495 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e7246f86-bda4-3bb7-8a92-faeb5e628832 | -1.07774 | -53.36728 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 280589ef-d61e-32a5-b004-7b6b84909183 | -1.62745 | -52.41172 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1691894d-1847-37e8-b7e5-b7ed8127e745 | -3.23773 | -54.25913 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 801050bf-01d2-3a94-9c9e-5ef8e46af1d2 | -1.27386 | -52.98592 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a8bc2229-21c0-31fa-8a94-6dea0a5c59c6 | -3.50706 | -53.81856 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 83aa637b-03b5-3c54-8822-8195799acdb3 | -3.67601 | -52.37509 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7d75d6d7-fb55-3a09-a4c3-46314a5fb484 | -3.08401 | -45.424 | 2024-11-22 01:06:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 0f2a6a49-09a9-35e3-9e90-6c97e40fcbd3 | -4.24057 | -48.62517 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| cabf51e1-5628-3464-a621-8d7851a288c0 | -3.11205 | -54.29235 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| c52c71b0-7e20-3296-af88-516edaa0c459 | -3.41201 | -56.40825 | 2024-11-22 01:06:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1288d7dd-1dbc-33c5-be0d-456ec1d544f2 | -2.30726 | -53.59652 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 01b30d92-0822-397b-9614-cbc0121adec9 | -3.47047 | -45.89813 | 2024-11-22 01:06:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4d3d31c9-803c-3f77-ba8c-1f3d59491c57 | -4.01492 | -49.92498 | 2024-11-22 01:06:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9da30e02-1dd2-36d8-96d3-375ed3183103 | -3.09939 | -53.73489 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 36e23d21-322c-3399-aec0-ad15cb3ec51c | -3.53657 | -50.5215 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README4.md)
