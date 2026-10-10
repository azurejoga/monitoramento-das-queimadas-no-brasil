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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 911537d3-7770-3b72-b602-a14ecd4f1cbf | -9.95416 | -55.11238 | 2026-10-10 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c07be9ed-ba80-317b-8f02-467f839639f5 | -11.50916 | -49.89767 | 2026-10-10 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0abecf6-7adb-3d56-a370-81c682da3caa | -7.93078 | -54.72946 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6a04038e-169b-3c54-9a04-8d80ec611e44 | -14.32454 | -44.66769 | 2026-10-10 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b92e36b6-83d4-36a0-bb36-1c26f6099c8d | -9.28463 | -47.38706 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c0549e6-5e67-3cd1-8d86-5873b5fa0c49 | -8.22365 | -46.3838 | 2026-10-10 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 696ca918-3e49-3d57-8f33-2e4d19587690 | -6.93497 | -59.25298 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8892b6b-f641-3bca-8cc5-86145601f430 | -12.37282 | -46.56303 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 844144eb-d316-33c7-8297-cacc71b3b2b6 | -7.10535 | -52.6675 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7ec47b4-46cb-3e2b-849a-f34e30906cc0 | -12.37809 | -46.57609 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 251c06fa-1e8d-3fe7-a57c-5aeff006c26e | -11.01667 | -49.1136 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c6da473-20ab-32da-b9a6-5a3545b1812e | -6.12566 | -55.69934 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 561f6874-5fb4-3cc5-8c72-78bd1b16b7b5 | -7.19679 | -55.14606 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c30c9d46-c19b-36b5-968a-04a15014985f | -11.17786 | -45.31421 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d63cf223-3223-343a-8b64-53c8178a1a1e | -10.90128 | -44.83605 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6b75857-5b14-3ee3-956e-1a51a12ba6cb | -13.77516 | -48.12109 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 554563a4-3a0e-32a8-8e6d-5fdb2ff6f40f | -6.50884 | -55.41122 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 084925f0-ed06-38cf-8483-99c1f70d39bd | -5.18743 | -60.30104 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 547088b0-4875-3828-809d-4d8b5eeb7316 | -8.45228 | -47.98515 | 2026-10-10 04:46:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7076cfa0-51eb-3548-9111-81416d1c5b65 | -12.00151 | -43.43591 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dba6d17e-8c8a-3316-98e1-17f3562c2b38 | -12.22481 | -44.69408 | 2026-10-10 04:46:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cb0b1bb-4c5c-34eb-8601-5d22eab2d702 | -13.75189 | -48.5174 | 2026-10-10 04:46:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e478e867-1bf3-334d-8227-461dbe53704b | -10.93508 | -45.37114 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57fb2dc9-c19f-3f15-b773-9cf3f6300bf4 | -11.50822 | -47.60353 | 2026-10-10 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0f11dd4b-91ba-35b2-a706-4a00c3f19cd7 | -9.31981 | -47.3704 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7419171e-5f8a-347b-86c3-c1afdcffb605 | -11.95381 | -43.47192 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b169407-d2b8-37fe-b549-b20cd87da3f9 | -9.17715 | -51.38267 | 2026-10-10 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fb3a306-0ca5-3548-8f30-cba9657c4f97 | -12.02389 | -43.48902 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b538472d-9fd2-3316-9355-bac0dd4deb4f | -13.25179 | -42.25398 | 2026-10-10 04:46:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| aafda86c-2d65-3f95-bdee-79245b4dea6c | -8.18123 | -54.71553 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a3a11a3-f1ad-3c35-b024-881d3e45db23 | -5.95259 | -55.3408 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f160b14-a74b-3f5f-b28d-caf8bd37a848 | -6.35711 | -55.15627 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c771d41-8901-3c7c-a930-8b371119c369 | -11.20137 | -49.93967 | 2026-10-10 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8fc7ece-e20c-3941-aa6b-10bd80267e7b | -6.93489 | -59.26167 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 296cae45-6d87-35fb-a9e7-4d1e2a54135d | -12.77582 | -44.88065 | 2026-10-10 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f90030e8-a325-38d7-ad08-8d9527ca8d45 | -11.65861 | -43.67409 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b841d4ae-9a0b-3154-a902-98ea13504cd7 | -8.1491 | -49.43864 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac2d16b9-82d1-38a1-9f1d-973ddb805b49 | -11.78627 | -46.8072 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 518f2a3a-43ad-333f-a16e-d9c5227340cf | -6.43867 | -55.27835 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13161f9e-d39e-306f-99b8-eda28f5d75d7 | -10.93876 | -45.37165 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63ac5b48-0559-3cbb-ae94-3869c52f9610 | -7.52482 | -45.31001 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 80b6e323-cc6b-36e5-8a3e-0cc3fc80e543 | -11.0295 | -44.02565 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aac542d1-2cdb-3790-b098-f212e3d74bec | -6.80436 | -52.77982 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04a48f0b-d8d0-3a05-89a6-335fbeebc661 | -6.08951 | -53.49771 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4e351c4-22f3-3e90-b071-b96511032ee0 | -13.52515 | -47.42388 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e6c1a5be-2472-3c05-b64f-3a2fa88cca4e | -9.93545 | -44.89214 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3ac3fe1-1bc3-3f17-b738-2b3c07aed17b | -12.30433 | -47.04464 | 2026-10-10 04:46:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3629d411-4dd5-3c10-803c-f1eb91d7f5a7 | -6.77793 | -48.66737 | 2026-10-10 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10969017-7ddf-3da1-b61e-4b9f2236da72 | -5.88745 | -55.53355 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3506414b-6257-3f38-91ff-f977d235a254 | -11.03364 | -45.43235 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb51ce73-2fde-3f02-bed2-384e6a8eb013 | -7.10377 | -46.71933 | 2026-10-10 04:46:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34104642-8454-324e-b827-f0c0cec97138 | -5.9469 | -55.34482 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 598d77ee-c216-3209-8bc0-8a6eb4264355 | -6.5439 | -55.29398 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb744bd9-e840-37c7-9b99-8c880cbfe0b1 | -11.75449 | -46.7955 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eabb4863-ae2e-3760-a2b8-ef6d4d8dbe91 | -7.92261 | -54.72324 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 189ba426-2686-38d9-a23a-9d224e7fe4a3 | -7.03779 | -47.6711 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d9e866cf-e584-3af8-a63d-8557c0092a71 | -7.90996 | -54.71618 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57303f2d-828d-3429-a5e1-b2437940f7d5 | -11.75917 | -46.78817 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 131c3f3d-784d-3083-bfcc-70ea27e4e4eb | -13.46522 | -41.35107 | 2026-10-10 04:46:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c14fd893-e707-31c8-8c23-03a319fea068 | -11.79554 | -46.72154 | 2026-10-10 04:46:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fbcc00b-78fc-33e5-9f64-61fe4a478435 | -8.49553 | -54.6087 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f82a7beb-c2e5-3b39-9f0e-801a5af39079 | -7.21965 | -55.06981 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7b701e5-3302-35d8-bc9c-ab31c71daa2b | -11.06842 | -45.77963 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3102c3b-b4a0-3c87-808d-2b7602218fe4 | -11.67407 | -46.78671 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f9c4f86-d8c4-3433-9169-fb96dc03f4be | -13.6356 | -44.42119 | 2026-10-10 04:46:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5acf6c95-f591-3706-8769-52378a8b521e | -11.48568 | -54.61882 | 2026-10-10 04:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b83a0013-603b-34e9-9deb-72999ba61d29 | -10.8946 | -44.80195 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a04da59-5308-300d-8c0e-ed50f0484f79 | -13.35862 | -43.92271 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c2bd907-cab1-3cd7-b1de-35d6949ab5eb | -6.92131 | -47.65998 | 2026-10-10 04:46:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55fd8c54-5329-3285-921e-89cc106714da | -13.67809 | -48.63852 | 2026-10-10 04:46:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cb7c3b0-203b-3dcc-b56a-cfbc1bce1bcd | -8.24587 | -54.72444 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9d2d76bb-ed90-3bfa-a41e-2883e3679312 | -11.92484 | -46.76763 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc04751c-9ce4-37e3-82e5-a9a78fbc651e | -12.37686 | -46.60854 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6ef5935-5aaa-36bc-ba81-c67415833f7a | -12.25453 | -44.42748 | 2026-10-10 04:46:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ed7b05e-17ae-3305-bffe-4934959e51e1 | -6.94456 | -59.10149 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41877d0f-0ab0-31f4-9c26-23c2c8e731ad | -10.25318 | -49.69201 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7f4562a-2f4d-3f88-847e-79d2d975f941 | -9.88335 | -44.79884 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ae4f965-1115-3795-895a-c13a0cdbc353 | -11.96642 | -43.47324 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11acc967-0475-3402-b6a0-ac431b11222a | -15.10117 | -43.63534 | 2026-10-10 04:46:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cee39217-3c72-3e81-9da3-1722172b8a6c | -6.48546 | -53.60668 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 553b08cc-8f85-3d5a-af6c-01db11df20c6 | -6.80092 | -52.77576 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c807562d-4c94-3774-aeae-332a99956aa6 | -12.24305 | -54.38794 | 2026-10-10 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d102a20d-836a-3697-bf4d-29e7ab501677 | -10.91787 | -45.51359 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95c5833a-c64b-3de1-a4a1-e9e4092770b1 | -13.10522 | -46.3567 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d2f7d21-3dd1-3fce-90b2-30e2fcbb80b3 | -7.24471 | -55.21123 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff207817-57fc-375f-8f56-afa90dca9b11 | -13.19381 | -48.1385 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d2737af-767a-330b-9316-3972817fc4d9 | -13.1507 | -46.33313 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e74cbcf0-cba1-3693-81b7-2102f5a37ae0 | -10.89325 | -44.81129 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 640bc7f7-fe84-3675-8b4a-92a9537fea6b | -7.17711 | -52.61874 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 406b7e06-1e80-3e69-a205-20fd3f60c2e7 | -9.71339 | -50.15231 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c03b612-9dd5-3893-8c72-2378a9f148c4 | -6.32539 | -55.3417 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f135572-f70d-30b5-a40d-27d1084f7476 | -7.52421 | -45.31401 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e7775ea-8f23-38ca-b0c8-e547b8fefe9a | -7.08687 | -52.68027 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aefcbcfd-aab9-3268-9d70-bb6f7d6b5244 | -7.23121 | -55.17854 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a89298b-885c-31f8-b5ca-ff71cfc5ef70 | -9.94488 | -44.87991 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c20a471f-81a0-340c-a424-01ae9e49b60c | -13.03595 | -46.81864 | 2026-10-10 04:46:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ce11879-310b-3c4f-a293-201435f847f0 | -11.97637 | -43.46303 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 274d0fe1-27ed-3cae-bfa1-d9e0ce3c448b | -6.73833 | -55.10689 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfe49fc6-62c4-3633-aa18-43345e3d2fae | -6.43835 | -55.05411 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6300f83c-8079-324d-b1c2-5f3bd2f4d864 | -7.03003 | -47.67702 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README74.md)
