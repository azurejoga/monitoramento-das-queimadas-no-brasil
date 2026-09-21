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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2a70213-3b38-363d-a24e-c4e5ba1c3d02 | -5.97878 | -57.77461 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e7fefa11-e1f9-38a1-9e00-8adeecfb973e | -6.73834 | -55.07124 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1f0f132f-d051-3531-a724-e17a8934bf55 | -3.3098 | -59.45893 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 95ab4b80-83e2-3ddf-8b7d-506ec71d148b | -6.15149 | -57.84229 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9afeaba0-19ba-3cb1-906b-c05ba617efdc | -6.61824 | -51.43567 | 2026-09-21 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7f56a4a3-18c5-32e6-a2b8-1c477434e8e6 | -5.2603 | -55.91849 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 395b88ce-def1-36f7-a0b7-843acdeac52b | -2.85938 | -57.63249 | 2026-09-21 00:22:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 42bae6e6-532f-3c2c-948e-d99fd05303b5 | -5.9318 | -59.95003 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| dea22b05-0267-3ac3-bd82-ef26ad050a60 | -6.7606 | -59.10942 | 2026-09-21 00:22:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 10721006-6f64-3adf-9d14-d8190bf37015 | -3.75358 | -58.33093 | 2026-09-21 00:22:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1e4448b1-f7e3-37e4-bd2f-f17d0bf590ad | -6.72709 | -55.05477 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6b0f6a0f-d859-33a5-9b84-11f85fbe237f | -7.40605 | -55.17089 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8ef7ec73-9e27-35a4-b999-3c39f33d0306 | -5.93391 | -59.96601 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5705e091-fe25-34f9-8c36-ac4552842486 | -3.33479 | -59.83904 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8577a3a0-42a2-36f2-adbb-00b8af65bed8 | -4.94395 | -55.82462 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9c5aa939-c3a2-3ef0-80d9-8dcc21c82e7d | -7.60061 | -57.67934 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 0440e0e8-11c9-30ce-9c52-9b16ab6e9556 | -5.85535 | -49.80872 | 2026-09-21 00:22:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2a6c1c1f-3e35-372e-90bf-329f20f24668 | -2.8736 | -57.80624 | 2026-09-21 00:22:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 93f4e190-f3d6-3d5a-b1d4-34c9d270ee34 | -6.14802 | -59.95206 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8856ef72-ba54-31d3-9cc8-9620dcabcbe4 | -7.24646 | -55.62006 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 674d75de-34e1-33c4-b326-7d96a1b4a507 | -5.77054 | -57.59156 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 37adf736-c3e9-3378-9c58-c28273c7f8a7 | -7.28546 | -56.45889 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0553ca26-95ee-384d-aef6-74797f27bd70 | -6.26252 | -55.43718 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b541040c-6457-366a-9928-17fc86453688 | -7.35008 | -55.22444 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 59e23a64-3ab7-3198-afd4-405cc1c5fd3a | -5.2108 | -56.09837 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 896c9fb1-1962-338e-b794-311df820b706 | -7.58355 | -57.70527 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3ea71713-5c7a-30bf-9c7c-b816b240bc88 | -6.13636 | -59.95361 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 9bb876db-97e1-3871-b66b-88db2445a86c | -6.76948 | -55.63334 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| fe07da5f-ddcd-3c93-a77c-77b757cef5f0 | -5.21728 | -56.07888 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2ec2e360-e6bd-3405-9b6b-8e0808276e71 | -6.64435 | -59.97281 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a0a74756-3a98-3191-abac-e1f680d26e4a | -4.09938 | -52.14713 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5350476e-2303-3cf0-aeb7-2ab12a958c16 | -2.79058 | -59.89105 | 2026-09-21 00:22:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| eaae476a-4003-36d0-acbd-864afe319b12 | -5.81391 | -53.51874 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 6e2ab23f-e694-34ba-bca9-347e3e915466 | -5.26154 | -55.92759 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6cc6d6af-2418-345c-b802-0b957179b54d | -7.57911 | -57.6705 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 7d945362-db02-305e-a4eb-0a710b48a50d | -6.2034 | -57.77803 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 9e823d34-8254-32c7-801d-988d377b99d1 | -6.03883 | -53.27933 | 2026-09-21 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 1016d8e7-5767-3f35-8a13-a73060a34b48 | -6.3573 | -57.77978 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| edc752c0-7bb0-33bb-ad83-167db69232bd | -4.34861 | -55.65948 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 6f7919ab-cdcb-366a-b4ef-b467cafd8b4e | -5.85345 | -53.53487 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f985607f-23a0-31b7-b7f4-6a6a9a8e88f3 | -6.92659 | -55.64234 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dd3608c5-2f6a-3edb-be98-ba7aa9006146 | -2.95143 | -51.04709 | 2026-09-21 00:22:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| c7f2c69b-f825-3e22-91e3-def83efacc46 | -4.56487 | -55.74698 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a987de44-efe6-329a-8906-4bc2ae30935b | -3.3922 | -59.58448 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 5186e722-5c24-3675-987c-cfecfa442349 | -6.72831 | -55.06366 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a6584734-cda3-3df1-83ae-37c7dfe577c3 | -6.09436 | -55.55502 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0e6dfde2-39c4-31ab-b0b7-ba33bfa9c659 | -6.31354 | -60.00082 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9ce2dbef-4d36-3dd3-a46b-f46f33377308 | -6.28028 | -56.03688 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 45d57e99-07a4-3a4c-a13e-8b5be435fb29 | -1.18574 | -49.13508 | 2026-09-21 00:22:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f80ca020-9364-3b83-b2a0-6989fea68314 | -7.24523 | -55.61089 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e270d6aa-dd69-3dbf-b586-a0ee896355a7 | -6.75497 | -59.0673 | 2026-09-21 00:22:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4e077508-e120-3bb9-904a-d941c58fcef1 | -5.20706 | -56.07088 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2e418d2f-1fb1-31cc-9234-60457b96969b | -5.89692 | -53.64986 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 1a56ba01-2519-34f8-8fb0-7f57789834ef | -3.68873 | -60.59532 | 2026-09-21 00:22:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 46f79f68-93c2-32a1-9648-9a8f351dce89 | -6.13679 | -57.72998 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1d9ab4a7-6969-31cc-b31d-2ab2a0f75368 | -7.25418 | -55.60968 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2b82d190-47f5-3ab4-811c-9e3fb18abb4c | -3.44429 | -58.23257 | 2026-09-21 00:22:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9c88ee04-1fe6-3595-89b8-c1df80bcd226 | -5.98026 | -57.78582 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bb362edf-f85a-3155-8064-8061595cfb69 | -6.13808 | -59.94349 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 896c8c4e-1a83-30a2-a63a-364e2348eb37 | -6.11762 | -57.74966 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| eab9b3b5-383e-3ddf-ba9a-833f44bc447e | -7.56962 | -57.67752 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a3ec8e45-df95-3836-892e-d40e60695530 | -6.09559 | -55.56401 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 41876df6-55ad-38f7-a84c-724a005434eb | -7.33017 | -55.22427 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 816fffc0-2228-32c7-8add-2e142d4ca626 | -7.33726 | -55.61082 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c497fa33-c1f8-38b9-b244-c6c6e59ddcf3 | -5.83094 | -52.07809 | 2026-09-21 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 34e42078-5b24-3deb-97a9-ba06a315ce44 | -5.37789 | -55.90543 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a3ce893e-bf5b-3e03-b92e-86299d1adfb8 | -3.90381 | -55.84249 | 2026-09-21 00:22:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 227775b0-b5d4-368f-9a0a-fe364e736ded | -5.87777 | -53.64327 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7d4635a5-a63c-37b0-a6e5-5127a7a76837 | -3.33096 | -59.81079 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e2845568-d8f1-3282-970e-18dfea2ce031 | -2.875 | -57.81648 | 2026-09-21 00:22:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f32adfac-ef43-3717-a9ea-7af30873ed50 | -6.20492 | -57.78929 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e770cb99-bc13-36f2-a0fa-c42b0d6a9f37 | -6.74498 | -59.42174 | 2026-09-21 00:22:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 0fa79d4c-b635-3b3d-b15f-76ae8a351a25 | -3.65976 | -54.26757 | 2026-09-21 00:22:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 581e7870-18fd-34a3-ae04-3251a32a8c42 | -4.34984 | -55.6684 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| a0a738ae-339a-3bb7-9daa-fa742d69ef7b | -3.81767 | -59.33323 | 2026-09-21 00:22:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0893c7a1-7c86-31f7-bdc1-87536783e0b4 | -6.30629 | -60.00816 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c8d6cba6-4b24-3ac3-b987-0542ae0ec41c | -3.50888 | -59.93499 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0891bf57-f39c-36be-ac4a-94186adc6b3f | -4.30193 | -56.25721 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f86c7dbe-63a9-3a47-947e-24a577eba9f2 | -5.20308 | -56.10882 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 3ec3a44c-5a4e-389f-a723-00822017d343 | -6.66101 | -50.88625 | 2026-09-21 00:22:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9195d8a2-936a-3a04-8ab0-c5042d1e4122 | -6.36383 | -58.28586 | 2026-09-21 00:22:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b62e6e2f-b8e6-3059-80db-199586bb3936 | -3.34969 | -59.86592 | 2026-09-21 00:22:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 50a9439c-7bf7-3536-bed3-259873ee1596 | -5.75941 | -57.58207 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8d54a10e-6676-3c3b-96ca-521b214aafc8 | -7.32952 | -55.62116 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f37dc4eb-a6cf-3d9d-831c-97725444aa31 | -3.53542 | -58.68453 | 2026-09-21 00:22:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7c94a6ef-611d-389c-ace2-96040fb06880 | -6.24629 | -53.31301 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5b579ff8-df07-3e68-83a7-f8fa9a1c1e35 | -6.20048 | -55.44585 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8c026c5a-c532-3bbb-8137-7c9596fb5970 | -7.32772 | -55.20637 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 39d1158d-5fea-36b5-983d-782378322e7a | -5.38682 | -55.90422 | 2026-09-21 00:22:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 545df3a7-f474-3111-a3f2-86e29e079e47 | -5.76509 | -56.51442 | 2026-09-21 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8971c542-b20f-3764-9405-a2397762bd5b | -5.87607 | -52.05014 | 2026-09-21 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 53fb6f48-bac5-3415-9ddf-c7d9ccd5439a | -7.32705 | -55.60275 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| eb0eb2e8-21f6-3e0d-a438-4910e7fc7bb0 | -2.99994 | -54.16309 | 2026-09-21 00:22:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fee7f5ff-f21c-3e3b-b7dc-c69605a76e60 | -6.74765 | -59.07614 | 2026-09-21 00:22:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7168499a-4f80-3f39-8a4e-c351b379e96b | -5.85309 | -49.79369 | 2026-09-21 00:22:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 50062cb4-e76f-373a-9179-39366e3a189d | -5.81519 | -53.52797 | 2026-09-21 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d39d24e8-695e-3127-ad86-069194f17e76 | -4.37409 | -55.02547 | 2026-09-21 00:22:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c16e1f44-ad3c-3b9c-9729-84a95a9c8aaf | -7.25049 | -55.58231 | 2026-09-21 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| dfd8355b-2b36-3a60-a091-0a922251b6f4 | -1.48309 | -49.011 | 2026-09-21 00:22:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 9d69a47f-197b-3986-b7d7-41b6ff3678e4 | -7.57807 | -57.66465 | 2026-09-21 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |


[Clique aqui para ver as próximas entradas](README8.md)
