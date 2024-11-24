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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 639bb8ac-e618-39b9-b56f-1ea7b2159828 | -4.09034 | -50.36625 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad6abcbf-61db-3668-8c5b-d54c6793c956 | -0.84353 | -52.55082 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96aed245-998b-3e81-b5f1-daf65fd64f1e | -1.60862 | -52.59511 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 026be97f-0e82-3d24-813a-bf2c6fe11aee | -2.95412 | -53.71526 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 155cdc1e-403b-3f51-8b36-1d630e6a1923 | -3.27616 | -48.75452 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3a68afe-c8e8-3803-838b-1e25153d3296 | 0.09792 | -51.0387 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa9b414c-50a3-3fb8-9704-049bba1d19a4 | -2.31895 | -51.31356 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61847ad3-94a1-3a9e-8d5a-e5c33a338583 | -4.19883 | -53.499 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a96c48a-64c4-337c-9c45-2a8a9e2044f1 | -2.21184 | -50.82229 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9ef3ecd-8af3-34e8-9291-300c61226193 | -3.70572 | -47.1188 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 927635ba-a8b4-34b2-8c54-64990c92b0ec | -0.88069 | -51.72187 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec5036dc-4b79-3ae7-b0e7-17fc1a60121d | -2.56763 | -54.05513 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fda081d-eb37-39fa-a64b-f9976393415a | -2.53988 | -46.40099 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 587b7abb-b2da-31a5-a7ed-4259fcb58a09 | -3.10447 | -53.98878 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bb2ace1-a15f-33f1-9c78-296000b7372e | -3.28776 | -45.44126 | 2024-11-24 04:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04cf22b7-bb6e-3c14-826d-d3f4ce30febb | -1.8889 | -53.32497 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d90b287c-1ddc-32ef-a1b4-08b1f24ffa74 | -3.10952 | -53.17683 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f04a21e-b883-324d-94f8-943a80f817dd | -3.25783 | -53.70603 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b472a0d-f43f-3624-92b0-1a9e5ca3b880 | -3.2555 | -54.2329 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e4ff2cd-45bc-3ce3-bb81-85e22520f216 | -1.79656 | -45.71507 | 2024-11-24 04:53:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7f1d6f5e-b24e-3f8d-95e6-876658fa350a | -1.39564 | -52.56512 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e033fa2-4f81-3f73-973c-dd93a75ead56 | -1.5284 | -51.62669 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09f3fb5b-c859-3056-a466-d0c622330030 | -1.46882 | -55.18615 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f7460b8-a0c5-38fc-9cc5-bce70ea737e0 | -0.0451 | -50.82097 | 2024-11-24 04:53:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fd500cf-a665-31a7-b941-feb78f9ba45a | -2.12181 | -48.95688 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c7f5dc2-7a78-3e38-b4b8-81ba9a8f9ca7 | 0.40888 | -50.85273 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7d075c23-8946-3821-a32d-a4845be641ef | -3.73239 | -50.43714 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fca4c0a8-e754-3070-ad2d-b970ae832eb3 | -4.85414 | -50.80844 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e714bca2-2e85-35f4-8675-4ca32c9245cf | -1.72628 | -53.25977 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db58c677-6154-350d-804f-809029cb441a | -4.72446 | -45.49594 | 2024-11-24 04:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb20caec-9641-3379-a886-3edb778c610e | -2.71503 | -46.10577 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a65216b6-7262-3355-a9f7-30d0f6fa1a54 | -1.14803 | -51.69017 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6680e066-f3f6-3450-b299-0b199ff3f98b | -2.61389 | -54.25065 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd8ab487-394b-3f3b-8e37-5f052baa0274 | -3.84075 | -49.95989 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 912e2dcf-6eac-35cc-aa39-ae0f8ecd4930 | -3.2415 | -45.55184 | 2024-11-24 04:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8c2a60b-b8d4-3a61-bda4-c5e347541381 | -2.74366 | -54.07373 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa2448d0-e3a8-3da1-b9d3-802c6a4c34f1 | -2.14062 | -50.49264 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b02a1a7a-6fbe-3379-a198-83bd8441cd10 | -2.73373 | -54.11431 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5297e28-c9d7-38c5-b3b9-8cc6e39464b9 | -2.26546 | -51.24104 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d47eb52-0c3f-3eef-8259-7d934f6e84b1 | -2.99342 | -53.44172 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3244afda-47ae-3438-95f6-9ba2d1120b13 | -2.37562 | -50.38119 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09bfaf97-769e-30c8-b70e-530c05a31713 | -3.42791 | -50.00031 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e21a10c9-bbad-34e6-ae26-65237067c66a | -3.47337 | -47.68136 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cdcbedd-8941-3427-833e-5fc1efdef866 | -2.61043 | -54.25011 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4807c63f-de93-3620-9d54-6ac9f026fa9d | -2.87498 | -45.83223 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dbc76c55-74ed-35cc-8655-e6ef34bd8725 | -3.84938 | -44.04846 | 2024-11-24 04:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b2ef2af-8470-3527-97d8-9cb14b3a9d0b | -3.53082 | -52.98508 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 093cc596-734d-3482-8918-878ec5561340 | -2.29149 | -51.09627 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd358678-36b6-3f68-973a-bd3dd5a8b0c7 | -2.9971 | -51.45811 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73bc9528-0edb-37af-a13b-6dc7f6da085e | -1.4122 | -53.4775 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c53cc1d-46c2-330e-adb6-0c755e0dcea9 | -4.02796 | -49.92451 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e73cc0d-fb17-3051-ba33-b1d1d24307cf | -2.73465 | -47.54211 | 2024-11-24 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cec8e0a-9265-32b7-970d-7c32d461c157 | -6.63964 | -47.34969 | 2024-11-24 04:53:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 135d907a-cfee-3c67-a8a1-c8ec0fb4922b | -3.46938 | -50.62122 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26c1489b-0b66-3c60-a6f1-4a657e6a82d9 | -2.99948 | -52.51152 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6576e9e4-5371-3660-8058-09ddceb5bc72 | -2.80329 | -53.00338 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da32cf66-bf40-3019-8337-b25a2dca05fd | -2.55556 | -54.06482 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a923278c-1242-3ac9-8833-19553d861785 | -2.91762 | -45.3676 | 2024-11-24 04:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf736ade-76fa-35a5-8666-4a4b18a20d42 | -3.13244 | -45.37577 | 2024-11-24 04:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 813b30fa-5486-38b5-b856-850a429fa55d | -3.57322 | -51.20833 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed4e8142-cba7-3b18-9a61-39f3be15e8d9 | -3.52916 | -49.91106 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d25acc60-81aa-390c-84d0-4f704c5bc5bc | -3.25726 | -53.70964 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56d3e3d7-54c5-3e01-b4ed-2516246c8d54 | -3.08122 | -49.19698 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| effab796-a2dd-3a5f-b402-4c137a47d720 | -3.71002 | -51.79547 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff36dcf5-50e3-35af-b3ea-8814f9b3393c | -2.75364 | -48.67001 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b41ef5cc-2032-36ea-9021-231085c642ad | -2.24927 | -50.73055 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38769087-16f4-38dd-a514-5441a5bad5e0 | -1.60247 | -52.41664 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d733ffdc-415f-34c2-aef5-00dffcb59f7b | -3.7358 | -50.43766 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c541fea-f364-32db-8b6a-4634530197a9 | -4.53917 | -42.91366 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c071f5ac-725b-33d5-aeb8-dcfffb0fdba5 | -2.12193 | -50.70054 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cfa8d22-1f05-3a5c-b4c0-1bce852d3518 | -3.28749 | -53.83359 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e79c1e56-02ff-3928-a90e-728da93b2f93 | -3.03505 | -49.45081 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4a35e882-2974-3cb3-be6b-70af8407da66 | -1.18928 | -51.97118 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 351aa7a4-d5ad-3cc9-9f16-4c4b842861ca | 0.41881 | -50.8512 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cf9f605-e41f-318e-87e5-b4ebdf94cdb9 | -2.82338 | -54.1017 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dee54e66-6023-385a-be10-04e318acad62 | -2.2757 | -48.99565 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 367d517f-d56b-3a27-9846-d352706fa868 | -1.91701 | -53.34401 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27de6fa0-8caa-367e-a22a-743dbb7eeb48 | -3.70014 | -51.79046 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe2c4f0b-4f56-3887-9d86-f99e240925a3 | -4.51889 | -45.73972 | 2024-11-24 04:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72790339-be22-3169-81fa-96e498a66d35 | -3.51095 | -50.55354 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2da55f1-6c58-3e41-a2b9-6a05fc93f850 | -2.47011 | -50.38478 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13bb5352-45c5-39d0-9d08-1a6c9f2c7cab | -2.37427 | -48.6296 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 101a3e0f-7990-3a34-855a-46b252ad5966 | -3.63885 | -52.25293 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e997f16d-fadb-32d3-a946-1465010d6dfa | -2.76309 | -54.08438 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5a3a8a1-2d43-33ec-8d1e-2e3beb2cdbe6 | -1.40744 | -54.47385 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aae9854e-c3c9-306f-bf7d-fd717612732e | -3.10272 | -53.9999 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81e4de89-008d-30e3-a37c-21b18e0c71d5 | -1.1174 | -53.38713 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0d737472-8f3b-3e54-ab6a-8258fc929f7e | -2.07987 | -50.31778 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af190489-5aea-33ab-b093-07a56e5ce934 | -1.93959 | -49.52841 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28c2ca31-e7ce-32a3-9910-be748f1a2594 | -3.39515 | -50.34954 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc5fb3b3-14c3-3a4f-af28-10cdd5ccf801 | -2.68216 | -52.43013 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d869902-c656-3bff-a977-c9106b2d8237 | -2.71262 | -46.29118 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 51e769ba-181f-3a56-8d01-486c092e5688 | 0.00868 | -51.19018 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 440fe250-5afd-3ce7-bfbc-5ce902d521b8 | -3.77605 | -52.17922 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8bf3fdb-df6e-3e20-99c0-f045bd5a3056 | -1.89902 | -53.32653 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f40208c-f155-3e0a-8d93-8ca1a38655dd | -1.31102 | -51.75457 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e39c3644-5dcd-3105-b274-c4a200588bc7 | -2.1544 | -50.61827 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac2ba4b4-afd6-3981-a620-457151fb0930 | -0.01654 | -51.41863 | 2024-11-24 04:53:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd9100a4-546b-3f14-9bad-6f508464e718 | -2.73821 | -46.08805 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a8f1817-146d-31d4-8684-22aa6c534625 | -0.87796 | -52.76442 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README63.md)
