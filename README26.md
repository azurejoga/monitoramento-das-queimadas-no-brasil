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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ddd1156-1319-37ff-a9ff-e7a824640016 | -12.27339 | -50.71888 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a927976d-f46b-3b34-99d5-48dc88dfdaf3 | -9.54054 | -56.15606 | 2026-09-26 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38101418-c923-3ca5-acf3-63571d5934e1 | -8.19234 | -54.82761 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba2a37f9-bfc3-3c78-8078-f8ee8c689c02 | -12.16457 | -50.31836 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e3282adf-30b1-3220-a843-1b5a59a2572a | -11.93142 | -50.59375 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a8bebce5-7ff5-3dfa-8998-0c659133fc2f | -12.76458 | -52.82006 | 2026-09-26 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c4c87b9-4bff-35b2-9dad-a57af916b0b6 | -11.93067 | -50.5995 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1096301c-7ae2-3627-bc80-cc95d5ba3d49 | -12.14218 | -50.30334 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d7ed44cb-978d-318c-80ce-8364ac848493 | -8.23245 | -54.66431 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea1b741e-7c6e-3f20-8c4f-732a91e3e448 | -12.13671 | -50.30568 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 342da850-68b0-30fd-8302-17aac22c583a | -12.7597 | -52.82365 | 2026-09-26 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7be0749e-878b-3466-a04c-cc7f36e1daab | -12.26243 | -50.32243 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 617cd90b-0cd9-342f-8fdb-0664e93b3bb1 | -12.25889 | -50.30956 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bfb0dc5-c2ab-3b11-8fdb-97da6e7bb1bd | -11.0432 | -54.03777 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02650e56-6051-33a0-a4d2-2f921f00fdb6 | -12.26605 | -50.36283 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 64664464-dbe3-3d97-bc30-30ac01d3d813 | -12.1653 | -50.32501 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1364bc4f-d23e-3786-be8a-0618dd946e28 | -11.85615 | -50.54813 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bb53bc1-076b-3380-961d-40df0b1d9178 | -12.25224 | -50.32107 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83167fc1-7c15-3a9d-afa1-683df53240d7 | -12.16138 | -50.31521 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3468a43-ff28-3d52-9392-3e86373f20b5 | -12.60652 | -51.95212 | 2026-09-26 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 21d2e53c-c744-3a9f-b5b8-15471492d5f7 | -12.24831 | -50.31123 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67f3692a-4c21-35bd-9918-9a62e0f95847 | -12.29105 | -50.73877 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dbdbaba8-d184-3603-aeb6-04f592f28d71 | -12.9513 | -51.05884 | 2026-09-26 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7245f25c-3dfc-39aa-bcf8-70be2fdf2028 | -12.16893 | -50.32514 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 203ecb0b-f450-3143-97cb-178dda23c4ce | -11.90817 | -50.58455 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd2bedbf-6c38-3f2a-b718-31333ac009db | -12.16569 | -50.32198 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3d3d7b3-8292-3945-ae8b-4b24c7b5e8c2 | -9.50865 | -54.65658 | 2026-09-26 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcf7a6c0-0e72-3291-bedd-215714963c84 | -11.95781 | -50.67324 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a16ff27-227c-344f-90ff-e13f32d1b2f9 | -11.28224 | -54.43664 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1dcf9d57-67cb-38cf-a5fb-51cd344086b2 | -11.17436 | -50.05052 | 2026-09-26 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7508ef42-309b-3572-9bb7-4ae0323549fe | -12.17078 | -50.32267 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| de335931-cedc-3792-94ad-0721c976349f | -12.17039 | -50.3257 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 06c18507-8783-300f-804e-99944fcb5503 | -12.26861 | -50.34156 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48294913-7aef-30c9-ad67-a14900ffde64 | -9.93772 | -57.51273 | 2026-09-26 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc6ebf53-c71e-3fea-be11-c05ea899095e | -12.26641 | -50.3598 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8855886-0ad9-3a94-8a33-d93246e42fc0 | -12.1418 | -50.30637 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f0e87145-731c-3d01-900a-3ccb287b295c | -10.33027 | -55.35744 | 2026-09-26 05:12:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6574e4a-4e2c-30f6-b470-73479b01a8b3 | -12.16608 | -50.31894 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a85813be-44e3-3d8f-b9cc-db5eb70b7484 | -11.9217 | -50.59816 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82880360-cd07-382b-8d6f-48c459fed343 | -15.42022 | -47.89473 | 2026-09-26 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f006c877-3bea-39a6-b4ee-cd63b1047a72 | -17.04173 | -56.58213 | 2026-09-26 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 96fe68aa-0036-307a-9dad-2bbe698fe865 | -13.0421 | -56.59578 | 2026-09-26 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20e9bcb7-bd81-3810-b8c6-d30bea3eeefe | -15.16106 | -48.81668 | 2026-09-26 05:14:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f0aa06e-19ae-3c59-81f9-89023088dd16 | -12.67102 | -54.64801 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca763d4e-ac49-3a8a-9fcd-71bb5a099bc6 | -17.04111 | -56.58655 | 2026-09-26 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| abce1d68-1e27-3566-b8e8-fd35df5a513d | -15.16195 | -48.80842 | 2026-09-26 05:14:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8e84d2f-e432-3067-a578-5f6145e95b25 | -13.71045 | -48.80851 | 2026-09-26 05:14:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e49ce01-ccc4-3860-a436-82182bfbcf18 | -11.87161 | -65.03298 | 2026-09-26 05:14:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3fd6279-3791-3664-897e-b18b44c5110d | -13.699 | -48.80687 | 2026-09-26 05:14:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb0456d7-3d32-3c55-86b2-9b065c48dcec | -17.55027 | -46.33712 | 2026-09-26 05:14:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 139fc25f-f470-32cf-8627-9b1ad216fbed | -17.55782 | -46.3401 | 2026-09-26 05:14:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb8da672-8a08-3d92-8069-418d9e09228d | -13.45801 | -61.32145 | 2026-09-26 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a801f802-9582-3ef0-8bf5-fcc09d7bc0f2 | -19.90939 | -48.25331 | 2026-09-26 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f07fd20-e69c-3427-abbb-82fb69257574 | -14.87109 | -48.20914 | 2026-09-26 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d6e3434-cd70-3226-9fb6-de35d2036994 | -12.66719 | -54.64743 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d9d4436-e83a-33c7-95bf-42abee5d5574 | -15.16149 | -48.81269 | 2026-09-26 05:14:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 614f4552-a6e0-3e20-9784-e2b523676904 | -14.86929 | -48.21086 | 2026-09-26 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c97ac8be-ddd2-3501-85c4-0ab0990870e3 | -15.17367 | -48.80958 | 2026-09-26 05:14:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 464d9550-d526-39a9-8316-5e2f3e53dbe6 | -12.67171 | -54.64321 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22b78d52-0a54-3155-9647-41ad8afaffb2 | -16.02296 | -59.78359 | 2026-09-26 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b98c9b28-5812-37f6-bc54-84a07a07555b | -16.76371 | -47.25798 | 2026-09-26 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6052a39-2786-3483-be2d-dbcc5a8fbdff | -14.86986 | -48.20572 | 2026-09-26 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2d96b19c-a0cd-3740-a450-3cff74a00e43 | -15.20393 | -49.29268 | 2026-09-26 05:14:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1753a8c-236a-317a-91f1-17ff78f47a25 | -12.67239 | -54.6384 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f1cdaa5-e176-36db-8c23-3d717eac81f3 | -15.73309 | -50.79979 | 2026-09-26 05:14:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bc94036-efaf-3b00-8ce3-39c7cb20d198 | -14.47234 | -53.66351 | 2026-09-26 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9bd43ec-237a-3e5c-9ebf-3cab4cbd1ad0 | -19.90895 | -48.25881 | 2026-09-26 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2a98a59-e6e0-3069-bf02-f26d1c29a35f | -14.33233 | -52.72454 | 2026-09-26 05:14:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b392c95-e579-3a7c-a235-a22ffbe7efd0 | -14.33404 | -52.72175 | 2026-09-26 05:14:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8f7f11c-0502-36b5-ae19-3b054d3478df | -12.66855 | -54.63782 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ca3a81e-7a09-3c5c-bbd3-a470848d7ea4 | -15.16736 | -48.81317 | 2026-09-26 05:14:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9ad1293-ba24-3715-a078-acf24b3db9d5 | -17.55723 | -46.33791 | 2026-09-26 05:14:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3af983f3-4df7-3bd1-9d2c-0dbcbfa84598 | -12.90022 | -52.06657 | 2026-09-26 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 923b0407-e982-3ebc-aedb-7c9cd0afc6e3 | -12.67068 | -54.63966 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91e9122a-3fca-370d-a7c4-a5172f523a1f | -12.66787 | -54.64262 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4617305b-ee04-3738-931e-0bc6a1629617 | -12.67002 | -54.64446 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc0d21ba-5916-3d08-a473-250d995f37fc | -12.66684 | -54.63906 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6280daf3-4024-35e3-a6cf-e8fbde1ca465 | -17.54972 | -46.3439 | 2026-09-26 05:14:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 5dfb9a56-d4c6-38f3-bf02-7fb75e3a9f95 | -19.91324 | -48.25952 | 2026-09-26 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ca980d2-0257-35da-a482-a0727552736a | -12.90055 | -52.06824 | 2026-09-26 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33ed52ca-bd29-3b58-990c-9509d1c6959b | -14.87163 | -48.20395 | 2026-09-26 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2644c36a-1c5b-375e-929e-6a9b0350503c | -12.90136 | -61.72397 | 2026-09-26 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fca451ae-8144-3ee6-8cee-ad558263db5d | -13.69332 | -48.80561 | 2026-09-26 05:14:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e105c45-4018-3e30-a93f-1f03d38ca065 | -14.47649 | -53.63165 | 2026-09-26 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9b318e46-b37f-3519-b8b1-ce72fbaf80e7 | -14.476 | -53.66812 | 2026-09-26 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19bbce23-a648-309a-b62b-ee8e9d602794 | -11.87235 | -65.02874 | 2026-09-26 05:14:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc7ea2ad-2881-3202-ad88-26f5f3572d0b | -12.66403 | -54.64204 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d85eb74-aa7a-3941-8494-8509a9080c29 | -17.55027 | -46.3461 | 2026-09-26 05:14:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 358183c0-7eae-3c70-a5b5-d643fa490741 | -12.67386 | -54.64504 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9441d804-d6f5-35d3-95fd-5222e4991cd1 | -13.69858 | -48.81044 | 2026-09-26 05:14:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fae9757-f31e-30b6-9be6-f6128d2418b5 | -16.57303 | -53.06771 | 2026-09-26 05:14:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f92ac54-7670-3caf-9869-6ad1d6449045 | -14.33345 | -52.72623 | 2026-09-26 05:14:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cbfd4f2-b09b-3427-b5ff-548fd11a4ab5 | -11.87085 | -65.03727 | 2026-09-26 05:14:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 915c681f-d04f-31bc-ad10-e835d91eccb9 | -14.47542 | -53.6398 | 2026-09-26 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 295b3808-d26f-33f1-ba63-ce74df4e2961 | -17.54391 | -46.33857 | 2026-09-26 05:14:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| dd7b6260-0464-387a-992c-58004e54a33a | -17.55147 | -46.33257 | 2026-09-26 05:14:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ce21755b-7e1d-306f-8739-cdf3025f831e | -14.86541 | -48.20491 | 2026-09-26 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce3da567-e736-38d4-a041-25b1ddb83cbe | -12.66618 | -54.64387 | 2026-09-26 05:14:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ece1cc3d-fdd9-35b5-99a8-2f03bdfa8ee4 | -19.91373 | -48.254 | 2026-09-26 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db4b6ddb-4587-3983-ae6e-134901793cfa | -17.55087 | -46.33934 | 2026-09-26 05:14:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |


[Clique aqui para ver as próximas entradas](README27.md)
