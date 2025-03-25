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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efe47bcb-a48b-345c-ae84-47d2425af7f5 | 2.32361 | -61.28286 | 2025-03-25 05:21:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba8cfb0b-c737-3cc6-8502-05edaa63767c | 2.90177 | -60.46334 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9480b97c-d22f-3f44-b746-422f205a008e | 2.24693 | -60.69849 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68ada214-01d5-38fc-bc6e-1450ddb6ea80 | 3.32382 | -60.1063 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f616d182-8ce1-3996-8cad-b3e6853f4a2c | 4.25589 | -60.88907 | 2025-03-25 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1fb5a40-2d05-3bf7-8b0a-78cca992cc2c | 3.32326 | -60.10266 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92efb78d-964a-3f48-8ed0-073943b9a7ad | 4.06199 | -61.56944 | 2025-03-25 05:21:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2ab9740-a173-30c5-aa15-f74fb555b0af | 4.02092 | -59.936 | 2025-03-25 05:21:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| daccb597-ae6f-3e5f-b41d-4ca3baea5e7f | 2.31302 | -60.23738 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e7f3243d-fdd4-3069-ae5d-44deef05a04a | 2.91091 | -60.43158 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 13e0e0d5-9a2f-39fb-b8e5-cb8136c62427 | 2.57748 | -60.27167 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 042f17fc-edee-3c1e-94d9-c7b27601c84d | 2.90519 | -60.46282 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 50104089-4865-3565-9180-128c63313cac | 4.07483 | -61.58051 | 2025-03-25 05:21:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 637d1850-8c7d-330b-96cd-2cc22454639d | 2.58088 | -60.27114 | 2025-03-25 05:21:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9d7f328-698f-31c4-85f8-ac60370b4935 | 2.90464 | -60.43632 | 2025-03-25 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78af5b45-b9aa-3a7e-b4bb-5a08f9d9bb8a | 1.74627 | -61.06704 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 807bef2e-0679-3db9-a6ea-a57d07cf2dfc | 1.66907 | -60.1379 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da76e4aa-4cf6-3370-ba9e-ed3165cd3a49 | -3.26049 | -49.13908 | 2025-03-25 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 106aa06c-43e2-3218-8d85-641c71626bef | 1.10664 | -59.47231 | 2025-03-25 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81efa6b9-f877-3189-97a0-23e1bfa4aefa | 1.36258 | -60.3787 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c2f7f69-8115-30e1-83a3-39edd90b8645 | 1.67579 | -60.13686 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19e4b556-fd1e-39db-beaf-7f07f8b8c529 | 1.67634 | -60.14043 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1241f960-6e29-3363-a120-28adccf5b97a | 1.52571 | -60.70843 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30a60330-2d66-397a-a37f-e4d39ddbd175 | 1.1102 | -60.54309 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70fec911-a9f7-350f-9a04-3d39e6fcc751 | 1.10681 | -60.54361 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e2069c2-cfdf-322e-8f17-d8cc92804863 | -3.25521 | -49.13375 | 2025-03-25 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58159b91-dd01-3237-a03e-f34b0490964f | 1.52628 | -60.71214 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 850ae0fc-d067-3564-8b8a-07dea4b6a3bb | 1.11189 | -60.24514 | 2025-03-25 05:23:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 547bbbc9-fa08-390b-8d89-ff509e960ce0 | 1.6618 | -60.13536 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37365e26-6c43-3a2d-9130-9fe41e997fde | 1.65844 | -60.13588 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c63c97-4c2f-3583-9e70-aed06949a3a6 | 1.23861 | -60.10237 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12c2aaea-cb8c-3fd6-ba28-32669b5f2bb6 | 1.53483 | -60.10723 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4530cef2-6fc4-33ad-a759-7bb37a4a1de3 | 1.66125 | -60.13181 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca92a2c9-c49e-3695-9c5e-221fc8a79fec | 1.52913 | -60.7079 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7971093-6aa8-38c8-85c2-cb99a9e25ab8 | 1.66516 | -60.13485 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42abcd80-2658-37c1-8a55-81deff25225b | 1.65508 | -60.13639 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a81b28c-b61d-3ddb-80c1-a3ba7f6ef9c0 | 1.13733 | -60.06343 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ccc76dd-b728-3213-a23f-987fde362000 | 1.53202 | -60.11127 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb3fa261-1a26-3791-ab1c-c006612d378f | 1.10718 | -59.47576 | 2025-03-25 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70510fa1-dcbd-345d-8f6f-19587e8ff3fd | 1.33313 | -60.71151 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e89c1189-6505-3235-b0c3-e89091bd8208 | 1.38109 | -60.79494 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81ae05df-5809-3583-9103-21feb0e21659 | 0.78 | -60.58615 | 2025-03-25 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26f43fd9-b780-3e00-a168-de88035ae352 | 1.66235 | -60.13893 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 026d63be-8421-361e-8f26-c7d42f9501bf | 1.38167 | -60.79865 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b209939-f054-3e08-b19a-34630eb093a8 | 1.65899 | -60.13944 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed9d03b2-1cb7-3983-b9fa-33cd229b2823 | 1.24196 | -60.10185 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0628874a-a81e-3963-b101-d63809283064 | 1.11398 | -60.24479 | 2025-03-25 05:23:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e383d9fe-dd8e-3dde-a060-9748219012c5 | 1.36596 | -60.37819 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d48f61d9-a4e3-366d-8ef1-2a3201d0b3ae | 1.37767 | -60.79547 | 2025-03-25 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf03c045-82c3-3b25-9fe7-c7d7a857e2ac | 1.93608 | -60.59372 | 2025-03-25 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54ba15fe-4ca2-34ea-8fb0-3b1249b5a9e3 | -22.19504 | -57.08652 | 2025-03-25 05:27:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e52b60f5-218f-3118-8086-c172eb03e500 | -21.88483 | -56.11505 | 2025-03-25 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76087384-fe58-3de0-bca9-01e7be12b25d | -22.20724 | -56.97307 | 2025-03-25 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea15eb98-7722-34b4-9360-9b335035d6ad | -22.20705 | -56.97092 | 2025-03-25 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e89ce5ad-d18d-3b6e-98e6-56a86e92c96c | 2.27402 | -61.22554 | 2025-03-25 05:46:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c4de026-c534-3808-bcb7-0270d50002f2 | 2.24751 | -60.70106 | 2025-03-25 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1dda657-fce1-3897-a819-7522c9aec944 | 4.25762 | -60.88935 | 2025-03-25 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3da7de01-543f-3516-bfca-434229395922 | 2.90118 | -60.46336 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3f49dbcf-06d1-35de-9162-89558b73178e | 0.77108 | -60.58615 | 2025-03-25 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e4a2a06-c7c6-3cdf-a18b-3ccf97ab667b | 1.5264 | -60.70651 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79cb1d38-1624-3c45-8123-608386a14cfc | 1.2421 | -60.10294 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19006020-bbe4-3398-8c9f-ad7cb8a28742 | 1.38049 | -60.8014 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 840fe516-9020-36fc-9933-fe75be42e99a | 2.67398 | -61.41384 | 2025-03-25 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a79c5129-c3d8-3e41-93c5-665b68361c29 | 2.91119 | -60.42786 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07168749-b8ef-3848-9040-99b52a17eda7 | 1.36592 | -60.37896 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5390a4e3-5437-3097-98e0-7b9073a21fc5 | 3.32373 | -60.10626 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39c1c29f-8105-3670-8619-cbdf10796d12 | 1.11189 | -60.54245 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45c6d994-08ff-3822-99a6-a82cc3b02a3c | 1.37975 | -60.79669 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e01656a-4b76-35ea-a496-1b568520d500 | 3.6141 | -60.76193 | 2025-03-25 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6695d81e-7978-32a6-893c-ee1a0c370a33 | 1.23809 | -60.10358 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a535345e-af5e-337b-9044-622b84439ea6 | 1.36198 | -60.37958 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58c30c0d-a876-35a0-92fb-3709bec07e79 | 2.90427 | -60.43383 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 565707d2-41cd-3ea6-8bda-d672795c17df | 1.7468 | -61.06764 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce83f6ff-4674-3448-b048-2b2d2e8fc47a | 1.65958 | -60.14012 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cd2e650-deaf-3bb6-8281-2da9bbebf770 | 3.32295 | -60.10138 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a9d7a08-063c-3227-922c-c364cd3c040a | 1.65875 | -60.13499 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aa38559-3794-3191-9234-20321d0daad3 | 2.89811 | -60.46867 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c3229490-30c7-396e-af0c-a4e706b199e0 | 0.77892 | -60.58494 | 2025-03-25 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 739ed7c8-85c1-32e8-80fb-2cfee9fc2dda | 3.70472 | -59.93539 | 2025-03-25 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c4fb6f1-2138-3059-b7b4-35bb65741ee2 | 2.90501 | -60.46275 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 461becd5-ddef-33f0-8af2-121a8dd6d219 | 1.52716 | -60.71123 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2104866-619d-37cb-913d-0e7f709c0024 | 2.9319 | -60.43423 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a8593d7-0317-3f1c-9bd1-ecbae9b71eea | 2.57814 | -60.27588 | 2025-03-25 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8209a5f-4774-362f-a550-fb6e4b3d59ad | 2.89735 | -60.46397 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0cee5216-5556-3306-b1ce-707ad65bbc54 | 2.47695 | -60.61253 | 2025-03-25 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1e5b297-3ac0-3c78-aa90-c8f08f197773 | 1.10797 | -60.54308 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49854dfe-cfe5-34e6-affa-1738aa848c76 | 1.52331 | -60.71181 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4b118e96-8e77-3750-a9e3-3bdd92172d68 | 2.24142 | -60.71155 | 2025-03-25 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c142db1-bd82-334c-af9a-27a6799b172b | 2.51967 | -60.99404 | 2025-03-25 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92ee8e14-a80b-3f22-b21b-b18756c04313 | 2.58126 | -60.27038 | 2025-03-25 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05be3f3a-249d-3aa4-b045-667ecb846cba | 2.90735 | -60.42847 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0d6e595-c70d-3b7b-a350-c2db197b82cd | 4.02088 | -59.93599 | 2025-03-25 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e306338a-6705-30de-b62a-8b7ed0dc76b2 | 1.53427 | -60.1073 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3156659b-4412-3dfa-8546-c4d1a564817d | 1.38359 | -60.79609 | 2025-03-25 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0fa2611-97e8-3d14-bb84-0df11d6ed4d5 | 2.90884 | -60.46214 | 2025-03-25 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d4795971-3286-3e7f-b02c-b03321f0eee4 | 2.27472 | -61.2299 | 2025-03-25 05:46:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b14ec88-0533-3536-ab97-ec43124d4d67 | 0.78284 | -60.5843 | 2025-03-25 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73e2fcc0-2253-3168-b612-c494957ccf51 | 1.93674 | -60.59354 | 2025-03-25 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a510ef64-b995-34cc-bf5f-3f9e05f1b0b6 | -2.53631 | -66.6888 | 2025-03-25 05:48:00 | NPP-375D | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 295ed178-33db-318b-a33d-f0ed8f00d4de | 2.90026 | -60.46833 | 2025-03-25 06:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README7.md)
