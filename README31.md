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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e42905d4-6f8a-3f39-b189-75967f6cf698 | -5.69402 | -49.88969 | 2025-10-23 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de29565b-810e-3a8b-a289-bbcefa07a1f4 | -7.27468 | -49.99345 | 2025-10-23 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6519d61-b5f2-3e01-b9cd-ccbcf3d51bbe | -5.31907 | -48.18133 | 2025-10-23 04:55:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9d70844-fdff-3eca-b6e0-269882f2f691 | -7.88763 | -43.55247 | 2025-10-23 04:55:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ca155f7-b1a0-32c3-97d7-d05daa1a3aa8 | -3.25095 | -50.13211 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 452f0ff9-4f65-336a-9d77-fac32d32c81c | -3.51707 | -52.82837 | 2025-10-23 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 231c9d53-ba1a-39bd-ac33-2fc8258b98e0 | -2.29504 | -47.99409 | 2025-10-23 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c139b7e8-54bf-3bba-85ee-b6abf0776582 | -6.32247 | -43.62794 | 2025-10-23 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45bdc90d-f3d2-383f-9a3b-607fc7b726d4 | -6.78934 | -45.44149 | 2025-10-23 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49e02163-cc05-3d2f-b712-684dc0a3e834 | -1.70807 | -55.68653 | 2025-10-23 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7740c6d-1a16-3fa7-b30d-44ca2d58d14e | -3.06144 | -52.31223 | 2025-10-23 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e42662a9-cdeb-340c-834a-c36efed65a38 | -7.07783 | -46.19386 | 2025-10-23 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb8ff113-c40d-38f4-adf8-0fb8f79907dd | -2.24934 | -51.92384 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a14717a3-c13e-3c35-94b4-20ee11408394 | -2.90584 | -48.98852 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a347264-0e8a-32a5-8bd2-c5c770904c56 | -7.62665 | -42.19828 | 2025-10-23 04:55:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a2ee673-a4a7-305b-8592-c57bcc52b40a | -2.80964 | -54.3786 | 2025-10-23 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ce123e87-9997-3e6d-8774-d179cfff499e | -3.788 | -52.42126 | 2025-10-23 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| adafade8-fa90-3307-bdd9-fc253fa82e63 | -6.59792 | -44.22023 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d74a954-11ef-3774-9ff7-cbe08a902518 | -3.13997 | -50.29394 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01c11360-d94c-3e0e-a894-fa8a9639e6df | -3.645 | -48.97557 | 2025-10-23 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8a64f1e3-9d56-3be6-9558-7747df984309 | -1.89324 | -54.07333 | 2025-10-23 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd695f4d-aad0-378c-8257-62d5ca7bfdeb | -3.31652 | -51.21517 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01bf2696-a7f2-3655-b19d-4cbd315b0405 | -2.88083 | -54.74376 | 2025-10-23 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1d8806b-6199-31b4-862a-af53bd28f45f | -5.68727 | -45.96659 | 2025-10-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b4c145e-20e3-33b8-943b-71a8cbe7f3b7 | -2.14304 | -54.44496 | 2025-10-23 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73cd378e-c19f-3d3a-b141-0419c53552d6 | -2.92561 | -48.30664 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| db3b2b75-34b9-3edd-a8c2-048cfaa9de43 | -3.02491 | -49.4786 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 063c0866-17e5-3d31-a821-d9d23688c680 | -7.07567 | -46.19909 | 2025-10-23 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c28da21a-1f69-3054-8d24-72c84d991599 | -3.65909 | -52.11879 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0db6298-6251-36a6-97d8-eb05aadfbace | -2.16105 | -51.94602 | 2025-10-23 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21d15d8a-b6b0-3f6e-b74a-cd6a71bddd6c | -3.47678 | -50.07301 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8dc81ce6-74b6-3779-bf04-d9e336f6ce08 | -1.4232 | -55.35627 | 2025-10-23 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e838cba-5691-3deb-bb01-181e6a377636 | -6.96217 | -44.01872 | 2025-10-23 04:55:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6440356-9d99-386b-a9a4-f8d13a01eff5 | -4.64005 | -49.54076 | 2025-10-23 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05b52fd0-5a7c-34ea-a714-9e0f56eb6279 | -1.5987 | -55.75898 | 2025-10-23 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a03cd78a-342f-38bc-9f56-0d5c187f02ac | -3.14181 | -50.44777 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ab9c11c-08f7-3140-8222-41b7bb55dff3 | -2.02849 | -56.88328 | 2025-10-23 04:55:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bd598d8-8d3d-3ddd-aa31-745407d9b542 | -3.39654 | -50.27579 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93692605-9cfe-3dd0-b986-9b917263c06e | -4.15109 | -40.91005 | 2025-10-23 04:55:00 | NOAA-20 | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 7b7631cb-d4c2-377c-960f-02fe616d0435 | -3.42123 | -50.36649 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aacd509e-ab37-30b8-8136-74e8e13ae5ec | -3.01629 | -49.4515 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e263b810-891d-3f1c-afa1-038eb7866ae9 | -3.73353 | -52.27214 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4c2e421-296c-3d90-83fb-911af872750f | -1.40796 | -51.63474 | 2025-10-23 04:55:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08795449-e5f3-3cc7-8c9c-81125a24b2b5 | -3.38216 | -50.27353 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40a54a43-27e9-3880-835b-b429cf077bdb | -1.92383 | -52.56857 | 2025-10-23 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b192ca25-d52e-3683-98c4-1b1a133e358a | -3.024 | -49.47555 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e3482863-648d-332e-bd63-c15e0a0e2b29 | -2.11013 | -47.10464 | 2025-10-23 04:55:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 298e63c2-9d23-3ca9-ae1b-4f7e07c8cc0f | -3.13326 | -53.0019 | 2025-10-23 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92be840f-ccdc-3fb0-80da-30f786139312 | -3.13826 | -50.44723 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ca26d22-0634-3c04-9f4d-ecdf58662bae | -6.27786 | -47.01093 | 2025-10-23 04:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88d1b58a-8288-39df-9d20-1a0baf83adcd | -3.14942 | -49.47246 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0af4a004-9f56-3ea8-85f7-62739a548ab4 | -3.01955 | -49.47949 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 52a417e9-31f6-328f-8c1c-5690605dbb93 | -2.732 | -48.29099 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 448a514c-3da9-31f1-b1de-43215004d307 | -3.14874 | -50.16462 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 282873d7-6b5f-3954-a4f6-ef34a9c70796 | -2.73547 | -48.29507 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2987f9a0-7294-322a-bab6-fca7b9d0b9c1 | -3.98909 | -47.88408 | 2025-10-23 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39132d96-4253-30ec-b311-6319becbdd4b | -2.251 | -51.91324 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cdfde7a-31ce-3757-b231-6460dac1f367 | -3.47913 | -50.08204 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18e19c03-eaab-3ed5-ad07-f12c6ae6bba1 | -3.9513 | -46.97072 | 2025-10-23 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c88506e4-649c-3352-a3f2-4a673d6499fe | -3.39495 | -51.50139 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7df174a-9eb8-3580-824a-e1c01b9dd267 | -3.02049 | -49.48252 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 12f924d3-1a77-3eb1-8e0f-98d2a46868a7 | -3.47977 | -50.07782 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 933f9bd0-22d5-3bf2-9846-efd21db797e2 | -3.22983 | -49.35002 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76acee0b-c883-3055-a7ed-fda19a918b6e | -3.01707 | -49.45446 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c44af90-3fb1-367a-ab3e-fc866514a231 | -6.32305 | -43.62379 | 2025-10-23 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0b5a25f-d993-3145-9b89-9393b7bd401b | -2.8057 | -50.27894 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7ea2701-5abb-340b-a877-47b782abbf53 | -3.01884 | -49.48397 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2a0d0aac-51b8-3a09-a774-fb7f1ebdf630 | -2.80337 | -50.27026 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a2c5521-c2fd-3402-862d-242f05e43e4a | -3.94158 | -52.13363 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc457e01-b27b-30b7-8326-7b5ee4f15d55 | -2.35154 | -51.98655 | 2025-10-23 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0626d779-12f6-32df-99a0-50ae638b3aaa | -3.02003 | -49.45206 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bffd28a1-df3d-317e-adf9-3a879d0f48b9 | -3.73692 | -51.37374 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f00e2dbe-b0c9-35cc-9d13-2d0107a2a4ae | -3.76528 | -48.92821 | 2025-10-23 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48d41f05-d8d0-31f3-b05a-1045e05ea19f | -3.32902 | -50.22478 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08d01345-d2b7-3e23-aab9-a186132f57ee | -2.72439 | -49.56588 | 2025-10-23 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a735a0d4-6d8c-3006-9494-2e48710f5c58 | -2.86051 | -50.74563 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec64d8df-7380-364c-a009-d9e308864594 | -2.69018 | -49.10956 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f7ccbdc-7d87-3490-9a7e-b9c0ca0782d0 | -6.78891 | -45.44457 | 2025-10-23 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2522273a-4fb2-32a2-9d0a-d81c5e961a03 | -6.55386 | -52.80092 | 2025-10-23 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae14d211-0b40-36db-bc3d-89217841ac8a | -2.73601 | -48.29158 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d200d808-88ed-3c5f-8336-18d8982e6634 | -5.31907 | -48.18132 | 2025-10-23 04:55:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea7c6f0d-794b-392d-87cb-c62662751821 | -1.89658 | -54.07386 | 2025-10-23 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 052e3f0a-7f90-3684-b055-c1583ffa8844 | -2.8057 | -50.27893 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e05a7c23-0eb9-3a25-9999-9296da664c77 | -6.59838 | -44.21677 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0a649613-4ab1-3964-98d8-071c0b9b85d2 | -4.15109 | -40.91004 | 2025-10-23 04:55:00 | NOAA-20 | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 3c6f2764-1711-37c7-9f92-139ac40a3b52 | -3.69592 | -49.56873 | 2025-10-23 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d02b4edb-dfdd-3fc8-aa14-197629adf463 | -6.59885 | -44.21336 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a7e0f5ef-533d-3ba6-b91a-5dbda53d24cc | -2.25548 | -51.9284 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4a842e6-9bb2-3216-a2c4-1a61ae718250 | -5.69137 | -45.97278 | 2025-10-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ee947c9c-2964-3ba1-8b1c-b5362fa289ab | -2.92508 | -48.3101 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f8f19c2-9099-3e93-85fe-b35b8cb7b63c | -2.90657 | -48.98374 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3801436-411b-3ff9-ad03-c7d7a1bcd251 | -2.87539 | -54.86476 | 2025-10-23 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05f8d27d-a03a-39f1-a207-ff2c1268f103 | -3.79927 | -48.99351 | 2025-10-23 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a5d06eb-5633-3ae6-80c0-4f334c5ec9e6 | -6.60444 | -44.21426 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86d18e35-7bb6-3185-9883-658c6ed73066 | -3.14811 | -50.16875 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 686d40e2-18d7-3423-9cae-577686f933a1 | -7.88763 | -43.55246 | 2025-10-23 04:55:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e8abc1e-c602-359e-a007-f2cdc33e248b | -3.59853 | -48.99341 | 2025-10-23 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb6be884-ee73-3abb-9e25-d5f474a79eab | -4.18641 | -46.23049 | 2025-10-23 04:55:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12d6b79b-8ff9-3aaf-9362-b3d32e911e1b | -6.32189 | -43.63208 | 2025-10-23 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0482e75-c7cf-36d7-98b2-191297f4441f | -1.79049 | -54.85017 | 2025-10-23 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README32.md)
