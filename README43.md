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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d817dc6-0192-3b5b-a130-8519791bb966 | -14.8706 | -48.0822 | 2025-10-25 04:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 1926303f-d222-340e-af94-3f0bd42ca157 | -2.8149 | -49.1354 | 2025-10-25 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| bb7a5c63-d682-397b-8f7e-81299166ebd8 | -18.5634 | -50.2666 | 2025-10-25 04:20:00 | GOES-19 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 51.1 |
| cfd6e57d-73b4-3536-a2ed-87dbab65bacd | -15.53424 | -45.6967 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8b44349-818b-35b5-8b2f-3ad11b8122a3 | -14.56754 | -49.84226 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69cef049-9f58-30c9-b791-ce8123a1cd3a | -14.84472 | -52.44318 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 21321c43-1182-37ca-9f52-760e1df47c5c | -14.33492 | -46.61378 | 2025-10-25 04:21:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11d870cc-3baf-3653-be83-7992663a2509 | -14.74785 | -46.60202 | 2025-10-25 04:21:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfa1ace3-332a-3d9e-922a-7259c81cc5ef | -13.26246 | -50.36193 | 2025-10-25 04:21:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cdd1347-0dc3-3abc-95c2-54fdc12bd7f0 | -14.41382 | -47.91525 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4176232a-1543-3990-8aa3-a4e17cf05596 | -21.08509 | -46.34541 | 2025-10-25 04:21:00 | NOAA-20 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 7a3da45a-014d-3a3e-83db-fd58f593385a | -14.37845 | -51.51958 | 2025-10-25 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de7fc45c-9d1c-3e78-a414-5bc35357c354 | -15.83142 | -49.08257 | 2025-10-25 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f6e0a79-2be4-387b-a506-79157415db32 | -15.24449 | -47.92664 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b1c7162c-78df-35ef-bbea-e21fcd21d2c0 | -14.02367 | -48.00655 | 2025-10-25 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9daad3b7-1dd7-3193-aaee-ba06772162d4 | -19.15335 | -44.63607 | 2025-10-25 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 872bfb18-33ed-3488-ac13-134b2ecd4676 | -14.92661 | -48.1276 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6207bf0-4b50-3106-ad09-c01b37faa958 | -13.6502 | -48.18353 | 2025-10-25 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b77ca852-e08b-3cdb-b0d9-0bd7e34f4170 | -15.74253 | -50.32043 | 2025-10-25 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 926bbfec-3b7c-37ad-a023-b46cf67c3b1f | -14.76735 | -43.08574 | 2025-10-25 04:21:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9532ee39-5b2e-3c8d-841e-248b9303ab8e | -14.38897 | -51.53611 | 2025-10-25 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e425757-d56c-3680-82b8-648c4c345eac | -13.91413 | -48.4127 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4788a2b-272a-38c6-8507-c6d383543fc1 | -14.52128 | -47.94519 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4ab02e5-7c28-3344-918b-f1cc0319d181 | -14.87627 | -48.09581 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a7a8eb35-86c8-320d-b8d4-412bac23af9c | -19.86783 | -48.33041 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a670768a-1412-3de2-b87c-227f5424e7ff | -18.16673 | -51.76654 | 2025-10-25 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6792a67-ca4a-3768-a3cb-54a186ae1adc | -16.77397 | -50.17638 | 2025-10-25 04:21:00 | NOAA-20 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b70cca31-9df9-3ce0-b08b-38bd65017c29 | -14.89826 | -47.8678 | 2025-10-25 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f9cbac7-eae8-3945-9667-8ebd1c8c9b59 | -19.87625 | -48.32057 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92310d18-796f-388e-81bd-bed2de040b15 | -14.45842 | -47.92673 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70bb3e41-e51e-39a9-bc17-5c232066d877 | -16.17033 | -45.08069 | 2025-10-25 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0b8fb33-4d28-3ab9-b2c5-9efd310493a9 | -14.32661 | -46.62333 | 2025-10-25 04:21:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22ea8faf-fb6b-3829-8879-252b5ba49f83 | -14.56695 | -49.84357 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bcf3c70c-b5ff-3bb7-985c-5070c177e182 | -14.44509 | -48.06999 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 959497cb-e913-353a-94a0-8f9763b1c655 | -15.27204 | -50.76454 | 2025-10-25 04:21:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ed623bc-38a0-32cb-ac72-94ebbc987695 | -15.93305 | -56.11504 | 2025-10-25 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d03d1fae-a5b5-3864-8205-439efa1f625a | -18.70236 | -43.72906 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0edb6fa4-d7bd-3bf9-b07c-27bdee30ec9d | -14.44632 | -48.06253 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d97b84fb-f603-3990-ba73-02a2a4bacb83 | -14.90281 | -52.45785 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99aae515-a65b-32a6-b43b-5c574691e21b | -21.08919 | -45.69921 | 2025-10-25 04:21:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66acd0c6-062d-39c1-af5c-32359322edb6 | -14.46579 | -47.92416 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31c8fe4e-e29a-3239-95dc-4506ea2b6923 | -14.91343 | -52.44757 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b8c17e3-b1b9-3a6b-ba05-f24db4d9733b | -15.27663 | -50.76054 | 2025-10-25 04:21:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85156592-53f5-348c-870c-106a5e33866b | -14.87966 | -48.09634 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 287519f8-58ae-31aa-878b-26cbc1d15515 | -14.93273 | -48.13263 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61f99482-da8a-3f2e-a698-639aaa314cb4 | -13.58014 | -48.20307 | 2025-10-25 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d56a6f0d-27d8-3ba3-bc9a-c2153a42050d | -15.56355 | -45.94507 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff9aac56-92d8-33d0-af0f-dcdb89b2a962 | -13.91607 | -48.40094 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7935b881-afed-38ed-9d36-ee7398d175bd | -14.92262 | -48.13071 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9722677-8857-3fee-b193-858aa1f27fea | -20.38637 | -45.91557 | 2025-10-25 04:21:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dfba3f5-e05f-3fc6-9a52-ab021fcdb44d | -16.84147 | -50.52345 | 2025-10-25 04:21:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a6a0031-a123-3186-a03b-95be465546bb | -15.12369 | -47.937 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99b3be3e-7cc8-3c15-8057-87e129267a0c | -16.06574 | -46.62341 | 2025-10-25 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 211f8c67-ec4e-3f23-a10d-6bcaa7f72e24 | -17.47271 | -46.00022 | 2025-10-25 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4901a01c-8ade-3a02-b6eb-94ce446505dd | -14.47968 | -47.90304 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66eecbb4-c4fd-3397-bc04-27ea68831fed | -19.87234 | -48.32365 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19a37399-041a-3055-b609-6a67c7e4ffdc | -14.86338 | -48.08978 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b073130f-1477-3a26-a880-c0db97c82ddd | -17.37491 | -45.49566 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4ffac43-4c58-3e81-aa06-c5fc92886739 | -16.00708 | -48.95935 | 2025-10-25 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b0af77d-56fc-3924-b22f-1ba031a568e3 | -15.57945 | -43.22434 | 2025-10-25 04:21:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 43efbb7f-afa3-3402-b0de-cca42f83e799 | -14.86336 | -48.08217 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bc3ec555-d7f3-3b20-ab09-ea3009b6b5ad | -18.16383 | -51.76074 | 2025-10-25 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dbc5710f-6b48-328e-991d-87815628048e | -19.62307 | -46.13161 | 2025-10-25 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 245069a2-3dfb-321b-bf32-8a6e0f462f55 | -18.47474 | -48.0514 | 2025-10-25 04:21:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ed2b5513-6505-3c80-b3e4-d8f012c4d2de | -15.22711 | -47.92741 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae032201-83d5-31ff-8e5b-e39b94904d75 | -15.50724 | -50.44241 | 2025-10-25 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fb737e7-ff76-354b-8d1e-b626e881fcb4 | -14.89862 | -52.45688 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2566f9d1-217b-3188-b902-e7cae6275d9d | -13.90537 | -48.42281 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6f22f4aa-8905-3ecf-99e7-12fdd29bb5f4 | -14.46517 | -47.92787 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27f96972-7a0b-337f-a382-1632d8ec4d61 | -19.30524 | -50.02352 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52248f8d-35a3-3d07-8442-afffdf4fc8bc | -14.94817 | -43.36674 | 2025-10-25 04:21:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b8e0545e-6240-3e5b-89fe-d9fbb09e2fe8 | -15.6983 | -52.77074 | 2025-10-25 04:21:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e111a15b-7255-3dc6-9d41-6b6cdbaa3a71 | -14.49511 | -47.05654 | 2025-10-25 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b24d4ad-9709-3a18-a7bb-d2cb7d924fbd | -14.33822 | -46.61434 | 2025-10-25 04:21:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4985216f-f2e8-39ea-b6d9-d60685617fcf | -14.49454 | -47.06011 | 2025-10-25 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 365d357a-6d31-3791-bbbe-31d5cbe998f4 | -14.16114 | -44.75946 | 2025-10-25 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be11a246-3464-3f1f-81e8-7cd3d38f5f0f | -16.36088 | -49.93764 | 2025-10-25 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ddbc4f2-7e28-34e2-954e-c045fc56e029 | -14.8655 | -48.09791 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c0891d51-5580-3cce-9e37-bfd44af2a6dd | -14.36238 | -51.81954 | 2025-10-25 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71779092-7d7c-313d-9707-d8c5a50ea80e | -19.76501 | -48.29292 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3490bcb6-256d-35c3-9277-6c2b3259487d | -15.88755 | -52.85283 | 2025-10-25 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce17b915-44f5-3111-a9bf-10c2ef24fd15 | -15.12429 | -47.93336 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b146661c-8a2f-3149-92ec-b9f75e21a52c | -19.95187 | -41.72319 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3c76af7a-8c4e-339a-91f5-b22c4aa12f2f | -14.20437 | -47.30224 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49485fb1-92f5-3e31-af89-4cbec3f4fbba | -14.27711 | -48.06435 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1533a17f-c5ac-373c-bd15-4a7b31b1b1dc | -18.16284 | -44.25072 | 2025-10-25 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01383936-c429-35e7-abd5-175bff6bc589 | -13.57951 | -48.2069 | 2025-10-25 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7621552f-ff37-3dce-9f02-0167d6e4c390 | -14.54073 | -48.01727 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64705877-3f77-3be2-8218-e2f5ab1062ca | -18.17237 | -51.75737 | 2025-10-25 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| fb2441b0-feee-311c-a0b1-94417cdd769d | -18.55338 | -50.27821 | 2025-10-25 04:21:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bb780971-567d-3533-bec6-ae4e74368856 | -13.89071 | -48.40461 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 105c6464-6a3b-3eec-8f9a-57689aa28666 | -13.9107 | -48.41201 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f7640f9-5d61-3f79-aa44-7307a252d8e3 | -18.56541 | -50.27196 | 2025-10-25 04:21:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| 09910ba7-3ad1-3787-bd76-993e8309b27d | -18.17146 | -51.76236 | 2025-10-25 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 536ca125-c75a-3582-b3a5-e60a9151acdc | -20.05306 | -48.29827 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42f624c2-13ae-329a-af7b-8dadfd9bf49c | -13.9167 | -48.3971 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e27ece1a-46bd-3578-ad40-fb042ce28dab | -13.88663 | -48.40791 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8ff2c7e-b242-38bc-9e91-0a218d50ed9c | -15.31501 | -48.07569 | 2025-10-25 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6798800-a622-3a6e-90e8-3b793109890e | -15.4729 | -50.46381 | 2025-10-25 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fb02e25-4288-3285-92e9-604671aecff1 | -14.92821 | -48.5206 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README44.md)
