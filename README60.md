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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 822b73ee-b100-3334-9312-92e5b70b59c0 | -3.25907 | -50.1414 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d9e423b-e3e3-37d9-a68a-1b78b3649bcf | -3.25655 | -50.1366 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19eef708-3421-384e-8e97-4e7b2386049b | -3.25623 | -50.10862 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43a35d67-7e3c-364d-8bff-1f25a5fab9fc | -3.25563 | -50.14208 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4844fb9-2c20-3608-8d78-d3369b6ee5b6 | -3.25451 | -50.10706 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebf7ddb9-9bdb-30de-9003-86538183dc26 | -3.25416 | -50.14059 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3c61eb2-8d0a-339c-8f3c-c9c7319185e9 | -3.25364 | -50.11248 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0491bcc-66a6-32bb-b519-e6c193e0f562 | -3.25132 | -50.10786 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0fc2834e-1299-333b-b8ac-55411229723f | -3.25068 | -49.40382 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d8e4b022-2aa8-38d1-9760-c873f8d3fbd7 | -3.24989 | -49.40873 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6cc7271d-c838-3336-914b-a4918e1ad21f | -3.2477 | -49.40485 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 34f5a7f9-cc61-3c45-ab73-65bb8e612346 | -3.24687 | -49.40973 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1e3c1c1b-1f34-3905-8266-34efc22041d9 | -3.24602 | -49.40302 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f3e09626-3853-3b73-b89d-99f7cb1a20dd | -3.24523 | -49.40793 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e682b18f-6974-3392-8341-c20dc979b98e | -3.24444 | -49.41282 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c691b7cb-0514-3370-aec7-764bb53f0887 | -3.23372 | -50.83649 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b96ec425-ed04-3fe7-bcc7-d5f34ac75ac8 | -3.23043 | -50.83138 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 68d17002-494c-3566-acb9-f90fa6eea9aa | -3.22991 | -50.8344 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8bd2a010-f44c-318d-b1d9-c99b72c1a0fc | -3.2294 | -50.83741 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3517830-f031-36e9-ae72-391840e76aa0 | -3.22908 | -50.83252 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b1ec71a-7fb2-3187-bd3e-0beb72cd8b80 | -3.22858 | -50.83555 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53700dcc-6cdd-3c1e-bc89-4ed531a78524 | -3.15255 | -51.30215 | 2024-10-05 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3f08246-15a4-3a62-88a5-659c0df2e964 | -3.15202 | -51.30539 | 2024-10-05 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5886fee9-5e96-3c25-b1da-855661558b8a | -3.15013 | -50.21951 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d477d36d-a129-3de3-901c-037aa7db83f0 | -3.14987 | -51.30289 | 2024-10-05 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80d013d6-d999-3dd7-9354-1e9ce2cc1283 | -3.14932 | -51.30614 | 2024-10-05 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84e1e956-b0e5-3866-87a3-25f4e16cddd2 | -3.14921 | -50.22503 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f4133ad9-2b9d-3617-ada5-c2c613a75b44 | -3.14518 | -50.21872 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 187f7cbb-a8ce-3b29-af93-889061e5a933 | -3.14426 | -50.22422 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d9efa6f0-84b5-3d90-9f80-04b134ddc6a2 | -3.14024 | -50.21793 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88b0d90c-40fd-3bfe-b3f5-3159437ba7a9 | -3.13931 | -50.22343 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f2ad300a-29f3-31b5-a535-4eb409b5a6b8 | -3.13893 | -50.2228 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e259445-92dc-3089-9b4a-e21e9c3b561e | -3.11939 | -48.62551 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e5c3c2d-6ee0-3491-9871-7ce829d30cc0 | -3.11233 | -50.47632 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b09f5bc-0064-37ea-bd43-762578313c03 | -3.10779 | -50.47254 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d8946e-19f9-36fd-b6ac-53868941ec73 | -3.05844 | -46.50753 | 2024-10-05 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6116377b-d452-3e92-8140-09582a5f7101 | -2.96057 | -49.3625 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09b96556-21df-3142-b58a-c684f4140020 | -2.95749 | -47.99914 | 2024-10-05 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c61d23eb-1775-31bf-a4e2-5b00afeaa293 | -2.95039 | -52.78057 | 2024-10-05 04:12:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b13d101-07cd-3cc9-8bc9-0d0f2f2e4c7e | -2.94971 | -52.78457 | 2024-10-05 04:12:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bbaf71e-0971-3952-a9ea-158520835fa8 | -2.94903 | -52.78864 | 2024-10-05 04:12:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4533bf7f-ebed-3f5b-885f-558870747480 | -2.94594 | -52.91526 | 2024-10-05 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb04299f-0bb3-3454-981d-d5962355a59b | -2.93999 | -52.91433 | 2024-10-05 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fdd0e92-4222-3aea-87dc-2df48607ae90 | -2.90902 | -48.91064 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e845d9a-3f80-3b9d-bfb3-0322a18c70c9 | -2.90826 | -48.91519 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5f7f57f-67e0-3ff0-ad36-92e64899eb0a | -2.90812 | -48.91325 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f32a4112-59fe-342a-a2af-cec13165c00d | -2.90372 | -48.91447 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3de13168-d397-36ac-b670-775f1db8d914 | -2.90358 | -48.91253 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 53172f01-e6b2-3ed0-a455-94ba7bd0e0ca | -2.90052 | -50.71064 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4c90e145-5d66-3c1f-b853-924215f4ad01 | -2.90002 | -50.71367 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| feffc82f-f508-37e0-8fca-99d557126e82 | -2.89953 | -50.71669 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5a28134-7917-3419-933b-7295026f157f | -2.89904 | -50.71971 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70e981df-5f84-3b41-a25e-61701150a31d | -2.89589 | -50.70673 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2b22ff24-6078-3ec9-83e6-5a63411cb6e1 | -2.89539 | -50.70975 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6413257b-c04e-370b-9540-db20086aef96 | -2.89489 | -50.7128 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a63b4f4c-8e52-3fb3-97a6-d9d10a24a3b5 | -2.8944 | -50.71584 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0416f79a-a2e1-3424-abaa-83b0c7695ccb | -2.8939 | -50.71888 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ebea39b-e06f-363e-af84-f4188a352ca1 | -2.89076 | -50.70588 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7cd15ad-eb79-37dc-8584-ff08aca1cb81 | -2.89026 | -50.70891 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acf25d5b-1f88-3817-a03e-5b4b04d55042 | -2.88976 | -50.71193 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afc4e81b-5aa4-394f-80e2-8556724821f5 | -2.88926 | -50.71497 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eeac3be7-d831-350a-9801-2db80b62ddbe | -2.88513 | -50.70805 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 925936b8-ec9a-3ddd-a769-71486397869b | -2.88463 | -50.71106 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31e3f734-4753-335c-90f5-ea9d3d648d4b | -2.8809 | -48.90876 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 085ef6a4-6ef0-3db2-9191-b3d43f6e43a1 | -2.87637 | -48.90804 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cd627bc-13eb-37a7-a497-0c57adb194c8 | -2.80156 | -50.31532 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 058383d6-fa53-32a8-a035-d2414afb4bcb | -2.80132 | -50.31861 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e5999ea-36af-3f17-ab29-f7817881fb28 | -2.8007 | -49.58716 | 2024-10-05 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fc2d6ba-b040-3ec1-85b5-8a4c1732eec7 | -2.80059 | -50.3211 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ccabf5ef-4254-355d-ba53-8650266252ff | -2.80038 | -49.58838 | 2024-10-05 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ab04644-2e2e-3267-8a16-740d60081684 | -2.80002 | -49.61976 | 2024-10-05 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1c4e3a7-a41a-37cf-b11a-44d4538615be | -2.79655 | -50.3145 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 748d2081-430d-3e52-b370-e8e5d6718685 | -2.79631 | -50.31776 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b2d53015-2a26-302e-ab55-2d98448a8c16 | -2.79594 | -49.58634 | 2024-10-05 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbf87c01-fc19-3547-88fe-682819bd182c | -2.79562 | -49.58756 | 2024-10-05 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02a3c8a3-e2db-3ddc-b56b-a158b7cd3142 | -2.79525 | -49.61899 | 2024-10-05 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c81c270f-f511-361e-8129-7a4712a52f51 | -2.78064 | -48.71874 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6298cb7-f592-3a0c-8c4e-fa69589a41d4 | -2.77992 | -48.72318 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a1abe23-007e-3f11-9e1d-b7a831d19534 | -2.77984 | -48.58343 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32ba6d20-5359-38b0-84f9-efb0cd96c649 | -2.77539 | -48.58271 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ebc4164-4dac-3f70-8a53-0ac662a2c2f4 | -2.76888 | -45.95095 | 2024-10-05 04:12:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e27dccaf-167a-3ef5-9db5-d89130d9b01e | -2.74533 | -46.78845 | 2024-10-05 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1462849-7b11-3592-9904-32727d26dc98 | -2.74058 | -46.79278 | 2024-10-05 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1593e98-e9e0-3536-b026-6df8a2a14e05 | -2.73315 | -48.89598 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33a25bfa-25e6-3827-b191-2188206f2783 | -2.7324 | -48.90058 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f291b36b-49ce-31e8-bb8a-1bcf7b05e902 | -2.72021 | -48.83334 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02cab59a-b075-31f1-acf2-6030f1c2bbaa | -2.71946 | -48.83784 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6b88d11a-e848-3f0b-8428-c19f848f14b8 | -2.6476 | -49.10951 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2d541ab-6481-3490-8eff-700f5ee10190 | -2.64299 | -49.10873 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 546fd4d5-d813-3743-94c5-84420e833b78 | -2.62523 | -46.91174 | 2024-10-05 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dea203e-1f9e-313f-8cc6-96859ef23654 | -2.62125 | -46.91109 | 2024-10-05 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64f7b0e6-4445-3159-8a38-ce5705637e53 | -2.61087 | -45.3364 | 2024-10-05 04:12:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33e3017e-1588-3c58-8175-7ad98731db26 | -2.60834 | -54.21253 | 2024-10-05 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a4db2e4-ee8b-378d-9f38-92be65661a10 | -2.60192 | -54.21119 | 2024-10-05 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 429b597c-486b-3282-b8a4-f733bed8ef89 | -2.5579 | -47.30139 | 2024-10-05 04:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3ff0d0a-a99c-3a6e-8181-312d321a797b | -2.54531 | -44.08688 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa56b9a0-0c8d-3943-9f29-4c9f65e105ee | -2.44071 | -48.68288 | 2024-10-05 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83a19b63-d015-36e5-afb0-577cbd8b2a14 | -2.36238 | -46.12859 | 2024-10-05 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2d03900-addf-3c59-a365-d0cd6133f3f1 | -2.31598 | -53.8595 | 2024-10-05 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 877f9025-4a27-3aa9-9bc4-c790181b2bd2 | -2.21225 | -46.87016 | 2024-10-05 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README61.md)
