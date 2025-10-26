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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a93f3ad-339a-343e-959f-7805f45bc354 | -13.64254 | -47.62727 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d40f6093-0fc1-3408-9ec7-1d1e4a812192 | -8.31526 | -46.81208 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e06ce7bb-c845-3b1c-b2e3-af1c59d7a137 | -7.80251 | -45.3979 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cf186e67-45c3-3cc0-95f3-36f452521c95 | -13.85234 | -44.35954 | 2025-10-26 04:51:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cf2264e-3ced-34c4-b61e-82e28a1e89f5 | -11.16635 | -47.79594 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8115146-b506-3a46-bccb-067cc4bedddf | -7.85403 | -45.37424 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 164b72a7-5dae-389b-a2be-54d833f9244d | -9.59984 | -47.69263 | 2025-10-26 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63210fb0-fa4b-3a24-a2ce-c36fc44a75a9 | -12.83585 | -48.65436 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5390a648-c90e-3e2c-9a8c-69daa021b830 | -8.41204 | -46.92194 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1253d5b9-43cd-3383-8ece-d6cf85bc8b4b | -12.30525 | -47.4646 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7c35c9e1-7879-3153-9138-712019856747 | -10.60067 | -47.86435 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cddecac-440f-3199-8be3-2784388aa7cb | -13.90023 | -48.44693 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f679ff90-91e4-31c9-b947-621f93d8483d | -10.99387 | -44.86507 | 2025-10-26 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaedfa47-9a3d-3479-9d70-9cdd08fdfe3e | -10.88988 | -47.94872 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68f96a16-0706-3221-8f0e-43941ae68e32 | -9.96797 | -49.05063 | 2025-10-26 04:51:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 261d567a-1682-3cb8-83e8-d5b92bc16c81 | -7.46248 | -46.64076 | 2025-10-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2c2d6ea-a35d-3e36-88d1-64e13a7c8841 | -8.21099 | -46.94051 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d8e9142-5eca-36f0-9713-dc45f30c9db7 | -11.11619 | -43.22502 | 2025-10-26 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc7ad3ba-20f3-3402-990f-10ce2ca31024 | -12.76071 | -48.62479 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f977540-e9c5-3ce9-b13e-4cf84fc2c463 | -10.98223 | -47.87801 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 929dd2ef-09f4-3b42-ac24-e96cdb465171 | -10.41547 | -44.50072 | 2025-10-26 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa2a06a2-7f1f-32f2-b288-bbae23b68a9a | -11.28739 | -54.181 | 2025-10-26 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3691e3f-7d23-3c70-97be-53e485b35897 | -13.89083 | -48.42038 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4c065ec0-cf6f-34cc-a7f6-dba876d9708e | -10.41587 | -44.49758 | 2025-10-26 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82886f15-770c-3902-a618-d0a28defcb02 | -8.03196 | -41.19676 | 2025-10-26 04:51:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5764ab5c-766d-371b-b1f6-4b9655d6b00e | -13.6438 | -47.62195 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87a44c84-9f01-3d43-b39e-88dfa3353ec5 | -12.31615 | -47.48359 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1d85854-b7d3-3492-9b08-458d0c2ed358 | -14.47228 | -45.28173 | 2025-10-26 04:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82c9203c-137b-3044-867c-c58fa6fcdf34 | -9.1616 | -51.30218 | 2025-10-26 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e77a05a6-7a15-3d96-b35e-b262ae51d074 | -10.59607 | -63.46287 | 2025-10-26 04:51:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86cf29cc-1aee-3fe8-a86c-c9ee6b1ae825 | -10.79418 | -47.61274 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0f4d710-488b-3503-9753-028e41498645 | -10.45484 | -44.99824 | 2025-10-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a00c4ffc-3a7d-3e33-998f-c14779c7189d | -12.76445 | -48.63004 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7615d35d-af83-39d6-a070-d39013ebc1db | -12.04628 | -54.24802 | 2025-10-26 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11f5302b-ec36-3d47-af84-7343e7488dd2 | -13.90076 | -48.44287 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 507f8dc6-d4a6-3131-947d-2435a216db90 | -11.2703 | -54.18182 | 2025-10-26 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62fad065-08a9-39c9-ac42-3ed54fce5694 | -8.32812 | -48.18682 | 2025-10-26 04:51:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a552eb43-5a9b-3c6d-83eb-267db0e49f2c | -11.91271 | -55.37666 | 2025-10-26 04:51:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04693472-3873-3af5-a6d6-e4ed7a9b6a26 | -10.81296 | -47.88987 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd84a364-f7b1-3606-8fc8-e690a2020f92 | -11.47996 | -43.24291 | 2025-10-26 04:51:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 59511c28-4281-3178-a1b5-7c9dc5ba9d50 | -10.81149 | -47.88995 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 414f3231-3ad6-3820-ac77-36ae0d049c04 | -11.88122 | -56.4063 | 2025-10-26 04:51:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 460b929d-ec97-3724-91c2-80a08753a7b1 | -10.82458 | -54.18131 | 2025-10-26 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3aed27bd-1d87-36c6-87c3-8ab4295b50ee | -8.03397 | -41.2018 | 2025-10-26 04:51:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 82cb97be-b11c-3332-b0aa-61f8e207eb08 | -10.90257 | -48.02701 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 864ed95e-303c-3e0b-b993-18e4f2edc3dd | -11.28795 | -54.17749 | 2025-10-26 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83d2bdb7-4cd1-3d98-ae28-a857ae7bb8f1 | -7.79309 | -45.38541 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66cc9484-10ec-3d50-b745-04443901f33e | -12.84222 | -48.63833 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 763f7e7d-9106-3fc3-bdd0-c35d46b9b67e | -6.81544 | -49.34919 | 2025-10-26 04:51:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae92b86b-15d9-31c5-a64d-ff16ceb7d895 | -8.91287 | -54.9321 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc734679-41f4-30e0-aae0-3f39dcc3eb81 | -14.17428 | -44.33694 | 2025-10-26 04:51:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb3bfb0f-af1a-3d1b-ab69-509937769adc | -13.2652 | -54.39448 | 2025-10-26 04:51:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9def1030-859c-3a5b-9b54-66619e50d273 | -8.33025 | -49.31044 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 490f9b34-09b6-3547-85d6-3160c2c247e2 | -9.93023 | -47.64745 | 2025-10-26 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6db8a34d-e70e-3915-b8fc-e163b834b936 | -7.8014 | -43.16018 | 2025-10-26 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a07beb2b-dad2-34dc-a1aa-4b16e89e9a0f | -9.28747 | -57.54568 | 2025-10-26 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8c10e66-6898-3d4d-9d56-692a1d7ca6cf | -13.00751 | -44.01474 | 2025-10-26 04:51:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2ac6c31-319f-3966-8f2e-8b323fcb9906 | -8.61254 | -54.66159 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25a7227b-bc6f-3959-a37f-b482c6690db2 | -8.12458 | -44.80532 | 2025-10-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a21fe741-7879-3834-b410-ebf9e690c9d8 | -10.76676 | -44.22623 | 2025-10-26 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74653d8b-2aaa-36b5-a121-7a1844f3f9b0 | -13.53216 | -43.00942 | 2025-10-26 04:51:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 681e5ecb-a24a-3add-a29f-969394c4b108 | -11.21622 | -54.84003 | 2025-10-26 04:51:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a679d6f9-a30a-38e4-88ad-dc348cb83c84 | -10.45049 | -51.7948 | 2025-10-26 04:51:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aebf0ea4-5082-3694-bc7e-fabbad241f57 | -8.02355 | -46.83252 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9021e127-01bd-35fa-9b8a-1edee6fb9cda | -13.87982 | -48.47241 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b7bee80-dcf0-3148-b558-4b3fbe22a32b | -10.86492 | -47.94512 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c486664-0cbc-3ccb-9e5e-699d2abb2710 | -13.40077 | -43.01766 | 2025-10-26 04:51:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 31d7ce8f-9313-3b94-9a1a-3999f35c77fe | -13.87698 | -48.39106 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6e7347c-259b-32b9-9663-3de39f5ea36c | -10.86549 | -47.94101 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c43417d-6d36-34b5-8560-b90610c28430 | -13.63891 | -47.62485 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d73b1495-23fd-3eda-b3f3-17e809e15321 | -10.89168 | -48.02634 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f10f8f7b-709f-3a27-aa46-2ac7bf7b5556 | -10.22204 | -51.00953 | 2025-10-26 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 151e503f-118a-3ec6-8546-9ec578e97e86 | -11.10307 | -55.55663 | 2025-10-26 04:51:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 305494fe-eda4-3e9f-9cba-ba4a12866a84 | -11.63008 | -54.55276 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 697b581c-2b68-3fba-af6d-3ca9340c9679 | -8.61007 | -54.95643 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ce81679-86c2-320d-ab4c-7aad1ec0f507 | -9.05507 | -46.98617 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 646bacdd-4214-3add-8583-e642ffac73f2 | -12.14363 | -47.0178 | 2025-10-26 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57d7452a-d40f-361c-bd7b-62ce24f524cf | -8.45055 | -45.12189 | 2025-10-26 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 817ba239-5b68-38e6-819f-91497469b037 | -12.00381 | -48.93732 | 2025-10-26 04:51:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aa890af-f2f2-3f0a-9436-07174a3da493 | -12.08018 | -56.67537 | 2025-10-26 04:51:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e462b3ff-95ed-3948-98ea-4f94ab5126fc | -12.35816 | -48.10596 | 2025-10-26 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d37b5c3-9b76-3bf3-8267-e05ee6ea55f1 | -12.8363 | -48.65108 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4efcbcf-3c9c-3586-b420-b8b16c97f17a | -12.91378 | -54.72118 | 2025-10-26 04:51:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49721112-ce09-37e2-b919-118d6f9b8462 | -11.09385 | -45.73308 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d0d49ef-66db-3c1f-9239-52addc00a76c | -9.16444 | -51.30643 | 2025-10-26 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3c9960a-93e8-326d-8193-7f3413fbb273 | -10.78996 | -47.6119 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a22bed57-477e-3848-b3fe-12394a001e5f | -8.32683 | -46.79264 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbe7f478-eb9e-33ca-9d24-8cfe57e3a887 | -11.84482 | -49.85808 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 903ec227-6b85-301f-9be0-ebf773a0f170 | -10.99002 | -47.88342 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ad973db-2a01-3f3b-a852-92b36bec1ee9 | -9.89608 | -52.19439 | 2025-10-26 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e7d8545-19ad-3e2e-828b-0445299c1dfa | -12.98083 | -49.9417 | 2025-10-26 04:51:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7be6685a-b932-34d6-b295-2c1921e1872f | -12.34922 | -48.10873 | 2025-10-26 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f2db2ef-1c04-3a9c-ba39-f789cbcd33f5 | -9.63488 | -57.01139 | 2025-10-26 04:51:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92c3f010-8d32-3a2b-b068-bde530056adf | -10.48546 | -55.61529 | 2025-10-26 04:51:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 761bd554-b763-3fde-85ce-56c413957c93 | -12.86132 | -48.65087 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6a4a0ae-3fb0-3b21-9594-3273ffbca62d | -7.6156 | -46.81588 | 2025-10-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06eb81f8-5f78-30bc-a294-a015a3614a39 | -12.86542 | -48.65136 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3cf9b83-e728-31ae-a7f3-89f017148544 | -7.84503 | -46.44563 | 2025-10-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bde680a7-255a-3e62-a9d4-816839d9a8db | -11.02199 | -47.80721 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6aac34d-63f0-32d2-a365-4457683fea98 | -13.87153 | -48.4704 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README42.md)
