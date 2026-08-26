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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 041e4fe8-7986-368a-8dfe-a9725156eb55 | -12.76195 | -46.45182 | 2026-08-26 05:29:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 089ab8ec-ad56-3f5d-8a81-46aa78ffe1eb | -11.19824 | -55.07889 | 2026-08-26 05:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6283ec17-a486-3e7e-bda9-2fea07b93109 | -9.20024 | -59.57486 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2b86b8b-e22c-3218-9e05-8de784836ce7 | -12.17329 | -50.60582 | 2026-08-26 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16fd8f74-32a7-3454-91a0-1fddf385e121 | -10.76513 | -54.02057 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c9b17f5-4be4-33c3-b2da-dde3cc149acf | -13.86378 | -54.03027 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc14a4ef-6a80-3fc4-ac8c-6781547a241e | -10.77208 | -54.03418 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2029c94e-588a-3c25-bf26-d378dd2c1e7e | -13.194 | -51.34088 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| efe2e453-cabf-3c5e-9029-02b9eeb00b05 | -9.9699 | -53.94665 | 2026-08-26 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49f48324-ee9a-31dc-afdd-6e2e8463fadc | -12.02813 | -46.01905 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 569b1d70-5fa1-3d3e-abc6-3a70d20fd317 | -13.246 | -51.51554 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d37e9c69-3e7f-3929-854e-a580afdc8235 | -8.64628 | -62.8935 | 2026-08-26 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51f0d3be-ad36-3054-9768-d264f005535a | -13.37238 | -48.21676 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75aba2b9-baa6-3268-b9a0-a364416dc568 | -14.12675 | -52.3559 | 2026-08-26 05:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6153284e-6e1b-3bf7-af5d-1caea25598b4 | -13.85162 | -54.04035 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5acd19e6-f943-3c20-a614-2e2a6ad0b16b | -13.24584 | -51.3816 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 04b6d443-78d9-33db-a2bd-8adad32b5f16 | -10.99534 | -51.15643 | 2026-08-26 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19a23539-aa32-3544-9b66-28a6938b4997 | -9.18973 | -59.57676 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d749e72b-59e2-3633-9729-10117aa9f865 | -13.19484 | -51.33402 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 38fc7cd3-31f9-34d3-9bd9-856756479bac | -10.649 | -57.24803 | 2026-08-26 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cdfab18a-482c-39e3-8411-573ab56aa53d | -12.75435 | -46.46919 | 2026-08-26 05:29:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2c913cc-8c24-35f5-8a97-d2cc1d0821ca | -13.23378 | -51.5275 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57ce5e59-60a4-3dd9-8436-e4db759f46a8 | -12.76294 | -46.45686 | 2026-08-26 05:29:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6a4dffb-d78f-3527-8299-ab832837e452 | -9.20301 | -59.57889 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b5543ef-80d9-38c3-a6bb-e546025bbb05 | -13.22942 | -51.36284 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 0aad362d-2b99-3a79-8309-12cf5d1aaf49 | -13.24357 | -51.53558 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1714c123-6f01-3199-b4ed-274df0ec0795 | -9.39166 | -55.97745 | 2026-08-26 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 285a65e0-f566-36c8-abb9-d90ff41f04e0 | -13.25737 | -51.37618 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 627d9cf6-57c9-3143-82e0-b7e80018562c | -9.65718 | -55.07108 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a8bcbda-3ff2-333d-b18a-4b17f41993f7 | -13.60521 | -49.01329 | 2026-08-26 05:29:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5dd75ac8-5916-3075-8e82-527e1da38c12 | -10.76474 | -53.99088 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 88c9de34-6eae-3ad6-b512-14412bfdb9dd | -10.06801 | -60.5015 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9195a3b5-b7d9-3a0c-94a0-bb58d4da59c8 | -13.23392 | -51.37036 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 28ed1916-4439-346b-a1a8-34277a9f83cf | -13.26889 | -51.4605 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d8a1cbda-a944-3c04-b586-a5cdc475d39c | -12.89752 | -59.92251 | 2026-08-26 05:29:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2444820-23df-3e00-9bec-b5ba06508cb5 | -9.28065 | -60.89896 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2821602e-1311-3dc4-8dfe-b01fefb0bce0 | -11.76838 | -54.52999 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d83e9abc-681a-3cf8-bed0-53bf68ac9f8e | -10.98621 | -60.79267 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df411d95-196e-369e-a733-fcc31395a9d7 | -13.23512 | -51.38019 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5984d4d1-aa98-36f3-9586-444e2b5336ad | -13.29146 | -51.45311 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e182827d-b771-3593-9796-70c4b2caee81 | -13.21827 | -51.36488 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| af976dd5-aff0-3753-a3fa-58ecbad5438f | -10.4288 | -61.21837 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5045747b-512e-38b8-bed7-ae51867fa6b1 | -9.48175 | -63.28041 | 2026-08-26 05:29:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c19e72c-51c9-34cf-bf0d-554b309b01b1 | -13.16634 | -51.34424 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0241b8c9-f513-3246-990c-0c0cfeb7dfba | -9.27093 | -56.90758 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd155a97-eb17-35c8-9d97-7e067f08b282 | -13.2417 | -51.37065 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 5068d124-8993-312d-9303-3df7e2d7d222 | -13.18863 | -51.34018 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| cf0e20a0-72ad-3815-a296-2ff02837ced5 | -14.7917 | -48.80534 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fca4370d-1125-35e4-a1d8-3739be22ed1f | -12.68234 | -48.41287 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d3133b28-dbb7-3c65-a698-c71e23f8a557 | -10.65256 | -57.24857 | 2026-08-26 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7ddb95e-23dc-397f-9d6b-da3cd76e07fe | -12.03405 | -46.04012 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 61859c89-d562-3193-b9ec-450b2720311d | -12.76229 | -46.46305 | 2026-08-26 05:29:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bc9b7d55-5bf6-31ec-a72a-f3b560676e9b | -13.23219 | -51.359 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 36.4 |
| a67a7382-da12-32b5-bc01-057fc4244f90 | -9.48461 | -56.92201 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f352ac2f-751e-3121-8397-a1ef46c0d63f | -9.09493 | -59.40412 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e10e6aab-b5dd-391d-a798-d8fede643f1e | -10.76422 | -53.98733 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2bff9c88-1b71-3acb-9fe5-5c229e311bb8 | -9.98009 | -48.32815 | 2026-08-26 05:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5107593-740b-37be-a5a9-2ec7145fd41c | -14.35987 | -51.75277 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 243585d2-fa62-3bc4-b3b2-79d3b285e741 | -13.24594 | -51.36148 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 19d167ea-d6d1-3ed9-8946-e5823f54673d | -10.64545 | -57.2475 | 2026-08-26 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 486684c0-40f0-3e5c-9147-d587f519ce54 | -13.22363 | -51.36558 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cefd7010-a6ae-329f-bc25-624b3718c38c | -13.2619 | -51.38371 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 2e6aef3e-5ce7-38f7-ba4a-c19b209ed9b0 | -9.1364 | -57.58245 | 2026-08-26 05:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 424d5587-501c-3127-8460-d35c263b6ba1 | -9.5727 | -49.26129 | 2026-08-26 05:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6836174-d7c8-39d4-aef6-401cc8b548f0 | -9.39244 | -60.57663 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15f81652-be34-3526-85cc-e03bc3b6b274 | -9.13243 | -57.56223 | 2026-08-26 05:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ee3b2d7-5af0-32fa-8a6e-ad01624d3182 | -13.24956 | -51.39594 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aecf02a8-0354-3f3d-b90a-72bc9a88be4f | -10.56289 | -50.43905 | 2026-08-26 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b70504e-4574-387c-a4f2-863c14d67824 | -10.7598 | -54.0179 | 2026-08-26 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d1eee8c3-2175-3bb3-a3b9-0a79ebeeb0c3 | -6.2676 | -53.3768 | 2026-08-26 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ce7788cc-439b-394b-b680-3e36f9ee5d47 | -12.0354 | -46.0374 | 2026-08-26 05:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 397.7 |
| 6d7cc0e9-201f-3750-84f2-1d3a8f141226 | -13.19 | -51.3593 | 2026-08-26 05:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 566e370c-7a4d-3217-969f-7900bb47955b | -7.5288 | -61.4015 | 2026-08-26 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 4f6fdaaa-201f-3879-867f-6a5d03f1765d | -12.0362 | -45.9917 | 2026-08-26 05:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 86c2884d-d92f-3134-b096-717d3ce6128d | -7.5104 | -61.3832 | 2026-08-26 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| be319274-cb0e-3663-8c83-3cbd68ce53e6 | -12.6836 | -48.4116 | 2026-08-26 05:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 49364f12-6cf2-3e98-84f3-799f4dfe9c0f | -12.0166 | -46.0173 | 2026-08-26 05:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 10a9872e-9518-3f6d-bc78-48208ce1dc7d | -6.6409 | -58.5181 | 2026-08-26 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 51c63f12-42ae-310a-b77a-bc10f1747d2c | -10.7596 | -54.0384 | 2026-08-26 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 9cd12694-aad7-33a4-b866-6177d5ccfd0e | -13.1711 | -51.3404 | 2026-08-26 05:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e1e31595-173a-3a84-917c-2b5d1dc1e932 | -13.2842 | -51.4541 | 2026-08-26 05:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| afd13bdf-c2d8-302e-a64d-4eeae1238fb2 | -13.3034 | -51.4517 | 2026-08-26 05:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 8e823e4e-f101-3380-af54-0d1ce1245859 | -13.1903 | -51.338 | 2026-08-26 05:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 3b33ec3f-781e-38d3-8536-51a5450dbbac | -13.1906 | -51.3166 | 2026-08-26 05:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 416ca854-e067-395a-820e-07c4dd91475f | -10.7784 | -54.0368 | 2026-08-26 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5016a40f-567c-336a-b194-b06485430c41 | -13.2839 | -51.4755 | 2026-08-26 05:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3abe6c81-32f6-381d-9eb9-239cf0e74932 | -13.2448 | -51.5229 | 2026-08-26 05:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 87d8bfdf-b6af-3f55-ab67-1eaafc90f84e | -12.0358 | -46.0146 | 2026-08-26 05:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 607.0 |
| 322f5dc7-d14f-38c7-8f4e-a9561e534097 | -7.5289 | -61.3825 | 2026-08-26 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 58db9142-374b-3747-9807-97f3bef417bc | -6.6595 | -58.498 | 2026-08-26 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 555247d7-74dd-3295-8029-cae9999d6c5f | -12.6644 | -48.4142 | 2026-08-26 05:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| fec0bfee-c48d-3368-b203-bec39f8f3b82 | -12.0162 | -46.0402 | 2026-08-26 05:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 388a632f-f606-3978-81f7-d84be1c113af | -6.641 | -58.4987 | 2026-08-26 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 42392680-aa84-3273-a31c-01a1cfaa87b9 | -9.6024 | -55.1078 | 2026-08-26 05:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 0de4a185-2c12-321b-ba35-c2f1b423a4cc | -15.56572 | -53.14069 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1a376fb-4b04-3252-b140-389c57b3d571 | -15.60945 | -53.11975 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0557a269-43d5-32a4-85ae-5bc4f360e60a | -16.08321 | -57.65472 | 2026-08-26 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 57362548-c373-318b-888f-587a5d0157b8 | -15.60094 | -53.1073 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9285fe3-d26f-3a30-8731-2c739e57c8c2 | -15.68826 | -53.89553 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 914ed20a-e5bd-3fe4-95ae-75cc1353905c | -15.6853 | -53.89622 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README66.md)
