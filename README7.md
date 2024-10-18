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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30d70bf9-7cac-3bb4-b1be-4ed81eb020c8 | -2.46079 | -48.34586 | 2024-10-18 00:43:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a9bc3de4-8550-3475-9935-efefd8eae725 | -2.45513 | -48.61399 | 2024-10-18 00:43:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5295f99c-1fe0-3aa1-a83b-d7df9ba35d99 | -2.44537 | -48.61533 | 2024-10-18 00:43:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b4e38d84-5861-3f94-92e0-750c96501d72 | -2.4431 | -45.89083 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0fb2fb32-5c90-31f6-a2f2-8cd21ebd5a11 | -2.43427 | -45.89207 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 99418fe1-0d57-3e0e-8870-df69dfaef5cb | -2.42423 | -45.88454 | 2024-10-18 00:43:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9524cf5-c9dc-31aa-8897-95051e6d0a84 | -2.41293 | -48.89061 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e6119ca7-2f69-30a8-912b-b5e8da296f8c | -2.41125 | -48.8852 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 52a70026-d845-371f-af8b-6946cd6a4048 | -2.36017 | -47.61349 | 2024-10-18 00:43:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4231d7f5-8d1e-30a4-8428-0377bc9d0226 | -2.35884 | -47.60382 | 2024-10-18 00:43:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| feb038cc-12a5-374f-8d1d-108027f8edb0 | -2.35159 | -46.49181 | 2024-10-18 00:43:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b196990b-7e15-3797-89cb-5161ac9e3a13 | -2.35035 | -46.48291 | 2024-10-18 00:43:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c9e8ac6a-5ed7-3e56-b79f-87d40e0ae05c | -2.34297 | -47.22059 | 2024-10-18 00:43:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7c70e931-19b4-39da-839a-66e08c25a5f5 | -2.34147 | -46.48414 | 2024-10-18 00:43:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 1c11b1dd-d47b-38b1-80b3-486414e570f7 | -2.33135 | -46.4765 | 2024-10-18 00:43:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8d34ad78-e0c9-340d-8d73-915854fb892d | -2.33011 | -46.46761 | 2024-10-18 00:43:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d97779c9-0a6a-33b4-827b-e103d3736df9 | -2.32534 | -46.76019 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 257d9864-6d0f-34e0-b15c-4a9e03df5344 | -2.31572 | -46.23489 | 2024-10-18 00:43:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 232ea721-d33d-3d68-8b35-9b5f41920782 | -2.30424 | -46.60759 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d8f85521-8e09-3418-8256-f2b6f5a24003 | -2.303 | -46.59866 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e7bc6359-2649-3aee-990d-5239564f8be5 | -2.30177 | -46.58972 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| badb15ad-a0ff-34be-916f-eab225b10c6b | -2.28019 | -47.90976 | 2024-10-18 00:43:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0cab2b2-1ca1-378d-90b8-00fa30741a0a | -2.26135 | -46.76579 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0e3b9a3f-7900-3907-bc76-3bb30f32b620 | -2.2601 | -46.75679 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e8c37075-2d86-3f94-bede-090a489e9acb | -2.25884 | -46.74778 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2140f07e-0af4-32e0-9ab3-c2d9f542163b | -2.25635 | -46.7298 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f3bbb3a6-378d-3133-87ce-8c4bbd592ff0 | -2.24348 | -46.7683 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 08eab861-8cd7-3f38-a30f-9b39f9f1085d | -2.21956 | -46.33529 | 2024-10-18 00:43:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82f31534-a7d7-374c-a338-aa47931c09c9 | -2.21586 | -46.30877 | 2024-10-18 00:43:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 23cc58d4-3811-3dd2-9de2-c68adb5648af | -2.20578 | -46.30117 | 2024-10-18 00:43:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7cba1495-c4e5-3092-9958-9e68d174a65c | -2.19227 | -46.73598 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b63aa1d0-bcb9-3ba3-ac7c-48a749f19b77 | -2.19125 | -46.45668 | 2024-10-18 00:43:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 557f4249-a923-3f54-9376-7947de290615 | -2.18608 | -48.73609 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 5a4fc965-343d-3171-ae5d-b8c5f05473bd | -2.18455 | -48.72514 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| b4c86132-8a97-38bc-9059-501be6c89391 | -2.17629 | -48.73745 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6e963252-1e3f-3db7-85b0-f6ea05a62054 | -2.17476 | -48.72646 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 014a2d04-6eb2-3ff9-b2a1-69c0a7d057a6 | -2.16342 | -48.40568 | 2024-10-18 00:43:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 85fcd387-d77d-3e1e-80b0-b4847e4732c3 | -1.99489 | -44.78874 | 2024-10-18 00:43:00 | TERRA_M-M | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a125a5a1-74a9-3b01-b4e6-1be8d1f20258 | -1.99363 | -44.77967 | 2024-10-18 00:43:00 | TERRA_M-M | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f93925aa-1642-30c9-9135-aefeef0d1eb6 | -1.8735 | -47.88626 | 2024-10-18 00:43:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3ca8a7d5-21e3-3387-a04c-1b4c428e214d | -1.8667 | -47.83748 | 2024-10-18 00:43:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e6774b25-1aa5-3851-b45e-9237d94bbb5b | -1.85879 | -47.84855 | 2024-10-18 00:43:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| efedf1eb-f745-3546-8127-9dc49442b1ef | -1.85744 | -47.83879 | 2024-10-18 00:43:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c5341d07-4c63-39c0-8efb-c0f8ca0a904a | -1.74488 | -46.17234 | 2024-10-18 00:43:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fa0de741-0024-3d4f-bdb7-eb54804b1e29 | -1.6005 | -47.0922 | 2024-10-18 00:45:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 2206a031-248a-306f-885e-46448e52fd02 | -1.619 | -47.0919 | 2024-10-18 00:45:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| d4b474c0-0a58-3ce6-82a9-f64d65ef28d9 | -1.6191 | -47.07 | 2024-10-18 00:45:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 37c12f97-6570-385a-bf2c-11241a55342f | -2.7045 | -54.656 | 2024-10-18 00:45:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 1a0b5df0-b8a6-3db8-947c-3c97671e69b5 | -2.7229 | -54.6556 | 2024-10-18 00:45:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 1a9a98e6-3169-351c-b5ee-6f62a7a9a174 | -2.8795 | -51.6695 | 2024-10-18 00:45:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| c95ad68b-e185-3f36-ab9d-1c1b130cc577 | -3.1382 | -51.497 | 2024-10-18 00:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| d22ee914-70c1-32bb-9744-d4cbf3c9ed38 | -3.1383 | -51.4763 | 2024-10-18 00:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 8d9832de-fe81-352c-90a8-a627dfd5239e | -3.1566 | -51.4965 | 2024-10-18 00:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 2e50d557-f85b-3407-96c0-bdfdca4a118b | -3.1567 | -51.4758 | 2024-10-18 00:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 024f968e-265d-3890-a7c5-0b9ebd535c2d | -3.2862 | -47.133 | 2024-10-18 00:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 2f21d337-e3b6-37f7-9ec9-87480af4c3fe | -3.3644 | -50.3023 | 2024-10-18 00:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a476bf97-7fd7-328f-84ba-c10d770fb2d7 | -3.7007 | -45.9223 | 2024-10-18 00:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| e90c03bd-6f3a-3c98-8f79-bafd4fb3949e | -3.7009 | -45.9 | 2024-10-18 00:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 2dfa597c-fe0e-3ff4-9ccb-1cf34292b39f | -3.8733 | -52.0715 | 2024-10-18 00:45:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d242df8f-cc0d-340a-9b2f-4a79fa5c1d6b | -4.4072 | -45.9773 | 2024-10-18 00:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 844a8994-5c79-3da9-be59-985023696165 | -4.4257 | -45.9987 | 2024-10-18 00:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 91cc83e4-0063-36e1-8199-0396e0ad3a2b | -4.4258 | -45.9763 | 2024-10-18 00:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 239.2 |
| acae6dd2-52a7-3cc7-8d50-d1ba2a480922 | -4.426 | -45.954 | 2024-10-18 00:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 995687c2-0e76-382f-a639-014fca9ae336 | -4.5613 | -48.0358 | 2024-10-18 00:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 62305152-59a9-33f3-be91-42db2f7f0e05 | -4.5614 | -48.0141 | 2024-10-18 00:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 37acd8e7-defa-378f-9ce0-1f0bb74ce187 | -4.5799 | -48.0349 | 2024-10-18 00:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 246932c9-9ae5-3b03-863d-3d2dfe71adcc | -4.58 | -48.0132 | 2024-10-18 00:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 9c06ba93-ff55-33aa-8a0a-fc87fcb3542a | -4.6653 | -46.3418 | 2024-10-18 00:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 67a254d2-282d-3940-b480-be556a71e768 | -4.8917 | -45.928 | 2024-10-18 00:45:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 0b90bb81-da21-30f0-92ef-d2bfb5e031c9 | -4.8919 | -45.9057 | 2024-10-18 00:45:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 486cfb26-9e94-3376-98c7-a2990a642050 | -6.6886 | -70.1171 | 2024-10-18 00:45:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c5e836ed-1be2-3159-aef3-3c7d13681cc7 | -9.4203 | -35.7801 | 2024-10-18 00:45:58 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| 0d21648e-13e4-3dae-8b3e-559dc085eed7 | -11.4859 | -65.1198 | 2024-10-18 00:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a79c178b-b873-3c7c-b6dc-aad0fcd50cc9 | -11.5046 | -65.1189 | 2024-10-18 00:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e5a8f23a-4c61-3067-9174-dc87f623548e | -12.5045 | -55.205 | 2024-10-18 00:46:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b24b5dea-876e-3dc0-a936-f06eac007b10 | -12.5048 | -55.1846 | 2024-10-18 00:46:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 2702c5d5-3675-3c4e-8d1d-c4c6a1bb1c2d | -12.5238 | -55.1828 | 2024-10-18 00:46:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3f64ff79-9a7c-36c8-9b9b-0e232fff9f88 | -12.4775 | -63.2268 | 2024-10-18 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6d321d03-21bb-3943-9e7a-8e50a64e0331 | -12.4964 | -63.2258 | 2024-10-18 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 52b7f28d-3bfd-32d3-9077-a78ac52573a5 | -12.4966 | -63.2066 | 2024-10-18 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.7 |
| c8691fd8-b72e-3af8-9aac-7c3a7505033a | -12.4967 | -63.1874 | 2024-10-18 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| fc2cbe8e-b1c1-3d5e-8aea-ed226e00fdb5 | -12.5155 | -63.2055 | 2024-10-18 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 3b2fc52d-bb18-3d97-94b2-e8f582d7dd19 | -17.189 | -45.4644 | 2024-10-18 00:46:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ab4c77c5-2a8e-3986-9168-7d77ed7d348e | -17.209 | -45.4602 | 2024-10-18 00:46:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b5e86306-4d78-3353-a7d1-47d59a0c9130 | -17.0191 | -57.4768 | 2024-10-18 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 522f8ab4-62df-3706-bae8-af4ed0a29e1d | -17.2177 | -57.3102 | 2024-10-18 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| b1075272-73ce-3255-8c0c-2e537896b188 | -17.237 | -57.3284 | 2024-10-18 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 7a1c99a2-42be-3adf-8da7-306d139b0467 | -17.2373 | -57.3079 | 2024-10-18 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 189.7 |
| 7e23b40c-9559-3618-ac68-f4fe427dd058 | -17.7851 | -57.4679 | 2024-10-18 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| c74dc62c-97c3-3833-bf79-a18fd4944d75 | -17.7855 | -57.4473 | 2024-10-18 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.9 |
| 389063d4-5f93-3748-a69a-52361b0f9343 | -17.8045 | -57.4861 | 2024-10-18 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 9dc075fb-e121-30da-bff8-d77b92449dbd | -17.8049 | -57.4655 | 2024-10-18 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 192.9 |
| d076bc38-94ae-3128-b355-3073a41c2a06 | -17.8246 | -57.4631 | 2024-10-18 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 78d01c05-b99e-3588-8b1f-ce204075b605 | -18.0632 | -57.3514 | 2024-10-18 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.2 |
| f72c8c3a-a76e-3759-9895-db2d89551778 | -18.083 | -57.3489 | 2024-10-18 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| ffa962c9-513f-3009-8983-7dbc61081b80 | -18.2537 | -56.6237 | 2024-10-18 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 181.0 |
| f5a49f37-9279-338f-9ba5-2b042be4a5d8 | -18.254 | -56.6029 | 2024-10-18 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.8 |
| a4307bec-e745-3af9-ab7b-3c037f0edaa6 | -21.9662 | -49.7186 | 2024-10-18 00:47:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 132.8 |
| b953528f-837d-339d-8565-faf291f7bb9c | -23.3701 | -47.3747 | 2024-10-18 00:47:14 | GOES-16 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.0 |
| 74b7c564-dbf7-3554-b364-16e28550e206 | -23.129299 | -45.5513 | 2024-10-18 00:50:15 | METOP-C | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README8.md)
