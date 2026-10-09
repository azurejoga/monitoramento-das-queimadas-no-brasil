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

## Dados Diários - Página 202

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb1718ff-3f16-3749-9ba3-5ece71c48e40 | -2.98473 | -54.07973 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3c87ee7-20a8-3422-b26a-95c429a0f1c8 | -3.58092 | -54.65551 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64e7f261-5741-3185-b8ca-60246b2a11b6 | -3.6813 | -60.63696 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6469d197-e36f-30ce-b722-82fa0d00548a | -9.00667 | -45.94512 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cc53a81-b565-3900-a24f-c85790cb7d1b | -11.87588 | -47.38719 | 2026-10-09 05:23:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a8623832-b7a4-3840-85c8-2b6154fc3e60 | -2.50328 | -58.06881 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9830eb4-d782-3166-9b97-f1404bdc7571 | -3.09008 | -53.94532 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cec489c-8e78-3ab0-bc10-deb7ba5858b9 | -3.54985 | -54.67661 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2cc6ca9-cf42-35a7-ae2a-eddbf82dd68d | 1.67892 | -55.63559 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76ca9ab9-6bc3-3677-982c-0cb158efcf04 | -2.85282 | -59.12073 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1182d00c-97a4-3322-9849-05ae1bb4e012 | -3.099 | -59.1949 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e981b54b-8894-349b-9fbc-d3a6aec9502a | -3.387 | -59.5202 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc5290f1-3d4f-3258-9f7d-e83740a9ae51 | -2.5094 | -56.32737 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 81adb698-7274-3ee4-9c32-e88a9cc1349c | -2.93452 | -54.04768 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48566015-d101-32a2-a894-fb7aaa4dea29 | 2.26383 | -55.98412 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c79071e-8cf0-35de-979b-876645272c12 | -3.62323 | -55.50162 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 775de6a5-b038-34f9-83d1-9a7260829752 | -3.43175 | -56.94569 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17620668-96f6-36c9-b295-914ad7a49bc0 | -4.66541 | -49.23124 | 2026-10-09 05:23:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3e197af-8e11-3491-b231-3e22d9ef8e51 | -3.08216 | -54.29892 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18bdd281-d37d-35ab-9eb1-ecf3cb449c26 | -2.94084 | -54.16022 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13ce7225-2702-35cb-b5aa-081dfecdc0ea | -3.17331 | -60.65929 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2db8e6b8-8c22-3fbf-9cd6-35c4a275d43d | -3.90222 | -58.95318 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a52ee5a-be74-39ed-95cd-1c97950aabb7 | -1.38697 | -55.19994 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3896c6bd-0ab7-316e-8d32-de02f1ae358d | -3.46992 | -60.25004 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a63d68d4-b3b4-300e-be8e-8bcbaea2f580 | -3.16526 | -50.45578 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 603e0f2c-80c3-3414-b72f-a98e6d5d72d1 | -9.29322 | -47.47263 | 2026-10-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71c30a6d-2bd2-3a1c-9ca9-0a6ce2c76d60 | -3.29275 | -54.01012 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 239068af-31ff-317f-8933-4218a422f12d | -2.94561 | -54.18004 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16939f6c-0cda-3fd9-89e1-594bb1daf47c | -6.45086 | -59.95276 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e591826-100b-3a0c-9115-fef01dce41d9 | -1.6425 | -55.27784 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68ee7edf-254b-3e2b-8d04-d8ae27ed7ec6 | -2.91286 | -54.11248 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c12bd5d7-e599-32e5-ae49-32b262f0d92e | -2.51358 | -56.25604 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83ac3ae0-9a02-352d-8b85-794c8f15036f | -3.31001 | -54.05241 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93bf3002-2a12-338e-955a-99cd021d35e3 | -2.95057 | -59.08207 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0ae494f-ff9f-33ed-8ad2-e266db1ca818 | -3.97585 | -56.11681 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a00b9580-9d1e-37cc-b58e-432466fa1076 | -7.56809 | -61.54375 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e99c3933-e73c-3e9c-a4b4-7b50f0137018 | -3.3185 | -54.04876 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16bc203a-e112-374f-9b44-6046547ba57b | -2.46804 | -58.01065 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f04a527-5afd-3f56-8144-4695f0097c3b | -2.50405 | -56.18206 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f627b9f-c05f-33c8-9dd2-92e2592c7c38 | -1.13163 | -57.28821 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ebab828-75f1-3a25-9f0d-2405558a93dd | -3.08348 | -54.26582 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22e16322-8998-3d99-95cf-1852e8398ba9 | -2.02613 | -55.62739 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c728c96-e9f0-396c-8ae3-eaa1620f40c7 | -2.34139 | -48.86299 | 2026-10-09 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85d5dd6e-e938-3cb9-91d2-93733d3ed209 | -3.66486 | -60.60738 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 990442a4-8a89-35ed-a1e4-a78de3f3d55c | -4.08495 | -48.96469 | 2026-10-09 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44700b7f-d0e6-31d7-8d72-c5773690b759 | -3.07768 | -53.94843 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 934efeef-08b9-3235-bf09-b0d7a8b6fa57 | -2.46607 | -56.0922 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0854bdf-ebbd-31e2-8923-191a11af41b9 | -3.59872 | -61.64407 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 034bb24b-a09b-3456-bc76-31323b11f0d4 | -4.36421 | -55.64448 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00b62853-54c6-3ab2-9634-1e53fc04c228 | -3.29766 | -54.05544 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81b0c1c3-b84b-322d-bdd6-5eb374665711 | -1.1145 | -54.17458 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab158dd4-5695-39bf-9667-6927abe7c8a5 | -3.62323 | -55.50163 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faaf3fb7-847e-33ba-a9ab-086ecadc97f6 | -2.21972 | -55.45144 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1aafe464-affb-3579-9d46-325a0726b1ce | -3.39045 | -58.21608 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75e0262d-579a-39ea-84f8-ff47837c0c49 | -6.85723 | -59.04347 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eae12e0b-6aaa-3c1a-904f-55e5ce12dbf4 | -2.745 | -54.10109 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4f33f68b-eb4d-3486-860c-d8f3886f8062 | -2.76341 | -54.10866 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1decc983-0633-3933-b38a-5cab55b867ef | -3.50809 | -58.65373 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbd5a816-9c96-378d-b4c2-c3cca58e508c | -3.28071 | -54.06274 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ad10ffa-5bd8-3278-98bc-74c91ceaf0a6 | -1.5346 | -54.5495 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38b0bdba-8025-368a-a00f-d51ef9966e07 | -1.32955 | -56.40562 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94566fad-fd27-3842-b18e-3bb651bde7ec | -4.57484 | -54.96028 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0ee7d222-55d3-3e0c-8cb0-9ffc6ed21b15 | -4.33042 | -55.01638 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4155b087-f4ce-3f4f-bc98-d9edae0ad473 | -3.78134 | -59.19965 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a75bcab-5f54-3878-ad21-fc4753f29ab1 | -2.93659 | -53.92203 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6deacc7b-e95a-3334-a8df-145b5b59cecf | -2.22478 | -58.10938 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 144467c8-8b9e-3495-b199-e37848704372 | 0.53175 | -50.9031 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b1a6f155-8884-3cf7-a174-7063dab369b8 | -2.76798 | -54.10454 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce799ef3-3d3e-384d-b9e7-7c60a468e8b3 | -2.54839 | -58.04064 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4162fbd5-7a85-3cb2-bbb2-05dcec81f321 | -3.65568 | -59.7075 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3af63543-3bc0-3410-9df4-936a5ddcd0b2 | -2.08409 | -46.5813 | 2026-10-09 05:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e82acb7-694d-3bc1-ba2e-a38361f73e58 | -3.10091 | -53.77063 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d68deb84-8048-362f-b12e-190a5901dd6c | -6.44476 | -59.94822 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2245e11c-d1c4-3293-8ace-551a5831734b | -3.52803 | -59.57492 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8de8b379-318b-3e8a-afd1-d4f2f627e155 | -3.74639 | -59.41899 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4a815ab-c26f-390a-b8b0-8f17baba38d9 | -3.45381 | -59.55243 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4df76760-8dc4-3ec4-b39d-e433db2905d2 | -1.72643 | -56.06844 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91490479-94eb-301f-b1e8-a05702a373ac | -3.05606 | -58.97466 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99b6095a-57a1-33ae-a409-24764e47fc5c | -3.30452 | -54.0367 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce552988-4a9f-356f-b12e-00abb3affe30 | -3.11428 | -54.16969 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eed21738-97f2-3236-904d-bb13d8fb2ed1 | -8.96706 | -45.91375 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f8aa0a2-4b87-3346-9b02-809b11d250ac | -3.71898 | -60.16216 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49adb400-c4f6-3079-8c8c-6f0ade8295d8 | -4.12507 | -54.25891 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0301e306-23c8-30b4-a8e0-cde74e8f2727 | -3.02152 | -54.04628 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e644bce0-7e72-3e82-9a25-4ac168820d18 | -3.78912 | -59.32203 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42743d0c-e29d-3eb5-8d6d-6310bbdf78a2 | -3.75134 | -59.49514 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da209039-0e30-3415-b503-11e2af5818ec | -3.77731 | -58.58373 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9754d73a-85f7-34c7-ad9b-f14728faed8b | -3.53186 | -55.43802 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fb5cc3c-91cb-34d7-a7a6-d2687ff868dc | -3.74645 | -59.31172 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 973e3a75-19e4-3fde-adcb-36fccf2c873c | -3.28648 | -53.99921 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f258ad00-1c18-392d-8faf-4874728c33df | -4.82101 | -45.83628 | 2026-10-09 05:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2b5c5663-d89d-30a5-9871-853a6cfb1bd6 | -2.88688 | -54.18069 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91bf1e51-ef00-38f6-8711-00ba97766e1a | -1.09135 | -54.10259 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d7a7683-c172-328d-a139-e3c4a045233d | -6.99423 | -59.101 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59a84359-15a1-358b-93fb-275d94237a95 | -3.29318 | -59.40489 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fb33ebd-4c8b-3e95-a914-640b8e8d76f7 | -3.25034 | -50.39463 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ff56c61-3dfd-3de2-9598-68dd870d0990 | -8.84004 | -61.46739 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6de4722f-0aad-32c2-9732-f6bf8d4d6d00 | -3.48079 | -59.50611 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e30eb6c4-ba38-39c2-af71-734fa1d865e0 | -2.98695 | -54.06544 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7331138-8165-3cb7-bb76-f513d5b49aa7 | -2.99834 | -57.75148 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README203.md)
