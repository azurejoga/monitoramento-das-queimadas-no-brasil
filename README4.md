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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b426f9d8-ba5f-3521-82b1-04fd52bc3003 | -23.5242 | -47.8109 | 2025-08-01 00:50:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 174.2 |
| 1a009ee1-6f9e-390d-b316-89bd1df5b9af | -7.7444 | -45.0762 | 2025-08-01 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 5a615bd9-1223-3666-b9ab-8b709e46aafd | -23.5234 | -47.835 | 2025-08-01 00:50:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 365.5 |
| 74d4e898-f054-3dda-8c73-3edac054150e | -8.3396 | -50.5652 | 2025-08-01 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 29317575-d57a-3c17-b2e0-a679b6705561 | -8.0321 | -43.1257 | 2025-08-01 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 153.2 |
| 8f2ed670-e73d-3c86-bf9a-cf1bdcbee59e | -8.0324 | -43.1022 | 2025-08-01 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 7cd6b164-e246-3e50-88b8-46f8d25308f8 | -8.051 | -43.1237 | 2025-08-01 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 202.8 |
| a59ca1d2-5770-30bd-96ed-ae7d13329759 | -8.0513 | -43.1001 | 2025-08-01 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 192.8 |
| 3984ac40-6845-3a0a-918d-f4506c6805e4 | -23.5226 | -47.859 | 2025-08-01 00:50:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| b03a5211-eeef-361d-b1f6-52f3895b3008 | -7.7632 | -45.0744 | 2025-08-01 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 97678472-6270-3ec9-80ca-2b3233ef3d80 | -8.3394 | -50.5863 | 2025-08-01 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 2133458b-69f0-394b-ac4e-19016d62b46d | -11.7666 | -44.9986 | 2025-08-01 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a03cdc02-3a0b-3a8c-8752-8ddb9e8b8f16 | -6.8026 | -59.2658 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 2f08979c-c8dc-3842-a6ff-98c178ff5121 | -6.8395 | -59.2643 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9ba61f0e-9d76-3df6-b59a-2f4ccd1ac65b | -8.0324 | -43.1022 | 2025-08-01 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| d46c895a-37e9-385d-ad07-2b7e01e2a51e | -8.0513 | -43.1001 | 2025-08-01 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| c3785c4f-a618-3262-9a48-eab16f8d4f17 | -8.3396 | -50.5652 | 2025-08-01 01:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 9c8cb258-c34b-3f03-8059-a223d9e6c274 | -8.051 | -43.1237 | 2025-08-01 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| b950d0f8-cacc-3b77-b703-224a11772db7 | -23.5234 | -47.835 | 2025-08-01 01:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 453.0 |
| 56994afc-e340-3f89-b4bd-86da38a35117 | -7.7255 | -45.078 | 2025-08-01 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| a0b7fd26-f708-3283-a506-a39620152134 | -7.7446 | -45.0534 | 2025-08-01 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a839157b-0e26-3d6f-ad13-50865174a21a | -9.3989 | -45.4928 | 2025-08-01 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 1d10f160-a62c-3a0e-a5bc-08df1a060e3a | -11.7854 | -45.0189 | 2025-08-01 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| d03cb71a-8b2c-3013-8216-6ed92133fb51 | -6.5074 | -56.213 | 2025-08-01 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7227f934-e678-37cc-a52e-80cd385330b2 | -6.8397 | -59.245 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 87d04672-5f48-3a2b-87bf-f04fd45ced78 | -23.5022 | -47.8407 | 2025-08-01 01:00:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| 296554fa-5b71-3dca-be19-f4df71de313a | -11.7858 | -44.9958 | 2025-08-01 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 270.2 |
| 727e2f6e-70f3-349a-8774-6fea0416b051 | -8.3394 | -50.5863 | 2025-08-01 01:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 0627d785-f076-3700-a791-785c832253d6 | -6.5258 | -56.2121 | 2025-08-01 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a7f94488-997e-3cd1-b892-0bf4bbc1ceff | -7.7444 | -45.0762 | 2025-08-01 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 55199e40-2d89-3464-ba55-6af08fbfd38a | -23.5226 | -47.859 | 2025-08-01 01:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| b0b045e2-0d16-39ff-9b59-4b7f53fd1b48 | -9.629 | -63.422 | 2025-08-01 01:00:00 | GOES-19 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 32a12a01-9048-3641-967d-211a71278b5a | -7.7441 | -45.099 | 2025-08-01 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 496883d8-d775-31d4-8303-24c83be0a82c | -23.5242 | -47.8109 | 2025-08-01 01:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 171.6 |
| 376632ae-22c8-38cd-bc46-4001445dfca4 | -6.8027 | -59.2465 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| aa0434b5-d3fd-3f4e-8a6c-0be61e7b1d2a | -11.7662 | -45.0218 | 2025-08-01 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 3e0deb3a-074b-3c3f-a249-f9b8003532f1 | -6.748 | -59.1523 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 5078c047-9447-315b-933d-ead3c4428cee | -6.7294 | -59.1723 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 452.2 |
| 4c2303b4-7cca-3a3f-9c8e-e74bc9da0594 | -23.5446 | -47.8293 | 2025-08-01 01:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.8 |
| 0724e068-b236-3e84-ad4a-e729e00f33e2 | -6.8211 | -59.2651 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 81a1db83-ae33-3fc1-90c8-11212a1121ab | -7.7632 | -45.0744 | 2025-08-01 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 9f34ff6e-5275-3251-8d17-138f13050355 | -9.4178 | -45.4906 | 2025-08-01 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 1c34adb7-6f61-3cc6-ba9d-8f810aad211d | -6.7295 | -59.153 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 970fd268-94b8-3e44-bf82-171656f71baf | -6.8212 | -59.2458 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| b3450893-7843-33de-8994-571b5d74cc61 | -6.7293 | -59.1916 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 39518ebe-9bf7-3d52-b619-5b64f5f197b6 | -6.5443 | -56.2113 | 2025-08-01 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 64c3349f-3ef5-38e1-b19a-d141520216d8 | -6.5629 | -56.1906 | 2025-08-01 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 32451b65-7c3d-32e2-a1c6-052ff064df43 | -8.0321 | -43.1257 | 2025-08-01 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 172e9e7c-02e9-3a03-9fa6-6cd3bdf3a20f | -6.7478 | -59.1716 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 225.4 |
| 6fed0667-2c0d-33ce-8a06-a4f23d22ae5d | -6.7477 | -59.1909 | 2025-08-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ce0f5dcd-ed51-38c9-ab8b-c7b5de91efe9 | -11.7666 | -44.9986 | 2025-08-01 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 5c7b4798-2b9f-375b-8f54-8d803f91dc33 | -6.5445 | -56.1915 | 2025-08-01 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| ba45e728-08f7-3e0e-bef0-4c654c93437e | -21.447201 | -57.135601 | 2025-08-01 01:00:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b81c802d-1e48-3b07-8f91-08babbb239b8 | -6.5347 | -56.198002 | 2025-08-01 01:00:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48894944-e7e4-3f91-84cb-e617d57be24c | -10.1159 | -58.228802 | 2025-08-01 01:00:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 821565ba-feda-3e5e-a098-07e38adb32c4 | -6.7224 | -59.171101 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 370fdb4c-fec6-3d7e-9cad-c028feb9efc5 | -6.8426 | -59.246799 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c1a78e6-6a95-3292-bc5e-e38982ee9198 | -6.623 | -59.964001 | 2025-08-01 01:00:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| febbe9bd-e79a-37e9-a32a-7c09446ce257 | -6.6512 | -59.083801 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58c18c94-12b7-3f9a-8031-57f3091d5b72 | -6.5466 | -56.2048 | 2025-08-01 01:00:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4c18677-e1da-3f53-bdb0-fe2ea0e4c685 | -6.8132 | -59.253399 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1554fc4-e1fb-305e-b790-f98161a688fb | -6.6261 | -59.977798 | 2025-08-01 01:00:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8adc4879-4651-3eab-888d-0fa4d87ccdb1 | -6.7322 | -59.1688 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73fc04c1-471d-3069-80f0-6644e6291ae5 | -6.8065 | -59.269501 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2fb0565-1b05-3a90-a53c-1d11151b8b43 | -22.506399 | -47.2061 | 2025-08-01 01:00:00 | METOP-B | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2725dc99-5188-313b-8931-12dc58cc5eb6 | -23.5161 | -47.803699 | 2025-08-01 01:00:00 | METOP-B | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d77f185d-2923-3c6f-8764-1863a2a60d3f | -6.7354 | -59.1828 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46ca1ba1-7d84-3630-9376-ce71cbb5e5a3 | -6.742 | -59.166599 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ecf257c-38d3-3ad2-a4ea-38b25ca9472f | -6.7503 | -59.157398 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0710b970-c7c2-30dc-a0c1-f33796f90f3c | -6.7518 | -59.164398 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88ed2dab-9803-3ac4-90e0-78a79e47736c | -6.8018 | -59.2486 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bbcc83fb-4376-3089-a86d-82e3df8b3912 | -21.4457 | -57.128201 | 2025-08-01 01:00:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 902afc8c-52d0-3578-959a-414130f8d6a0 | -23.525299 | -47.837601 | 2025-08-01 01:00:00 | METOP-B | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 70a846b2-82b6-3fae-ad79-f9c3c094364a | -6.7291 | -59.1548 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 405cd16a-dc56-3df6-92a6-755061f97105 | -6.8148 | -59.260399 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d12d1604-9fe7-3676-8cb6-a3937410436c | -8.3269 | -50.5695 | 2025-08-01 01:00:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77c7439e-3f79-3bb9-bf05-86087a84aecb | -6.8328 | -59.249001 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44a7a817-9cd9-313c-ae51-e1a6c43f288e | -6.8277 | -59.272099 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bcf74b67-ac47-365f-b12f-9a740cfc7b61 | -6.8198 | -59.237202 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| caedc209-aba6-3b4c-b74b-6b319a9b5216 | -8.332 | -50.5896 | 2025-08-01 01:00:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55bc9702-8e95-31a6-bc3d-997343a05513 | -6.8163 | -59.2673 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6684e712-8447-3116-9f9c-86b41fd5dedc | -6.6246 | -59.970901 | 2025-08-01 01:00:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 945ea4b5-fc46-328d-928c-8a95de5eb739 | -7.3266 | -59.611401 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53ea68b9-5708-34b2-bcb0-395f33757b0a | -9.4589 | -57.8335 | 2025-08-01 01:00:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c01c886-50e4-31b1-8b6e-8cce0ced41b2 | -23.511101 | -47.8237 | 2025-08-01 01:00:00 | METOP-B | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77d5bcdb-65d5-3b0f-9219-44f4244bdecd | -7.0832 | -60.041698 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 762758c9-5a3a-36be-b69c-4e28cb297ca7 | -9.4606 | -57.840801 | 2025-08-01 01:00:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68b2e69f-d396-3fe6-b9fa-23399e2b5c32 | -8.3366 | -50.567001 | 2025-08-01 01:00:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abde11b7-21a6-3133-a52c-bb796ed67ce3 | -6.8179 | -59.2743 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e926450-1bda-3b96-a8c0-3ec2e50466be | -23.5207 | -47.820599 | 2025-08-01 01:00:00 | METOP-B | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 954d9d8b-6060-3815-88c2-f4828c028bd4 | -6.841 | -59.239799 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 342790ce-9a83-3f84-89b7-3b83f46ea5f0 | -6.5173 | -56.2117 | 2025-08-01 01:00:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad76b786-f6f3-36de-9817-7ce1fb90b7ba | -6.7389 | -59.152599 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa611789-2ebe-35c5-8c55-463f1d8862ee | -6.6544 | -59.0979 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0856e2dd-4ff5-3573-a5a4-c8b3a034353c | -6.8375 | -59.269901 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 644ddb0e-aad4-3ce8-a732-f8e8fedffe3a | -6.8034 | -59.2556 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e26a2325-0ec6-30d7-a626-66dbbc69f17e | -6.6276 | -59.984699 | 2025-08-01 01:00:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| abd5b8ef-f656-377d-8e79-9e2aa8c54a62 | -6.5151 | -56.202499 | 2025-08-01 01:00:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a226021e-a768-30bb-bab3-4f22548f9376 | -6.7471 | -59.143398 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e92f0ce4-2d0e-3108-9a97-9a47cf3cf05d | -23.515699 | -47.840599 | 2025-08-01 01:00:00 | METOP-B | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README5.md)
