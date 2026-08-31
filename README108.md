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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8e3546a-8609-313b-bd4e-e8c28beb0c74 | -19.08026 | -40.07468 | 2026-08-31 16:28:00 | NPP-375 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a0c6f1f0-9e5f-3e03-a67d-e913cf221ee4 | -19.26146 | -40.1721 | 2026-08-31 16:28:00 | NPP-375 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7d55c906-a8f7-3cfa-a128-37b2cce9cc9c | -15.11118 | -48.10352 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3bdac918-36df-36f8-8188-681254bd9337 | -21.23239 | -44.12134 | 2026-08-31 16:28:00 | NPP-375 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 89bb55b0-3975-3569-8e5a-6eb021c6169b | -17.85374 | -52.10299 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| b9ef29eb-1818-3b4b-8460-b84da94ddeb9 | -17.88552 | -52.10085 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 279.8 |
| 19167934-9690-3da5-8c1b-244c5c331e12 | -17.3761 | -44.88097 | 2026-08-31 16:28:00 | NPP-375 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f45b8685-b94f-3686-8639-549afff74edd | -14.23076 | -42.4075 | 2026-08-31 16:28:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 07ca18cc-7a19-36f8-9a89-42f4aa544f4a | -18.21053 | -43.98529 | 2026-08-31 16:28:00 | NPP-375 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6075448b-cf8b-3dde-8206-8a6f0449f079 | -15.94552 | -41.47154 | 2026-08-31 16:28:00 | NPP-375 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 42366912-d52b-3fb2-bd35-33c7fa67c40d | -16.40029 | -39.70488 | 2026-08-31 16:28:00 | NPP-375 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c8aebfc7-0bfc-3177-a614-9a86acd743ea | -14.59749 | -44.91087 | 2026-08-31 16:28:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3387ba4d-cca8-30ce-89c4-4d32ea1e889d | -19.98077 | -43.96179 | 2026-08-31 16:28:00 | NPP-375 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 66e48900-a71a-370a-a5ce-623b63d47ebf | -19.2872 | -47.18702 | 2026-08-31 16:28:00 | NPP-375 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2f6e6537-2d63-3693-bea2-2ec38103b939 | -17.72777 | -44.28602 | 2026-08-31 16:28:00 | NPP-375 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 966ab6c3-b830-3780-bd3b-bf064635a476 | -19.82528 | -43.41387 | 2026-08-31 16:28:00 | NPP-375 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| b030beaa-918c-309e-8ea7-e6bb50b13333 | -17.87674 | -52.19384 | 2026-08-31 16:28:00 | NPP-375 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 34e903fc-cce6-3ee3-b527-929673fe9bed | -15.82627 | -42.61154 | 2026-08-31 16:28:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 97b10272-a0c7-3521-85dc-036ebe21d071 | -20.28815 | -47.84035 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 3ae4e49d-8f47-30cc-9852-b54e32305869 | -14.50948 | -40.17405 | 2026-08-31 16:28:00 | NPP-375 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 7e0c1383-6be4-3639-a966-230507dfdfd4 | -14.70791 | -40.08089 | 2026-08-31 16:28:00 | NPP-375 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ae6b113b-8ea9-3d43-8b95-31fd2b90cee6 | -18.12058 | -51.61766 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ed7ec8c6-a183-3bcf-ac86-834d63313d94 | -17.88759 | -52.12169 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2098bce5-74b4-33d4-8e6d-359efc5573a2 | -17.37545 | -44.884 | 2026-08-31 16:28:00 | NPP-375 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 59b6d826-92fd-3edc-9201-4fa03d6e9ff6 | -14.32043 | -41.34516 | 2026-08-31 16:28:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8099f063-323c-34e5-9949-ac9bd52b8883 | -19.80853 | -48.07629 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c6876101-d44a-34ad-8f46-68f14bc8f5e9 | -17.88179 | -52.10873 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 5d208068-200f-3fbe-813f-2aa43f328bc7 | -18.26905 | -52.70001 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 45150af6-b350-3f30-b7b2-f6e5c71ab68d | -17.7459 | -42.44681 | 2026-08-31 16:28:00 | NPP-375 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6a225015-e50b-3a60-8d60-7442e98af31e | -17.88707 | -52.11647 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e390781e-4751-3f5e-bebe-167104bf883f | -17.86112 | -52.11301 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| d35f1e07-bea1-3954-8b90-77050797456f | -17.8753 | -52.17799 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 38c5be6c-647d-34dc-83a8-566a31e417ab | -15.64448 | -50.10263 | 2026-08-31 16:28:00 | NPP-375 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 32fbbe31-ae81-35e7-8f3c-93c065d30cab | -15.67855 | -45.94765 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 054275e7-1385-3ec9-b098-9bf218c8618f | -16.81138 | -49.09193 | 2026-08-31 16:28:00 | NPP-375 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b6e30c94-f751-31c7-a3c9-9fb71f9dbe15 | -17.94756 | -44.57714 | 2026-08-31 16:28:00 | NPP-375 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 2fed5e84-bf3c-33ea-bb22-7ed953c960a7 | -18.00764 | -43.48042 | 2026-08-31 16:28:00 | NPP-375 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8812a856-b0ec-354c-90aa-9a4db703b7ff | -17.86214 | -50.50328 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 283.8 |
| 407fbf04-ad55-3e90-a9a1-ff7eadde6e6a | -17.83963 | -50.51033 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fb08a68e-ca8a-31fe-9b4e-fa1e7c5b8984 | -18.41769 | -47.96727 | 2026-08-31 16:28:00 | NPP-375 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 98ba94f4-921e-3d65-ae40-453fe1f5329d | -19.75381 | -44.77681 | 2026-08-31 16:28:00 | NPP-375 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1c8d3a64-1841-3c38-a54f-e50874269b37 | -17.54281 | -44.61163 | 2026-08-31 16:28:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 65a9bca4-7a93-3638-8980-f6c7c677cffd | -17.28339 | -46.00301 | 2026-08-31 16:28:00 | NPP-375 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7f30985-ce6f-3f20-917a-eea7d34c84d8 | -17.87592 | -52.11451 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b9a73071-00ed-32cc-85ed-4f5e64654ea0 | -17.85807 | -50.52034 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2819ac4b-c2aa-397a-855f-3a0299d9760f | -17.88083 | -52.09826 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 220.8 |
| fbf0699e-28ba-3b47-b35d-7b2ddd6dc95f | -19.81354 | -48.07555 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f5dcc445-3114-3ae9-8b85-f37cc2141718 | -14.99717 | -48.13046 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b8b2eb08-2e20-32e2-aa1d-7b5bc54cabdc | -16.56458 | -52.50361 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 77a05862-e0a1-30d9-9292-591f7f7463e5 | -20.29786 | -47.83186 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 104.7 |
| bbca9bdf-1cbd-33b9-b8b7-1d53cee94da7 | -19.8357 | -47.9517 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e484f35-fc70-3687-97d7-cc0eb21ed490 | -16.89469 | -40.2155 | 2026-08-31 16:28:00 | NPP-375 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5991bfff-ad71-3e02-b099-b0d4caef6609 | -20.00929 | -40.75011 | 2026-08-31 16:28:00 | NPP-375 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1f38ff25-4ea5-36da-a09c-6fb7bac811c1 | -19.55309 | -48.27325 | 2026-08-31 16:28:00 | NPP-375 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cbec5e1b-773a-3ea1-b7b5-461b4fca3cf9 | -15.65402 | -43.32551 | 2026-08-31 16:28:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6b22e7df-6c9c-3901-a05b-d18597d9944c | -15.82974 | -42.61103 | 2026-08-31 16:28:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1d620a4e-00e4-38e0-b458-65fbdeff72ed | -16.55868 | -52.50959 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 836af2bc-d69d-36d9-80ab-f1eb6ce858e0 | -20.33387 | -46.57903 | 2026-08-31 16:28:00 | NPP-375 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ce014d28-3279-3ea2-8918-8049001839fd | -19.84437 | -47.93872 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 110.5 |
| bb11c27b-0a6e-3b1f-99a7-ffa93284f39f | -17.84633 | -48.75067 | 2026-08-31 16:28:00 | NPP-375 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1cb1e52c-dce8-3ff8-809d-2c5d8a921c67 | -16.2847 | -42.57904 | 2026-08-31 16:28:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 12f4191c-c2bc-3a79-bf8c-6bac96b6e229 | -15.67442 | -45.94816 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 175d0a2a-1edb-3976-a549-32b7c4513e70 | -16.19645 | -49.31816 | 2026-08-31 16:28:00 | NPP-375 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e93ad788-0d19-3370-917d-aa5efdf5562e | -19.373 | -43.44276 | 2026-08-31 16:28:00 | NPP-375 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 90553edf-c022-3353-b6b5-1b4d26bf03ac | -14.68669 | -41.15 | 2026-08-31 16:28:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b892eb43-3d96-3b70-a93d-df3f21bb70de | -16.56506 | -52.50865 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ce5b5aae-6564-39a1-88bf-2a2da84326f9 | -15.18589 | -46.24535 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1563122f-8683-3e11-afcf-d635ffc77e39 | -15.18641 | -46.24925 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 09034212-2303-3ab3-921c-042ba6d68437 | -16.70354 | -49.35107 | 2026-08-31 16:28:00 | NPP-375 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ca87f27-b7eb-3bf7-bb46-0bc41fc90522 | -17.86223 | -52.10478 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 8ef5fb65-d93a-3a56-923d-15cf29607a14 | -18.20812 | -43.85435 | 2026-08-31 16:28:00 | NPP-375 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed273576-6ce2-3793-a8a5-cea2952d3e1e | -17.85231 | -50.52089 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0c73d865-df4a-3ce4-9bb2-4f6f17312c05 | -15.19047 | -46.23813 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cce1b642-a1ea-39e2-b88b-1662da4e9862 | -16.27835 | -42.58422 | 2026-08-31 16:28:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bcb97e41-14f8-363f-bedd-8936a1eda66b | -17.71254 | -49.23293 | 2026-08-31 16:28:00 | NPP-375 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5c8a9ad-694d-38ab-b16e-b8700036ffcb | -15.94055 | -48.0756 | 2026-08-31 16:28:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 003789df-d52a-32e7-98e3-1f1d45de031a | -16.26869 | -39.46537 | 2026-08-31 16:28:00 | NPP-375 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9bd17fa1-15de-356c-b090-4e03b713a0c3 | -18.26028 | -52.73233 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20e682aa-cd67-3354-ab9d-5530afa6d614 | -15.41193 | -39.33953 | 2026-08-31 16:28:00 | NPP-375 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b46afd64-2297-33ef-acec-10d56ffaf5e5 | -14.79939 | -40.67275 | 2026-08-31 16:28:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 49fd4319-421a-3fa7-9be2-8f840a649399 | -17.56514 | -44.71896 | 2026-08-31 16:28:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2fdb9ac9-54b4-31fa-98ee-711821277526 | -16.78812 | -49.25727 | 2026-08-31 16:28:00 | NPP-375 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4aa6d7e6-6b19-3ab2-b2d5-27d166eca197 | -18.85353 | -40.62988 | 2026-08-31 16:28:00 | NPP-375 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 56c21801-8a9a-3483-8994-e930ccaef21f | -15.17734 | -48.71935 | 2026-08-31 16:28:00 | NPP-375 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fd69a50a-5a48-3ba5-9efc-9565cfa7285a | -18.9126 | -50.88111 | 2026-08-31 16:28:00 | NPP-375 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 0f0cc8c5-f236-3ccb-a49d-ab1a492f44db | -16.57786 | -52.50726 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 23982124-89b3-3b46-a813-8b419945e6a3 | -20.70258 | -41.82467 | 2026-08-31 16:28:00 | NPP-375 | DORES DO RIO PRETO | ESPÍRITO SANTO | Brasil | 3202009 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| af3802a2-5cdb-31cf-9749-68b305b4dc74 | -15.08525 | -48.36989 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d983239a-84e9-3eaf-ba77-33055300bb51 | -15.19 | -46.23443 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 257123bc-b457-3b8f-9726-41bf950e6bb5 | -17.72083 | -44.26245 | 2026-08-31 16:28:00 | NPP-375 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 72bf5946-ffd4-3922-9cd6-2ebe1c1954b8 | -14.16391 | -39.97205 | 2026-08-31 16:28:00 | NPP-375 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6f706313-19f8-3d70-9bfc-5e7f184ae511 | -18.10661 | -42.87445 | 2026-08-31 16:28:00 | NPP-375 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 9533593f-453c-3499-9764-529f0e5d68e1 | -15.64538 | -50.09626 | 2026-08-31 16:28:00 | NPP-375 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 80a6d185-7b19-336f-b322-a94a5d9698d2 | -19.38387 | -41.16455 | 2026-08-31 16:28:00 | NPP-375 | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3422a7fc-fa4d-35c1-a4c5-3d416da08f08 | -18.20609 | -43.98104 | 2026-08-31 16:28:00 | NPP-375 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c8cb5fa0-1161-38d1-ae5a-4a61392e1ed2 | -15.18775 | -46.25029 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c704adbc-f7de-35f0-a50e-f755c7edd4b0 | -19.85368 | -47.93159 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 391d3c5e-d5a7-3743-a18a-b34fcc9d0ff7 | -19.36927 | -43.44327 | 2026-08-31 16:28:00 | NPP-375 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 23948f18-21cb-3327-913c-d1e22ed171a1 | -19.81944 | -47.94146 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8ad6b4f5-bba4-3665-bf58-d93fd7911d34 | -15.53342 | -45.91635 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README109.md)
