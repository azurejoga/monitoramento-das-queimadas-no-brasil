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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f6f781d-924e-3930-9074-64fba4d78829 | -11.7564 | -54.3774 | 2025-06-10 12:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7b35d5a0-74c0-3fa6-b5ea-b9c46b2ace2a | -8.7993 | -45.1044 | 2025-06-10 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b67d1d1e-3dd2-3af9-953e-adf8f1e90aa5 | -9.3972 | -48.4305 | 2025-06-10 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 7f163fc2-c92d-3eec-9902-31c629b03a8c | -10.3781 | -49.8864 | 2025-06-10 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3243ddaa-72ca-3621-a74e-2d5c588d1ec7 | -9.3972 | -48.4305 | 2025-06-10 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 21ae0cc7-72af-39e2-a5cc-c38306dff0c6 | -10.3781 | -49.8864 | 2025-06-10 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 8c7612a7-189e-3bbe-9708-4fe7c478f50f | -8.7993 | -45.1044 | 2025-06-10 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4447909c-9214-36eb-a5cc-0246812a4241 | -11.7756 | -54.3551 | 2025-06-10 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 4c646d0e-b6ce-3d68-8e6c-4d8001de5b23 | -11.7754 | -54.3756 | 2025-06-10 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 18145b7a-08c9-3422-903e-2c96678d885b | -10.8694 | -54.3151 | 2025-06-10 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 43aa7808-50c2-3edb-9626-56bef589bbdb | -9.3972 | -48.4305 | 2025-06-10 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| fd281aef-19b8-3b3e-90c9-5e2b7137c646 | -10.3781 | -49.8864 | 2025-06-10 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 74203bd4-2743-3389-8dc3-8c02398a3b89 | -11.7754 | -54.3756 | 2025-06-10 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| bcb2dc46-257d-38e7-b933-f368dfc01c4a | -8.7993 | -45.1044 | 2025-06-10 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| af7ff2fc-1e78-3473-a67d-80baaffa9618 | -10.8694 | -54.3151 | 2025-06-10 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d6b69340-a001-35fc-a26d-8b08172103bc | -11.7754 | -54.3756 | 2025-06-10 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 600bc5aa-532d-3de7-8a86-045551ee401a | -10.8694 | -54.3151 | 2025-06-10 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 133e5757-5d6f-3eed-b3c8-13499ac96402 | -10.3781 | -49.8864 | 2025-06-10 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| bd84824a-c5ed-3308-bd2f-11c0620ca90e | -9.3972 | -48.4305 | 2025-06-10 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| cb9f7d4f-d625-3a9e-9187-d91e901be686 | -8.7993 | -45.1044 | 2025-06-10 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 817e96b8-90cb-3d8d-bdda-f678d4eff179 | -11.7754 | -54.3756 | 2025-06-10 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9ca7fb8e-d7bb-3bcb-be1b-fd4ee874ec96 | -10.8694 | -54.3151 | 2025-06-10 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| f185115b-1019-372e-bd1b-5e5978115397 | -9.3972 | -48.4305 | 2025-06-10 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7763d319-e147-3d82-a7d1-af8fcac0bfcb | -8.7993 | -45.1044 | 2025-06-10 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 0c8b7e44-9364-31c6-b162-7fa8ab4e5375 | -8.7993 | -45.1044 | 2025-06-10 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 17498c57-43e7-3c76-8035-54710d5c485f | -10.8882 | -54.3135 | 2025-06-10 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 7a526e7e-68a8-306b-afa4-a49e0a5b1042 | -10.2674 | -46.9903 | 2025-06-10 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c448500f-e28a-38bf-be48-de0ca849891d | -13.7454 | -45.2388 | 2025-06-10 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| aee8c868-2147-3c09-9ea6-2765ffb75cac | -10.8694 | -54.3151 | 2025-06-10 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 64d2e49a-98ed-3ca5-8528-58484323cfa9 | -11.7754 | -54.3756 | 2025-06-10 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| db3fa294-0c5c-3a2f-9db3-c4b55ad4b9e0 | -13.072 | -49.2374 | 2025-06-10 13:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 33409ec6-7a12-3266-a2fb-61554acb811a | -11.7754 | -54.3756 | 2025-06-10 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| b42135a6-92a9-3515-a685-d0b073644fb6 | -10.8694 | -54.3151 | 2025-06-10 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.2 |
| a82091be-dee7-324f-b336-94de4870ebf7 | -13.072 | -49.2374 | 2025-06-10 14:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 4d45b6d5-0a77-3812-a7c9-5e91253db00a | -11.7754 | -54.3756 | 2025-06-10 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 4f25ba6e-f6c1-3944-b7b3-1b287d88ad47 | -10.8882 | -54.3135 | 2025-06-10 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| f9abb1c3-07ec-3676-ba45-072b909ca09a | -10.2674 | -46.9903 | 2025-06-10 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| eeda5e3e-1b35-32a3-a2fa-476750e36b83 | -6.6306 | -49.717 | 2025-06-10 14:00:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| b7668b78-6800-3221-a569-34fec7b43f03 | -8.7993 | -45.1044 | 2025-06-10 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 62431223-9b5b-3a24-9ccd-747ecfb34230 | -10.8694 | -54.3151 | 2025-06-10 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 1a53c946-34ec-3961-a550-94cc32215fb3 | -6.6306 | -49.717 | 2025-06-10 14:10:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| e58e7cba-eff1-3730-a829-80a289c4c6cb | -11.7754 | -54.3756 | 2025-06-10 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 2acb6890-41f7-3904-b2af-354b2c5f979b | -10.8694 | -54.3151 | 2025-06-10 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 0940b93a-2a66-37e5-b62a-a0a9cdb69492 | -13.072 | -49.2374 | 2025-06-10 14:10:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b56a82da-6333-3b2a-8c7b-693dfd240e9d | -10.8882 | -54.3135 | 2025-06-10 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| eff6ef2d-fc60-380f-8d9b-e07b0cc830ad | -10.8694 | -54.3151 | 2025-06-10 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 4116c082-14e5-3ede-91ef-87079df55578 | -10.8882 | -54.3135 | 2025-06-10 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 29fb9b3a-abe3-37f2-ae58-6d3e362b534a | -11.7754 | -54.3756 | 2025-06-10 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| e787161d-6c11-3a2c-9066-1b4b2abe0136 | -13.072 | -49.2374 | 2025-06-10 14:30:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5b918993-8349-3921-bb7b-2e0cb15fe271 | -11.7754 | -54.3756 | 2025-06-10 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 97a3f1b7-de07-3933-8d16-1214adcc0c3f | -10.8882 | -54.3135 | 2025-06-10 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d99db206-4a4b-39e7-851c-1efb92190847 | -10.8694 | -54.3151 | 2025-06-10 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 8581a3ff-1083-3d11-ae3e-1b1ad4814893 | -11.7754 | -54.3756 | 2025-06-10 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 10333972-02b3-3f12-802a-a01dd335fce5 | -10.8694 | -54.3151 | 2025-06-10 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 2563fdcf-434e-3edc-a061-e389db331f07 | -10.2674 | -46.9903 | 2025-06-10 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 55c96639-02d3-39e6-a8f7-84e759754e7e | -10.8882 | -54.3135 | 2025-06-10 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 5400ee36-91b5-3e6a-944b-8a1975f575ab | -10.2301 | -46.9501 | 2025-06-10 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| fe960ed3-bd32-3b3a-ae55-9fe972766b3e | -14.0328 | -55.13 | 2025-06-10 14:40:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |


