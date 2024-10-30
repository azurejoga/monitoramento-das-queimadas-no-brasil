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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 152b78e4-24c4-3d3b-aac2-08fc144f714b | -5.60991 | -44.8984 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c36a49c5-1ae5-3b3c-bac3-c7906add8bd9 | -5.60661 | -44.89788 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3e89734-ce6f-3d4f-be2c-03ed64552162 | -5.60606 | -44.90134 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 754a073e-7cc0-3ed3-9ef4-139935168fb5 | -5.55719 | -44.67454 | 2024-10-30 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94970d18-4f93-3d8f-8b10-198f97ecfa67 | -5.48369 | -44.8573 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a49d0fe-6a33-307a-b8cb-64a8154aec11 | -6.66923 | -44.69937 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e35213b-d0cc-30b6-9716-b7cc78352260 | -6.66593 | -44.69885 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a3a8592-2f1c-30b2-b131-21bc7ff02ad7 | -6.66263 | -44.69834 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7619718-7652-3198-8a28-40a684662aa7 | -6.65504 | -44.74662 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf406304-1a3f-367e-bc99-ed4ca5acdc9f | -6.64915 | -44.24003 | 2024-10-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3c0daa9-7cf8-3505-8c43-c2686efdaa98 | -6.62534 | -44.74196 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| baf2c86a-7894-31f7-8c92-62cb361f5506 | -6.62522 | -44.00153 | 2024-10-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05068157-fefb-304d-b072-ab1a29b2f37d | -7.54552 | -43.83306 | 2024-10-30 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22d82648-b091-310e-ab5f-2de7954f2e33 | -7.54498 | -43.83659 | 2024-10-30 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06132991-cbca-3b18-ab49-c5f8a6ab511d | -7.49564 | -43.85001 | 2024-10-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8032c00b-ec40-31fb-8218-1d38d3c258a9 | -7.47782 | -43.83277 | 2024-10-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3ef68a7-3eac-3f8f-aa0f-459b688497f3 | -7.42639 | -44.79558 | 2024-10-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4de67c22-0277-3ad2-80f2-ea2c917d891c | -7.44439 | -45.30876 | 2024-10-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db7fb028-9d5e-3564-8913-fb518580454d | -7.2579 | -44.91714 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aa72002-18fe-3c5d-803b-dec68fc16a90 | -7.22087 | -45.15215 | 2024-10-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3afa5e49-2460-3feb-affa-65cd90d34826 | -7.07619 | -45.22496 | 2024-10-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b58c2829-7dfd-3da7-abca-88c4787400d8 | -7.06504 | -44.82297 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 793c7803-bcc3-3930-b48c-aa03e7be2018 | -6.97631 | -44.32343 | 2024-10-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fdabc35-5e14-35dc-be92-da4aaa1065f0 | -6.97577 | -44.32691 | 2024-10-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a428ed8b-5d9d-37df-8846-4cb69ad0506a | -6.96961 | -44.71542 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 027c6490-54b1-3569-a802-2d8f72e599d4 | -6.93181 | -45.06321 | 2024-10-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc6fa303-6ae8-3141-9add-aabdf8ec2141 | -6.92851 | -45.0627 | 2024-10-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fa166ff-e237-3c71-97b4-0d7e8ad0b7d1 | -6.92797 | -45.06614 | 2024-10-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e637b25e-d5c5-3cf0-811f-a89459498a89 | -6.92396 | -44.3117 | 2024-10-30 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86718c67-e6b4-31c1-a3bb-df584d9122f8 | -6.92344 | -44.51008 | 2024-10-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 012d0ec6-e807-36f2-93ca-1b04e4aef790 | -6.89813 | -44.97283 | 2024-10-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f313653-3742-3126-b271-d104d5b062af | -6.89445 | -44.56567 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 599fd53e-8265-3aea-a248-96b71fe7ddf5 | -6.89391 | -44.56913 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d12dba64-d832-3550-83c8-b247fb5fc48c | -6.89337 | -44.57258 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ff12023-b867-30ba-a6e9-4a273ebcd740 | -6.87099 | -45.18826 | 2024-10-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19234ce8-ab73-3632-bd0f-1d95ea7c6112 | -7.78376 | -43.8985 | 2024-10-30 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d2029cb-fb27-3dc0-8dbe-99454e3ef2d8 | -3.44278 | -45.97034 | 2024-10-30 04:19:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01503537-9075-3c4a-be76-3676f4b91fe2 | -3.44219 | -45.97406 | 2024-10-30 04:19:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 272bc183-a434-3ccf-8964-55913d5da123 | -3.17348 | -45.78448 | 2024-10-30 04:19:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49bb7c53-c74f-3354-85a3-364664f4196c | -3.62411 | -44.54445 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c57c6b02-38c2-39a2-9f5c-eb213fa80da4 | -3.24651 | -45.57181 | 2024-10-30 04:19:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 044853f8-c720-3e12-a0ce-ce1a77f9630b | -3.24593 | -45.57544 | 2024-10-30 04:19:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee643585-b35c-37ca-90f1-f471682c30e3 | -3.24313 | -45.57128 | 2024-10-30 04:19:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c84c1a3-022b-39c8-866e-502d8719e9bf | -3.24255 | -45.57491 | 2024-10-30 04:19:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b13caf9-70fb-38f5-bb1e-ed6ddd4d2094 | -3.20036 | -45.00521 | 2024-10-30 04:19:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0825fec-4a42-3f6d-9406-7443cfbfbeca | -3.19702 | -45.00828 | 2024-10-30 04:19:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acd4c15a-33ee-31ce-9792-b230abc0ab77 | -3.11397 | -45.23082 | 2024-10-30 04:19:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8922d68b-0a3e-3a8d-9704-852f2bc761a4 | -2.57167 | -45.34756 | 2024-10-30 04:19:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d83c62d5-c408-3bdd-916c-573a9929a60f | -2.53943 | -45.15894 | 2024-10-30 04:19:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e0806c7-84f5-3c98-9c5a-06efe859f70f | -2.53017 | -45.28214 | 2024-10-30 04:19:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c44d8bed-09e0-39a3-9515-d1ed70e95655 | -2.38629 | -44.85952 | 2024-10-30 04:19:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecefc229-fe7a-3eba-a56d-2aad6803da53 | -2.38334 | -45.24858 | 2024-10-30 04:19:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 558573f7-c2d7-34ae-a01f-6d244fecaccf | -4.23292 | -46.10458 | 2024-10-30 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb7273f5-78b5-34d9-8855-18a9f505d3b9 | -5.11869 | -45.14397 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96c64899-136b-33c4-a9a4-2093aad4b4cb | -5.11814 | -45.14745 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd6f56ac-30e4-3339-9feb-88c7463668e3 | -5.11537 | -45.14345 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab7bf694-4304-36ff-85e7-e901348c073e | -5.11482 | -45.14693 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c617d7c-0321-3553-9674-4676d162fd23 | -5.11142 | -45.06088 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7b2c9d5-3127-3787-b1ba-38db9ade6012 | -5.05121 | -45.16193 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca26d0dc-076b-3baf-aa83-7874169dede4 | -5.04789 | -45.1614 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ff93a4c-568e-3f29-994a-aa2978601148 | -4.8581 | -45.4367 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 221b7759-af2a-3d9e-8a33-24a2b55c5f85 | -4.85754 | -45.44024 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0180f60c-5a67-3c2a-9195-f4c1da98d468 | -4.83352 | -45.71387 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a8832b5-c8fc-3564-a6a5-c9a15cb29eb0 | -4.83016 | -45.71333 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70c0018b-55e5-3380-8864-866869f10f2d | -4.82831 | -45.71246 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95096277-b65a-3a23-b157-8ee053761930 | -4.82775 | -45.71606 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6fc9283-5b80-3de8-a58d-fae68868bfa0 | -4.82495 | -45.71194 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 587fc3bb-5142-35cc-bffc-ef0416dfbec8 | -4.82438 | -45.71552 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38aee28d-6a48-3941-85d5-856feba308c1 | -4.81933 | -45.72571 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4152868e-f8fb-3cc2-8276-ec2e21a21803 | -4.81606 | -45.65925 | 2024-10-30 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70ba2df2-5d3a-380e-9ed1-2fb94a42a372 | -4.81597 | -45.72514 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeec8678-be20-3096-805e-833bfd0d6f18 | -4.74718 | -45.65933 | 2024-10-30 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 876de8d9-2bef-346d-84f5-3560adb1ef18 | -4.74661 | -45.66291 | 2024-10-30 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba1adcfc-855f-3ae1-8dc8-174e8c489ad4 | -4.52383 | -44.75082 | 2024-10-30 04:19:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7d16636-814b-36d4-b34d-51c96b6c6c44 | -4.52328 | -44.75427 | 2024-10-30 04:19:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47b0315a-8f18-31e1-86d0-b4c521fbb352 | -4.34595 | -45.681 | 2024-10-30 04:19:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77c41eb8-b250-3f51-a3cb-789d1118db04 | -4.34537 | -45.68461 | 2024-10-30 04:19:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac5cd571-d21a-31c1-9ec6-0ad0c287cea8 | -4.34201 | -45.68404 | 2024-10-30 04:19:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52822ad9-cc9a-38b3-9c95-26f4aeb810bf | -4.29403 | -45.72464 | 2024-10-30 04:19:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eddffa6b-2915-3374-a1ca-d2476c38b6c7 | -4.29065 | -45.72411 | 2024-10-30 04:19:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2bbc222-00f5-3b7c-b361-d8c3a71ec924 | -4.25479 | -45.67789 | 2024-10-30 04:19:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d182429e-033d-381f-aa93-b20f29c75ed2 | -4.25142 | -45.67738 | 2024-10-30 04:19:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 033e1a82-bce4-346a-9090-4050b2bc0909 | -4.14597 | -45.61253 | 2024-10-30 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0346cc3-ec85-3376-82fb-5799e1a4d923 | -4.1454 | -45.61613 | 2024-10-30 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12bea6cb-0db2-361a-a40a-d48d50d75d02 | -4.14203 | -45.6156 | 2024-10-30 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a32261cb-8759-3797-af96-d69597892b61 | -4.03218 | -44.7193 | 2024-10-30 04:19:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4130f3ac-b1c1-3274-a1e2-37fdff662adb | -3.9068 | -44.93029 | 2024-10-30 04:19:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 097afddf-b2ee-3100-97be-99db9377fbb6 | -3.68742 | -45.47456 | 2024-10-30 04:19:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a8692ee-a09b-391e-a583-b4f31a7b2219 | -4.91981 | -45.83384 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4d04c8a-4bfe-33d7-9ab1-f5919ccb00f1 | -4.7514 | -45.89247 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1ce34f1-be3c-37c3-bdf7-1b05d1e94d30 | -4.74802 | -45.89193 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97a3237d-afef-381b-9a8c-c033199a6169 | -4.64485 | -46.18726 | 2024-10-30 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a01deba-eaf5-32b6-a40a-5168f00bcf2b | -4.23634 | -46.10507 | 2024-10-30 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4ede55b-2979-386b-9667-660049bbef07 | -4.12425 | -46.10278 | 2024-10-30 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fba32f49-0aeb-3654-9a82-e9a665218cc2 | -3.84838 | -45.93902 | 2024-10-30 04:19:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bee0690-d54f-3111-a073-b4c194a49c14 | -3.84779 | -45.9427 | 2024-10-30 04:19:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac638ad4-8096-3113-8698-462bf5260bfe | -6.46856 | -45.79411 | 2024-10-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce5b7f03-5bcc-33fe-8987-54974051239b | -5.97459 | -45.36985 | 2024-10-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 23ae03ae-3ac6-3ee5-9945-b1825f38ace9 | -5.97403 | -45.37334 | 2024-10-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| de604196-521c-39df-aaef-1e65ba55da10 | -5.97199 | -45.36512 | 2024-10-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README38.md)
