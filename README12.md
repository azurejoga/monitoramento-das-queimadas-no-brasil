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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11034a2b-29d0-34c3-be82-2f16792d2392 | -5.11827 | -47.307 | 2025-12-27 04:40:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e9b6d47e-85cf-310b-a0dd-3a9f72092258 | -6.22582 | -55.65863 | 2025-12-27 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be488100-623c-345c-bc60-b9c448ea54d5 | -10.49534 | -44.92807 | 2025-12-27 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 24db1452-0521-3d31-99db-1240496f8b0d | -3.46943 | -52.80363 | 2025-12-27 04:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abdf5beb-3caa-3db1-8500-8273020f6c0b | -6.62233 | -43.86645 | 2025-12-27 04:40:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19223adf-8aa6-342e-91c9-a67c95e9e8e9 | -6.55167 | -43.10215 | 2025-12-27 04:40:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0542d251-99c7-3c8b-9b01-a70f3f4170c1 | -10.94488 | -49.41914 | 2025-12-27 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5642d579-1619-3c66-91d3-efe805670d00 | -11.93809 | -52.46424 | 2025-12-27 04:42:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae147c1d-097b-3e6d-8fa5-2c0638372182 | -15.75104 | -47.73057 | 2025-12-27 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da83c04b-eb69-35b9-b386-ae1c2367a396 | -11.63655 | -49.42588 | 2025-12-27 04:42:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0555f91-f29b-37bd-b8c6-bc9c89d681b2 | -13.55259 | -49.90691 | 2025-12-27 04:42:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17ee8563-a466-322c-bf7a-3a56475adc2b | -15.73913 | -41.89651 | 2025-12-27 04:42:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d04b63d6-31e8-3e79-a195-c938c2878650 | -11.46202 | -54.35774 | 2025-12-27 04:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bdc2e0a-572e-3bc7-b058-e2c5378e3f27 | -11.94009 | -47.88139 | 2025-12-27 04:42:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ec6e060-6904-33fd-b0ef-7012fd45c547 | -11.45908 | -54.3527 | 2025-12-27 04:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d89a3316-bf4f-39b7-9169-8ce23725903a | -12.16122 | -46.6762 | 2025-12-27 04:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 192db34b-ff82-3c43-b159-09d5d0218175 | -12.6654 | -46.77369 | 2025-12-27 04:42:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8058b050-a78a-3871-be09-4e8e43af927c | -12.51932 | -48.38229 | 2025-12-27 04:42:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10a78ac3-f9a8-3956-9d06-8985f4cefaf9 | -15.65622 | -53.68546 | 2025-12-27 04:42:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70aeae04-4329-33ec-a037-7e1f091ab7c6 | -12.51641 | -48.3777 | 2025-12-27 04:42:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41504526-e484-3a21-a9a7-42f1c1173491 | -15.86983 | -40.93158 | 2025-12-27 04:42:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 97fe61c8-7495-3630-86a3-9969ffc84b89 | -15.88522 | -43.45615 | 2025-12-27 04:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 3686c2b8-729a-329e-ab20-d0f2c44f50bc | -12.51701 | -48.37367 | 2025-12-27 04:42:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4682fc61-314b-3e1d-b9ba-160c4c92ebd1 | -15.2681 | -43.17747 | 2025-12-27 04:42:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 07c290b3-0b71-3a52-9582-f659f64174aa | -12.29545 | -44.34978 | 2025-12-27 04:42:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd65480c-5971-365a-afb9-0724a5a60326 | -11.94367 | -47.88193 | 2025-12-27 04:42:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91d61a27-b420-34c4-8888-1fbf657e6ada | -16.12898 | -56.85303 | 2025-12-27 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0922ca1-d3f1-30e7-9619-e3072afcc59c | -14.44008 | -44.85843 | 2025-12-27 04:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e780318e-1778-3d42-b62a-10705f0d9393 | -15.8909 | -43.45105 | 2025-12-27 04:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 7cc1d8f7-3066-33a3-91e3-98a66467a693 | -15.90502 | -43.33484 | 2025-12-27 04:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09bb5aa9-7b6d-33c9-be57-11ec8487f2a9 | -15.89137 | -43.45272 | 2025-12-27 04:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 3ed57786-809f-38c0-b5f1-604da2960a5c | -12.5127 | -43.69295 | 2025-12-27 04:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc1ce040-01e1-3a38-a807-1ce7715a069b | -16.09233 | -55.42649 | 2025-12-27 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3db2b03-1358-30fe-a30a-b2eb97e3e2f6 | -12.51993 | -48.37823 | 2025-12-27 04:42:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39f19e7c-9b45-3fbb-aaef-5eef94d1ac15 | -11.63876 | -49.42252 | 2025-12-27 04:42:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb0564f1-c40e-31e2-8a53-f733fea66f8c | -12.66853 | -46.77904 | 2025-12-27 04:42:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36289e77-1709-3e27-8478-bbc111a9de3c | -9.71771 | -60.20353 | 2025-12-27 04:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fd576e14-c077-3923-9935-70db76d43fc6 | -13.34248 | -49.09367 | 2025-12-27 04:42:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7e94954-d684-3254-94eb-3494aa9382c2 | -13.51915 | -43.67599 | 2025-12-27 04:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e507de8-5c76-3f6c-a4e7-648d6833d8dd | -15.97087 | -56.27639 | 2025-12-27 04:42:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b22392ae-3282-3e2c-9336-5de4b161c4cf | -12.66157 | -46.77311 | 2025-12-27 04:42:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65e02db7-cfef-38f4-ac27-7fb975697b11 | -11.63375 | -49.42173 | 2025-12-27 04:42:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56c9b984-1d0a-345c-8c54-4d77fe2f3751 | -15.87713 | -40.9319 | 2025-12-27 04:42:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5f3ad896-e4c1-3986-af84-400888b31b5f | -14.43993 | -44.85226 | 2025-12-27 04:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 876d1d08-a353-3214-96cb-03f46ed717f7 | -16.0928 | -55.42817 | 2025-12-27 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5fffbb2-7865-349a-934b-4c8ceee2b83b | -15.84945 | -55.20608 | 2025-12-27 04:42:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01fbd000-0ea4-34be-912a-983ec610ceac | -15.97099 | -54.8889 | 2025-12-27 04:42:00 | NOAA-20 | SÃO PEDRO DA CIPA | MATO GROSSO | Brasil | 5107404 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e423625-da79-3342-ab33-19160839eb44 | -12.67211 | -46.77234 | 2025-12-27 04:42:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1816df8-0aba-36da-bd42-35ba488674f9 | -15.87575 | -40.93186 | 2025-12-27 04:42:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1a5dcbf9-dedc-3717-b986-94593942cd0c | -11.45833 | -54.35714 | 2025-12-27 04:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9f09289-4525-3326-adc7-cd4bf163e281 | -15.89019 | -43.45682 | 2025-12-27 04:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9422b6aa-4759-315d-a8da-bf4e28dab878 | -11.93949 | -47.88549 | 2025-12-27 04:42:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3122ae2-4573-35d7-a7a1-80eec9578a71 | -11.53774 | -54.37429 | 2025-12-27 04:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d17a56da-3369-3d83-8880-923d6f63d197 | -12.72064 | -47.72628 | 2025-12-27 04:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb446fe1-3a51-321f-8f66-fe83323bdd0a | -11.84871 | -48.79286 | 2025-12-27 04:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dc51136-673f-3f40-9fda-48f61a6b877f | -11.80122 | -48.27876 | 2025-12-27 04:42:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d80629a-6ab0-350c-b728-9cf951b3ae5e | -15.96955 | -54.88746 | 2025-12-27 04:42:00 | NOAA-20 | SÃO PEDRO DA CIPA | MATO GROSSO | Brasil | 5107404 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b295280c-959c-36f6-a95a-acb3820c84e0 | -15.90001 | -43.33411 | 2025-12-27 04:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ad4558b-fde6-3c55-a761-9ed2011c1117 | -15.8712 | -40.93171 | 2025-12-27 04:42:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| acdaeaba-bbea-3c0e-82eb-faff228dfa49 | -14.43937 | -44.8567 | 2025-12-27 04:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 584f7a4b-3a1f-37cd-9b8c-d3b0dcdcc253 | -12.67145 | -46.77713 | 2025-12-27 04:42:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e077da9c-93d5-327d-8bbe-0ff81bad43a9 | -10.74835 | -52.78657 | 2025-12-27 04:42:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14d27b27-4c67-3bce-b3c6-6fb276343e80 | -12.0814 | -49.52446 | 2025-12-27 04:42:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aa84c701-856a-3350-a32f-79076df0c9ce | -14.44067 | -44.85401 | 2025-12-27 04:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 518d3417-95fb-388e-a010-44b6e9b97857 | -12.08533 | -49.52135 | 2025-12-27 04:42:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e86ffa6-e92c-325f-ac6a-4da653aeb99f | -15.88592 | -43.45035 | 2025-12-27 04:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| bf013f61-33f8-3773-a765-255ab8c1cb90 | -11.4103 | -49.17051 | 2025-12-27 04:42:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 562c4d07-d9ab-3796-8346-e552b0c8f27c | -17.19653 | -47.02902 | 2025-12-27 04:42:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a38c6927-ddc1-3060-af9d-6770d99699a8 | -12.62973 | -54.22081 | 2025-12-27 04:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c61b9a7c-8a6c-3abc-a672-1c0d661af88b | -11.56418 | -48.49616 | 2025-12-27 04:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 102f9fca-148a-309e-8088-da32b1eaed85 | -11.63711 | -49.42226 | 2025-12-27 04:42:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be36fef7-ca7d-346d-8644-ea5ff3188c5a | -15.89071 | -43.45851 | 2025-12-27 04:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 32.5 |
| c5319c23-a05e-3c27-8ab5-176d0f091c90 | -12.66922 | -46.77427 | 2025-12-27 04:42:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4d719668-1e7e-35cb-b4dd-08977c0be8b6 | -12.66471 | -46.77846 | 2025-12-27 04:42:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9318e3c-7ae5-3e2e-8672-be863ef6b143 | -12.50803 | -43.69232 | 2025-12-27 04:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6aeab30e-776a-31d8-a22a-3e5b7b616b78 | -19.90686 | -47.4727 | 2025-12-27 04:44:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b2dae53-fbfc-31d6-af32-fa985931275d | -16.30119 | -58.25933 | 2025-12-27 04:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 04801aa4-3756-3704-a9cf-40de6a319775 | -19.17506 | -50.61315 | 2025-12-27 04:44:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 572be81a-26ee-39d2-a582-26d75d31b5a8 | -19.31132 | -43.52635 | 2025-12-27 04:44:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 969ef71e-9f9a-3f8f-88c7-670ce9a7abcb | -19.55839 | -49.40878 | 2025-12-27 04:44:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdf20be3-a7c8-3254-b451-eaf663b36213 | -19.55479 | -49.40819 | 2025-12-27 04:44:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65af5368-99e0-35f9-86f7-6d866fb2936c | -20.28127 | -50.57217 | 2025-12-27 04:44:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 059b9ba8-2aa6-3758-b3e9-7c52396876e9 | -20.28415 | -50.57673 | 2025-12-27 04:44:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 70e35ca2-2688-3c43-8a47-d8164eb81fea | -18.31235 | -46.40387 | 2025-12-27 04:44:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e6a2e60-f6f3-3ca8-b408-11b6ebb48f81 | -17.52622 | -50.44138 | 2025-12-27 04:44:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5dd2e40b-6aa5-3432-b1c8-712e9189cc3d | -19.30956 | -43.5285 | 2025-12-27 04:44:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5fec303-44ba-3bd6-9e86-fca994c700a5 | -19.31164 | -43.52322 | 2025-12-27 04:44:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9fa419ed-58d9-3f06-a5ff-6e99226941b6 | -19.3099 | -43.52542 | 2025-12-27 04:44:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5353824b-db55-3291-bb9f-51a23e8be10e | -17.98106 | -47.8825 | 2025-12-27 04:44:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c350ac17-810e-3bed-83d7-a052b6d2b057 | -17.83858 | -50.81158 | 2025-12-27 04:44:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef57f91b-5249-3e18-b4df-6514758e11aa | -18.30824 | -50.21293 | 2025-12-27 04:44:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 13f07f7a-4fc8-3215-ad9a-34c68c3d16b1 | -18.30814 | -46.40315 | 2025-12-27 04:44:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f397315f-ef9f-3aeb-9236-48732157b919 | -21.71533 | -47.11168 | 2025-12-27 04:44:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e0692b6-9202-39a8-8b60-6c2db641b833 | -23.77083 | -54.57037 | 2025-12-27 04:44:00 | NOAA-20 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6d38913a-d0f4-3c39-b641-5d88ff81d4b3 | -18.44512 | -48.73548 | 2025-12-27 04:44:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f323f7e5-ff30-3a6d-bdfa-3935ff77b79d | -17.52565 | -50.4452 | 2025-12-27 04:44:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38854919-f415-351c-8a56-c79fb8cdddd9 | -20.28069 | -50.57618 | 2025-12-27 04:44:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f0bf14eb-f07b-3e92-9ad4-77957737b040 | -20.55081 | -54.63082 | 2025-12-27 04:44:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d8c3e07-dbdd-3238-b4cf-8b4b18896796 | -19.17449 | -50.61707 | 2025-12-27 04:44:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 47176744-66ba-339e-bc68-a40f0a33c133 | -18.83985 | -53.62507 | 2025-12-27 04:44:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README13.md)
