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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c491070d-16c7-3020-8089-7a3d2385c0f6 | -4.09813 | -48.26661 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| eb930707-1aef-3114-af01-2b7cb349166b | -4.09754 | -48.27039 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 84e45b86-4c2a-3ff2-bb8f-d82ab988a939 | -4.09643 | -48.2548 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6d9b5c4-9eb0-3fba-a6a4-7c7d2b781c52 | -4.09526 | -48.26234 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5604ca9d-f669-35c4-850f-92e949fa0479 | -4.09297 | -48.25427 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46c604fc-dfc2-3df7-b1b9-7014ddef9fdf | -4.09011 | -48.24991 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5466f675-9de8-376b-b93c-2e655ae7671e | -4.08602 | -48.27636 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d1dca3e-78a4-3dbf-af26-523bcfe698a6 | -4.08543 | -48.28012 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f1b00fbb-b1d5-30ec-89b4-8ad55db7eb98 | -4.08257 | -48.27581 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69613b83-d72c-3b11-8f6a-13a8105e5485 | -4.08198 | -48.27958 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2636e9a4-e6d6-3593-a741-b0ca5384ac60 | -4.07888 | -48.11576 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae88d635-c082-3d52-86bc-03941fff65b3 | -4.0754 | -48.11523 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2de505b-1e9e-34ae-be3a-3ea7d56ea2b3 | -4.05317 | -47.92667 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0a05569-f054-3f7d-a602-2ab5815cac57 | -4.04967 | -47.92614 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ee2cedc-72f7-3647-9f98-79cb1df9c38d | -4.04556 | -47.92951 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f792289f-f36c-389a-ad12-0c007fc936d6 | -4.48214 | -48.10756 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73f7df5c-4c29-3ff2-8e64-929f2dcbbc05 | -4.48155 | -48.11144 | 2024-10-10 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2fe97dc1-07fd-37dd-8147-6211439776b2 | -4.17893 | -48.00845 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6c1498e-b936-329c-ad89-46fc74e67908 | -4.17775 | -48.01622 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc046866-f10f-39f2-8177-87bae53d3401 | -4.14849 | -47.87253 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 529b7288-e682-3d54-aa8d-3700448a9b0f | -4.14498 | -47.87196 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b78974e0-ca6c-3d68-ac26-e0ebdc9b1d58 | -4.11541 | -48.26918 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 9039a6c4-0426-3536-acbf-029cc14b015e | -4.11254 | -48.26493 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 3dbe19e9-59c4-3a54-ad03-c8c93dce0442 | -4.10908 | -48.26439 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e035a782-a59d-3940-aa91-ea64e4a2e985 | -4.1068 | -48.25636 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| e4db813d-b4df-3945-b93d-6f80064a45a3 | -4.10334 | -48.25584 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 9db2e37c-d8b2-328d-bf75-af34d1b4862b | -4.10159 | -48.2671 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 6dd956fb-0a81-3934-9653-d0c30492f849 | -4.10042 | -48.27464 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 747251c9-70f1-31fd-803f-02836f8de629 | -4.09988 | -48.25532 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4638bc75-cca3-37f9-83ed-d331fdc795ae | -4.09702 | -48.25098 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fa310fad-a5b8-3024-b926-ac36f4d8ad85 | -4.09584 | -48.25857 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3374d31-cd8c-32bc-a2a5-54ad7bd23ba1 | -4.09467 | -48.26612 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 68bb2dd5-13c7-31dc-a723-4eb71750822d | -4.09357 | -48.25045 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62be58c7-52e0-3a23-9939-4f58f7615c58 | -4.04906 | -47.93004 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78bd7f64-08c5-3a49-9aad-ef465c37f1ba | -4.04617 | -47.92562 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aef521a-4c36-3668-801b-faa7afeec348 | -4.00271 | -48.38257 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3262fd17-2940-398d-a31f-e914cc34efea | -3.93972 | -47.95739 | 2024-10-10 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbb5064f-0e90-3ae7-987d-909dbd33803b | -3.9167 | -48.35083 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8e65bec7-1f20-30d2-9ba7-46382f95c179 | -3.91383 | -48.34658 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4b6fd96c-3074-3353-ae8e-ed03983cd28d | -3.91326 | -48.35031 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf89a964-a562-3619-8d90-97594a4732c4 | -3.91039 | -48.34608 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 292804e5-7d5f-31b8-a109-0175d0e24751 | -3.90982 | -48.34981 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ab0afd0b-4003-3ba9-a19b-d4b8b61b2267 | -3.90408 | -48.34133 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| baced2a6-ff44-3be2-9f96-346eeef0c060 | -3.89475 | -48.33624 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f42ae0ed-d33f-396c-84b9-3ff9b9dcaf26 | -3.89131 | -48.33571 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d23260d3-eb7d-3d47-a15e-641dfbed5031 | -3.89124 | -48.35862 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23e273e6-065c-33da-9220-7d1e871fa46a | -3.72446 | -48.349 | 2024-10-10 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7806f00a-9495-36dd-96ed-0edc8f6e93a6 | -3.72389 | -48.35267 | 2024-10-10 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2e62609-3367-3ae1-b91e-4bcfa0f28788 | -1.28827 | -48.81949 | 2024-10-10 04:42:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76b24cf0-f046-3e51-bce2-5db0b2217c8c | -2.16299 | -48.96146 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c6812364-ab96-373a-a135-fc270ff3dcad | -2.15402 | -48.90968 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dd5a3c4-52b2-31b4-a2f9-42351512829b | -1.92787 | -48.94353 | 2024-10-10 04:42:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5c7473d-3939-3d49-a09d-b9b8757e8391 | -2.01169 | -49.55699 | 2024-10-10 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43dde40b-70e0-37d6-b009-176d9ed11cb2 | -3.075 | -50.48714 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8295cfd4-7694-3a62-8d31-150bdede40ab | -3.06785 | -50.48955 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0f2b761-f219-3ec4-9c1a-63b55186fd0b | -3.06721 | -49.5195 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c3a3ce1-39d1-3a76-a64a-3c0018e5672b | -3.06667 | -49.52297 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54ea59f8-3a68-3e6e-910a-a927cd97863e | -3.06613 | -49.52644 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4122844b-56ab-385b-b71b-0c5b8a24c62a | -3.06455 | -50.48904 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de833b8e-2350-3c7f-891b-faf01a760df0 | -3.06281 | -49.52593 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6dce588-63b6-3d50-9a49-68c89285ecf0 | -3.05642 | -49.37147 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb5318d0-f2fd-329a-abc4-b440ffa1dd4c | -3.05592 | -49.39637 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe1666ac-5a17-3297-b2ed-7d2f91d62907 | -3.04374 | -49.6255 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a02694cd-d7fb-3dba-b82a-41687efa1606 | -2.9932 | -49.70971 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43a77385-98b0-34f5-8f93-68fd7516792a | -2.99099 | -49.52867 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f790c61f-0e22-3522-b7d8-cc03bb405f4b | -2.99045 | -49.53214 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3ffa515-8198-3e22-aba3-90eb282a8428 | -2.98767 | -49.52816 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13b3a9ed-6469-3d99-ba21-bac28c0b6e10 | -2.98713 | -49.53162 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6bfde829-3936-3cb6-8feb-e8b27b4d1849 | -2.98381 | -49.53111 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15837118-0396-32f0-8e75-c9a119e37cea | -2.98104 | -49.52713 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 562608b1-0d42-3ffe-8743-f2ff2665fc0d | -2.98049 | -49.5306 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c96dfca9-c0df-3044-9efe-74740742ed2a | -2.96732 | -49.29045 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d120018-1d00-35a9-b34d-8d4c375ff4ab | -2.96677 | -49.29394 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08b4a4d5-1e84-3d86-a1b3-afa7bce0812c | -2.96622 | -49.29743 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fe79413-7d49-35ca-97d5-93bc776f816f | -2.96357 | -49.35775 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f8db2f8-59ae-3546-9acf-d96f43ba34d9 | -2.96344 | -49.29343 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c55f051-08b0-30f8-9114-9609d854eb7e | -2.96302 | -49.36124 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b05a830c-8254-3105-979c-4d2f00ea68db | -2.96248 | -49.36472 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cd8962d-b949-3d17-b3b3-a13da1416ce7 | -2.96024 | -49.35724 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3092ff9-f477-3a51-9157-c367618201f6 | -2.95435 | -49.19887 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25275394-c413-37d5-886e-d775d7a7c5f1 | -2.9538 | -49.20237 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79a296fd-f29e-3c90-a3fa-40227bd539bb | -2.95102 | -49.19835 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0feb553e-5db5-3936-a471-c3bef5da14f0 | -2.95047 | -49.20185 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c383330-1805-3c50-879a-6d76f83bae56 | -2.94992 | -49.20536 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0d542f5-6b51-3eaf-a3cd-6afc17ea5006 | -2.94938 | -49.20887 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc4ef875-bca2-37cc-9a5e-1552d2f66b89 | -2.94883 | -49.21237 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e7bcaed6-fca9-3ff9-bad8-b631f700cd5a | -2.94713 | -49.20134 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78eda65b-a5f5-310e-9174-ea40a1c0509a | -2.94604 | -49.20835 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7cb605e5-5ab9-329d-a93d-b4f9f927655e | -2.94549 | -49.21185 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f5d76411-d493-317f-8a4f-d73548c71672 | -2.899 | -50.39584 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d86346f4-4a62-3c33-a8e3-4c129fd77897 | -2.89846 | -50.39928 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3987ce10-f358-3289-a64d-6047bf2296b5 | -2.8957 | -50.39532 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 422f4946-c4b0-3d16-854f-403fba109bd7 | -2.89516 | -50.39876 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 320928ae-314e-31a3-9afb-72a649022bd7 | -2.89462 | -50.40219 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe89a48a-aa78-39b2-9737-0668520a64a6 | -2.8924 | -50.39481 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7067dd5-6de0-3005-9f4d-09ed583271ea | -2.89186 | -50.39825 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b043358d-d01d-3ed5-81af-1b71e3982686 | -2.89132 | -50.40168 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2248a016-6a0d-3d96-ba7a-939764491617 | -2.82741 | -49.53199 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b0d1670-8a49-3b52-a9eb-f0be02e1324f | -3.65939 | -49.51149 | 2024-10-10 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90ab8f6a-c719-38f2-915c-92bef0d75194 | -3.65311 | -49.63874 | 2024-10-10 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README89.md)
