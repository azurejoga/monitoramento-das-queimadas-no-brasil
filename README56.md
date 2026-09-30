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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff7e4c6e-fc1f-32fd-809b-5c43334a03a1 | -11.35942 | -50.9798 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c549bb5-bb15-335c-a708-ff2f9a3fd4dc | -11.40314 | -50.9755 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cde69b3b-f01e-3ea0-abe8-65f6f3b5ffaf | -20.50456 | -49.62988 | 2026-09-30 04:55:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 143f6e24-b6ab-38ef-8675-502c0d45199c | -18.88263 | -43.82125 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68b8c0d4-0091-3b8d-ba42-65661ca51cf5 | -18.8868 | -43.81341 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5acb1eca-11da-388e-be21-7e3336a49f5c | -19.21631 | -44.76136 | 2026-09-30 04:55:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93b4920c-5943-3d10-b365-cc9d8ed0b060 | -11.80239 | -50.4392 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| deda35a3-9d62-336a-8390-a223472b62c9 | -12.19509 | -47.11236 | 2026-09-30 04:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2800b29f-7869-3a1d-bc7b-0bccbe0ce287 | -11.79133 | -50.44656 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 456c7d99-c22c-3fe4-aed6-823eb8ce03ee | -11.32181 | -50.9776 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd628263-40da-3fa4-9c50-890865353c91 | -11.32462 | -50.98176 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30c78758-86b8-3e27-b56e-67315308c924 | -11.82247 | -46.9027 | 2026-09-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34ee750f-8481-3ed2-8d41-7154de7fec91 | -18.89598 | -43.80285 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd5a187d-21e6-3539-91e2-fbbda613116c | -12.76907 | -47.25271 | 2026-09-30 04:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7511b864-3447-31b0-a568-fbbf04246228 | -11.79782 | -50.44625 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ec1d289d-8d6f-3b7e-8fbc-0c6355915602 | -18.23392 | -53.01946 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d492e53-329c-3c99-a7b8-0bb487e7e96d | -11.3813 | -51.01674 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c959b809-2874-3bd9-b7f3-7489c71fb71d | -11.79895 | -50.43867 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b703d85e-8d93-3d3e-b70f-83c415e73601 | -12.15026 | -47.20142 | 2026-09-30 04:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3b255884-5a2c-322e-84cd-67ba13ce0d4f | -12.79022 | -54.01382 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81c845a9-5798-33a6-a8cd-88832d05f3d7 | -11.34765 | -51.03373 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f657af42-206a-3b13-b4f4-bc13f95a96d5 | -13.42672 | -43.81136 | 2026-09-30 04:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50079dbe-a339-3d81-adec-23fbf16fa867 | -11.80525 | -50.44353 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07effeeb-a2fa-3f83-8fa8-4fbbd4106517 | -11.82987 | -50.46677 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 385bb3fb-5cdf-332d-819b-728c54940995 | -18.28248 | -53.05392 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a68303a-2926-3b61-b8fa-4ef013d95c30 | -12.7823 | -54.01997 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ffa2309-e204-3f1c-ab65-d829357eb387 | -11.32635 | -51.0378 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c54797c8-9cf9-32e7-8089-b33877f29911 | -12.30669 | -47.95507 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4a65bab-4ee5-3c2a-bf38-9bc66feb0a77 | -11.83845 | -50.43315 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 848e7807-5b2a-3236-8109-2bbcfaf36628 | -11.85352 | -50.95884 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1bb759c-0cc6-3b17-b2f3-d0f9bc66a3ff | -11.36166 | -51.03223 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57080744-176d-3d37-bb4e-74281e4132d4 | -18.4973 | -45.14986 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84ef2c1b-4b59-38c1-9cbd-f35129270d0c | -11.38638 | -51.01756 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f047651c-2091-3844-b895-b7b70d4c0cda | -11.39141 | -51.00719 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d1aba6ad-f2d9-3012-9b0f-ccae7508df90 | -13.53735 | -49.18422 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2fa1ef3-df04-34f3-a06f-c7bbe64e214c | -14.19874 | -42.0779 | 2026-09-30 04:55:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 6bf2693b-4909-39dd-8eb0-47d3451c89f4 | -18.88905 | -43.81439 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ec79e5ec-4c52-30d0-9f9a-df2e91997bdf | -11.84791 | -50.97299 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50bd4dd9-17fc-3556-9f7a-606d701658bc | -11.30892 | -50.99417 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de683220-5452-3937-b488-e6c0a996d4fb | -18.49837 | -45.14038 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7dff73a-c524-3619-aaf8-4e85b484f4e1 | -13.53064 | -49.17817 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0746f19a-1861-34b8-aadf-5ebd7f090790 | -18.27914 | -53.05336 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5515600d-ba5e-3ff6-a48b-a826f3e9629c | -12.78014 | -54.0121 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41eb286a-b98f-360b-93f1-eef544c159d2 | -18.33416 | -53.07396 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5661c638-4557-3573-a04e-6a4b0362b22a | -11.98644 | -50.88879 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b089b1b8-6cff-3d39-b931-a134629d850c | -20.5013 | -49.62404 | 2026-09-30 04:55:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e985ef81-0c15-3d46-bb89-b41be7250f15 | -18.26857 | -53.05536 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58b5f4bb-a114-3e01-a7ce-41805ec8d079 | -11.35212 | -50.98236 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a79780d-7048-3818-8426-32312b4c4442 | -11.81958 | -50.46517 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18e42d3e-82fa-3a16-a728-fdac31edcd77 | -18.26523 | -53.05479 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 989df216-5214-370d-ab02-3c931875e001 | -11.84676 | -50.95778 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc67daa9-f0e4-3372-add2-3d4a3e100747 | -11.40369 | -50.97186 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d3d89d8-1979-388e-ac11-2148296a05ec | -12.34349 | -48.19766 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| baf9a8c8-62d1-357d-a160-0ce7d7415e7a | -22.99991 | -48.61995 | 2026-09-30 04:55:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a58fd5e-3e8d-32c9-a1ba-38f5e8755701 | -13.54536 | -49.18104 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d36db2e-ec6a-3209-ad11-5998de051b38 | -18.2775 | -53.04174 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcca90fc-e253-3749-8c4f-6e2441e3e48e | -18.88983 | -43.80709 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a10233fa-59d6-3a78-94e3-7c9cd78bf4ef | -12.24034 | -50.25395 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7fdb4ee1-3b8b-3666-b408-b031fe118116 | -11.39751 | -50.96715 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a878970-d9fc-3141-8782-4cf5ef791953 | -11.29431 | -50.97698 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2205364e-a98b-3f42-bc47-5cf89d85b067 | -19.19009 | -46.81299 | 2026-09-30 04:55:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35c7b392-b22b-3320-9f84-95297b83a22a | -12.43552 | -44.17167 | 2026-09-30 04:55:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f35ad30-b907-3a54-a48f-9b9b49139a69 | -13.68714 | -44.0827 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c2d6ecf-f49d-368d-bb8a-7982bb341adc | -12.78648 | -53.9945 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 374286ce-695e-32d2-9e3c-1341d887d85a | -12.30739 | -47.95007 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dc08676b-2b0b-3be5-be8e-65a80d718986 | -11.40088 | -50.96768 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4b2b282-930b-3da7-b1ae-f7e08df3d95c | -11.40373 | -50.99423 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe39925a-b3ff-3b8c-806f-6c1285e71b8e | -21.38308 | -45.31271 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e403d591-34b7-30f0-9f49-445626d091d2 | -12.78805 | -54.00597 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0190fad-65cf-37d0-90a6-0a223126d3bf | -11.82184 | -50.42668 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 561aea3e-f3a5-348e-9517-90c764b3a867 | -11.37344 | -51.02294 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caa5c9b2-bb45-31d1-9b81-53d1cda51b8d | -11.80412 | -50.45112 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| fa2e17dd-d984-3c4f-bdfd-9edc938f2680 | -12.30276 | -47.95464 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48b1d4ff-1301-3ff3-bead-a3b2c15c3147 | -12.76548 | -47.24833 | 2026-09-30 04:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b579a09-54b8-31f1-bf36-e30f53175f9c | -11.79878 | -50.44384 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 37f33fca-9986-3ec7-b7f5-304a007cfee5 | -18.5945 | -43.4438 | 2026-09-30 04:55:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 05ad98d4-c64c-3d37-bab2-233f57f29fa6 | -11.79725 | -50.45005 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c6324272-eb2c-3cf1-9dec-32ee53850b99 | -11.83331 | -50.46731 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d5d811f8-cb9d-34c5-bb61-e90db68d308b | -13.33414 | -43.96242 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9467c0ba-49ff-35cc-9bfc-24cf7fb9181c | -12.23687 | -50.25341 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fa189e84-d955-3fd9-aee1-db862963b06a | -11.39925 | -51.00098 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0aeb5d0-8f31-34ca-9e1c-d131b13ffb95 | -11.39196 | -51.00355 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86bb0394-d18d-3ab2-80f0-7120c57a2541 | -18.23278 | -53.02682 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b62833da-6e85-325d-9a48-50f9747e305c | -21.06167 | -48.47535 | 2026-09-30 04:55:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d5baf00c-3adf-307f-b24f-b1d88d5d3806 | -18.25634 | -53.04575 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e4a6a6ab-0056-3b5d-981d-ac135528f7e7 | -23.00476 | -48.61617 | 2026-09-30 04:55:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 529ecdd4-840b-39b6-b888-dfe435347ecf | -12.43513 | -44.17468 | 2026-09-30 04:55:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| feac6736-e0c0-3a42-bcf3-c159b827862a | -13.33068 | -43.93912 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93db3ae1-bf06-38e4-8aa9-d909d452726e | -12.77894 | -54.01939 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 134c9fa7-8d64-379f-bd73-51788bdc55a5 | -11.82413 | -50.43481 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e27c6e62-b1ae-389b-b9c5-c2acd06513bc | -11.79762 | -50.45142 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 450917e6-6794-3213-a3af-402460420206 | -18.89906 | -43.80466 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b24a0b4e-e295-3cf5-a73b-ce65b7067479 | -11.79936 | -50.44004 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| fbc8d6bd-75d4-3761-b487-defc023b96b6 | -12.24093 | -50.25006 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0d68304-3c1c-3c93-9a9e-99183015a234 | -12.62905 | -48.35551 | 2026-09-30 04:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a50e4526-64f6-32f6-b462-a6d438e4d6d4 | -11.38749 | -50.97676 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea7be58f-f15c-39c6-9c1c-697498d1efb6 | -12.78626 | -54.01689 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09147b09-3574-3e93-9cdf-3d239b549d11 | -11.29712 | -50.98114 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b9325e2e-aa65-3212-9efa-e02327c3cff4 | -11.8293 | -50.47056 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e6c115c9-7f5e-3510-8027-2c81e65eaaf7 | -12.74728 | -54.05568 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README57.md)
