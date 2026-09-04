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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d5dc79c-5ec5-3e36-887e-e03fd7339d2a | -14.91001 | -44.67643 | 2026-09-04 04:21:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 366ccc2e-124d-386e-b14b-72c88ccb4def | -18.98098 | -46.8199 | 2026-09-04 04:21:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 52c1ffa2-2d56-3af2-af0e-21f2cd8d77cc | -15.32622 | -47.04645 | 2026-09-04 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4d72da0-c85b-3f5d-b4ad-064451751fb4 | -17.09947 | -56.86668 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c2d092b9-db6d-3be4-b353-8ea59cd06675 | -13.4079 | -43.87815 | 2026-09-04 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f6d528f-8234-3571-8a88-930e98ba479d | -17.09915 | -56.86756 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| da811d7e-2028-32f2-acac-cc6670b07197 | -19.31295 | -47.09687 | 2026-09-04 04:21:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92227088-d9c4-3f24-8dbf-3e8f66bb3bed | -15.32544 | -47.05095 | 2026-09-04 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 198a74b2-6b0a-3731-9941-bd1abe6b8825 | -16.57112 | -51.62394 | 2026-09-04 04:21:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e03fb52c-7768-3c83-b588-d7f5074f0530 | -19.80651 | -49.42084 | 2026-09-04 04:21:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8719abf6-705a-39e7-8a20-9d39e031349a | -17.83993 | -44.68785 | 2026-09-04 04:21:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b820840-69e7-37c2-86bc-f18e913696b6 | -13.58231 | -47.87976 | 2026-09-04 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31632132-f773-3e1c-8de2-fe4a019261c3 | -17.09274 | -56.86593 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e94556d8-4fff-3931-be63-363007c563c4 | -17.09307 | -56.86502 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f4598387-c4ed-3362-94bc-ae7972a99542 | -18.55914 | -48.40226 | 2026-09-04 04:21:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d7856c9b-49da-3b22-ad15-e9664066bc32 | -15.32103 | -47.05474 | 2026-09-04 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f02ab13-8a5d-3f34-bb60-961957457fa9 | -17.10297 | -56.85088 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0b785970-8b53-330d-90bd-5469f22e9ef0 | -19.35343 | -47.09192 | 2026-09-04 04:21:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cad015fa-bac3-3162-9371-44bc79af38ab | -17.52412 | -44.61095 | 2026-09-04 04:21:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad52f6e7-9b45-3ced-84f5-ea4b5eb6f3b0 | -17.31932 | -49.6159 | 2026-09-04 04:21:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee9438b4-1082-3cee-aa8d-03e438b1171b | -14.90665 | -44.67585 | 2026-09-04 04:21:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 727e4429-811f-3fc5-8a57-6def927ac460 | -15.90884 | -50.16201 | 2026-09-04 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de2f5f77-e992-31bb-93a1-02fe392cf318 | -17.09146 | -56.87149 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 29ea7992-5b49-3966-bf3d-23e4446c1980 | -18.52531 | -48.43958 | 2026-09-04 04:21:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66139c64-824d-3c52-b7dd-a78eba69dc11 | -18.13256 | -51.80465 | 2026-09-04 04:21:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51a959df-628c-340c-bc56-cd7ec45ba95d | -18.51932 | -48.19012 | 2026-09-04 04:21:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c9725e06-8faa-3a90-be1c-f95d3f2495e4 | -17.08683 | -50.06838 | 2026-09-04 04:21:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 68da133f-c11e-34e0-9c94-70480b04b24e | -17.30226 | -48.79892 | 2026-09-04 04:21:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85f43ba9-6086-303c-8615-1ea9896ad76a | -17.52354 | -44.61458 | 2026-09-04 04:21:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fccb37f8-76ae-3146-8a7f-4e3c715ba113 | -18.52 | -48.1924 | 2026-09-04 04:21:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a67e17fd-a381-3b55-950d-fdbcce6c6c38 | -18.80347 | -47.5507 | 2026-09-04 04:21:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d659e63-2f0e-39e7-9902-4afb9fa7aedf | -15.32699 | -47.04198 | 2026-09-04 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9810c56d-1a87-3005-b3c8-90af66c1c221 | -16.51318 | -46.59436 | 2026-09-04 04:21:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ddeff70-d4eb-3f46-95ab-f3e90e18f7a0 | -15.62937 | -45.90342 | 2026-09-04 04:21:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 699061eb-b447-3018-a9c9-6734aa78e78c | -17.24681 | -44.86645 | 2026-09-04 04:21:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c10ff68b-23c2-319d-b580-f752fd3708f2 | -15.7262 | -47.79085 | 2026-09-04 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da793b0c-3c01-330b-a97b-c9b49afdcb88 | -19.35412 | -47.08788 | 2026-09-04 04:21:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5468786-6a09-3469-9dd5-8a9a2543fcac | -15.68681 | -47.70676 | 2026-09-04 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61873a9e-6843-3e13-b745-7da22571f881 | -17.09182 | -56.87062 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e1cd3d50-26b0-3b4e-a85d-dc4d92d03a85 | -16.64606 | -49.39957 | 2026-09-04 04:21:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 439e70cb-7538-378b-8f28-5d6c9e2024d2 | -14.90605 | -44.67951 | 2026-09-04 04:21:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 61bfbdf2-8efc-3045-b146-03b1ed515209 | -14.09104 | -45.62059 | 2026-09-04 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea689f4b-7ace-3c1f-b276-8b2e001449ae | -17.10071 | -56.86111 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 91363c39-e8f7-391a-9d6b-e7894b11050f | -17.09823 | -56.87224 | 2026-09-04 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9fc0d7e0-18cb-34db-ac13-5915d03cb524 | -13.41181 | -43.87514 | 2026-09-04 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16e751b8-79d6-3f75-af7e-562732871372 | -18.73678 | -48.91726 | 2026-09-04 04:21:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba69dc05-f90a-3429-9c74-08a10a85869c | -18.1372 | -51.80558 | 2026-09-04 04:21:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fcf1f2ae-0560-376c-8032-3db7bbf843aa | -15.06886 | -45.32145 | 2026-09-04 04:21:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e04ea97-2668-3c47-baf0-31534b74c0b0 | -15.06824 | -45.32523 | 2026-09-04 04:21:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c2946ca-693b-385a-9852-fef03df55ada | -15.77129 | -43.31699 | 2026-09-04 04:21:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dfbc78f-c424-3a13-a7eb-2b52526aff0e | -13.41457 | -43.87928 | 2026-09-04 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f315d4b-6cdf-3424-957d-0971f81becf4 | -18.21017 | -44.08661 | 2026-09-04 04:21:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0025bde1-1ab1-36a0-be17-288e083d120c | -19.31365 | -47.09282 | 2026-09-04 04:21:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19753b78-582a-3c82-94d0-1df90ebef2b3 | -14.08953 | -45.62115 | 2026-09-04 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab75ccab-8a55-3993-8c3b-117806a8fcb7 | -17.2474 | -44.86279 | 2026-09-04 04:21:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 070e13c6-5b0e-37c3-863d-e9aa9f8a8661 | -23.40799 | -46.42307 | 2026-09-04 04:23:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4b0ae220-20b7-3d7b-9d0a-d5453e5f1e36 | -21.64058 | -43.9874 | 2026-09-04 04:23:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d5989f3-554b-3105-b85d-393480e4ec01 | -23.27706 | -46.60303 | 2026-09-04 04:23:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8f11b959-0250-3bcc-b920-d34100d5585f | -21.06092 | -48.46315 | 2026-09-04 04:23:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37d5bf68-3c90-3ce0-9a8f-bd4c935ce068 | -23.08281 | -48.61417 | 2026-09-04 04:23:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d21ff49b-859b-3eee-a412-fb1e6dbb0aa1 | -20.9725 | -46.4932 | 2026-09-04 04:23:00 | NPP-375D | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29440942-ec39-3430-93b9-c9e8e31f9087 | -21.06897 | -48.46013 | 2026-09-04 04:23:00 | NPP-375D | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4680279f-b3ff-3b25-817d-27d01f75d844 | -23.28041 | -46.60369 | 2026-09-04 04:23:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 5b72fb93-2a93-3e8b-b27f-f87e248baef0 | -21.26118 | -47.35425 | 2026-09-04 04:23:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 00ad4139-879d-3e3a-8ea3-d937800e2ea0 | -21.89806 | -55.3723 | 2026-09-04 04:23:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 884f5f21-5177-3741-90a3-3b7e35a6e80c | -21.46188 | -48.67291 | 2026-09-04 04:23:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 739278c2-e21d-3b2f-b05e-25aee1eb71e8 | -22.31382 | -54.87609 | 2026-09-04 04:23:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48255cba-039c-378d-87c9-e4f531384ae9 | -22.84637 | -49.34733 | 2026-09-04 04:23:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0ea10b2-2efb-3608-8c82-7f94468b1328 | -23.32649 | -52.31248 | 2026-09-04 04:23:00 | NPP-375D | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bf4dd825-2904-37a5-8849-8bd346266eb1 | -22.02076 | -49.57059 | 2026-09-04 04:23:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 56df2c41-8636-36d8-a04f-b3e0d4f7bdad | -21.63721 | -43.98682 | 2026-09-04 04:23:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ca550261-a8a3-3233-b247-e61e0deed7b1 | -23.42881 | -46.75845 | 2026-09-04 04:23:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| afcbb9e0-da31-3e45-b365-27e5097e5b94 | -21.41717 | -45.11069 | 2026-09-04 04:23:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| db216eec-3c42-386c-9941-0da94e35d8ff | -22.02453 | -49.57144 | 2026-09-04 04:23:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b9ea8de9-e6ea-364f-acc7-35f3cf11b629 | -21.23791 | -45.61737 | 2026-09-04 04:23:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1c5a4ddf-0415-3f05-9fb2-95aa181ba006 | -20.915 | -48.48134 | 2026-09-04 04:23:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 596c567a-c1bc-364f-841a-180cb9aab694 | -21.45824 | -48.67216 | 2026-09-04 04:23:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f06e5cea-dc52-344f-99ec-598c2d2e4f77 | -21.58055 | -48.65745 | 2026-09-04 04:23:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0db72a9-8d55-3bc3-9c2a-a28f8113aee3 | -20.97278 | -49.10494 | 2026-09-04 04:23:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29616129-393c-30e3-8198-2d0861b93c1a | -23.32742 | -52.30788 | 2026-09-04 04:23:00 | NPP-375D | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7239f7f9-991e-3672-8e67-2ba1da215a45 | -21.58136 | -48.65292 | 2026-09-04 04:23:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 92928ea8-74db-33ad-832c-a41e184a1358 | -21.06455 | -48.46388 | 2026-09-04 04:23:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3af64123-0744-33a4-b383-7738c9e87d5b | -21.72258 | -47.13074 | 2026-09-04 04:23:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61354cdc-a83f-3677-bc8b-bf33b5d1fa26 | -23.08637 | -48.61494 | 2026-09-04 04:23:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80f5b2e8-b361-37fe-afd7-4bc59009f4a4 | -21.25772 | -47.3536 | 2026-09-04 04:23:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad7d2a27-063b-3806-94ad-97db1d1a50f5 | -21.25703 | -47.35764 | 2026-09-04 04:23:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 3e31355f-1a8d-3e20-a1b5-c52bac96d76e | -21.41384 | -45.11009 | 2026-09-04 04:23:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f70d399a-2a74-3ef6-bfe3-1e0848617bc7 | -21.7213 | -47.15918 | 2026-09-04 04:23:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f3d044e-98b8-3b1b-b5bd-d2d712a800ac | -22.31379 | -54.87556 | 2026-09-04 04:23:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce6269ef-7f07-3b9b-965a-ff3f2c83e4c6 | -21.585 | -48.65361 | 2026-09-04 04:23:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec08db74-2cad-3ba5-a871-b3a13e8c0853 | -27.24139 | -48.77698 | 2026-09-04 04:25:00 | NPP-375D | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 380d298a-ea96-3024-801f-cf4750f7b20f | -7.566 | -61.343 | 2026-09-04 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| cb779838-1cd5-3727-8db7-9b56aaef7736 | -7.5476 | -61.3437 | 2026-09-04 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| dae18ef5-f189-3b40-b06d-a8ec83a966a6 | -8.5048 | -54.6606 | 2026-09-04 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 7dbea2db-9f67-365f-a2d5-bca14396bf2d | -5.565 | -60.1739 | 2026-09-04 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ec458564-e017-346f-9249-234461f35a60 | -8.505 | -54.6404 | 2026-09-04 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| d876d792-90af-31f1-ac5f-db899102fa7c | -8.4863 | -54.6417 | 2026-09-04 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ac6b45e1-4ff8-3cd0-ae01-3c11affedaf6 | 2.15878 | -50.69357 | 2026-09-04 04:36:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca80f383-6d69-3db4-a14e-2210d7282d08 | 2.37437 | -50.76404 | 2026-09-04 04:36:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bee3342d-3014-35a2-ba94-a7f36dbdf884 | 2.15486 | -50.69417 | 2026-09-04 04:36:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README15.md)
