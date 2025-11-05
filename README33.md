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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cef6fba-3e67-35a2-adae-d788816a1118 | -4.86186 | -44.62236 | 2025-11-05 05:01:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19cbf830-af69-3193-8fab-8f587695a63d | -4.14954 | -50.6906 | 2025-11-05 05:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3ccb8d4-5a65-3f82-bd95-33f3da5c0f72 | -2.78544 | -50.31825 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0ac84c63-4738-3ff0-a6ef-1c3248e9b1af | -4.46499 | -43.22329 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c899c04b-158b-3df0-a84b-9f0e84e3e183 | -3.49822 | -50.45984 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9753e240-3876-3d17-a3b0-c7bd4e18ab13 | -3.5748 | -50.64215 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0745c98-3ebd-3525-8b18-7d1ab9eaf3b7 | -2.8361 | -48.83193 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dac09709-d436-3b08-941a-f0a5de7bdd54 | -3.49835 | -53.45559 | 2025-11-05 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fdb1c13-f9da-3172-a3d7-855b45677cba | -5.05767 | -45.825 | 2025-11-05 05:01:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4359517-113c-3b67-9442-c97a15a0af57 | -2.84084 | -49.40926 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| baf07712-708c-37bd-88f5-a4102d9a2f46 | -3.75648 | -52.07713 | 2025-11-05 05:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e29e782-6c6e-32af-afcd-84df5accd149 | -2.8786 | -52.61062 | 2025-11-05 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a56200d5-a551-35c9-95a3-3a8fabc2d939 | -1.26091 | -49.14029 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ecf8b88-b035-3d40-b88c-8cd08baff953 | -2.35076 | -48.49123 | 2025-11-05 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79880957-1de2-3d92-8160-64c070c19606 | -4.91697 | -46.7206 | 2025-11-05 05:01:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52039cd8-b5b5-3355-82a6-821e9f27b2ca | -2.93007 | -51.30581 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 943be6b4-4148-39b2-8763-c1a0c56040f8 | -2.84441 | -49.41362 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af97f5fa-b9d5-3165-a524-7e16ad3646f5 | -3.42818 | -50.10172 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c10f6ff-3bc4-376b-96bb-7cb147b01381 | -2.37175 | -53.98 | 2025-11-05 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34da2f1c-6414-3b88-bf48-5bb12c8112eb | -3.14599 | -50.29436 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09ceeb25-7971-3382-82d7-516a494b9c6c | -4.46347 | -43.23386 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ee4f6eb4-1a62-3f3a-9a45-d45a5a30d597 | -4.55183 | -46.76287 | 2025-11-05 05:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da7305c8-56b1-326d-a786-b0117b1ed473 | -4.58321 | -43.339 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 510f7c45-fb04-3819-a15d-c09fd21b90b0 | -4.25516 | -48.58395 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d039aef5-092a-39e6-b353-fc163fa24a46 | -1.24807 | -49.14204 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9d4b353-fe85-3e80-9c4c-42651d93a473 | -2.32215 | -48.59296 | 2025-11-05 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5ae0263-893c-351f-b8bb-7643c39b2850 | 3.31875 | -60.07388 | 2025-11-05 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 565b5ff6-3e3c-3d2d-8cc5-d27f4acd12eb | -3.07288 | -47.77653 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14a5b20e-c9f2-3ebb-9d13-2a43e465f3e3 | -3.07224 | -52.63195 | 2025-11-05 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7679e475-4333-3781-992e-303b7ee9253d | -2.84909 | -49.4105 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2a47c0d-268f-3361-b924-d5940b4446b4 | -5.11177 | -46.22108 | 2025-11-05 05:01:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9be37c0e-c33f-357a-8a71-ae07bcc3d788 | -5.47761 | -43.58293 | 2025-11-05 05:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 73fe0176-7a2f-3b68-8a02-c435094f7776 | -4.05046 | -54.45135 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d678c96-44e8-343a-8e5c-3f2c3e56ef21 | -2.81991 | -45.15102 | 2025-11-05 05:01:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| aaf45ebd-676c-3b71-b070-9fbe2a03405e | -4.59784 | -49.55518 | 2025-11-05 05:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 29c4c1fe-4778-3909-9faf-abe986762be8 | -3.70957 | -51.62247 | 2025-11-05 05:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 260e607f-5ad8-3e6a-b9df-35c50a41efea | -2.81962 | -54.36077 | 2025-11-05 05:01:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54410e74-a4f5-364d-ac37-06dcb5d6acd5 | -2.78901 | -50.31234 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5ed8a714-dc34-3045-afa9-defb416890c4 | -5.9044 | -47.29255 | 2025-11-05 05:01:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2640b79e-3a9f-3f6d-a12e-ed369c332a11 | -2.64952 | -48.51439 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5b8c5b0a-53fe-3617-8d1c-21cdac791a3a | -4.18289 | -48.58931 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8136d32-5bb7-352b-b103-631ee8444f2b | -2.45515 | -49.42784 | 2025-11-05 05:01:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 988a57ad-2286-34b5-ab4a-e0d89e85bfe0 | -3.96977 | -43.78719 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 618396ca-50a3-33c6-a1f4-4635fa3289d3 | -2.68838 | -48.46408 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 693203ad-6194-3ab5-9cad-ccb38f24e05a | -4.11296 | -43.88272 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0680afa-0e65-3ee0-893a-ff7b5cabe1bc | -3.48395 | -43.63341 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a89702cd-2489-35c8-b9a7-1d459cc94aae | -2.37694 | -47.72458 | 2025-11-05 05:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fbf21e8-9dfa-379a-b7cd-758e1487cb19 | -5.91765 | -44.01583 | 2025-11-05 05:01:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e87d38d1-94cc-3f9d-ad91-17b70964cf97 | -2.8367 | -48.82793 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0388e6d2-4d70-3e4a-83be-c6f99b2af76d | -2.93515 | -49.53184 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7f326ab-5f35-3cac-bf42-40c2502f50bc | -4.29536 | -43.79261 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b765bda6-5e0c-35c0-a438-bcb54914ef64 | -2.65389 | -48.51502 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1716ce43-f076-3ad3-a7ff-5fcef04b3a46 | -3.5949 | -49.28308 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85055516-34c2-3073-b822-b2379c3d0a70 | -4.1476 | -50.688 | 2025-11-05 05:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 440c2e8e-aeca-3825-b173-f56a105d86a9 | -5.03435 | -43.61742 | 2025-11-05 05:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 52b6af40-f85e-3230-98ee-f66b94911e02 | -3.80611 | -50.02465 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a19024d1-cc05-3aeb-a973-b70411824a9b | -3.23566 | -43.44499 | 2025-11-05 05:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29efdf53-29ff-3606-9f65-058c75c1b40b | -3.84145 | -49.9068 | 2025-11-05 05:01:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccdbd214-5256-31e5-838f-a399dc822ac4 | -3.45748 | -50.22482 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 134cabc7-d5cb-336d-8d9c-77b16f80b975 | -3.07931 | -54.3522 | 2025-11-05 05:01:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c845b0b6-7424-3d99-9c4e-413a5a887b82 | -4.71636 | -46.43909 | 2025-11-05 05:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eccecb73-6115-3c02-a600-7e2b162cf165 | -3.47684 | -43.6409 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a33529ca-1ad0-3b13-a86c-c7c1d95bcb13 | -4.47345 | -43.22396 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4734a1ea-468a-33ec-9ac3-cc02e305edab | -2.83672 | -49.40865 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9ac92cf-98a9-36de-be00-edfb29d1cd36 | -3.23916 | -46.87593 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a0284584-688c-3d30-bae3-ace37600e40b | -2.11349 | -48.03605 | 2025-11-05 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f551262b-23cb-3409-9ee4-3c8c8c5ad2d7 | -3.57107 | -50.2704 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 116a529f-601b-35bd-b9c6-b3bb0eefec86 | -1.43078 | -55.22947 | 2025-11-05 05:01:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c09a0aa9-30d1-39fd-bb9e-8d76c3e2951f | -2.79602 | -50.31834 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| de169d7c-6aaa-3359-ac0b-8efa5d60b50a | -3.4581 | -50.22345 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c41c976-d17d-37aa-8c07-aa2e4eb47f1a | -3.48341 | -49.59788 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42f87cdf-f77d-30cf-90bd-976bcb55c8c1 | -2.96573 | -54.07588 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bf56d52-7bcc-3f1c-ab7d-0d3f2c80fd66 | -5.43236 | -44.66169 | 2025-11-05 05:01:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34a3a173-6fe4-3719-93e2-ce64c0cc2166 | -3.43924 | -50.2411 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9b15ee0-7d76-3afe-8907-ae27db377558 | -2.25593 | -47.99137 | 2025-11-05 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d93a0ab2-929d-3aed-9590-976c67002beb | -3.10911 | -51.03262 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e312a5ec-7d7d-369f-a6c0-2f3bc5c79d6d | -2.88033 | -49.59136 | 2025-11-05 05:01:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6852a4aa-fb62-3d9c-a836-d3ae3835dd00 | -3.96434 | -43.78151 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f6096a01-59c5-3397-8631-70ee009f302d | -4.71331 | -48.14211 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d28812b2-f78f-3ffa-8404-380fce8238a9 | -3.77383 | -47.95852 | 2025-11-05 05:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 223be1ae-d10e-36c7-babc-e51e441a9875 | -3.49077 | -43.62969 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3899bc74-2061-382c-bb62-e5ebdfa96b60 | -3.4431 | -50.21601 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60455421-67f8-3472-ad0c-a24565af1922 | -3.6476 | -44.43672 | 2025-11-05 05:01:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c674b231-73e1-3a54-88a4-169e6face2ef | -4.71739 | -50.95182 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36d022b7-8056-3b1e-a617-74f8ccda4c16 | -2.79214 | -50.31777 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 177ad385-88c7-3646-8519-383c50f6a328 | -4.71161 | -46.43515 | 2025-11-05 05:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e198788-9ed3-3a4d-9096-355f86334c73 | -3.31877 | -53.84166 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce5a4288-43ef-34e9-8104-1746bdd4565f | -4.10357 | -47.28627 | 2025-11-05 05:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47b61442-73a3-3fe9-bb58-9903fb6a6580 | -4.08058 | -53.55573 | 2025-11-05 05:01:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c2fec72-6134-3ebe-9440-7318362bae07 | -4.40592 | -48.22202 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be43f051-53e5-3bdc-bb1c-90eac74c8afb | -3.35553 | -49.50373 | 2025-11-05 05:01:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e2599fa-3e4f-3570-949c-be49326f0310 | -5.85696 | -43.99661 | 2025-11-05 05:01:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0566775-24af-378e-a28e-b4eb5c33f89a | -1.29665 | -49.15336 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 062949d4-8e9b-370f-aabc-8cecefbbeac2 | -3.70673 | -50.81623 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ad13d47-e48b-31f2-b606-c40487d0e75c | -1.29722 | -49.14971 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6195c614-84bf-305f-b2da-169b3393cbb8 | -4.29491 | -43.79303 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9aa2081-5de7-3d56-903d-85d8395a3b99 | -3.4793 | -49.59726 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36a81449-c2ef-3866-9a07-f71fa46309a5 | -4.10633 | -48.02173 | 2025-11-05 05:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e9d7a722-bc63-382b-93f4-cb95ba35ad96 | -4.30237 | -43.78455 | 2025-11-05 05:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9163d20a-ad46-347d-94e3-04466b33c7bd | -1.29312 | -49.14907 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README34.md)
