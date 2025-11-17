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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65a7366f-d90e-38d8-a3a7-6e0c2a49b4dc | -9.5147 | -40.3558 | 2025-11-17 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 38922c5e-c080-3d3e-ab86-9b8d9cfae507 | -6.6875 | -42.0296 | 2025-11-17 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 415.6 |
| bf86fffd-8035-3f76-858e-3a807eff4f2b | -4.1781 | -50.2091 | 2025-11-17 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 476d5246-6134-37bc-86ea-77aed8f8d6a1 | -10.669 | -49.3597 | 2025-11-17 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 71905e78-ce34-33c6-8019-7eae1b913619 | -20.3302 | -57.7806 | 2025-11-17 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 6c8b5bc5-ba64-317e-a64d-69c35eb29029 | -6.6875 | -42.0296 | 2025-11-17 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 394.7 |
| daaf4ff5-74e0-3b8d-9a75-1fb277dbf2b3 | -9.5343 | -40.3282 | 2025-11-17 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.7 |
| a4771b60-0ef3-31e0-8b4e-cbbf0ea9967c | -2.5053 | -47.812 | 2025-11-17 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| a5d14886-d2c7-322f-955a-9414f59a74dd | -11.7021 | -48.8474 | 2025-11-17 00:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| efe9113d-eb91-3451-93c5-91e4a0a2b15d | -6.6684 | -42.0553 | 2025-11-17 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| f549dfd8-4f72-3d24-9f53-0abd7f3956f5 | -2.5238 | -47.8115 | 2025-11-17 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 5fa590fe-17b3-3eb6-8045-25a2ae8563de | -11.8295 | -49.2242 | 2025-11-17 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ae1e54ba-9545-3379-8cff-abc3e0cd2c69 | -9.5147 | -40.3558 | 2025-11-17 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 141.9 |
| b08b5af5-6c58-30d9-af82-7699537f9b7c | -10.8936 | -44.6378 | 2025-11-17 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| f22165da-3df3-3bc8-a8f9-8ec2470fe77f | -11.8486 | -49.2218 | 2025-11-17 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| f438256e-d52d-3acd-b9e5-180db8fe46f3 | -4.9967 | -44.3607 | 2025-11-17 00:30:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| de6a3187-a4e4-3793-af5e-755676f0768f | -2.5238 | -47.8332 | 2025-11-17 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 622075d5-2411-3d03-aa8c-99e214f5e6d9 | -12.853 | -46.462 | 2025-11-17 00:30:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| b42e7710-b792-3965-83ab-a02d843748ce | -10.6687 | -49.3813 | 2025-11-17 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 887cddc4-aad4-3641-8d80-5105f4557a5b | -10.8745 | -44.6404 | 2025-11-17 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5f69fab4-4997-319e-ae70-bffcd8a245a5 | -3.2344 | -50.4952 | 2025-11-17 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 80426784-4b8e-3cd7-abb2-09018aa31893 | -9.5152 | -40.331 | 2025-11-17 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 335.2 |
| ef27f71f-aa46-31ec-b612-86c5088f0b96 | -3.7193 | -45.9215 | 2025-11-17 00:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c81abd1e-b994-343a-9c58-6202aac8058d | -11.849 | -49.2 | 2025-11-17 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 28e3b8b3-053a-39b2-af81-1cd9d7a1bcbd | -2.5053 | -47.8337 | 2025-11-17 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c7ab3875-ceb5-39c1-95f2-a8ebfd25f5eb | -4.1596 | -50.2098 | 2025-11-17 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 6e01ac36-1a4b-3757-9d5f-1559c71838cc | -2.694 | -52.0653 | 2025-11-17 00:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6c8d6390-08a9-32a8-84ae-cd1fba00b68b | -11.7208 | -48.8669 | 2025-11-17 00:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 24e6504e-8bd2-3bb7-a6b8-d2ced8086a14 | -6.6873 | -42.0535 | 2025-11-17 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 238.4 |
| 2d76265c-3d4a-3fde-96b8-ef4f6ad93bae | -6.7064 | -42.0278 | 2025-11-17 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 690974ce-a300-3614-9c0f-db121b7db77a | -4.7209 | -46.3832 | 2025-11-17 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 4b6eee64-1565-3c69-9dfe-9388e234eb5a | -6.6687 | -42.0314 | 2025-11-17 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 272.2 |
| 9be9cc14-5f82-31b0-bcf0-5798c60d61e3 | -11.7017 | -48.8692 | 2025-11-17 00:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 3d783e2f-bd60-3632-86ea-ce0a90b921f3 | -11.8299 | -49.2024 | 2025-11-17 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| cffa6cc9-cb7f-32a9-b661-ca19572052e8 | -12.2027 | -54.2663 | 2025-11-17 00:31:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9eda048-fa44-3abb-b09c-500803fe2850 | -4.1685 | -50.2071 | 2025-11-17 00:31:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7026d01-4d2a-3cd3-bc56-829da19fcfd0 | -1.5308 | -55.514 | 2025-11-17 00:31:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6e76103-9c46-3518-b432-e3479181cba3 | -9.5786 | -49.1007 | 2025-11-17 00:31:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35de86aa-c5c7-3c27-a9ff-7784c0654506 | -3.5187 | -51.224701 | 2025-11-17 00:31:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fd64857-aeb4-389a-841d-8199e7578a13 | -10.5451 | -47.9231 | 2025-11-17 00:31:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4f2e015-c770-3fd0-b3d9-41ad1775abe1 | -3.8314 | -55.803001 | 2025-11-17 00:31:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52138626-3078-3a05-8c4a-43ec66e680bf | -12.1913 | -54.261101 | 2025-11-17 00:31:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e234521-1140-3b7f-95d3-c6a286f7e90d | -3.7593 | -51.1068 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c4def9d-6a06-3bf2-a44e-cdba1167b079 | -8.5238 | -46.0732 | 2025-11-17 00:31:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5099c135-c0ea-31c4-9618-697aa6195c39 | -3.6051 | -55.530102 | 2025-11-17 00:31:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04f30127-13af-31da-bf79-3b768d2b5cf9 | -4.0977 | -48.021301 | 2025-11-17 00:31:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a19b5ec8-dfc8-36a5-88ef-8c3e5f23b548 | -8.2905 | -44.194302 | 2025-11-17 00:31:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c973fc33-baf9-3a4a-803b-f805a8387840 | -9.5072 | -47.263199 | 2025-11-17 00:31:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7827767c-618e-3679-93a4-cd2c86fa05ca | -9.3272 | -46.5718 | 2025-11-17 00:31:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6280830e-9f1a-32d8-a712-de394993d64d | -2.5025 | -47.8312 | 2025-11-17 00:31:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eba4907-0741-3af7-a6f2-aac6d9212fd6 | -4.0448 | -49.0186 | 2025-11-17 00:31:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9903e1c9-138b-3774-9308-fa34f18cb8b7 | -7.634 | -48.216599 | 2025-11-17 00:31:00 | METOP-B | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a1b970e-e39b-3dc1-85e8-7a4ccefa0444 | -3.3464 | -51.370602 | 2025-11-17 00:31:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3086f22e-523b-3c90-b3e9-d66785b0e436 | -4.7138 | -46.3862 | 2025-11-17 00:31:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd79297-bb7d-3411-9d07-69247d51575f | -20.333401 | -57.756401 | 2025-11-17 00:31:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 30b9df24-629e-3466-9b0d-691a8bda2adf | -3.701 | -45.925201 | 2025-11-17 00:31:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82e1582d-8e87-34de-8faf-756c749d811c | -3.3025 | -50.069302 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfdf3a1b-7db6-32ff-9081-df5b217d151c | -10.8455 | -46.744301 | 2025-11-17 00:31:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf11b78c-d409-399a-8fe0-bc5072d98288 | -11.8433 | -49.200699 | 2025-11-17 00:31:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c77d94c-96d4-3e17-85b0-e0a571707a14 | -9.6273 | -47.884701 | 2025-11-17 00:31:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 622dfff2-974f-3952-b8af-d4f2b3cf480e | -3.5854 | -50.711498 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 120da0b3-29dd-35a0-ab99-9dfe84de8932 | -6.3501 | -46.146198 | 2025-11-17 00:31:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e12b64b-bb16-3c1f-b536-0874b5cef862 | -3.1799 | -50.6506 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cb79847-2863-3f77-bea0-b9a7b494fb67 | -11.1567 | -49.4412 | 2025-11-17 00:31:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| acd011f4-df36-33c5-8572-02250512a217 | -9.5809 | -49.1101 | 2025-11-17 00:31:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca4c8242-7cb0-3053-b131-faed7afd77f6 | 1.6358 | -55.953899 | 2025-11-17 00:31:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f90ccac7-f3da-304d-8c70-38f1fe74bcf0 | -10.8486 | -46.756901 | 2025-11-17 00:31:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc4ea51f-f931-3ebc-9574-55689cbcbf61 | -8.6878 | -51.285099 | 2025-11-17 00:31:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71d7285b-5fbd-3cbf-a4e0-e5e96859aae8 | -4.1609 | -50.218899 | 2025-11-17 00:31:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad652c7-d335-3039-9db5-8fa84d2d4aea | -11.8356 | -49.2117 | 2025-11-17 00:31:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1724e28-6420-3fa4-a516-b68247a9151e | -10.525 | -44.159199 | 2025-11-17 00:31:00 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 50d5ad4a-cffa-3a6f-86c6-17a02f133d22 | -6.2912 | -43.791 | 2025-11-17 00:31:00 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f75dab38-60ef-3d32-a274-1d6b883be0f5 | -3.4041 | -50.108398 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b954acb4-c9eb-3ec2-8dc6-26e827f4ce88 | -3.7887 | -51.1898 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cdcd25c-76de-3c5b-b59a-34eb6172a605 | -4.3967 | -45.836601 | 2025-11-17 00:31:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f12fb55f-5680-32fb-b259-5609841b58d6 | -11.8376 | -49.220402 | 2025-11-17 00:31:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7190f02-fdee-34ae-93a9-7ee046f09d3c | -12.2011 | -54.2589 | 2025-11-17 00:31:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8072eb18-7ea2-325c-b963-2626a93d2d41 | -11.8474 | -49.218102 | 2025-11-17 00:31:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| daf4d6cb-7ac7-3991-ba2f-7e8b5726aa6e | -4.8838 | -44.8475 | 2025-11-17 00:31:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 301b3dfe-5b07-3c9b-bafc-4036d213460b | -3.7449 | -51.803501 | 2025-11-17 00:31:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea92dff1-b844-32d9-9e0b-4c9bdd7ed232 | -3.7348 | -52.6563 | 2025-11-17 00:31:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bdebcd2-407f-3a0d-b784-16ecd38a130d | -2.89 | -53.288601 | 2025-11-17 00:31:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78e507fe-9200-372a-8baf-e79e12d402b3 | -2.4445 | -56.273899 | 2025-11-17 00:31:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aa63dac-d4db-3cde-88d2-169f5af8babb | -3.7467 | -51.811401 | 2025-11-17 00:31:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb2f5839-4414-32a3-9ffb-c7289fd6ebdc | -8.5298 | -46.055599 | 2025-11-17 00:31:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a628592d-a5f8-39c5-99cc-66255468fd17 | -11.2963 | -48.5107 | 2025-11-17 00:31:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 101534f5-04f6-32f4-b0ce-c3155b8da402 | -7.6366 | -48.227798 | 2025-11-17 00:31:00 | METOP-B | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04c3e648-2270-3bd0-8ef5-2b9c979f8f74 | -3.4368 | -52.885201 | 2025-11-17 00:31:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc582b11-4511-3a15-a142-cfe0a9d7ae08 | -3.1472 | -50.198299 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62cd05bf-63b8-306f-b6fe-494019f6d295 | -8.5728 | -46.480301 | 2025-11-17 00:31:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dba509bd-fa64-357f-80de-f86f3d6aa26a | -6.674 | -42.072701 | 2025-11-17 00:31:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 480ef12a-f1fc-37cd-85ef-38c7ec986315 | -11.2986 | -48.520302 | 2025-11-17 00:31:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59ba4bbc-eb8d-3165-8425-aef4ff245809 | -4.1542 | -50.190399 | 2025-11-17 00:31:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32700a46-6352-39ed-b946-ea4b7fcdfe9c | -4.7098 | -46.369598 | 2025-11-17 00:31:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c56be432-ec5b-3652-a10a-7eb6877157c2 | -9.1535 | -48.059101 | 2025-11-17 00:31:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1efc7dcd-eb42-322f-80c9-c73752d28c77 | -9.5689 | -49.103001 | 2025-11-17 00:31:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d071b092-206c-3fea-88c6-500d0d6e407d | -3.5738 | -52.089802 | 2025-11-17 00:31:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d3a4ff8-8dae-3eee-8bc1-fa14f9857e2b | -11.7249 | -49.835999 | 2025-11-17 00:31:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63643578-085d-30c1-ada6-bce541bb9ca7 | -2.691 | -52.0592 | 2025-11-17 00:31:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3806c861-53e5-3f5d-a868-f64c5a5762ab | -10.9604 | -44.530701 | 2025-11-17 00:31:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
