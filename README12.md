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
| a9e64ff3-3855-3d37-8708-acefa3927f0a | -12.04858 | -45.76659 | 2025-08-11 04:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7096f0e-e3f6-39e0-883d-b368e57aab58 | -11.71015 | -50.10869 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03580209-3b37-3afb-9b3c-26c8093261d5 | -11.77622 | -47.39814 | 2025-08-11 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75a72e8b-b181-3c26-860c-f90149d5d791 | -11.69075 | -50.12509 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13306e26-ceb7-3f69-a037-8130bcc2a4c2 | -8.787 | -48.3545 | 2025-08-11 04:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1226745a-bb49-340b-9e55-6e8f44072b2b | -12.04554 | -45.76081 | 2025-08-11 04:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 616c7d8c-4534-3aea-958c-c24971e258fc | -13.60977 | -46.92979 | 2025-08-11 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4104f07c-a598-3ddf-9551-ac41ae552064 | -7.66398 | -43.84199 | 2025-08-11 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcd0c746-e2a1-3733-a320-b9ebb2bdf74c | -9.2155 | -44.5288 | 2025-08-11 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 032e8072-cf21-3f66-9339-08976f8ba4df | -10.37065 | -50.81671 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a79c5ce-6d24-3c6a-990f-240dcf96ee14 | -12.60739 | -47.14561 | 2025-08-11 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8df90efa-62ad-3a18-b713-70c728d8989d | -12.08285 | -43.36321 | 2025-08-11 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67e31309-497f-3cda-9bc6-802f24b35461 | -9.86914 | -43.54877 | 2025-08-11 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af3f93a9-ff72-35ad-aca2-c3e63470bb79 | -7.87474 | -44.97394 | 2025-08-11 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a0fc474-9c46-3037-b762-f146d936642a | -11.93346 | -41.66588 | 2025-08-11 04:04:00 | NPP-375D | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ff4be687-a9ab-3689-b3fd-7b40db2f258f | -12.70719 | -46.36397 | 2025-08-11 04:04:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d58935c-42d1-3f07-b94d-b77298c77d93 | -7.61842 | -45.19049 | 2025-08-11 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f109bd9-bc63-32b8-9ac9-21f1af1b6c19 | -8.56584 | -54.67578 | 2025-08-11 04:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8525d8c5-25d7-37c9-995d-36870fe213a0 | -7.61377 | -45.19342 | 2025-08-11 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64c9cf9b-711f-3b06-a474-0bc1e98d7dbd | -11.69014 | -50.12836 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 543bbacb-997d-37e1-bc8c-077a2d3e56d1 | -7.87407 | -44.96527 | 2025-08-11 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 714a2036-2a16-3cf3-adc7-832f9d9ff855 | -9.30314 | -40.22248 | 2025-08-11 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bafaf5a9-706b-3bf1-87e1-f10833a75553 | -9.64162 | -43.83477 | 2025-08-11 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4351db31-c37f-3a93-b525-2212a6e43f6f | -7.61435 | -45.1899 | 2025-08-11 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| da14bbd5-24ea-33d3-830b-5c47ae483421 | -12.70657 | -46.36752 | 2025-08-11 04:04:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa6f53e6-aae1-32de-95ea-2062485b276f | -7.66026 | -43.84133 | 2025-08-11 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a64a1cb3-6d26-3383-8a18-a39d631cf903 | -10.36291 | -50.82682 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d0a5054-666b-3540-aad0-59708ef01740 | -14.68044 | -42.51387 | 2025-08-11 04:04:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 13f0a2cf-7c90-3374-8cdb-fda97c74a8d3 | -13.80054 | -41.20167 | 2025-08-11 04:04:00 | NPP-375D | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9f5b949f-6119-3685-9b6e-3801aedca604 | -11.71469 | -50.11002 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b766c433-67a6-3313-b6f0-73c917e75add | -14.11002 | -45.39516 | 2025-08-11 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 633cd93f-f4d1-3bbb-a327-3877d69a71d5 | -11.75289 | -45.03123 | 2025-08-11 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e2f741c-531a-3ab0-bcad-b05293727c66 | -14.12332 | -45.40699 | 2025-08-11 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4834ad4-c73a-3c97-85df-5586c79e58c6 | -14.48096 | -47.07304 | 2025-08-11 04:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70ef8f3f-9471-395e-b503-ec82337286fa | -11.71596 | -50.10351 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4173b55c-4f38-3b42-8997-10f3cca25e9e | -11.77668 | -47.39549 | 2025-08-11 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ce0e77c-af3b-377f-822e-d3f47ed8a7ca | -7.22065 | -46.25159 | 2025-08-11 04:04:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83d57aca-ed1c-337b-b0a2-baede3b2577d | -7.61902 | -45.1869 | 2025-08-11 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8b169623-d5a8-394a-ac37-e616232f47b0 | -9.2071 | -44.53223 | 2025-08-11 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b03a3a10-2838-3bfe-ae9a-e1aedae52383 | -10.37207 | -50.80914 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b753b9e-fe30-3303-aa17-565e12b53b8a | -9.21091 | -44.53286 | 2025-08-11 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d2ffaf3-2110-394d-850f-05673aff3e38 | -11.77701 | -47.39387 | 2025-08-11 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cd6bbe7-8864-3690-b064-5ca7fb4c0819 | -13.61806 | -46.93093 | 2025-08-11 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff65f408-c3eb-359c-8756-6a3518821d4f | -14.1132 | -44.88239 | 2025-08-11 04:04:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| caac0cec-d0fc-3b39-ba49-3a430d4b3ce4 | -10.30945 | -48.11123 | 2025-08-11 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2480ada1-549a-3d90-acff-af2abe8c3289 | -12.578 | -41.27441 | 2025-08-11 04:04:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2e608f3e-2716-3a6b-8b9b-e91261bff923 | -11.77907 | -44.94501 | 2025-08-11 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d087ffa-e1c2-3be4-8d02-7bdf52656962 | -18.61668 | -46.86005 | 2025-08-11 04:06:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9eed80b4-58a8-3c92-9a44-5499ed246e3c | -19.77233 | -42.09932 | 2025-08-11 04:06:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 3abd27f9-6e5f-3b56-83c2-39e3c7e49a1f | -17.23141 | -46.95363 | 2025-08-11 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64cae66c-fd5f-300f-8484-2dcf4dab0f1f | -19.82158 | -47.97839 | 2025-08-11 04:06:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51bf192a-22cf-3bac-ae7b-e7af6758353a | -18.45979 | -45.89956 | 2025-08-11 04:06:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be8d108d-de2f-3026-a2ba-41f580d3542d | -18.79248 | -43.87602 | 2025-08-11 04:06:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ba5b3c5-b3c4-3da0-b7a2-31e822e60ad1 | -17.85881 | -44.4186 | 2025-08-11 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d580dd92-6f2f-34e1-a401-09b33df60a90 | -18.71938 | -49.16154 | 2025-08-11 04:06:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50f024ef-0055-3296-a705-7cfa13c2f214 | -16.30847 | -52.92038 | 2025-08-11 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 448f12e3-3825-3017-bd7b-9bc51c7459cc | -17.92416 | -42.89011 | 2025-08-11 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f08d16c-9f85-33f9-8ae1-7a2cbc7da767 | -19.5512 | -46.58557 | 2025-08-11 04:06:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd28ac57-a43d-3341-88d4-ae5dcfd0a7b9 | -18.93491 | -45.73137 | 2025-08-11 04:06:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4889db14-e29b-368a-b232-4cff31e27022 | -19.60726 | -42.62353 | 2025-08-11 04:06:00 | NPP-375D | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5b8ca899-ab57-3d6a-acb9-518d6a90b5c3 | -17.80739 | -42.92269 | 2025-08-11 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8a89063-8056-3523-a30e-ce3e50332a8e | -16.29324 | -52.93555 | 2025-08-11 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38d0f6ed-61f9-39d8-88c5-d3fc55b65361 | -20.60485 | -48.87962 | 2025-08-11 04:06:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d44971f2-e3ad-3448-a0e1-ce8de051f65d | -18.05126 | -45.2397 | 2025-08-11 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 82e46ac1-4b8f-3c69-83be-f3c15d0a1cfa | -19.73084 | -48.99802 | 2025-08-11 04:06:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a24b39e6-a3d7-3b67-8ce6-2db27df7e1df | -20.95864 | -46.95019 | 2025-08-11 04:06:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 748dfffc-7e7f-3ab3-9851-df139b729519 | -19.42048 | -43.37027 | 2025-08-11 04:06:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae22d62b-5824-3dff-87dc-72fd0c7858d4 | -21.15091 | -42.91032 | 2025-08-11 04:06:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0656f4d4-99e9-3e4d-a333-0324d87e0b44 | -17.80074 | -42.92152 | 2025-08-11 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfb8bd18-8724-3d41-838f-4045eae185fc | -18.17393 | -47.01332 | 2025-08-11 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 593d9153-10ca-3fcc-a496-893652190081 | -17.22757 | -46.95265 | 2025-08-11 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1111484b-040a-3953-b82d-dda73c84d08b | -20.86376 | -46.64079 | 2025-08-11 04:06:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7d8ad37f-e0f1-3e11-bb9a-c31e321c3a69 | -19.42107 | -43.36663 | 2025-08-11 04:06:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6095ec96-ff7e-39eb-aefb-5726bbe04449 | -18.0348 | -44.45919 | 2025-08-11 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61410b59-0026-3f7e-8508-80a675d80c72 | -18.96965 | -44.84225 | 2025-08-11 04:06:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24e71b0c-8c24-303f-8656-d44d086b5603 | -18.79521 | -43.88044 | 2025-08-11 04:06:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 306d96f2-b00e-3bf2-9b04-cacee2596ee4 | -19.42165 | -43.363 | 2025-08-11 04:06:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75ab943c-fbe6-31b2-8f63-daa532bd2a91 | -19.41531 | -43.36614 | 2025-08-11 04:06:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fda82337-ee74-352e-9cfa-953177275aa7 | -19.41714 | -43.36972 | 2025-08-11 04:06:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fdafea2-2b9a-3990-9604-4a057f0442ff | -17.96191 | -44.28623 | 2025-08-11 04:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eddd9c63-f52b-3d76-83b4-c9617e3421bb | -16.28747 | -52.93434 | 2025-08-11 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36fd43b4-4d43-3999-8ade-6b59ed405adb | -16.30745 | -52.92527 | 2025-08-11 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 602af0d0-a5d2-3c23-90f2-01e240def1b4 | -18.00737 | -43.48283 | 2025-08-11 04:06:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6afa6069-9915-33b4-954b-8e0178337cb1 | -19.16628 | -44.52849 | 2025-08-11 04:06:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96e94fde-acbc-3fd2-8915-10cf553bc433 | -18.62045 | -46.86081 | 2025-08-11 04:06:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f73d5154-360c-33c2-b55d-1fadd25681ec | -17.747 | -46.17877 | 2025-08-11 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4febd5d9-c2d5-3b06-9454-66af48c4b8bf | -17.22661 | -46.95792 | 2025-08-11 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d08871ba-c46d-3665-b923-a28901ea6832 | -19.55855 | -46.58707 | 2025-08-11 04:06:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df07c007-192c-35d5-affa-1c8cb7d5e921 | -18.30214 | -43.9636 | 2025-08-11 04:06:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27f3773e-3914-36f3-87ba-de2e77c2b234 | -20.6056 | -48.87562 | 2025-08-11 04:06:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74da0be3-904a-340d-b00b-3cbff5fec339 | -18.6129 | -46.85928 | 2025-08-11 04:06:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 04be1e6c-9a62-30c0-93ab-98f2a231f317 | -17.80015 | -42.92517 | 2025-08-11 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a511c691-5f09-3c68-bafe-0404b61db2be | -19.67181 | -44.87509 | 2025-08-11 04:06:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 31c6aeb0-9f25-30e8-a67c-2f5ae8a8395b | -21.15149 | -42.90661 | 2025-08-11 04:06:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2845bbe2-28a2-3647-ac08-79a05f3f02e5 | -18.03544 | -44.45533 | 2025-08-11 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b7d1cd2-ef96-30b4-8ff9-ad1dc71e1f60 | -19.68516 | -43.84667 | 2025-08-11 04:06:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20e83018-83b5-3a11-84a9-068516574c8d | -21.85194 | -41.32801 | 2025-08-11 04:06:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1fd597ff-2a99-32e4-9a60-8b19f5bbac7e | -19.22028 | -46.80512 | 2025-08-11 04:06:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48bdda57-4f2d-38a7-a997-69494e140e17 | -17.96254 | -44.28244 | 2025-08-11 04:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f62f4008-a7a9-3402-8c44-8abad163cdd9 | -20.64817 | -48.69448 | 2025-08-11 04:06:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)
