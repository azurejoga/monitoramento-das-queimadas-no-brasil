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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d454c42-f133-3915-aed8-0513d4d3d5f1 | -13.376 | -48.00826 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de17a4d7-7cc5-30eb-8a61-a9d103331ab0 | -16.02743 | -47.90366 | 2026-09-12 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f4c328c-29b4-3bce-809d-f7d589a867ea | -14.842 | -48.16385 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46fad182-eee5-3bbd-a37d-e7b220ad5485 | -18.66791 | -42.00433 | 2026-09-12 04:36:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 143415c3-754b-333e-abb2-172407cc0e2e | -18.64909 | -42.82875 | 2026-09-12 04:36:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a9e98f1d-f24b-3218-a07d-20721b856d5d | -15.98735 | -52.72017 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84e7b62c-c89b-3de8-8e5a-180688cf8a65 | -18.62261 | -46.32089 | 2026-09-12 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef792452-cc96-385b-9446-0b78ea7c9630 | -18.4866 | -51.70874 | 2026-09-12 04:36:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac297694-7449-379e-b54f-f3187f3d38a8 | -16.02984 | -52.65846 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d8fa36d-877e-3aa9-b5f7-006aa115e0b2 | -14.95627 | -47.52808 | 2026-09-12 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a93de95d-9ce5-371e-bcba-4d696cb27943 | -13.30774 | -51.64317 | 2026-09-12 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63db87d2-e259-3760-9dea-14343e08dd94 | -14.58674 | -48.82995 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff41b598-e38f-359d-a56c-261517576006 | -14.90562 | -47.75424 | 2026-09-12 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08cbebd4-da86-33f5-8857-c555049f3c20 | -13.30837 | -51.63939 | 2026-09-12 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26660f7b-34df-329f-8711-2dae853ed4ca | -14.58618 | -48.83359 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0c1f717-7097-3804-8c40-f3013952b2ae | -14.58863 | -48.83423 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e43fdb15-5801-30ff-a298-5286f1e3e0d3 | -13.35416 | -51.76907 | 2026-09-12 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69e945e1-bb57-3f79-85f0-006d0920dadb | -17.03631 | -47.17276 | 2026-09-12 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd13759c-477a-32ab-8e20-9d31d86745f5 | -17.10907 | -51.25668 | 2026-09-12 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8adacca-b450-36be-87d9-607eade1492b | -15.45011 | -41.38601 | 2026-09-12 04:36:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bffd9b30-df7c-3383-9a23-b20fb9aeb2d1 | -18.66868 | -41.99726 | 2026-09-12 04:36:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e4360af8-34e5-3dd8-856b-f9b94c2e6d9c | -14.84087 | -48.17154 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 972e3a3a-692e-35f7-99ec-34db0a0a9c0c | -18.64995 | -47.29369 | 2026-09-12 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa3f39d6-5010-3eae-8e3a-c2faac9ef6aa | -13.37491 | -48.0155 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ab6ede7c-70b6-3282-9536-14f624a3b602 | -19.86888 | -42.64086 | 2026-09-12 04:36:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2906ab03-cb93-3faa-b6ad-71374a76ec59 | -15.98253 | -52.72754 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f1a6cbc-36fa-3f25-be98-45bb8fda8949 | -15.7737 | -48.564 | 2026-09-12 04:36:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16482053-0757-3e7c-b1f8-8ea2fd955ee2 | -18.93944 | -46.83331 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba7d2385-6c04-3021-b0ea-1df278ed3e16 | -16.96253 | -53.08304 | 2026-09-12 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3067142c-b07c-38ae-87f9-748b3840df66 | -14.39146 | -43.78563 | 2026-09-12 04:36:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3840a70f-9f53-3e3a-b021-24a359d840f5 | -14.29576 | -43.69283 | 2026-09-12 04:36:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71fba8d2-a9f2-36c7-b809-ccedd221913b | -17.03269 | -47.17227 | 2026-09-12 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0cc0e111-6365-3080-a9e3-da2367740296 | -14.59031 | -52.66602 | 2026-09-12 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7058eb5-0ba7-3843-9108-8d9fee3ecef5 | -17.17463 | -55.92783 | 2026-09-12 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6802bf01-8fb9-323c-bd21-125e64aa79c6 | -15.0572 | -48.52568 | 2026-09-12 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0412bb2d-bf4c-3692-a439-95cee3c91b20 | -17.03209 | -47.17662 | 2026-09-12 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06c62756-f2b1-3152-b27a-7a4dd97cea80 | -15.019 | -48.5042 | 2026-09-12 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34ce5012-a0fd-3a69-8f34-742d1d43f708 | -14.59197 | -48.83477 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ac4ad4ba-299f-38ef-9ef8-57578695ec4c | -18.64262 | -47.29262 | 2026-09-12 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 211afc02-b565-3680-b9a5-f1954e898491 | -15.44533 | -41.38256 | 2026-09-12 04:36:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f25f5ce1-344e-348f-a9ae-d67fe651166e | -19.74589 | -46.04767 | 2026-09-12 04:36:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 224c7e88-531b-3bf5-af28-6e3ace248dd8 | -14.59142 | -48.83844 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7aac80ed-7178-39c2-9eb0-af4ef8a3eeb7 | -16.03744 | -52.65568 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dfb6c9e9-ff82-35af-9c7d-a1000ccd7841 | -13.46737 | -48.50232 | 2026-09-12 04:36:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e454650e-e23f-346c-8578-b6f1ac5e4fb1 | -13.37099 | -48.01859 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 650fafdc-637d-3d24-8070-f927fc65fd9f | -15.55907 | -54.24273 | 2026-09-12 04:36:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c095f3d1-20e8-356e-b33b-4c6e2760876d | -16.52685 | -50.83096 | 2026-09-12 04:36:00 | NOAA-21 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ca64b4f-9ecd-3f2c-a124-d9e474d214f3 | -16.04437 | -52.65694 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d343c51c-08c0-3eb6-af90-959b87bc9f4a | -15.68875 | -52.76562 | 2026-09-12 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 27b5f275-3ae0-3483-a65d-b2f0be89b8c8 | -16.29118 | -53.85106 | 2026-09-12 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c930633-8591-35d5-a7f0-943082a19f3c | -16.03397 | -52.65505 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e5cada2-a009-3c4c-a50e-71400a256d3b | -14.90907 | -47.75476 | 2026-09-12 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9e7ac4f-3f48-393e-9766-6e3f825035b2 | -14.57908 | -52.66813 | 2026-09-12 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7092ff54-3fcf-35ed-860e-0a4f3281e614 | -15.66014 | -48.29182 | 2026-09-12 04:36:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94eb0f63-f2a9-339a-bc75-91f9247d55c5 | -14.91298 | -44.67149 | 2026-09-12 04:36:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 252a4704-afe9-302b-b1db-a159126a2d31 | -16.68453 | -43.08292 | 2026-09-12 04:36:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 275ab29f-8f7f-38fd-81d4-61fdc93741cf | -16.09383 | -50.12296 | 2026-09-12 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 406ddddf-b14f-3514-ba0c-12cee4d432f7 | -17.6823 | -44.19868 | 2026-09-12 04:36:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2366e2f7-f008-32c6-adad-4a63293e9f2e | -17.03571 | -47.17711 | 2026-09-12 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad06e901-5f56-3477-b3d1-a13a15654d6c | -17.69597 | -52.34074 | 2026-09-12 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 031bab5b-ec58-3208-8abd-b444a37c1197 | -18.41076 | -46.05193 | 2026-09-12 04:36:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c541289-8986-37f9-89e7-d2b6e68de65f | -13.54065 | -49.48877 | 2026-09-12 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be9eb1c7-45cf-399d-8202-a627b3758c9b | -18.87454 | -46.97677 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fcb23f7e-1cb0-3196-b27f-c3d05bd39c0a | -14.98298 | -53.95342 | 2026-09-12 04:36:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b2bd743-7670-3970-9945-69d8ec19bcf7 | -15.02292 | -48.50104 | 2026-09-12 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a46591b-5416-3e63-9607-d61ceae5d00b | -17.69937 | -52.34131 | 2026-09-12 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 323ff72e-8d2b-33a2-9c01-77ab88225762 | -16.01275 | -52.6967 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5abd7f6-9fe5-3415-af11-daf38c1629b1 | -15.62146 | -48.26691 | 2026-09-12 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23bd9233-e91e-3831-9366-65779f5eea38 | -14.58918 | -48.83057 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3f489911-8f99-394a-9776-14e899da8a4b | -18.66829 | -42.00083 | 2026-09-12 04:36:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4ade1150-c751-3eb0-add0-0b0af382a268 | -15.98387 | -52.71956 | 2026-09-12 04:36:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 699c91de-e045-3ba3-ad81-01c13ad87b6a | -19.74397 | -46.04835 | 2026-09-12 04:36:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2112fe90-e458-3f82-9fb7-b47b27372db1 | -19.11265 | -46.7482 | 2026-09-12 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9e34676-8c65-3072-9115-56108486732d | -14.91347 | -44.66778 | 2026-09-12 04:36:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14e69e2a-2254-37e6-8055-0c05828edf33 | -15.2542 | -53.89083 | 2026-09-12 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ad3f06b-248d-3a9b-b2bb-8667fc83e562 | -18.86387 | -44.08536 | 2026-09-12 04:36:00 | NOAA-21 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b44d458e-4f14-362a-ad7d-a99b16999d56 | -13.37938 | -48.00883 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 640ad69f-317e-3b60-a762-d8046a4f842e | -14.59087 | -48.84209 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07acf517-74ec-3270-816b-e9caa321d7c7 | -18.93568 | -46.8327 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db30a358-d9d2-3fb4-b8ee-1ada8035be80 | -13.37884 | -48.01244 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9568750c-f0d4-396c-a658-2873b4f9ac67 | -15.55534 | -54.24187 | 2026-09-12 04:36:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9028d36c-2a22-3c87-93fc-90aa65329abc | -13.46239 | -48.51258 | 2026-09-12 04:36:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bab05dc-a9cd-38e8-aa58-7ec056487d14 | -18.62003 | -46.32273 | 2026-09-12 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ca647aa-b9fc-328b-b7bd-3d44519fbc2e | -16.02528 | -47.90378 | 2026-09-12 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 321efb88-3daf-30d7-a7c3-f609704ea734 | -14.91754 | -44.66836 | 2026-09-12 04:36:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f957b6c-44c7-32c6-b3a8-15d6ed2c8f9b | -15.04765 | -48.52032 | 2026-09-12 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01c570d0-a552-36df-a14a-4f194f295b0e | -16.02875 | -47.90426 | 2026-09-12 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55194324-c486-34d7-9e03-228d7d32ce7e | -13.79257 | -48.80063 | 2026-09-12 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e62c6660-b0eb-3b7a-93ca-53744c7180ca | -15.58825 | -54.52308 | 2026-09-12 04:36:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a35304d7-5799-31f7-a963-50f838d8e2dc | -13.37044 | -48.02223 | 2026-09-12 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c38eccf7-493a-3e60-85dc-9247447a2db4 | -18.66316 | -42.00031 | 2026-09-12 04:36:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ca883687-aaf8-36e3-a0e3-2e56092a9bf5 | -18.41789 | -46.05828 | 2026-09-12 04:36:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11cdddfb-3215-336d-9951-21c9b9629021 | -15.62951 | -48.89436 | 2026-09-12 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f602d432-d90a-300b-b285-36e834b5fc1f | -19.1123 | -46.75161 | 2026-09-12 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c027eea-4def-3ba9-81e0-3687a2d8d856 | -13.48074 | -48.50444 | 2026-09-12 04:36:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce20b3f3-f975-3fe5-8790-e4d9b9ae1fab | -16.29481 | -53.85181 | 2026-09-12 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3c4eb91-9d57-3430-8638-109d826be36b | -13.86105 | -49.89631 | 2026-09-12 04:36:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21f09747-9c9e-3f94-8828-a61c5cfc6481 | -14.58507 | -48.84088 | 2026-09-12 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7e16183-4dcd-3955-9b13-b4bc574026a3 | -19.7723 | -43.97485 | 2026-09-12 04:36:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d98b7ccc-872b-3cb3-b5e3-81dc395fff1d | -15.01955 | -48.5005 | 2026-09-12 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README31.md)
