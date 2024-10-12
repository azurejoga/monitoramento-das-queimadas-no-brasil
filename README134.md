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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a213445-6693-3de6-992c-08a7c4616761 | -10.59976 | -63.99221 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f904b2e-969d-3802-9b2d-7d26213046b9 | -10.59624 | -63.99158 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cddc6d48-a2c3-3faa-ae6a-644b1ede49ed | -10.58987 | -63.98617 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31c730a3-069c-3dcd-a71b-f71cb6f1092f | -10.58701 | -63.98151 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ceccf058-cab4-3276-a8a0-d85fd4543318 | -10.58635 | -63.9855 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc9e9204-6771-32ea-bee3-341e9b35b7f0 | -10.58584 | -64.50711 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3f5462d-77b0-38a0-b478-ae1dc95bbe86 | -10.58282 | -63.98489 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8daa7952-2cc2-3d6e-ba79-32e77be45193 | -10.58146 | -64.48888 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e1cf521-c2b3-3b23-a922-1e6746c37418 | -10.57857 | -64.48396 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59d0d679-c823-3f09-8b12-83bee4260f86 | -10.57781 | -64.03726 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0387283a-6de0-38ed-b1b7-66d0766a5485 | -10.57713 | -64.04139 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21bb5db3-c556-39bf-8a8c-302be751c600 | -10.57427 | -64.0367 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b994dee-7c04-32df-a401-3d6933670f6b | -10.57359 | -64.04082 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7041b2a2-2a84-33cb-99f0-a55ce7c31c0c | -10.57072 | -64.03615 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5bc92bb6-0c1c-315c-8f97-bf68229054e4 | -10.57004 | -64.04025 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf1e0a3d-b7be-3b5e-8760-bdf3038ba9b6 | -10.4958 | -62.97934 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a27886ea-179e-3df1-bc31-ac8e299365d3 | -10.49238 | -62.97884 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73fe76c8-0cfe-3c78-98bf-baba1954e56e | -10.45753 | -63.14879 | 2024-10-12 05:25:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68b4ec49-687a-3824-974e-570d7102f265 | -10.2621 | -63.34282 | 2024-10-12 05:25:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c815e34-8386-3770-915b-d5a5433ea589 | -10.21065 | -63.31075 | 2024-10-12 05:25:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81e508d3-15e4-3913-9205-44bf3d73b31f | -10.16277 | -63.22128 | 2024-10-12 05:25:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48cea908-9605-30fe-968f-f61817d84b24 | -10.15933 | -63.2207 | 2024-10-12 05:25:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e74de78-3d27-3b9f-8338-1c6f60852eee | -9.7171 | -64.13623 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1637706-2b89-3283-8a40-2b3211475376 | -9.58622 | -64.09366 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7b8a7abe-2d14-32bb-b41f-8e06b7b46727 | -9.58553 | -64.09779 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 67e63a6c-5391-3c34-8ff4-345ef32ca4e5 | -9.58264 | -64.09302 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fed6bc6-c606-3c7d-9cd4-be3d5a95163f | -9.58195 | -64.09716 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b294c44-d8ff-32f8-9af3-9470ab4c3ecc | -9.58127 | -64.1013 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 443540e2-4290-3704-bff3-70d5a6dea0bd | -9.58058 | -64.10544 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58080046-4537-3865-a1f0-9bfdae5a9c3c | -9.57768 | -64.10068 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4b8fe14-06fc-3dc1-83e9-6c46f8f0a791 | -9.577 | -64.1048 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91459bfe-7889-3ba9-b10b-819ace7ecfcd | -9.56186 | -64.19604 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15f6fdb2-0082-3185-a375-fd3f2c9882e0 | -9.56117 | -64.20021 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1993425-26aa-320b-bcb9-01ffad88448d | -9.55756 | -64.19959 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 193dfbd6-e1a9-3597-92dd-55398ce6405d | -9.51335 | -64.3085 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23f24130-aaad-3c85-a972-45568f7c0c0e | -9.50972 | -64.30789 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de73821b-0626-3a7a-b77b-7576c5c79176 | -9.5061 | -64.30727 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80796493-286f-3dd0-8ccb-c74386dfb365 | -10.69496 | -63.63564 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a066cff-ee04-38c6-9e4d-f5329947173a | -10.54673 | -63.83218 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 535fd3dc-a07e-34e3-9c21-6af12d524530 | -10.54608 | -63.83604 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e45aac01-f732-3cd3-9289-9e0e2cb48ea3 | -10.54322 | -63.83159 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a528117-cc4f-3a74-90e8-f58797ccf9af | -10.54268 | -63.83247 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b44725ee-2081-3590-9a80-f6b79102e884 | -10.54257 | -63.83547 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9ea699c-9484-3ea7-9028-ca04a9e44288 | -10.51635 | -63.90533 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b553dc07-632a-3e79-a516-11f1ba676df7 | -9.91988 | -63.82222 | 2024-10-12 05:25:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10f12c6e-d75b-313c-8e46-a8affee04146 | -9.82128 | -63.63187 | 2024-10-12 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2845c995-ac9f-3b86-aae0-e576337ebd60 | -9.80967 | -63.8537 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b048515-a919-3285-8ca9-4ce209cc0db1 | -9.809 | -63.85771 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73dcd2a9-2cff-3003-ac85-590c5ef1325b | -9.80613 | -63.85311 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b444ea55-043e-3d05-8492-7e52a53bb231 | -9.64132 | -63.41108 | 2024-10-12 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dadc911b-667f-35c4-95d1-b56674e232b7 | -9.5129 | -63.49019 | 2024-10-12 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4c9b6fd-d09b-3474-b0a2-214a5fb1baba | -9.51225 | -63.49411 | 2024-10-12 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d99a819-d402-3dbb-b373-bd18363461ad | -9.51198 | -63.49081 | 2024-10-12 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89f1a0a1-328c-364a-86b7-cfb2ca6d363b | -9.49544 | -63.13313 | 2024-10-12 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e2dbcf0-31e3-3226-a9dd-8b7458da2a35 | -9.49261 | -63.1288 | 2024-10-12 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75004b45-4695-3e8e-b6a0-ad36621929df | -9.49199 | -63.13256 | 2024-10-12 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a16b202-ad7a-3cfd-8440-cc43cadccae8 | -9.46274 | -63.70517 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c27c4b6-0f80-3acc-a3bd-d99d57383299 | -9.4621 | -63.70914 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f576499-3e2c-3601-811d-49f4de90fa50 | -9.45921 | -63.70459 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5793ca51-a2e0-3592-918d-09ce7263d51f | -9.35748 | -63.81434 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d6d5645-25f4-3faf-98bc-e3407603ddc1 | -10.05686 | -63.25092 | 2024-10-12 05:25:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef50131a-c1ef-3220-bf32-8281d7f02c2f | -10.00865 | -63.28577 | 2024-10-12 05:25:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5d89955-424b-36a8-8e5e-07ae4f58a2d6 | -10.97492 | -63.99477 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40f20ede-7fd9-3bc1-a6c0-27e5fa8ce51b | -10.97143 | -63.99401 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dd1d3af-40a3-344a-a12f-de5e503ab121 | -10.97031 | -63.95746 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7cb627f-c578-3053-8402-ca6696770d88 | -10.96965 | -63.96138 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c3944b2-151e-3d59-8294-fc7231112c75 | -10.969 | -63.96531 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c2d1d36-a58a-3d9a-afe4-373b0763d68f | -10.96857 | -63.9895 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 252cfa2b-bf66-3d91-94d0-68022edd5ad5 | -10.9679 | -63.99351 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18f097bb-4550-39fe-b39e-33f85ed6553e | -10.96502 | -63.9891 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2451d33-ef9b-3b91-ab8f-fa7aa2bd6f30 | -10.96128 | -63.96822 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f712d714-8ddc-3bd1-9d10-2f623e82c0e6 | -10.83897 | -64.22364 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb08afd9-45d9-31a4-a34c-f711cfb9e56c | -10.8354 | -64.2231 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 60ebe006-b7c8-361a-824b-d1443a5f1786 | -10.83281 | -64.17313 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bf23f50-3cdf-394b-9cef-368f74060bcd | -10.83032 | -64.20979 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bb45e8ac-61b5-313d-9778-ffd668ffe96f | -10.82859 | -64.17657 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 325c9379-b724-37ac-9103-4a36ec956b2d | -10.82675 | -64.20927 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 524465b2-db37-3739-a9f2-5e8d2a0160a4 | -10.99304 | -63.59578 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3364d53c-3ca6-3093-8eb2-050482d56f69 | -10.98958 | -63.59521 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2106d96-9396-342e-b94f-fae1f8c5ffed | -10.97855 | -63.59745 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 337722f8-404d-32ba-9bd8-a14fde8ccb05 | -10.97711 | -63.93834 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eeb60d6b-3ed5-3b75-a2f5-8288d4b50360 | -10.97646 | -63.94226 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e1bcc5c-430d-39a3-88f5-77e9152b6cfd | -10.97509 | -63.59691 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a40e39ed-2aef-33ef-965d-782c63edad5a | -10.97226 | -63.59247 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| feddbd41-646b-32c0-8f0d-e13506e565f5 | -10.97099 | -63.60024 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ef775ff-92a1-3d4b-b73c-d63ab9669a44 | -10.96817 | -63.59576 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a20c7854-baad-30ea-b220-879a43d73078 | -10.96753 | -63.59961 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6c87dcf-19f7-3ad8-9ed1-b7524850d0e4 | -10.96408 | -63.59898 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| abb2bdad-19b5-3a40-93b6-f996f933818d | -10.96365 | -63.57998 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff128644-94bf-3e3d-85f8-e52605549471 | -10.96063 | -63.59837 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e4c5b11f-bf96-3fc5-9eae-52b10630e296 | -10.96 | -63.60219 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95abbc8b-c3c5-3514-baf9-244ab12e3e8c | -10.9555 | -63.58635 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94db9d00-4515-387b-a6f4-33f5d172a28f | -10.95201 | -63.58591 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa28992e-05a7-303d-95a5-ffe9ace1415f | -10.93853 | -63.86348 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33d1f112-2500-350c-b8e9-a399aef05af5 | -10.93791 | -63.86723 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 325c90a0-3545-3a38-9d0f-1d687468acd1 | -10.93729 | -63.87102 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c1c671c-f35d-3352-b60a-eb50dcfa67e7 | -10.93568 | -63.85898 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64bf49c8-b11b-3b27-8a77-98aa2e4b7604 | -10.93505 | -63.86275 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6ea21c9-456f-3a96-a8c9-695953d517f1 | -10.93382 | -63.87025 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b30cee6a-71db-3572-9afe-f03206f11a8e | -10.93316 | -63.87424 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README135.md)
