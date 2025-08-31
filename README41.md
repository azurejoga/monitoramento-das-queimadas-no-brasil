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
| 53409e16-9361-38e9-9fce-a259ba86ddd1 | -12.09411 | -44.72408 | 2025-08-31 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| e5dbe601-c1b1-30a2-956c-4fc41aaabd16 | -13.02624 | -56.90614 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88c4a994-564b-3516-83d1-5fde68348658 | -11.0813 | -45.12496 | 2025-08-31 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 490c95e8-d3ed-3ce9-9704-753c3f07ce3f | -12.31794 | -45.72899 | 2025-08-31 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40b40ef8-ec3a-3069-8c53-9acaa2512928 | -13.35485 | -46.96929 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73f5a457-7cee-3e77-8bfd-d04e9b09f8a1 | -11.79821 | -46.45541 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c0b1361-fd20-31ad-9fe5-305843cbafbf | -13.9883 | -46.32012 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45be704e-b757-36c9-b235-e1df9c5471cb | -14.54181 | -51.97879 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1df2e495-5de6-349e-8447-4eb15db363c4 | -13.69266 | -46.91599 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6801c25f-b785-3cf1-9550-578cf628aa5a | -11.31573 | -43.68736 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ddd110e-d295-35c8-9189-c8cf968cac04 | -9.47556 | -47.6055 | 2025-08-31 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f11f0a7b-ce32-334a-beec-3bbcf2c19695 | -9.69098 | -47.03902 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d628d069-d546-314e-8e7a-1c0b7fc7e4a8 | -10.10044 | -49.28022 | 2025-08-31 04:29:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 826f6181-d24c-3355-8067-073bc6f571ad | -11.48732 | -48.29461 | 2025-08-31 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8800c5e7-4994-3ff2-8a57-621e9cecdcd6 | -11.82872 | -46.51503 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b019cd87-2095-3c8d-b2b6-5961c135dc67 | -13.47108 | -46.9727 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f5f28b15-02cd-3031-8583-0f9a657c9aaf | -13.5749 | -46.92278 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 443dbb6a-5fde-3a45-af24-57c1ac1ea4c7 | -13.02701 | -56.90922 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee805b59-ba0b-36dc-b5cc-81ea535b022a | -11.89729 | -46.38248 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3d8c32c9-a40a-3c78-b556-84707f1e412c | -15.07459 | -48.62719 | 2025-08-31 04:29:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 065ccdc7-2091-38f9-ab54-cbc1e43a25cb | -12.85482 | -48.08324 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 47f4fdba-9480-37dc-9740-907187efee91 | -11.88679 | -46.49481 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6a68fe3-d32f-38dc-9df5-a3f1c2543317 | -13.36134 | -54.38569 | 2025-08-31 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1eaaa3e-edfb-326d-9a7f-18e56f49972a | -12.63219 | -48.22211 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ab5cb85-8fa1-35e4-baaa-7268db728fef | -12.97775 | -54.75776 | 2025-08-31 04:29:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6a1521f-03d0-3f78-8181-255c78c7ee77 | -11.8639 | -46.50954 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4bb14e0-e240-3b57-be2d-674ede9fa476 | -13.30628 | -46.88407 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1817e263-a139-3a11-8c06-99b5f6874e85 | -9.70373 | -47.04466 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f79d7325-dce8-3749-a83f-1be382bcb97e | -11.3028 | -43.67191 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd18ce05-ec9f-3707-95f0-c5e21c6159eb | -13.69989 | -46.91364 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8522fd12-f1fc-386e-bf0d-8b59923e8812 | -11.01034 | -46.95147 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a9dee02-0af4-3c9b-bd95-86afb318b6a8 | -11.81574 | -46.44316 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fd160df4-e52c-3aca-80d8-fbf8bdc6d40e | -12.16435 | -47.18399 | 2025-08-31 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a93c5e4-6a25-33fb-b54d-5eedc13fb037 | -14.83737 | -46.74355 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca08d9b2-0822-3639-ac19-ba39f5e9bfd7 | -9.53654 | -45.84178 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77d84f16-198a-3d2d-aecc-470f8941bd43 | -11.90543 | -46.69513 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db9f26ec-d921-3eae-b78c-ccdfd8be4cac | -12.98888 | -44.85425 | 2025-08-31 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0b3cdb2-0891-39ca-a6cc-f5ea65b340e2 | -13.46878 | -46.9432 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c520b85e-af42-3206-b701-6ff410079e40 | -11.91412 | -46.40714 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1244218-a8cf-3d67-8bd4-ee06f933e91e | -13.57546 | -46.91918 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61c804ef-97da-31ea-9405-2c041893a37c | -10.75689 | -46.36504 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b3c7040-4451-3c08-83eb-d3648612a825 | -11.85997 | -46.49056 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57380795-3677-3cbe-ad8b-d378a7f1e0e8 | -12.61173 | -57.01482 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b74b60ed-fefd-3caa-8f5b-20d25e4a1bfe | -10.0302 | -48.10023 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dbbc6c2e-b649-3517-b713-a39a5be3eb14 | -10.5203 | -51.93662 | 2025-08-31 04:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fe468bf-875c-34a0-8c5f-b51f1f00c9c3 | -12.80481 | -48.09682 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf900dc4-56e2-33c3-9bbb-b31fa9215e80 | -11.07093 | -44.73812 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c690359-f69d-3b59-8a7a-ccef1f7f3657 | -12.64468 | -48.16565 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c33405a7-5b61-31cf-8d0f-3608aec08274 | -15.94691 | -41.40163 | 2025-08-31 04:29:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ecc5627b-7575-3faa-b2ac-83e63885fc68 | -11.06055 | -44.63893 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63857023-7db3-338d-b588-1ec231b63a95 | -13.35096 | -46.95021 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5fcccb66-131b-3f57-8bc1-0809b626f90d | -13.30908 | -46.8882 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7acc8830-471c-3e36-9620-217cac8803f3 | -13.34873 | -46.98665 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42184c17-13cb-3d98-bc96-cfbe85acf65c | -11.06741 | -44.73758 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be475c9a-5e64-36a1-9d5d-680b25921c98 | -10.95136 | -50.84672 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 354420d0-48b6-3637-8676-e8c0480c8beb | -11.06156 | -52.05345 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b5b008d-61f4-3f88-a855-aaab34c3b819 | -11.35151 | -43.62456 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 25b428ee-5c3b-3ff4-bd2a-ca56ed1ccd45 | -11.41397 | -44.68068 | 2025-08-31 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 809a3401-eb0f-3c34-8449-10220c59e42d | -13.02882 | -56.89314 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4b1e31e-c8cf-3179-8806-b3ea5fb917b9 | -13.46934 | -46.93953 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eca68398-5dd8-3670-887d-96a42cc09ddb | -9.58659 | -46.00668 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f02f2911-d1ed-3590-8702-249f8a65ebb7 | -12.93503 | -56.98697 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c8dbbae-35a8-34bc-b355-6399fe8e378b | -11.56235 | -47.6111 | 2025-08-31 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41217592-20a8-3b5c-9918-b3c06841764f | -14.81249 | -46.74768 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3318a6f2-2957-36df-8491-6cfca270ce2d | -13.48875 | -46.83517 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85f10ef0-efdb-3901-b5b8-8483ed9da4ad | -14.34584 | -51.88088 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 989c6cf6-0b52-3d82-9267-41cf101202bf | -9.66277 | -48.34529 | 2025-08-31 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69ac5e4f-ca56-3079-842f-f4ed3848d846 | -14.33543 | -51.87417 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3096e50f-7d8d-35de-ada4-1e61ce8eb8d1 | -11.06 | -44.61834 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 950aa9c8-49f3-3553-a7a8-efac75bce67c | -9.49075 | -46.70569 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 111c38ad-185d-3290-8c49-8e528320c1ab | -13.01063 | -56.909 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96a796a3-c70a-38e0-8dfb-0785aae2c44e | -13.32744 | -46.85821 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b9a2125-e858-3a2a-9b3b-f9ab3b8e3fa0 | -11.34952 | -43.63807 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8ee980ef-c888-3af3-a4ef-06ebb37bb22a | -11.9029 | -46.39073 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dad3a797-2da5-3961-a709-4220c9fa945b | -11.82817 | -46.5186 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0aa6670a-0cf0-3d49-806d-c8cecd098e58 | -15.67304 | -43.22993 | 2025-08-31 04:29:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d3205207-abb0-3286-af16-80bb64762155 | -13.31414 | -46.94427 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93564d65-ffee-36c4-9c2c-7c345ef0cee4 | -11.85999 | -46.5126 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d3de79b-0d2b-36f7-9797-1a3637e0b7e1 | -11.90407 | -46.42761 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| edadfdec-cd5a-379b-9f3b-02ac2870a3a2 | -13.36145 | -46.95894 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fecd697-0da8-3f54-be0b-36c6dd2d3ea0 | -11.91881 | -46.69723 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d0c223f-4b40-33ef-9339-9908a58ef77a | -11.05933 | -52.04275 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05154d4f-157e-332e-a856-db717b855557 | -11.36425 | -43.58971 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df925540-4fa0-342c-a39f-d9cf507c98d2 | -13.58636 | -46.90238 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 785bbf00-aeb2-3a27-ad70-490cfc492a96 | -14.27603 | -51.88233 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7556dac-79ca-3c77-bbf3-a7a00c83360c | -13.39388 | -47.03759 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2088e59-8424-3a3b-a3bf-20939dd8d968 | -12.9244 | -56.98495 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52aca95a-6e3f-3168-b3ef-3198ef9b893d | -11.29489 | -43.64783 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 164a5d8e-b476-30cd-afc0-17a87dd308ba | -15.67709 | -43.23043 | 2025-08-31 04:29:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c2403a13-667d-3634-978c-e9f2cc54deeb | -13.35206 | -46.96516 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e163eba8-9e6b-3e72-978f-5a5e8421ef2f | -11.36453 | -43.5619 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab5cc305-2031-3324-b6f6-bf54145f2ca7 | -14.03997 | -44.55457 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a242420-67df-316d-8f2f-6d246ff9dcf3 | -12.86269 | -48.09232 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ea0a72c-b17f-312b-9eee-3fddf1aff3cf | -13.35095 | -46.97233 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f93d7ba-800f-388a-852a-5e156b7a0384 | -13.48331 | -46.96021 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04b80869-27d3-34f6-a4d7-739461190538 | -14.03188 | -44.48167 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4a04231-2d65-34f4-b1ea-8dccbf0a3eed | -12.93635 | -56.98028 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d87ba3b-ce6d-3b1a-a7a8-c8ec002eac0d | -12.09707 | -44.72871 | 2025-08-31 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 908ea186-3692-3e7a-8725-e4a10422fac4 | -13.35977 | -46.94753 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 51f561ab-f643-3d1f-8ffd-adfdf1467718 | -11.89658 | -46.73017 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README42.md)
