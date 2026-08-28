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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08ae470c-b802-37cb-8853-86488ff3495f | -8.82756 | -70.55134 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6304bad3-94f2-33eb-8f2a-bb842e8e576b | -8.65385 | -70.67084 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 16.9 |
| df836eee-7a35-370a-8656-808e899d7ba1 | -7.58924 | -61.31748 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6e71e1bc-2240-361d-b33e-f7908dfe8833 | -4.90318 | -57.51797 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 49f718fc-622f-3627-969d-163021519f87 | -7.48401 | -61.40653 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d5fe7dbe-8bd4-3447-a32d-c8aef5c7fa5e | -7.57892 | -61.29628 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37ad181a-8e26-3e63-9d3a-bcd65dfe837f | -8.90074 | -70.68929 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d08f008e-30f2-39b6-83e9-8d98182abe3c | -7.88201 | -72.99665 | 2026-08-28 17:47:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 18ce8b6e-be55-3b3b-948f-d2458f8eefbb | -4.4401 | -55.62968 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7f8c9670-e4ab-36ce-abac-9a172651de0c | -4.47434 | -55.40176 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| fddf68ff-2734-3d3f-ba18-d8c1cff25ba3 | -7.95311 | -72.38442 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 79a89506-e47c-3c89-8a38-f56f3aaf1af0 | -5.81995 | -57.63596 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 671efd5b-5db2-3a32-85da-71ffb76b3ad9 | -3.34795 | -58.20127 | 2026-08-28 17:47:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 93a721d9-f72c-3c80-a4bb-c69d5a27783c | -3.203 | -61.14122 | 2026-08-28 17:47:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4204cdb8-6d3d-3856-bcef-1125b0f24f33 | -6.66498 | -59.43452 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 993b72c9-be6e-38e4-8430-4228938dc675 | -8.79442 | -62.47762 | 2026-08-28 17:47:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a66679a9-e861-37e5-8d57-c1c3b6cc3305 | -6.31996 | -54.74112 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5dbcdaf1-d1ce-322a-8c16-7add40dbb148 | -8.68191 | -62.80576 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5da2f9c1-41b0-35ed-bcbf-04ec968731d1 | -9.16654 | -65.79535 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 57e5781f-6f73-384a-a00f-4ad73d88227d | -4.16091 | -60.6895 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5b6e748b-8012-3522-8d38-7eb559c501ce | -3.43509 | -59.40311 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a8aba3c3-d548-3df5-aab9-759b851b6c51 | -9.11791 | -70.17303 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 16a17412-0867-3741-89be-df272cbb97ca | -6.14701 | -57.64829 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b34da6ec-aa23-3634-9892-e17cd4e9c241 | -6.93692 | -58.95255 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 8d7b8353-fb36-32f5-9097-97824f5f9548 | -8.69592 | -70.97934 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d9baff36-2e79-385e-af1f-8edeaf235377 | -3.43368 | -59.39946 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6eed4567-2d66-3b36-8eeb-ad142eb457fa | -8.67152 | -63.87803 | 2026-08-28 17:47:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b41dc2e5-0033-347d-80da-7f6916f0a05e | -6.16805 | -53.49807 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 600c0d74-6bd4-32cb-9dd8-665e86cd43d2 | -6.37579 | -54.95761 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8feb867e-415d-32d9-bf2f-eedea93bc378 | -8.8659 | -71.26254 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a527f96c-7ca5-34af-bc3a-3807792346cd | -3.6388 | -60.55746 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| aa8bbc66-5cca-310e-a6db-56c7991246ef | -8.91673 | -70.87812 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 90c790d0-2253-3fea-a01d-98d9d6e28bc4 | -6.91822 | -59.48587 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| d60fd4b9-7de7-3d86-ada2-a75427135a46 | -7.59323 | -61.32064 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 147565e6-5165-3d90-9a64-7fce82a3e539 | -7.58866 | -61.31377 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0003353-5fc7-3334-92a1-90cdc6be0c3d | -9.15276 | -71.9207 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 89ea779b-7336-3e5b-8388-4289585618ee | -7.58416 | -61.32963 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 193a45cb-d5b4-3bcf-bd6d-e8812cc81781 | -8.64468 | -66.53941 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 81ddb5b3-0466-3a71-8e6c-a6f568f2f4bf | -9.03105 | -71.42946 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 28676dc8-7931-3f12-a683-7026e64af919 | -7.74826 | -61.05891 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| af5ecc04-c00b-339c-987c-151da1bc7fe7 | -4.30195 | -59.47411 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 757f9b10-e7ce-32cd-b6de-c69b8dff2cdf | -7.75196 | -61.10452 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f40f2181-ea53-3a80-872c-c23ecb271e4f | -6.01856 | -57.79013 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ebd56cd5-d7fd-38b1-a0b8-a3b875690730 | -7.60577 | -61.33384 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27c05f16-048d-3557-bd04-33932a9461b3 | -6.42294 | -61.3886 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0d0efa73-378c-3bbe-8fd4-4c20fa6ee30f | -8.92307 | -68.85497 | 2026-08-28 17:47:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cacf9ca5-009e-30f7-be72-f6eba42a541e | -9.06532 | -71.94347 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16612d2e-41db-3e93-8f0d-63ff289bddd2 | -6.82105 | -64.31834 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d34243f-2fd6-37ff-9cf0-40b242e8e909 | -4.47746 | -59.88622 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 53b125a9-5143-36ab-83c6-0c2f308e0d79 | -7.59024 | -63.0338 | 2026-08-28 17:47:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46335be7-66e8-3a99-95a3-dbe48ab76494 | -8.26605 | -71.99506 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3cfb5b44-46a3-3574-a1e2-5d03d2308079 | -7.1012 | -55.47686 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ca244c8d-6cdd-37f8-a74c-8fb3e0285f34 | -3.90976 | -60.9435 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 2cf29752-84f1-369c-ab0c-88f75edab035 | -7.91921 | -61.32164 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1e4b85cb-0293-3f1f-a92d-4b14353f7c78 | -8.43413 | -71.15528 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 74cf05a9-51bc-3f6b-a17e-d8792c5c3f98 | -7.95265 | -72.38095 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 38a91bd6-9646-37e0-b712-903b0b65fee1 | -7.58067 | -61.30742 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 30184f23-3bae-390d-854d-9e2b630e1618 | -6.09263 | -63.42882 | 2026-08-28 17:47:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ce64c81-9832-3bdc-bb91-86e07234b693 | -7.47031 | -61.386 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c16b018c-a7a9-3f1e-b247-f653bf3de506 | -7.59838 | -61.33121 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a07fb46f-fc46-3f96-a58b-eae9cc0d43ac | -8.04894 | -68.24129 | 2026-08-28 17:47:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b57db6ea-13cb-3992-a46c-f3699c153d9a | -7.6291 | -61.34909 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 31c5050c-b81e-3394-b081-3bf3c4b92111 | -3.81588 | -60.91962 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e6dc8bd0-c333-3b46-aee9-840e2b8a43d4 | -7.7659 | -70.74377 | 2026-08-28 17:47:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| af68613e-1931-315f-ab83-482067855ec7 | -5.99659 | -57.68437 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3b487e68-9138-34fe-9aa3-4c54a18a0d52 | -8.4361 | -70.72012 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 47452333-e1aa-3273-a76c-62dad303b1de | -8.54907 | -70.47504 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 27.4 |
| dd386aa8-8003-399c-80d8-f753b60a0051 | -8.26787 | -70.85656 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4e323dea-8a19-3fe9-9d85-ba2d25793896 | -6.27224 | -53.13755 | 2026-08-28 17:47:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| dc3d9e50-5650-373e-921c-f2ad0b05803a | -7.72483 | -72.70217 | 2026-08-28 17:47:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25d5eb50-7553-3af5-9ea6-afbd7f1c13c5 | -9.17073 | -65.79897 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2311f7ef-fdf2-3a8f-930a-765e1a5b40c7 | -7.93407 | -61.37206 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5574b3d7-3e44-3f0b-b92a-e9bedcc223ee | -5.97086 | -61.47848 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 694e814a-1f6e-3ade-aa18-fb14faaa06ec | -7.3549 | -55.17283 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 5545fe66-26ed-3af7-a286-f5154b00ada8 | -8.92769 | -68.82524 | 2026-08-28 17:47:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6f1e25e-2d2a-3ca5-8496-37f8b4b8c777 | -5.99919 | -57.82924 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e6466d3a-d076-36a5-9a5c-3a9f0bfa5972 | -6.4845 | -64.24459 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa81eca0-38c6-369e-ac4c-afede5ac9625 | -8.84412 | -70.67442 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 34143603-ca0d-324d-aec4-b947338f7d00 | -9.37824 | -72.72094 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2ae60509-cd42-3234-81a9-70914969c9a3 | -6.73097 | -59.64566 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb230149-4556-33ea-9676-9c47ed75a1dc | -8.86457 | -70.90205 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.4 |
| abc12264-5564-3be4-bddd-5db5dec0c854 | -7.07608 | -59.71606 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6edbe4c7-be1f-3a24-9638-be3b74b3c3f6 | -6.8375 | -59.74175 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 080dfa72-efd1-3f81-9414-4acf193f35b5 | -7.92612 | -61.36577 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5a0fbbc3-fe47-3fac-80e6-de39effbca17 | -3.93721 | -59.33088 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 7719aa44-ec13-370f-ae9e-88bc1c277ebe | -6.82967 | -55.60894 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d0655c4f-204a-3784-9344-a03c2d3c5e4f | -7.06933 | -59.22452 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8ba7893-bb4f-3b31-bde1-dd7bf19af0c5 | -6.16966 | -53.47433 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| ecebb1e0-5c33-3b48-99b2-0c266015d3c5 | -8.48736 | -70.74469 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 5399180f-54c0-3e6d-bc35-d268f9a534b2 | -4.3084 | -59.47132 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 116f9510-d1a2-338b-a8ae-a9520356bca1 | -6.8427 | -59.94033 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e4fb91e2-2750-354c-b230-b28449150340 | -4.96151 | -56.27134 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9f2b538d-04ad-3153-8f1e-684b950eedd7 | -9.16831 | -65.78249 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cb4c65f6-eed8-37b2-a738-f533cd2ccbd8 | 1.78868 | -55.8266 | 2026-08-28 17:49:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8432f614-1999-3edd-bb5b-f624db44c72f | 0.14168 | -60.40367 | 2026-08-28 17:49:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ad0511c2-9b6b-3a87-8c4e-a2f62f72ca0e | 4.93651 | -60.30133 | 2026-08-28 17:49:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e899eb37-99c9-3460-b52e-2e7fbe108755 | 1.78972 | -55.81961 | 2026-08-28 17:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72ecf096-67b0-3bcb-b174-88cb12138ef6 | -1.25644 | -55.70573 | 2026-08-28 17:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 887ed69e-f79c-359e-a78b-dd1fd41a45d2 | -1.24699 | -55.71386 | 2026-08-28 17:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e535f300-a5b7-3d7e-8715-6c021a880b43 | 3.28533 | -60.61594 | 2026-08-28 17:49:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |


[Clique aqui para ver as próximas entradas](README156.md)
