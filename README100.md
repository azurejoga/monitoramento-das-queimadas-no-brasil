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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1514e379-9c45-31d9-b8cd-0a102ba781c9 | -3.1097 | -54.2865 | 2024-10-30 06:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f7fa267c-1e58-3c5c-b48d-b93f13390b89 | -3.1098 | -54.2665 | 2024-10-30 06:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 851feb76-a609-3988-9cfc-435785e8587c | -3.1281 | -54.266 | 2024-10-30 06:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f4d974e2-6cf4-374f-8273-57f477c37286 | 3.5448 | -51.2772 | 2024-10-30 06:44:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 37d53883-9d04-366a-a290-2553acc4b3d9 | -24.0123 | -54.151 | 2024-10-30 07:07:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| 2aaece36-a4d2-3c00-97d1-1b5ecf1b652f | -19.6063 | -56.7108 | 2024-10-30 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.2 |
| ccd10fd8-7d56-389e-8466-7bdea1b63dff | -19.5862 | -56.7136 | 2024-10-30 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 0e30693e-8ebf-324b-ba15-1ed49485d69c | -24.0123 | -54.151 | 2024-10-30 07:17:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| 9be045a2-911e-3083-b5cf-f36ef9c31f9a | -19.5862 | -56.7136 | 2024-10-30 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 17e4af3f-6807-35c5-b4d1-49c23fd15171 | -19.6063 | -56.7108 | 2024-10-30 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.2 |
| e46e6ec4-a9f6-3cff-8920-855d789dcd0a | -24.0123 | -54.151 | 2024-10-30 07:27:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 99.8 |
| a770af5a-db00-3a26-9808-f05ab546e416 | -19.6063 | -56.7108 | 2024-10-30 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 2bd427ed-da12-3ced-9210-ded0c38a04b9 | -19.5862 | -56.7136 | 2024-10-30 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 25c1c5c3-3ec6-363b-a74d-18f85663d441 | -23.8183 | -51.9917 | 2024-10-30 07:37:17 | GOES-16 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 61.0 |
| 20e04a0b-9bd4-3e00-a31c-494fbdc564de | -23.8394 | -51.987 | 2024-10-30 07:37:17 | GOES-16 | FÊNIX | PARANÁ | Brasil | 4107702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.0 |
| a6f4c000-c555-3882-b59e-09155678a87f | -24.0123 | -54.151 | 2024-10-30 07:37:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 73.7 |
| 740c2d75-4806-3ada-ad5b-c53f6f1b7f90 | -19.5862 | -56.7136 | 2024-10-30 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.3 |
| e5bc81b0-eb03-3020-bcd7-076b53319173 | -19.6063 | -56.7108 | 2024-10-30 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| f12cafd4-d52a-3392-9e27-70bc07abb005 | -24.0123 | -54.151 | 2024-10-30 07:47:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 4b40d2b1-5f0f-301b-ae16-f872f7cd52b0 | -19.5862 | -56.7136 | 2024-10-30 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| b1fcd7b1-2c8a-3c1d-ba5e-9144bde78486 | -19.6063 | -56.7108 | 2024-10-30 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.4 |
| c8444218-e2d4-36a2-939f-2e6a45d70163 | -19.6063 | -56.7108 | 2024-10-30 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.7 |
| d35f7412-dcab-3f7d-a79d-5b0ea34b8770 | -19.5862 | -56.7136 | 2024-10-30 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 4fc4394d-439d-3b7b-b89e-8f1a737773b1 | -19.5862 | -56.7136 | 2024-10-30 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 1b10c9d1-9651-354a-8e68-9bd103e30405 | -19.6063 | -56.7108 | 2024-10-30 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 60a1d152-cc5b-38f7-a102-7699770eb3bf | -19.5862 | -56.7136 | 2024-10-30 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 26973f8d-30b5-312b-9b00-edd59b633cd1 | -19.6063 | -56.7108 | 2024-10-30 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 254ea6ae-bc7a-34c4-99a3-c6ea082c6b62 | -19.5862 | -56.7136 | 2024-10-30 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 2653c83f-1136-3b7d-aca6-eda4970b212f | -19.6063 | -56.7108 | 2024-10-30 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| bbe26268-e44f-3d26-b45d-5b36f87580f6 | -19.6063 | -56.7108 | 2024-10-30 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| e6776548-f3d1-359b-bc6b-88ada9819c7a | -19.5862 | -56.7136 | 2024-10-30 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 4e80c3a3-8fae-3818-9050-ca8a6c307e8a | -19.6063 | -56.7108 | 2024-10-30 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 90b7b94c-fdf3-3f34-abd7-ea10d8157009 | -19.6063 | -56.7108 | 2024-10-30 10:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.8 |
| 0a5c7cd6-a9b2-3b08-a058-936266836e4b | -19.5862 | -56.7136 | 2024-10-30 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| ddec610e-5300-3ff7-a7a6-1c8ec110ad1e | -19.6063 | -56.7108 | 2024-10-30 11:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 09200927-2682-39a2-a5d6-cb91b1e67bd2 | -19.6063 | -56.7108 | 2024-10-30 11:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| f76d0e24-8b43-3f0a-87d9-436bfeee2477 | -19.5862 | -56.7136 | 2024-10-30 11:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| 2f99bfaf-ac5d-3f22-9e58-37be5a1e90f6 | -19.5862 | -56.7136 | 2024-10-30 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 934f79d8-9a4c-3214-bfc5-09d13d976b1b | -19.6063 | -56.7108 | 2024-10-30 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 77e5a3e5-823d-3ee7-b609-46511df16197 | -19.6063 | -56.7108 | 2024-10-30 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.5 |
| af98c1cc-6448-3a86-b33b-10dcebc3cd05 | -19.5862 | -56.7136 | 2024-10-30 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.9 |
| 25cecfbb-29cb-3044-98a1-f6439608792b | -19.5862 | -56.7136 | 2024-10-30 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.0 |
| d2672a2b-3201-3105-bf1b-c6f7a7dcef28 | -19.6063 | -56.7108 | 2024-10-30 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 130.9 |
| 83851e46-4a6d-3e24-b599-4a3fdc9eb72d | -19.6264 | -56.7079 | 2024-10-30 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 3c5540fb-d538-3ca6-9ab6-15ab65ec0267 | -24.0123 | -54.151 | 2024-10-30 11:47:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 102.6 |
| 1fedaa0d-208e-33ab-a7e4-d29cd560d9cf | -19.6063 | -56.7108 | 2024-10-30 11:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 125.2 |
| 78c21f31-2e5b-3e95-a03e-ffeec619bf93 | -19.6264 | -56.7079 | 2024-10-30 11:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 5b1a98ea-7c67-3ce0-9bb5-1c770632a347 | -19.5862 | -56.7136 | 2024-10-30 11:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 145.1 |
| ab8f20e5-170c-32ab-89e1-d2e8103484dc | -24.0123 | -54.151 | 2024-10-30 11:57:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 99.0 |
| 7daa0586-2d97-370e-a188-88a92511d86d | -19.6063 | -56.7108 | 2024-10-30 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 151.0 |
| ca3c89f2-aa6b-389b-b75c-1a806585c2d7 | -19.6264 | -56.7079 | 2024-10-30 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.4 |
| f31bd80b-f2ee-3c6b-8478-2f9a05d51207 | -19.6067 | -56.6898 | 2024-10-30 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| b4e9a8e2-88bd-34b8-8cb4-112f90b93ea8 | -19.5862 | -56.7136 | 2024-10-30 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 117.6 |
| bf8f7680-e417-3485-9b73-ab382f98dacc | -24.0123 | -54.151 | 2024-10-30 12:07:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| 431ff214-5a83-375f-b164-a5c6fffded42 | 1.6934 | -55.8434 | 2024-10-30 12:14:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 521e19d4-85e2-30bf-a53b-a408e7f95c4e | 1.675 | -55.8831 | 2024-10-30 12:14:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 23565eb0-c599-3c44-a009-90ae3eb913b0 | -19.5662 | -56.7164 | 2024-10-30 12:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 0c20030a-6e64-30d2-bd0a-7374477bbda9 | -19.6067 | -56.6898 | 2024-10-30 12:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 3fae5aee-b387-34a8-b4fc-94d7db3b4119 | -19.6268 | -56.6869 | 2024-10-30 12:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 1c443660-35f3-3ffe-b152-9121cfdbf756 | -19.6264 | -56.7079 | 2024-10-30 12:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 106.8 |
| 9b8c0ca1-9a63-3866-bdf4-6d5eb69b0f30 | -19.6063 | -56.7108 | 2024-10-30 12:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 187.1 |
| 37bd59ad-316d-36eb-8775-9884e5635158 | -19.5862 | -56.7136 | 2024-10-30 12:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.1 |
| d8f84364-f718-3125-8206-14a1bc640936 | 1.675 | -55.8831 | 2024-10-30 12:24:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 88e61597-0c33-3591-9905-a914a0737e5a | 1.6934 | -55.8434 | 2024-10-30 12:24:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| eb4cd4b5-51b7-3474-8de7-4bd9d6fd78a8 | -17.745 | -57.5138 | 2024-10-30 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 5a7ac2c0-9d12-3c2f-a091-cda5ceb461b8 | -19.5264 | -56.7011 | 2024-10-30 12:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 86cdb982-27b2-3fbe-b8dd-6413271ad6e3 | -19.6268 | -56.6869 | 2024-10-30 12:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| d9761239-3a46-3b0d-8049-9960c058a413 | -19.6264 | -56.7079 | 2024-10-30 12:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 105.2 |
| 432feac5-c964-3ca7-b2e5-694835921354 | -19.6063 | -56.7108 | 2024-10-30 12:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 174.0 |
| 6ce8a01b-a340-3515-b9ed-ff3857f7c4a2 | -19.5862 | -56.7136 | 2024-10-30 12:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 175.4 |
| 250d70c4-3afe-3915-bed4-70408161758c | -19.6067 | -56.6898 | 2024-10-30 12:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 7047b56f-80f4-3fa6-9df6-1614df23f242 | -19.5866 | -56.6926 | 2024-10-30 12:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| bf7fdea0-5239-3417-9a65-e1b4d2daf521 | 1.6934 | -55.8434 | 2024-10-30 12:34:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| a5cf39ab-833b-3667-9168-a3faccd31212 | 1.7483 | -55.8428 | 2024-10-30 12:34:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| dad82ad4-228a-3a71-917c-d706e3185764 | -3.3889 | -41.6441 | 2024-10-30 12:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 132.9 |
| e79833dd-8754-3260-90e5-19d56d81ade1 | -3.4076 | -41.6432 | 2024-10-30 12:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 1bcdd6d6-5633-3cf2-8abc-f14248a2aba9 | -3.4078 | -41.6192 | 2024-10-30 12:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 137.5 |
| 4c883c2b-fadd-3bf0-a88b-1b8a2280b74f | -3.3891 | -41.6201 | 2024-10-30 12:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 117.7 |
| b1ab3418-358f-33c8-96c9-34bd152fbc34 | -17.7246 | -57.5574 | 2024-10-30 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 3d0fa7c6-3f7a-3e44-8788-527df904ece1 | -17.745 | -57.5138 | 2024-10-30 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 48ff3589-2100-332c-b038-b5c4f46d0a63 | 1.7483 | -55.8428 | 2024-10-30 12:44:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 621a1b5b-9fc8-3349-af5b-eae334a2d6f3 | -3.3891 | -41.6201 | 2024-10-30 12:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 654104a5-1f1e-3476-bd50-19a15c6e6c67 | -3.3889 | -41.6441 | 2024-10-30 12:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| fa109ee8-c6a0-3107-8664-d62b57546870 | -3.4078 | -41.6192 | 2024-10-30 12:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 127.1 |
| 7f33c6e5-5a4d-3548-a4a8-cc412b271dd9 | -3.6648 | -42.4384 | 2024-10-30 12:45:27 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 273.5 |
| b3cfee54-0d98-3981-8903-af1c30c3ad22 | -17.745 | -57.5138 | 2024-10-30 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 69cdfa97-e77a-362e-9fc2-088b4b7d4f55 | -17.7446 | -57.5344 | 2024-10-30 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 29a27dc1-1bbf-3adb-b2c3-3496dcf4daee | -17.7246 | -57.5574 | 2024-10-30 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 8049d26b-800f-3c60-8910-f799af227544 | -19.4874 | -56.6437 | 2024-10-30 12:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| e8ade241-7a25-3d7d-8b8b-0725ec6df672 | -19.4677 | -56.6256 | 2024-10-30 12:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 32fdab93-ea6e-3dab-a74d-9bbbc1548fe2 | -4.17719 | -45.93219 | 2024-10-30 12:53:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 46e0790f-b13c-33c7-8832-b4fcfbdf831d | -4.03736 | -44.72178 | 2024-10-30 12:53:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 56ca603c-95e2-3615-a4b5-7f72e773d9cb | -3.82831 | -51.69036 | 2024-10-30 12:53:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 08767e29-e2c1-3d2d-b163-e815c1f6a385 | -1.18463 | -47.13683 | 2024-10-30 12:53:00 | TERRA_M-T | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1a69033a-9097-31c2-9200-e95dd295fb9c | -3.69512 | -51.84004 | 2024-10-30 12:53:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 42945e42-3f3b-3f62-8459-1507f8279f7e | -3.46504 | -44.3839 | 2024-10-30 12:53:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 2bc7f264-805a-356d-9a9b-a8727810b703 | -3.46286 | -44.39946 | 2024-10-30 12:53:00 | TERRA_M-T | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ed35963f-747d-38f1-bae0-0e64414207a4 | -3.37016 | -44.23632 | 2024-10-30 12:53:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c67e5656-910b-31f6-9328-a82038d87a04 | -3.36797 | -44.25218 | 2024-10-30 12:53:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 589a3b18-d5d3-3451-befc-2ad499acb46e | -3.26226 | -51.013 | 2024-10-30 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |


[Clique aqui para ver as próximas entradas](README101.md)
