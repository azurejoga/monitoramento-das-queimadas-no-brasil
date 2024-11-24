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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7723a328-da7b-3d08-9c21-2c543e2e0281 | -2.3245 | -51.32149 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01b0d3cc-0276-34f8-9ad5-d1e2e432945b | -1.60583 | -52.59112 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 15efa9cd-055e-3cb1-90cb-7e4fe2521ff5 | -2.85523 | -51.27597 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1304fe39-c1b7-3d65-b498-7ce4364c16a6 | -3.25755 | -53.27175 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dce07ab3-7faa-3b36-acfc-a064a776e52c | -2.61849 | -46.19701 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2de356c-61b0-35c5-bd2e-033c301808ef | -3.82982 | -55.68851 | 2024-11-24 04:53:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 881971e4-7fee-37f7-b0ee-a5ce127af8bb | 0.41604 | -50.85515 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8731fb8d-2a24-371f-bd93-159eef53d391 | -1.2582 | -51.74646 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d717319a-08bb-38a1-819f-f4613230dcbd | -2.95647 | -51.41278 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47ffb98a-58b4-3727-9ee0-f724c5feb2d8 | -0.94261 | -51.65482 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9612c371-0d64-3db7-8efd-76d05a60c04a | -3.78253 | -51.87372 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 406f0485-048b-3559-ae41-14b576e3f9f5 | -1.53519 | -52.45591 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efce1a46-2a18-3315-9edb-cab222e74b34 | -1.04472 | -51.7409 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9db3ab8e-81eb-3375-9601-a913008afeac | -1.98959 | -53.28958 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b93083fe-9a72-39f1-a020-bd0a410642c4 | -4.63777 | -46.87304 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93a39f57-3a88-3b48-a48c-f0082fbb2517 | -3.27673 | -53.83568 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c284894-5912-36ef-8def-f33d1be1db26 | -2.70299 | -51.9936 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fca4128d-a5f7-3123-b089-b69cc65a7fba | -3.15834 | -49.90253 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f998df5-47f7-367d-b2b7-58ac32d52574 | -3.34518 | -51.20938 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b7bc513-1705-3ee6-b324-8ff52a872dfb | -3.25811 | -53.26823 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5290e260-4f2c-3f16-84df-ac9f464d0b6f | -1.57591 | -52.17221 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22bd2fd6-f3a9-3fc1-8a6c-f852b2c5fa25 | -1.8399 | -46.64583 | 2024-11-24 04:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 290248bb-0d90-35da-9128-d670ca8e1029 | 0.69418 | -51.44099 | 2024-11-24 04:53:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03165524-cad0-3872-962e-a0ee13e2ad47 | -3.53511 | -50.44169 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd371b8a-2921-3d31-9073-6fc68a4e6b53 | -2.22669 | -53.61423 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 309560c2-2150-3115-9c4e-fd1329b9a48d | -6.64019 | -47.34591 | 2024-11-24 04:53:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d4b38a4e-f83f-3221-87e7-5c31cc8b8822 | -2.58941 | -54.05085 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43f4bf69-fa52-3067-a06b-e89717e0d0df | -3.38805 | -50.73438 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| acf9a402-3a81-33a7-83c1-d7f6ecc64b3a | -1.27441 | -52.68911 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d243c98c-321d-3229-a65d-77787f4f5be7 | -3.37232 | -50.72462 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86a028ed-9faa-30c7-b2cf-9c776950d2d9 | -4.52059 | -50.57864 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00b36c3d-99e6-324b-aee7-a10bb4e32827 | -2.70167 | -46.27745 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9d26002-7425-329d-b100-c59ea037af87 | -2.26096 | -50.41911 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28cbbd07-c4b3-391c-968c-78b7d244d382 | -3.60314 | -47.5127 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c8995b71-0fe0-3154-8bc2-317523fc49a2 | -4.63358 | -46.87244 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12cb92cd-af66-3181-97c5-cc52bcb39525 | -0.85638 | -52.25042 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e42a1e6-e090-3b6d-956b-09db63348361 | -1.50409 | -51.17224 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6f5f68b-daab-328b-b517-0148d7f4c24e | -3.04935 | -53.42834 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 337c0a9b-176f-393c-b05e-491be37a8af5 | -3.04269 | -49.44794 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 635e2167-832a-3366-9251-0e7b35ccac5c | -3.03565 | -49.44688 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7750713f-7c1a-35a2-b706-42cd48fc94ec | -3.12136 | -51.29247 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73160364-780d-3e75-b769-f6a9aade970a | -3.5741 | -53.31793 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea32e65e-ba2d-3ba5-8150-d9f8f012dbc0 | -2.09523 | -50.49663 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed542ef1-d16f-376c-84f4-6bafac5c4a20 | -3.48525 | -49.91985 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29d82339-0d00-35c5-8fa9-24d0d5d2c7fd | -1.19239 | -51.7742 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad45b649-a1ee-3eae-bee5-01add73cb918 | -3.66036 | -49.94962 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab54e275-21dc-356d-bc2e-17ed81bfae27 | -3.19137 | -54.33075 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efe87475-af6d-310b-8dbe-54f10ef6541d | -2.19981 | -50.67966 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e88f42fc-faff-39c9-9278-f5f34511fae8 | -4.5296 | -46.4308 | 2024-11-24 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5c8ae87-f991-3d03-bdce-93c2325a63c7 | -3.68334 | -47.12996 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc84a4d7-6caf-36bc-bbcb-d17beba4bbcb | -1.11997 | -53.7073 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f584b54e-ff60-394f-a45b-a2208e8f79af | -2.2943 | -50.68317 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ef2595e-26e0-3962-9f6c-1644bc711e7d | -1.42654 | -46.062 | 2024-11-24 04:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7373e6ac-a67a-3b37-bf6e-02ee067f8474 | -0.91603 | -51.73847 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30c543fb-7176-36fa-a385-a15ca82af3d3 | -2.80729 | -54.02639 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3daf420f-9d99-3bdf-93b7-3b1aee716cac | -2.62505 | -53.97966 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed35943d-4c04-3f26-9918-594ac8692f6c | -1.06016 | -51.7503 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a112373e-f926-300d-be65-7cfc92e9d381 | -1.61151 | -46.88155 | 2024-11-24 04:53:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cc257af6-618a-38f7-8645-ad29dae82324 | -2.71995 | -48.88763 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0663fb6f-4e2d-3450-9eac-175efec5e755 | -0.21189 | -51.77887 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8472028-2e71-3286-8a9c-b58cf2f54399 | -1.90718 | -48.67461 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da6090a8-f2ec-3dcc-b5eb-beed060fc1aa | -3.91287 | -50.5879 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 384a002b-be9a-3be6-b262-42b2bfe41804 | -1.25273 | -51.6298 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ba75a9f-3596-345a-900b-bafa829e42ad | -1.07034 | -53.64282 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14558931-3c9b-35ce-88dc-de857e4a3fda | -1.8967 | -53.01297 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b75c3a78-1baa-3a29-8b36-191d7f33f060 | -1.24499 | -51.74443 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e6e5a026-c372-3ef6-bdac-a948cf8dfafc | -3.52226 | -53.81395 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 30a2a4ce-a7ea-3904-9e36-e967c4a7ba32 | -2.40038 | -46.99178 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37af4359-bb91-3bc0-ab35-8b0aabca4f4d | -2.24966 | -53.46954 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16cb90a7-8253-31fb-8c24-e880368f253e | -2.21144 | -53.7541 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f80dbefd-bbf5-3045-aac5-c3ab46d18397 | -1.42429 | -53.3786 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 279f011a-fbe9-35be-adfb-90114219d7db | -3.30413 | -50.02838 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 833fdaa7-bb50-3677-a191-d8443507ae45 | -3.84016 | -49.96373 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c544d7e-a357-3a1c-97c3-12f05c2ea84d | -3.05721 | -53.22649 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff582d7c-1467-3a00-bed9-a130f3e52b94 | -1.43211 | -53.41714 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5d8dc99-818a-3697-8b0e-df9f9d31eb4a | -3.47915 | -50.43743 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c46a373d-40a3-3b9a-a938-a4b6faa85e10 | -0.57806 | -51.72435 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75649c57-7962-3166-bda8-4b8af2d0f024 | -3.81488 | -51.99511 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 60dac8ac-ab4a-3f01-b5ed-2efdb09dd850 | -1.45472 | -53.40583 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2515d121-6ef0-3a8f-804e-6197b5935f2a | -2.87367 | -45.83446 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 61404d55-91cd-344a-be82-54813fb5645f | -3.25552 | -52.85294 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbedb1f9-d9ce-366c-8695-20e3beaba5d6 | -3.0069 | -51.54811 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 414ce127-5bd5-3162-b1b1-473694288a9c | -2.53694 | -47.36652 | 2024-11-24 04:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6ce799b-c065-3a5c-a7a4-a13bf6f471c3 | -3.50768 | -53.79667 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40ec9dfa-b916-304f-a18e-2da5d8cb322f | -0.57423 | -51.72726 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d00bfa3-45be-3ad8-b9f8-4ced7b34f851 | -2.74932 | -49.11643 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a8e454ca-faf9-374f-81ce-1fd117974416 | -2.85828 | -53.9702 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05e11542-b153-378e-8fb9-67a74e998a0e | -2.7723 | -54.07051 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c05de87a-ce25-3ae4-9e3e-4719b3532ff5 | -3.01167 | -51.38584 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cc3fd97-7001-37fd-9145-eab99db824fb | -0.81916 | -51.48783 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae8a9211-f1e4-34c0-9e04-cd9906e1676e | -2.58539 | -54.05408 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84dfc5c2-088f-3794-85e3-04d7d40cd3ca | -0.95796 | -51.64314 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0a1a47b-9359-3fda-8c2a-21aa4500e61a | -4.11349 | -49.50392 | 2024-11-24 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3b5de4c4-53a7-3909-b15d-220335504c40 | -4.85075 | -50.80791 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a769a8a1-7c13-30eb-82b2-552aa37c4295 | -1.45415 | -48.20551 | 2024-11-24 04:53:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2cd7e98-d8f5-386e-90ca-9c5b980d9633 | -4.24186 | -48.63155 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 92ae65a1-9a5f-39c9-900a-692787f93ee7 | -3.67126 | -51.73655 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| babd1cb4-c651-341d-b304-539e29b5f889 | -3.22235 | -53.93171 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49629d98-90f0-37ff-93af-95696a7df9f8 | -3.07874 | -49.21313 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7110f651-b6f5-351f-b656-0a734821fa5a | -1.199 | -51.77522 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README59.md)
