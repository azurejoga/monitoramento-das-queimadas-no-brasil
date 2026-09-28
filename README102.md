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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5022a8d-0d71-3c53-959e-c9d05f8c1723 | -17.17779 | -51.73559 | 2026-09-28 16:24:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 60eb7346-5d89-335f-928c-b7b5f52fdc3b | -14.81107 | -41.73524 | 2026-09-28 16:24:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 235.3 |
| 74c4d30f-2e8e-3ffd-a2da-b6547acf79d3 | -16.69208 | -50.66248 | 2026-09-28 16:24:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a82d197-68e0-32e2-9a49-6f80df57f584 | -12.44896 | -48.21894 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 243d3fa4-ded6-37ad-a851-0582c210708a | -15.08182 | -54.62265 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6dcf352d-c2bd-3064-9405-70f3a2ba2803 | -11.69226 | -44.50972 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 66935331-a373-3c26-82eb-21fa4ad07200 | -15.45966 | -41.4459 | 2026-09-28 16:24:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.8 |
| 7c769c66-e59d-3b8c-8254-aff428db8bbe | -16.54395 | -50.51632 | 2026-09-28 16:24:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2ff4dc9f-bf94-3290-b57e-35df1d87a116 | -12.31272 | -50.25426 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a131d989-924a-3395-920e-d1ccbd1ab404 | -12.05395 | -46.48363 | 2026-09-28 16:24:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7e61ed7a-c3c9-3e66-bd4d-54e9f683d4e1 | -14.5281 | -48.29776 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cb46421b-b6de-3295-90ed-c38ff8e66494 | -15.39869 | -47.91066 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b5a4f940-4284-34e8-bdd9-6dacafbac35f | -13.5872 | -40.01315 | 2026-09-28 16:24:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 68c556f9-1a45-3669-a1a0-86e2db254580 | -12.37969 | -50.22945 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 690738f7-3504-352d-ad2f-9a90c2d393b3 | -14.77658 | -41.14315 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| def0ded5-bdb5-3e6e-8c17-09c385525060 | -15.94435 | -42.33859 | 2026-09-28 16:24:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| b122ec36-4a24-3860-a22d-16f71e81fba1 | -11.05319 | -42.99101 | 2026-09-28 16:24:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 373774c7-93bb-33e5-a1ca-f750161663a2 | -16.99867 | -41.84624 | 2026-09-28 16:24:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1ed1c257-9ca6-38ef-b5db-2058bae43498 | -12.16041 | -50.40647 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 253c07f7-b347-3058-a4b2-492168546ca2 | -11.71545 | -44.51894 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 9d4e1c7d-d325-3231-b6d1-13cef04c2530 | -16.25989 | -40.79218 | 2026-09-28 16:24:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ae082b65-8f57-3c21-8290-027da3467e7d | -15.16673 | -39.82344 | 2026-09-28 16:24:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 087eb7af-d4c8-39e9-b5a7-415353a42937 | -12.75562 | -47.34268 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fd31c8ed-0679-3da0-baa9-99b9f8649107 | -11.52874 | -47.37983 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d1fa057f-3663-382c-8374-2b5391042e5b | -14.66302 | -48.76199 | 2026-09-28 16:24:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| beecc0ec-39eb-326a-989b-088d35a2e162 | -12.64648 | -47.34099 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 915f80fd-c7c1-3ec1-b012-23ce7a9ebe1a | -13.08104 | -47.41312 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1f3a43cd-b06f-3073-9571-6bb063603ad4 | -11.83795 | -45.00695 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e4d7bc5b-e23a-3afb-975e-d31bb51e1685 | -15.55765 | -47.91933 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1d53ad9c-ac83-300f-8694-8d053eb6f9f2 | -11.49609 | -47.32815 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f5e4ead3-0d2f-3ba1-80f5-1db5a0e56258 | -13.08945 | -47.44505 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4ab776f3-7e5c-381b-8bf2-7a1198eeb874 | -15.8724 | -40.45294 | 2026-09-28 16:24:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 26c7d3f4-5aea-315c-876d-afb7e19ae81c | -11.55038 | -47.38094 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 3412f881-1e04-3883-8604-a3ed5dcc4d66 | -15.4104 | -47.92905 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2fb38981-3e2c-3f95-9de9-677b88c7445c | -11.37151 | -43.36436 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 52534968-0989-3694-b5f5-08ae8f90d25f | -15.84994 | -41.26784 | 2026-09-28 16:24:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 389fbad3-1139-3830-ad05-3414d9d20040 | -11.49915 | -47.3835 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 7f5db6d1-5dfc-31b4-af2c-5043f166f592 | -12.22946 | -50.3583 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| efd94116-1bab-3d42-be78-5a8f03dc9130 | -15.06495 | -54.59585 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 88cc74d9-9a6e-3b2b-bb5a-ebda21ac3104 | -12.79701 | -54.00996 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 7021b161-4dfe-3cda-895e-0355c92c4703 | -12.68817 | -47.36022 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 341eabf4-f8c6-39f0-b2b2-85048789a973 | -15.40646 | -47.93506 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8d7229c3-503f-338b-a017-6dda69a78027 | -11.50234 | -47.37516 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 79e23dea-73e2-3ebd-b174-5ab860a06c6e | -11.53878 | -47.39055 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 5d1d0d5f-d696-313d-b895-a5da7cf4865a | -14.12094 | -46.29036 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| d0ab1688-1e91-3343-88eb-b66c30fd689c | -16.29111 | -40.19783 | 2026-09-28 16:24:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| c02ec92e-5da7-3dfe-a908-922c977b1854 | -13.89313 | -53.66907 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a5ec4506-a788-38e1-97e4-b00f6da52305 | -15.40612 | -47.90236 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 31a09eb5-095e-3183-a6b7-b6106464ba46 | -16.33706 | -43.72496 | 2026-09-28 16:24:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bb2166da-7829-30c0-8e33-8f400740d74c | -12.75159 | -47.28935 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f43dadd1-10bc-3192-b4b9-310af37c26e0 | -15.18246 | -46.14022 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c21cc2e1-d124-3f58-b1a4-d19237f0d3d3 | -12.73045 | -51.5823 | 2026-09-28 16:24:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 92b5c1c2-16e8-3a71-bc25-e74dd1b11c86 | -12.71023 | -46.97693 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 278795f5-0322-3eac-ace5-c189ec5605da | -14.54166 | -40.847 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1d20f933-8c1c-32e0-8668-da2707b6a728 | -14.32071 | -44.82381 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 43b2e69e-21e6-3960-998c-43f9ac4eb09b | -13.46782 | -48.63187 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 51195ef3-e54e-3cc2-9049-47a8893ff128 | -13.96927 | -54.00503 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b09d8fea-6846-394c-9724-b7b5bd2867e5 | -12.88264 | -44.77398 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| b243c1a6-7f7e-3df8-bb35-08c9658838b7 | -11.66499 | -43.53061 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 81b5cdc2-28bb-3b1d-aee5-1a6423972a68 | -15.07235 | -54.62292 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6df9df1a-b76c-3db1-9b45-c35da63197ba | -11.56997 | -47.39839 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 41ef391e-a367-335d-9787-0b8790570569 | -10.55444 | -40.29699 | 2026-09-28 16:24:00 | NOAA-20 | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 20e40717-650b-3312-b029-d0ba30de1ace | -12.64082 | -47.29071 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 20f70daf-cb47-3273-a531-7ca0e2912b8a | -15.41125 | -47.90605 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f3b60e84-28b1-34bf-8d9b-e3b2018e4acc | -11.21142 | -44.76306 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 180878dd-300f-3a79-9c59-82397b920f7b | -15.4602 | -41.44952 | 2026-09-28 16:24:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| 481ca804-5794-3478-a17f-c1877c8803aa | -12.68228 | -47.34842 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| ee657d34-740e-3225-9103-eef8fcb21b47 | -15.05786 | -54.59609 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5e6e16e2-e7cd-3e3b-922a-3efd3f362beb | -15.25364 | -40.2705 | 2026-09-28 16:24:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e9e51ccb-58dd-3c8e-a78b-f6a174d0054d | -14.52866 | -48.30236 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 919729f1-b50c-3364-9516-93025186441c | -15.04597 | -48.03877 | 2026-09-28 16:24:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f29fbd26-f1f1-35f8-8d32-235b13beed53 | -15.21361 | -46.19477 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4e0f9d68-4903-3027-9ee1-51c2bd77f79f | -15.02725 | -49.58256 | 2026-09-28 16:24:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d683390b-a781-3583-87b2-84a459448633 | -12.86916 | -44.81155 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 0d32f97a-c2ff-3d68-9b3d-f35ea6c8f9ad | -14.95441 | -41.04087 | 2026-09-28 16:24:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 996d5a98-9535-3aec-b152-a6baf98c76b5 | -11.70063 | -43.48707 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ac83af35-d2b6-37f6-8dc0-4ef8f199673e | -11.60293 | -44.13974 | 2026-09-28 16:24:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6ad830d8-c0c6-3208-a5f5-082b96db80aa | -15.18214 | -46.14412 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b0debcb6-1239-3a68-a40c-408dffadf1a8 | -15.93913 | -44.08051 | 2026-09-28 16:24:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e12c26d9-40ea-3709-8c69-26888b57a263 | -13.5746 | -46.35611 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47fca080-4d8d-3289-b716-3426ec1743c3 | -12.72434 | -47.27185 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d1da09cb-e82e-31de-bbed-e8b412d48f5f | -13.08316 | -47.44434 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| be68c065-f2ed-31a8-8a70-5d64b667eb2b | -12.68141 | -45.01702 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 2e9a0199-e806-3572-9ef2-9a3a46b768ba | -14.5867 | -41.23315 | 2026-09-28 16:24:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 6a4a6d05-b328-3384-a3be-767ec957dc36 | -13.65387 | -49.8273 | 2026-09-28 16:24:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30ce2a3d-cf62-3b60-be2f-01eec71021a9 | -11.37789 | -43.43177 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| d905890b-319c-3e25-96b2-c2f5c96bb44a | -11.35242 | -43.42421 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 006cbaef-5512-33c1-8608-91246fc529b2 | -12.1652 | -50.3601 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| edb975ad-a5a4-312d-ab63-cc7fa93296fb | -14.87023 | -41.02216 | 2026-09-28 16:24:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 30.2 |
| 3e5fa3ec-5196-31bd-87a5-2ab592e6bd8e | -12.31803 | -46.40605 | 2026-09-28 16:24:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b02a60c3-6a6a-3ecf-be2b-5a87dd35cd19 | -11.19312 | -44.8026 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 14d809cc-adae-3f4d-af1f-e4143f2f2744 | -12.29157 | -50.25374 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4f566129-dd92-3749-9bdc-e0afa1742886 | -14.99623 | -47.86135 | 2026-09-28 16:24:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| da707012-79aa-3f7f-8199-d78a61b8564a | -11.2051 | -44.75853 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 78a8aaed-d33e-32c7-98a0-8f029f91b41e | -14.09817 | -41.38952 | 2026-09-28 16:24:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| aa8184e6-4c97-3242-a957-8b17a7e905ba | -13.58392 | -51.4479 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5ab6197d-7458-347d-a3d6-60ecea17aff6 | -11.27379 | -43.53228 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 07ca4f42-1770-39fe-8617-54d05097165a | -12.44348 | -48.22239 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e72a23c5-36f7-30ab-aa49-1471e1e95e52 | -14.12171 | -46.29413 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| da1b8dc8-6f31-3d33-9493-ce00ec07870a | -11.19612 | -44.79795 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |


[Clique aqui para ver as próximas entradas](README103.md)
