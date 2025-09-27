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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25abe5cb-f729-3fe3-845a-e3886c458f39 | -10.46711 | -52.15115 | 2025-09-27 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49dbb104-c797-30ea-be33-2ac3a3d48337 | -15.44632 | -43.64595 | 2025-09-27 04:46:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9b2cef14-4681-3c26-9073-53293389d126 | -17.11597 | -46.87219 | 2025-09-27 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4520afc7-5908-36ce-9d87-f2d10d355b1a | -15.57757 | -51.70274 | 2025-09-27 04:46:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 110f92c7-c0cd-375e-94d5-f67b973b131b | -10.39917 | -46.1319 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44447a7f-44b4-35c9-9059-c58d239ddace | -12.02879 | -47.07836 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d14c6a04-f128-37d9-97e4-3541c457f26a | -12.0351 | -47.06414 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9daa578b-2c5b-3c87-8c23-4bb34105c99a | -10.12084 | -45.33176 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9dea1409-3770-3f64-ad9f-c1b100df059f | -11.43103 | -44.99012 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cbdc0ad-f66e-31a7-84f5-f51296507124 | -11.99563 | -46.62096 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12bd8d9e-fc1a-3173-8542-88cac2de4768 | -12.03284 | -47.07892 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e57ee0d-cdac-3ce6-8e5a-5c3c70fc5e95 | -12.64891 | -48.15332 | 2025-09-27 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b49c6a9-63c2-3f4d-a49c-89219bb3ad5b | -15.27873 | -46.44333 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b538aa0f-58f2-3e31-a9cf-168f41c4cb9d | -11.97469 | -47.87752 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e29c97d-4953-3685-9a72-4687cf5074d3 | -14.02256 | -56.10068 | 2025-09-27 04:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0e3f031-f7da-3e89-a9e5-d262e9680c02 | -10.40229 | -46.14029 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61fa68d2-178d-3df5-856e-0b51d2541085 | -10.12288 | -45.34343 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ed5896bf-307b-30d5-989a-e4003228ff2e | -11.37421 | -44.95701 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fe1ac5e-2b08-3858-b058-243b0712081e | -14.58983 | -48.24927 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5042d301-3531-31a4-9bd2-7ab796d122d1 | -12.9845 | -49.43239 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7993ec02-d54c-3424-bb16-410f1c728d3b | -10.80855 | -45.3784 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73d556f7-6df4-37b2-8257-816d5a72a355 | -10.25614 | -50.24154 | 2025-09-27 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 861b9f18-a708-3d35-9084-874625067151 | -11.22579 | -49.21232 | 2025-09-27 04:46:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 249d134c-8ff4-3287-850f-4adaf9a8e890 | -11.97445 | -47.90687 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8678e2ce-3fbf-3a89-876d-4a58327a8a4f | -14.0634 | -48.82634 | 2025-09-27 04:46:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2af82e23-94d6-3bd6-b1d5-767e58bfb595 | -11.60966 | -45.42568 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f507d10-1313-37d5-ac2d-7c533eb6c4aa | -16.12398 | -47.39015 | 2025-09-27 04:46:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1359a831-cdf0-3a7d-992c-594861dd5799 | -15.26606 | -51.47528 | 2025-09-27 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4e9962b-2b44-3ec6-bdf9-064616fa8dac | -11.78309 | -43.76082 | 2025-09-27 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1072942-74d6-363a-9eaf-2ac5a68d4483 | -11.68628 | -44.43084 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1e616f9-a14a-3327-81da-4e1996934a57 | -9.91415 | -58.56264 | 2025-09-27 04:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30e123a6-cb43-3bf2-a562-c2b4f2a3e9ae | -12.64865 | -51.6658 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5adbf576-3098-3717-a3a8-c2dba99a3367 | -11.35392 | -45.00803 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d38183ff-3c1e-389b-9fa0-5fa08f1b4270 | -15.26719 | -51.46783 | 2025-09-27 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8c583e14-67ee-3ee4-a204-303ad88d5cbd | -9.94179 | -48.4967 | 2025-09-27 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69ce70ec-6d41-392b-b08e-9ba5aa625206 | -11.35662 | -45.0196 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7616fa20-dba9-3d54-8833-8f7725249ffc | -11.61186 | -45.42384 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f9a7953-5073-3b8a-9347-e0a2f0f0c8fe | -10.11577 | -45.32917 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0963d21d-f1aa-381a-9dd1-ceb61518af26 | -14.84706 | -45.6133 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e3d1c91-6af6-3ac1-9fb4-250974aa8e03 | -10.28341 | -45.22069 | 2025-09-27 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 28481461-a39e-395b-a9a7-937e45b20a9d | -12.98807 | -49.43301 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5a432c4-d955-3786-bac0-a5f568474b0c | -12.03084 | -47.06395 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2cbfbf9a-de7a-30c2-b035-77c94d7424d3 | -13.32814 | -47.30817 | 2025-09-27 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51757cd3-c302-38e9-a48a-d01725399f02 | -14.46165 | -46.84581 | 2025-09-27 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ffe247f-9dca-3e31-8c3e-33ce4f1a8615 | -11.96045 | -47.89487 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c3db37a-888c-3574-a400-e376952f94db | -10.11641 | -45.33115 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8fdfe2a-9424-3a87-a473-41ee636e3d74 | -11.61898 | -44.42492 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 883cf0b7-8ab4-3648-9eb1-71e6f2d5ce91 | -17.37041 | -48.1779 | 2025-09-27 04:46:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 862f7487-79c1-31f0-869b-f317aab74bd0 | -14.97416 | -46.76709 | 2025-09-27 04:46:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6af234f2-e8d9-3eb5-9474-6f2962b3af04 | -15.97101 | -50.87487 | 2025-09-27 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 65729b12-5b64-394e-8dc9-65865946344e | -14.95362 | -50.1536 | 2025-09-27 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 101ca925-203e-3024-8a98-9f51d0e0253e | -11.4755 | -47.24618 | 2025-09-27 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eee77904-fc94-373d-b5ae-de7e60066b2e | -15.4193 | -48.20075 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80d955d5-6e57-37a0-86a4-795e1499d754 | -12.65364 | -51.67753 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 381578fe-7da4-3672-81d7-8d0c4b2cd52b | -14.83184 | -45.62164 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab03fc79-ab81-39a6-8b35-40812a04fa59 | -11.97231 | -46.59449 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a31e211e-5106-3c47-82c6-5abf5873a5cc | -11.37361 | -44.9616 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fad2dce7-7c09-36bb-a2c7-e08bf13aa88a | -13.60143 | -47.31097 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67537c1c-f9df-355a-8387-57667810d9cb | -13.95055 | -50.10171 | 2025-09-27 04:46:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 019cc3bc-2a04-3bc9-af6a-b67db5f5e4ff | -11.97651 | -47.89239 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42585a68-413e-3c5b-97b4-442aad5ec043 | -15.42888 | -48.21884 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2948c346-a4a6-3d8d-96a4-11fd649f2696 | -15.02946 | -46.94677 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f2ab2b8-d5ed-3858-b5b1-30cc13847429 | -15.54054 | -44.3421 | 2025-09-27 04:46:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1851dc9-9c33-3c35-ad33-a544c4fa2729 | -11.04171 | -45.87407 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddb26efa-a022-3922-b3ac-465af7c3b22d | -12.83076 | -44.69176 | 2025-09-27 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4cb3bd5-1d65-394d-b52c-af8da2f6f5c3 | -12.6542 | -51.67397 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15364bb6-2e76-36ea-a6ce-35475899eb83 | -15.21658 | -56.00385 | 2025-09-27 04:46:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c794790-c08e-35ff-878b-addceac3595b | -11.36375 | -45.00097 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75e60947-2c1f-39ce-8e5e-8f4f2b06f6d4 | -10.11076 | -45.33923 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44bd9318-d0db-31fa-b753-fcb38671ac0e | -11.37484 | -44.95223 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87ce4584-1798-3ae5-b002-773e50ce7dd8 | -10.58185 | -46.27502 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 660f2416-dc7b-35b2-ba39-2ac90a8026b6 | -15.26944 | -51.47582 | 2025-09-27 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d382f57-aa69-308e-92cf-05ab768e1b03 | -10.18466 | -49.51134 | 2025-09-27 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfbcd7d7-0586-3208-8e29-b3d37a9c74d3 | -15.27198 | -46.46106 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4eed3816-1963-3705-b62d-66449fdee7ac | -10.80526 | -45.36914 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e9c6f1c-4bf1-3245-9168-478f32285c73 | -10.11396 | -45.3485 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28398f82-703c-33f4-8507-1ceadf2ce2d7 | -10.119 | -45.34475 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d50980af-5682-3ec9-b74c-e82dc4f91ef9 | -14.83712 | -45.6172 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a26c881-c426-3003-9709-54f1e245abff | -11.44786 | -44.93561 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e6f249c-6757-3181-8283-ed531274e814 | -11.36186 | -45.01544 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1735e1ce-3b0a-337d-9718-de14206137c4 | -13.70327 | -47.89679 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68ce8822-f549-3bc6-96a9-077cf58db444 | -15.90226 | -57.48815 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19759f03-55e8-353f-b128-e189b3f3efc7 | -15.01613 | -51.30299 | 2025-09-27 04:46:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7c228c4-8fbc-349a-ad40-2fcb982619e7 | -15.2686 | -56.82087 | 2025-09-27 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1ac503f9-572c-32b9-9e62-4a8375b19111 | -10.6026 | -49.63996 | 2025-09-27 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 35b7dc4b-1c13-3923-aa87-d5a35493df15 | -11.4455 | -48.52507 | 2025-09-27 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47b9f24a-a644-30ff-af2f-8ed909dc9009 | -11.35327 | -45.00932 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11b22f01-0043-3504-859f-af57f4ad4959 | -14.97468 | -46.76302 | 2025-09-27 04:46:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5b8821d-d2ce-36d5-b1b5-974c2ba93537 | -15.19978 | -48.46432 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9199351f-e7c0-36e1-9534-0222c5eaad5e | -15.04963 | -48.36128 | 2025-09-27 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02760cbf-914c-30bd-bd51-29124ae800f7 | -11.43232 | -45.01526 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84654bcc-d396-37b8-aac3-cc8e75b9924a | -11.71321 | -44.41273 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2ea437b-ffc1-3e5f-860c-d775c4ea469d | -10.12347 | -45.33908 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cd4f6cde-8143-387f-bfb2-45c7f78b9ad7 | -11.97513 | -47.90205 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce890d19-c18f-3753-b3a7-130b9d4672db | -12.9649 | -48.90618 | 2025-09-27 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fde46fd-9430-3599-ade6-7be6dc3e033e | -14.06404 | -48.8217 | 2025-09-27 04:46:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96cf5c7d-caf6-3a87-9a1a-e2d4ca10c4ec | -14.96807 | -46.76268 | 2025-09-27 04:46:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 229be503-4051-3795-85f5-a0b5ca2c4d81 | -14.84578 | -45.62358 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e05a8687-9395-3cf3-afe5-ac511fb465fd | -13.83547 | -47.95352 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c39e81f7-e26c-3252-b2be-601f05a30955 | -11.62774 | -44.42836 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README54.md)
