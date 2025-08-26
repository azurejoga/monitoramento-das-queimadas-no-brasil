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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52dc2fe8-a17b-3fc5-b08c-7b426e2fa9f5 | -9.15167 | -59.55322 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 636c58cd-e387-32f7-b383-aa2a73396541 | -10.60921 | -54.89478 | 2025-08-26 04:23:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05a812fa-6f71-3a8e-aecb-61abb6ee5d5b | -13.41405 | -46.92295 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f3c5abc-b7d5-36e5-b176-a01e087cff8f | -11.52934 | -52.13287 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e34a76cd-23d7-3f2a-b956-d639dbace48d | -13.64449 | -45.70539 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a73cdb0-1298-31ee-983d-84c782ffa39a | -9.17651 | -59.54252 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ffe02258-9b43-3892-aa2e-8f848eef6c85 | -12.75538 | -48.13381 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4678bd41-4fb7-37c1-a3e1-d3dee64fc44a | -12.7748 | -48.11209 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c760ea8-5815-31a3-8500-d295200f9d0e | -15.08675 | -48.54796 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e64f2c6-6706-31a3-9bb2-af6a265c7a67 | -14.35993 | -51.91542 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c2663b5c-9128-33cd-99f9-90bc15dab986 | -13.48448 | -46.86868 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ca19d63-caeb-398d-be21-d877c536256e | -13.43291 | -46.93358 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1ae955f-ea88-3e41-b3d7-ff3a3728bd02 | -13.49887 | -46.88585 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e7dc14b-6932-3168-b9e1-548fd57a9610 | -11.56196 | -52.10326 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b277f9b6-6194-3da5-9637-3c6b7d6e127e | -9.1671 | -59.51223 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ea09f43d-a4d8-3e95-af2d-d15f14de3b32 | -15.05656 | -48.70587 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bda672b-b831-3574-9f75-29ceb8f58a8d | -12.93309 | -46.31762 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f18da9e9-4c44-3024-ac04-bc0ae31786c6 | -11.30364 | -55.11114 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 04c92ab5-180b-326b-85ac-77d76b4b5bc5 | -11.30038 | -55.10816 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d4d4b626-9a8e-3535-bfbc-8bd5f371c205 | -12.66214 | -47.86839 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ceab894-4553-3cb5-9671-1a12b810a91d | -13.41345 | -46.92661 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 104a4a25-d375-3582-b487-71c355dc0b19 | -13.05327 | -46.30812 | 2025-08-26 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c504d7ef-22b4-38e0-a4ee-db9b13ceceaf | -13.71893 | -52.01204 | 2025-08-26 04:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06a1e179-2146-3754-85e0-5e3d23836626 | -13.51057 | -46.8912 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91f866f4-3979-3639-a80a-37a0e5923c9d | -11.63344 | -46.40625 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28cd54ca-ff01-3e47-94cc-333a7b72e659 | -12.73275 | -48.14175 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 892dac32-549c-37f9-8d47-b50d7f794e4a | -15.64136 | -52.72915 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 782e18c1-8daf-302a-bf52-d3749514ca6e | -13.42511 | -47.02458 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1eef65f-ef00-3959-a46e-1b0ad38c45ac | -15.08541 | -48.55589 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10ab3a75-188a-3cd2-afdf-7f8edc2a01a0 | -9.17871 | -59.45337 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ec8981fd-db93-3e40-bc1a-3c2f08fa8753 | -12.77135 | -48.1115 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0d8b722-00d4-371f-bd1b-b1aefc585a50 | -11.5632 | -52.12136 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e142dfe-a0f9-3bfa-af6e-69bb53b098e0 | -13.61075 | -48.15886 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a3050937-ec23-3761-84ac-88d1aecf733f | -15.06838 | -48.72017 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b77f61f-fbea-3539-b371-39b078527320 | -14.45115 | -53.35307 | 2025-08-26 04:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ff766e2-7bd7-3892-820b-9af4921eb08d | -13.84039 | -46.69725 | 2025-08-26 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da92967b-293a-3627-8abc-dc7e63d462ee | -14.71753 | -45.38118 | 2025-08-26 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 237d5e2f-2da6-314a-be01-f8721190ecda | -13.8304 | -46.69558 | 2025-08-26 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c04e8c4-77c6-30f5-99d7-9d13e4ce27eb | -14.76136 | -59.70695 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1d128e7-02f4-3ed7-9224-435d3baf0a13 | -9.64362 | -59.63833 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 18144c6f-a836-335a-9551-43061472a5f2 | -13.0566 | -46.30867 | 2025-08-26 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ebefa1b-092e-3875-af0e-31187eef6eb6 | -10.38847 | -57.6979 | 2025-08-26 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 68ccafd3-0168-376d-91c1-68829d7957a9 | -12.76933 | -48.12347 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c42d1e8-ca2c-3bbd-bdab-ae76fa44d40e | -12.37614 | -46.55749 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bec5556-6a8c-3187-abd5-f9377a81226b | -9.18738 | -59.44746 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0f7a81a4-4855-3b30-b2d2-2833d734ef57 | -11.52071 | -52.13296 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| bf0eee94-ba74-33de-b8bb-f8808c0f80d9 | -12.74531 | -48.15179 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4acebcc6-8435-3702-895b-19356f079105 | -13.59009 | -48.19852 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 199fd284-46d3-3c10-ad56-91aca5d8ba24 | -12.78117 | -48.13767 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bd8aef90-dc09-332b-85fd-c0c938b00d60 | -13.44637 | -47.02049 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04581fb6-a55a-39c6-8da6-1053a39d51a1 | -15.05441 | -48.69752 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 408c2748-bebc-3df4-99ba-3002a6b7e3d6 | -13.46713 | -46.99819 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 717e3e8e-50ea-3408-a573-f86d97930069 | -13.43016 | -46.92937 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee17650e-8c99-34d6-a524-ae1b43899cf3 | -15.13963 | -48.6769 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4485319e-91da-3268-83d6-d9003a06136e | -15.17818 | -48.18937 | 2025-08-26 04:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91bc108e-c2b1-3f71-b22c-a8dc4c26cb1a | -17.81608 | -42.83033 | 2025-08-26 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 740c0a07-f6a0-3d76-a181-11604d0b9e2c | -12.75983 | -48.10659 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 532a92e3-13a0-3f95-9eb4-32e7deb6b11f | -11.55804 | -52.12481 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5926fb51-accd-3bdd-b7ab-e73402e2366d | -12.78052 | -48.14151 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8943269-75d8-3713-89db-ac9487a23ae1 | -13.01184 | -56.89275 | 2025-08-26 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 950fe833-e234-30fe-826f-ace52cdca830 | -13.41083 | -46.90038 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2503e23a-a775-3a38-879a-509bef5bbee5 | -14.79143 | -47.92717 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc75bd3b-ad97-3bdf-84f4-b90f6b1f2341 | -9.19121 | -59.5072 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a16be55a-4640-3305-8898-6e1c59ec8054 | -12.94848 | -46.32353 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d638309d-1eeb-3036-b285-6e5643887637 | -13.44027 | -47.01574 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 041b8a5e-f6db-32f7-9e37-6fb226710111 | -11.56398 | -52.11703 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 142be5af-c9b2-324d-b4cb-f6e2ba2db74f | -12.70489 | -47.88266 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ea9fb63-921c-3c9e-81e4-a06ef14ce058 | -15.0656 | -48.71556 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5df5613-c3e5-33ec-8223-ebcddf09ca47 | -13.05271 | -46.31166 | 2025-08-26 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00e8e940-b791-3978-8284-e3334eef82f7 | -13.44143 | -47.00854 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 893a4a9d-0ccf-3152-8c9a-cd9bb29df2e5 | -13.48749 | -47.01272 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c70fde7-ef73-3584-8cdc-6e9ee57377f1 | -12.72959 | -48.1609 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 612358ba-f3c1-3125-ae37-24a15b8fdc4c | -12.4433 | -48.71225 | 2025-08-26 04:23:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99cbfea6-928c-3d91-8290-d7ebdc7bc281 | -14.26557 | -48.02346 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15627e5a-6382-313c-9353-e65f0fc83a6d | -12.48614 | -47.2366 | 2025-08-26 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d83c346-aba9-33a6-b405-d571b7573891 | -9.16417 | -59.5271 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f3c28e01-70d7-36fe-ba68-997029fb46a5 | -11.55757 | -52.10247 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8986b1c-407f-3e0c-9a13-41ab2df698fb | -10.64731 | -51.59297 | 2025-08-26 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80eb2593-767c-3710-8146-4bcb797215d5 | -12.48336 | -47.23238 | 2025-08-26 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 073b9283-644d-391a-bbce-da90188e403d | -15.05588 | -48.70988 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e584cc6a-31dd-342d-ad96-0953c89e34aa | -15.64985 | -52.73085 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6876087-1cc8-3cc9-92ef-059611989ff0 | -11.56555 | -52.10839 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c07dafb4-6e54-3058-aa07-6d31d67a5d65 | -14.4038 | -53.28053 | 2025-08-26 04:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ddb4cabb-9093-3254-a216-264edaccabb5 | -13.59697 | -48.1997 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4276def0-3b89-35a9-bd16-f8caf36fb2fa | -15.68457 | -48.23632 | 2025-08-26 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c22057d-0f03-3a68-8ff5-614bf8556cb9 | -11.62559 | -46.21955 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 315eb902-a3ab-38a3-bd71-b1337057be76 | -12.42199 | -43.4911 | 2025-08-26 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab5196ac-3f3b-36d7-9ab5-ce92910d196f | -12.78181 | -48.13382 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60291809-1e85-36f9-b472-f50d9aa05a78 | -13.5171 | -46.91444 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6907936-e17d-3475-8643-9f5262d2892e | -13.46665 | -46.87304 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7c326302-4e04-34da-938d-60087fdfdc72 | -13.44085 | -47.01215 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b8a7a0b-2f67-38c2-a42e-28db1c4eb3b0 | -13.60887 | -48.17033 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8be5fbe6-1db5-3e97-ac2a-3349e3cff676 | -13.82707 | -46.69503 | 2025-08-26 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74f0e738-cbf6-35f5-8204-720ea4d00f91 | -11.53541 | -52.12674 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dabee43b-6f8e-34d5-91d6-426ab9d8a0a2 | -13.51448 | -46.88821 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fe0c8e2-0cc7-36df-af28-0ea8870c110c | -13.64699 | -49.00608 | 2025-08-26 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15abcaeb-5392-331c-bd03-3b35b95265ea | -15.11592 | -48.6487 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b0f29ff-24e0-3068-9c2b-4a0318331cad | -12.39211 | -45.00364 | 2025-08-26 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08c4e7c1-4a34-35be-9b13-1a2d4184b8f3 | -14.72089 | -45.38173 | 2025-08-26 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8298cbd-8130-321c-a3ba-b0d2a8daadeb | -13.5139 | -46.89176 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README50.md)
