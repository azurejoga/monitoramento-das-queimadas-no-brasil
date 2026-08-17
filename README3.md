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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06770946-9d8d-36d9-a185-8449ce92ffb4 | -15.63557 | -48.89315 | 2026-08-17 00:28:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4c06c80b-234a-336d-af68-1286bb8e0f53 | -13.52407 | -46.30813 | 2026-08-17 00:28:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 40.3 |
| a14c8d60-e7d0-397e-8413-752021a3be83 | -16.60433 | -52.59021 | 2026-08-17 00:28:00 | TERRA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3c8ee8ed-5f47-3c17-8f2c-79e0be680585 | -13.79044 | -53.81249 | 2026-08-17 00:28:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 426aeef7-7766-3459-af28-14cbf16341a3 | -15.91453 | -56.47966 | 2026-08-17 00:28:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 51afac96-42e1-353e-bcae-cd94b4ec644c | -12.74941 | -59.78871 | 2026-08-17 00:28:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| cf6b4f0e-1c8f-3474-b773-4052a412e185 | -12.36512 | -50.86965 | 2026-08-17 00:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b4f0b1db-91ae-3c6e-9c2a-753e2f4e6893 | -15.90226 | -55.5174 | 2026-08-17 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 05180c0d-f8de-3b66-9635-627eefa000c5 | -10.3705 | -48.31059 | 2026-08-17 00:28:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 096882d0-f1a9-3f37-bdd8-9b196c821b71 | -14.40319 | -53.06011 | 2026-08-17 00:28:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6dd22d0-480a-3e64-bb20-7187993ea506 | -12.54936 | -47.87546 | 2026-08-17 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 8230a50a-096f-3810-805b-e6417a270765 | -14.46973 | -45.67859 | 2026-08-17 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 50fc3cdb-3210-3bee-8971-27e9b0fc9709 | -12.66754 | -48.50782 | 2026-08-17 00:28:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| e881ce51-0ca8-3530-a9db-3f1ba0447311 | -14.71152 | -47.96871 | 2026-08-17 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 0fda820d-76c6-3e7b-b652-4663cb7be4a5 | -13.5188 | -46.28739 | 2026-08-17 00:28:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 5ad60532-78d4-3f96-8c77-5b9b334207d9 | -14.49504 | -51.98811 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8f3e82a4-a4ad-372b-8deb-e1131c58ef37 | -11.70771 | -54.59616 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fc0a25eb-d48f-3350-b991-3b28c4af5cb6 | -14.45145 | -51.99067 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| df43f3e9-bc2b-3f2c-9740-15d20cc82917 | -11.48785 | -46.59402 | 2026-08-17 00:28:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| dfa4b13d-06ba-3909-b322-ede3a15b3bf0 | -11.57056 | -50.22263 | 2026-08-17 00:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6255d3cc-23cb-33df-8a9f-4345b69df86e | -15.23292 | -57.65388 | 2026-08-17 00:28:00 | TERRA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5b1d20b7-eb92-3c2f-b7e9-4cabf70cfbcd | -13.78916 | -53.80336 | 2026-08-17 00:28:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b672601e-f822-31b3-888f-e2eb98fab436 | -11.79059 | -51.80046 | 2026-08-17 00:28:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4a2cf672-f313-3ae4-8c7f-1cc5122f4000 | -15.02958 | -52.73266 | 2026-08-17 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dffdc039-2ac8-3676-8678-53b71251a1cc | -10.51083 | -50.00364 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 6ee17ac3-f331-3403-8d12-cb018fad1264 | -15.92414 | -55.54382 | 2026-08-17 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 46234d2a-999c-398b-be95-11c19ed90ac2 | -10.47106 | -50.41436 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4b73702f-3219-36de-a5ea-97dd8d9a7664 | -10.51334 | -50.01968 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| af53a217-4ceb-3b89-ad69-e2e091d790cc | -10.79097 | -50.32242 | 2026-08-17 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 759919a7-11f1-3f9d-b4d5-82ff1b52b680 | -10.50469 | -50.26237 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5804bbdd-0f80-3a36-9102-6264ab08f9d5 | -11.84832 | -51.77935 | 2026-08-17 00:28:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| dd85e356-4d31-35dd-91d6-00d1af17dc9e | -11.72535 | -54.59356 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b1ec9477-cca2-378d-848e-8b1009c2a7b0 | -14.31884 | -53.05012 | 2026-08-17 00:28:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf0190d3-b2c6-34a8-98fa-4595eb2ad71b | -14.51227 | -52.03896 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fb55b73a-6679-3a75-a945-57422826e833 | -14.47616 | -52.09372 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6ee5e541-e4a0-3b4f-a8f8-73f6e9595ca5 | -14.40555 | -53.20497 | 2026-08-17 00:28:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8e34002f-d673-3ded-9c65-a5e972ebb396 | -11.23689 | -54.01007 | 2026-08-17 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1fdd3b17-d4ca-3476-a8d7-304d7be9c00a | -10.45985 | -50.41618 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 35cccb6b-0957-3716-8815-1227583b3cd3 | -12.67059 | -48.52643 | 2026-08-17 00:28:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 987d05a6-1f00-3326-a06e-fa870a7678a9 | -12.2064 | -52.86401 | 2026-08-17 00:28:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fbb120d3-3691-3f91-96b6-76cfd9cb871f | -10.92714 | -57.1337 | 2026-08-17 00:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dffdbd70-93cc-3a42-95ed-a2c86865a4ec | -10.46219 | -50.43113 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b99dd7ce-2979-3a30-b89d-5aacf0aa1ad7 | -12.36715 | -50.88264 | 2026-08-17 00:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 37000d45-22c1-3b46-ad1c-b030771f3c50 | -10.4575 | -50.40117 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 56a8d203-3c4e-3c00-944c-4f5774e2ff29 | -10.94549 | -57.14524 | 2026-08-17 00:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 7d107a94-975a-33c6-bc3f-699c63b51d0d | -15.2363 | -56.47396 | 2026-08-17 00:28:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 656853d9-1592-36d3-b514-652b64cecc79 | -10.93902 | -57.15219 | 2026-08-17 00:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 518f4b4a-d20e-3128-929f-812968a79e6a | -15.91257 | -55.52583 | 2026-08-17 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| c88f7477-d93f-39f6-b68d-cb0ee74177a1 | -15.94061 | -47.84263 | 2026-08-17 00:28:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 45.4 |
| c52ff357-e582-3daa-a582-343b0adb1601 | -15.6384 | -48.89899 | 2026-08-17 00:28:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| faf27293-243d-31f3-b98d-67315e0f812f | -16.29316 | -53.19123 | 2026-08-17 00:28:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 30e6d05b-6d05-3e91-bdb7-7deaab252ed9 | -15.8803 | -56.33133 | 2026-08-17 00:28:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f1df3f51-3386-31f7-bc1d-85ec7ef6558a | -14.47192 | -45.68353 | 2026-08-17 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 091e22d3-bd65-313f-8d8b-531b86649572 | -11.13517 | -46.50203 | 2026-08-17 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ea505345-82ad-3ea3-bebf-299270c88b84 | -16.60573 | -52.5998 | 2026-08-17 00:28:00 | TERRA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 19d61fb4-224b-3e20-b75a-48fb5b93d426 | -15.91507 | -55.54497 | 2026-08-17 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5a40f693-80b5-3d9b-bd1a-da0b9bc8d8bb | -11.71022 | -54.61412 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| d28800e4-d9d5-37dc-99b9-f00f8960112f | -14.40421 | -53.19555 | 2026-08-17 00:28:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac365d23-0825-3690-81a8-3dd5228c1c3a | -11.50729 | -54.62574 | 2026-08-17 00:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d8cc989d-b327-337e-9476-3c2b3aa2b9a0 | -16.21994 | -57.64109 | 2026-08-17 00:28:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 28359054-90d2-36d6-b434-6f8b0918e46c | -15.91382 | -55.53539 | 2026-08-17 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 1c1a3065-4b7d-3512-aca9-c4f4d7a3297d | -11.91677 | -55.44614 | 2026-08-17 00:28:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9430e582-23d6-3864-b6db-a1ce7798ab1a | -11.70896 | -54.60514 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 29754984-2aa8-35b5-803a-6962ef268600 | -14.37811 | -53.14177 | 2026-08-17 00:28:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fe49f962-9fb0-3077-9185-d85d038c2fda | -11.88245 | -50.2226 | 2026-08-17 00:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 682b4a82-ddcc-300f-beba-31d1b898bd11 | -14.48475 | -45.67569 | 2026-08-17 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| a6061874-588f-3128-8eeb-810835583f12 | -11.23819 | -54.01929 | 2026-08-17 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 796dec00-3212-3d3f-8687-eef4a4597c5a | -11.21138 | -54.02337 | 2026-08-17 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 03987b45-8dcd-31c0-82fa-b9e74ea8a1ac | -14.40421 | -51.86805 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eee15feb-336f-38f5-a220-1aba9c5eb4c5 | -14.09445 | -53.61039 | 2026-08-17 00:28:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 07dee11a-8e72-33b4-a1f3-c66e0671eb94 | -11.84833 | -51.77298 | 2026-08-17 00:28:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| aa7c07b9-2ae2-32ba-8688-4ec26971b696 | -15.92528 | -56.48886 | 2026-08-17 00:28:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 064435c5-d4a8-366a-b451-78a94f4a3480 | -16.22796 | -49.70873 | 2026-08-17 00:28:00 | TERRA_M-M | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| baf75b57-55a9-3afc-966c-67ceb44f4e54 | -15.90601 | -55.54611 | 2026-08-17 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0ddc2e02-e34e-3646-8d7f-bba6d41658c3 | -11.71904 | -54.61283 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7b23b5d3-3e5c-398b-ae79-f2d21a6c41eb | -10.46638 | -50.38431 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| be37c4dd-1331-3d38-b14b-709b8ad49203 | -11.503 | -46.59302 | 2026-08-17 00:28:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 148b5a5f-5610-316b-8344-516ec4d362d4 | -15.1686 | -48.64755 | 2026-08-17 00:28:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 724c4cd3-54bb-3854-8c3e-deca7004950b | -14.76231 | -56.36264 | 2026-08-17 00:28:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9ee6cf78-f83f-31ed-b26c-788eb8422ee8 | -11.22925 | -54.02065 | 2026-08-17 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 13c90941-79f8-3b3e-aead-a7bfd6f47826 | -11.33316 | -55.21967 | 2026-08-17 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1df54bbf-5e92-3e40-ae5a-f36add92c5cf | -11.72029 | -54.62181 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| caf4f2e5-826c-33e2-8404-d7163dea0386 | -16.29185 | -53.1819 | 2026-08-17 00:28:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bb4aab89-cf57-3990-9f98-724cf482e051 | -13.78157 | -53.81383 | 2026-08-17 00:28:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 43a349d2-dd2e-3d92-a6a2-e098a6730abc | -15.94242 | -47.83656 | 2026-08-17 00:28:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 34.1 |
| cd8eace4-ef37-36dd-a0dd-a83d6e0c9c64 | -12.9032 | -52.82561 | 2026-08-17 00:28:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f257ff4b-4ae9-333b-afe1-d37cd0a54073 | -15.91322 | -56.46917 | 2026-08-17 00:28:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| babf8ec2-7314-3ee8-a174-7fab765b884a | -11.82851 | -51.78266 | 2026-08-17 00:28:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a26a79fd-9a7e-3f6d-83aa-eaff63c847d3 | -14.09616 | -58.43374 | 2026-08-17 00:28:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 98c81a75-77b9-33c3-b0a2-3e7b280668da | -6.6199 | -58.9643 | 2026-08-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 27b5167d-7c61-3fd9-8108-66e050831343 | -8.9038 | -60.5962 | 2026-08-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 5558d186-c4a0-39de-b90c-ac812a105aca | -14.4739 | -45.6682 | 2026-08-17 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| eb5ca4f0-b23d-3ce0-82a1-23980c713cb6 | -8.5977 | -54.6948 | 2026-08-17 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 09ebb0c9-9b3a-3744-b649-0f33ef2f2e7e | -6.6014 | -58.9844 | 2026-08-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 17bb2929-1ef4-35d2-9b52-3f26c761082a | -6.1107 | -57.723 | 2026-08-17 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| deb21270-04b9-36eb-b49c-62d2c77418e4 | -6.1106 | -57.7425 | 2026-08-17 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 19102225-78ba-36fa-9f6b-bc42879654c5 | -6.6015 | -58.9651 | 2026-08-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 5108def4-0f1e-3835-905c-61fd118e664f | -6.6384 | -58.9636 | 2026-08-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 87b3db4d-347f-3338-ba07-3d0d09e41740 | -12.3565 | -50.8848 | 2026-08-17 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 0faf455f-2ccc-3841-bda9-161487aa92c1 | -8.9041 | -60.5577 | 2026-08-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |


[Clique aqui para ver as próximas entradas](README4.md)
