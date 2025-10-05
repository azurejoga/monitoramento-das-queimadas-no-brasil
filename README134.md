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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b0b36e0-e9b1-3d61-a78e-9202ef0ec1ad | -17.96466 | -57.58627 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5d530649-b2aa-3f60-a718-48f3b07b8b42 | -11.8732 | -56.87733 | 2025-10-05 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 36c13d75-818b-323b-9946-d55d8a14eaff | -13.57603 | -48.17012 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a8c994d-4542-3857-b643-829817f5a090 | -17.89558 | -57.63921 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b65cbd95-16c2-3675-b334-315f9ec1414a | -10.65624 | -58.75926 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf71f805-7f63-3c9b-b6d9-e72a271ae745 | -14.75942 | -54.65513 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfc601dd-3e27-3161-b62f-be125ec3b726 | -12.89484 | -47.32439 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8aa4579a-e1d2-394f-a84d-a9ef5c2cf93d | -14.30048 | -52.92064 | 2025-10-05 05:16:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f5026ba-2431-3f9a-83a9-163d810a4ed1 | -13.28599 | -47.6088 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 039678cd-1540-3605-a019-085109035b0d | -14.64847 | -48.33126 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b1e5dc2-7ffa-376a-a614-ae8e717edfc3 | -13.07672 | -47.91854 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 924f0afe-59e8-3d0a-a378-2c2543904704 | -13.23043 | -47.82194 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 554dc3d2-7ff7-3f62-8bc0-62a63379d272 | -10.18299 | -63.62894 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e5f46e2-182e-367f-a75b-87c111efa943 | -15.22178 | -56.8005 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9afba2b-7fdf-385e-b464-272258e03cb9 | -16.88133 | -49.39812 | 2025-10-05 05:16:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9935ccf2-9ef6-3048-8d3a-7d438fa576bd | -13.14838 | -50.92632 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 62d66fd6-3c97-338d-963b-c5535a205646 | -14.99417 | -49.98052 | 2025-10-05 05:16:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c336441-835f-3598-903b-aa80e1665dda | -13.52066 | -47.28851 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc93c41e-266e-3445-976e-76a05f5aa2bd | -12.91746 | -47.31434 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fd389412-79e0-30ad-a1c9-08112537ab21 | -15.59346 | -52.51318 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e8cb204-0b5e-3550-b990-f53a62d59e8d | -15.29591 | -46.30805 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4034cef3-0405-33a7-99f2-b14ec257296e | -15.58157 | -52.45541 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1819482-eedf-305b-a24a-f4e2a350b3bb | -16.04947 | -50.93737 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb038576-454d-3bfd-8c48-65d6ae779d9e | -13.15049 | -50.90942 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 79bbc542-1bdd-3cfe-ab0b-3b173e594a59 | -15.61349 | -52.50026 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a85a4ae6-9961-308b-ab0e-61d1b4577981 | -12.31456 | -55.14231 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13039c3a-903b-30e8-875b-2b3619bdf1a8 | -15.59012 | -52.50294 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9ea79948-b728-3fec-9c83-2f4d58dee53d | -12.59237 | -48.14595 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd8611d8-9513-367d-9493-40622e1a818f | -18.24335 | -53.36538 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6731f44d-3532-30d4-a40b-38a5d9201682 | -13.56717 | -48.16721 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a8e35f9-9dd6-3248-a749-0213e3aa347e | -17.87802 | -57.63667 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9e11e284-7e55-3d63-973f-385b4ff8a98b | -13.30087 | -47.80128 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17f39087-363b-34f5-b073-556783e7af7c | -14.92024 | -46.8403 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2412f44-c16f-367c-a664-2d49c5ce202e | -13.08598 | -47.89069 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2784979b-5457-3e78-8501-813f2f4d3677 | -15.60402 | -52.46325 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 117818b7-8575-325e-82f5-995c1bc5f834 | -13.13705 | -50.89613 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad8dd010-32ad-3939-ae28-d1f8ef858341 | -15.1989 | -56.83585 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f63730a-83f6-31f9-8da5-1a80ac5df9e0 | -13.49008 | -47.27685 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8924ad7-3cac-3961-adaa-b4687e99ec60 | -16.16406 | -57.57756 | 2025-10-05 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1e35ea22-c55c-39ca-bceb-a0615107b8f0 | -14.65966 | -48.3395 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba733e7b-569e-3a57-8f22-4cf807a5d1c6 | -13.73406 | -48.07676 | 2025-10-05 05:16:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f3981cd1-2353-32d8-b601-68690f0a1801 | -17.96217 | -57.55377 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5c6a3efd-3cb7-3038-9605-7619c42e4428 | -12.59084 | -48.15942 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83972b1c-ce09-378a-9d62-4b1b1db2de9f | -12.89537 | -47.31953 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6e495d81-adca-3a52-8f45-76509356ead2 | -14.70282 | -48.35149 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0ec7606-6028-353b-b530-f137ac8be920 | -10.83157 | -57.168 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3205556-86e8-3e55-b2f7-51fb9b4391e3 | -17.91137 | -57.63203 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ef2d7661-d022-3ee3-a0de-ea49bbcfb0f5 | -13.10485 | -47.93911 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd28ada7-9b64-3146-973b-67436ecca688 | -13.2561 | -47.81273 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46cb453e-e03f-3b97-8fb7-099ae850f03d | -13.25165 | -48.49475 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2b9fb05-444e-3650-a4ae-ca8164537bf2 | -16.07278 | -50.9166 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 093b25bf-ad6d-32db-82e0-42d502a0a20d | -14.74694 | -54.65815 | 2025-10-05 05:16:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 669c9ade-f372-3f11-ab05-eab7e418f1fb | -18.25283 | -53.3407 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8e6371a4-ed7a-31c1-b9c6-d0a5e43d0a53 | -14.75405 | -54.66475 | 2025-10-05 05:16:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4cf8c1cf-d996-3629-a31b-4d24bd4d2aa2 | -12.81968 | -46.85769 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77e896df-21b6-31c5-be99-da3885fd203b | -18.16524 | -53.33116 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4429654f-a764-3ee6-b3e8-8fc1f525e228 | -14.33474 | -47.68157 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9952aa56-9b63-3fb0-861d-38edb219c919 | -15.91618 | -48.82995 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 21769b35-3e0c-3f37-b964-d89c87c5f598 | -13.20958 | -46.78148 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7b2ee7a4-2f9c-342b-9a5c-324a250404c9 | -14.69107 | -48.27608 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b2f09c4-0117-3a0c-8f6f-f8bfd53f1cdc | -13.30202 | -47.79104 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35383c69-b307-33ea-9e20-e049241be470 | -18.20477 | -53.38195 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7539dc8-2f61-382d-93b9-d9464cf49a76 | -11.95353 | -51.4679 | 2025-10-05 05:16:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62491090-8568-383b-98a6-0794fd683d75 | -13.14525 | -47.98035 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4878b1f5-4ae1-3243-a4ce-a41235a923e5 | -13.28479 | -47.61005 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c52e32d-0878-35c8-8fb6-3a0a29cb2cda | -15.31383 | -56.93331 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf660d03-cef7-3988-bb08-640b04390ffa | -18.25225 | -53.36729 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69b93b6b-c090-3877-9812-31b0f6f8a035 | -15.5251 | -46.8704 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16145f59-e414-3c8b-9e01-6df7f528a30c | -16.34022 | -51.4707 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9238e3c5-2778-3b31-baab-cb2f49f3a1c1 | -12.98899 | -51.0148 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2de429f6-5011-3935-992c-1ab1f2c9d661 | -15.39454 | -47.9545 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 753ec4c4-b198-3629-8afe-f9e59f2bccd7 | -17.89969 | -57.63848 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ac7e25f8-dd4b-3c28-a937-be360f46ab89 | -16.36575 | -51.46849 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25d723f4-c675-32fc-ac5e-0cafe48b04aa | -13.1413 | -50.90245 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2cf7c40f-007a-329e-93b8-1e0705074707 | -13.30237 | -47.62025 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df5adc88-e8f8-325d-81fb-0c9a93042479 | -11.22033 | -57.02199 | 2025-10-05 05:16:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3aeef68-c2a3-35f1-9ea6-69d4d4752622 | -14.66904 | -48.30987 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b41f1f73-e154-37ca-9876-b8269608129d | -15.60375 | -52.50356 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f36bb6e-2b13-3889-a5a8-032a916dea45 | -15.36687 | -47.98052 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45265793-89ff-3300-bfb0-fc9d608c2282 | -12.9827 | -51.04428 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4e3c08b-1105-3e12-a6ae-a28ef818bbf9 | -13.15166 | -47.97736 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d63f443-84fd-3e23-b928-c81a2bdc2ef9 | -17.95695 | -57.56496 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ab4dffbd-baf6-3686-a592-898ca8bc8c6e | -14.58886 | -52.45252 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 207f966f-5b99-3698-b7af-15410a11ccd0 | -12.30713 | -55.1412 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23afe197-db29-3cbb-8b26-0e7ccdac2c5c | -12.31391 | -55.14674 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3945c42e-b9b0-39b9-bcc0-03c1c92c0449 | -14.7578 | -54.65645 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd58d055-fdb4-3078-9f0b-8da70cae0982 | -16.38648 | -52.15834 | 2025-10-05 05:16:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 03c06fa7-a35d-32f7-8e4a-038d1c401dfc | -12.30101 | -55.13113 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2db9c693-5ff9-3388-88e2-35c76547294a | -16.06343 | -50.90747 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c622546-783f-3595-a9b6-6422f01b64b8 | -13.13065 | -47.97902 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df5d7f1f-0855-3360-9b18-5bab6c2cc39a | -14.83118 | -54.76514 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f27539bb-710b-3ee4-bc6c-89283215fb6a | -13.4897 | -47.28031 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6f69bf5-a741-3852-b2db-d9ef7f650e3d | -11.51183 | -54.46903 | 2025-10-05 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 321e4d6c-1075-3597-9558-90d5785d13f5 | -17.33235 | -54.20177 | 2025-10-05 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 71c2b525-6b8f-31ee-bf7c-10e7ad1869dd | -13.24216 | -48.47496 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6d46ae1-f1e1-3294-b7cc-dd839c5fa0bd | -12.81334 | -46.85632 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 859e3802-4f04-302f-9bf3-bcd813da4d07 | -15.7772 | -49.09375 | 2025-10-05 05:16:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b31d741e-9967-3db3-8055-557d5022483c | -15.61409 | -52.49546 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca82d3ba-704a-345f-a39b-8e470a6185e1 | -17.70885 | -56.77603 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a4757750-d3ad-36b2-97d0-1addc43fbdfb | -15.29795 | -59.23693 | 2025-10-05 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README135.md)
