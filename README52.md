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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2de48bee-8e6f-3f29-8ca3-580540325f97 | -11.22246 | -55.07692 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe286359-370b-3c8a-925d-4912e153e13c | -10.90942 | -56.37146 | 2026-08-20 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23750de4-8554-3021-baa4-a34cb2c74696 | -11.20774 | -54.00451 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d834a121-8e2c-3804-b3cd-3eca17aef80e | -13.4108 | -54.36848 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e27d900-b683-3f2d-a987-da129eed7cb0 | -7.60979 | -60.95345 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81459402-5b23-3258-92e6-cc45914f545f | -12.79647 | -48.41915 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd294c67-8ec7-3484-99d3-1d209a366255 | -8.54268 | -54.72074 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 718bdda4-d4a6-36c4-aedb-9eb8876efe5f | -11.19285 | -54.00651 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8512e39d-d699-3431-8eee-de21ab1d8eb8 | -11.24277 | -54.82403 | 2026-08-20 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f16d2a8c-8268-375a-b3e8-e3b6b47d87ff | -9.05662 | -57.06728 | 2026-08-20 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87e0e0b2-767b-3c21-80df-73d0c7b86a6e | -6.7968 | -59.58023 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ebc67f4-4bd5-3a89-9177-9757bc58bba2 | -7.77143 | -61.13779 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29f1006a-cc5b-3b61-95ac-e261d20b5f6b | -11.39468 | -47.22232 | 2026-08-20 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6acb457d-aaab-3794-9013-673a7b5ec768 | -11.81257 | -56.59792 | 2026-08-20 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7bc7c9f-1822-335f-b496-6b75539328dc | -8.09342 | -51.66122 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a7f17f2-85bc-3e09-9110-83a0ed831fc6 | -8.54978 | -55.31932 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f7b69ea-31fb-3f76-90a3-00e02789b9d6 | -6.92459 | -59.3476 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4d877e35-93dd-34da-8c06-10a3bd405290 | -8.57781 | -54.74871 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5342f01e-29f7-332f-ad85-ed505ee31ead | -10.40104 | -61.20305 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 662efefa-01b0-3cb9-b834-9e8e018ecadc | -11.42317 | -54.31383 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 667ceddc-d2e8-3d11-ab65-74ccf8289d69 | -8.672 | -54.6541 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 6e15824d-006d-3605-9731-8697cf88a7b2 | -8.6645 | -54.58865 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b363b0e5-c497-38f0-9193-2c94430716b0 | -13.63473 | -51.77689 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 482fc7f1-7203-3599-af8f-476ac56a30fe | -10.37926 | -61.2143 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f0700f6-9d52-3452-b752-a666bdb78ca6 | -7.61287 | -60.95925 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e40d2450-0313-3b03-a5ae-a0ce94adb7fc | -12.76918 | -48.46247 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fa1ba07-4dd2-3996-9f5a-96ee6e143a7b | -8.56578 | -54.66027 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b53dd754-c7a9-3541-818d-6bdf9a4c1f09 | -6.77193 | -59.45538 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 203202fa-8847-31f3-ad73-52646597f16f | -7.44571 | -60.00925 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16c25f00-4822-3a13-abd6-37b0716dcca0 | -12.77478 | -48.45985 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d864e456-d187-3b90-b664-37e5646602fc | -9.39959 | -60.55346 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b16a5ecd-6d08-31cf-88c1-a36528fe35cf | -11.19702 | -54.00292 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a118baf4-5e4b-3c62-858d-76929804e938 | -10.93342 | -57.11502 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de89bf18-052c-3d64-9478-3fe52cb23f37 | -7.33848 | -55.67957 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dbe58b9-375c-3048-a173-cdaf343e7547 | -8.1888 | -54.99353 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96bfa78c-9af1-347b-ab39-db950948a1f3 | -7.41875 | -60.00935 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ceb2ff63-901e-38a6-a6f5-a68ed24572ef | -6.86819 | -59.02632 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c5a82d2-d5d0-3bbb-af57-eafa564f3b85 | -7.77288 | -61.1415 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93b6c51b-1139-3196-869f-968c83651d6a | -9.80148 | -46.64045 | 2026-08-20 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd269c45-3aaf-3797-b65f-7f4ba2b18edf | -6.7551 | -59.46606 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3541bd0-40a1-373a-86ae-2dfb706fcd3a | -9.17499 | -57.00704 | 2026-08-20 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e217bdf-3e14-3c2a-b49f-72e4c432d131 | -6.80418 | -59.58146 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 004c5d36-e6e5-3aee-8d87-c3e0d0f18185 | -7.47995 | -55.31556 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc70af8a-357b-3c3d-a2ce-8142e2971726 | -8.57397 | -54.77429 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd4ee9d0-e22d-37ea-a5ed-fe553f7a657e | -12.79608 | -48.42244 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19be508d-0876-358c-ac22-59aedabdb623 | -11.81141 | -44.8064 | 2026-08-20 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4480b533-68e7-30ac-b9bb-ba2679d8c076 | -8.2855 | -62.89528 | 2026-08-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 880b607c-4112-30c2-aebb-657254a2aab1 | -8.28994 | -62.89603 | 2026-08-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e1e25b8-183b-3b96-9585-b8a7af4a4691 | -12.00957 | -53.44217 | 2026-08-20 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1af7f277-a8a7-3f1b-9e14-b68f2ba25cc8 | -10.39165 | -61.21149 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4dddab0-4b4e-3212-ad24-fda16a0aeedf | -8.03072 | -51.79462 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4c20f96-debe-32f2-8528-1233466ca794 | -13.47721 | -51.44122 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06d90564-5e5d-3247-9f29-68c48487f2fe | -11.19524 | -54.01531 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db3da133-aa7c-39be-8104-63d2056517a6 | -8.57726 | -54.75238 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d05560cc-5576-3bc7-a6f4-9102005aa85c | -8.49182 | -54.8733 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56abe6a3-5fb8-33f4-87c9-69694953b262 | -8.68104 | -54.64039 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f011a44-0c6e-3a1f-b1a8-cf50d7c8e0a7 | -9.2204 | -60.81171 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea19c9a2-c0d4-36ee-94da-c7ac08f49609 | -13.44773 | -51.43285 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4f626bda-cc04-3750-9db8-aacd972ffa59 | -8.50987 | -54.89092 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 817ec7a2-1bae-3ea7-ab24-c116d6278f37 | -9.10524 | -60.93113 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 886a366d-1e32-3cf3-a71d-e9795856077a | -8.66575 | -54.64935 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f32fbab6-7198-3d37-ae23-d465e1e357f0 | -10.63534 | -51.61568 | 2026-08-20 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35185106-1079-3d58-a846-e395667a00f8 | -9.39628 | -60.59561 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64b947d8-948d-3eb4-8963-f9e2f6b9086d | -8.46913 | -57.65895 | 2026-08-20 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e29b7e7-c688-377d-905e-f8edca2a7b97 | -12.54059 | -54.75746 | 2026-08-20 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ecf5890-4bfc-3945-add0-800526aac712 | -7.3644 | -55.51264 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebd78ced-fe9a-3f40-b685-393d38317f4e | -9.98555 | -53.9346 | 2026-08-20 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b81e6661-8a5b-300f-94f3-a866a86eb76d | -11.20714 | -54.00864 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3b532e5-0043-3b7d-bd9a-96629c2e85a1 | -13.7383 | -51.87135 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0fd20c4-b70a-3ed7-873e-fdeb293941d6 | -9.22027 | -59.76834 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 742fb825-7bbb-3caa-b1a8-799ce8d47985 | -13.40339 | -54.38262 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cc195589-80e9-3363-9dfd-b0f4daaf9580 | -12.92074 | -52.81632 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96cd00fc-7afd-3a7a-8f37-96d511ed35bf | -10.48299 | -50.317 | 2026-08-20 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 25b379cb-6166-3b01-90fa-bace9cd3854f | -8.50305 | -54.86763 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c80203af-c586-3240-a939-8035ba6d04b4 | -12.13 | -57.2038 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f618fe8-df10-39fb-9b4f-362f06ef68b5 | -7.87751 | -63.76723 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4393f59-a712-3569-bc16-e70d1c5b8b5a | -9.39207 | -60.54884 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9dc3b3e-07d3-3daa-aad8-348273fc45d6 | -11.22189 | -55.08067 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e9aed4a-a5bf-30fa-bf84-864761053317 | -7.7957 | -61.18843 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1acca14b-37c1-317d-9e12-7567bca6a0bf | -7.37517 | -55.53189 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 583ca0ab-ec45-3198-a3ec-881c8c0400e7 | -12.76385 | -48.46286 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a584b36-bbcc-3f0c-9088-ef41ee1c0e20 | -13.44828 | -51.42871 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| aaa704bf-3a45-38ed-94a2-6faafd096208 | -7.82778 | -61.61372 | 2026-08-20 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1be9e0c-3caf-3b36-b2e0-8ff0667e6afd | -7.54934 | -55.59171 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46735ea5-2503-3f68-9f1c-84c422107a84 | -9.2073 | -59.77922 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 57d252d7-8e65-3560-9710-fe1260ec4a2b | -7.5316 | -55.57468 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4c95c95-2c82-3558-a1ef-383085c5ddd3 | -7.47941 | -55.31908 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9222e94f-a4e2-3041-ab1c-84bbd6b42016 | -7.53824 | -55.57571 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f5d7039-7b8c-3ae7-8561-33c7079f4b53 | -8.67992 | -54.64778 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08670f7f-d6ea-3652-8dc9-b33a2b91266c | -12.47936 | -54.17905 | 2026-08-20 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64154a70-e843-3040-8a07-c4319286c834 | -10.12374 | -52.11697 | 2026-08-20 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 461e4ad7-f696-3a52-b42a-55f10fb538b4 | -9.21234 | -59.77134 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5618faf9-197f-3861-8caf-7e8285753f99 | -11.1875 | -54.01837 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec3979bf-60ba-32be-a274-9912c959d8e6 | -7.60495 | -60.95797 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1312231-19b7-3773-a236-98fe6c1345ef | -8.10055 | -51.66737 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e2028de2-cf27-3813-bdf3-2c1a3f8e751b | -13.2519 | -51.64249 | 2026-08-20 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b85b0841-726d-3c83-9e80-344559c2f181 | -6.92389 | -59.35184 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8b638c83-4a32-3aeb-a9f0-70a594ec624f | -8.57377 | -54.72174 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95bd9d27-c25a-3ec7-b5e4-4ece10f64e42 | -8.66282 | -54.5998 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b762d282-05cd-36a5-9fd4-39866e7f3340 | -8.5802 | -54.77899 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README53.md)
