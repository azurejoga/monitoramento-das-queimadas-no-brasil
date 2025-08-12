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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d0349ae-a08e-3f65-b7c3-f20350c15586 | -11.44962 | -50.17153 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50903c41-7738-3c14-b835-cb123cfbe38b | -11.25395 | -41.4735 | 2025-08-12 03:47:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 417d1181-0f12-3072-bb99-8dcea35f29fa | -14.63547 | -45.85628 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efad4459-de21-3f9f-a97b-ff9841b83e1f | -13.9674 | -42.58292 | 2025-08-12 03:47:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4156fb1b-b167-3d5b-a155-ffb625809b64 | -12.77924 | -45.45498 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3b46393-c1bb-33a5-ae2b-16e6db31b450 | -11.46488 | -50.15367 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3ab9cf4a-a63c-3011-acb7-2bc9a9bf94ad | -23.29196 | -46.79481 | 2025-08-12 03:47:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0902baf3-3c36-3bc1-84d1-a2b8fced35fe | -12.56719 | -46.99552 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 13ca00ab-50e4-3351-b1a9-6c1fce2c0ddf | -14.64061 | -45.85733 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c61ae8f-7b28-3850-8eb6-ef262956a91c | -14.02844 | -47.40924 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c5691cb-e397-3c05-839e-5d7748988ba2 | -14.03899 | -47.41619 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 084798b2-d610-3efa-a353-d7ede14d268f | -11.54179 | -47.30878 | 2025-08-12 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e983e00-8280-33bf-8f0c-c836b9758609 | -10.24111 | -48.25195 | 2025-08-12 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42721a5a-1a32-38b4-baa0-b16e32c61086 | -12.04253 | -40.29367 | 2025-08-12 03:47:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fd74cf11-aa3e-34bf-9722-6d65c6d2334d | -12.64116 | -45.33507 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f2af6e6-9702-3150-897e-d641f0c6f8af | -10.96945 | -49.56638 | 2025-08-12 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e1024cf-c771-333b-9e60-2f324cd34eb3 | -12.57647 | -47.06883 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 954edc2b-b1d8-318b-bc67-97a1a343030e | -12.57372 | -47.02263 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 419b4a73-4123-3730-aa5d-156f9180cb05 | -11.66375 | -50.13231 | 2025-08-12 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 176a57f8-7301-3671-8815-476f8c2ec263 | -14.12092 | -45.38557 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90ab8890-b3db-3de2-a6d1-c2d70f4b55f3 | -21.24563 | -46.71836 | 2025-08-12 03:47:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 95bf372e-ef77-3e18-9f1b-8e96db69ecce | -23.08066 | -46.98059 | 2025-08-12 03:47:00 | NPP-375D | LOUVEIRA | SÃO PAULO | Brasil | 3527306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3fd23669-901c-375d-8cb2-9b5e49dc17ca | -14.4613 | -47.83952 | 2025-08-12 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68e02ba2-f1cb-3fb3-9a75-8a5448974d17 | -11.45665 | -50.1731 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 208f0cf3-d4a0-3415-aafd-954a9b28e8ec | -13.34923 | -50.2495 | 2025-08-12 03:47:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f544c6dd-adca-3ee9-9cde-4dba537f4bb3 | -22.9885 | -49.02736 | 2025-08-12 03:47:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 2a4b5ac6-8e73-33ca-b033-7e29127fb41c | -11.76692 | -49.11366 | 2025-08-12 03:47:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fc477f5-ea27-3df7-915b-56a57ce6b2bc | -13.87504 | -45.56797 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ebc677f-70c2-3084-9e9b-ca398e184dfa | -22.98154 | -49.03339 | 2025-08-12 03:47:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e1fb47d-0a95-3600-98f7-b8d8e514567a | -12.77408 | -45.45388 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29480f74-0528-3724-b622-3accbf22ca91 | -11.75482 | -45.02769 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cc2d424-5822-39cf-8485-394382d022db | -21.24091 | -46.71698 | 2025-08-12 03:47:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ddec5dd5-f545-35fa-8d3c-ed585b432bd5 | -12.55061 | -47.0483 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4e6241f2-73a4-37f0-accb-17e95e3d5444 | -22.71561 | -43.23887 | 2025-08-12 03:47:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 161ff3bb-e39b-3024-92eb-9ef8b935149c | -12.77864 | -45.4581 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21da1824-e1a5-3f1d-a1e5-2bb3570f77bd | -9.71374 | -49.47816 | 2025-08-12 03:47:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3df5e33d-9616-3f50-b47e-27b5199fa3e5 | -12.49864 | -46.34338 | 2025-08-12 03:47:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6c8097b-3949-3148-9577-5db3425f55ab | -10.36484 | -46.64256 | 2025-08-12 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1fa130d-498a-3436-aa9f-f39440f5969d | -12.56314 | -47.0157 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a53675ae-f318-3148-8652-82bdc557a6fd | -13.87896 | -45.57523 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86bc0847-20ba-324a-8cef-742492c6dc84 | -15.66998 | -43.49185 | 2025-08-12 03:47:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 08b69a57-4eb8-3759-9404-2bd6af9c7707 | -11.66161 | -50.13131 | 2025-08-12 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4314ccc5-b675-3ccc-9892-bf819ae2aa56 | -9.72071 | -49.4796 | 2025-08-12 03:47:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e212bf11-84dc-3279-8965-0b5675c5e648 | -12.49526 | -46.33146 | 2025-08-12 03:47:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc3ed85b-7f64-338b-9fab-6c832952a88b | -12.56233 | -46.99 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0fe5290f-a738-3e8b-b742-981ebdebb931 | -11.9172 | -44.85436 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| daadb601-2670-3b7d-918d-21745646fdd3 | -14.04043 | -47.40907 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff81f9f9-8896-396e-a389-9d945f639f18 | -16.00822 | -43.27708 | 2025-08-12 03:47:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b353d70a-75a9-33ca-b980-0328801177c6 | -12.50011 | -46.33592 | 2025-08-12 03:47:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44ec3411-5c6c-3fb0-8881-ce17ca77c1fc | -14.46132 | -46.21642 | 2025-08-12 03:47:00 | NPP-375D | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2cca9df-2eb9-33c9-976c-83d32ca448c5 | -12.57215 | -47.00055 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 35739b10-7038-3afe-9e04-b683506ae918 | -14.101 | -44.84704 | 2025-08-12 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6d16b28-01cd-397d-bded-9bc62144f2da | -12.77985 | -45.45183 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82545080-2973-38f6-b5bb-089a6a11fffa | -11.74809 | -44.97116 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dd5e6ca-e53f-305f-a915-f77e3e84cdbc | -12.04209 | -40.29602 | 2025-08-12 03:47:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 353cdf55-99ac-3a48-b611-d97d7f44296d | -10.36405 | -46.64659 | 2025-08-12 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6187e000-5267-32d4-af62-917a1a26e8c5 | -11.7445 | -44.97084 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f30d345a-e47e-377c-afa4-a3c9213e98ef | -10.06608 | -46.39816 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 717bd9ed-cfa4-3d73-87fd-f933091e7270 | -11.79948 | -44.93235 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ba67d0b-fb4e-36c8-a93e-322040c70c24 | -13.58138 | -46.95148 | 2025-08-12 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d702e98b-287c-3cd9-a05d-982982524859 | -14.64122 | -45.85422 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad0325c9-04a5-3baf-b3a4-5c4d17154caf | -12.77468 | -45.45075 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4a2afa2-7343-30d1-aa2b-032da9c4fa1b | -11.45808 | -50.16619 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c99a77e-1a5a-3644-9339-7839cf80fc64 | -12.77286 | -45.46018 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c48fcdbc-81ca-35b0-b82f-3ff3bad22a02 | -11.46093 | -50.15236 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a767e70-8163-36b1-b9b2-abc7eab73d8f | -14.03971 | -47.41264 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c1c8214-af9c-3c18-9bdb-ac3e2aa7c4e9 | -11.80457 | -44.93335 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a42a85cd-fe40-3d33-8165-f13e5359bddf | -21.11983 | -48.82914 | 2025-08-12 03:47:00 | NPP-375D | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e15150b1-f691-329e-9893-467c1376d279 | -11.54771 | -47.31014 | 2025-08-12 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1df9e492-cd7e-31e4-b923-9509bcc1db2c | -21.12024 | -48.8307 | 2025-08-12 03:47:00 | NPP-375D | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3a40dd5c-9f8f-32b5-a1c8-98055b29bbd3 | -13.62743 | -46.92546 | 2025-08-12 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3df1f16-ee9d-3863-9ba4-b33233841e9e | -12.76951 | -45.44971 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c9c959d-a435-332e-836c-8a7b2633f02b | -13.35602 | -50.25124 | 2025-08-12 03:47:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4cc9c94e-31b6-3256-a5f0-29e8007b2f7a | -11.72231 | -48.34774 | 2025-08-12 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 519d51d6-d68a-3b33-9b7e-3e3b66dc769f | -17.56677 | -44.33525 | 2025-08-12 03:47:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d82da72-c9d9-33c5-8b8b-ad8e7507a6bd | -11.73161 | -50.11146 | 2025-08-12 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 053fac86-de20-33b2-9d5b-f7d71c1960da | -22.99302 | -49.03225 | 2025-08-12 03:47:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 843d0262-862d-38ce-8d98-76890d4cd934 | -22.98604 | -49.03835 | 2025-08-12 03:47:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4ac98ae7-c489-31f6-a281-fbfc0e14bf94 | -9.71933 | -49.4864 | 2025-08-12 03:47:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a598def4-68c7-3df4-9f86-2369a485a866 | -10.96813 | -49.57294 | 2025-08-12 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21e4fc65-9478-360f-927a-cb6eaf344442 | -11.45105 | -50.16461 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04df480c-d280-37b4-b04b-cb5f39b21940 | -12.73242 | -45.89647 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61928aee-8d79-37dd-8c32-cdcb434aff53 | -12.55801 | -47.01151 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9b9a6f1e-b673-36dc-9d23-90183ade5219 | -13.58772 | -46.94903 | 2025-08-12 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36c28de2-f87a-385f-98a4-61dee322cef2 | -11.7594 | -45.03155 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11f2ddb3-97fa-3c59-a137-71ec2a0cc541 | -13.34262 | -50.24727 | 2025-08-12 03:47:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f059e054-1788-39a8-ba7f-2242fe92fd17 | -10.96913 | -49.56656 | 2025-08-12 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0c10fe5-96c6-353d-a0c6-fb467dae06ac | -13.34242 | -50.24781 | 2025-08-12 03:47:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d53adda1-a4be-3421-bbf1-91003b85dd35 | -21.23957 | -46.71809 | 2025-08-12 03:47:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 49ee82be-0069-3c11-8c4d-600dc356a1e5 | -12.56315 | -46.9859 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d528307a-7110-324d-9a73-15066fea3c69 | -10.64624 | -45.24027 | 2025-08-12 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55f04d99-39e9-3dd7-aa68-5aec4762784b | -13.00102 | -44.89047 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98d7bbc0-a0e7-3bcb-9478-df7d35dd65c4 | -12.49456 | -46.33502 | 2025-08-12 03:47:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80d161a0-760c-33f6-958d-02d85f220021 | -12.56467 | -47.00808 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6aaabb09-8374-378d-9893-f4ce125c6745 | -14.11475 | -45.39048 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f7413c0-c22d-3ca3-afd4-564459360b02 | -12.64437 | -45.33855 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 389611d5-a7fc-36b8-8fef-5ee7bd1fc6f5 | -13.03927 | -39.91936 | 2025-08-12 03:47:00 | NPP-375D | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 99a4da86-a02b-3a5e-8f81-f43dcf6e6d2a | -9.71235 | -49.48501 | 2025-08-12 03:47:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 6c7f93f9-496e-388f-b693-f0192cf73f4d | -12.14062 | -44.92551 | 2025-08-12 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17e40b3e-20fd-33a5-a0c9-209c6ceebdd1 | -13.02815 | -46.67319 | 2025-08-12 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README11.md)
