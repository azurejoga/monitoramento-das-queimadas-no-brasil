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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dc7efee-368b-303c-9322-4da0b52b4ac3 | -10.6319 | -44.3257 | 2025-01-04 00:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 06024f5a-3df8-3c8e-9587-49bf93891d53 | -10.6124 | -44.3517 | 2025-01-04 00:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 78a3326b-cf2f-3e6e-917b-1e3518bb9194 | 1.34 | -60.3122 | 2025-01-04 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 5b863308-ecd5-3e6a-abac-8dfcf7d5c80e | -10.6128 | -44.3284 | 2025-01-04 00:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 7da105b8-3328-335e-a23c-9e479a4ea361 | -8.03135 | -35.13846 | 2025-01-04 00:09:00 | TERRA_M-M | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| ce5105f6-e259-32d2-8cd8-f203b709b7b4 | -9.24367 | -35.59543 | 2025-01-04 00:09:00 | TERRA_M-M | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| ebf06a36-ed6d-3840-8147-4e565a02dde6 | -7.85042 | -37.71431 | 2025-01-04 00:09:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4d075af0-2815-32f9-b55f-b49f4c7f99ee | -9.24218 | -35.58519 | 2025-01-04 00:09:00 | TERRA_M-M | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 033f076c-6cba-32a0-9658-228f825a6887 | -9.27841 | -43.05075 | 2025-01-04 00:09:00 | TERRA_M-M | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 4244136d-cfb2-36e1-9b6d-d904d1371b1f | -10.41905 | -39.86431 | 2025-01-04 00:09:00 | TERRA_M-M | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| a15f3aab-b829-3a17-86c0-09e7f9447352 | -9.48545 | -35.99343 | 2025-01-04 00:09:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| b397fbd4-e435-3d83-84f7-063a0275e303 | -11.76749 | -38.68409 | 2025-01-04 00:09:00 | TERRA_M-M | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| feb360bf-cb89-3396-a0a4-e6fbb7003b9f | -9.98371 | -36.38436 | 2025-01-04 00:09:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 97ee8fd9-0490-3a92-8c24-c2da5cab999e | -9.86448 | -37.09719 | 2025-01-04 00:09:00 | TERRA_M-M | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6ed96054-7fc8-3662-a4c4-0325bc23dab0 | -12.56433 | -39.62653 | 2025-01-04 00:09:00 | TERRA_M-M | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ba85a273-6405-3868-91a6-b053b51f629a | -8.50819 | -40.84069 | 2025-01-04 00:09:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| c36c5d1b-8958-3d0a-8df3-52a4b8dcbf0a | -9.62072 | -36.16411 | 2025-01-04 00:09:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 6ea09d98-8497-341d-b0e5-6e77bcd56e19 | -8.58963 | -35.10639 | 2025-01-04 00:09:00 | TERRA_M-M | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 0bcb6878-9566-3495-ae27-1778678a27c9 | -9.86575 | -37.10619 | 2025-01-04 00:09:00 | TERRA_M-M | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 17e99e66-9019-3720-b271-8ffad4a2e5b8 | -10.54501 | -36.89838 | 2025-01-04 00:09:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| bef86e07-7191-3bb5-ad8d-75fac9235581 | -9.84873 | -37.12382 | 2025-01-04 00:09:00 | TERRA_M-M | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 44ead6ee-50e2-3626-ab2a-3534750ec415 | -7.85167 | -37.72321 | 2025-01-04 00:09:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| fb5422d8-51c5-3623-aec5-2be6c126ac55 | -8.4353 | -40.6636 | 2025-01-04 00:09:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 5f2f056e-2b5b-3708-a99b-1d0d9aba12b6 | -9.90287 | -38.10859 | 2025-01-04 00:09:00 | TERRA_M-M | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 4fb7b629-2565-35dc-9df5-14abf92aee90 | 1.34 | -60.3122 | 2025-01-04 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.1 |
| bd30b6c5-9803-3be9-a54e-92f732b4ea90 | 1.3583 | -60.3121 | 2025-01-04 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d449b909-8d64-3008-a7e3-fbd77f268d7c | 1.3401 | -60.2932 | 2025-01-04 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 00df7b3a-2e48-3970-9a38-7aa75691ab49 | -6.34722 | -39.56523 | 2025-01-04 00:11:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6f727776-6b65-32fa-9220-14fd405a18a5 | -5.99714 | -41.13942 | 2025-01-04 00:11:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 6ee6f87e-6c2f-38a9-a6a9-73a9c7dcbb65 | -2.96758 | -41.86235 | 2025-01-04 00:11:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 9df98625-fdc0-3728-a562-ef1c19b2f4ec | -6.08252 | -39.85165 | 2025-01-04 00:11:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0cbe8517-71c0-31c6-8a53-deb36276b5e0 | -5.8572 | -39.41425 | 2025-01-04 00:11:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e19d10bf-ee63-3c00-a6ce-e9c8074f16f1 | -5.14651 | -39.4712 | 2025-01-04 00:11:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e20837a1-5262-33c7-9f22-894b8449bbac | -2.96371 | -41.85775 | 2025-01-04 00:11:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 7fd27fdd-d914-3d63-bbfa-344ff4e2a9df | -4.52082 | -38.68439 | 2025-01-04 00:11:00 | TERRA_M-M | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2a915072-49dd-304e-8a21-ef034e5bba06 | -4.38703 | -47.74105 | 2025-01-04 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 3e0920b0-d266-34bb-8733-390e0e12992c | -7.29187 | -34.98705 | 2025-01-04 00:11:00 | TERRA_M-M | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 8f35dc34-ff2a-3fe3-9355-547968284b29 | -5.72257 | -39.5099 | 2025-01-04 00:11:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 8174911b-7601-3d98-ae65-d5d432e5f049 | -4.91763 | -39.01727 | 2025-01-04 00:11:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0621a2e6-a2d7-3094-b43b-f0e4f5e9e798 | -5.24104 | -37.70884 | 2025-01-04 00:11:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 037092bd-39ec-3307-9546-fe621acdc807 | -5.62966 | -38.6426 | 2025-01-04 00:11:00 | TERRA_M-M | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b276ab0b-71a1-3704-b431-ec1395eab975 | -6.704 | -39.14875 | 2025-01-04 00:11:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ccf248df-31cf-3dc4-8624-753d1a1cd50f | -7.48373 | -37.07702 | 2025-01-04 00:11:00 | TERRA_M-M | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a8a8be41-caf2-3ae3-9d3f-f74b5e5909a8 | -5.23978 | -37.69978 | 2025-01-04 00:11:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 66aad530-8b1b-3172-96f1-35aea5da4d0a | -5.13884 | -39.48143 | 2025-01-04 00:11:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a57f4b3e-01d5-3285-8fc7-a90dc45eed05 | -2.96615 | -41.85169 | 2025-01-04 00:11:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 96af3b0d-539e-3116-8741-f5a96c217a66 | -5.20161 | -39.73944 | 2025-01-04 00:11:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 6cbdfa8e-6708-3e08-b66d-04e71c40fc09 | -5.51083 | -39.11365 | 2025-01-04 00:11:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 44cefa9f-08bc-38e2-83af-913dd50d1370 | -5.1376 | -39.47246 | 2025-01-04 00:11:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9a401b5a-237c-32a6-9f91-11a1dd2d5f72 | -5.71834 | -39.61211 | 2025-01-04 00:11:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 579663be-4d25-3333-9c61-a9b54b96c0dd | -3.00014 | -39.9373 | 2025-01-04 00:11:00 | TERRA_M-M | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 37ec12c8-204e-3f32-94aa-36c415cac072 | -6.44427 | -40.00653 | 2025-01-04 00:11:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 1e378483-6d6d-360f-97e4-df9b047d6f5b | -6.97853 | -40.01186 | 2025-01-04 00:11:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 182b28a9-5614-3839-ac5a-f12b82ea34d6 | -5.50959 | -39.10475 | 2025-01-04 00:11:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| c40522a1-82dd-329a-87b1-974616c86add | -6.57347 | -37.15728 | 2025-01-04 00:11:00 | TERRA_M-M | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 7a908b31-4200-36a0-8f10-4106b586c84e | -6.18562 | -36.5616 | 2025-01-04 00:11:00 | TERRA_M-M | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6954042f-2a88-3199-a819-97214000b309 | -5.71959 | -39.62123 | 2025-01-04 00:11:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 5c4d79de-f8fd-3f54-8f98-c71f78fc7367 | -7.60385 | -41.25095 | 2025-01-04 00:11:00 | TERRA_M-M | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| f84e3548-52da-3b5a-9123-4396b5fa98e7 | -6.83388 | -35.07503 | 2025-01-04 00:11:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 33d4f6be-d42b-3070-8fad-558f59561dd4 | -10.6319 | -44.3257 | 2025-01-04 00:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 63436252-c86f-38a6-b48f-895ac0942bc5 | -3.8604 | -47.2849 | 2025-01-04 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0604c64e-7446-31ac-a1a3-cb643adfb09f | -10.6131 | -44.3051 | 2025-01-04 00:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| f38a2797-70f7-3f69-bac5-40e600a91c61 | -10.6128 | -44.3284 | 2025-01-04 00:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 8ced4d7f-9701-3b9b-b7f9-15c1277e85cf | -3.879 | -47.2841 | 2025-01-04 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| b2133d3f-1a5e-31df-87ca-a283dca3c3d4 | -10.6124 | -44.3517 | 2025-01-04 00:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 9dccb2df-4850-3f4b-8a67-b4e1da1e6c42 | 1.34 | -60.3122 | 2025-01-04 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.8 |
| e79fc56b-a079-3c01-b30a-21b5f2be0a7c | 1.3401 | -60.2932 | 2025-01-04 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e8e4da0e-5c94-361c-a199-88bf0dfff1a3 | 1.3401 | -60.2932 | 2025-01-04 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 3685b33d-b499-3dff-85ea-ccb23307124b | 1.34 | -60.3122 | 2025-01-04 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 5d94906c-f908-3dd8-a486-86f7ffb29f60 | -10.5469 | -44.670601 | 2025-01-04 00:34:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c7763e0c-770e-3923-98fa-5e103e4696ba | -9.8511 | -37.1171 | 2025-01-04 00:34:00 | METOP-C | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| c4faeeea-1400-3ade-a7d2-9d7421dd3261 | -5.9104 | -48.072498 | 2025-01-04 00:34:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b82a030-0ab8-3b8f-b577-b98c1a14db27 | -3.8647 | -47.281799 | 2025-01-04 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ea0a5b3-a554-3f58-aa17-6a6cfe55ad8a | -10.6162 | -44.345501 | 2025-01-04 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 935ec9b9-47ba-308b-a730-313af5f636c3 | -12.5014 | -46.3367 | 2025-01-04 00:34:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66bf8c9c-9c43-3827-95b2-e9131feff48c | -9.2787 | -43.043499 | 2025-01-04 00:34:00 | METOP-C | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ee939331-2261-34e7-89be-64bb0e8df64a | -6.9777 | -40.004299 | 2025-01-04 00:34:00 | METOP-C | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4ca33590-41a7-35e9-b091-ef21ed0abb80 | -5.4184 | -46.861698 | 2025-01-04 00:34:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8966ed0e-c8b3-3737-8e32-9999c2fb38a7 | -3.8745 | -47.279598 | 2025-01-04 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09894df4-3161-3f94-b3bc-80d0f1d30bc9 | -5.7187 | -39.613499 | 2025-01-04 00:34:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c39a2e4c-0348-3134-a039-41ec909c23d5 | -5.5056 | -44.294601 | 2025-01-04 00:34:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13aef674-9c7e-3532-8c17-68df4a01711a | -9.2903 | -43.049301 | 2025-01-04 00:34:00 | METOP-C | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 48c30f46-18d0-3f52-a929-9739f39b54f2 | -10.6129 | -44.3311 | 2025-01-04 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c584c09-64a9-3813-b43c-f68d34c20b76 | -9.2884 | -43.0411 | 2025-01-04 00:34:00 | METOP-C | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 205d6df6-4dba-34aa-bae3-4f5776721594 | -9.856 | -37.135799 | 2025-01-04 00:34:00 | METOP-C | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 128a9166-01fe-38d0-a50a-1d8f21c0330b | -10.6145 | -44.338299 | 2025-01-04 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0529d1-dfe5-366c-8e84-9c60a4c06723 | -12.503 | -46.3438 | 2025-01-04 00:34:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c977889-20cc-38e0-b665-3711bd1afc8b | -7.6913 | -35.4048 | 2025-01-04 00:34:00 | METOP-C | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| c6db1c95-ae99-3302-a263-07eaeaa87209 | -10.5485 | -44.6777 | 2025-01-04 00:34:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6f57e03c-7ec7-3f09-aa25-3c357106c4d5 | -3.8761 | -47.2864 | 2025-01-04 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b005ff-80e3-3046-9e21-78e8cd770a3e | -3.8663 | -47.288601 | 2025-01-04 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3b0ae4-c2c7-3f94-873a-31b40e7cd1a3 | 1.34 | -60.3122 | 2025-01-04 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 102.7 |
| e07f4218-4a19-3aaa-b367-24a1c05629c1 | -3.879 | -47.2841 | 2025-01-04 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 9c1489d1-ad4e-30ff-8a62-2e45fd9ecdb5 | 1.3401 | -60.2932 | 2025-01-04 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b6dbb406-58e5-302f-9c55-5f4f01876718 | -5.2607 | -37.7172 | 2025-01-04 00:40:00 | GOES-16 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 56.1 |
| e63be206-386c-31d5-956e-5073e390cb65 | -10.6124 | -44.3517 | 2025-01-04 00:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| c2f6be43-fc83-3979-834c-27092df5f6ac | -10.6319 | -44.3257 | 2025-01-04 00:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| ffba3dde-ed83-3c32-8b08-553fa441bfc2 | 1.34 | -60.3122 | 2025-01-04 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 205ab99b-dcdb-336e-931e-f4d647e34992 | -10.6128 | -44.3284 | 2025-01-04 00:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 62fef36e-6f0c-3177-89ff-3ac701074b56 | -10.6128 | -44.3284 | 2025-01-04 01:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 220.5 |


[Clique aqui para ver as próximas entradas](README2.md)
