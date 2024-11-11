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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d328143-e7e2-3c6e-8cc3-5bd6acc53c84 | -1.7573 | -53.756802 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6306b89e-47a2-34cf-a4de-807f25f48609 | -1.3193 | -54.636398 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3121577-61c0-3e34-bb97-00ca3d79d69a | -17.5798 | -57.4207 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f91fd8a0-8073-3ab2-8361-838e10a0df1c | -1.3879 | -52.368599 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c56d8c52-2055-3f26-88a8-966910b7eab2 | -2.3756 | -50.3381 | 2024-11-11 00:51:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cdd4e50-abaf-3180-b9ae-38fb47cf359b | -3.8925 | -52.406101 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 235f37a5-10ce-3783-87c7-9ee7c3f8b466 | -3.4441 | -51.573399 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b1f84de-618e-377c-ba24-3706de9b116f | -0.6503 | -52.5261 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22834d21-1bcb-3782-9250-87f7b604e901 | -1.6207 | -50.688 | 2024-11-11 00:51:00 | METOP-C | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f7c271a-b867-3315-a6d4-40e7d93e7732 | -3.9546 | -46.412498 | 2024-11-11 00:51:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d13baec6-4e1a-3e57-958a-d2ecc361ec82 | -3.8795 | -52.394501 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 169e5a29-ac01-3e34-8f6e-05db80e4755a | -2.7124 | -49.2966 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4988b49-579b-35c9-b1ba-569f6d610f07 | -2.0975 | -46.5266 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e29c6604-6b33-368a-a08f-eb95913051b7 | -2.4482 | -53.938599 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98d84be6-d061-37de-a088-cd4d670702f8 | -2.4283 | -50.521702 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01ba1eb1-df3e-3090-b262-b25bba4986f7 | -3.34 | -50.135799 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 689686be-f5a0-3be2-8a8f-4af8d6e6ad2f | -0.8327 | -53.051399 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f68e47ee-24b3-3713-982f-7d1b49dc7152 | -3.8957 | -51.923401 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0385ed4f-2dd3-31fb-bf8b-6ccc15ccecce | -1.8686 | -54.198898 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 491549a8-c30c-309b-9624-b83fa40fb715 | -3.0511 | -50.4039 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12fe274e-7bec-3bd7-ac03-043c2fb313a1 | -2.8335 | -52.555302 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7730bf7a-ab94-3b7c-a512-cd64cdc4ee9a | -2.2234 | -53.6759 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a872dcfd-5df8-30be-b7ae-6c7eb57c1d6b | -3.2267 | -53.057999 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2adee23e-2b62-33c2-8883-2103712f7001 | -2.775 | -49.388401 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 663c03ca-5fa2-3ec6-b043-66b70bbaa9bc | -3.2666 | -48.752102 | 2024-11-11 00:51:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57e098fe-540a-3c64-9afb-04c04dc35f9a | -3.2991 | -45.341999 | 2024-11-11 00:51:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af1cedca-bd1e-384c-900f-9d997876d769 | -3.5318 | -54.083 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb2358d2-1e01-3d0f-900e-69ecf1ff84dd | -4.2806 | -50.679199 | 2024-11-11 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 047975da-7a70-34c8-a27a-25c1b34d8efc | -3.0266 | -50.968601 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da1d2904-e90a-3534-80b0-c6522fbc1a82 | -2.873 | -49.366199 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aabe8c8-6376-393d-af30-0e06ee708931 | -2.7606 | -49.326599 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29a008a6-26e7-341b-90e9-d01bfb68d881 | -4.279 | -50.672298 | 2024-11-11 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32465e67-2cb2-304c-9e77-a27e0c42d70d | -2.3758 | -53.847198 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 771e3dc7-1ccd-3622-a011-176aa9d34ab8 | -3.7596 | -51.824799 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a135e369-cb06-30f8-a228-36065917ebd9 | -4.1205 | -43.5821 | 2024-11-11 00:51:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0637a8fb-0ddf-3124-8aad-62c8dc59506d | -3.626 | -50.6147 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8add108b-2055-34ae-88af-ed7d941b5562 | -3.0896 | -51.063202 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cacd3f5-3825-3bd8-bd6a-45f8bd64c9b0 | -3.2508 | -53.707001 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a30c9b33-8f18-3383-bc55-f7fdb7a8c0e1 | -3.1037 | -49.426899 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f0f164a-b860-36e9-904f-37ba2fa0c855 | -3.2178 | -50.276501 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86d2c182-b1aa-3be3-b59b-3d459a347fad | -2.3204 | -50.679798 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 936e2c35-56bd-3f2b-902d-c42d6a6decbe | 1.4864 | -56.017502 | 2024-11-11 00:51:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e1cc74c-2226-3556-a559-08918ba6084c | -2.7705 | -52.866299 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8235c9e4-17cb-398f-9f52-cc1a106c21c2 | -3.6592 | -50.221802 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d64ff4bf-1fea-389e-a185-b26e2892117e | -3.5872 | -53.464401 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfb8d836-1919-3900-8495-d2173a134c42 | -1.4008 | -52.380001 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bad08790-9985-3494-af28-2a88e0eeb4a7 | -2.7678 | -49.357498 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6fa134d-959a-3968-8f13-2c3ce981d663 | -1.2032 | -53.6334 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e3fcabb-6fd3-30af-a480-00a6591303f3 | -1.3895 | -52.375401 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc3019db-77bc-3a78-9bf3-59fa18345223 | -17.5776 | -57.520802 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f4000cd8-1f9c-3734-a85f-84b977dc41da | -1.5407 | -55.877399 | 2024-11-11 00:51:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61328017-cf1d-3d82-8202-4246a187034a | -2.6313 | -49.881599 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad4b97cc-c235-3c7d-8639-9e3d1e49269e | -3.2438 | -53.4044 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95645e92-361b-32bd-9c27-e0478264da85 | -3.0863 | -49.574402 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bec80b2-edd1-3295-bbe3-0e0cba9d35a1 | -5.9744 | -45.377201 | 2024-11-11 00:51:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1e00365-c46b-3c58-bc8e-7941efd1505f | -2.1001 | -46.537899 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 595edf3d-bb09-32b8-a563-26e9e1d66de7 | -17.5895 | -57.4188 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8b93614e-66cb-3124-8bdb-fc3de84d3578 | -3.3388 | -51.654202 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c259d8e-743f-3e33-94dc-d3db0bd5b5e2 | -3.1296 | -50.430901 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a87fd27f-1271-3440-9351-21dc97f49fbd | -1.2325 | -51.781601 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f24559dd-c04f-3f27-8612-2f2ba71583b7 | -2.5893 | -51.7146 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cba018c-d5f3-388e-8967-a0b7ef837503 | -1.1982 | -53.701401 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbbac258-bd63-349b-ae97-cc1e8f1e9d90 | -2.1957 | -53.734901 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af6a43ff-0db6-30aa-ba5c-0db91a508738 | -17.697901 | -54.098801 | 2024-11-11 00:51:00 | METOP-C | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0f0d89-193b-3450-a2f3-8274703de0c7 | -2.5085 | -49.886002 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 555d265c-755c-3431-941e-90cfca85950d | -3.0282 | -53.272598 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5de347b-9193-3d61-a6ee-4ae4546f7b27 | -4.1152 | -48.498199 | 2024-11-11 00:51:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c293952-c0dd-3db5-9726-667ecb1094d1 | -2.8285 | -49.130001 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b056b1b-3620-3441-8c90-8c97246e7341 | -1.1457 | -53.787601 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88d88cfa-aa65-30fb-be8e-3fd96a3ae408 | -2.9368 | -54.456001 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00e7a28-40d4-372f-991f-898a45a97336 | -3.1965 | -50.273701 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a3c31e5-262a-3706-a43c-0ef61b980938 | -2.2382 | -53.786201 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08360dce-c250-31b5-884c-87f1bc44d69a | -3.0495 | -50.396801 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af70b2f9-1085-3f5c-92c5-285a3a1b5bba | -2.5755 | -48.130901 | 2024-11-11 00:51:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 354d51ca-9430-3a1a-b03d-856c43f3e403 | -1.2229 | -55.792801 | 2024-11-11 00:51:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebd90e15-dae2-39b9-8ced-8931c1bc68a9 | -2.766 | -49.3498 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d751373-8347-3430-b375-3e918996ab8f | -3.2568 | -48.754299 | 2024-11-11 00:51:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc503f7c-95b2-37e1-b2a0-e48a73b25a4d | -2.9684 | -53.869801 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45b3aa52-621f-3f84-b78e-38103f80a212 | -1.9586 | -54.186699 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fff2ff3e-4558-3248-86d6-e0a1043ae35b | -2.733 | -49.3409 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8893b055-f962-3c7a-9d74-a7e79561eb51 | -2.9245 | -49.499599 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94fceb54-5572-3ba5-acea-cc4d2aadb08c | -2.9434 | -49.358398 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd0fbfaf-96c7-3edc-b68c-d4d2bee2ded6 | -3.5312 | -45.712799 | 2024-11-11 00:51:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e420973e-92c7-36a9-a551-1433346a92f6 | -2.1759 | -53.694 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0933851a-6fd1-320e-aaef-67367e630c0d | 1.555 | -56.032902 | 2024-11-11 00:51:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0bfe915-c9df-3276-9dd1-b0455a862814 | -2.2561 | -53.729099 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 103d8911-7d39-37ed-90a0-5fa2c994fc73 | -2.7598 | -49.3675 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d280f423-80e0-3791-8538-16c821f114b4 | -3.6163 | -50.5728 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d381780-d82e-3814-b27b-e3df799fa634 | -2.8778 | -46.650299 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87386d16-b08d-398b-a875-5f570afbdaa9 | -2.9725 | -45.8298 | 2024-11-11 00:51:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99312268-f1e1-366c-8784-f31f40fef875 | -3.2832 | -53.260601 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4675d73f-c768-3e78-ad54-a0611e6190ee | -3.252 | -53.395 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c255263b-6dd2-3052-ab13-edc5b3f909a4 | -3.6065 | -50.575001 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b7efbef-e687-3a73-ad4b-77dd627f615d | -3.1394 | -50.428699 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c34b9b4c-af71-3b65-a568-ca03e1dcb196 | -2.1764 | -48.8531 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ff926c-52c8-313c-9c2c-56f5e6bdfa6b | -1.5485 | -51.854198 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 172b86d3-1bfe-3c27-8ce8-099dd9fd99c9 | -2.17 | -50.519798 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 507c7aa0-d074-3c7d-be93-4224d23749c5 | -2.5377 | -47.307701 | 2024-11-11 00:51:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a50974fa-258e-31b6-a119-267310f657d0 | -3.0951 | -54.2915 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1920f977-f546-3e9e-9f89-8a28bb42500a | -1.3777 | -52.413799 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
