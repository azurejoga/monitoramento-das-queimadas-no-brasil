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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 906eb85c-ec1f-3aee-893c-aac47dc3b536 | -12.12905 | -50.17304 | 2025-06-26 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a534be7-9774-3386-b9be-5586aa04d720 | -11.06456 | -46.64279 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5537b3c0-b63b-36df-b25d-86e92cf2566a | -8.86337 | -50.15709 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 355038d7-cf8f-33d9-9aa8-b7f6b46931fb | -11.07503 | -55.37428 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fe9b0956-00ee-38f7-ae9c-755cb715d26e | -10.83143 | -53.74013 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf352ccf-cdab-3230-98b6-2e7546019c7f | -6.41955 | -47.32795 | 2025-06-26 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 970672a1-0ec0-35e9-8bcb-3573b3248e76 | -11.93434 | -47.84908 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9be8fab2-69bc-38dd-bd79-a2aa3aa4720a | -10.81997 | -53.74245 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5fff4dc-7a55-3d4e-9fa4-15b97b6867a9 | -10.32196 | -52.56519 | 2025-06-26 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6ad76fb-70a3-3d6f-928c-e990975c0d1b | -11.44378 | -54.47662 | 2025-06-26 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70676dab-af36-3771-a559-ab8e0598bb26 | -11.95896 | -47.01957 | 2025-06-26 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55717038-f2b0-3f36-aece-9e34f00ede01 | -13.03798 | -48.83429 | 2025-06-26 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19e8b72f-88e9-3eb9-98c4-bc82a8baf7dc | -8.96991 | -49.86456 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5853570c-9734-3543-b460-4583ea7fb1d0 | -8.37501 | -51.0737 | 2025-06-26 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e078c126-9ee1-319a-ad57-a4622bb6d99c | -11.57058 | -52.10076 | 2025-06-26 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 599e7687-086f-34f8-9372-558813989c6c | -10.29988 | -57.13946 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffd78ba1-ac0e-3bed-bf27-6db5c652355b | -11.06718 | -55.37293 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3dca3f4b-bbc4-3e35-ba61-c4c82b0332fd | -11.80671 | -57.35855 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f358106-f44d-3f24-989c-b749eb39d3b6 | -11.8149 | -47.55583 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1401e86-59a1-33c9-a51c-e3b627997c89 | -11.13891 | -53.92349 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87e96c5d-d38d-3e38-aa30-7e28a466bd92 | -8.16842 | -46.86868 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5abe7439-2a4e-3c01-b24f-b303e7f3606a | -10.86571 | -54.29945 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d129329-47cc-3ee5-bc51-7e3e4d376c36 | -11.25101 | -51.09284 | 2025-06-26 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2dd2402-98ef-39da-8d73-deb24e569fcb | -10.30149 | -57.13055 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 096cf264-d568-3a57-bcab-d14b5a66cac1 | -13.27513 | -48.42873 | 2025-06-26 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbd12afb-ecf7-328d-834a-3ddfb363eee5 | -7.94555 | -44.87614 | 2025-06-26 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acbf03d2-9b11-3a48-bc2b-68957817b20b | -9.71027 | -49.47656 | 2025-06-26 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0b2050e-6693-384b-9ddb-c0bd05e70a6c | -10.51269 | -47.2057 | 2025-06-26 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71102365-cee4-33d8-9075-52fdaf091ab4 | -10.65354 | -44.48493 | 2025-06-26 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f370b4b3-234c-3885-8c47-3780e3c91051 | -8.71312 | -47.85499 | 2025-06-26 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7836e825-116a-325f-abe1-88f1beb95b4c | -11.0891 | -46.63247 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d266891-d7fd-34b9-9f8b-54eb1b688848 | -10.234 | -47.45686 | 2025-06-26 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41c10a6d-327e-38d5-9f54-eef900198725 | -11.29915 | -54.70705 | 2025-06-26 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f162052-3462-3fd2-b1fd-540ddb57d9d5 | -11.80286 | -47.53707 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f051466-6429-304f-929b-6729640ef3d3 | -11.8344 | -51.2566 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35f84938-3bcf-3568-ac18-4f9144d596bb | -13.10134 | -52.29493 | 2025-06-26 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9bbb14a6-b117-335d-928e-37ade47cf01d | -12.79648 | -48.73571 | 2025-06-26 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 27cbfd3a-43a0-320b-9825-0872bd5c4169 | -9.79081 | -48.56746 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31e0328c-d8e4-3ed2-8ce5-bebef1057e55 | -12.02216 | -57.09059 | 2025-06-26 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25e8048e-a2d4-3f6b-8a56-1b7e9129a7a3 | -11.84046 | -51.26119 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de1d9505-582c-3fdd-a3f8-12097f49850f | -7.11277 | -47.84151 | 2025-06-26 04:40:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c688d56-fff3-3368-83c7-a3faab2f77bb | -9.1171 | -49.44167 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 77facdc4-904b-3e0d-951a-97a81ef9cb7f | -10.82924 | -53.73117 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 428c5ed1-2468-3454-8f40-d97063ae3f20 | -12.79302 | -48.73515 | 2025-06-26 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5c7511fd-7f36-3b0d-a2f8-66ab3d1474f3 | -8.78068 | -50.46411 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f5980bb-75ba-33f9-afdd-065ff029bbfb | -5.87322 | -50.14874 | 2025-06-26 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f9217672-8ec9-3c1e-b2d7-574ba598c842 | -11.81552 | -47.55163 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84efa7c8-5766-3f1a-a594-434706c3066f | -11.95523 | -47.01901 | 2025-06-26 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 870cbae9-e40f-3c84-9911-b5a072ea635e | -11.23913 | -49.50028 | 2025-06-26 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f75da3fe-9899-3943-97c5-ccf4d1cb635c | -11.95959 | -47.01504 | 2025-06-26 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e089a59e-28dd-3830-a6eb-e172dfb1903d | -11.81852 | -47.55638 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 85e1014e-20ab-35a8-9644-f5b3fdbf4854 | -9.11432 | -49.43764 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 885da5c8-093b-3a35-9a68-c12f17f9f7d8 | -7.94154 | -44.87544 | 2025-06-26 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03997753-7dc9-3b30-aa9d-2cd9a87014ed | -10.88027 | -56.45742 | 2025-06-26 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 92ab4c45-8f0a-3cf0-a57d-7126a55ee67c | -10.3011 | -57.14154 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99dc2699-8b6a-3423-85c6-8267d4a8500d | -10.50466 | -53.58529 | 2025-06-26 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 837ce3ad-2de0-350c-9683-2926fe6fc9d1 | -6.28682 | -47.01637 | 2025-06-26 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f2a98a0-c792-31e3-abd3-3ef98c57d73a | -8.708 | -47.98241 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e27efa2-6b1f-3609-9fee-34fb9cada8df | -8.67467 | -49.94968 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b6b23ee-53ea-3cf3-8b2b-9d6d7213a322 | -9.50767 | -56.09406 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1fb1c24e-5e55-35c1-b6fe-d78339415545 | -11.144 | -53.9375 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 393b8489-47b1-3dd1-95c6-6eaa8fbea3c4 | -11.57174 | -47.43071 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c1ac77c-6bbf-3511-818b-0755afe0af06 | -11.58491 | -44.64338 | 2025-06-26 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 827b42dc-8996-3952-a854-022a4e3a4020 | -6.95682 | -42.80508 | 2025-06-26 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c54dacfb-bc57-3719-9865-e416779dde21 | -12.80686 | -48.73731 | 2025-06-26 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1892d158-2cb0-3184-b736-5a7cad582e56 | -9.17112 | -61.40213 | 2025-06-26 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8785b314-12ab-301c-bb9f-fd737eb9d614 | -11.56838 | -52.09297 | 2025-06-26 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc248756-9c34-35e3-8072-7cdab01c93a6 | -11.6076 | -55.53704 | 2025-06-26 04:40:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b04d71a6-a395-35f9-adb6-841f4ed620f8 | -11.11378 | -46.65321 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 89b10abb-a831-37b2-9abe-ce9c651c564b | -11.80829 | -57.34988 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a5374b8-3531-3299-a007-05c361b555bc | -11.24356 | -49.49362 | 2025-06-26 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9462da40-e5ce-3dbf-8a18-c33002bc0876 | -11.57 | -52.10438 | 2025-06-26 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 942db0a1-687f-3003-a79e-6073ee5bff11 | -10.23757 | -47.45741 | 2025-06-26 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f9f5965-795f-3d42-8060-e07f0e2ebcb8 | -8.84541 | -49.85589 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6adf777f-23b2-3426-ab45-4afd12101fb8 | -6.73455 | -47.37815 | 2025-06-26 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d48971d8-1a41-389c-8de0-0e65765dab7b | -11.81191 | -57.35501 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b195370-92a9-33d8-8aa7-3ff2574f8693 | -8.48296 | -48.26178 | 2025-06-26 04:40:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 018e166f-c7d4-32aa-8b5e-c522455bd4c9 | -9.12265 | -49.44973 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c8750baf-54b2-3882-85cd-8a340f38d19c | -10.29623 | -57.13419 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f563428-0077-3954-83cd-c47ed8f78e38 | -10.1658 | -53.92406 | 2025-06-26 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07fd5cc9-d201-3ae3-85b2-47314d93c286 | -9.44406 | -47.24781 | 2025-06-26 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2afd0a8-d0c5-3f26-b673-3f7ba04b5fb4 | -11.05933 | -55.37155 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d91b8459-ea2d-3262-ade8-abe0a2408a4a | -7.74251 | -47.59518 | 2025-06-26 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1730add-0a96-367a-9454-0a4c95e28922 | -11.57718 | -46.89882 | 2025-06-26 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5f1b95f-958c-315c-8ae0-915fcf2ee6b2 | -8.70858 | -47.97863 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af5d45b2-37e8-3d03-9677-7e53202bebcb | -12.04545 | -48.08162 | 2025-06-26 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dc723865-931e-3ac9-b7f8-556e50284b25 | -6.18226 | -48.07682 | 2025-06-26 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| acc25ade-699a-369c-a141-e93f7fac9899 | -11.82583 | -51.26609 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbd010b3-18c8-3366-a667-0833b45cb83d | -10.82425 | -53.7389 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2e41376-93bb-3289-a951-ff65eba16253 | -10.87292 | -49.54251 | 2025-06-26 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d46721d9-bc2c-3adb-8266-524eadba7598 | -12.48767 | -45.89672 | 2025-06-26 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c649f956-ed6a-3b0e-89ca-c520674b2b06 | -10.87309 | -54.32357 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe56241a-ac82-34a4-96eb-83d53872bf99 | -6.17773 | -48.06144 | 2025-06-26 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 669db03b-735a-3570-adc4-824ccf690c26 | -11.07274 | -46.63933 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d8ac9ac-96ce-3b75-9e6c-21229984d96b | -8.80085 | -45.00375 | 2025-06-26 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9b20c4d-cef9-3b4d-923e-042e22c3081c | -9.50345 | -56.09338 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0c5f2283-560e-3578-9d18-e670bf4cae64 | -10.65238 | -44.4932 | 2025-06-26 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fdbf4863-e91b-3e31-8eb1-6788d96adee1 | -11.13529 | -58.61288 | 2025-06-26 04:40:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cafdf3c-764c-31e6-a3af-3dc5491a36f3 | -9.75153 | -48.66713 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ba0a541-247c-35c2-96cc-88311ffb0c05 | -6.96071 | -42.81049 | 2025-06-26 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README10.md)
