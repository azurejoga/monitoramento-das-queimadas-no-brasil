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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fc1552c-78d6-3a02-84b8-1e3e5a36b368 | -15.77334 | -55.5809 | 2026-08-19 06:01:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72969f7e-5215-3108-8bfe-1d3813c7b93c | -16.26457 | -57.66425 | 2026-08-19 06:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f68b6589-d179-3365-849a-11d0d82921b2 | -15.32086 | -56.45073 | 2026-08-19 06:01:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3f4fe5a-5d84-3fb3-9771-d8a37d4b8975 | -11.22783 | -55.07488 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 198fe1ff-8638-3aa3-a8cb-585afe1ca769 | -15.88425 | -55.5704 | 2026-08-19 06:01:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f28ce49d-795a-3257-9476-a02584d527c3 | -15.31372 | -56.45517 | 2026-08-19 06:01:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bef38937-4ae8-3781-9fba-433f32def358 | -9.07753 | -65.40941 | 2026-08-19 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7b26c946-8520-3315-ba98-4718385441a5 | -9.081 | -65.40996 | 2026-08-19 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e07cbe6-1133-334f-b73d-dfc3c71e0081 | -10.91681 | -57.18245 | 2026-08-19 06:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7043c2b6-8fe4-3706-b042-ff7b2d5295c3 | -15.88475 | -55.56495 | 2026-08-19 06:01:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 86fd709f-fd52-37d1-b821-151355ff711c | -11.19535 | -54.82004 | 2026-08-19 06:01:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f739715e-1fe2-35e8-96ad-6761b61540c3 | -15.31944 | -56.4505 | 2026-08-19 06:01:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6075bb6f-0c4b-3ad3-849b-8e66005c85b8 | -15.87979 | -55.56337 | 2026-08-19 06:01:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15e4041b-71be-3fc6-8d1b-1fb373fd1512 | -11.23682 | -55.06913 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08d1b14c-73ec-38a0-9c4a-a0d0d02e008e | -16.26411 | -57.66872 | 2026-08-19 06:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5d64a40d-c671-3629-bb98-9c55cb7533c4 | -15.77388 | -55.57545 | 2026-08-19 06:01:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a98437e-3d2f-3415-baad-119f12bd37cd | -10.9128 | -57.18345 | 2026-08-19 06:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0787dc68-2445-32b1-a3b3-ad7d2e710f28 | -11.22173 | -55.06783 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4accdc1e-647c-37e5-ad3b-8f830d57e4de | -11.23611 | -55.06329 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 707bae13-1ce1-3376-b9bf-a091e0c3370e | -9.08104 | -65.38636 | 2026-08-19 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c5ddb3f-446d-3afc-8dc1-891715af16f7 | -15.88618 | -55.57009 | 2026-08-19 06:01:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69c8964a-5901-301a-ab31-263c986c326a | -9.07694 | -65.41325 | 2026-08-19 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 58f07806-f921-3bf6-80dc-8e28d6857433 | -16.26366 | -57.67312 | 2026-08-19 06:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 84566e3b-ca7f-3751-a575-bbcaaac6c9f2 | -11.69203 | -54.55512 | 2026-08-19 06:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bab521c7-669f-384d-ab51-e67c58b08aa3 | -11.22712 | -55.08093 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4816f39e-8772-3590-84a6-611917d6730b | -19.74497 | -57.92747 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ce833dfe-31c4-3d49-bc2c-20436aa1e9a1 | -19.75081 | -57.93341 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a2641952-85cf-3f7b-82a1-b60e54e7f9ce | -19.74558 | -57.95479 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 8e5c1627-bbaf-32df-9fa5-444e534c19b1 | -19.76348 | -57.93472 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 3a0797c5-74e6-3435-9759-ca221d9009a3 | -19.75033 | -57.93869 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aa5fe495-c42f-31ec-a5fa-771bb47cc8a6 | -19.75327 | -57.93966 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 03cc715d-1485-39b1-9ad1-9f1930e37331 | -19.74785 | -57.9284 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 09a11773-3823-377d-8470-134091df5cc2 | -19.06527 | -57.35738 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b07eca02-f568-3461-963a-7a5fa7d5d4b9 | -19.07125 | -57.36369 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 502828ae-67bd-34ee-9bef-d852a1a53e8b | -19.74739 | -57.93369 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a0551a20-392f-30c0-8cc2-e8aa79d2689e | -19.74886 | -57.95451 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 018f0ca9-4d0a-3f9b-bd08-b5d8d3d49e86 | -19.76005 | -57.93505 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 919d5e07-6084-3c14-9863-6b14e72e9095 | -19.74449 | -57.93275 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 27adfe1e-1df6-3d33-8363-f5c2ac8fbba2 | -19.76298 | -57.93999 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| b8c5a8b3-dcaa-3f0d-b0e3-835d3a900224 | -19.75764 | -57.92878 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 34bd48ea-8024-3425-a2c1-3a0787268c0f | -19.76638 | -57.93573 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| e3ffb7ef-2660-37f2-822e-19a4b80c1c17 | -19.75665 | -57.93935 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 207784bb-b763-3049-85ee-bfe495424e29 | -19.06401 | -57.36222 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9a7d22b3-9c91-3d1e-aee0-73301876c102 | -19.07052 | -57.36291 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1f7e2d6c-e44a-3dd2-995f-cefbd5932a45 | -19.76832 | -57.95121 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e8415cc6-570e-3f9b-bccd-89ab585f2341 | -19.77179 | -57.94696 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 924a5c77-0eb7-3115-8d1c-1da5568d91a6 | -19.77514 | -57.9466 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bd276dd0-12ba-3a84-a699-519fe3f75697 | -19.76931 | -57.94065 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 60dc299e-8e8b-306a-b3ca-41071cee334e | -19.7596 | -57.94033 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| cad0f128-05b4-303d-86ed-dd08c16601f3 | -19.76397 | -57.92944 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| bf48a155-2fc5-343c-bbe8-1aa11a478ad8 | -19.74254 | -57.95385 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a97137c4-c314-31fe-96d9-3d07cbe4fd71 | -19.75372 | -57.93438 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b12d9db3-a767-36af-b527-2580a41bce26 | -19.74984 | -57.94397 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c8ffcb7b-40f0-3958-bf29-1fa1e9b36bc2 | -19.75714 | -57.93407 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 8e812fff-80f4-3ec1-b6f3-cf8e558864ba | -19.77465 | -57.95186 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d3eda4d1-690d-386c-8a94-5349b4562a9b | -19.76592 | -57.94101 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 755f38df-84ea-30b1-8a64-897e32c10202 | -19.07177 | -57.35805 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 06522506-20a6-3678-a466-79104af0829e | -19.75418 | -57.92907 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 646403dd-d4df-39ea-b242-3f081dcd238f | -19.76882 | -57.94593 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| de858717-0064-349e-a6ff-4ff1398990be | -19.0645 | -57.35658 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4eb607ba-738a-3a34-acdb-b5d1abd04e63 | -19.76051 | -57.92975 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| f3dd5220-bff9-31a0-89da-dae1f4c045bf | -19.071 | -57.35727 | 2026-08-19 06:03:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4af786cd-931c-3495-a227-02dcd3a304f3 | -5.9011 | -43.6279 | 2026-08-19 06:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e44a85d6-5d18-33b8-9bd4-f7d6e9e2dd57 | -14.8028 | -46.6683 | 2026-08-19 06:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3cfd323b-c586-3a54-8fc2-8a1e4fa3a287 | -19.7643 | -57.9399 | 2026-08-19 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 220.9 |
| e46f74f4-dbcb-333f-bdcb-eb9a8ba1008b | -21.5343 | -52.0046 | 2026-08-19 06:10:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.0 |
| 5f579826-5587-3b45-8485-1defde4a67c6 | -8.5785 | -54.7566 | 2026-08-19 06:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c3518106-403b-3f2b-b91e-51712615a4df | -8.5598 | -54.7579 | 2026-08-19 06:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ab898abf-fee9-3a0f-8c5a-bfe97a0e8ec7 | -6.0912 | -57.9187 | 2026-08-19 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 39db0649-d124-3296-8546-d4b128649f0c | -21.5338 | -52.0269 | 2026-08-19 06:10:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| 2fd38907-4668-351c-9850-3e452b6676ae | -19.7446 | -57.9217 | 2026-08-19 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 76fa05a0-e3fc-3e2d-9c4c-45cf0b102f6a | -19.7647 | -57.9191 | 2026-08-19 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.4 |
| 58e78492-456e-3579-8bce-fada5c38a8ba | -5.9198 | -43.6264 | 2026-08-19 06:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f72d58b1-126d-3a62-ae21-f6305b7c633e | -5.4317 | -48.4212 | 2026-08-19 06:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 60f74185-e18d-3c1f-917e-a8fb2d028a83 | -9.4256 | -60.4353 | 2026-08-19 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 14d2a4a1-2c57-3121-a51c-057fb2fb5228 | -9.08 | -65.4163 | 2026-08-19 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 79653d7f-0d1d-3e63-94cf-c00ebaf70ff7 | -8.56 | -54.7377 | 2026-08-19 06:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 47d35d7a-1f10-36aa-babf-890118352385 | -14.8033 | -46.6453 | 2026-08-19 06:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 2d6b970c-4462-3c57-9cdb-70ea4ed34159 | -19.7442 | -57.9425 | 2026-08-19 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 147.9 |
| 6346cc9d-adf1-33d9-9fb3-a6645fc332d1 | -19.7844 | -57.9372 | 2026-08-19 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.0 |
| e478c306-5224-3adb-918d-69c9460c38f1 | -3.10238 | -61.22028 | 2026-08-19 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 525b192e-6539-30b5-8b0e-4f94ff7b7dc6 | -3.10166 | -61.22518 | 2026-08-19 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a29781fb-c04f-31a8-9869-b097864b12e3 | -4.27681 | -60.8566 | 2026-08-19 06:18:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a670e4ee-ea30-3868-aab9-8e1e41993753 | -3.098 | -61.2165 | 2026-08-19 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c38ce4f3-05f6-33d5-a1ef-8c1d0b820804 | -3.09616 | -61.21939 | 2026-08-19 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bdd7e05-f228-3cf0-9273-1002496e627d | -3.09725 | -61.22137 | 2026-08-19 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2293b53-ac0e-3462-b0ba-ada362ff5039 | -3.09687 | -61.21452 | 2026-08-19 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2253a4e4-1e40-3745-83d4-c4da941a5a47 | -4.28328 | -60.85751 | 2026-08-19 06:18:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92e3d334-0051-34ba-8478-d72e0790401b | -4.27734 | -60.85513 | 2026-08-19 06:18:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ec2de59-0bf3-3bd8-904c-02b5fc3391ce | -9.08 | -65.4163 | 2026-08-19 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c279cb4a-16c8-3acb-8f25-5d1e35f79669 | -14.8028 | -46.6683 | 2026-08-19 06:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| dc8c4cdd-acd0-344b-bf3f-b677ebe90af6 | -19.7643 | -57.9399 | 2026-08-19 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.5 |
| 34231eb0-e478-3a03-88d3-050d87d5924b | -21.5343 | -52.0046 | 2026-08-19 06:20:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| de0f4739-2861-3dbc-960e-80f6fb71e02b | -9.0801 | -65.3976 | 2026-08-19 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7ce04e99-793f-3d93-b743-520eae9ffb68 | -19.7446 | -57.9217 | 2026-08-19 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 81c0fd15-9b15-365a-9784-6fa881f52f31 | -14.8228 | -46.6419 | 2026-08-19 06:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 5ac31d46-cbec-3433-a159-5ad0a8961adc | -14.8033 | -46.6453 | 2026-08-19 06:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 1c8629ce-826c-30de-afc8-323a92ee3c3e | -8.56 | -54.7377 | 2026-08-19 06:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 82850dec-6f8c-38c0-9979-8cf6999172f1 | -19.7647 | -57.9191 | 2026-08-19 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.8 |
| 0a446d8a-e164-384d-b36d-14d0ee4a42cc | -5.9198 | -43.6264 | 2026-08-19 06:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |


[Clique aqui para ver as próximas entradas](README71.md)
