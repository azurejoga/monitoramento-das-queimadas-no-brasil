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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa0ced51-5488-3800-9ac8-2fcffed6f172 | -3.2569 | -54.2226 | 2024-11-23 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 45453a87-a705-3a76-873d-96eafffd63c7 | -3.2386 | -54.223 | 2024-11-23 05:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a8f6f7fe-1d59-3edd-a94d-a138c2e14aab | -3.2385 | -54.2431 | 2024-11-23 05:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7d612a24-f381-3aeb-a72e-77ec99591e26 | -3.7191 | -42.7182 | 2024-11-23 05:50:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 46b97df0-613f-3b66-b900-edeec77cae8e | -3.2569 | -54.2426 | 2024-11-23 05:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 91ccfd52-ec06-3bd0-8244-e3cc784029f5 | -4.6085 | -46.5002 | 2024-11-23 05:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 0a5fd2b0-d6c2-3d0c-a47b-64f2d56af304 | -1.6809 | -52.6578 | 2024-11-23 05:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b9bbfa4f-e3c4-3ade-afa4-952ffe44bb05 | -3.719 | -42.7417 | 2024-11-23 05:50:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| dc8ecac1-d932-3f09-8769-e55b98aa525c | 1.36756 | -55.94093 | 2024-11-23 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19d56699-de0c-3ecb-aeae-00307bfa8ec8 | 1.36719 | -55.9455 | 2024-11-23 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8eed444-a401-3868-92d5-d78a22b98c50 | 1.37282 | -55.93901 | 2024-11-23 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0b8d503-3530-325a-980b-90e2a0886d31 | 1.36845 | -55.94648 | 2024-11-23 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb5b15c1-6100-34dc-8c67-af478d6b6e20 | -0.14446 | -60.86552 | 2024-11-23 05:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9bf8ee88-bc62-342a-b81f-871e681c7ae6 | -3.2386 | -54.223 | 2024-11-23 06:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 15c2e66d-75e5-3e51-98a3-48f75516b4fc | -3.2569 | -54.2426 | 2024-11-23 06:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 127331d7-7ee4-38ac-9554-7c6e1527e342 | -4.2605 | -48.697 | 2024-11-23 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ee864374-e7e0-3d43-9b6a-36635e9356f0 | -1.7359 | -52.7181 | 2024-11-23 06:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 837bfb50-bad3-3cbd-ad9e-c11861879a8a | -4.6085 | -46.5002 | 2024-11-23 06:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 81496ac2-1281-39dd-9f14-ce18625b4417 | -3.2385 | -54.2431 | 2024-11-23 06:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| da1a1961-1f8d-3789-8886-7124e00dddaa | -1.6075 | -52.5977 | 2024-11-23 06:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0fc88b7e-661a-3e90-896b-7c97500eea25 | -3.2569 | -54.2226 | 2024-11-23 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 986f0d3d-2388-3ea0-9cbc-c821d5f8a9b2 | -4.6085 | -46.5002 | 2024-11-23 06:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 136.2 |
| d352ef9e-aa0a-3462-b398-aa0e4a8432db | -4.5403 | -42.9066 | 2024-11-23 06:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0f729aa8-29c2-3143-80e3-4c9847a248c0 | -3.2569 | -54.2226 | 2024-11-23 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 5c861f88-1e8e-3a32-9c14-cdebb4f76245 | -3.2385 | -54.2431 | 2024-11-23 06:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6db0e395-adab-3f52-b4ff-858872518aa4 | -3.2386 | -54.223 | 2024-11-23 06:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| c13bfdaf-31a4-3742-8048-0903b7882229 | -1.7359 | -52.7181 | 2024-11-23 06:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| c9fe8bf7-97e6-3994-a0bb-356dc36434e7 | -4.2605 | -48.697 | 2024-11-23 06:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 485e4f94-fc3a-3271-bae8-1d29d7d633e1 | -4.6271 | -46.4992 | 2024-11-23 06:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 586df73a-f34f-3144-b277-a721b31b12b2 | -1.6075 | -52.5977 | 2024-11-23 06:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e505ed47-e74d-3982-96d5-abedbb374425 | -1.2596 | -51.762 | 2024-11-23 06:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a001cd1c-1105-3d92-8cc0-7cb07dc07770 | -4.5403 | -42.9066 | 2024-11-23 06:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 3f3d1d04-e6af-3b8c-a0d8-2010d5b8d8ed | -3.2385 | -54.2431 | 2024-11-23 06:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| a9a1592f-9238-3810-bbbf-07596c3431a1 | -1.7359 | -52.7181 | 2024-11-23 06:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| df99054d-ba25-37d2-a5a2-67ca9220a78f | -4.6085 | -46.5002 | 2024-11-23 06:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 12fada79-b29c-3f9e-ae98-600832f9abff | -4.6271 | -46.4992 | 2024-11-23 06:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 24b52325-8210-3375-af04-f1984d872a88 | -3.2386 | -54.223 | 2024-11-23 06:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| a7fc4054-9c26-3bdf-872b-30a56ffa3b71 | -1.6075 | -52.5977 | 2024-11-23 06:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5f6960e4-d3bc-3538-9d5d-50aa71544c72 | -4.5216 | -42.9078 | 2024-11-23 06:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 1bdb08e3-ec60-38e3-ac4a-85eed7085c85 | -1.7359 | -52.7181 | 2024-11-23 06:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9721ed44-1054-35f4-8a01-996aeb8ceffe | -4.6271 | -46.4992 | 2024-11-23 06:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9fee6194-47dd-33e9-82f1-a46ae9bd23f9 | -3.2385 | -54.2431 | 2024-11-23 06:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 91be801f-2bd2-3b77-ba5f-83fe70b45cae | -3.2386 | -54.223 | 2024-11-23 06:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 1dceb285-5b34-3e4b-a2cf-34cde84b6e16 | -4.5216 | -42.9078 | 2024-11-23 06:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6c28355a-80d3-3873-b525-258ef0a0a3ba | -3.2768 | -53.8199 | 2024-11-23 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 5ed61d43-ee40-3bce-9195-d1e1a9569397 | -4.6085 | -46.5002 | 2024-11-23 06:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 111.4 |
| e40b114d-d420-3e10-85ad-b104108fdfc0 | -4.5403 | -42.9066 | 2024-11-23 06:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 7c191c9a-7cda-353e-ae68-1c1786673899 | -1.6075 | -52.5977 | 2024-11-23 06:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 11062c16-f62b-38fb-8e13-cf77dd53123e | -4.5403 | -42.9066 | 2024-11-23 06:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 2eee1286-0c2d-3e9a-98bb-fe264fed63e0 | -1.7359 | -52.7181 | 2024-11-23 06:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5fca9aa5-d8ab-32e6-9ae1-20c63a506b0b | -3.2569 | -54.2426 | 2024-11-23 06:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 603080ed-b769-34de-a960-32ee94b32171 | -1.6075 | -52.5977 | 2024-11-23 06:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 5068c96e-63c3-31e9-b718-7c05be39e8ce | -3.2569 | -54.2226 | 2024-11-23 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| b7fd42e1-2adc-3b04-aed0-b857f0778910 | -3.2386 | -54.223 | 2024-11-23 06:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 434dfd25-41f2-31d9-86a8-83ec3980c05c | -4.5216 | -42.9078 | 2024-11-23 06:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d0819ea5-2349-3a3e-bac7-7033a641bc84 | -3.2385 | -54.2431 | 2024-11-23 06:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9eaba34d-9eb9-39b2-af04-2cb399beaf2b | -4.6085 | -46.5002 | 2024-11-23 06:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 127.1 |
| d88c4ebc-fa60-32bf-9acd-10406dade42e | -4.6085 | -46.5002 | 2024-11-23 06:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 148.0 |
| a595045e-8fa0-3128-888c-e6029935b97c | -1.6075 | -52.5977 | 2024-11-23 06:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 704c6538-f620-3aac-8b51-f55b3b83dc6c | -3.2386 | -54.223 | 2024-11-23 06:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| cfe14d23-5a4d-39ef-9835-16f18a982d1a | -4.5403 | -42.9066 | 2024-11-23 06:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 50ffa2ff-af86-3c52-8ba9-970675b4100e | -3.2569 | -54.2426 | 2024-11-23 06:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| af12c993-f6c8-3f20-bd55-2dd108e0f366 | -1.7359 | -52.7181 | 2024-11-23 06:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 3b4169eb-748c-36bb-8b41-4250c729882d | -4.5216 | -42.9078 | 2024-11-23 06:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 54ed364e-41f1-398a-864b-18780c155347 | -3.2385 | -54.2431 | 2024-11-23 06:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 91d04846-9fa2-3543-98d1-20c27d9716a1 | -3.2768 | -53.8199 | 2024-11-23 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| b13a417e-bbf2-3937-bc85-4c31923ef11c | -3.2569 | -54.2226 | 2024-11-23 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 27c2548b-05e7-3087-8117-08b2d297d9ac | -3.2569 | -54.2226 | 2024-11-23 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| f6d3035a-16be-3a08-af6e-aa1d25209d0f | -3.2569 | -54.2426 | 2024-11-23 07:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 290e7cc1-d0ed-38d9-bf1a-a9a58bd336ed | -3.1273 | -45.3861 | 2024-11-23 07:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 65aa8184-f5cf-31e5-bb2e-5d0fc770b0e8 | -4.2605 | -48.697 | 2024-11-23 07:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f96dbd76-86a7-3443-85ff-70d1eb22d437 | -1.7359 | -52.7181 | 2024-11-23 07:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 276a6ded-502a-347f-81f1-69ae4ae717ae | -4.6085 | -46.5002 | 2024-11-23 07:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 35292a5e-27b0-3485-80ee-419185b657c6 | -3.2385 | -54.2431 | 2024-11-23 07:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 5d539238-2aa3-3fe3-ac60-bba8b0096b05 | -1.6075 | -52.5773 | 2024-11-23 07:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2983ee5b-1b0e-3412-b077-a347f18d8021 | -4.5216 | -42.9078 | 2024-11-23 07:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 65912176-0dae-3ac1-aa1d-0fde01932048 | -4.5403 | -42.9066 | 2024-11-23 07:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| bca52660-0242-3c7e-b4c2-63bbb63245b7 | -3.2768 | -53.8199 | 2024-11-23 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 3e9e957b-2ef7-3a27-8baa-60149f410a5c | -3.1272 | -45.4086 | 2024-11-23 07:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| a7600de9-daff-370b-a1b7-db7cb3984999 | -1.6075 | -52.5977 | 2024-11-23 07:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 09c75469-f763-3d67-9fde-777a220b6a13 | -4.6271 | -46.4992 | 2024-11-23 07:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| e9ab17b3-4d2e-3e54-b8d2-ff04a8c6f986 | -3.5159 | -53.8132 | 2024-11-23 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 35b5af7d-5f53-3626-b990-2abf13b5a7bf | -1.6075 | -52.5977 | 2024-11-23 07:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8d319f37-ac4c-3e46-987a-eeba5967a816 | -4.5403 | -42.9066 | 2024-11-23 07:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 0ce7e3a7-26f2-3662-92e1-2c47c34f6ec6 | -3.2569 | -54.2426 | 2024-11-23 07:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 626e0bf4-76eb-3546-a6c2-3c36b4c37a43 | -3.2386 | -54.223 | 2024-11-23 07:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 3d03f8c8-0861-3e57-a0b5-3e2ebfeb9e39 | -3.2768 | -53.8199 | 2024-11-23 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 02d94b12-563b-315f-8a43-044e10d78243 | -3.1273 | -45.3861 | 2024-11-23 07:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 187.1 |
| dd019f38-c374-3a3a-bdbe-3eaadb521ca5 | -3.1457 | -45.4079 | 2024-11-23 07:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 8a4b2bc0-e50d-3dc8-8ea5-5dd43e334c31 | -4.2605 | -48.697 | 2024-11-23 07:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d97e072d-075c-3fad-a1fe-15e2f462d66b | -1.7359 | -52.7181 | 2024-11-23 07:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 30484c29-ec97-3f1f-971c-446d1de21831 | -4.5216 | -42.9078 | 2024-11-23 07:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| cad78f7f-d2fe-3648-99f0-63cbef1ebeae | -3.1459 | -45.3854 | 2024-11-23 07:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 9ecbae50-f0c0-316a-94f5-7a2ae76257e8 | -3.1272 | -45.4086 | 2024-11-23 07:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 311a41df-3345-3f45-911f-64b58775d810 | -4.6085 | -46.5002 | 2024-11-23 07:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 90fd68b1-5529-3d5a-bb7b-d8bb5ebcb80d | -3.2569 | -54.2226 | 2024-11-23 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 91f1883e-89c6-3414-a3fd-5d37d0d69fc4 | -3.2385 | -54.2431 | 2024-11-23 07:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4b996859-4930-39e5-942c-7b6ee3146dc5 | -3.2768 | -53.8199 | 2024-11-23 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2b8c8e13-4a58-3b59-aded-903622a0f8a7 | -3.2385 | -54.2431 | 2024-11-23 07:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| b226fe93-7dc9-3220-ac22-132e2f93718d | -4.6271 | -46.4992 | 2024-11-23 07:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |


[Clique aqui para ver as próximas entradas](README68.md)
