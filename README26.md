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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d91ef93-bc64-3959-a4c4-db75ded45c50 | -4.16692 | -42.44052 | 2026-08-23 04:44:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bd4d2943-2d64-39d9-ae07-8d0179b3ef8b | -6.4423 | -56.05942 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f32da6c8-52f0-3736-af02-01caddd16598 | -4.79316 | -49.35809 | 2026-08-23 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c205d350-5c0a-3a3e-88d1-55c433044324 | -2.91471 | -48.86952 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0e9eae00-d1ce-3e9b-b2b1-f7a22888a195 | -6.77405 | -59.44837 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3777cd7-26e3-3598-9719-f19366ce2e65 | -7.14968 | -42.79058 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 87561039-bc24-30f2-aff6-67c0a3137cd2 | -6.67133 | -58.79472 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7d83846-19a3-3952-b472-91725f945c3b | -3.59513 | -54.04745 | 2026-08-23 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 468c1e18-8daf-31c3-b6ca-da952f7ac619 | -8.81764 | -46.62938 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7c6aacb-4090-338d-be3f-51ffd2d548d9 | -6.19188 | -53.53008 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d10d1800-c616-338c-9fdf-14d07860f0e9 | -6.67308 | -58.75051 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e65b72a4-9350-3f62-bd88-5fee21029497 | -8.92397 | -48.54363 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1706981f-2efd-34d8-985e-f8b3d7ca6ab1 | -6.5448 | -56.17825 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52af2c62-c316-39f3-877b-731f92d20936 | -6.94494 | -59.07013 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3236636a-095c-373b-99d9-6d49dd6792de | -6.80472 | -59.42006 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3675bab-ae59-300d-805e-310c0a03ad4b | -8.81683 | -46.61865 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3c6961a-961e-3b76-b437-6e536ac4f8d6 | -6.75833 | -58.67031 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd2b59d9-7158-3b9b-925e-a65853a9c9c1 | -2.53734 | -54.01295 | 2026-08-23 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da174101-911c-3b39-9048-26b2f46298cf | -9.45028 | -40.32319 | 2026-08-23 04:44:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| ebe0021c-f142-372f-a366-b3bf405e0439 | -8.58061 | -45.54689 | 2026-08-23 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e076f65-96c7-3fa8-8855-3d9fd30a79c2 | -6.8998 | -55.71045 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 905eddfa-368f-31bd-b805-6cb2b77b6f41 | -6.65975 | -58.74411 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 753649c3-185f-344c-aa2e-19bde999894a | -6.78245 | -42.67726 | 2026-08-23 04:44:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65e10607-a5aa-36ca-b72b-062256acf41a | -6.79519 | -59.80185 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8fabe726-09a6-3eaf-bf68-9a478b729bbb | -2.98789 | -48.95949 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6988adc8-1702-32ee-b875-40345003385a | -6.19387 | -53.51851 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87161635-4c53-3227-a398-70e506c24e99 | -6.23747 | -55.38132 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7f9596a-ca44-3d68-9722-3aeba29ae7c0 | -6.12449 | -57.85484 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c8e5271-833b-3ba1-ad59-8f09883a8471 | -6.96372 | -59.06905 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d854c9ce-4353-3204-9ed5-ea04ac932758 | -6.89593 | -55.70439 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e647878a-45c9-3767-997b-5d5ec93c1466 | -6.90223 | -55.70454 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0121b1bf-ada2-334d-abbd-628bb5bf5918 | -5.01101 | -47.07192 | 2026-08-23 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5e05525-ccde-3a3a-a73a-8b4dde72ffd2 | -6.95858 | -59.06339 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04d55f00-80ec-3116-b0ce-43faf1672d06 | -4.17501 | -42.44178 | 2026-08-23 04:44:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 33be12f8-465a-3073-b652-9aeee2480173 | -6.67388 | -58.73367 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 928fe118-6bae-3905-9674-efab164d6574 | -8.08605 | -47.25998 | 2026-08-23 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 780edfce-4aed-397a-8d66-01e67a950653 | -8.34939 | -46.50255 | 2026-08-23 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8809546-8005-30f9-bf97-ce7f103f6aa5 | -7.06354 | -44.98969 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71f0450c-af7e-340f-a970-7fc2d46a8311 | -6.79217 | -59.66249 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 62f1eca8-915d-3e5d-801b-cdb61ded614c | -6.96289 | -59.07355 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 768af40d-5c39-38b8-813d-45a1e83d591a | -8.92507 | -48.53666 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d459eebd-b100-383c-b647-8bfff413ecc2 | -7.52053 | -47.63724 | 2026-08-23 04:44:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d847956e-6108-324b-83ec-fe469e2a1d4f | -6.79749 | -59.66862 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f34e607-a17c-3e15-8348-9f2313095725 | -6.668 | -58.73251 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 295e9c64-dcd2-3251-8826-4ea30a1e1ec8 | -6.38042 | -54.96666 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32d629d3-6563-3e3c-b861-6a01819ef43b | -6.68936 | -58.72732 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19f0f3e8-1b82-374c-85a8-82e64ddab89b | -6.13894 | -59.91732 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e9530bb-aae0-3025-802b-041c7b7e30f2 | -6.18943 | -53.51872 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53d39db3-b433-3610-a96e-9b2ca438204e | -6.806 | -59.67603 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fd7d6b4-2d8a-31d2-8b13-5032ec6e7207 | -6.51621 | -51.45161 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb0c15f2-3ad0-3fc1-8bbd-d679fc5c4788 | -2.95992 | -49.26704 | 2026-08-23 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ba94db9-3719-361c-9aea-ab59772aab61 | -6.55429 | -55.10083 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 543db4ff-7aae-37f5-99fa-b77b09fc0adb | -6.86919 | -59.03609 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 337ee008-5927-349b-9e0b-4c8419987152 | -6.1242 | -59.9254 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82e5bb2d-b556-3d8c-947e-35415277a95d | -6.68422 | -58.72201 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 273241bb-342d-3ef6-bffe-2872205a5ccb | -7.15459 | -43.09949 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8c25cc56-1ad1-35fd-8ca7-d0d3036954bf | -7.05212 | -50.75235 | 2026-08-23 04:44:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e64b95d1-a74a-3977-89a9-bef858931ff3 | -6.66795 | -58.79869 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82b9f87f-c094-3e16-9648-9a841b75f0ce | -6.85725 | -59.41017 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8ae0d7f-15a9-3491-9e12-137fd5f667f2 | -3.70278 | -53.68833 | 2026-08-23 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 414aecf8-40e2-3524-8830-9be28c3aea4e | -6.18417 | -53.52476 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5828eb3-78c4-3d11-855b-7bd3f5a0a3d8 | -6.55653 | -55.10296 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd194c02-8472-366f-b433-ee8e2b048251 | -6.96888 | -59.07465 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dac762f2-c6cb-324d-9f42-89c1a96e2241 | -6.2265 | -55.61653 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3d8404d2-a825-36c2-9afc-6e9156fbf5e6 | -6.22557 | -55.62194 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a130b623-f115-39a8-b527-4b9ea62842a2 | -6.84251 | -59.45643 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffa8e645-72bc-3c63-8777-c6e7d6782161 | -7.18518 | -42.75005 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 39e9cec7-24d5-343b-9a62-7370af5ed2da | -7.74082 | -46.17245 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6027f0d5-2810-3f0d-8ea7-44bae0d72a98 | -5.30762 | -49.05248 | 2026-08-23 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0af2fc67-c118-3f5d-9817-1b450eccc45f | -6.76419 | -58.6714 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9eb5bed3-adb1-3b3a-84bb-ed73ad30a95f | -6.52426 | -51.44852 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1751010d-af4b-33d7-819e-9e116bf05883 | -6.76494 | -58.66724 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f15bc2c8-a0cf-3e37-a027-2d978a1b6276 | -6.79997 | -58.66282 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 72bd7017-dd68-3ea8-bca5-5e4b51235409 | -7.18217 | -55.41785 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b4547a5-189c-34ed-b57a-712784cfb83d | -6.82859 | -59.67477 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 41ff88b6-3af1-3785-8fc2-ba82f8bc2f60 | -6.82115 | -59.66404 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e3be8ae-120f-3f0b-b411-e134833c0ffb | -6.12516 | -57.85107 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ab880ba-7334-33d3-a9a8-ea16f9e7fffb | -6.80969 | -58.64293 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55663f0e-ef04-3b66-b60e-ce5ab87efc95 | -3.27015 | -49.52368 | 2026-08-23 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d17bc345-266f-38ca-90af-8ff320019f8c | -6.8104 | -59.68687 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4176447c-5b05-34a9-b3a3-435ec0f3d613 | -6.86337 | -59.41133 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a55f6cc-f5c2-327a-b100-468a4a19f9a7 | -6.79602 | -59.43276 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01047ca6-d07b-3a92-930c-129924efb6da | -6.19321 | -53.52234 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21fa94cb-048c-3096-b162-0465a7f877e2 | -6.69666 | -58.74224 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df26ae9c-251a-3cdf-a6fb-b0223e981fbe | -5.76713 | -57.5803 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1249ca1-ee6a-3fc3-bb96-3da5984bbd3f | -6.65534 | -58.80068 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 595b81bf-fd79-3934-b65b-57cb15a29a94 | -6.80344 | -59.65549 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5599f868-1a5f-3219-8a44-9ac2b5ff9e90 | -2.52322 | -54.88264 | 2026-08-23 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fa910a2-c6c2-387c-b4cd-c44ed5625e4d | -7.42537 | -44.6862 | 2026-08-23 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9431a673-60df-3747-b642-43f8fcd13cf6 | -7.80503 | -50.78296 | 2026-08-23 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e474329f-8fb5-367c-8a60-d989136dff43 | -7.26571 | -49.90744 | 2026-08-23 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d688828-3d0f-3c45-9c6c-0b2874f91031 | -1.74627 | -55.24967 | 2026-08-23 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31bc2e9b-cdd8-3d47-aef5-9a93404e86a6 | -6.83176 | -59.95583 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dcb9057f-ab12-30fb-a511-86e82ebbb434 | -7.73808 | -44.55653 | 2026-08-23 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d180f40-fb5f-346e-8bf7-dafaa1bc6d07 | -8.47019 | -46.98756 | 2026-08-23 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a5b6195-219a-3728-a071-d09860efa823 | -6.90026 | -51.56598 | 2026-08-23 04:44:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a527d0f-0934-3075-9e1a-019f7cd9e899 | -6.80451 | -58.64883 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 03ae0143-477e-385a-b1ac-70c3bd838663 | -6.55273 | -58.52207 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dca49348-2c4d-3001-a120-e0e9c851eac9 | -6.17045 | -55.56728 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a018a89f-6955-32f1-a3f5-03d96a6d35ab | -4.26754 | -48.19282 | 2026-08-23 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README27.md)
