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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd04a3bb-6fdc-3094-ae83-3ecd0dcc6f92 | -11.01901 | -45.06868 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 310fe5a9-6cf1-3191-bb8a-1c455db9a9da | -13.17936 | -51.34153 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a2625538-95d4-351f-aadf-aaff028d2d08 | -13.30234 | -51.46221 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.2 |
| e0ece7a5-55a4-3b97-99bf-95081c038e38 | -13.19303 | -51.34188 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2d14acf3-24ca-31b0-a62b-5b200b609b2e | -15.60549 | -53.11807 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2740383c-56e2-328e-926d-08111c44e98a | -10.43448 | -50.45748 | 2026-08-26 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2b195c4-a3cd-33c1-995f-2fe16c789925 | -13.33933 | -48.23092 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f0f48fc-b499-361e-ae66-a69ed508ae2d | -12.08451 | -64.24921 | 2026-08-26 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55e957b6-e3ef-3625-a171-079c89aa2fa8 | -14.29021 | -51.12905 | 2026-08-26 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8edaba51-0f5b-3e44-b4bc-98a554502354 | -12.89834 | -59.91312 | 2026-08-26 04:53:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb568c51-b9a3-33b5-8a0d-5680bd272434 | -13.23641 | -51.3696 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7cf03904-74dc-3561-a513-46088f0f0f11 | -8.66115 | -62.84364 | 2026-08-26 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd6ba0ef-c445-34fc-8d78-c8431c1878ac | -9.13132 | -57.55817 | 2026-08-26 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f2d3967-9458-37c9-b812-c26370bb4191 | -14.39367 | -51.76273 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f9bf895-ea43-3488-ace2-da80b2fab967 | -12.02314 | -46.00974 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e8c04d79-3899-3c13-bef8-68cdf3848f33 | -12.6355 | -48.40785 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| def2172a-3131-3475-ad31-e27d7dd01fbe | -13.23997 | -51.37015 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 66fab492-e379-3e8b-9598-54202fe27091 | -13.28046 | -51.46307 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6eeda853-fe74-3c23-bdd3-218927d33ff9 | -14.34809 | -52.99802 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27cda2cf-27a3-317b-9060-123862201b02 | -13.25539 | -51.38935 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 697f807d-2c98-3edc-b226-448c7278aa77 | -16.17397 | -49.32752 | 2026-08-26 04:53:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3085ce4c-c73b-33d1-b1be-60b79024f99f | -11.55278 | -46.97748 | 2026-08-26 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09c6ca67-f652-3b95-b437-9d9f4001657f | -13.36066 | -48.23523 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68a1e8e0-ccf2-3e52-9147-302fa70b60b7 | -9.46858 | -56.90422 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 983f3250-7ce4-3846-a323-3f8263456079 | -10.43686 | -61.21973 | 2026-08-26 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33760bd1-632f-35a2-98a6-f949e2b3777f | -9.6791 | -55.09138 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0d86f09-0038-3d01-a1db-12ee16b2ffd9 | -9.97116 | -53.96874 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 947d03d4-18ed-31be-813f-85411b166225 | -13.25124 | -51.39294 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a5e751e1-f749-3741-b86c-72dccdbaf033 | -13.27777 | -51.45997 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0ee598ee-32c8-3765-b7e9-fa00a6051ab5 | -13.33752 | -48.21133 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 007d91b1-753d-3d1e-959c-83d1b615d930 | -13.26251 | -51.39044 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| ade973b6-6dda-32ad-8c7d-228450054d0c | -14.79458 | -48.79643 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77b40468-517c-3ad1-885c-f94ef6fab64c | -13.85737 | -54.0753 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 342f498b-ef46-3cbe-874b-04afed8d9317 | -13.22929 | -51.36852 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 436f797f-5c0f-372a-9e7a-8540fec8acf3 | -9.67735 | -55.09515 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2087c67a-12d8-3cf5-9722-ad8f4a60d656 | -12.7662 | -46.4508 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f43782d5-c7a0-3aa4-b708-5524a6e0448f | -13.33861 | -48.20299 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d1269f5-6d8e-32c4-8134-2b0a845366d9 | -10.5645 | -50.4362 | 2026-08-26 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cf98143-03a7-3452-af26-79a70fdd6061 | -8.82622 | -62.33731 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d9df9bb-7cfb-3bef-aa60-a56478f906ac | -9.06641 | -60.43575 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e172e984-d146-36ae-8b29-9e7588179ab0 | -13.33654 | -48.21886 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 672aa7b9-f3a1-301f-bac2-4817a2ae3cf2 | -13.41828 | -57.07356 | 2026-08-26 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22d26e09-9f7f-37b8-be6c-d77753f3f404 | -8.81691 | -62.32889 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 50987c26-9a4b-3ee5-ab5e-c39d0ba07c09 | -14.58613 | -52.02971 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4cd60cde-f6ba-33e6-b0c5-3f75a831a8ac | -13.36115 | -48.23153 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bcc8424-0eca-3a27-9fb3-f9a21d3e31a7 | -14.29939 | -51.11705 | 2026-08-26 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a2b3008-bee9-39da-8f4a-365740b96933 | -13.37301 | -48.20815 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e47003e-8789-325c-a5e8-f26a050ca425 | -13.33505 | -48.2302 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e3758ee-809c-3356-b239-c8e8eb4e14a6 | -12.17618 | -50.60841 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| eebf4a13-bb04-3f42-bbd8-421800ca0bff | -12.68587 | -48.41568 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 92c98670-64d6-371c-be8f-2c48bedfbafe | -11.19032 | -54.00084 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f71c0e95-e068-36cc-9c4e-c2b8be027f33 | -14.36222 | -52.9806 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aca296f8-5787-315c-8aab-4f15189e7038 | -12.7541 | -46.46987 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b18e726-4457-3ceb-8b22-c176f1f30498 | -12.63491 | -48.41239 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d77a27fa-bdca-3d59-a91d-3c9739770950 | -12.72981 | -48.37919 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52b4342a-017d-3ac9-9b4e-2a1732e2e523 | -11.4857 | -45.09299 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 161264e9-1a8c-39cf-9e5f-58149e522b28 | -12.73817 | -46.48102 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9089a57c-e080-3d84-8a87-eb69f86a99b3 | -13.19127 | -51.35429 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4c40fe7-113f-3c8d-8989-f31f949cff0a | -15.59869 | -53.11699 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53367e0e-b1d1-31c8-ada5-2c7986f171ad | -14.39721 | -51.76327 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8317c31-b29e-3ab2-880f-08a235d9f991 | -13.25955 | -51.38578 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a47f08c1-d4c0-3b99-a6bf-7febced923a2 | -10.76857 | -54.02258 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89db90a7-8499-3ac4-ba24-b2a49cac1e0b | -12.68635 | -48.41216 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b9ed8eaa-6ccd-3a91-8e09-a73af04ad788 | -9.18277 | -59.38451 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8f9c76b-b395-3787-baa7-675850bcc4f9 | -9.47741 | -56.91916 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4f3ffd2-acae-364b-bec4-617f5d06a2d6 | -9.48178 | -56.9154 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b2c8c2a-7d05-3cba-bff8-1f33e6b53a98 | -13.21386 | -51.37461 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6bf5519-e5a2-3e4d-8875-af3b899428d2 | -11.1559 | -54.00251 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6305426-82f5-38f9-967a-2b39f5c53dcb | -11.16992 | -54.00116 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a68ff3d9-8742-3bb3-8372-9d79df75c7be | -12.63131 | -48.40706 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de594d67-f371-350e-aaee-48536c50deee | -12.03082 | -46.02781 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 39d05f39-0a7e-3102-b62a-0944ccaca231 | -11.49129 | -45.09042 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f5b08f5-23de-39e5-9526-3c5d1a81c344 | -14.43964 | -53.08789 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9a9d07e-a5c6-3ebf-abd6-72418ccafae1 | -14.55469 | -52.31659 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f9c84c9-c0b5-32c8-aa35-d9a9bb72853a | -13.86395 | -54.03276 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50db38a4-eca1-314d-a325-6983d266edc6 | -10.98355 | -43.70984 | 2026-08-26 04:53:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df6efcc1-ec56-38aa-948f-f4372d6fe3a7 | -11.75947 | -54.53312 | 2026-08-26 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39dbbc09-17bb-3c99-8b58-17386d196bbc | -10.07008 | -60.50141 | 2026-08-26 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d8177c0-13bc-3c6b-a165-55ede1a3d75c | -10.76526 | -54.02205 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 37f9e86b-1d87-3798-a5cf-1d111e95ab17 | -9.99213 | -53.96492 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bc22afe-6411-3a90-81ce-d6c4a1af234f | -14.12863 | -52.35244 | 2026-08-26 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ddc3bfb-9fba-3341-b94d-b92b676284ef | -15.60321 | -53.10999 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84881c41-3653-30d8-8b74-23b04c022f52 | -8.67596 | -62.94581 | 2026-08-26 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e636d39-e245-37e6-8ca8-67be79f72aa9 | -13.24694 | -51.52208 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| eb609422-8e46-3b92-9408-a17d9471b1c9 | -12.76062 | -46.4585 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34a23282-005e-37b4-8272-d52bbb344e88 | -14.58262 | -52.02916 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0d38d911-1c17-39db-8e1e-0aead790d95e | -9.46786 | -56.9086 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01300bb7-3fa9-37a4-b3f5-a6e772aaf894 | -9.67631 | -55.07991 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4de2c1f4-0b3e-3daf-b25e-9689072232ad | -11.76279 | -54.53365 | 2026-08-26 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1141a046-a347-3dc8-868c-48ee550014f0 | -13.34357 | -48.19854 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac55cd45-c0e9-3546-b69e-406a74d14059 | -12.69481 | -48.41298 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 836590bf-3f66-314e-a6f4-06201d0952c6 | -11.7462 | -54.53097 | 2026-08-26 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f74d2279-91a2-3942-9aef-c314e14bc12c | -9.67338 | -55.0983 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9752860-7551-334a-ac52-67be86ba4059 | -12.7535 | -46.47472 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 116ae83b-75bc-3fcd-b62c-13975fc42aa6 | -10.75091 | -54.0054 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e109177a-c4d5-3a46-a4f8-d5e487e6d0e4 | -12.08481 | -64.23637 | 2026-08-26 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d0346b6-c474-3f91-b8db-38889213afda | -13.24575 | -51.53022 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e2ac90b6-4882-32c7-86aa-58d9695af9be | -11.42501 | -44.54278 | 2026-08-26 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 532d5acf-747f-3d9c-886a-21a7ba55b201 | -11.28181 | -47.07615 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0fb0c1d4-8cb8-3c6f-999a-98949dff38f3 | -13.29111 | -51.46468 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README43.md)
