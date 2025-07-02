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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5e42114-daa1-3872-8c4d-f73735934b9e | -7.2219 | -43.0682 | 2025-07-02 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| aad6bc79-2a71-3cf2-a025-6c8a28c8e78a | -7.7947 | -44.0145 | 2025-07-02 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 230.8 |
| d9886147-51a8-31c6-b654-3a7ab8c5a7d0 | -7.6051 | -45.7464 | 2025-07-02 01:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 5b2c7f06-9e12-38c0-ab2f-782aefa540c4 | -7.8321 | -44.0338 | 2025-07-02 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| bbabedc6-57a6-34fd-99b7-5f45b75a28c2 | -10.883 | -56.4567 | 2025-07-02 01:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0d3c88c8-ab06-309e-8688-5630cd23de50 | -7.2031 | -43.0701 | 2025-07-02 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 147.9 |
| 28fe2c17-e47c-34b6-8795-9f35b9f500de | -7.2219 | -43.0682 | 2025-07-02 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.3 |
| c524ae77-8128-3395-9cb9-7086b750037d | -7.8133 | -44.0358 | 2025-07-02 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 7615ec26-ab58-32bd-b606-8f62b841e345 | -7.6239 | -45.7447 | 2025-07-02 02:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 1ba42411-79a8-36d9-aac6-1082e723530c | -10.883 | -56.4567 | 2025-07-02 02:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 411e1fdf-7617-3a3a-b606-c1cab612b8f8 | -7.8135 | -44.0126 | 2025-07-02 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 357.2 |
| 891aba6e-8e68-3349-b191-a73715ac9565 | -7.7947 | -44.0145 | 2025-07-02 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 220.6 |
| 30f76959-2a8c-322c-90b6-3a8ac70cfb18 | -7.2217 | -43.0917 | 2025-07-02 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 216.7 |
| d7775ecc-d7b8-3ee2-b4d1-1a8489a21aaa | -7.2028 | -43.0936 | 2025-07-02 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 166.6 |
| 758fc33f-f133-3815-8db9-35780b98c893 | -7.2031 | -43.0701 | 2025-07-02 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 9059316a-8c7d-33d1-8708-ad029465eea8 | -7.6051 | -45.7464 | 2025-07-02 02:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| d6adbcaa-e8c0-3dec-b739-694c13b05ca2 | -7.7944 | -44.0377 | 2025-07-02 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 27a94161-cb4d-3f99-9b1d-be48a87c0d72 | -7.2031 | -43.0701 | 2025-07-02 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 479f6493-8b48-340e-a23b-f9c8ae49ab99 | -7.2217 | -43.0917 | 2025-07-02 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 188.1 |
| 7cb5c965-fc90-3a9b-a0ec-3bb06ab799e9 | -7.7947 | -44.0145 | 2025-07-02 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 1c844a15-8ea2-3ada-970b-1420ff499094 | -7.8133 | -44.0358 | 2025-07-02 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 187.8 |
| ef007927-0da1-3729-80c4-86a57c958fcf | -10.883 | -56.4567 | 2025-07-02 02:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3671bee6-6a88-3592-b9dd-715c6786a28a | -7.2219 | -43.0682 | 2025-07-02 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 120ae024-ad1b-3e0a-889b-ad9eb57abe93 | -7.2028 | -43.0936 | 2025-07-02 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.8 |
| 2b0887ed-a6ac-339d-bdb2-b1ef275c95b8 | -7.8135 | -44.0126 | 2025-07-02 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 286.1 |
| c9eed080-b474-3675-9ac7-218af83fe7ba | -7.7944 | -44.0377 | 2025-07-02 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 1543aca6-a7d9-303c-b631-08e9a4d8e8f1 | -7.7947 | -44.0145 | 2025-07-02 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 6b1ceb2f-a4c2-3cb0-95be-78c854769dfb | -7.7944 | -44.0377 | 2025-07-02 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| ccb6a963-f542-3a90-a3ad-2a93ae9f93d1 | -15.5332 | -49.9707 | 2025-07-02 02:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 09301a4f-662f-3dde-9ca4-d761bc6dd5f6 | -7.8135 | -44.0126 | 2025-07-02 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 272.7 |
| 0edcf60b-52c1-3ecc-8df5-123ee9c2bd1f | -7.2217 | -43.0917 | 2025-07-02 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 163.8 |
| 9acab7cd-1e64-3d80-a943-879c6981726f | -7.2219 | -43.0682 | 2025-07-02 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 3f4e3300-4e14-3730-b6f4-9e04c5e9adc7 | -7.6051 | -45.7464 | 2025-07-02 02:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 99e2c077-b314-3b56-b65b-491aa8fad3bb | -10.883 | -56.4567 | 2025-07-02 02:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 5198d719-f2b9-320e-8e54-0141947aa66f | -7.8133 | -44.0358 | 2025-07-02 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 4829af2b-3380-3bb3-9bfc-444c04fb0e27 | -7.2028 | -43.0936 | 2025-07-02 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.5 |
| 5955ea98-18ac-3a4a-81e8-e2361fe00b0e | -7.2031 | -43.0701 | 2025-07-02 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 1da74422-f6ab-3fb9-b2eb-d707f7e0869e | -15.5327 | -49.9927 | 2025-07-02 02:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 141.9 |
| f9d0d96d-f72b-3df5-991d-51106e6c4bf4 | -7.6239 | -45.7447 | 2025-07-02 02:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| bd53d4ec-e554-39c7-afb4-2102fead3116 | -7.2217 | -43.0917 | 2025-07-02 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 158.4 |
| c0fe5e98-d06d-3790-9605-b0ea107e24d6 | -6.7093 | -51.4165 | 2025-07-02 02:30:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 0b589ae3-2005-30c7-8669-0f000d204f91 | -7.2219 | -43.0682 | 2025-07-02 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 636034f8-81c4-324c-abd3-1c83211a8bbb | -7.2031 | -43.0701 | 2025-07-02 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| dd3d9308-954d-3b5c-9924-1806c48ef4d2 | -7.7944 | -44.0377 | 2025-07-02 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 99d6ecaa-9174-3502-98e9-b7214b1bc942 | -7.8135 | -44.0126 | 2025-07-02 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 282.6 |
| 23b67d15-4ade-3573-9f47-f8bd4619cbd8 | -7.6051 | -45.7464 | 2025-07-02 02:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| b65e05b0-19c9-3c37-872c-4dcebfd73dc5 | -7.2028 | -43.0936 | 2025-07-02 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| ca1e3cd2-97aa-31a3-b9b7-f17e2a09b4f8 | -10.883 | -56.4567 | 2025-07-02 02:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| f85b5d32-b7b7-34d0-bd75-ebd3e0f098d4 | -7.7947 | -44.0145 | 2025-07-02 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 2bf57d47-e011-3d20-a764-55adb07ea450 | -7.8133 | -44.0358 | 2025-07-02 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 0b8917f7-d1c5-3f84-a5a2-39c7a5ea6ce1 | -7.7947 | -44.0145 | 2025-07-02 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 221.6 |
| ce60aaba-6005-3086-bad4-d3c0a98b0882 | -7.8133 | -44.0358 | 2025-07-02 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 217.5 |
| e00abd7b-5dbf-3b54-aa2f-001421372c32 | -7.2217 | -43.0917 | 2025-07-02 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.1 |
| 09ac38b2-c3f9-3c81-bf28-dc370264f513 | -7.2219 | -43.0682 | 2025-07-02 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| ec0bf268-e0eb-3027-a1b7-d12bcd098ae2 | -7.0943 | -44.3819 | 2025-07-02 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 4c94bb99-07cb-39a0-a21b-a1be8d44ab49 | -7.2031 | -43.0701 | 2025-07-02 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| b93ae100-5995-3a60-82fe-1b38bffeb4e0 | -7.8135 | -44.0126 | 2025-07-02 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 312.0 |
| 8cb833f3-210b-34be-90aa-254930ed38ca | -7.2028 | -43.0936 | 2025-07-02 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 3c6e8c0b-c830-3748-be1e-b615faaed471 | -6.7093 | -51.4165 | 2025-07-02 02:40:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 59c9dca3-d065-343c-bab9-0f2c0eec0f43 | -7.7944 | -44.0377 | 2025-07-02 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 8f5753ed-5ea2-3bbd-95e1-d5c797e75e1e | -6.2945 | -43.6659 | 2025-07-02 02:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| b6bbf47e-5266-3064-9015-3b58fc59c848 | -7.7944 | -44.0377 | 2025-07-02 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 3f5d1fbe-5e6b-36f0-99cd-05c0dda11b66 | -7.2031 | -43.0701 | 2025-07-02 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| c7f11465-e1a4-359d-9300-43b1a6f2b544 | -7.7947 | -44.0145 | 2025-07-02 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 279.4 |
| cfe915c5-0da6-3d93-bc72-234606cc0df8 | -7.8133 | -44.0358 | 2025-07-02 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 159.3 |
| f37389d5-9e80-3798-a253-23213030ca9d | -7.8135 | -44.0126 | 2025-07-02 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 268.1 |
| a7e0e953-46c1-3549-8688-4d7a0e197121 | -6.7093 | -51.4165 | 2025-07-02 02:50:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 242d2027-5af9-307f-87b8-e0522b6c4634 | -10.883 | -56.4567 | 2025-07-02 02:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| b30b9eaf-1e42-3f51-afe4-fde094944b56 | -7.2028 | -43.0936 | 2025-07-02 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 9603a79d-7de9-30dd-9b61-a60daa9f7d57 | -7.2217 | -43.0917 | 2025-07-02 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 4ac85389-b91f-3f51-ad59-3cd2d9a63105 | -7.0943 | -44.3819 | 2025-07-02 02:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| fa5891c7-04c0-3309-ab10-24bf50c64124 | -7.7944 | -44.0377 | 2025-07-02 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 73aeff9c-38b0-3c35-a731-43c213c9ab3c | -7.2217 | -43.0917 | 2025-07-02 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 143102e3-77e0-342b-a627-4135af92afb0 | -7.8133 | -44.0358 | 2025-07-02 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 4e5ecc0a-7727-32e6-b435-349778810578 | -7.2028 | -43.0936 | 2025-07-02 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 8fe3c599-8aea-3c69-aa8f-b92106ed40bf | -7.8135 | -44.0126 | 2025-07-02 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 270.4 |
| 4e23b25c-3c10-36e4-ada1-b96e9cc9e631 | -7.0943 | -44.3819 | 2025-07-02 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3a695d12-2b49-3d97-8bfc-9ccc029fee61 | -6.7093 | -51.4165 | 2025-07-02 03:00:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 9b5f3f70-9a3e-34ab-bea5-797e34db88d2 | -7.7947 | -44.0145 | 2025-07-02 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 192.2 |
| a49cece2-1aad-3390-8f7a-f1c80a0db60e | -15.8955 | -43.4523 | 2025-07-02 03:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 61924774-7af1-35a0-a037-455085093cae | -6.7093 | -51.4165 | 2025-07-02 03:10:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 3da4d998-d336-3e1c-9202-0cc3a19c9fb4 | -7.8135 | -44.0126 | 2025-07-02 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 47ddf2cf-784b-3077-8d8e-52a799b59455 | -7.2217 | -43.0917 | 2025-07-02 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 07e92e07-74d9-352c-b0a7-22758228497d | -7.0943 | -44.3819 | 2025-07-02 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5c8ec0e5-7d35-38dc-8c3e-5989d50ca967 | -7.2028 | -43.0936 | 2025-07-02 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 72a5715f-fbb6-343a-9737-5c0e5554c728 | -7.7947 | -44.0145 | 2025-07-02 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 211.6 |
| b18ce8c5-6794-3e47-b08d-cfcfc348dd0f | -7.8133 | -44.0358 | 2025-07-02 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 1df98d14-642d-3b8f-ae9c-bdf3269ed385 | -7.7944 | -44.0377 | 2025-07-02 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9dd6f3e3-914a-3fb0-a03e-43c116624ba4 | -7.20812 | -40.25074 | 2025-07-02 03:13:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 086fab6e-9917-32be-bd77-9aa99df79762 | -7.2127 | -40.2478 | 2025-07-02 03:13:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 58b4edf5-aafb-3388-8196-50fc32bc7f82 | -7.20925 | -40.24481 | 2025-07-02 03:13:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3554c7e5-ad12-3821-b3c9-3f888d6f17c1 | -5.07179 | -37.7165 | 2025-07-02 03:13:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 77def550-8fcc-3770-a7a4-0fb02e82fd98 | -15.90032 | -43.45668 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 26256e73-e6de-3a79-9608-511e25efa2c4 | -15.89751 | -43.46291 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| b60aa2b6-a6a8-3646-af1b-4e8ca06f8a0a | -15.89876 | -43.46358 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 219c9241-0999-3e32-90fe-aca011ee171a | -15.92235 | -43.52073 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1c8c2016-9fc2-3f80-8c12-91017d258d7d | -15.92389 | -43.51386 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3337d263-a571-3598-b8c1-e28daf5b3a78 | -15.89342 | -43.45499 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 688d4553-a4eb-3791-ae6c-021807a3c1ee | -15.89912 | -43.45602 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0828503e-0419-3720-a98d-1ca03039df52 | -15.92239 | -43.51298 | 2025-07-02 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README5.md)
