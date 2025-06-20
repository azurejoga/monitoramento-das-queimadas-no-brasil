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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d761388b-772f-32ee-b67e-575027648ec2 | -12.02932 | -57.08843 | 2025-06-20 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8aafc60-6862-35d2-a088-aa7fbed30e8f | -14.30847 | -59.8909 | 2025-06-20 05:21:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a56c20e-b634-35c0-b555-1ade3eff265e | -11.9569 | -58.75536 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 01f7853e-a82d-39f8-b0e0-debbf246cd9d | -12.28494 | -57.27075 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbd9fba3-b63f-3fd1-98c2-691b137444ec | -10.07911 | -52.74645 | 2025-06-20 05:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 15e45fb9-71de-32da-8b81-54e47d84a9a2 | -12.50837 | -58.35844 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ebc98843-a192-3c26-ba01-4f043600a984 | -11.96086 | -58.75219 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c9c4d0f-6be6-3ee4-a9a5-f78c11bb45b3 | -10.83356 | -54.01665 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37d68e14-4007-3a70-bc7e-07713b4f4410 | -14.48077 | -50.28899 | 2025-06-20 05:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d46c5c6-d7fd-3ec0-99e7-7ec89682a13f | -12.04109 | -63.7763 | 2025-06-20 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1f68d0c-fc2c-3ea4-9653-25116579a59d | -11.9603 | -58.75586 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c20ee4f5-0134-3150-a008-915ab8a395bf | -10.47736 | -47.03126 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 0b0e4eaf-bbf4-3796-ba63-426f4853716b | -14.03805 | -53.37044 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1328ac32-babd-36da-986e-83f604481944 | -10.45858 | -47.06234 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5133766b-96e3-3118-b5ac-a528aff26db4 | -11.82221 | -54.50018 | 2025-06-20 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecddb335-d30c-346b-9184-014649ce4cd7 | -14.03741 | -53.36358 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3aee6778-6ac8-3940-b096-aa960d6001bc | -11.95067 | -58.75062 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f510653-be25-34de-ad6e-9906bdfa3e26 | -12.04844 | -63.77761 | 2025-06-20 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5e85e7a3-a4f2-3379-adfc-aeeb3bf2d828 | -15.47725 | -46.59182 | 2025-06-20 05:21:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 70f2d550-c549-37bd-adac-c6c04e72510c | -11.92013 | -54.82004 | 2025-06-20 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 145a9822-ebdd-38a0-ac20-43019a91f0ea | -10.52886 | -46.6472 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d39b502a-c618-3488-9e0e-d18e0232f497 | -10.6616 | -49.36594 | 2025-06-20 05:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f467b6d8-16bb-3f74-99ca-aee999a47704 | -10.52191 | -46.64639 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60d4e5ae-bdc9-3f94-a0f1-e7cdfbc79153 | -10.54607 | -46.98962 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d8686fb-58cf-3ec2-99f7-123d6a93ac61 | -10.83568 | -54.01457 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94412af6-e998-3d5d-80bf-549305360cf0 | -12.19994 | -49.61735 | 2025-06-20 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e0a2a68-3c6b-3123-aba8-0b79e3789af8 | -11.95237 | -58.76221 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c48d2d8-12bb-390e-9f12-cfa0f8885c93 | -14.81375 | -48.46491 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32d3279a-de13-31ac-91ad-b17994b7781b | -13.77922 | -54.19481 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd80f1ff-5fbc-3e11-b2c8-d669a1f737df | -8.91359 | -49.85106 | 2025-06-20 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c03cd5a3-3457-35c4-af1f-57bfc0aa67a9 | -11.12538 | -46.67248 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd80aa6a-64c5-33e2-ba72-b5cc7ebcf7c4 | -10.54497 | -46.9838 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1969996-9ebe-3aca-ae53-505101bf99de | -12.52465 | -57.20903 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebb87b64-9ffa-3307-bdc2-77e2e3f4e666 | -9.93676 | -65.01283 | 2025-06-20 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33574e95-9a5d-3b22-8dfa-4d4169b9c860 | -11.535 | -56.98693 | 2025-06-20 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc05577a-c721-335b-a98c-7f3336d2a936 | -10.86981 | -53.75903 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55cb188e-7373-3a53-91db-fa14defdd8d5 | -9.95741 | -64.99035 | 2025-06-20 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17d977ed-68d6-35f6-8f9d-5e74313b0fea | -10.46002 | -47.05052 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 2a5ea7b3-55b3-34ac-8944-966ff4d37346 | -13.1458 | -56.81153 | 2025-06-20 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94e6a361-3908-35e0-8e18-9cea20bd053e | -10.46917 | -47.04262 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| e8470b16-138e-3df2-82fa-a6f6bc4214b6 | -12.3538 | -49.30869 | 2025-06-20 05:21:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51d72657-0d86-300a-981e-987bf58efeca | -10.83138 | -54.01394 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c80f2a99-b7ac-317f-a717-f1d707d44766 | -12.64666 | -54.12199 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5b9c611-5384-32dd-aebf-24fa03f203e7 | -11.15119 | -46.64956 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b12cf992-001a-35b2-b0f2-9cfd0173b1bc | -10.54423 | -46.98998 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ac01184-6644-3ea2-a684-4b7f529f3023 | -12.02448 | -57.09632 | 2025-06-20 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a748063f-2f9b-3390-9345-c3a0f878313b | -11.94671 | -58.75377 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6ac7994-74bc-347d-add3-f588d7bf4666 | -13.97736 | -58.10438 | 2025-06-20 05:21:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72c9d690-cd36-3def-bc61-8e32a8a6c3f4 | -9.46037 | -57.8425 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2572b086-4d3f-3d53-b3f3-7052efcda1c4 | -10.86486 | -53.7627 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08563438-3cf6-3493-af33-cf097fec1f2d | -13.26166 | -46.81984 | 2025-06-20 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e487af2-5611-3db0-860b-08557bc962ec | -11.53377 | -56.99536 | 2025-06-20 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abe06063-1d6c-3c56-8dfe-fbd48909705a | -9.48815 | -56.08204 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b9c21844-d275-3ab4-bafd-e7a05250a34c | -12.55097 | -57.70692 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e452e6ee-9b1b-3bc8-9865-5cba77cbb123 | -12.20532 | -49.6224 | 2025-06-20 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1353cc1d-8c82-3371-978b-5f62764e2496 | -14.17254 | -60.05061 | 2025-06-20 05:21:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19ffab78-4521-303a-8eab-ea3d12d3c6f2 | -13.10014 | -52.29342 | 2025-06-20 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59ce50ac-98e7-3886-a612-57ca52983e54 | -12.0275 | -57.10112 | 2025-06-20 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e691686e-bea6-3239-ab31-ee2a00abe50d | -10.15657 | -48.98522 | 2025-06-20 05:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cb1ff3a-671e-3048-a737-47547c3bcb39 | -9.31541 | -47.79511 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f8bd117-7475-3264-be04-407bb6580966 | -11.13113 | -46.63953 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6618454f-3998-3467-a587-66601099cbc5 | -11.92064 | -54.81628 | 2025-06-20 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce0ae0d6-afdd-3be0-882a-6c746ac12cd3 | -10.02787 | -62.1346 | 2025-06-20 05:21:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee3b8e66-159b-3775-a8bd-17b6a336733f | -9.46493 | -57.83557 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db597947-5954-34ad-840d-e37630e87584 | -10.51818 | -47.58267 | 2025-06-20 05:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77552715-4c65-31d0-a5cc-acd4fcf91728 | -10.49024 | -47.03872 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a27c9191-15c7-3c24-abd8-744a894afe9d | -10.45291 | -47.06445 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 00ae9059-fbf2-3a76-aaad-dd09d9df0ead | -13.14207 | -56.81099 | 2025-06-20 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd12676f-d5ba-3a96-b4f7-3f0883738b78 | -12.23067 | -54.29777 | 2025-06-20 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7310141-998e-35d6-9f35-3dd59b00a692 | -10.48329 | -47.02897 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 13d44e56-2960-3dc4-adbe-f2247af97710 | -11.84079 | -57.76453 | 2025-06-20 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46a62eff-862f-3509-92ad-175cc16b2c32 | -14.43048 | -48.92167 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f2b4edb-10a5-3edf-97c0-3027ddaec468 | -12.04476 | -63.77696 | 2025-06-20 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0762197-f9a3-30f5-81ee-7418a29210f8 | -14.04276 | -53.37108 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8569d131-6672-34ab-85c3-bfa43211d40b | -15.47742 | -46.59466 | 2025-06-20 05:21:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 75cae629-9d10-3c38-9898-97cb3f8297af | -9.09662 | -50.02988 | 2025-06-20 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51cd0c0f-9fbc-3110-8cab-3c6217b61b95 | -15.47818 | -46.58665 | 2025-06-20 05:21:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e0a8bc16-8250-30da-a88a-e66dedfadc0c | -11.87455 | -54.67814 | 2025-06-20 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45f260c9-87b1-3781-984a-8c3d3a654b6f | -12.52528 | -57.20479 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef9b85d1-fd60-3652-b039-097f70b42f3d | -10.85959 | -53.76907 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a8b5b6b-cddd-3de7-b772-af66cee49f04 | -11.95463 | -58.74747 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3106a532-7454-36d7-8c35-07355a015ffc | -14.03868 | -53.36534 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f02b74e4-c26e-3ad1-ae8d-9168dc5f9c6e | -12.04401 | -63.78132 | 2025-06-20 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f62f91ef-fa4b-3ee5-891a-8dfcf6ebe84e | -11.45857 | -47.30077 | 2025-06-20 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ece6c498-59ca-38ad-96f0-2b5ed06d572e | -13.39245 | -48.45598 | 2025-06-20 05:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbe0f3db-67aa-32ff-a0b3-053f95b30645 | -9.10214 | -50.03057 | 2025-06-20 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fb0c91c-fb18-30a2-9bd4-3fc7073f380f | -13.77863 | -54.19924 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ce8f8443-8463-3c6d-8b0c-dece60cba00e | -9.45581 | -57.84942 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31d2ec27-0545-3c40-b4a6-028442e62f49 | -12.5533 | -57.71558 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20ed1956-bacf-3c4f-9c0e-d250188983ce | -9.46094 | -57.83877 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b5149e4-2091-3d19-aef0-8ac144b812ab | -10.48487 | -47.02584 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9edabcbb-e257-32e9-9579-ba8a0404f725 | -10.53579 | -46.64811 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ba662a9-9bd5-3d02-9900-747a78888798 | -13.38603 | -48.45509 | 2025-06-20 05:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37f26354-50bd-37bc-8b9f-62b067cfedcc | -11.79801 | -48.0935 | 2025-06-20 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed01b049-4bf5-3708-af27-ba8598312deb | -10.52473 | -47.58355 | 2025-06-20 05:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77b467dc-dbea-36a6-a7ac-0514985b8f34 | -11.1504 | -46.65619 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 67360d45-c119-3232-acb0-ab400ecaf5bc | -11.80447 | -48.09431 | 2025-06-20 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93045617-c829-3f30-89e4-66377c8463ca | -10.48252 | -47.03518 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d920ca0d-897a-31d7-875c-bd96d2c2475a | -12.58054 | -56.97318 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2219d2a7-4271-3895-bbe6-313f024789f4 | -9.4638 | -57.84304 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README25.md)
