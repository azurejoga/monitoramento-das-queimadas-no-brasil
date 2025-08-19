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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24890553-c36d-3bdf-b766-94cfec986cef | -13.01604 | -56.82961 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f394ef20-526c-3130-8305-63ddacab0253 | -12.98339 | -56.84906 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad700fba-4449-3488-9d04-ffd38bbdb814 | -13.67332 | -44.22241 | 2025-08-19 04:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34bdf1e8-8e7d-3f4a-b0df-acbec0f58630 | -16.47645 | -45.09383 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7df6549a-0132-34f9-ac69-8d10a7164353 | -13.16115 | -54.93884 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e60d7f78-620f-31ef-9a9c-84aa2980d5d7 | -14.64438 | -54.90912 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3458add2-4b5a-307c-b3de-cf3b1f643444 | -16.80803 | -49.20483 | 2025-08-19 04:55:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec6f9eab-4ee1-352d-b2b8-87c032342d86 | -13.37453 | -54.40908 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 416ae5c9-96c4-3b67-9053-491cd8ed2c7b | -14.84933 | -48.04988 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c7b8b84-c5ef-3f12-aaad-55f24d7a53b9 | -13.25683 | -50.79942 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 51050d06-bf35-33ea-b0b2-9c51b358c2c4 | -14.30778 | -51.96688 | 2025-08-19 04:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efbdaebf-b4c6-3202-b956-676cf546eaf8 | -13.24593 | -50.79776 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 186efb26-00d7-3cab-8c32-bbab18e0c38a | -13.01821 | -56.83843 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 105e650a-dee8-3eec-b75f-08ca3286e95d | -12.98266 | -56.86225 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f50a1a1-5f77-3f37-96f8-4738a7f997b9 | -12.98625 | -56.8538 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d53b8844-ff01-373c-8733-5b01b3e703c2 | -12.97983 | -56.84845 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cad07014-b35e-3e69-85c9-7d7045469279 | -19.19963 | -46.8452 | 2025-08-19 04:55:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79c42234-5420-3924-b411-937100b38aa7 | -14.29889 | -57.76437 | 2025-08-19 04:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f0ed075-bd13-30ee-a082-834fadb4d59f | -13.00189 | -56.84816 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de536fad-b144-3b3c-9c0b-98704ad33d77 | -12.98269 | -56.85316 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c61ca6c6-4e5f-3033-88fa-28f6e9d17fa8 | -15.15785 | -48.78192 | 2025-08-19 04:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d232585a-24df-3d07-94b6-7e3599686e1f | -14.9642 | -54.78983 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f23bc1fc-84ec-35a9-9942-3a482f647bdd | -15.7436 | -46.61105 | 2025-08-19 04:55:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 447a08e4-40c3-3177-a6a7-7a004890b43b | -13.16958 | -54.92915 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 546aba5a-fb3a-34e2-9d82-80f979c3b48e | -17.81771 | -44.49187 | 2025-08-19 04:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a35172d6-d173-3bf2-b924-c3776eaf8084 | -13.13519 | -57.15792 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a95b407d-572c-3f55-888d-388c0186d132 | -15.02684 | -54.80395 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e9925a5-d27f-374a-961a-000c5c92a4ec | -13.16173 | -54.93523 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7cc5a723-6eda-3fa9-bc9c-8a0d06823b99 | -16.48153 | -45.09814 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdb1debd-3c51-3e73-87c5-2bb845c291cd | -14.87493 | -48.05523 | 2025-08-19 04:55:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bee0a58-e2bd-3412-8209-978dd6bef88e | -15.03454 | -54.81997 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e1d73d94-c53e-3666-98e8-9d7bfc81c84c | -13.59402 | -46.98669 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3619a370-1912-3794-b2e2-d18ba29d3f0e | -13.18142 | -46.88303 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d39eaf6-75a1-372a-98f8-89836361be8a | -12.99196 | -56.86334 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eda1971-cb63-34c1-bfc7-0ae9cf52d5ac | -15.35753 | -47.25934 | 2025-08-19 04:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3de38dc0-353a-3c9d-a244-d51121db4507 | -13.07998 | -49.33714 | 2025-08-19 04:55:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3f7cef9-1c90-382c-95d3-b2de03554251 | -19.81749 | -44.32478 | 2025-08-19 04:55:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eda8d61-e39a-3bbd-b5d4-4e1d8f2267d7 | -13.18678 | -54.95055 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d2b978-39f6-395c-8538-120bf7d87d22 | -14.87109 | -48.05031 | 2025-08-19 04:55:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 077ba52f-d60d-3a60-be66-19b879af0532 | -12.9841 | -56.84497 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 854641ea-8b1d-3f78-9adf-d415ade10e99 | -13.18517 | -46.87992 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64aee4fe-80d2-3d05-a053-21d86cae8b08 | -16.81347 | -49.36716 | 2025-08-19 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0b3e6bd-58de-316c-8205-f101495ea0a5 | -15.03901 | -54.81335 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efea148d-e479-36c6-8991-5dc3d42c44a2 | -16.62794 | -51.35853 | 2025-08-19 04:55:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 776c231b-62d0-3471-afcf-db07e1c60983 | -18.43127 | -49.16974 | 2025-08-19 04:55:00 | NPP-375D | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 651f849a-3510-3123-94a2-3edab242cc10 | -15.03844 | -54.81693 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 079aa7d4-6785-3676-a6f9-4594a090a612 | -13.17396 | -54.94471 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8687ed8-a6fa-3045-8480-8847062e6533 | -12.9854 | -56.84575 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 785e5b38-d67e-35d0-940c-84d205e0d21c | -10.44475 | -64.45972 | 2025-08-19 04:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6906be9e-f9aa-333d-89fd-0713bdc9e782 | -12.98404 | -56.85397 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f152530-b347-3420-a2d9-67541033b855 | -12.9884 | -56.86271 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52154ad5-f328-30c4-bfa4-b608d9720d54 | -13.17731 | -54.94527 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86510e70-6156-3214-9b25-d243f45c6a97 | -16.79641 | -50.09205 | 2025-08-19 04:55:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a01c26b9-f6c4-3038-ba55-17c28732b2a4 | -14.84382 | -48.05775 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c9df6a0-a56e-3e20-801b-1819c5ca266a | -17.33638 | -47.16394 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bc52b38-6191-3925-bd06-a2f0a66e230d | -16.30794 | -49.16774 | 2025-08-19 04:55:00 | NPP-375D | CAMPO LIMPO DE GOIÁS | GOIÁS | Brasil | 5204854 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba38f056-7fc0-33a9-9907-03ab40dd2109 | -13.1728 | -54.9519 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be672b90-7f53-31d1-8414-e7aa65b22419 | -13.17673 | -54.94887 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46e5fc36-2c98-3749-9953-767e43d2fe86 | -14.47918 | -53.04097 | 2025-08-19 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 628703f2-9c9d-32c2-90cf-3ba044da38e9 | -13.59287 | -46.99585 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a79030d9-fa04-3033-8254-5b5029a06495 | -12.9891 | -56.85857 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0bf6445-900a-3af6-a294-8da005f4be86 | -14.84803 | -48.05613 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0961d86e-f434-38dc-bf8d-1ed1859b011d | -16.71669 | -47.62112 | 2025-08-19 04:55:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f305f40e-d189-34ca-a7d1-18a3bc037bb7 | -12.97771 | -56.86079 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01477f28-b2bf-3439-9d8e-5ba6630a2174 | -13.59028 | -46.98886 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bc90a6e-5a48-3ed0-915f-c268d3b571eb | -13.1323 | -57.15301 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e22f208f-cab7-3d89-affc-e5f1e750c7b6 | -14.62542 | -54.92063 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a65f88a-d801-30b5-bdf8-052963e6684f | -14.86841 | -48.03632 | 2025-08-19 04:55:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12673737-8ad5-3bd0-9784-9b4765a699f8 | -14.98463 | -54.81166 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eae436ce-48e0-35d7-897e-ad5799023eae | -16.47605 | -45.09749 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d567d25-75cd-3fe4-b525-dfa9c502a1e9 | -13.00614 | -56.84471 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b934677e-b064-3e2f-942b-91d2e7874858 | -13.44209 | -56.85353 | 2025-08-19 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64aa59ad-789b-372d-b325-21a119c12ad1 | -16.79248 | -50.09134 | 2025-08-19 04:55:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b567746-7a81-39eb-ab49-9710bcebdc9a | -13.15735 | -54.9197 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96a15b38-78b9-35cb-87f5-f548d7359a07 | -13.16347 | -54.92442 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a72db2e1-a9a6-3b51-8829-0b8202a1afc2 | -16.62729 | -51.36309 | 2025-08-19 04:55:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 649f97f5-8126-3284-bcb2-9ddddda25d75 | -13.37396 | -54.41263 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a90b67f2-be5f-3902-a2db-0875826bed52 | -12.97913 | -56.85254 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd475f36-87f9-3c26-a2fb-95a14e721faa | -13.58725 | -47.00308 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d14b84f-fc13-3e86-b5d1-101247031abf | -14.96638 | -54.79755 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2451705-b8b5-30bc-a981-12efa8f88cef | -13.86809 | -45.55123 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86cadf14-1a75-3219-bfda-621c0eeccbb3 | -17.90644 | -44.42448 | 2025-08-19 04:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2a46933-75fc-33bf-80c5-b862798b0db5 | -16.81173 | -49.36822 | 2025-08-19 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7c78bf79-896b-3727-9d4b-11a6018e77ad | -10.43876 | -64.45861 | 2025-08-19 04:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aefef5a9-9397-35cb-8946-89c47a9d2c4d | -15.38371 | -53.91152 | 2025-08-19 04:55:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a762c51a-db36-3b96-ac50-f804586dd62b | -17.33569 | -47.16988 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa40af8c-ae6d-3b0e-9c12-a4374dce0969 | -13.00754 | -56.83651 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ebf52fb-0086-3873-90f7-9937e028ff26 | -13.14022 | -57.15007 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a1648b6-fe1d-3cb6-abdf-0f2aa1660fe3 | -19.29487 | -48.4321 | 2025-08-19 04:55:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab512d63-4f7c-38eb-93c9-90bab6c0caa3 | -13.16128 | -54.91665 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40672446-d847-3bc1-a5b0-b4dc40e41955 | -14.8475 | -48.06034 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e1e11d9-dfa2-3a0d-b5f4-8f7d094a04e5 | -13.37616 | -54.42029 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17fdb5ec-7441-3581-9344-f2a1dc60c44c | -15.03122 | -54.81943 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5ae0e7cb-e4fa-3f62-9856-db9532a1e526 | -13.16566 | -54.93219 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a51b399-e722-3bb2-aebd-485a54292993 | -13.37673 | -54.41673 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dde8fe5f-7c5b-3ba5-99b0-4c8c2a50c653 | -14.96971 | -54.79811 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08d88e60-37f6-329f-9b12-732d86e73631 | -13.58906 | -46.99804 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ba4d061-c57b-3448-a7fc-f619ec79f505 | -13.14305 | -57.1332 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 683ef77d-ab43-3fa9-b330-29ae4eb70612 | -14.98016 | -54.81826 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cd7eeb0-6b53-3dd9-8186-7b27edaf14e9 | -17.34121 | -47.16459 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README44.md)
