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
| 4fb492cd-2a05-3bda-b4c7-055cb1b4200f | -14.69752 | -48.13174 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f19049c-ee84-3534-9051-5dd47bffb5bb | -14.60535 | -48.21933 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5647a23-8cdc-3130-a6c0-a40d6f9e4012 | -11.57414 | -47.64477 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bba5eba4-b846-317e-ba66-339265bcb8d5 | -11.27359 | -47.21532 | 2025-10-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e6f500a-eedb-3bf6-b9d1-17e86340e024 | -13.65771 | -48.03655 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ddd2fba1-f4b0-3dd7-a2dc-741291841a2d | -10.93476 | -46.50148 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1f7b79d9-ce7e-32c7-81a2-2d4606af4ad2 | -12.78362 | -46.86363 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20e25398-07ce-3309-82f5-4323f1784192 | -10.65374 | -48.52604 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2d09c50-7664-3f60-a6c7-879840cefcd0 | -14.01954 | -46.31797 | 2025-10-01 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8ffd164-4f68-3f87-a014-b0d138fc4c13 | -9.40054 | -54.71394 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9eb99881-b53e-301f-91b0-2fe2157258cb | -11.63369 | -47.49222 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a987ec89-a083-31a0-a465-62cf4f64fef3 | -11.6838 | -44.29596 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7863e27c-c93e-3168-ab3d-afabfa6d11f9 | -14.7067 | -48.2665 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3ede23a-7239-3554-9d55-21859ca0800f | -12.43184 | -50.17033 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e4db397-9e52-3ed6-a891-1c256890a396 | -14.49974 | -48.43927 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99ddb50e-f85b-3ddd-b153-05cf6fef4044 | -16.57688 | -45.11185 | 2025-10-01 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc3277ab-6185-3771-9d99-9bddc0da2001 | -14.59583 | -48.21399 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbc5790c-1977-368a-aacf-ceeaf5d6dc8a | -14.37834 | -47.13244 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ba3b428-21aa-3608-ae2f-39c1bb2d2a31 | -11.12785 | -49.78509 | 2025-10-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e998ce4-dcf3-3ea6-88ea-4bb932f2653e | -14.78964 | -45.80107 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ece1c67a-322d-3af0-8548-bec9dd4da626 | -12.85624 | -46.94092 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4eda636d-5b8d-3486-b761-e63a3bb2b504 | -16.05589 | -51.01578 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12bfbd99-0c60-3e05-8036-b9ee3807a82a | -14.18565 | -46.12418 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ed82c7f0-c78d-3fe3-bc35-e0958650f515 | -15.16132 | -49.09167 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 285627f0-0e71-3e0d-89aa-bf0a499fc968 | -13.74033 | -48.69195 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0df95fcf-e266-30f7-9b51-fc56d1e2ea55 | -17.43616 | -47.13985 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0bd3189f-eb6b-3400-ac0b-cd0ef94d576d | -15.53796 | -45.22448 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d5fefa83-900a-30dd-b3be-212b7ac5719e | -15.55129 | -44.34799 | 2025-10-01 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f54b37db-898d-325e-822d-59bb502baadc | -12.84848 | -46.94701 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b398dc59-539f-328e-bff4-b6832840a62c | -13.65177 | -47.31105 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf0cc634-fb90-3a4a-9f36-bf574c946a19 | -11.83469 | -44.9623 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eab6c9ee-aec2-3dbc-8ccb-a5547f69218f | -11.82035 | -44.98923 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8929bd8-01ba-3d5d-8a83-2183b75cbfcd | -12.58774 | -41.28655 | 2025-10-01 04:21:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| fa222a9c-c131-3990-8656-5f6c6466d4ff | -10.82745 | -47.95333 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87b09679-c342-3647-b4b2-c4d2860f6d5b | -15.53514 | -45.22018 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e3f02922-115c-38b0-ade2-c323fb2fedbe | -13.31095 | -47.22843 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff1c8d09-baeb-32e4-a7e1-1bf52b92c5d6 | -12.77166 | -50.54957 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cccf29ab-03b5-33d5-9a45-575e0d2b55b5 | -13.73406 | -48.68699 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a8d4ee5-809a-3463-8ca8-cccfae5b2697 | -12.84872 | -47.03108 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b43eb6b5-b400-3d17-b3ea-cd7a8d884185 | -11.42376 | -43.5031 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d58ab2c-7f7d-3305-b790-e16b96b8df34 | -11.67692 | -45.34755 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19682e09-4964-327f-b301-40b1833a667b | -10.62899 | -48.58855 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8924110-3d14-39c1-815b-be7d5c4d6363 | -13.29539 | -47.24049 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14cfef91-2d58-36f9-83ba-73527e0e9c1e | -11.47169 | -45.09074 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3190019d-dbf6-35a6-8067-87a8e00a3822 | -10.19412 | -52.55977 | 2025-10-01 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a25a53b9-9ef6-37d2-888c-de6129d214ee | -13.29893 | -48.70236 | 2025-10-01 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c54a6f0-d757-385d-9d57-d26ba818ced2 | -10.90658 | -46.50774 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 857a0831-282f-3b54-97b1-5857212f7058 | -11.668 | -47.49389 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fce22bb8-7030-3b39-9526-e434d3f0189a | -15.32446 | -47.3682 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5699d14a-6892-32d4-9f56-f3ce6fc28cdb | -12.66852 | -46.88116 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acffe633-a2a6-356b-a7fa-f4d3436d46be | -14.88704 | -48.32718 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dc07dba6-bf95-37ce-8f26-24ef859d5ace | -14.72415 | -48.26576 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82590cb9-becf-366c-a1a9-db4885d7df0c | -12.90666 | -46.81831 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d72f2921-af17-38a3-9896-556645288179 | -12.47812 | -54.42144 | 2025-10-01 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30debd0d-495f-3b25-85c7-b94c68216587 | -11.47363 | -44.98934 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c85fbe32-00a9-3e31-9adc-a8af9a83de1b | -14.13913 | -49.19747 | 2025-10-01 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d55d41c-e6e6-3344-82f7-8d1afbc7a1fe | -16.12994 | -49.14886 | 2025-10-01 04:21:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 063e7b68-7256-3bc5-b58b-821d0385d59e | -15.24988 | -49.72623 | 2025-10-01 04:21:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 762c9b29-b1c4-3b9a-8179-9e70d5c59849 | -10.92024 | -44.3368 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dc52850-9a9a-33b0-a459-ee5bd9865b6d | -14.94821 | -45.53707 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 580c3e29-f127-3864-88a7-516b91dc98eb | -14.22876 | -44.78665 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a361c41-f506-3225-960c-e66c14477f5c | -15.29972 | -47.86242 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fd56298-8397-37ac-8720-440391638a1b | -14.783 | -45.8 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e658928-bd99-3913-b7be-a1da24d0cf84 | -17.91197 | -44.60371 | 2025-10-01 04:21:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42301ccb-f040-33ca-b035-5aab6657194e | -10.83262 | -46.6517 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1159330-746d-3cdf-8f96-37ed0cf36ee0 | -13.46127 | -47.24619 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ef4025a3-1781-33e0-ba3f-a4935ae71d25 | -13.76586 | -47.95584 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a6e13519-a346-3c06-abd9-5f1e64467db4 | -16.88676 | -47.47392 | 2025-10-01 04:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d33a15e-b2ce-3578-81e2-cf7001d2e2cb | -11.26805 | -47.20699 | 2025-10-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d488c3d-10b3-3f32-9f4f-7a758c9facf4 | -13.71793 | -48.65623 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e83ed4db-66e6-33bf-bed2-6aab0146aa32 | -15.00924 | -46.97195 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b82c46c6-5688-3ef9-889e-1f7249d2ec38 | -15.28986 | -56.78552 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c26d4bcc-ea17-307e-a318-a6cdd1bb1ad8 | -15.17236 | -49.08942 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 42b1cf45-f1c9-3554-9127-5c7a9695c62d | -13.35952 | -46.38339 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60ae7261-44cc-3634-8962-dba473cf1721 | -11.7958 | -47.6014 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ebf4d25-9f97-397d-8a69-af87f8c52f85 | -13.67072 | -48.08475 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3db1233c-35e1-3a3f-9ca5-be6f59bb39f6 | -14.18893 | -46.10295 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e78e0a07-9b2e-3554-97d3-915b2d13aede | -14.50285 | -48.42051 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0954874-99a2-398c-90cb-ff4a7347651c | -15.24526 | -48.73684 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8df6a74e-94a5-3638-833c-6c51aaa3fc6e | -11.04975 | -47.81842 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 702768f0-afbb-32d7-b56e-9d997ade732c | -15.24799 | -46.96761 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10953bb0-9493-33d1-a598-6c352eddd3f7 | -17.40358 | -47.17153 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a23cb05-62c2-3cf3-bc31-068cbec2cf9d | -9.55895 | -54.59008 | 2025-10-01 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00d70a69-3888-39bf-b216-c06852ce4a61 | -11.47724 | -45.09884 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c58df29-89d0-3810-a524-7ab0cbef542c | -14.78818 | -46.97137 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bce8f0e0-6116-39bf-aad1-82a5a2fb8a5e | -14.35312 | -45.89966 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65905715-84a7-3f15-b7f9-5f59c410e508 | -16.24952 | -50.93784 | 2025-10-01 04:21:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 546e06a3-c013-3baf-bdf7-fe154a391059 | -11.20022 | -47.73499 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ae5021b-76f5-3510-980b-3a6076388197 | -14.18895 | -46.12471 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c9ea98c-b186-33a8-badb-2c33f44104d2 | -15.68958 | -51.28059 | 2025-10-01 04:21:00 | NOAA-21 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 771c6580-25a4-3fa6-baf9-9056be4d73a7 | -12.58993 | -44.79937 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07efc736-cc7e-33a8-9115-eea9ef9c983d | -11.60649 | -45.03176 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea1a907c-2b64-304d-8f3d-107c0dfd2116 | -17.33722 | -47.57308 | 2025-10-01 04:21:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61a3f24b-1c26-3740-bb0c-fa527542a746 | -11.9193 | -47.89682 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8af0a1a5-477b-3087-be53-68c16cac106b | -12.92689 | -54.72847 | 2025-10-01 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8772879d-8eb4-3197-9e58-f5819b226db0 | -11.99034 | -46.64928 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 261a19ed-4127-3fe7-8de0-d8b68a68da36 | -15.78196 | -43.69696 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1ccef47-9d47-34c6-8cdd-2455f3fc8733 | -13.74646 | -47.92635 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9a8ad43-ba1f-370a-a349-9bb0568ec2b5 | -12.8056 | -46.89622 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ec10c11-f697-338b-a5ac-268f57f19538 | -13.45907 | -47.23862 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README67.md)
