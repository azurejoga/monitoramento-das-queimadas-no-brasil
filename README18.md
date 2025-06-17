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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbb8d5d3-0788-3384-bd98-fa16dc232b27 | -7.2396 | -43.08394 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 277598a8-c1c4-3f6c-bfa9-2adede6f816b | -2.44829 | -47.49672 | 2025-06-17 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88c9ccb3-2b61-307a-a0c5-0aff2ef834c0 | -6.22395 | -43.3321 | 2025-06-17 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02109838-6beb-3451-91a7-e58f5bda1222 | -7.72108 | -55.13618 | 2025-06-17 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd1467ec-a397-3a35-8c48-3177325f9248 | -6.16025 | -48.06063 | 2025-06-17 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ff0bdd3-88ae-3509-92eb-c737219588e0 | -7.23897 | -43.0886 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8ffef764-b7a0-3773-b8a6-c2de4f7461d7 | -7.19895 | -45.35144 | 2025-06-17 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce99dcb7-7666-38d6-ba9d-5b294bd6e9fa | -7.26709 | -44.64415 | 2025-06-17 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e542448-97f5-331a-817c-4a05ecc77794 | -15.40543 | -47.84461 | 2025-06-17 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e5a78b3-b94b-3c2b-83bb-5a1bc6d9db8a | -10.84293 | -53.77934 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29d96700-2001-3841-b1c7-bd043c244d85 | -10.92719 | -56.83994 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa3c6631-7416-3d2e-8b09-2be0e87616d4 | -15.26354 | -51.47002 | 2025-06-17 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b647b9d5-96db-39d3-83e3-7be66ec01a13 | -9.46281 | -55.93328 | 2025-06-17 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f13185a5-6f04-3e06-828c-69a75ba5bb54 | -12.02683 | -57.09273 | 2025-06-17 04:57:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 546a6f17-d765-3a22-85cd-8cccc67d5f7b | -9.44715 | -58.21768 | 2025-06-17 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9cea8fb4-2254-36f6-9b34-a341d4dc8536 | -15.57084 | -55.64812 | 2025-06-17 04:57:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eec49cc8-b4c4-309e-85ef-a7892a0bcfa5 | -13.38714 | -48.46225 | 2025-06-17 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5517a9f-f9e4-3b22-b24f-355f35fc9e1d | -10.92779 | -56.83625 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3be68ab9-8cb5-39fa-9dc3-b9de6b5b8f37 | -11.57046 | -54.56535 | 2025-06-17 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93dd1862-f81b-38b4-bbec-cc1406e648a8 | -10.92659 | -56.84364 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c561e906-b4b7-339f-b4e7-575ed50bfd79 | -11.1361 | -53.94749 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ad2c69b-3a31-38da-b230-4fca1f433c5e | -13.58422 | -54.28359 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 707a10dd-8feb-3399-a56b-27022a3c04b1 | -10.24181 | -52.22028 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1884424f-24a1-3b1d-b169-9e986dec8cff | -15.40103 | -47.83812 | 2025-06-17 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d794e64-a88f-352d-afbc-9b5d3248f052 | -9.70137 | -49.47982 | 2025-06-17 04:57:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37d1e9ad-36ea-38be-ae0e-762e22e6936d | -14.02585 | -55.12731 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7984b693-e99f-3836-8a91-f1d8baebbac2 | -11.88369 | -54.6694 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc3cfd1c-580d-3729-916c-79e96251945d | -12.02653 | -57.08939 | 2025-06-17 04:57:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13572f5e-8b68-365e-bd20-ff22f61656fd | -15.8875 | -48.89381 | 2025-06-17 04:57:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8bc479b8-bba0-3860-9df7-15bf9274890f | -14.84809 | -52.28578 | 2025-06-17 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2af3793d-99bb-3696-aa79-65e0571dc5ad | -15.40577 | -47.84174 | 2025-06-17 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 925b4024-4776-3337-a0c4-7fc45c292c45 | -12.23032 | -44.2169 | 2025-06-17 04:57:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16237983-b7d6-3836-be82-5275b805f941 | -14.82075 | -48.43362 | 2025-06-17 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d2c64d0-aabf-368c-a5d5-b05ba077e50c | -14.93671 | -56.29473 | 2025-06-17 04:57:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 308a8bdb-3531-349e-8024-481d7810bde3 | -9.40858 | -48.41997 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98977e1a-d8bb-31e5-8b5d-9eb5d55e76ce | -12.66042 | -54.11894 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fc1240c-3813-32d3-a65f-f116eb929ae9 | -13.44068 | -56.85231 | 2025-06-17 04:57:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a8d67bf-29c9-3d08-a4f5-5921d750bcbe | -10.29336 | -60.54687 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87c531d6-b2ed-35c0-968d-32be0cfdea81 | -11.78835 | -54.78106 | 2025-06-17 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd3c263d-3bed-317d-a9c6-53a45607b7a7 | -13.29151 | -57.08089 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea4952b2-d259-3448-9d20-298075856f97 | -14.03306 | -55.12479 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0498e588-63aa-3921-8753-8837bedf756f | -14.02974 | -55.12426 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a990148-8258-335f-a3b4-930116d991c8 | -10.92899 | -56.82889 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f52604c-3545-362e-8927-58e6c56880e2 | -11.33659 | -45.21107 | 2025-06-17 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32f011f3-8c90-3565-b75c-2b11c6118406 | -10.85243 | -53.76225 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3eb062e-17b2-39e8-b89e-813cf2e1eb07 | -10.67137 | -56.55441 | 2025-06-17 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 972189b2-54cb-3995-9158-09431ebfe766 | -15.3961 | -47.83738 | 2025-06-17 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 225b25fb-3af0-3c1e-857e-7ab39f7cc33f | -11.00579 | -55.05268 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 889be74a-da93-3ce4-8ada-576cea541c27 | -12.65422 | -54.1142 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e2c8733-8c10-35dc-8e30-4d13b6f1a142 | -13.36012 | -47.84865 | 2025-06-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81388454-9935-3e1a-9caa-522d301c2fd4 | -10.45174 | -47.94975 | 2025-06-17 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0424fb2-be8e-31c9-a8d6-651f66c61659 | -11.91489 | -54.81961 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3286a25-5bbd-30a7-8b9c-a68050fcb0d3 | -11.56271 | -54.57139 | 2025-06-17 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29d06338-fdbc-3c18-823f-ec72f81978fb | -15.26996 | -51.47797 | 2025-06-17 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03d71516-c0f9-3771-957f-a6486ef2fcf6 | -14.28273 | -57.50376 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 310fba79-ddd9-3412-a261-8af8f48f9299 | -11.8826 | -54.67651 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ac3231e-2963-3431-a753-486500ef6409 | -11.91047 | -54.82614 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ed12417-3e07-3b96-8a1a-02f0f044b0c5 | -9.41869 | -48.41232 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74835f16-01c2-35bf-b990-f968cd0edd71 | -9.39408 | -48.42679 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf1f33c7-4c8f-32b3-be48-d47217bc92b1 | -9.51195 | -55.96341 | 2025-06-17 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c53e8cd7-e6b3-31bb-90ac-1bc842c402a6 | -9.52043 | -54.7146 | 2025-06-17 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 828cbccc-5bcd-355e-bc43-30934210c2a1 | -10.27883 | -47.6108 | 2025-06-17 04:57:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa50c5d3-2eb9-35f8-9ba9-497bd547fc22 | -11.14166 | -53.93357 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 09ee5301-e44f-3fa2-906f-1b05f2b58b0a | -11.00524 | -55.05618 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 640bd8d8-e858-3ac2-944f-893cd6ffd198 | -9.40353 | -48.42375 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7def0ea-1e6e-3dac-9346-7777a9163405 | -9.39027 | -48.42181 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 954f1556-0b1e-386d-971c-322001fb3685 | -11.89702 | -47.4702 | 2025-06-17 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 071424bb-2a52-3f59-ba9e-13945b6157c5 | -13.44009 | -56.85593 | 2025-06-17 04:57:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 805b4826-534b-3314-a568-610372e50ebc | -13.46975 | -46.25376 | 2025-06-17 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebab5bc5-ed11-3ea0-8594-5a5053f5d8b2 | -11.91102 | -54.82261 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d0f675f-b33c-3639-9a42-8ffd9359333c | -12.23087 | -44.21231 | 2025-06-17 04:57:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f05e2d62-0316-334c-a35a-ecd0f1000563 | -9.72324 | -48.31618 | 2025-06-17 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10059639-d295-3c69-aaa2-cbb53a83e672 | -10.93297 | -56.82581 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eefe70f5-1a73-38d6-8a75-843e40c189e1 | -15.40109 | -47.8382 | 2025-06-17 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9a3cc9c-ca67-31af-851f-92c4b3ef96be | -11.08305 | -55.05786 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e3532fc-e3ac-3315-8299-165e17b4732e | -15.57361 | -55.65226 | 2025-06-17 04:57:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 891bebfe-26b8-3b26-b39d-76461162e371 | -11.91543 | -54.81607 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 009b19a9-23f6-3597-89c6-cc1c9b3ceb86 | -11.56937 | -54.57244 | 2025-06-17 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9598270f-899a-3087-b5f9-447a7d789beb | -12.22976 | -44.2215 | 2025-06-17 04:57:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32e8fe5f-113e-337a-aa32-354943d6ece9 | -10.87974 | -54.31463 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0692cc58-1395-3a69-87e6-2bd8bb87f971 | -11.07698 | -55.0533 | 2025-06-17 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 870ca200-029a-3832-917b-613149f6a357 | -10.28924 | -60.54612 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37226a96-36bb-3779-9494-30d95c5d7d13 | -10.74482 | -48.57732 | 2025-06-17 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6effd46e-d303-3e2a-93e4-e0d0a8dd7b8f | -13.72294 | -58.68375 | 2025-06-17 04:57:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f886f3f-170e-3a6b-80d9-8b9c07f1f6dc | -11.13941 | -53.92581 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bd54fe5-9051-3de8-9f0c-c654cc3e0bd3 | -15.38574 | -47.83836 | 2025-06-17 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59b3085d-9c3b-31e4-917c-f3585f3b152e | -9.66879 | -48.76986 | 2025-06-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82d7cfe2-0bc6-3189-9418-e2eb57e25450 | -12.82725 | -47.37395 | 2025-06-17 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4481bb77-98e1-30fb-bbe1-0285136adff3 | -12.2264 | -54.29821 | 2025-06-17 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8096c8c-f4bb-30f3-8d4a-e8c137feeb1e | -9.70082 | -49.48362 | 2025-06-17 04:57:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6138da0-1057-381e-9ec5-4c2e2d869748 | -14.86291 | -45.12874 | 2025-06-17 04:57:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5137d2cb-54a8-31fa-b970-6cc15abf145e | -13.5831 | -54.29097 | 2025-06-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7bee6a4-d56f-3358-8dcf-5f08b9f1cba4 | -10.28643 | -60.53786 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 046441f2-e3af-3966-b06f-3194cb5a5771 | -12.2034 | -49.62892 | 2025-06-17 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9db1c142-a199-342e-a6fe-8a661359b994 | -9.46348 | -57.84749 | 2025-06-17 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9dfa8d3e-670e-3e1e-8c20-82f354cc93f1 | -11.39736 | -47.6362 | 2025-06-17 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ae13e5b-c0ee-3ac7-af27-6d6f79316036 | -11.13885 | -53.92943 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e39a23d-fce0-392a-94f2-d09d0a37c300 | -10.3593 | -57.22424 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 118cf2c3-b242-3bc8-b662-086fa314e787 | -10.93516 | -56.83372 | 2025-06-17 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 405663c7-ad6b-3ab7-b420-237addc0befa | -10.33206 | -48.10564 | 2025-06-17 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README19.md)
