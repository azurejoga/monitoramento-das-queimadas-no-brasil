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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12173fcc-876c-3e76-b7cb-cbea26838cf2 | -13.43317 | -57.02163 | 2025-08-24 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 039a8e3b-59ab-3b23-b162-4c81c1e5f9e0 | -14.33198 | -58.59329 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 013af99d-4b47-3909-a7ad-bfa6c440bc7a | -9.00749 | -65.70269 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5bcb3b4d-2c1f-3c35-a211-0c7863fbbeaa | -16.51763 | -46.73156 | 2025-08-24 05:01:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0df72c36-45a4-32f8-9f45-aaf90031c709 | -13.14023 | -44.90408 | 2025-08-24 05:01:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dee1c9e-7811-37ce-9308-08eccf5b46d4 | -9.00832 | -65.69827 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ac0574ff-9d50-3baf-94ae-d166f009e687 | -11.53234 | -51.85206 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 9ce3014e-d951-338b-84d3-1716aa6c1e7a | -17.60558 | -44.29536 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 8e892225-433e-3cfe-9b78-c11c366ed132 | -11.79122 | -48.78727 | 2025-08-24 05:01:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 015a0e52-3787-3a5b-bd50-f2bd19861752 | -13.4996 | -47.03292 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0175cc55-d7cb-3db8-820b-2e2c390ea65f | -15.0711 | -48.52909 | 2025-08-24 05:01:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 490985d7-f661-3ba4-9ede-e5991bc85ff5 | -11.93598 | -46.73057 | 2025-08-24 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 151174a8-4e22-31b2-b680-54ac909596e4 | -9.95347 | -60.1956 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e4f8274-1f90-3af9-8e64-7748fcaa4d87 | -9.64936 | -59.64063 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5ccd122-d4e7-314a-a53c-b3bf422e4dc8 | -15.52972 | -54.7483 | 2025-08-24 05:01:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ebdc6c8-ed79-30df-a3b2-dc3e407e1d13 | -18.39786 | -46.85243 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22bd02a4-6a66-32f5-9822-ffc00ac6fb3e | -9.95665 | -60.1773 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58b41ae8-7988-3503-87c1-4aea6a8dffb1 | -10.42111 | -64.42933 | 2025-08-24 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ddfc4d01-7290-3e6e-925f-c4cb66cef4ee | -16.79857 | -51.35507 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b9e89e36-2035-345e-b7e0-56c8c70d0700 | -9.96075 | -60.17802 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48351fb8-7f02-30ba-827a-32d076ab76d1 | -9.51875 | -60.55771 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 93a8279d-fb30-3475-a562-5e0154372402 | -9.02725 | -65.70686 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6659ec1d-8fb1-3ae5-b66a-7ce83b1f580b | -14.28259 | -60.37678 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed56b5c7-9848-3eea-aa5c-8163e49c6001 | -9.81484 | -64.26936 | 2025-08-24 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ac5853c-98b7-3cb5-9eda-a208cd987cd3 | -11.51454 | -51.87132 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b6141e5-1264-382c-b875-070da9353f0a | -9.03062 | -65.7217 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a0f31875-baa2-324d-bd2a-750a1fc73c43 | -11.52588 | -51.92134 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fea372ab-8894-395f-acec-0b51fd35d2f3 | -13.17206 | -46.91966 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa27cfb3-86e8-343a-854f-f542b6bec218 | -17.6046 | -44.29485 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0eb33d14-eac2-32ea-bd82-a0212365eeb6 | -9.02465 | -65.72041 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb0e374c-9fea-3378-85d5-3746254aa5de | -11.17977 | -55.03329 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08c82fe2-9c31-3b57-8dfa-b4647cd3815f | -9.01188 | -65.69001 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2626f5b3-54e8-3564-b9a5-14237f2c22e2 | -11.18476 | -55.02327 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c9c42b4-578d-3da2-9571-4ea8f15ce663 | -13.04979 | -45.22613 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6205612-ec1f-3b38-be3d-da65084e9065 | -12.48773 | -53.82278 | 2025-08-24 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d5522e6-68c3-328e-b514-4bdc7143409e | -9.80306 | -61.20825 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e97eb58a-dda2-31a6-b26d-bf83dbe46902 | -9.50927 | -60.51125 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8330924c-4f4f-3225-bcdf-72776a8fadde | -11.18805 | -55.02386 | 2025-08-24 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 085cc889-026d-3a1b-a8ef-0380d7482d7e | -15.65012 | -52.71295 | 2025-08-24 05:01:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51cc2a85-b527-30b4-a0a9-0b9c3fb039f2 | -9.01269 | -65.71793 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e1f0eea-7875-3e45-aa4b-a77ed29ad5d6 | -14.3461 | -58.59581 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32dbdc02-69c0-3bbc-8e22-3135d01eceb6 | -15.09389 | -48.65393 | 2025-08-24 05:01:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a87b1a33-2a5c-332e-8a17-42d1ba0bc153 | -9.00525 | -63.63038 | 2025-08-24 05:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c920f02-8f88-32f5-8cda-797efe3120b2 | -16.48999 | -52.55546 | 2025-08-24 05:01:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8844adc9-2742-3bf5-b485-eab11f3ec0b4 | -9.06832 | -65.71942 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a00bcd75-40df-3a07-a7e2-9812781de4b0 | -15.29792 | -56.15613 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8c5bd844-83ea-3085-ab38-f5bd8e63b62b | -15.30125 | -56.15669 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ac147fce-cb1b-34cb-a6ae-280eba2271cf | -14.50653 | -53.09477 | 2025-08-24 05:01:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7968c3bd-b678-3769-9aec-8438ed15ab4b | -15.29679 | -56.16329 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c21d53d4-a6f5-3f3f-854b-95021df7723c | -15.91642 | -52.20733 | 2025-08-24 05:01:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17119594-d9d9-3076-bdb7-cb04dd35d342 | -9.51029 | -60.55621 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1899599c-0bc9-3b5d-bbfd-8a3dd3ab0a02 | -13.17243 | -46.91675 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a2feb0a-9ae0-3455-a34a-6c94e0fc28b0 | -12.73067 | -48.12159 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8fbf058e-45a7-3647-91f5-bb5c7b94d523 | -14.28549 | -48.02762 | 2025-08-24 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cca839ab-11e2-384b-bff8-bef9f7e09a36 | -13.47356 | -47.01529 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e358d9b-7d94-3f3d-90f8-6f349611354c | -13.50438 | -47.03662 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea443e1b-7a6e-3030-ad19-4b24b4fc7f49 | -17.06164 | -47.15153 | 2025-08-24 05:01:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e04e18f1-82d5-3f7f-9f19-5a2f7215b031 | -15.6484 | -53.86125 | 2025-08-24 05:01:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bf0bd8b-8ee0-3b3b-84ba-3ccef33ffe6b | -9.01128 | -65.38754 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c795a937-f2f7-3302-b503-fd0ace6ef5c7 | -12.59449 | -60.36354 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4307e48-42c1-39e3-bf7c-0900950b70f7 | -13.41293 | -51.80824 | 2025-08-24 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02334e66-a515-3494-a8b4-ed5af58dfca5 | -14.80955 | -47.9326 | 2025-08-24 05:01:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c5209daf-1520-3c59-a6fa-4e236927d1da | -9.5181 | -60.50884 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8b0c895-8018-323a-962d-f29ab482e0fb | -9.5174 | -60.51277 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79a4aacd-88dd-34e3-a434-188d88744cad | -11.53872 | -51.91022 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19de5dd8-1c66-30ce-943d-6d6ecb27d92d | -9.82293 | -64.26299 | 2025-08-24 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4c49eed-0731-3af6-a86b-072c4822b46d | -16.79452 | -51.35461 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5d518d7f-bb3e-38f2-baa3-ebacf4892bd2 | -11.70003 | -60.18388 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 096502c3-c0eb-30c6-bb9a-e9a1afe85198 | -15.65525 | -56.43992 | 2025-08-24 05:01:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e3fd676-8c78-3524-9a2a-c840d10a1150 | -14.6555 | -56.57462 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f675c4e-347a-3482-94d1-1a4efc1a03d1 | -8.99297 | -63.63809 | 2025-08-24 05:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5d832f8-38c8-3f48-9ec2-806525e6a427 | -13.05409 | -45.23904 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a842a926-7f85-39f6-a4da-b7b7b1eff7b6 | -18.40469 | -46.84138 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98be4442-1ddd-38b9-8991-600809d89387 | -13.03683 | -45.23678 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e11cd9a3-0d39-3f3d-bb49-4609ab431433 | -14.6719 | -56.62183 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ac43599-0ef6-3440-93bd-479a81aa4e51 | -11.90444 | -47.11485 | 2025-08-24 05:01:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d5eda31-46f7-33ba-9bc1-256d4e6d0979 | -9.01674 | -65.68634 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c9ab941-9911-3b4f-a80f-e36d75edbd0e | -14.36473 | -50.70636 | 2025-08-24 05:01:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0505509b-3e14-3a78-8372-2db1362892f1 | -13.05214 | -46.32703 | 2025-08-24 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ebf6d5e-ebb2-3c27-80c4-40961bb28dbb | -11.18528 | -55.01981 | 2025-08-24 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 273caa35-0e19-38ea-a96c-383ab1afc047 | -14.50948 | -53.09943 | 2025-08-24 05:01:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee205b5c-5fc9-33b7-996f-e32e73504b7a | -14.81938 | -55.97435 | 2025-08-24 05:01:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9186dd5-abf7-3a0e-8bb2-2b678a64457b | -9.03148 | -65.71719 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14c9ce3d-07f0-3635-8a86-cfc0f06078fd | -15.09792 | -48.6599 | 2025-08-24 05:01:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b39487cc-e7a9-3a3a-96b0-eb1ab5e306c1 | -13.36674 | -47.50245 | 2025-08-24 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5970996-b701-37fd-a8de-7e155a0bac98 | -13.05077 | -45.21794 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e245e549-9ad8-373b-9e16-0d9eedf98364 | -13.46314 | -46.8871 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec97d0a1-eb80-3ce0-9d4f-92c2a88faf29 | -14.75856 | -45.37494 | 2025-08-24 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c6a4cce-91a0-3dbe-aa6c-3916ca9120fc | -9.01611 | -65.72318 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b4db730-9de9-3a5c-9cb5-47293a92b72b | -14.77402 | -55.91549 | 2025-08-24 05:01:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fa19438-b1b9-37ef-880a-8edab3470f98 | -13.46795 | -47.01833 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55830d6d-90bf-3d85-a07c-fd95d950e358 | -9.01177 | -65.71307 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b0dd59c4-0db1-343a-a9ce-d4f77cc07234 | -11.55033 | -51.90752 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e764ba7-4a3f-3fba-b8e5-bfdc82cb268c | -9.01954 | -65.71466 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a02b4f9-d6ac-37ae-9024-39a9cc13e435 | -8.99357 | -63.63486 | 2025-08-24 05:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a77d514c-6098-3b20-82cb-3b31e425516a | -11.5252 | -50.47016 | 2025-08-24 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 701a770f-55fe-37e9-bda2-b0a9510c8816 | -17.6046 | -44.30593 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 92bcccae-212e-3660-9854-6aa901fbdf92 | -12.73829 | -48.10964 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da8d0aa6-d725-33a4-8918-9232995c3325 | -15.52632 | -54.7478 | 2025-08-24 05:01:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df3379e1-b73b-3738-90ce-49877dbcf6b3 | -11.52621 | -50.49132 | 2025-08-24 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README67.md)
