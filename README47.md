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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1217e33e-2dab-3a1c-ad65-b7ff17fc4dc1 | -1.72362 | -52.46353 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4aeaa737-8c6e-3b98-adb1-d02285c177ae | -2.89543 | -48.2949 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0fdb2cc-37f2-3280-9fa5-182838f323cc | -3.2813 | -53.678 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8284f410-08cb-3df7-b127-ef1af18803bf | -2.39773 | -50.31815 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fc295d5a-d3b2-392f-a442-ac0f16820a3f | -4.71854 | -50.84612 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 415c11ab-b41d-3cd8-a850-04a7130cdafa | -4.21551 | -48.60867 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30491d01-cb08-3b5d-a094-3a116408b263 | -3.01509 | -51.04123 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f195405c-f67a-3940-9f5c-53ad201abb2f | -4.81918 | -44.35482 | 2024-11-10 04:14:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3ffaacd-8762-3d74-aeab-6d903081f406 | -5.36007 | -43.42577 | 2024-11-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34a5298b-27bf-3e29-9b0d-10226d27ddf8 | -1.62297 | -50.68686 | 2024-11-10 04:14:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7f85745-0eca-323f-858b-4e64c1bd51ed | -2.8499 | -51.96037 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 15c8fec7-15a0-31b8-8f31-b5358285bfa5 | -3.24528 | -50.31166 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f6e836f0-595e-34fc-a217-2f0f979e0848 | -5.37232 | -47.91879 | 2024-11-10 04:14:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 753df4df-fb39-369b-9641-1540fd76f20a | -2.1274 | -46.39035 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1656a8b2-f779-3d03-8b83-2bcc9d3718a1 | -4.10805 | -49.12215 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1ece326e-355e-3c7f-83c6-24eb00dd21dd | -2.20312 | -47.74258 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 275b0875-fd48-3d84-82ee-fdef39700dab | -2.51063 | -50.1978 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4ea9ba2-cb96-3b57-b1b1-35624d5b8e6d | -0.04212 | -50.76925 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ca3c65a-3f76-3a9d-beb8-285e546d7896 | -3.74026 | -44.53738 | 2024-11-10 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5dee648-6a77-3b8a-9613-53fec7b31410 | -3.92277 | -47.95037 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b5b161f-789d-30d6-9bc0-859d5b3b36d2 | -2.48989 | -47.22923 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a7f9850-f03b-3ef3-bc79-504e1d04f1fc | -6.20755 | -41.66413 | 2024-11-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6dc442d6-d4a4-30ec-a74d-de6c7310b925 | -2.12121 | -46.48006 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8f1c3d0e-89b8-3069-984b-bba26e2d06bd | -5.86635 | -44.16631 | 2024-11-10 04:14:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd6999ff-4579-3deb-9fb8-b43a0ab38d3e | -4.07436 | -47.96742 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd0ca9d2-a3f2-34f0-810a-5eb5f52edf09 | -5.47282 | -41.64777 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cb75aa46-a50a-3f8c-a00d-b631b9d57fdf | -3.96368 | -46.70466 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca51a632-946a-3458-bc80-d17f959722d0 | -5.8301 | -43.89848 | 2024-11-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2104d2b6-f478-3e5a-8a0d-6eeb01708e47 | -3.63908 | -50.18436 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d019b3ad-3808-3137-919c-6890639294ad | -4.20722 | -48.12708 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 880629b3-adaa-398b-b702-56b95112f233 | -2.5436 | -46.31063 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9038c742-3bd8-30df-9d91-6096793d3d39 | -3.23798 | -45.38418 | 2024-11-10 04:14:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4425dd5-cba2-3a6b-a15a-0968050e6d4d | -2.87479 | -49.45226 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a11bc24f-4d83-3759-8712-3dcc11569223 | -1.14844 | -53.78646 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3acf3ff7-1d20-39f0-ab43-b97874a7224e | -2.39507 | -49.07547 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc724922-c249-3c3e-9030-0c838905fb48 | -4.46259 | -45.86957 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4528750b-2054-356b-a6a9-a6dbbd77db0c | -4.43348 | -43.92999 | 2024-11-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 684c294d-569b-3b30-a9f1-377648ab4d98 | -3.21926 | -50.31853 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6587764-87cb-39eb-87c6-8da54633f492 | -3.96021 | -48.17959 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| bd1e4408-fe76-3c6b-8b91-7eab26a46353 | -1.54513 | -52.21469 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b0d9a6a-14b1-3f34-a0ba-d737df904b57 | -2.28849 | -48.42588 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1243462e-bc13-3ba4-979e-d876661cdb97 | -4.53834 | -43.56615 | 2024-11-10 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fff4992e-8555-3410-a0b8-83b8f750c240 | -2.66625 | -46.78133 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cda3e42-938a-3cfa-b6b3-c60393942d0c | -2.07738 | -52.04646 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62506563-89b8-3123-b8a3-a61f2d4755f2 | -3.2222 | -50.68246 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1bbe59ed-5f7d-377e-a9d7-ca39d7ebb9b2 | -2.71665 | -49.29572 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| df7d314a-76db-3583-9a2d-670d533a4b49 | -3.08989 | -51.11414 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13893b7c-3c22-3dbe-aa81-f03f2a80ae81 | -4.43309 | -47.25734 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b87f6dee-a91e-3ed8-aaa6-c1902fe82734 | -3.22136 | -50.27498 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| e02a9b25-d82a-334e-a58e-700f9e568cfb | -4.31242 | -45.49231 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e77e73c1-8592-3ad8-9aac-1bf0ac888fb4 | -2.47115 | -48.44515 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3672b4a-96a6-3112-8218-adebbc8fc39f | -1.40109 | -52.3655 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d1007cf-f08e-3143-b6fd-4c92fe7b6048 | -2.31793 | -50.67515 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c85aa04d-0d4b-3e7c-bd39-65c9bd97fb95 | -2.8899 | -48.3022 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cd29eb0-de0d-3a74-a104-fcf9a0a5a527 | -4.09914 | -49.12229 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e00e82a2-2f45-3a57-b613-eb78074d8eea | -3.95885 | -49.01264 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e34c031-7f5e-3c3e-9dc3-83823096c251 | -2.14252 | -50.14202 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02b9148e-c604-31dd-a2c1-e31509e88a68 | -1.86967 | -50.78854 | 2024-11-10 04:14:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7a23854-63f1-3b4c-b101-cd831c9960f4 | -2.8647 | -50.32185 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 79c7fb70-f3a6-3c70-9ebc-94a15a1d3b66 | -5.31281 | -47.68638 | 2024-11-10 04:14:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7dfe7367-e0d2-32fc-9e07-45538d9555b9 | -3.89549 | -50.30036 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b548aafb-dc3f-34b5-93d3-ffe350b55d0f | -3.17691 | -51.30775 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c8bacc2-4d7f-3894-a932-a8c6e1362982 | -3.62557 | -50.61371 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 95533252-ec5f-3bbd-868d-b888a0363003 | -3.20863 | -46.5 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 985dcbbe-7988-3ff5-9fe6-adce1f5b99ed | -2.30243 | -46.7214 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bab5c3a-00cf-3e6a-81dc-aa9837519223 | -5.50751 | -41.68264 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 448e94c4-6f89-3268-9897-acac9539597d | -4.22039 | -45.45447 | 2024-11-10 04:14:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dace8979-9baa-3896-9b1d-d7a9d44ea95e | -2.87595 | -46.65826 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b11ef7d0-267d-37a9-8244-32591fd82929 | -2.87253 | -49.43732 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9d2f1818-f66b-3567-9dee-4c9c477856d4 | -6.83127 | -40.70217 | 2024-11-10 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d7787ece-2935-3678-b4a2-d220742a276f | -5.53048 | -41.68984 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 83306212-6c6d-3d7d-ae3d-77cd433688ba | -2.94418 | -54.6825 | 2024-11-10 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf19585a-4c39-3e2e-b2c2-b5c01ac9399a | -5.69567 | -47.01689 | 2024-11-10 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe9556e4-69d9-36b3-bdab-e12d4f95a269 | -2.8968 | -46.82228 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4703b4f-6c46-3aa1-9b8b-35761a8691b5 | -4.73063 | -43.25224 | 2024-11-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e67eaa52-84be-33ee-9f58-b181cfa36e51 | -2.6763 | -46.79279 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bd09c18-9235-3ed5-84d0-aee4cc88a822 | -4.88372 | -48.5847 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c3371d8-efcc-32d8-a41a-653fde1bb272 | -3.8245 | -44.8479 | 2024-11-10 04:14:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e213f0e2-07d4-3411-81c3-cb71a7d6479c | -3.82523 | -55.66884 | 2024-11-10 04:14:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5a00346-f611-3692-b0c2-600da8ce194a | -2.7 | -51.69434 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fcb0530-ef7d-391c-a298-f132e14b2496 | -1.99298 | -46.35654 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9c89747-38ba-3597-bbfe-3fa58d41e68e | -3.53717 | -50.32722 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fc9d37f-8779-36bd-bf33-40a33df52194 | -2.57409 | -50.68259 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b5a7cdc-9eeb-35fa-b7e9-1b92b1997a5c | -3.66923 | -54.6604 | 2024-11-10 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dc50f6bb-a2ec-35dd-8349-c031ca46b398 | -3.92382 | -50.24829 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88a7ecd4-604b-3ba9-92fc-02b6597d2b56 | -5.83798 | -45.86601 | 2024-11-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 642d580c-36db-3395-bf90-259e8431c3fe | -3.94604 | -48.16229 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e137cfb5-74fd-3798-9a71-ef93b2132958 | -3.04151 | -50.32956 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71c83821-4f99-313f-a8db-d5d19cb05440 | -4.02787 | -43.61046 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4180c0e-627a-3fba-8ac1-6dda736e7731 | -2.76613 | -45.04154 | 2024-11-10 04:14:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b17f92a3-95c4-3734-b218-455cfda01a4c | -1.5121 | -52.15059 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bdc5d2a9-a003-3e7a-a765-75011870e3ef | -4.92565 | -45.36061 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d14f7e55-a98b-3eaa-8bd5-7168b9c0aba2 | -3.22898 | -50.32008 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d16bf82-97b7-31cc-acb6-ad97e3762388 | -2.65457 | -48.5578 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b38607f-4df6-388f-b932-20302e5d6f60 | -2.63916 | -46.80186 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63ba735e-a587-3115-8cb9-1cee6ad2ce46 | -2.20341 | -48.36321 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24b392a9-fe3e-3a63-aabf-5e2e27bf93df | -4.05913 | -49.28657 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7a3c9c27-3bd1-3e4e-9fcc-bb9ddb0a6185 | -6.44913 | -42.74525 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e7bab10c-35e9-3cc3-b27d-945d8765f779 | -5.59151 | -41.69553 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c5363337-bf8d-3b58-8a2c-23d340151a52 | -2.62401 | -51.29478 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README48.md)
