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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6440ab6-6302-3896-af0a-b198a483fa70 | -5.4217 | -37.6138 | 2024-11-27 03:55:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd96ec95-1755-30be-a347-b41caefd068a | -4.00297 | -50.35355 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5971fc4c-0d01-3ce8-ae96-e9010540c9ea | -3.97072 | -48.07822 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 251f8433-48c7-3f82-9c15-92fd904bef04 | -4.20906 | -50.89893 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0f569d7c-b89a-3b57-94a4-3c932291ad69 | -3.97826 | -48.06782 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb5dfe8b-2c36-37ab-bc9f-1c807e54bb4a | -3.09235 | -51.0298 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a90905ea-7c92-327e-a6c0-7360c9dacce2 | -7.69022 | -42.96875 | 2024-11-27 03:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bcbc485f-4725-3bc8-b600-455a345bf266 | -4.04785 | -48.33186 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 288bdd30-7710-3c2b-bb48-3dbaee0692c4 | -3.44521 | -50.29707 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e19d9ba3-02f5-3f59-b4f1-38307dd5d8d9 | -4.65236 | -43.81709 | 2024-11-27 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77ce3504-e817-3c5e-9c21-bd8e3909648e | -4.65593 | -43.82158 | 2024-11-27 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0100edb0-73ed-335b-97d6-cb84d514f10e | -5.65282 | -46.6469 | 2024-11-27 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6eaa6db-a0dc-38ca-9066-0692613fcfcb | -6.68747 | -48.87257 | 2024-11-27 03:55:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a5f2ef8-b20b-3d8d-b42a-cd48b298f458 | -5.98689 | -45.36018 | 2024-11-27 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 33ff1133-50ef-3a30-a946-214b6e33cad6 | -3.96449 | -48.06529 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8fa0ea4-491e-36af-b135-26378ea0ecc0 | -2.69334 | -45.66286 | 2024-11-27 03:55:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 598901cd-16f6-3e1c-a064-2d46eea1d239 | -2.81361 | -46.82956 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e4877e3-ac77-3a40-8a1c-4acad30e538e | -2.86507 | -46.81416 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea526af1-73b7-3417-923c-39260f922bd7 | -3.16493 | -48.43549 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 323bd85e-4d02-3df4-abe3-c461d0e70d63 | -4.00281 | -47.91974 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68ab06b0-52e7-34a5-ae29-f071554380b7 | -3.00055 | -45.46579 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7e2c069b-459e-39fd-bc5a-fc21bc93d89c | -4.23903 | -41.92933 | 2024-11-27 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b96c239-8547-303a-a279-b00f7f480b29 | -5.58835 | -43.15549 | 2024-11-27 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 43982a7d-c05c-3c6d-a00d-596a6ed24ffb | -4.28422 | -37.99555 | 2024-11-27 03:55:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0be49d60-349e-3e3a-828c-de7f02600285 | -3.71809 | -50.18658 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15597414-4118-3def-9dea-583798c8df45 | -5.63917 | -46.96861 | 2024-11-27 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a89c70b-0132-3242-9c17-e610905b969b | -3.70993 | -47.66969 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 168d2726-09b7-3972-8c93-70aa53967833 | -4.16087 | -43.74266 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 143bdf69-f4aa-3dd5-ab2c-2acc3e6d19cf | -3.04992 | -48.51558 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f2949127-e3ea-3f6f-9184-e6bd14661096 | -3.97886 | -48.06416 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cc92cd0-71c5-3691-a258-cee66c80001b | -2.42466 | -48.54851 | 2024-11-27 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd84b9d4-cbf1-3dc2-9f79-871fb353669e | -4.14048 | -43.84338 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8aeed57-a6e5-30d7-8f6c-ff121a9d6d3e | -4.16167 | -43.74234 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14ec1d7a-5901-32c3-9d18-4512a12672a1 | -5.666 | -46.42402 | 2024-11-27 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bd1dea4-7761-315f-8af3-f8fc7c43e59b | -3.17736 | -48.43319 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 578d78a0-717b-3d0d-9bec-30878e1d76ff | -2.90148 | -45.38248 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e402fe68-8ddf-398d-8cb0-4e3be02e3f3c | -3.93058 | -45.84414 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9441d9ca-e2c8-343c-894e-aa66215d85e6 | -2.10384 | -46.55904 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97c50382-07be-3b0e-a8ae-71467eb1f529 | -2.81892 | -46.83036 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7179f31-83a9-3703-ba0b-c5e98d52f183 | -3.94815 | -46.91324 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8632064-c5b3-3ead-b22f-70bfb7ca9ecc | -5.86574 | -42.76991 | 2024-11-27 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f471441f-48d1-3187-9e6a-b69c2ae27f6c | -4.50215 | -46.60363 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0055ea38-0b29-3cdb-851f-bce598b346e6 | -4.22001 | -47.2163 | 2024-11-27 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 716dda8e-9f41-3258-a878-391bd932f99b | -5.69627 | -43.01329 | 2024-11-27 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 32e8a00d-94b2-35e4-8acd-da4f830eb0f1 | -2.68933 | -45.65664 | 2024-11-27 03:55:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b9beb2f0-9f8d-35fc-b874-bf4de4013758 | -3.94842 | -46.9141 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c204d06-480d-3f28-9019-4d64bc11589b | -4.14736 | -43.80034 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55b07946-2abf-3998-a80e-7f73869b89a0 | -4.21289 | -50.89509 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 19b80a2e-02fc-34d9-825c-46bcdfbbc0e2 | -4.44667 | -46.60149 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 684e9e9e-d169-3101-9f9e-c042ce3f3f78 | -5.58525 | -43.14975 | 2024-11-27 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 64f104e0-1951-3b62-9800-f7f116b50637 | -3.90508 | -50.60822 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c00cae4-9d91-393b-b57f-2b4ad38f7f94 | -5.90921 | -43.41014 | 2024-11-27 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61ef2188-7472-3521-8a4f-bb1ad1bd8340 | -3.33419 | -46.68025 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d9a20bc-7f00-37d8-a763-4978f986cee8 | -4.22821 | -46.88555 | 2024-11-27 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f75bca30-2e51-3e78-b0c6-0bc94cbf2f9d | -3.06539 | -49.19777 | 2024-11-27 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8aaba8f1-4a82-3d1c-8ac8-fe443b289a42 | -4.14188 | -43.80753 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8ce2e0a-3ad0-3bb7-bf97-f50ad6c32419 | -3.94087 | -47.98006 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed44e93a-3ea4-3e80-a28d-5250620881f1 | -6.82307 | -36.34537 | 2024-11-27 03:55:00 | NOAA-21 | CUBATI | PARAÍBA | Brasil | 2505006 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| deb3d39d-d3a4-304f-9ecd-ed6da99a8675 | -4.57402 | -41.04315 | 2024-11-27 03:55:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c1878bb1-2b36-3ebe-b5de-72b638eac464 | -3.50466 | -42.78287 | 2024-11-27 03:55:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4541f22e-c4f9-3cab-830c-0c6a0c1371dd | -2.80035 | -48.68361 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d8e8b72-4339-3698-9f53-f612966689ec | -4.02575 | -45.54149 | 2024-11-27 03:55:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 571a3de4-6c6c-3fb7-ab79-940afa7b0c89 | -3.91399 | -42.41278 | 2024-11-27 03:55:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dbf73c18-e943-35c1-b86f-fed8adb8d1c9 | -7.69702 | -42.97467 | 2024-11-27 03:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b8ff5f4f-8fdd-3310-9d0a-aef6cf63f6d1 | -3.35006 | -50.18933 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3001e426-ea73-3309-a919-93b465927ee0 | -3.50995 | -50.30648 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2691083f-2c88-3de5-9c1e-5514f3809866 | -2.68663 | -48.59427 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65ff3e5c-8787-3c85-97e9-4250a01cd6a1 | -3.13016 | -51.01819 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0b6c510-f545-328c-919b-023030da2c45 | -3.59539 | -47.34242 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ceaddd3e-7ee0-371c-80f8-279632db85b3 | -4.85175 | -40.75375 | 2024-11-27 03:55:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 76afd71a-34c0-399f-a026-92000c97d152 | -5.98533 | -45.36937 | 2024-11-27 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| d146d9e2-dad2-399a-89d7-e34fa0913c40 | -3.17647 | -48.44506 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d4888ed6-a7ea-3640-8d4c-82be92b41e1d | -3.24485 | -50.14155 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bf216d1d-fe79-3e84-b176-8f0084688fc9 | -3.28534 | -41.77601 | 2024-11-27 03:55:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7acc52ee-a419-3050-adf1-cc7cd568f0c5 | -2.70405 | -45.65892 | 2024-11-27 03:55:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0817b72e-8cde-3866-ad0a-b1f3e2897347 | -4.25312 | -48.67218 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b0e1521-60e2-3be6-b55a-4db25008a42b | -2.28618 | -47.91514 | 2024-11-27 03:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dedf9b60-c6ba-36f0-a467-457c4a75cdcf | -5.92748 | -39.81366 | 2024-11-27 03:55:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 91a44321-f2f2-35b7-923e-f09c5e6cfeeb | -3.00173 | -45.46248 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 82a3e190-245d-3e0e-bc31-bb7f8ba1772d | -3.69786 | -50.22599 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7caa2e03-ead6-3445-9d0b-f03c7404a1cc | -2.86561 | -46.81089 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d87753df-b698-3929-8663-8caf988d40cf | -4.21938 | -46.44983 | 2024-11-27 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14b027ca-d2f3-3562-9ac4-03b52302db66 | -7.68945 | -42.97339 | 2024-11-27 03:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9ac0b0ad-6d65-39e6-9718-fe48cb53a1d8 | -3.97588 | -46.64825 | 2024-11-27 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3583d39-1bc6-3d2f-b2ad-4d8c53df3962 | -9.76912 | -36.41987 | 2024-11-27 03:55:00 | NOAA-21 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c0b31678-4ac3-326b-9829-9e5d29d09b10 | -4.21885 | -50.8823 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 557aed2d-3d33-3c7f-bea7-c9636dbade9b | -4.18238 | -49.41388 | 2024-11-27 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ea20529-3ffe-3880-87e8-dacd286e5f69 | -3.51553 | -50.3131 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9477a43b-3d9d-3eb6-be1d-9c5d5a804c2e | -3.14944 | -48.53635 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc4ba73c-e7be-39fb-8269-a7f0581b9ab2 | -3.1898 | -50.82822 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60f8f27d-e049-34e1-b3b6-e0460780425c | -8.10992 | -38.95972 | 2024-11-27 03:55:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a1235ecc-b5d3-38d1-8db1-0dae3747f963 | -2.93074 | -48.63726 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc381df2-f952-3c21-91c3-8620ba7d71e8 | -3.27065 | -43.04317 | 2024-11-27 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c40c14c-f1c3-3c9c-980f-d13d741ad6c8 | -3.45271 | -50.29255 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d247d065-f75b-33d0-8a43-11b51a493e90 | -5.49969 | -46.2501 | 2024-11-27 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10237ecc-528e-3a81-944e-7061ea8f31ab | -4.23599 | -41.92425 | 2024-11-27 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e1e53008-aaef-3177-a159-556b2a1a532d | -4.17715 | -48.45359 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e63ef86-3264-3662-8be0-f306ae548426 | -4.70878 | -47.93075 | 2024-11-27 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cd50135-bb96-311c-9fcb-368ddb3ad39c | -2.8359 | -46.82639 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0386322a-0313-3802-9de7-b1a81ee93a6f | -3.97254 | -48.08586 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README25.md)
