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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7e53e03-321a-36bd-a963-ccbd0de99912 | -13.82395 | -55.22528 | 2026-08-26 05:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1278cd9a-5bac-3251-9474-694f9a09f7d0 | -9.67874 | -55.09019 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05ac7244-5ab8-3aa0-b834-54b8667000b0 | -14.36559 | -51.75012 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9782160-f36a-33c9-ba93-f77771a0b973 | -10.75459 | -54.0239 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 51574b11-7e8d-3747-bda7-ef7303f94528 | -12.01995 | -46.02596 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7b550c80-92d1-3f1c-961e-7e53c19dab37 | -9.09328 | -59.41461 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2cb5db4-b9e6-3ff7-8c4d-c88ff128a978 | -12.95502 | -56.61357 | 2026-08-26 05:29:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dd3b340-e4d2-3031-baad-36766229395c | -9.13302 | -57.55841 | 2026-08-26 05:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4e7d147-ddc1-399d-b7bd-268a7be3398d | -13.28571 | -51.4558 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4903e4b-0220-3518-bbd3-0268b07e7c1f | -8.81666 | -62.33601 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0636c364-c9c0-38d8-97bd-e9f9b153e3fb | -13.23391 | -51.39044 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8935aed-40d0-3c2d-b69d-b73b84ecf3a9 | -9.47428 | -56.90545 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5b00252-1028-3d8c-8c28-f987fe8c7ffb | -13.20021 | -51.33472 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 6d7fec48-b86b-3321-a96b-af68048fc3f9 | -9.47213 | -56.90774 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfc9be7f-c421-3736-a026-1fd10aad4e91 | -13.23553 | -51.37678 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc0a73e5-13d4-3819-ae28-0301b0d6166b | -14.39521 | -51.76234 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb78bcb1-ecbe-312e-9d18-c93b28a1cf04 | -12.66906 | -48.41505 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e539736-9229-30b9-ac69-30f7fb09dfcb | -12.66969 | -48.40945 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d565b47-00fa-38c5-9437-70e9b8cf723e | -12.64824 | -48.42643 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2418cc37-16c1-3bf9-ad37-1a013d3c6458 | -13.65154 | -51.84962 | 2026-08-26 05:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0f965bd6-ce63-38c3-a6ea-2619d5767e52 | -11.19773 | -55.08248 | 2026-08-26 05:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad4c5865-4bd2-3da7-b7ac-a482f591dc1e | -13.34604 | -48.23129 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d5e29e1-3691-3617-9548-340a9a0df21b | -9.27718 | -60.92049 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46ce1c26-8020-33f4-bc5f-c2b17935fc3c | -13.42292 | -57.07241 | 2026-08-26 05:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88734499-3e61-3d6c-8eb4-e551902666b1 | -11.16943 | -54.00054 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 752fdb3c-1131-31d1-8af1-0f28e46278b1 | -13.85878 | -54.05545 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 425b2243-8b54-3c56-ad8c-ae2cb3a2d36a | -14.1322 | -52.35352 | 2026-08-26 05:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5efde23b-f4d2-3183-8c04-c1ae22d2a3fb | -13.2693 | -51.45714 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6433d86-6f78-371b-8442-500b347d52c4 | -11.76414 | -54.52942 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00f8ea55-d6da-338b-b713-54af8babade5 | -9.69758 | -55.1554 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7be61f44-e6f6-3c88-9848-237d4e6a341b | -9.14476 | -59.39058 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe62d3f4-fd20-3933-8a0b-4056c540a82a | -9.15583 | -59.38518 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68a57e64-1c98-3db3-bc63-f1d521ee5af5 | -14.79217 | -48.80109 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50d32295-cc97-3922-9a4e-4d3469087bde | -9.99388 | -53.96261 | 2026-08-26 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2343a4d0-da60-30ff-b8ac-eaec71916d34 | -13.22985 | -51.35942 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 0317d6a3-f9f8-3cb5-93ff-0f7d0bd9abc2 | -10.74831 | -54.0061 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64f5d2a9-1cce-37bc-84a4-b505808f3a3c | -13.33356 | -48.22411 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90cb8700-5b22-369f-b405-6e60435c0888 | -13.2853 | -51.45918 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 689bba90-6834-390b-9c33-09dafaa9666d | -14.79906 | -48.79764 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| df11b2cc-3273-3352-a2b4-768bccd8762a | -13.25491 | -51.39664 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1389ab90-5d86-30fe-af21-7b3479934506 | -10.42822 | -61.22197 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15ecafc6-d956-3544-a52c-ab54f9eaebf6 | -9.48939 | -56.9144 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10f99139-c568-3a58-a459-f39cd4410bf3 | -7.80953 | -63.26275 | 2026-08-26 05:29:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| abd5a72e-6704-306b-aaa3-acc0485b95ba | -9.72021 | -49.34434 | 2026-08-26 05:29:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdb6a239-8656-3eac-ac0e-968c18e3914b | -13.26603 | -51.39463 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d646ffdb-f0f3-3671-ba69-a558add323d1 | -13.86635 | -54.03331 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfdad958-dab6-366c-9f3b-3d33cb005148 | -14.29075 | -51.13413 | 2026-08-26 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d14d024-fbcb-3588-b04a-5ed7a0770f43 | -13.17707 | -51.34562 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f5dffaa-39d3-3338-84ce-0072b15ef02f | -10.75086 | -54.01915 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59af09d7-f481-3188-ad83-d48ffce0ca9a | -9.48103 | -56.92153 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08648818-0261-3000-bac9-d63a53bd34df | -7.60386 | -67.41771 | 2026-08-26 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adf26ef3-0c16-3015-9b59-7e9a86ea7fcc | -13.19894 | -51.34501 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 57bd6e84-c0fe-311d-9aad-a89d5f7e1425 | -9.99816 | -53.96329 | 2026-08-26 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfb7fffb-57e3-3774-a222-bb9a55aacfd2 | -12.64182 | -48.42567 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4333fce-1b8b-3797-b7da-7a795b3d529d | -14.79301 | -48.79675 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb2d8915-7fd1-383f-9992-86686708aea8 | -13.23928 | -51.37104 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 7e73967b-9f89-3709-bb7f-03daab3250e5 | -13.24048 | -51.3809 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cb5b926b-b67c-3041-aaa9-d35be8611892 | -10.42485 | -61.22142 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f60ce44-3211-3144-9d06-4ca4c48abbd8 | -10.7533 | -54.01029 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e8d6d3e-dadc-3bb6-9f74-735e4de3cad3 | -14.29119 | -51.13046 | 2026-08-26 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcd45eb8-ec9d-30b1-8c53-7cb727f7bf9f | -12.68877 | -48.41357 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1dc6669d-904c-346b-ad8f-19af6c237ff1 | -9.97477 | -53.94315 | 2026-08-26 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65e0b855-400a-352a-b84e-f27e84cb0992 | -13.19936 | -51.34158 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| d35a34a2-e83d-32fd-a067-c940e5236dad | -12.21896 | -54.23401 | 2026-08-26 05:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f91b028-3078-37d8-9f4c-8884face286c | -12.89642 | -59.90772 | 2026-08-26 05:29:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a9f0186-bab3-3621-9692-452011a37d21 | -10.75275 | -54.01442 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60e56de2-691c-31a6-91f8-648e6fe1b453 | -11.16449 | -54.00414 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96ed07f7-b197-3717-af64-3cc190be64e9 | -13.87483 | -54.08728 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a00fddc-82e3-378f-a62d-3741e94a6676 | -9.45105 | -60.53173 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75c89f1c-8e73-31a7-ad9e-8e3da7cdb570 | -9.39521 | -60.5807 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb7f2189-36f5-3e45-ac91-027ddd9aa958 | -9.65356 | -55.09654 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c05f957e-6e8c-3c85-bcc4-edfb43216276 | -9.66292 | -55.08765 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93b83021-e61f-377e-bf20-b45e0dc0d57e | -12.03293 | -46.04288 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 850281c0-206e-3c22-977b-b288c24f1292 | -13.26356 | -51.4598 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff55588d-94f1-36f2-a4fb-a0e1e586a6f2 | -11.21395 | -55.08472 | 2026-08-26 05:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4fa7bd0-2b31-3972-b471-f5ed8c5079e7 | -7.77698 | -61.56884 | 2026-08-26 05:29:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af58b2de-8745-3c9e-afe1-82a1cb2e0598 | -9.0977 | -59.40815 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 485e2f08-0ddd-35aa-9e5b-d9fbaa69c446 | -9.69364 | -55.15475 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4354b784-aa0d-322a-8bcb-eaf4184c5d9e | -14.36417 | -51.7515 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27298d80-42d5-3e04-b032-bd3efa7530bd | -13.23799 | -51.38128 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 65997831-9280-3e3e-92e1-79c34d01966d | -12.89586 | -59.91129 | 2026-08-26 05:29:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d598c7d0-e86d-3cb7-bd57-d085689b8122 | -12.7018 | -48.41362 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 653b5823-7035-3541-bee7-c311e1884311 | -9.91192 | -63.05669 | 2026-08-26 05:29:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41588486-60bf-3b23-9112-802a59e2fe22 | -12.08039 | -64.24636 | 2026-08-26 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47d5a66f-5989-371b-ae18-2f9818ff8ded | -13.25009 | -51.52626 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78310527-6729-3f0a-b3ba-d92145c36685 | -13.25078 | -51.38572 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f754e5cf-732d-3b3e-a0d0-ef876c1088bc | -12.21871 | -54.23181 | 2026-08-26 05:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64de080a-5fff-3b09-8ef3-1457e5fa2ebd | -13.24559 | -51.51888 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae2d8b05-f9f7-3989-abde-bece50228895 | -13.86186 | -54.03253 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e31e467-b639-3238-b0b2-a897f2379358 | -9.13582 | -57.58624 | 2026-08-26 05:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46c2d905-bd8f-3ce9-968f-092abe52855c | -9.66835 | -55.07795 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d0c9133-1b46-3fa8-a670-59852edbee0e | -13.24291 | -51.38538 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| b5534466-9a3f-34a2-b891-6384b6a4cc91 | -9.60868 | -55.10821 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 90dfa287-6451-3ddb-9277-f824a307eeb7 | -9.29233 | -60.91879 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90926559-8fe1-3d45-acab-3779c0ed0761 | -12.66161 | -48.42336 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ccd54132-8482-3de3-a0c6-b80eaf61be81 | -11.76892 | -54.526 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6b8f1825-d413-3fd6-8e20-87bc8db9ad63 | -10.16485 | -55.30967 | 2026-08-26 05:29:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d144820c-f369-3d2b-af87-a44b9aafc39f | -12.67673 | -48.40483 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0730f7d9-7289-3354-b78e-cb80c262dc11 | -8.81641 | -62.31539 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a657801-fca4-34a0-b68d-49c4014a5e07 | -10.76401 | -54.02877 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README63.md)
