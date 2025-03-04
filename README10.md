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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d47a166-43f5-31ee-80b5-f9beaea40783 | -14.0285 | -45.6072 | 2025-03-04 13:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 658496b8-355a-3442-a466-34826caf0c24 | -14.0085 | -45.6338 | 2025-03-04 13:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 317.4 |
| 70705ecc-6376-3b87-bcdf-7f617a81679b | -14.009 | -45.6106 | 2025-03-04 13:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 227.1 |
| 758cfb2d-e32b-3c0b-bda9-f39de214cdf3 | -14.0285 | -45.6072 | 2025-03-04 13:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 752459f3-28c6-36cf-b15f-0d4065e7adf5 | -14.0085 | -45.6338 | 2025-03-04 13:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 384.1 |
| fc4383e4-ae91-31d5-8e8a-b5d8602b1e79 | -8.8607 | -44.7541 | 2025-03-04 13:20:00 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| fa89426d-25f7-360f-b701-143e7a0e609e | -14.0081 | -45.6569 | 2025-03-04 13:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| a498d5c9-8f7a-3ba7-b82a-ffa5a6ec69b1 | -14.0285 | -45.6072 | 2025-03-04 13:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 17692111-6001-3335-a0c4-7b5a2e670db3 | -14.009 | -45.6106 | 2025-03-04 13:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 3b3bea7a-ec4b-323d-8676-c79a6592cc24 | -14.0085 | -45.6338 | 2025-03-04 13:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 375.8 |
| 454c4130-be44-3eef-b6f8-468520f1076f | -14.0275 | -45.6536 | 2025-03-04 13:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| ad47c066-f017-35b0-925e-17ab7d77d911 | -14.0085 | -45.6338 | 2025-03-04 13:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 420.8 |
| bb6120cb-32c8-3381-878d-3cf5ec78b62b | -14.0285 | -45.6072 | 2025-03-04 13:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| cd288db5-4a2b-3f39-9131-dfbfd87d5022 | -14.0081 | -45.6569 | 2025-03-04 13:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| d004e387-a627-3ba8-8b67-6163df7ba68f | -14.009 | -45.6106 | 2025-03-04 13:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 217.1 |
| b1502b6b-111c-3997-870c-1853d3f36750 | -14.0275 | -45.6536 | 2025-03-04 13:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 78c30f75-7f0a-31e5-bb51-ced6ee58ac53 | -14.0285 | -45.6072 | 2025-03-04 13:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| a998ac05-d3a2-32ca-9fb9-4bae8583cf47 | -14.0081 | -45.6569 | 2025-03-04 13:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 3ed650af-fb48-352c-9287-21c92913fcb6 | -14.0275 | -45.6536 | 2025-03-04 13:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 271d708d-b4a6-37fe-8a4f-570ce817004f | -14.009 | -45.6106 | 2025-03-04 13:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 308fc4cc-8da8-3ae1-9f4d-535f8ac45eaa | -14.0081 | -45.6569 | 2025-03-04 13:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 69186760-3ffc-3d4e-a43c-032517bc685e | -14.0275 | -45.6536 | 2025-03-04 13:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| be43f8cb-be76-35c2-af1a-1a8805451b1e | -14.0285 | -45.6072 | 2025-03-04 13:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 29838a43-7fd6-364b-8fd9-f2bb27f479f9 | -14.009 | -45.6106 | 2025-03-04 13:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 187.0 |
| ec20fb9a-b09e-3729-9c87-7ca0f56762c6 | -14.0285 | -45.6072 | 2025-03-04 14:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 4c788e68-4e46-3872-8a70-8bad81332aa6 | -14.0275 | -45.6536 | 2025-03-04 14:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 5f1791d4-eccd-3d98-bd5d-cffb0f5a74ca | -14.009 | -45.6106 | 2025-03-04 14:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 067b93f9-dfc8-39ce-bce5-ca9272d12056 | -14.009 | -45.6106 | 2025-03-04 14:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 1b016517-e158-3fe1-95b1-98f21e093fb3 | -14.0275 | -45.6536 | 2025-03-04 14:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 41d9583c-c3c1-3d9f-a5b0-9329fe6dccd8 | -14.0285 | -45.6072 | 2025-03-04 14:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 9a36f6a6-c808-346a-8418-50ca3901019a | -14.0081 | -45.6569 | 2025-03-04 14:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| e321cbfc-9f4f-3f26-a0fd-45d9fa6c80d6 | -14.009 | -45.6106 | 2025-03-04 14:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 2e23498f-4e90-3f9f-8788-dc5bb9aa38e0 | -14.0275 | -45.6536 | 2025-03-04 14:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 061d9b49-6048-3ab1-ab42-bb87ee29b7ee | -14.0285 | -45.6072 | 2025-03-04 14:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 66c85d54-25fd-35d5-adcf-b0f5f839056a | -14.0081 | -45.6569 | 2025-03-04 14:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| a2e618c4-d37d-35de-8797-52909f0c4f91 | -14.0285 | -45.6072 | 2025-03-04 14:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| f578e347-69ef-32d7-ad7d-0b8ba459a06d | -14.009 | -45.6106 | 2025-03-04 14:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 4288d077-a8a7-316e-9533-97b99dbd204c | -14.0275 | -45.6536 | 2025-03-04 14:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 9ce552dd-7859-3aa4-972a-49c0fbe7bd0f | -13.9896 | -45.6139 | 2025-03-04 14:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |


