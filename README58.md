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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3edb16df-e1bd-3669-9f9a-54c5382a5750 | -14.52178 | -48.30742 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1fd247b6-f4ef-3227-93b8-85a09ec1ec90 | -13.42408 | -51.33563 | 2026-09-28 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21635950-39fb-308a-9069-79ba8b2d8299 | -11.10646 | -51.34136 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ef731b1-3f95-380d-8ff9-4a5ae97ed4be | -13.46681 | -48.59008 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 309e37b2-70d7-3df1-af32-b4f68ff03bd2 | -10.40738 | -53.81378 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af0fbdde-f6ec-3460-9156-3f97fd860cbd | -10.81803 | -57.22699 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d1ee517-7e48-3599-a9eb-072fa28df7b5 | -13.10309 | -47.4188 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 07be6a98-df57-3c78-b81e-16844001c4a7 | -12.68803 | -46.98116 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73a6b5bb-3401-39a0-9c28-2759b22c7703 | -13.46813 | -48.60144 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c55787b-4fe6-3a60-b03c-8b3eb5fd125d | -13.10081 | -47.396 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a4d88e32-a18b-3b3f-8c79-81cb6d4e1335 | -10.93647 | -50.67002 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81ee9484-c5bf-3c28-aff3-bde69d03c912 | -13.69216 | -48.81388 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c6cadbc-593b-34e6-8d4f-5e97dba09d39 | -12.7644 | -54.04155 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e5edf8b-fb56-386f-9f2c-5b61e33935d4 | -10.60898 | -53.99706 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6872c1cd-998d-3129-bc7b-92c9c452da81 | -13.15011 | -48.54359 | 2026-09-28 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a62947e1-47c7-3e28-926e-99ef99fc4967 | -15.14943 | -43.61231 | 2026-09-28 05:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 82665b32-1440-3674-8681-6344a1149abb | -10.42033 | -53.81953 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 578d2321-798c-3eaf-9e5f-a42952257047 | -12.71631 | -47.30647 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c8a9ebd0-746c-3127-ab1f-31b5ba044a37 | -12.70837 | -46.98573 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55a71ffa-6a31-3ec3-bedb-1d87523bc9d6 | -11.43926 | -44.9271 | 2026-09-28 05:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 533a3a67-6a1f-337e-b00d-a4c78ec68aa9 | -11.68651 | -44.53974 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfb2f7a9-b0e8-31fe-a443-dfc96f02fa1d | -13.45687 | -48.59344 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42517aeb-dc1b-315c-8f6d-290fbf2fb511 | -13.46959 | -48.60474 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 76e4ff29-ff00-3316-84d5-7e8c63fd47d0 | -13.69616 | -48.81921 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c21df56-0f00-3e20-bbe3-8cffd8b829f3 | -10.7245 | -53.99263 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57cabbec-2ec5-3ee3-badd-77260ec82095 | -13.56137 | -46.35862 | 2026-09-28 05:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1f01390-f1d3-3473-be65-2b7b546e8ae2 | -10.2564 | -57.71804 | 2026-09-28 05:12:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18833810-3658-3abe-9c44-78312c4a8b7b | -10.80048 | -57.20444 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1782cc64-ca25-3669-bd22-276ffcdd1fd2 | -16.21941 | -42.86999 | 2026-09-28 05:12:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8b61971-f0e4-32ec-b3b8-24534be2348d | -11.13381 | -50.05661 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97f55211-1fcb-3505-b7ab-5b1399d5c967 | -11.70004 | -44.52808 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63d6d43d-1c39-3ca3-9afc-39bc0944f0ca | -10.81988 | -60.74478 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3ef2e505-5537-3bd1-8776-f31fcd1f46c7 | -11.01838 | -54.14587 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14e525a3-7c93-31c3-9b72-4c316f17e6d0 | -12.69458 | -46.97095 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df801b8c-394a-392a-8676-cfa61ef95690 | -11.038 | -54.04173 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 546b9ba3-9600-32f7-9ec9-aab005fcd1bd | -12.61998 | -47.31026 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27999da4-2a80-336a-bf61-13e526d76067 | -11.62649 | -46.79513 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d1d727da-7ead-3831-a505-6192b32aee9c | -10.81922 | -60.74861 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2ac0ecfa-3562-37c2-b28d-a46c98a955eb | -15.26555 | -47.62429 | 2026-09-28 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 453b5eb5-56a1-3ee4-9931-3705f08855e5 | -11.4282 | -47.41638 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c026e46b-d6b5-34ee-b295-285e52273ce9 | -11.33402 | -54.11309 | 2026-09-28 05:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 102f4e9f-dbea-38c0-bb2d-95109a22df31 | -13.46873 | -48.59666 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0315806-8fd8-3527-8c38-9b6a87d2f64a | -11.37505 | -47.4416 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 84973dbc-38a7-39da-9ff1-122bccaaab83 | -12.73365 | -47.29108 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1c1555e7-60e3-3b25-adc5-8ce89b40f1a9 | -12.78712 | -54.02992 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96798ec5-89cf-3eab-b84d-bb0c843c3199 | -10.41189 | -53.82935 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fc10c2e-834b-3343-b776-f8e9ce3ff9b4 | -15.40785 | -47.91011 | 2026-09-28 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4ace2f0f-2753-395a-87da-fc1e05a9a6fd | -12.63354 | -47.32403 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| feb36934-bfda-3a95-8e29-455874e36dd7 | -13.725 | -48.8138 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca65a3b4-755c-3750-82b8-3fdc00e69c8b | -11.35466 | -47.43231 | 2026-09-28 05:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a389851-1122-3ec8-bfca-fe3403ae622b | -12.15322 | -50.35936 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbf9ff91-37c6-3139-af28-f05c70060f9b | -15.65486 | -52.67851 | 2026-09-28 05:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 759c928b-6732-3f07-98ab-82a5f21238dd | -12.59456 | -51.96166 | 2026-09-28 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2934e5a4-6409-38c7-a999-f4932d8f3551 | -11.10848 | -51.32753 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a5de7c1f-0bd2-339e-83a6-ee05018b6567 | -11.7044 | -44.542 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88417ede-bb9f-321f-ab44-8c765c03af68 | -13.07988 | -47.44537 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dc0b8607-201f-3796-a4d1-67184318efd8 | -10.8237 | -57.19279 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 886920e3-7052-3a14-92b0-18c81fed8b04 | -15.17042 | -46.16554 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0060e84a-69fd-3c94-bc0f-f2d80186086a | -11.8408 | -50.49725 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 64bb71be-bf5d-3d41-9a0e-7ce09e3c43cf | -11.11469 | -51.33788 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a7be893-ff76-352f-a30f-a2648c274b0d | -9.69189 | -59.21596 | 2026-09-28 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc9768e5-49f4-37cd-998a-6bf529632263 | -13.33283 | -46.8057 | 2026-09-28 05:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 949f6c39-a387-3e06-acba-9ad90581d30c | -14.79005 | -45.94573 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d702676-5200-32b2-b299-f562285a4a47 | -10.81221 | -60.73947 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53e1f521-ca42-3246-b315-a4e4c1eddc3d | -13.45162 | -48.5973 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fa2e78c-0499-3c1e-bbbc-22a5f1b2bb5c | -10.80394 | -57.20501 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 261fa53c-a417-3c23-9da0-0e0d63cf0f62 | -12.17824 | -50.41825 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8942e55a-7cb3-3325-a76b-a4af5e313774 | -10.40456 | -53.80961 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40c57ef3-0a0b-3910-a113-d50e83f48f39 | -15.16697 | -46.1456 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a965126e-2ae3-33de-a027-de965683866d | -14.48458 | -53.63431 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6efdd867-0e38-3507-87ae-ded910ce52b2 | -9.1648 | -61.40853 | 2026-09-28 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| fb6a0277-d4cb-3eba-a036-bc4dfeb8cd99 | -12.13413 | -57.17295 | 2026-09-28 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 869aa7e2-7da7-3acc-abfd-4b7fdad68a95 | -10.41019 | -53.81795 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9837fd64-f53c-3167-9aee-84fd8ce41b51 | -10.41357 | -53.81848 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0c60cef-bef8-3968-a026-6b3334f1a0ec | -9.16927 | -61.40936 | 2026-09-28 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 4847ac30-7fd9-333e-b64d-c000592d766f | -13.4234 | -51.34057 | 2026-09-28 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d1528d6-21fa-383b-b311-050fe8f920f9 | -12.31498 | -46.40336 | 2026-09-28 05:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a67ab096-405d-3fdb-b864-262d09e8b4b9 | -12.14987 | -61.13816 | 2026-09-28 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 832d4bd0-b041-3ca0-a977-312f98817d49 | -15.156 | -43.61307 | 2026-09-28 05:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| be79b011-dc1f-3a97-8469-378df4327d52 | -12.74151 | -47.30962 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 7bde1cc0-08a9-39f6-af21-94bf227e085d | -10.42708 | -53.77598 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa67419f-f7b3-3654-92e0-007228f98234 | -20.35041 | -46.38386 | 2026-09-28 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 172af068-451c-30b8-b97c-c03be2bc26e8 | -20.18389 | -48.58032 | 2026-09-28 05:14:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40fa8666-6ded-332f-a38c-53ab71b94e90 | -19.15333 | -43.83327 | 2026-09-28 05:14:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8aee80a1-6f73-3edb-89ab-d31f3898e4b5 | -21.52597 | -45.11244 | 2026-09-28 05:14:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e0ad180e-85d3-3862-acf5-55ac75790ce1 | -18.10961 | -44.37657 | 2026-09-28 05:14:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 542122a8-fee9-3d59-b4b4-efb9fd440a60 | -20.20024 | -48.57278 | 2026-09-28 05:14:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8dd8c9ef-efb4-3090-805f-973fa1de4728 | -23.32403 | -52.31243 | 2026-09-28 05:14:00 | NPP-375D | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9494154c-4dcc-39b7-a4e0-91b2d835fcce | -19.14663 | -43.83188 | 2026-09-28 05:14:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46105038-fdca-3849-b457-99c601e4d703 | -18.10855 | -44.38781 | 2026-09-28 05:14:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 397d6c86-a3f5-3aa0-bb0f-c5147b893c9e | -17.83288 | -44.4002 | 2026-09-28 05:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 829b920e-e630-36c4-907c-6169234ad71b | -18.1036 | -44.37072 | 2026-09-28 05:14:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db2ec522-08d3-3414-a5b7-52efbbe48f34 | -17.83931 | -44.40132 | 2026-09-28 05:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7c8e31c3-85b4-379c-a686-69fc10495515 | -20.83524 | -57.69707 | 2026-09-28 05:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ea4e8e21-c48f-36a4-a3ab-4208c0717f82 | -21.02412 | -47.26193 | 2026-09-28 05:14:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69c10e7f-8bc6-3b75-bc56-cb1eb35d794f | -22.3454 | -46.96184 | 2026-09-28 05:14:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e10dd560-6a30-3c01-9f3d-8e157852a19d | -17.68878 | -47.98891 | 2026-09-28 05:14:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 044d2090-542b-32f0-a832-b2a230f23b7c | -18.73756 | -45.02314 | 2026-09-28 05:14:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dfa43ec-60fe-3e86-80ef-3ac55b2c8d86 | -17.68402 | -47.98477 | 2026-09-28 05:14:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d208e92f-c7f6-3479-8709-8a20b1e7fac3 | -19.82946 | -53.75876 | 2026-09-28 05:14:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README59.md)
