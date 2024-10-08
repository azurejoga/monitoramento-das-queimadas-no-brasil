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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 444c7fd6-106f-3a4f-acc9-6efd2805d1d5 | -10.81091 | -56.27032 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b22a966-b3dc-339b-82b5-cc7fa52ddcef | -10.6621 | -56.04974 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d53f081-c69d-3f6d-846e-30679522eb99 | -10.66152 | -56.05334 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0983f74f-9fa5-3be4-ac9c-65bc145e558e | -10.66063 | -56.05 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fecf03d1-5562-3697-a380-8ada0f86b780 | -10.66005 | -56.05359 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a854661-e571-347f-bc1c-81ed2659a87f | -10.63428 | -55.91368 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8d54d1f-346d-3598-bb28-153b2e1027c9 | -10.63272 | -55.88053 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63833601-b7dd-367b-ab67-62efc69b570f | -10.6315 | -55.90957 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 773a20f1-f371-3239-963e-69621c58abcb | -10.63093 | -55.91313 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4232861d-0084-3de2-92f6-7e0ac3c447ba | -10.63036 | -55.91669 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3d19306-1c75-3205-a8cf-e9b2ea27a6af | -10.62979 | -55.92025 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f952f076-dac7-3de0-9cd3-9564df9c7774 | -10.62922 | -55.92382 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57a231c5-f6d2-3342-8ccb-6249ba82441c | -10.62816 | -55.90903 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f6254186-fa55-3059-b397-ab8ed3074be4 | -10.62702 | -55.91614 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 323ce443-9b1c-3f20-88dd-90fcf0d316f3 | -10.62645 | -55.9197 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 173312f9-d1e7-3ad3-8b5d-a4fc963e84a0 | -10.62587 | -55.92327 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bc935378-1517-33bf-8d55-3a383d6a2422 | -10.62481 | -55.90849 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e98f10cf-f212-3027-86d7-bd174d0df129 | -10.62424 | -55.91204 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66d0ce0f-0272-3ea5-9fcf-2ac20af66e5d | -10.62367 | -55.91561 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cc813a1-0a0d-3b31-93ea-8b6ff812320e | -10.33974 | -55.59331 | 2024-10-08 04:57:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dccc5e55-84de-3afa-bda4-dcc94aec185e | -10.13125 | -55.20579 | 2024-10-08 04:57:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2014dd6-0ce1-3534-ab62-ba04db4d6650 | -10.12848 | -55.20175 | 2024-10-08 04:57:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2749b29-99ea-3ee0-a84a-b479670a9794 | -11.47513 | -56.76384 | 2024-10-08 04:57:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9daea319-250f-35ef-9564-50f59df671ec | -11.47453 | -56.76751 | 2024-10-08 04:57:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 943273f5-256a-3f2c-b6ad-4f02d8c71dfd | -11.47054 | -56.77061 | 2024-10-08 04:57:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c4a19c5-17ce-30c8-bb38-9d2a11968527 | -11.40724 | -56.73042 | 2024-10-08 04:57:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 971caa9e-e5a3-303d-8729-9ea749f513cd | -11.38395 | -55.5993 | 2024-10-08 04:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb7f8c48-4504-3bf3-892d-788f7f9462e8 | -11.3824 | -55.59583 | 2024-10-08 04:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f182075a-88f5-3fe1-8ed0-1ca67ea0990c | -11.38184 | -55.59935 | 2024-10-08 04:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| badb265e-ce37-32ee-8304-2ca88f874cf9 | -10.91156 | -55.79124 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc71baad-c0ba-3c99-bf71-6b6ce2889c9d | -7.11152 | -56.44578 | 2024-10-08 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e2d2611-1d2d-337a-8594-7dfef26a7363 | -9.36078 | -57.50258 | 2024-10-08 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cb6a894-c809-32db-9ca0-717e8486ada7 | -9.35722 | -57.502 | 2024-10-08 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dda8323d-8164-3caf-98a8-10c52c26485a | -9.3439 | -57.60369 | 2024-10-08 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1a7d9d5-7c45-384f-b3ce-258b43e83a25 | -9.79264 | -57.11837 | 2024-10-08 04:57:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5697d8f4-0db7-345a-8773-8bc3cd95e4e3 | -9.77377 | -57.95635 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74900a03-8d45-3f98-951d-fae4749d6337 | -10.59923 | -57.52841 | 2024-10-08 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6290381a-bc28-3d80-b2fb-f82e2930a884 | -10.56107 | -57.69375 | 2024-10-08 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9bc57cd-a84f-3464-904d-5cb26f274587 | -10.55753 | -57.69315 | 2024-10-08 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cc67dad-6d4e-3125-915a-2107a84d998d | -10.33288 | -57.50088 | 2024-10-08 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31bf7cac-1178-3a77-b4dd-5fa659638350 | -10.33141 | -57.79399 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb14276a-1d25-3af5-93e0-ca4874a647ab | -10.32784 | -57.79342 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6e1d9b4-46f4-3e95-96a1-b8e58ed56137 | -10.24365 | -57.73448 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 736c0617-df69-3036-97f8-6cef2d5f418f | -10.24298 | -57.73853 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b28310c8-95d8-3433-9f92-b9eaa41ce83d | -10.22289 | -57.79361 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c89fc422-5e03-39ea-b971-a2428b639cc2 | -10.22222 | -57.79767 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ddab8c0-fc1e-3579-862f-4ec4e96eff22 | -10.1207 | -58.20552 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 839162f5-7163-3924-ad23-72fedd0bed34 | -9.54371 | -57.90318 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 591b5d86-7996-3658-b264-1ec8798a0e2d | -9.48713 | -57.92916 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c751093b-70b6-3b82-9ff8-df8a36eb9e6f | -9.48384 | -57.92763 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6892e140-3808-3835-9267-eebc6c548359 | -9.4835 | -57.9286 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce40d017-5e5d-3beb-8601-ddab303701cf | -9.48312 | -57.93184 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5375790d-4ccf-3700-bf8a-6a95a71ce15c | -9.48281 | -57.93282 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f6f1de2-1c12-3cfb-86ff-f74da89865e0 | -9.48126 | -57.91963 | 2024-10-08 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d89ca67a-da50-3e07-a680-71a2cecffa7f | -12.47657 | -57.66493 | 2024-10-08 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f03e7b8-552e-383d-881c-91c1a17cc6f8 | -12.47245 | -57.66822 | 2024-10-08 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9177bbb-83a7-3a73-869b-18d019effd67 | -9.21208 | -59.37548 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbae5ace-df1e-3a32-a99d-bf4efdacecf8 | -9.10848 | -58.99381 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd36413d-3b7f-35e9-a364-59ae6c97b72f | -10.2172 | -59.40358 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5500d005-05d0-3785-920f-09abab459b84 | -9.51811 | -59.50787 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25a34a73-3aec-3d0f-8de5-51ddf0b09b82 | -9.51415 | -59.50718 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0d97991-819f-3334-b568-22475836503b | -9.44872 | -59.02033 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9abea7d5-de77-3abc-8fa1-0834e23ef348 | -9.44077 | -59.04374 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9d6fcd1-10d0-31c1-a34e-df6f2ab7e990 | -9.43692 | -59.04308 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9fe629d-bc1f-33eb-a3f3-1463e9aee3f5 | -12.31167 | -59.18027 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86e2ca54-93ee-3299-8015-224372e73a6b | -12.31063 | -59.1826 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cccd55dc-5f00-387b-b784-81ae940d109e | -12.29495 | -59.18455 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5fd4895-3e94-30e0-95cc-86280e0d77cb | -11.71021 | -59.14284 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a803ab1e-64cb-33b3-af1d-3310ddb032d1 | -11.49037 | -59.09377 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 424c8061-a95d-3894-8284-096112514e39 | -11.48958 | -59.09831 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 080d36ef-6dad-3285-ab7c-b856971bc88d | -11.48583 | -59.09766 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd00d1ea-2116-3d48-8bc5-0806d106b6e9 | -11.36847 | -58.99451 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6938276b-3215-36f7-a2cf-22a9c65d8bb5 | -11.36727 | -58.99651 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55bc1d78-e5b6-35c6-a279-c2fb63454e24 | -11.3419 | -58.9872 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2159b6bb-14d3-31a6-be13-ab4ea56e7465 | -10.98178 | -58.96833 | 2024-10-08 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d30af63e-47af-349b-9936-f49c60517a91 | -7.13344 | -59.29649 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bc2e59e-8cf6-3279-ad33-887009d58d8e | -7.13284 | -59.30005 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de2284ef-655c-37c7-ac26-6f702c22f77f | -7.06952 | -59.52386 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b71077fd-adc2-3168-8764-62edf936f9e7 | -7.06648 | -59.45272 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18257cdf-e467-3fbf-9bea-186f6e003b11 | -7.06588 | -59.45639 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1bbed69-0b79-3613-9c41-d30053086b06 | -7.06505 | -59.45164 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ce87ff0-5174-3dab-bc27-9da58aa81b60 | -7.06442 | -59.45531 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a38c7b4d-987f-3697-969d-f275a81cbfa4 | -7.06239 | -59.45203 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2568ff94-a21c-3317-b6d1-d404a740f245 | -7.06178 | -59.4557 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6c9f867-e300-30ff-8459-81ea1b284dc2 | -7.04042 | -59.40709 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e742deb-f21e-36d1-9ffd-de93596c1ac3 | -7.03694 | -59.40276 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77afc3a1-0bd3-32fd-9fdf-6b3d07c5ee19 | -7.03633 | -59.40639 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd0b2b0f-63c6-3e62-9d7d-9e958ed4e33e | -7.02755 | -59.40866 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c936dedd-6d39-38cd-be5a-daa4d326ca59 | -7.02407 | -59.40435 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35c0b233-fef1-364f-b270-9143d4c2dbe9 | -7.02346 | -59.40799 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3069725f-6992-3377-b126-a40fbffa7985 | -7.01937 | -59.40731 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f530ca3d-0e57-3a4e-96f2-ca9ab9bd91f8 | -7.01876 | -59.41094 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6e63a32-fe0b-3cc7-8230-79eb10e4e3a9 | -7.01529 | -59.40662 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92567cf1-73c6-3313-87a3-49752be7e29a | -6.73485 | -59.63405 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a66016a-71e2-3a93-b296-37686db0a59b | -6.73421 | -59.6378 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b13d6d0b-9093-3b4b-952b-c9e500fce8e6 | -6.67788 | -59.48206 | 2024-10-08 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a456f261-cdbc-3cb3-a928-b5fd91f0057d | -9.24308 | -60.43829 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbdb438e-77e1-3ce5-8670-308a2ae60efe | -9.2397 | -60.45795 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97922f84-8191-3087-be1e-9487a2f768c7 | -9.12435 | -60.39788 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52b13c9e-2ff9-3744-afb8-421bfd6f17b3 | -9.12368 | -60.40177 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README88.md)
