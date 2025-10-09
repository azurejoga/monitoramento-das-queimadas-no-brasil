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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 715fbf3e-5ac9-3ed3-a693-8735dcb873bb | -18.063 | -44.48175 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0d34aa1c-57fa-372f-9fe6-97c9635e03b8 | -11.98145 | -45.21779 | 2025-10-09 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd58697b-37fa-3c4b-8d30-11e60a3fe234 | -15.78219 | -46.24754 | 2025-10-09 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ff91590-f628-3c35-94e3-5b15a7402572 | -11.47488 | -43.47818 | 2025-10-09 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8eeadfe-1a2b-3091-b9a5-293826f4b351 | -17.98004 | -44.96441 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9c233bc4-a5fc-37d4-93a2-8e00a437990a | -11.78454 | -45.15601 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 04fe82d6-986d-32db-bd7b-40bf26097e26 | -11.74844 | -45.14269 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f9ee48d-69d9-3ed4-9691-1c77b62cd7d7 | -17.39602 | -46.89346 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcb07394-0619-3050-ac65-865d895c6b4e | -11.79389 | -45.14176 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7c0b74dc-17e8-3579-abd1-ddd56da94379 | -13.48265 | -42.02097 | 2025-10-09 03:32:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0b2f54a0-80df-3ff6-842f-313482bcb198 | -17.99393 | -45.62292 | 2025-10-09 03:32:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b7855beb-124e-3d15-a2eb-34572e86db20 | -13.78236 | -44.34858 | 2025-10-09 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 554ce240-366d-3016-a614-1609b0f81375 | -12.829 | -41.03183 | 2025-10-09 03:32:00 | NOAA-21 | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e1b80a3-82bd-3d25-979a-f8ba57107fc6 | -18.41426 | -45.24218 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 0f5af1dc-f34a-37d9-99f6-c9e359e2bb7f | -17.95402 | -45.00698 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c2c0f117-0936-3c0e-a582-f5284a36433d | -11.77489 | -45.0519 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 937b45f6-ef27-39de-8e72-9e89d1189191 | -15.55901 | -45.31855 | 2025-10-09 03:32:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f25c99ee-5b94-3ac0-bf1b-49be3e37b7e6 | -18.06897 | -44.41807 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca62098c-2e7d-3365-b0c9-ceaf63e203ed | -16.28409 | -47.13998 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd217c7e-e3b6-3bda-b810-6589c2ecd85e | -16.61635 | -46.77574 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4a75c46-a173-3d90-9549-436c6ad4658f | -13.79114 | -45.84222 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a4ddf5d1-5984-3ef3-a809-e18872722e21 | -16.37142 | -40.75175 | 2025-10-09 03:32:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ace0da78-6ca4-3055-a2c9-e1ce15300478 | -11.79357 | -45.04789 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06e83489-1758-3037-8a2a-2f404bb4b6db | -18.40085 | -45.25064 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b220a5d0-35c2-3232-948f-8258fbdc16e0 | -18.30275 | -45.43381 | 2025-10-09 03:32:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71256269-9ee9-398f-ac93-1c2af320c69a | -11.87523 | -44.92801 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f103c38-68ec-3226-82f8-0951643b2fe6 | -14.97694 | -46.29742 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b12ebe72-cd95-3e0c-be5b-79c732ba9748 | -18.03446 | -45.00581 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6d304be-2196-36ae-871e-e5d9d512176c | -14.43888 | -47.51037 | 2025-10-09 03:32:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2996b2e4-10ad-30b8-9ab3-fc6095e5f191 | -13.8276 | -45.82387 | 2025-10-09 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76cd6327-2416-3892-90c7-7f39bbb4ac2d | -13.13001 | -43.90647 | 2025-10-09 03:32:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c2529a9-22bd-3c6e-adac-e14866f20867 | -13.7922 | -45.83718 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4c844af-b18d-346f-b74a-832c5eb28065 | -15.06009 | -42.33142 | 2025-10-09 03:32:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d10febe5-5266-330a-904b-cc8d2fd385b0 | -15.29763 | -46.18298 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 07d69e35-8736-3aad-9cb8-0ab7bfabbce2 | -17.53453 | -46.75834 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54c43ad8-1068-33dc-abb1-27c41a509319 | -17.9892 | -45.6171 | 2025-10-09 03:32:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c1669e1e-9cfe-32ec-a186-1d0a42c94a65 | -17.38281 | -46.89408 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 813d2ce9-9145-35d2-8b81-98e661b07a74 | -11.75573 | -45.13868 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d4528d1-5223-335f-a5a8-a2b2c0f90462 | -17.65576 | -44.43994 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86de90ea-b113-3c54-9848-c446cd7b611b | -18.30002 | -45.43194 | 2025-10-09 03:32:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2beffe35-e519-3986-9ba9-9f5d9aaf9297 | -17.95024 | -44.41985 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cb076b5-0c40-3748-8710-31e4b94eec46 | -14.42148 | -43.9873 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 91af12c7-5367-39f2-a753-1bf304061a30 | -11.72738 | -44.30271 | 2025-10-09 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 266d023b-f2ad-3639-89c1-9e987dfb31be | -17.89582 | -44.25762 | 2025-10-09 03:32:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09ad7891-350e-3e96-bc8f-b58988213c17 | -18.08715 | -44.46291 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aa5da03-7e2d-3b07-853d-55a194e6987d | -12.0524 | -43.50261 | 2025-10-09 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c76fa51-1e5d-3c66-a927-1c6bf8eff0c7 | -15.81551 | -43.78046 | 2025-10-09 03:32:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f3924667-c5f9-349d-8749-51cc8ead9a3a | -13.79947 | -45.83368 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f84e98d-abaa-3e9e-9ec7-0f41703e4ab6 | -17.89042 | -44.26145 | 2025-10-09 03:32:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e269790-0955-304b-9f1e-4c3e248f2bc5 | -16.28529 | -47.1345 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b47c0356-6c1c-34f3-bc56-016e8ee3090e | -13.7984 | -45.83875 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15c434d7-dbaa-3e06-92ba-5ac0f85b630b | -15.22732 | -46.36823 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3fc68ac3-3946-3211-81ba-de194d906eb3 | -18.64475 | -43.91409 | 2025-10-09 03:32:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 492f1835-79c9-368c-848d-e929a0cd2acf | -11.9835 | -45.20773 | 2025-10-09 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 937fc90d-0905-3ee3-86f5-34f02aadd334 | -16.75076 | -43.97864 | 2025-10-09 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 2295fa86-0a3a-3c88-aa17-b0b27f16d02e | -17.65116 | -44.43525 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02c3a9c5-cd4f-3cc5-9d18-2aac561688b9 | -17.21879 | -47.65407 | 2025-10-09 03:32:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3b5e9d54-2df1-3659-a7c5-6d70e9b54385 | -16.07924 | -45.78886 | 2025-10-09 03:32:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2560bfe-92c0-3668-bde4-404b26a6fd42 | -17.16012 | -43.43353 | 2025-10-09 03:32:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4301aa8f-e03d-36e2-b045-eafaf48a9ec5 | -13.81914 | -45.83315 | 2025-10-09 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e156c879-0d77-320b-a6a0-188bfbe11e47 | -17.3753 | -46.89845 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf7990a-3f55-3470-9087-6a5fada46627 | -18.05228 | -44.94844 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce5fb1a2-3f1f-3fa8-8dbf-aa429db9f806 | -17.95484 | -45.00304 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e4801d4c-3168-360e-ba53-4783f26d826b | -18.04334 | -44.99093 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa4723b0-a2df-38bb-a038-afed6c0fcdb1 | -11.86321 | -44.92439 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 702bc099-dbf8-362f-a840-e35e05f8a530 | -15.2359 | -46.35885 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b56deec3-88fb-33e2-a9db-e184e56260f7 | -17.5284 | -46.75682 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b1d0056-2b90-3a9c-ad7a-97d6037b7ace | -18.04827 | -44.96752 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d77cecf-0e1f-3e35-a799-724d2a365524 | -17.95562 | -44.99931 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9e78dbff-50b0-3782-80bc-55f3218d7dd8 | -18.03391 | -44.98116 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a23e1115-3ceb-3b49-83be-0f10b6067a6c | -17.38566 | -45.05776 | 2025-10-09 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 104f6175-19c7-35dc-a41c-2e1362af7afa | -15.29663 | -46.18755 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 77de2ea5-3cb4-30c8-a151-fcadb131f4d2 | -17.951 | -44.41615 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f3fdd28-263c-3c4f-8081-2b921d558882 | -16.74936 | -43.9786 | 2025-10-09 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a784d4d0-a05c-340d-a5ee-f0f22cc7f1dc | -18.05372 | -44.96884 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 578de9d3-6d7b-3b66-9e10-68c8efc9d9bc | -14.93355 | -46.78911 | 2025-10-09 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 55cd2f88-56e4-3d2e-abbe-9afa2d3f0771 | -11.79451 | -45.04324 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98951333-5843-3101-a508-1e1e0ef6bfda | -13.79099 | -45.87385 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 401cf3de-8a17-3c5b-86c7-936c585dfbbb | -16.74677 | -43.97116 | 2025-10-09 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 39a3341b-b8b6-3c19-a9ed-ecca58606556 | -16.6238 | -46.77183 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9c89603-7354-333a-8acc-95bf49a0be10 | -16.28452 | -47.13896 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f4bef90-3043-36f2-a1bb-d6bddc60fce9 | -17.95708 | -44.41357 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20257967-31c8-33f6-a483-06f4e4bcb011 | -18.41046 | -45.23283 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9830d356-cb5c-351b-8974-d340f2df1796 | -18.09325 | -44.4603 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e62447f3-8803-342a-b1a2-8ca76b236087 | -16.39675 | -46.35528 | 2025-10-09 03:32:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a696ded9-b855-38e9-83b6-367a4e3d8403 | -18.05148 | -44.95224 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d846d232-6301-37b9-9400-8ae9ea8614c8 | -15.389 | -48.05977 | 2025-10-09 03:32:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2d6679a2-8ece-3a2b-a86e-54bfce4ae39f | -16.28574 | -47.13358 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f67cc492-2da2-30d2-84f5-6bd367f55548 | -17.33162 | -42.137 | 2025-10-09 03:32:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 327a7260-5c05-3cf1-bd40-606179b79cea | -13.61912 | -44.43895 | 2025-10-09 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67b16e07-d02e-3523-aa52-19e09447d183 | -18.24851 | -46.99776 | 2025-10-09 03:34:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b85dfd21-4a60-3d09-9fb5-5a3b288b82d1 | -20.11961 | -49.53773 | 2025-10-09 03:34:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 15b53ae0-3915-3e91-ba73-42d811c056af | -18.3968 | -46.87733 | 2025-10-09 03:34:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f803788-9b1c-3a89-9907-05ab92ddd1e1 | -18.99422 | -43.08699 | 2025-10-09 03:34:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 64f04591-03c1-3f5b-9291-a296d6fe2257 | -19.50376 | -43.83519 | 2025-10-09 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51cadee7-5709-32ce-930d-5b7e3613a4d3 | -18.99319 | -43.09198 | 2025-10-09 03:34:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 334fd46b-c93f-351e-a1ee-4520bb4dd1c1 | -19.71926 | -44.00021 | 2025-10-09 03:34:00 | NOAA-21 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c102885-a898-37ab-91f6-4026a3375a99 | -18.5436 | -45.06524 | 2025-10-09 03:34:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25de7891-cb5f-3beb-88c2-046c2d52ab8f | -20.11284 | -49.53578 | 2025-10-09 03:34:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 0642dc15-4601-3e7a-993b-4bd98b8934dd | -18.00344 | -48.32253 | 2025-10-09 03:34:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README16.md)
