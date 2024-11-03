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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e585140-8971-3a14-b449-b7285dada58e | -2.95692 | -48.6372 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c72742c0-ba0e-37af-8d6b-9b67d036f853 | -2.95465 | -48.62947 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42afd144-baa6-3f80-9a15-88e4fdbbbb20 | -2.95354 | -48.63668 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f628cade-93c4-3b7a-8224-79ec5de436d1 | -2.92787 | -48.75822 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac473d45-8369-31bf-992d-8647ecf7362d | -2.92587 | -48.61391 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0ad92741-30d8-374d-abfe-fe7e93477bc8 | -2.92304 | -48.60978 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0d536cf4-548b-36dc-9851-1ab578f48172 | -2.92248 | -48.6134 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bf5872fc-fcea-3ebb-9ac8-92fb57454699 | -2.92102 | -48.95814 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dd972bc-c888-3f05-8e53-ca42c2058414 | -2.92021 | -48.60563 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a5e1431-5178-33ff-ae3d-d415a9f62059 | -2.91965 | -48.60926 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5bf3995-3305-39dd-95fa-17d3147a711f | -2.91738 | -48.60149 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 795d53f2-b09f-373b-b979-c3dc31b982fe | -2.91682 | -48.60511 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80301a0c-4026-3f9c-b97c-e40967c3ba3f | -2.91399 | -48.60097 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 616a9bac-fc67-3df3-be72-99393f908610 | -2.91328 | -48.76332 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7624106b-18c0-30db-a130-fac614ec3ecd | -2.91239 | -48.63405 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bae3c39c-aa0f-329a-8ade-6c927f5efc28 | -2.91061 | -48.60045 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef2c0239-90f3-39ec-890b-863e6429a8ec | -2.90956 | -48.62992 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab85c4af-3cae-3511-a586-0f565c6b90b3 | -2.90728 | -48.62218 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e85a10cf-1344-3128-b561-d009f89babce | -2.90722 | -48.59993 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 787e9142-8fa7-3f07-839a-5ff9f8c6f86b | -2.90673 | -48.62578 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8c58c6e-6917-38b5-a6f6-9f1b354a4c45 | -2.90501 | -48.61443 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fb99860-d54e-3ecd-92db-b8619823557f | -2.90445 | -48.61805 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7f7e75c-60de-3f3c-ac9c-615f0b9e648f | -2.9039 | -48.62167 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce196599-b514-3f1f-a6f2-0336a02500c1 | -2.90383 | -48.59941 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23d44e04-6795-36d7-8ce2-b2afa3fd9266 | -2.90311 | -48.73971 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61a690b0-e9fd-3bee-9af7-639dd1c7c5a8 | -2.90256 | -48.74331 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 490033a9-c590-3cf0-b441-952c361aaa6a | -2.90252 | -48.59951 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d93026a-9080-3289-95be-31b1f539dde3 | -2.90201 | -48.74689 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c5c2f64-2c4b-3259-9147-b21c61f8dcaa | -2.90195 | -48.60313 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b3c8ac6-f084-33bb-b90a-0be0b23b0db8 | -2.90145 | -48.75048 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ea4a2cb-009e-3fd8-9ae1-951348ac3168 | -2.89974 | -48.7392 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f72e475-592c-3026-b7bd-bd0ef4b28e04 | -2.89919 | -48.74279 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0ccb66b-78e6-3798-9527-62662bd4c4cf | -2.89863 | -48.74638 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d55e2f0d-952f-3bf3-861a-3c9094689df7 | -2.89857 | -48.60261 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 900acd7e-487a-3ada-bf4b-9ee778995704 | -2.89801 | -48.60623 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 679f882d-d789-3deb-a1c0-58c62ca486e6 | -2.88695 | -48.77761 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a725b5c-393e-3bc0-b534-51f609bb2171 | -2.8811 | -48.62582 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ef0900e-58ba-3fe5-9b21-f2f825e8d3af | -2.24741 | -48.82576 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d432a59-9087-32b1-a3e8-e3ce108bed1f | -2.24351 | -48.82879 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 314a32be-7c5b-34c5-9037-d22309c2ad1f | -2.8434 | -48.66813 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7b65ebb-e964-3c9b-948e-b0867465e1fe | -2.84002 | -48.66761 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4628a591-a9c2-36fd-8906-f3cac37087b0 | -2.83664 | -48.6671 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bab6732-b6cb-3334-8192-7dcc218de43f | -2.81952 | -48.5533 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 778d0e04-58a7-3a8e-9130-d421bebf4c1c | -2.8068 | -48.65882 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ce199e4-d412-3463-8ed2-a627ad89563c | -2.80398 | -48.65469 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3bcc29d-d062-3d79-b46d-c28d52032d56 | -2.80342 | -48.65831 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4cdba9b2-f0bc-3f78-97e5-5312e177f647 | -2.80115 | -48.65057 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d6f96c5-4fb7-348f-b087-e2e93b6ba45a | -2.78369 | -48.57437 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0f6fd93-1e06-3a9f-9b90-4e53c25a33bc | -2.77692 | -48.57333 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef1323b8-3bc1-3697-93b7-beb3530732c8 | -2.71164 | -48.63732 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b0c1298-23a5-3961-b805-48fb139503fe | -2.71053 | -48.64454 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97d855d6-98a7-38e5-b866-27277ebe2cb2 | -2.70771 | -48.64041 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 644e4353-06c4-315e-ad70-1237fee80e79 | -2.70715 | -48.64401 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89f3862a-af0f-3fcb-ab38-792edca3e54d | -2.7066 | -48.64762 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e594e53e-ac1a-3718-aee4-216175fc31d4 | -2.70378 | -48.64349 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73ac99d2-45e2-33b0-b8e0-b583a83a4a8c | -2.70322 | -48.6471 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46f1de19-90f2-36a6-95f9-c48712e79145 | -2.70267 | -48.6507 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 058cdf31-9e8c-3219-aece-b140b041d46f | -2.67749 | -48.64657 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 096454de-e2da-37ef-836e-364f8cb694f0 | -2.67468 | -48.64245 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fc50fe5-e1e4-30d2-82fd-e86b72e03f56 | -2.67412 | -48.64605 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 399f0268-15c8-323a-ba9e-c86927c419eb | -2.67355 | -48.64964 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ece7cb77-6e1a-3fe1-8175-2e5837552b7a | -2.6713 | -48.64193 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33336533-029b-37dd-96c4-97b92391e723 | -2.67018 | -48.64913 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab029606-2b44-3982-962a-47f37599999a | -2.66962 | -48.65273 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dd8816c-5744-36d7-8e2c-8eb11c78c3dd | -2.66847 | -48.57127 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94f0f0db-29a7-342c-917d-af1c559a669f | -2.6668 | -48.64861 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0fbd670-1f4f-3cde-8dd9-451b51f2a059 | -2.66508 | -48.57076 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 937b28e4-3dca-30d4-bdea-ebc071ba3723 | -2.66455 | -48.6409 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db31b6cc-90d5-3a61-aafb-eca0795af426 | -2.6617 | -48.57026 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96ba74ca-7cdb-3ce6-9c4d-bfdcdcd9a293 | -2.65095 | -48.52778 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8361ec4f-1fa4-3815-acf1-b7b2876fc892 | -2.64761 | -48.5718 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e2e8edcb-2cc6-3d13-868b-aa05dc5ca86c | -2.64705 | -48.57542 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cd306b29-60e1-363e-a3dc-7af09f9499bc | -2.64701 | -48.53088 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d619676c-dbbd-3c7e-a30b-6c4d3c56fea5 | -2.64649 | -48.57903 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 364e7ec3-45b9-3618-9143-5a20c401f372 | -2.64593 | -48.58263 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5790d104-a0cd-31f9-a974-0fd082b1e0c0 | -2.64591 | -48.56041 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef30cd21-0a45-3312-8c22-be9d38222216 | -2.64535 | -48.56403 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9bee4c4-0267-35b9-b316-bbf23f4165f3 | -2.64478 | -48.56766 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5d966547-df61-3e8b-864a-6a2d62de01d0 | -2.64422 | -48.57128 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0cdb2474-af8c-35c0-8060-1b7a1cbc040f | -2.64366 | -48.5749 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3d45530a-1117-3d9f-8a7b-8b5bc5e103c4 | -2.6431 | -48.57852 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ac0f31c-83c8-3a69-a65b-ae93c529af00 | -2.64255 | -48.58212 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 284a5600-d621-3f6b-b060-975b6894fa5e | -2.64196 | -48.56351 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bcc488b-f36c-3828-9f90-88f32684efdc | -2.6414 | -48.56714 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 907f76b0-986c-394c-85fa-86b9d4413f2a | -2.64084 | -48.57077 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2895fc6b-d22f-33ea-ba53-ff9fbe214b7e | -2.64028 | -48.57438 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ada064b4-0a0f-39ad-9e68-2373c755516a | -2.63972 | -48.578 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 52a784ee-2a47-3582-afee-5386912c1d00 | -2.63917 | -48.5816 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3880b68b-205b-3fb7-9e24-cb6bb8567bf2 | -2.63858 | -48.563 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| adafeef0-8c3c-364b-8634-ecb83bdb9ba1 | -2.63802 | -48.56663 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff478ac3-aa56-3f42-b746-58500babd6bd | -2.6369 | -48.57386 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 13f33237-6a5c-3427-9bc4-835d22dfd563 | -2.63634 | -48.57748 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4b9004bf-56d2-3f5e-acf0-bf11b8f84432 | -2.62951 | -48.53194 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ddabfaa-7a61-32eb-a32c-7b472c4a42c1 | -2.77608 | -48.72409 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecc6f19c-78a7-34ab-8aaa-981ffba26264 | -2.77527 | -48.71709 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97dc1bc5-79e6-3484-8374-03b125fc187f | -2.77415 | -48.72426 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17048299-a346-379f-b9c8-cc9ce3100ad8 | -2.76909 | -48.71246 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1d4f452-6a71-30ef-8246-4cbb4e12cf18 | -2.73993 | -48.74471 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e0eccfa-7c72-325f-85be-cb4c617f7caa | -2.73937 | -48.74829 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d7ee552-1b34-3460-adc4-58cafd23ddcf | -2.73881 | -48.75186 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README39.md)
