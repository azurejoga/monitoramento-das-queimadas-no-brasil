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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6393fa0e-de2f-3773-9980-e5f11b47e3e6 | -19.72615 | -48.97792 | 2025-08-25 04:44:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a5e3fc1-2649-32e7-a749-df841741611d | -14.91203 | -45.54608 | 2025-08-25 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e85ed1a0-3f3a-3c30-b369-57ab1efcbbbd | -15.04647 | -48.67167 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b215661-d774-33e2-b3f6-25d5526d4a23 | -14.71978 | -55.9325 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90c59b06-b1fe-32d9-b12c-ad5208216e29 | -20.34972 | -46.72072 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cc04a21-f090-301b-b476-5e8363b52c6c | -14.11349 | -53.99745 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b6c60d2-4506-3f4c-b67f-748c18a4133d | -14.10636 | -53.99622 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61c2b0cc-e2aa-3ede-92d6-977a92ef9e39 | -15.08058 | -48.68534 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd878aee-d024-3f41-ae86-45589c6752e6 | -15.18055 | -48.19997 | 2025-08-25 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bf86167-0008-3c91-a8d2-0c7968451062 | -15.13684 | -59.59444 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1200db4c-732e-37f5-a56d-3140f05a9d2b | -15.98645 | -48.06955 | 2025-08-25 04:44:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28b11326-9def-3448-aa64-298ad53052f2 | -14.8169 | -47.91417 | 2025-08-25 04:44:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff8dad58-b646-36fa-bf29-ec0d0de09ee7 | -14.47945 | -52.06575 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d20c3709-6c87-31ab-8a20-e93de486aa55 | -21.63173 | -44.02407 | 2025-08-25 04:44:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e2bc3147-02ca-3478-824a-9215f511919e | -20.29777 | -47.17865 | 2025-08-25 04:44:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45d91878-89dc-3e18-998a-4cf5b01c7534 | -14.4378 | -56.46624 | 2025-08-25 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f26dd3b-6245-3d9c-8278-1275baf42eec | -19.35019 | -46.15104 | 2025-08-25 04:44:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 621559b2-0f87-3e38-ab78-b5532d65ef06 | -15.07887 | -48.54776 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10131b5c-ae0e-3ce5-beed-776697394e11 | -15.0545 | -48.51527 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1f4d1ad-8e5e-3d55-85e1-c1e80bd13c16 | -16.6824 | -49.1636 | 2025-08-25 04:44:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c85084ce-50aa-3f8c-befb-6046c122dd86 | -14.42903 | -56.46818 | 2025-08-25 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a806bdc-8d4a-368c-9998-6e12890a5892 | -12.85627 | -60.16233 | 2025-08-25 04:44:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92f78841-7a84-372a-a4f3-6a785ab1b80d | -13.00644 | -56.88235 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7ba87a9-d3ba-357b-b166-a1fb5f6875cf | -17.92847 | -46.07122 | 2025-08-25 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d99b1ce5-ff35-3a11-bd5d-e8f8b1216bb6 | -13.00426 | -56.89455 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8ed13bd-39fc-38be-a1be-356426a6c746 | -15.13612 | -48.14918 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fdba8724-e3ed-3ad5-9464-b62a05ce1e62 | -14.20815 | -58.6222 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22b1068f-f682-3713-a14a-2f380ded66b7 | -20.38104 | -46.74408 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07070924-d702-35e0-9031-984d72dbdfa4 | -22.01256 | -44.2918 | 2025-08-25 04:44:00 | NPP-375D | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 533d9d6a-1d42-3b5f-b3b1-f726acd17d72 | -20.72947 | -49.42567 | 2025-08-25 04:44:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b049638-858e-3abe-a3d4-f47d0e23bfec | -17.3451 | -47.8527 | 2025-08-25 04:44:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1ba82b1-7c64-3b07-ae0c-10a1e9c73ffe | -15.62752 | -52.70277 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb97bc30-cd11-3997-8443-76edcdcd6e8d | -15.13246 | -48.652 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 347ec651-171c-330a-8680-9c475ee6d0c0 | -14.7643 | -55.92648 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7258f7d-1ae3-30ad-aa39-b7df09f14421 | -17.58073 | -48.48295 | 2025-08-25 04:44:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ea16bb2-9763-379e-b18a-c9b50935b7c3 | -20.37962 | -46.75562 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 54972e0c-c64a-3cdc-8444-8a45b729d7d9 | -21.27954 | -43.78592 | 2025-08-25 04:44:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3297f119-ebd1-363f-9cbb-e7e4957d73f7 | -12.99567 | -56.89303 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af0e5b1b-afa8-30d7-beef-18412488689d | -14.30674 | -60.37335 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8fa15bd-2ab0-3867-9725-cf7ef58ea54b | -21.13083 | -48.92178 | 2025-08-25 04:44:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 877dca8b-ea8c-3fb5-98b0-e0c012cd8845 | -14.47508 | -52.05012 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3900cea3-6269-3223-bb6d-26f38096109a | -20.38152 | -46.74024 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40af72f1-c33c-399e-8040-c861ecfad4b5 | -14.09922 | -53.995 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2a42ca81-52f4-3275-8f76-055b3a5fb690 | -20.37774 | -46.73621 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce6dae08-a49e-35c1-bf02-c940aceb06d0 | -15.62848 | -52.71808 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5829fe3f-2d80-3bbe-a152-b9d3bebcd61a | -15.0847 | -48.68186 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e47b8ce7-6544-3ae1-8adb-830d6520d2f9 | -22.53512 | -46.81706 | 2025-08-25 04:46:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 558e4a5a-44fb-3f71-b146-bf0e8250a6cd | -23.35463 | -48.18014 | 2025-08-25 04:46:00 | NPP-375D | GUAREÍ | SÃO PAULO | Brasil | 3518503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e04cfa9b-4ebc-30fb-a1aa-f5cf120270a0 | -22.723 | -52.16275 | 2025-08-25 04:46:00 | NPP-375D | PARANACITY | PARANÁ | Brasil | 4118105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e6137c34-fd18-3b1c-a7eb-934770a3272f | -22.86099 | -52.08012 | 2025-08-25 04:46:00 | NPP-375D | PARANACITY | PARANÁ | Brasil | 4118105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82ef567b-f58a-3dfd-a4f0-fc72f9d9aef2 | -22.59872 | -46.03619 | 2025-08-25 04:46:00 | NPP-375D | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 90aee722-f7c7-3cfb-9451-cf9e2e40c2a4 | -22.8817 | -46.43572 | 2025-08-25 04:46:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 37790b1d-ca10-32de-8241-d8661b4c0f77 | -22.53995 | -46.81329 | 2025-08-25 04:46:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2dbf8fcf-dff4-3d74-8701-4f15206ea146 | -23.32646 | -47.84292 | 2025-08-25 04:46:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 93f0d40c-4fda-3aae-b595-17b1d94e4014 | -22.71571 | -52.16538 | 2025-08-25 04:46:00 | NPP-375D | PARANACITY | PARANÁ | Brasil | 4118105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ddfbd8ac-1106-3c56-a8bd-409cf52a6596 | -22.68838 | -47.35242 | 2025-08-25 04:46:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13fe81de-0229-3d84-9636-9bef3c28c5aa | -22.68886 | -47.3485 | 2025-08-25 04:46:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84bb23a3-9c45-3351-a868-066e8d16b2bc | -22.88219 | -46.43148 | 2025-08-25 04:46:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 54ce436a-6876-3f34-a04d-5d6fbaf0d40d | -23.18207 | -51.86473 | 2025-08-25 04:46:00 | NPP-375D | IGUARAÇU | PARANÁ | Brasil | 4110003 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2e5394ef-131a-3252-a88f-f81c36aff2a9 | -22.69255 | -47.35295 | 2025-08-25 04:46:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdcc59e1-c250-3697-a9ec-291e7876bde7 | -23.17868 | -51.86416 | 2025-08-25 04:46:00 | NPP-375D | IGUARAÇU | PARANÁ | Brasil | 4110003 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39dde2c7-118a-3666-9d4b-a3c909f2e05b | -22.53942 | -46.81772 | 2025-08-25 04:46:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7469c6d6-d10d-3e33-af30-275493ac3e59 | -22.72243 | -52.16657 | 2025-08-25 04:46:00 | NPP-375D | INAJÁ | PARANÁ | Brasil | 4110300 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6ab727f-22eb-36b4-97a0-2057d8bd7bc8 | -8.2129 | -61.3739 | 2025-08-25 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6a7b6c76-c5e1-3f00-9113-bdbe8e73f11c | -6.8229 | -58.956 | 2025-08-25 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 768fb532-2134-34fe-a15f-51afe1db2579 | -14.1076 | -53.9847 | 2025-08-25 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 326350aa-b5d2-3654-a619-fc11ee6f8a9e | -9.0972 | -65.7145 | 2025-08-25 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a812b71e-c509-3fc0-9db0-22c1f3754597 | -9.006 | -65.4 | 2025-08-25 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 69927b0c-13fd-3aac-8944-b7563866678a | -5.1181 | -43.1964 | 2025-08-25 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 85ba84e5-f7af-36c0-a068-77676756cefa | -8.8734 | -62.4495 | 2025-08-25 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 5d67149f-2130-3c41-851a-0bde16cfea4e | -8.0496 | -49.6753 | 2025-08-25 04:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c73d20fd-2545-3528-a681-1f835d5fa4f1 | -9.0061 | -65.3813 | 2025-08-25 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 19c24ad5-0b70-3594-bae2-817112606f4b | -8.9875 | -65.4006 | 2025-08-25 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| dc9f1138-d222-352f-be7e-1d1d68e9127b | -8.9874 | -65.4192 | 2025-08-25 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 65b3c654-1176-3b55-b167-a8ce8910edbe | -8.0683 | -49.6738 | 2025-08-25 04:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c953df32-a70e-32e1-994a-dde07da3c60c | -9.0416 | -65.7163 | 2025-08-25 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| db8f531a-fa88-3fb3-8d7d-b087d89f34bf | -8.8919 | -62.4487 | 2025-08-25 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a5e2d5c2-e28a-312e-8ee5-8f72138153b2 | -9.1812 | -60.7939 | 2025-08-25 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 77c6acfa-f8ca-3276-a962-481096ef3b24 | -9.0787 | -65.7151 | 2025-08-25 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 936d61a6-56b3-3f54-b5fe-a03314fe682b | -6.8413 | -58.9552 | 2025-08-25 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 30c48e72-2395-34bc-b5d4-39f61d0cd36f | -8.8733 | -62.4685 | 2025-08-25 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 7e24452b-44aa-3d00-8600-d4c1d1e5085d | -8.8735 | -62.4305 | 2025-08-25 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1c8d73b4-64fb-3be8-b906-cab213ac27f2 | -9.0601 | -65.7157 | 2025-08-25 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| ea93d58e-b464-3178-8576-f1e0b10ce65c | -8.0683 | -49.6738 | 2025-08-25 05:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e615dee7-fa23-3f7c-b0dc-fa1804a1a2e9 | -9.0787 | -65.7151 | 2025-08-25 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 2f795546-2f51-3052-a821-93ebe996925d | -10.7209 | -47.1142 | 2025-08-25 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| cac8a061-b9bb-3559-b42f-fb273cbffea3 | -8.8733 | -62.4685 | 2025-08-25 05:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 09d29c07-7787-3de3-9b35-404946aa8be9 | -8.0496 | -49.6753 | 2025-08-25 05:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 383a826d-28bd-3fa5-a4f0-167f06ef65ab | -8.8919 | -62.4487 | 2025-08-25 05:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 4bac03d1-a5f0-3199-b0c9-6c6f3c6f6af6 | -8.9874 | -65.4192 | 2025-08-25 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 27c7c8d7-5a86-34e3-8eab-d6e2a70c2446 | -8.8734 | -62.4495 | 2025-08-25 05:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 86ae8031-83fb-394f-96bc-9eafc3f85671 | -14.1076 | -53.9847 | 2025-08-25 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 4f508acd-e192-3d4e-b7b9-5598ecf33608 | -8.8735 | -62.4305 | 2025-08-25 05:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e1f614fc-256b-3a43-b09b-843df83a4fc1 | -9.006 | -65.4 | 2025-08-25 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2cfa651c-a89b-3078-82c7-0d590a3321cc | -8.9689 | -65.4198 | 2025-08-25 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 5b8111fc-1a6b-31d3-b089-e32ee33c46da | -8.2129 | -61.3739 | 2025-08-25 05:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ed99b925-e0d6-3108-822b-de99ac585d7f | -9.06 | -65.7344 | 2025-08-25 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 35540cc9-0b61-3894-958a-fa842dd444da | -9.0972 | -65.7145 | 2025-08-25 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 010cb12f-0916-36f6-9dab-8097b67b97a2 | -9.0601 | -65.7157 | 2025-08-25 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| b11431ce-c7d4-3471-b758-2d2f53290bc2 | -5.0994 | -43.1977 | 2025-08-25 05:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |


[Clique aqui para ver as próximas entradas](README57.md)
