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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a859d264-a0b6-39f8-b360-8145766ea910 | 0.95335 | -50.75677 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cea0eedc-78a4-32ea-9c88-e140b8d4b94f | -1.17837 | -53.41569 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6635615-3c2f-38ee-acff-769e47ad37ac | -3.12476 | -53.26755 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5adef4d-4348-32ce-b418-7f4b3c8df9b7 | -4.50929 | -50.13973 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b519c089-4bc5-3edf-9b41-42f0152afbd3 | -3.46289 | -50.23152 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47f6a553-2217-3641-91bb-d3f569483606 | -2.58246 | -53.99594 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bcce821-9f97-3aca-be83-cc891be81467 | -1.14041 | -53.70147 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d6c6fa2-d1a0-3d3b-94c3-fa3f1c0ea377 | -3.11282 | -53.97796 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9b7538d-f051-34d3-8990-036cb321ece0 | -2.23496 | -53.6249 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| beb6ffdf-3859-3e82-8946-e7e6235866da | 1.87301 | -55.73821 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d12c8625-2e28-3983-ae6e-fc7ee8ce25c2 | -0.99618 | -51.71585 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf2b50d2-08b9-3ad8-a764-5cc9bafe631f | 0.06741 | -51.49361 | 2024-11-30 05:01:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b54ffb8d-4931-3b94-bcf5-d8aa22278034 | -4.30205 | -48.21187 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 464a2546-1d08-3231-858a-404aa21effc6 | -1.30737 | -51.73202 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d5ddb31-4edc-3e08-bcfe-c5e0ceba3f63 | -3.96754 | -49.91162 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b7bc7ac-0d65-3ee6-8591-81f732306058 | -2.73026 | -54.13748 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 458e8b55-6647-3554-be91-74c0282dc2ed | -3.01471 | -45.1032 | 2024-11-30 05:01:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3e4ace66-5d25-3d12-a9ac-8103c9f9cc98 | -2.65923 | -48.7911 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74c879bd-7b29-33f9-886e-80cfcd8d5767 | -4.08122 | -54.56126 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5f7ee00-9492-3680-b68d-cb93b50dd42c | -2.44847 | -53.62175 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4250915-3276-3b54-a7bc-521362ad096a | -3.4997 | -50.45741 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee508e37-fa4d-3814-84b4-8027a4faf23e | -2.38283 | -53.65911 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ddbbb6a7-4477-3277-b432-0dad66457497 | -2.47498 | -50.36424 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ffaa7ba-6ac2-31aa-8630-503b2f48ad9a | -2.40707 | -51.98869 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d4031cf-c6eb-346e-b334-4cd34e020ad4 | -2.50169 | -51.95629 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 410d70c1-fcab-3f0d-a54c-de92056c67ef | -3.25063 | -53.6468 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ac9be5f5-ef6f-36e4-af3a-656e8a01d104 | -3.93764 | -47.98076 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f23782a-d22b-303b-a37a-cb3ae673803c | -2.80763 | -53.04308 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5394e750-e0f0-3d08-bceb-2204382b745c | -1.58495 | -51.25819 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a7093ac-ee47-335c-b92f-4aefea6f4883 | -1.63376 | -52.46579 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d73b184-d89d-33db-8390-26d8b0f40124 | -0.76573 | -52.45948 | 2024-11-30 05:01:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb6e96d9-485c-328e-8727-e754bbf11bbc | -3.6954 | -51.80283 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ac13277e-826c-3fd9-aba4-6a3bf00cd65d | -3.69296 | -47.13956 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63f2e73e-6f3e-3f8d-862b-64e8eaf06d6a | -1.7125 | -52.63131 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8c46a414-b2b2-3db3-be7e-b5eae67962fe | -3.65373 | -54.17643 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d174c695-0dfd-3053-8d37-3aa7f9b5c107 | -0.24756 | -53.76184 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7b4653b-3125-312f-9c9f-144b14050f72 | -3.30432 | -50.37791 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88f1a876-52b5-310f-9e06-63b7c51edc47 | -1.5695 | -53.83569 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34f2b81b-9b9d-3b98-aba5-fe90cdf36dd8 | -3.03339 | -54.03357 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c9de29f-c8aa-3ac9-8404-8e5c2d055db3 | -2.62217 | -54.07006 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fde0f6a-fc7b-3518-b29a-266799a2ef3c | -3.46342 | -48.92637 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dac08906-9326-3a0a-a28d-2edcea27b52b | -2.96811 | -53.73815 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5617d73-7102-3dec-b5ea-a86c5b442b2e | -3.48014 | -53.81287 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04a12a06-1cf1-3056-96f5-e7409f613193 | -1.07197 | -53.20685 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 579f086e-5b27-3534-ab6b-c7faf9764dde | -2.84154 | -54.0293 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 962228b3-e52a-334f-818e-3df5f91f9e4f | -1.47179 | -52.66039 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b05d0ecb-773a-30cf-b9c5-4f4a1c6d5e50 | -3.46779 | -48.92699 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e2c38a48-7a00-3999-ba9e-e56daea6d5c2 | -3.64573 | -52.34261 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9258ddde-a0c0-35e3-a96f-509a37bd08bc | -1.13345 | -53.81104 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df89f655-cc0c-3192-9c25-b8291ac0cfd7 | -2.97411 | -53.29378 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db9d26b2-1a4e-32eb-82cb-3c8be1312b2f | -3.27646 | -45.56651 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b4792375-281b-389a-9975-e3d867e76960 | -2.98321 | -53.28023 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dc5407d-7181-3e56-8908-a294f6457e61 | -3.49125 | -54.02855 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24870067-0335-3a85-8523-c68e1f81309b | -1.06556 | -53.38043 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eba406ad-b06b-3871-9b00-337f41825faa | -3.25054 | -53.29091 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e5e08b3-6dec-3b3d-8876-d6d3e8a77b08 | -2.54488 | -52.91235 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c8e9edf-907b-3011-88fc-be2d87f303db | -2.58908 | -53.97546 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dac4a391-94ed-3b41-b257-5dd367963897 | 1.1915 | -55.95426 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 720d696a-b587-3e83-b9c3-ca3a610ac39f | -3.00119 | -53.725 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84316d57-0a96-3230-b1a2-5a98a83ddec0 | -1.17556 | -53.41163 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1aad8bb-9274-3226-950e-b649edea52ba | -2.44908 | -53.66195 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23cab6da-032b-3d1c-bb52-5ee073895312 | -3.89352 | -50.07499 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b70981a3-5367-38b1-bfd2-c4a44652950a | -1.72155 | -52.49485 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 142f11d0-ae78-37db-81b8-f73ca78d9a40 | 1.44429 | -55.87827 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1158993c-4281-3365-b51f-7fba9b62b5ef | -3.04977 | -48.96663 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fc94d636-ada5-3fb3-953d-6b9fd68cb1a1 | 1.28207 | -55.91048 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b64bd09b-bbd8-328b-93ab-0fafd1918c57 | -3.70721 | -45.6906 | 2024-11-30 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bce462cd-5247-35f0-aa89-10d9aa9fd3d0 | -3.41175 | -50.24499 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ba51823-be83-3c9e-9b32-b16abb801c68 | -1.78627 | -52.74575 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2deaea59-60c2-3cb9-b98e-201ed32bd09f | -0.2466 | -51.4444 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94e77878-966d-3388-896f-978a85293b7a | -2.69675 | -48.60299 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae8f2f44-82a8-3def-a503-deec6528c7e2 | -3.09752 | -54.03988 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1e40037-e675-3ee2-90ca-be64454301f0 | -3.21778 | -54.17364 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 783d1774-0e90-3c94-b96b-c0beb7efa492 | -1.62263 | -53.8833 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f3444fa-3f04-33d1-9d4a-3f6ee43578b0 | -0.26471 | -51.647 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3239fa30-694d-38b6-a245-876f9afa1ecf | 0.93899 | -50.7373 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e5c865dc-497c-3579-a945-46707b6cc879 | -0.99495 | -51.72383 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| daebc155-a6b5-328b-aeb7-a11db88d2496 | -3.26086 | -53.78668 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6324a5af-7f99-3869-a769-6a0d3d2fbbdd | -3.25682 | -53.6294 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 20ddf9ef-3852-32ef-96a5-a7fa9418f170 | -3.68146 | -49.57276 | 2024-11-30 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e96399b5-4f27-3f8b-a4f8-e2d569a0fc05 | -3.60568 | -49.98085 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b506a93-c81d-305b-abe4-af224e05ac0e | -2.7602 | -49.40372 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b682c291-d85e-3827-a29d-3d3201d20ce1 | -3.33662 | -53.21027 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddc4f637-4d1f-3239-99a3-e65f4c3cf692 | -3.96635 | -46.7424 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae0ed4c8-9037-38aa-a7d2-be89829c5932 | -3.17598 | -51.28559 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2542cca-fa7e-3eb3-ac40-c8bfa86a7ac6 | -3.29007 | -54.12737 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f5dc16f-e441-3aa3-904d-bacd93900335 | -1.08124 | -53.39008 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33c10790-bb3e-3935-8c29-5c0de3756e20 | 1.78809 | -50.42436 | 2024-11-30 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0f5d4a1-69fb-3f18-a433-c0fa2e56d8d8 | -3.29105 | -51.49702 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d9450a3-ddaf-34a6-9461-8225ffc12b3f | -2.61097 | -46.57544 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8411be64-42bf-31ef-ac5a-48486470c7e1 | -3.49698 | -53.81548 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cc7adfb-5241-3237-b4eb-9dfeb65617ab | -3.04809 | -54.41494 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1481b15-ebf7-3052-a8ac-5dae615c7f89 | -3.33295 | -50.05648 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4e8048e-55e9-3017-861b-14e929076a35 | -2.82324 | -55.58663 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b6e2c29-2ed8-34ba-9e2e-6ec61e8883e3 | -1.70329 | -52.64521 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ce979d4-70d2-33b5-b50e-fbaf9b41c23e | -2.95891 | -52.91728 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2575c889-581a-390b-aaf0-ca8856d844b9 | -3.7608 | -49.93799 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 27a61033-251a-3e0e-a296-ff45e1b3f756 | -3.64574 | -50.2315 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 010a714a-9140-31c5-a905-ae141b296f2d | -1.4929 | -52.32428 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 587250e3-2df4-362d-82be-1784b86708fe | -1.53423 | -51.61455 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README88.md)
