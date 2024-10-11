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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac66dd3b-763d-3def-856f-921abe66ac13 | -6.72839 | -59.65835 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a78c9b6-220e-3f45-88a3-57a1cda985ab | -6.72728 | -59.66531 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5366f70e-4999-3666-8104-7ec757602885 | -6.72673 | -59.66878 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 834f805e-4b31-3996-b76a-b37cb65e1812 | -6.69565 | -59.86396 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e7832ff-1548-3474-8451-3b308721a42e | -6.69289 | -59.85994 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af984bb6-b329-3dd2-836a-18c86f03f648 | -6.69233 | -59.86344 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ba66b93-b9e0-314d-a55d-048be5792fe8 | -6.67953 | -59.81475 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bee0ab0-93a2-3a65-8047-cd5de2cfa338 | -6.67677 | -59.81072 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15160254-79c3-3dda-95ef-87763ea68ead | -6.67621 | -59.81423 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90c9d2eb-4e5d-3305-9fad-3ecca9beb6b6 | -6.67345 | -59.8102 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 522e3d15-9b70-365f-9ed8-cd7b5db56404 | -6.66515 | -59.7767 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f8ac8ec-d83a-3adf-8d73-f124b7ce22be | -6.66128 | -59.77967 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b892faf-56bd-344e-9035-f568ff5c5c45 | -6.66073 | -59.78316 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1be21e85-eff5-3f43-a685-790422edba3d | -6.65797 | -59.77915 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2370e4a-ec54-3c91-8983-f7115cabd1bc | -6.65741 | -59.78263 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9923071-b184-3fb8-887a-05e3f1c98f50 | -6.65465 | -59.77862 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d1a02d9-4735-3e31-bc9f-fe154ed820ed | -6.6541 | -59.78211 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d242ccca-bf99-3aed-80fc-8cfbabe7247f | -6.65134 | -59.77809 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 536240f1-f545-3a67-b5d5-628a70b12369 | -6.64185 | -59.96675 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c11b4767-def3-3945-b670-5cffc48080ba | -6.6413 | -59.97026 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a53ae578-9f61-3ff8-bec0-61c025d9f193 | -6.63733 | -60.0599 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5aac375-6dc1-34c8-b87d-72ffd14fc013 | -6.634 | -60.05938 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ccee464-d6d4-38f7-9827-d5d1b289f7f2 | -6.60852 | -60.00478 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b96889fb-4746-391d-b337-c8add26d1cdc | -6.60576 | -60.00072 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8947930d-7899-3842-8576-a6c2dc7d339e | -6.60519 | -60.00425 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3068fac5-7766-328a-90fa-a4e8a41003e8 | -6.60299 | -59.99667 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72ef994e-110b-30b2-819c-a69cf3c9f4cb | -6.60242 | -60.0002 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ce0e065-0f86-3930-98b7-afba102bf01b | -6.97271 | -59.47005 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94afca35-8bed-3a52-bc75-257d1cb2f7f2 | -6.97216 | -59.47352 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6c6e668-d413-3941-afac-4bc54298782f | -6.9683 | -59.47235 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e3a1fe4-7497-3e45-a627-910bc65ea0f4 | -6.96499 | -59.47184 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e40d9724-e4a6-3a9b-8c60-47759e0d0f13 | -6.96445 | -59.47531 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17a6a642-a8e9-323e-8274-13b07322a3ed | -6.79869 | -59.36408 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65e593d2-553b-3b4a-98b8-c5e46120ba58 | -6.79752 | -59.32854 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58c4cd53-77bb-3e9c-a740-60f13e2c8aaa | -6.79313 | -59.33494 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d5949ac-82ba-397f-8f7e-12a0f70adbfb | -6.79258 | -59.33839 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5dbf021-84d7-39d1-82b1-539be4fdd34b | -6.7865 | -59.31266 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d529c22-1738-3612-b216-7269b6a80433 | -6.78595 | -59.31611 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d88396d-f2c6-3bd7-9c41-a6887bfc21b9 | -6.7832 | -59.31214 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a37d106-04ef-32ce-8341-fb56b46560ae | -6.78265 | -59.3156 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a402cd77-bb57-3c83-9b59-56d979758d27 | -6.7821 | -59.31905 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87c08ea3-02a5-344a-8835-32eab50b6ea1 | -6.77989 | -59.31162 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67a911f7-a187-333c-8954-d804f16ab92f | -6.77935 | -59.31508 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f4ed067-7cf6-36ec-8638-39f0d8b5cd19 | -6.7788 | -59.31853 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dad64a88-6baf-3658-b65c-980e9e027041 | -6.77826 | -59.32198 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 155aa264-62d1-3a2f-9473-cd917cc1e670 | -6.77678 | -59.43856 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb767c1e-0c4b-36a7-9ca8-807aab1b7180 | -6.77536 | -59.31435 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf872559-d470-33fb-9ff2-efe26a2ef341 | -6.77482 | -59.31779 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5fc2df0-0879-321b-b764-15def8a90095 | -6.77427 | -59.32125 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89e0cfc9-0eef-3748-bbfa-b27e52add3eb | -6.77373 | -59.3247 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a8a6cb9-0158-3ce5-ba41-044a6a6d7751 | -6.77206 | -59.31383 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c51601c8-df54-39cf-b5f4-5ea0f25b1347 | -6.77151 | -59.31728 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d0d444f-3cdd-38b9-845b-35cae26ca0b7 | -6.77097 | -59.32073 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1595e6fd-741b-31ef-818f-4bef89f1d983 | -6.77043 | -59.32419 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c332491d-7845-3560-9a80-621ba6d01779 | -6.76821 | -59.31676 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 937981b7-9cce-3a56-ad26-136bf074b1d2 | -6.76767 | -59.32021 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f78988d5-56b1-3d76-97a2-e7bef9211a3f | -6.76713 | -59.32367 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e2ac4c2-c4d5-3fd0-93c5-715278f63a2b | -6.76658 | -59.32712 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 725c8fcf-b34e-38d4-818e-98f3530dcebd | -6.76437 | -59.31969 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c7d07bf-a252-3c27-8e8d-558e6f878433 | -6.76383 | -59.32315 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af1a1258-f48e-3563-97ed-7c5d4ccd421a | -6.76328 | -59.3266 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47488d3e-96e2-38f5-a5f2-376c36923575 | -6.76107 | -59.31918 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 958740d3-f94a-305a-b7de-c42ce5314875 | -6.76053 | -59.32263 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08d929fc-f519-3fa1-8a90-2f403cecb752 | -6.75998 | -59.32608 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17a5744a-8228-3b40-86c4-1ebc6cfae8b4 | -6.75777 | -59.31866 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5aba1ca3-48fd-39e2-a47c-510231843729 | -6.75722 | -59.32211 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e727b76-b78e-3dc8-a60d-f5b723919202 | -6.75505 | -59.33593 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8e31dfc2-185c-35d0-b261-c5ae7ca90a35 | -6.75392 | -59.32159 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1d6a974-3a2c-3735-a25d-57dd7b9dfcf4 | -6.75338 | -59.32504 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35a5abf1-15cb-375e-b30c-6aae5ac7cc81 | -6.75284 | -59.3285 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8514548d-5436-3b9f-9831-6f5d1aabd84c | -6.75229 | -59.33195 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 980e48a5-2a1b-3bcc-af2d-eced73bb6b91 | -6.75175 | -59.33541 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 60e88dd8-9579-36fe-82af-926375d831c6 | -6.75008 | -59.32452 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6720bc3-9a5d-3e4c-bc2b-5d758052e1f8 | -6.74954 | -59.32798 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e6f7c87-89d1-3251-b4d2-827768172d92 | -6.74899 | -59.33144 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 122d0425-aab3-31bd-8360-10af2d330bec | -6.74845 | -59.33489 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 56ba0f47-daaa-392a-9381-962c2b6360bf | -6.74678 | -59.32401 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86ef0c58-84bf-3842-92bd-c54d9a48b3e6 | -6.74623 | -59.32746 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9b5ea6d-1140-331a-a822-7f1288efd013 | -6.74348 | -59.32349 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e887a723-518a-3faf-b084-9b3961be0f77 | -6.72806 | -59.31398 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2fca24e-c611-30d3-bf03-f3950dca855d | -6.72752 | -59.31744 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09035180-dede-3153-82f7-c7de3cea7721 | -6.72697 | -59.3209 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12664046-cb42-3453-bb75-ec818028ed8a | -6.72421 | -59.31692 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20bbf6f8-3e6e-3f3c-b3d6-52cf8620c2a3 | -6.72367 | -59.32038 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 346f14a4-aafb-38de-ae59-e80c77545cad | -6.70794 | -59.46307 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76d98ba8-5f57-3bb6-bcdd-24b7797e57fd | -6.70464 | -59.46255 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 054fa74b-672a-345c-97d5-4fe04ed762ba | -6.68973 | -59.42831 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc374437-9456-3f2b-9792-9d1406ee6e42 | -6.68643 | -59.4278 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29cc3001-54a1-32f4-afcd-786be2e7b0bc | -6.68427 | -59.4629 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84ab35a9-bd69-340c-a69d-94e5111f8605 | -6.6782 | -59.45842 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ecc4c99-f055-3f77-8673-19f7b2828f4d | -6.67765 | -59.46187 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8276cabe-e2a5-3d85-b048-6f972965eb72 | -6.67492 | -59.47916 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f2d35a7-4ed3-32f6-bf4c-383ddc6fdd57 | -6.6749 | -59.4579 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68c730eb-8409-37a0-8750-1ce9cc8339b0 | -6.67438 | -59.48262 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8657d9d5-ef78-380d-850c-24f5f2097cce | -6.67435 | -59.46135 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb96d64a-ab75-38a6-9c75-f39a14f901e7 | -6.67383 | -59.48608 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6acaad69-742d-3f69-a8ef-9591ffc67782 | -6.51229 | -60.09735 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf863c9a-6014-357c-becb-a25d474c03a8 | -6.50896 | -60.09683 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33d705f4-d225-333e-ae05-c3fc91d3fc61 | -6.55683 | -60.0291 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22cf07dd-e164-3200-b7fe-d6dcc4b79910 | -6.55627 | -60.03263 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README85.md)
