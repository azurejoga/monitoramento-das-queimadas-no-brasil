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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60cf681f-56bd-3af9-8356-994c554cd5ab | -2.58946 | -51.92141 | 2025-06-29 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b8ae351-f2b5-3647-a45d-4f0c30130364 | -9.11086 | -59.04915 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c32baae0-eb12-3946-a75f-ed62103d82b6 | -9.47436 | -57.83842 | 2025-06-29 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfd6b81d-0322-36b8-90ae-c3a558aa056c | -9.35097 | -58.83571 | 2025-06-29 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c3afb12-caae-342c-bcc2-8b4c80a8586c | -9.36054 | -58.85278 | 2025-06-29 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 589d43b6-93dd-3b51-a22f-fa74f5f4c8af | -10.35147 | -57.50622 | 2025-06-29 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| aa3f1e29-42f7-382a-b7da-7634f4e8e4f8 | -11.26202 | -52.74175 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72cf8a67-66b9-3461-8f30-42aceef27209 | -11.55385 | -52.8008 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbc8c925-cda7-31e2-aabd-10f452d4c0da | -11.0311 | -56.26948 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6caade1f-deb7-3a51-be1b-17441132120a | -10.95263 | -54.36933 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b5dfbe50-8b21-3d77-ad7b-de0d32095905 | -11.26117 | -52.7461 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb542a49-4893-3b1a-9f1c-e208f7ed4433 | -9.47501 | -57.83406 | 2025-06-29 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e3ee08a-1be6-3eac-89e6-598875db2a2f | -11.77612 | -54.37117 | 2025-06-29 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7a91aa8-0120-3fb5-b767-eb78020f9764 | -10.56558 | -52.03407 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 963c71fb-45f5-3b91-bde7-b9814c417973 | -11.25676 | -52.74104 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f93e68f5-b9ff-320e-8597-e2dd222cf597 | -11.55675 | -52.77781 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aa30566c-91e6-31da-8331-5ef14c49bba8 | -9.13331 | -61.44168 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe8d05bd-2637-39fd-be26-4dd3eb6a8711 | -11.54818 | -52.80325 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 84b4c9bc-b210-3e4f-9278-fcdac29df8c2 | -9.17286 | -61.40524 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76ffe5ec-8550-34e7-809d-60bc3745012e | -11.55023 | -52.78696 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2c0eeb59-0025-3294-918e-09ffab7bc190 | -11.53568 | -52.77474 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6309051f-0ff0-3e79-af0f-304f6693ecf3 | -2.58687 | -51.92149 | 2025-06-29 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f6c0d843-497f-37d0-a38a-2ee44e100e42 | -9.92055 | -59.91122 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 656159fe-4541-3d4a-8ef6-fe1e4f6e338c | -4.5407 | -48.02648 | 2025-06-29 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4bd551c5-37e5-35e8-a2e6-53d70fb2ea50 | -9.5308 | -63.57508 | 2025-06-29 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af198910-911b-391a-938d-abba802d2862 | -10.55831 | -52.04764 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c641e376-be45-3d48-9238-0c9aabdad1a1 | -10.03342 | -54.3288 | 2025-06-29 05:23:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1df3461-641f-37be-b608-b3b9a14a8ccd | -11.01255 | -56.23284 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5200b5f1-56d3-31e8-bf0b-eabd09aab043 | -10.04261 | -59.35762 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 32962e6c-33bc-37f6-afad-d9e0df785caf | -4.54138 | -48.02145 | 2025-06-29 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80168617-4e98-3ebb-b42f-4fd7dd88f4da | -9.70541 | -56.1872 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 194274cd-0e25-3081-8891-940227437687 | -10.55285 | -52.04689 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6c1bf4b2-a598-3d43-83d5-1cfeeaba67b0 | -11.02908 | -56.28452 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e470af18-b9ed-3ba7-8028-2ced2a57b33f | -10.56011 | -52.03333 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd3a1fcc-db69-35ec-bb08-2287dc67b6b3 | -11.5587 | -52.80478 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5da6d281-ad7d-382b-b7d1-83c65e535d1e | -10.5542 | -52.03615 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e6f1bc7b-f3c0-3707-b519-cc6a98522964 | -9.43193 | -47.95334 | 2025-06-29 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 38e66aef-703d-3092-bc8d-08cbf71fcd49 | -9.42423 | -47.9585 | 2025-06-29 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f34a0aaa-5b0b-31b1-8c8b-59fe7e600a38 | -10.83885 | -53.76943 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2655f3b1-86d8-32f6-914c-aee3e400cce2 | -3.62544 | -47.54315 | 2025-06-29 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dccfb598-aa47-3878-9cfd-3b1debc61130 | -10.05638 | -59.35978 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c55d9793-2646-384d-9ca7-236cb3999770 | -10.83465 | -53.76334 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2fc012ff-a6e3-3748-88c8-b58dc5c6f3a9 | -9.25342 | -57.52954 | 2025-06-29 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67c1b31f-0101-3c7e-a7de-afad8f0d4885 | -11.0337 | -56.2814 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dd501e3-971d-3ac1-8a17-2f641ff5de66 | -6.6283 | -47.28045 | 2025-06-29 05:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4ea19e04-2e5c-3d1d-ada7-934b0a507ebe | -11.55468 | -52.79423 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 81410cc6-7931-352e-9ee5-d2bbee6698bf | -11.01202 | -56.23665 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0265519-7378-3113-9a4e-0b306211ee3d | -10.52797 | -53.6265 | 2025-06-29 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abc2f35a-73c7-3f10-bd39-eaad8bb80309 | -9.09015 | -59.49216 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86e32791-9aa0-3695-a627-a5c27067c04f | -11.55592 | -52.78437 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e6c49b03-5af8-3cfb-814b-25c3d7b93fcd | -9.44224 | -67.55453 | 2025-06-29 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b98f4f5c-6d20-3831-96c4-6af7912d55e2 | -11.26771 | -52.73915 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74ecb2c7-5776-3824-af5f-698a47e6bc92 | -11.56036 | -52.79161 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b6395679-236b-39cc-98ac-788b362ab8d1 | -11.54136 | -52.77222 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bd4ae426-76ac-3806-90a5-e752797df224 | -11.53972 | -52.78534 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 248ac6a3-9b24-33f4-a5a3-d75d41b515b5 | -11.03472 | -56.27387 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74652ec8-afe3-34c8-8f45-994c47ec16ec | -9.08274 | -59.47207 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 948f888e-87c4-3ccd-a7bd-58a477aed0cd | -11.02084 | -56.28329 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64c76977-577f-3773-91b0-f074842f9b7d | -11.04211 | -55.3761 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33088e79-4606-3c61-b7d9-ce916b0e65e4 | -11.13993 | -53.93086 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5375aec8-1ed9-3af1-9d6d-b887fcf63ee6 | -9.70644 | -56.17991 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70c0955a-b09d-3cc8-b096-d6a42703daa0 | -9.70999 | -56.18419 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4414cb4f-97b2-3e93-9981-1804494430a3 | -10.8556 | -53.75507 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83e7745b-8dd5-346d-a66a-49f64acfec59 | -10.85001 | -53.7599 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 735951d6-ecf1-3c93-bce5-677f4e6cf58c | -11.27291 | -52.73753 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd831026-8edb-3d87-9693-60cd905524ae | -11.0079 | -56.23594 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a9900bd-0a5b-3ff8-b585-7015c0f90cd4 | -11.01855 | -56.27998 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d12b7bd3-6c08-35f6-9265-3e6dcd1b3e94 | -11.02336 | -56.26446 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 282f7c7d-58a0-39e9-8ecc-3e59cdaf58a1 | -9.08731 | -59.48793 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 816eb632-fa77-3b3d-89ce-51d23ef3b520 | -11.04165 | -55.37452 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 225fb9f3-35cd-3735-b74c-d41b283507bc | -11.55953 | -52.79818 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 567b8335-3073-3f0c-8ef4-53fcc46a2d3b | -9.08614 | -59.4726 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 433f47e3-81a9-3b81-905e-cebd8c539ecf | -11.26685 | -52.74582 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bcccb305-a214-3476-84af-68d0bae5c916 | -9.47057 | -57.33517 | 2025-06-29 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97355c68-8b40-321a-a3bd-782a5001bdf8 | -10.55464 | -52.03258 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e6d9566-19cd-37af-8b6d-ae710bd2a3b9 | -11.03833 | -56.27828 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c301bd92-67b3-390d-a00c-403732dd62de | -11.54621 | -52.77632 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3da68847-d8ba-3530-ab16-7b9f9a2e7790 | -11.54663 | -52.77299 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| db0c0059-6ae6-34c0-804f-74901106a089 | -11.00896 | -56.22836 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e7286a0-b614-3135-8c3a-01c1f6aafba3 | -9.24984 | -63.29342 | 2025-06-29 05:23:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4599be37-3d9b-34bc-8db6-8dc7e7565137 | -11.02437 | -56.25692 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bea04ddb-20a4-3af6-8bdc-6db5e9870b60 | -9.92111 | -59.90757 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb399ed3-0fd5-3823-9850-7f0ab7638fbf | -11.26198 | -52.73939 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05ff5ed6-a463-3e61-ac11-6131a333e151 | -4.66357 | -55.96546 | 2025-06-29 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dde24e9-0d8e-3f65-9adf-0fa51bcb91f7 | -9.04037 | -61.23139 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88004044-3058-37ba-8af4-ba5eb9f0134c | -9.71051 | -56.18053 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4aedc126-d15b-3aaf-8af9-00f64a30313e | -9.71814 | -56.18539 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f979955-13e8-32f8-b854-aa963a97765d | -9.70947 | -56.18784 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 761be49a-edf6-31bd-9f57-fbcae2b17f61 | -10.56422 | -52.04483 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26c6eb00-5d4d-3671-83a6-0f3bff896eff | -10.83535 | -53.75785 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3146f748-74b9-3525-a567-c4960170cd09 | -11.26075 | -52.75163 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e0c2645-eb0a-38c4-b25c-ede00aeed653 | -11.03263 | -56.25811 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ef9d51a-91fc-3ada-9ecf-a8dd0f399fb4 | -10.55787 | -52.05117 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1552086a-9809-3d8b-aae3-308423e094fc | -11.27341 | -52.73651 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84958a27-af69-3275-8ee7-fd7993f4aea0 | -11.02546 | -56.28015 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17129408-1828-38c1-b3a9-acc8ce40217d | -10.83396 | -53.76876 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ad5da42-e208-30cf-8fcf-9eb79ce9522a | -10.55921 | -52.0405 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6a64e828-cb10-38f4-b153-9031327dacfd | -11.01309 | -56.22902 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 740a8842-bd5b-320f-be28-4709b0aa1a37 | -10.57059 | -52.03841 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8f8a5d1-310b-3749-bc4c-ff07d8bf5e04 | -11.56439 | -52.80215 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README27.md)
