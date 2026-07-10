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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ed98e8e-9f6a-3768-8379-4b380106dcd9 | -5.47253 | -45.42783 | 2026-07-10 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb9dda2c-82e7-389e-af28-d5ea76bbadc5 | -5.69773 | -46.54701 | 2026-07-10 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9079273-999e-3a5d-b82f-9336dd7d65f9 | -4.15648 | -54.98327 | 2026-07-10 04:32:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6789cbda-48f0-371e-b61e-46a6d8ceddca | -4.77424 | -41.79308 | 2026-07-10 04:32:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cf9c1f59-a67d-35e0-97f3-874672638296 | -6.50332 | -42.21276 | 2026-07-10 04:32:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 347a1d7e-1fc8-31c1-8c9e-9cc0aed45f05 | -7.01564 | -45.41722 | 2026-07-10 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9d2b6ab-ab02-3b26-b709-a2c7a6b324d5 | -5.6253 | -47.10365 | 2026-07-10 04:32:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c4e7e28-2ccf-3954-abeb-2d1c31d8dc0f | -4.34478 | -47.7654 | 2026-07-10 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58555148-213c-3f54-9aff-dca9897c8b2a | -3.32174 | -40.0042 | 2026-07-10 04:32:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 878df889-613f-338d-b34b-37d5a9806f46 | -3.21124 | -49.05997 | 2026-07-10 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3e3d196-e22f-310e-aec3-8d94a6be4c42 | -3.49558 | -43.3122 | 2026-07-10 04:32:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d69d8be-e7d1-360f-9c8d-f450c81bf720 | -4.94655 | -48.24685 | 2026-07-10 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e81e1a15-5be0-3968-af4b-ca27de1e02ba | -2.80644 | -48.59317 | 2026-07-10 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f7c5471-eda6-3946-804d-af44e024f2f0 | -6.7372 | -47.12766 | 2026-07-10 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ecb7476-3a2a-31c4-8381-978e7e4e3ac7 | -6.66923 | -47.52195 | 2026-07-10 04:32:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8393d057-d110-3db1-a00e-f9423b8b6032 | -4.15672 | -43.09304 | 2026-07-10 04:32:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1a8f190-4448-3565-89fc-aebbddfc0e5d | -2.48668 | -47.08971 | 2026-07-10 04:32:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e066154c-1949-3975-a4ac-0bace63888ba | -5.97716 | -43.61356 | 2026-07-10 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 291b6d56-2df5-3658-ac5e-97463a0f9fa0 | -5.46565 | -45.42675 | 2026-07-10 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19dabc4f-cbcd-30fa-beb1-4126bd90b7eb | -3.20781 | -49.05945 | 2026-07-10 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a85d1ed-0529-3003-b0cb-f3fb3535fc9e | -2.76761 | -48.57608 | 2026-07-10 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92d7477c-b452-36c7-b1fb-0194fba6d467 | -5.34385 | -45.35126 | 2026-07-10 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b0caf73-060f-3d29-aa8f-4b55d99375b1 | -4.64037 | -43.12714 | 2026-07-10 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57694703-d377-3a0d-a3a4-401c4769f0c1 | -3.95541 | -41.53406 | 2026-07-10 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af0e61bb-6e33-38c2-b281-4bfbdb890957 | -4.34755 | -47.76935 | 2026-07-10 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51c90fa4-3fc5-3526-94d3-3c34726455a3 | -4.98211 | -37.47742 | 2026-07-10 04:32:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b933c9b8-e5bf-321e-87bd-028b1fcb9769 | -2.90281 | -40.39592 | 2026-07-10 04:32:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3a8142c-6f7a-37ea-abec-6e916b7cedd9 | -6.94189 | -43.71095 | 2026-07-10 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9056e7be-6c4e-3262-9118-e9f35d41467e | -7.01394 | -45.41817 | 2026-07-10 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fed06da2-a2fa-3163-9987-e02a61885810 | -6.42244 | -43.71916 | 2026-07-10 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6982ff61-b07f-32a8-a47d-94cb316f89c8 | -4.16054 | -43.09361 | 2026-07-10 04:32:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eca8616c-18bf-32a7-acd1-75988df5c43f | -5.97673 | -43.61643 | 2026-07-10 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3e659be-ee90-3626-aa3b-5e8b79501ffe | -3.32103 | -40.00905 | 2026-07-10 04:32:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2b6ec9be-ec80-3569-aa96-dfa1a384c97d | -5.02347 | -47.51668 | 2026-07-10 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02f40e86-7999-3a86-a7c4-4cf9078ef6f2 | -10.12823 | -50.18751 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a55cf49a-d112-37e6-8248-c148be0fd906 | -10.40332 | -49.44651 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daa26507-b000-314f-a3fc-410605439e6c | -11.87759 | -47.68086 | 2026-07-10 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 963caf20-5bcb-386a-ba68-5ea0bbf26166 | -12.84861 | -44.35613 | 2026-07-10 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecd0af51-5e4a-364c-b577-ab7978dc0dc0 | -6.42761 | -55.79913 | 2026-07-10 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d167f7be-6fec-3360-b10e-d359291e5343 | -13.36236 | -54.37471 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a21c3d9-4f09-3bff-9635-48d50747d9de | -6.56061 | -55.15197 | 2026-07-10 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f445f35-dd60-36b1-a8c2-957a0cafa1dd | -13.76771 | -46.30684 | 2026-07-10 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f1cef83-699e-330a-911f-e2acf41af5f5 | -7.8956 | -48.25737 | 2026-07-10 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea640a38-3516-335e-acb2-50a4c4843e5a | -10.83255 | -49.37896 | 2026-07-10 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f149c70-98f5-3f55-aaab-74c766c49078 | -10.85183 | -45.03788 | 2026-07-10 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| badec94d-2ba1-3eb4-8135-cf98f7c1a87c | -8.00511 | -46.62233 | 2026-07-10 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50d57efc-c727-33d3-8570-5693ec79b609 | -8.22548 | -47.35617 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d22b34e5-15f5-314d-83b4-47c82f2d1dc5 | -8.00174 | -46.62181 | 2026-07-10 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd14b06e-ad65-3046-bcc3-27c9e828b6b3 | -7.90548 | -55.42939 | 2026-07-10 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0edd8bdd-17c4-3a93-830f-3c181b0ae840 | -10.13278 | -50.18077 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f86a7d9-41d0-3e6b-9083-ddf32af0bd48 | -10.40719 | -49.44352 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8f83e0d-7e1c-3d5a-a0c5-3a61dad63afa | -13.30841 | -54.34167 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0821a37-5659-3483-9ca5-b4a225a8e436 | -8.12143 | -47.59063 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae313b3f-59d3-3d81-9e0b-bb2113bf9b07 | -7.90304 | -48.05312 | 2026-07-10 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 245cc213-302c-386c-8e68-f7dddb78dd3a | -8.13184 | -47.87329 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73fe7e94-0434-3417-8362-d407d7d54008 | -12.4541 | -49.58228 | 2026-07-10 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85c18517-0f0b-3570-a48b-ed1afc89195d | -11.32914 | -54.47218 | 2026-07-10 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bd75cac-6e98-34e7-aa7e-f8fc768b5e31 | -10.85913 | -44.4429 | 2026-07-10 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6b91fe7a-2cee-3fb5-988d-3e048a2471a7 | -10.15624 | -50.20705 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9e3f8bfb-06b7-3941-95e6-3abc0b877454 | -11.85249 | -48.24552 | 2026-07-10 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb6c9a2b-996a-3e6d-bae0-112a8287dac2 | -11.4882 | -52.92041 | 2026-07-10 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 650983fb-685a-3b14-8413-3882222bba05 | -8.72319 | -47.83451 | 2026-07-10 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe2be1f5-d30e-38f1-8172-6c7698fd9cae | -8.50338 | -48.06678 | 2026-07-10 04:34:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10c7156a-4952-368d-99da-7625b6ef4f8a | -13.3133 | -54.35102 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a4f4409-f7af-36c2-80c8-a2a1a94c8e46 | -13.3131 | -43.71774 | 2026-07-10 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65c103f5-436c-3a40-8328-bfe6a774f985 | -13.75806 | -46.27122 | 2026-07-10 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dbc274b-cf5c-3e0e-86de-178157c92449 | -10.605 | -46.56572 | 2026-07-10 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92135839-ea34-30a2-ac0e-bfd5f0823d9f | -13.37552 | -54.36979 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b0858d1-cf93-37a6-a101-6bcb7f2c980d | -10.15521 | -50.19191 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5156a911-6610-37c2-b010-7ebbe3c11000 | -13.26978 | -45.14116 | 2026-07-10 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfd86ea7-1b81-3882-9520-15c0ab48b47e | -11.41952 | -41.42117 | 2026-07-10 04:34:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e3ecf8db-e84a-3ebe-93fb-a4d1d3946578 | -8.03735 | -47.43041 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf20dbf9-3533-32da-9513-b3fd82eec020 | -13.36361 | -54.36762 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29bf85d1-218f-3095-9928-c344d1daabe2 | -13.26913 | -45.1459 | 2026-07-10 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a75c7a26-d50f-3d61-ad47-c23605f2282b | -12.3756 | -47.89104 | 2026-07-10 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22879131-741a-3e44-b64c-a9cae7358088 | -13.2965 | -54.33956 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c69006ec-5f37-3de5-9f53-6e91f0d042e6 | -6.55975 | -55.15693 | 2026-07-10 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfd1ee06-0793-3aa0-9ae2-5d6703ecff52 | -11.47245 | -52.92239 | 2026-07-10 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adcd8580-efd1-3d6d-a264-9c143577d30a | -13.27542 | -45.15667 | 2026-07-10 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6953584-8e40-3918-9f20-b07edbc2e757 | -13.30781 | -54.34514 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10a3eb18-050d-3e5e-8a71-e4582f748fc7 | -11.83643 | -48.23933 | 2026-07-10 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 98e97003-f2bb-313c-8744-1d039a3ecce4 | -13.31393 | -54.34752 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe50e6ac-300f-3fb8-b62d-45cabab86506 | -12.50038 | -43.768 | 2026-07-10 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f182220-e94b-39d0-9253-6430ffe6eaa4 | -7.28994 | -49.27236 | 2026-07-10 04:34:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e48cb891-5239-37a7-a1f3-08e4ecf1dfed | -10.8598 | -44.43801 | 2026-07-10 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 88523fec-2d4f-38bb-8a08-f179ac289c72 | -11.43717 | -41.43377 | 2026-07-10 04:34:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 64368b95-dd95-3dae-832f-359e318837b8 | -11.27787 | -55.79127 | 2026-07-10 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfbc7613-8cc8-3dbf-8204-0fd193ade862 | -10.26224 | -46.39412 | 2026-07-10 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 820c757f-3e4b-3620-b2e2-69583830b18e | -13.37093 | -54.37259 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2317ffcd-289c-3f31-b266-4922eaaeea43 | -11.51522 | -56.1274 | 2026-07-10 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6895780-6590-3f98-b05f-55578aef6663 | -10.15683 | -50.2034 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e24127f0-8074-339c-b381-0020af1d2b81 | -12.45135 | -49.57822 | 2026-07-10 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8565bb16-36fb-3e4c-8258-5a014de17ebe | -8.72703 | -47.83154 | 2026-07-10 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5c402b9-ab12-3a72-98d3-1279e7c9e81c | -12.37225 | -47.89051 | 2026-07-10 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8400350b-39de-3367-a5bd-ff542664705d | -10.12486 | -50.18696 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b773335-4810-3497-a3c6-457eed993ce9 | -7.7285 | -44.55748 | 2026-07-10 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca57be68-8954-3384-9588-f281b6324ce2 | -8.50391 | -48.06331 | 2026-07-10 04:34:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10221bff-045c-33f6-8433-63ce139c6629 | -13.26848 | -45.15067 | 2026-07-10 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35911e1a-3158-3b0a-8279-f98ff4be0db1 | -6.55418 | -55.16118 | 2026-07-10 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f09809be-61ca-31ce-9d4f-15a2f41d2734 | -11.49195 | -52.92105 | 2026-07-10 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
