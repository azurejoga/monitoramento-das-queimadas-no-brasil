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

## Dados Diários - Página 205

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7234a78f-01d1-35bc-bcc4-88f190195652 | -11.3172 | -46.7024 | 2026-10-08 10:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 7e373141-7205-396e-99ba-e15fa32174e7 | -11.3363 | -46.6998 | 2026-10-08 10:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 2e7e2172-97bf-33f5-9030-53e16e60bcac | -11.3176 | -46.6798 | 2026-10-08 10:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| fb2626b8-3175-364d-b82e-e85cc16f4c51 | -14.2092 | -41.8318 | 2026-10-08 10:10:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 560126bc-c6e1-3a26-9e5b-688b32e58a1c | -11.3172 | -46.7024 | 2026-10-08 10:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| a9f3db13-ce1b-311f-9bc6-1d0c44431fc4 | -11.3363 | -46.6998 | 2026-10-08 10:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 68faee40-6593-3b9c-a50d-1575c3f346d9 | -14.2092 | -41.8318 | 2026-10-08 10:30:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 7d74a101-feb4-3270-8aa5-a2658e7d3052 | -11.2482 | -46.2604 | 2026-10-08 10:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0c29ace1-f9aa-3eeb-bf8a-cc5bc76006f4 | -14.2092 | -41.8318 | 2026-10-08 10:40:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 3023a58c-a44b-32a9-8d62-837e995f0773 | -6.88329 | -35.29359 | 2026-10-08 10:41:00 | TERRA_M-M | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| bb4324cb-e396-3fa9-90a1-92b644c2269f | -8.68134 | -36.89315 | 2026-10-08 10:41:00 | TERRA_M-M | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 5f7cff5a-6d37-3b91-8d51-365d648fd16a | -14.20228 | -41.82114 | 2026-10-08 10:43:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 79.5 |
| feb9c35d-268b-36db-82f3-1c509e5ff248 | -14.22583 | -40.64032 | 2026-10-08 10:43:00 | TERRA_M-M | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| dcb21873-1a84-3757-966b-45073bf2a507 | -14.21679 | -41.82414 | 2026-10-08 10:43:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 2c692e64-9a67-3312-b3cd-356f6856c3e7 | -14.2119 | -41.85167 | 2026-10-08 10:43:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 26.6 |
| dbaae456-79c0-3e6d-9e82-675d0730953f | -11.3172 | -46.7024 | 2026-10-08 10:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c216d77a-fbe2-32a6-b945-2d6feedefda7 | -14.2092 | -41.8318 | 2026-10-08 10:50:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 118.6 |
| cd5a4d44-e988-3e33-967d-86adebdb9082 | -14.1896 | -41.8358 | 2026-10-08 10:50:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 94.2 |
| a4732d58-8f23-3883-9350-015faabd1c2d | -11.0953 | -44.0037 | 2026-10-08 11:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 70f7a948-3774-333b-9bc7-37250c8886c6 | -11.0953 | -44.0037 | 2026-10-08 11:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0a485314-986f-3307-abdf-3fbe151b7b05 | -11.6369 | -43.6876 | 2026-10-08 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| fe4b71d9-53dd-37ee-af6b-a689699210da | -11.3176 | -46.6798 | 2026-10-08 11:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| edf9fd03-8b70-3184-980e-530aac8915e9 | -11.2482 | -46.2604 | 2026-10-08 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| bff0c0ca-a370-3eb4-8b72-27e22b78bf0a | -11.6369 | -43.6876 | 2026-10-08 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| d8263b08-24b2-383c-b4d5-614ca2a4dd7f | -11.3937 | -46.6922 | 2026-10-08 11:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e3af08b5-aac8-325b-b4e9-a23b2734e4e8 | -11.6365 | -43.7113 | 2026-10-08 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 157d6813-8294-3d03-bebb-a616b1f2f85e | -11.6186 | -43.6433 | 2026-10-08 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 289aa2a1-dc41-3cd7-8d5a-334e080131ab | -9.1543 | -49.8142 | 2026-10-08 11:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 4a367f0d-00ad-3c47-b247-59225bafab9b | -10.4337 | -47.2824 | 2026-10-08 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 9bcdf7f3-caf5-3a75-a957-f762dcaadc07 | -8.6107 | -67.0301 | 2026-10-08 11:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 67d8046a-f9aa-3b6c-880a-7bdab6a513bb | -11.3176 | -46.6798 | 2026-10-08 11:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 1dc85118-310d-396a-919a-d7517a5b0d58 | -11.6369 | -43.6876 | 2026-10-08 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 917504af-b39b-3a10-b841-d0dbee20f19f | -7.2185 | -55.1016 | 2026-10-08 11:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| cf3d66f5-f387-3674-8aab-a3322675be4f | -7.2369 | -55.1206 | 2026-10-08 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| ecb0875f-6f4e-3268-885a-cc2281d139d4 | -7.2185 | -55.1016 | 2026-10-08 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 0e6b9167-89c2-39e0-9a5f-19b4555ac612 | -8.6107 | -67.0301 | 2026-10-08 11:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 3c5c807a-aba1-3287-8eeb-b132a873e1e8 | -10.4147 | -47.2846 | 2026-10-08 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 7010cb98-5fb9-3791-9f69-aa5eaa8d7d28 | -11.6365 | -43.7113 | 2026-10-08 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 2a1e734f-6680-3c4e-8ab1-37b91b698782 | -11.2291 | -46.263 | 2026-10-08 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 48f0d664-6c8f-313f-9bd7-d0d8f2d31883 | -14.2092 | -41.8318 | 2026-10-08 11:50:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 9a5f466f-45cf-3e0f-acc4-829c1bf506a0 | -11.3176 | -46.6798 | 2026-10-08 11:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 7d9c907d-4a36-3929-9578-8a3a86b7754f | -11.6369 | -43.6876 | 2026-10-08 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 9fdddb57-cc2e-33ac-add7-b95ac1fc73f3 | -11.2482 | -46.2604 | 2026-10-08 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 6fe26d14-0eb2-30c3-8304-c5f9f4582504 | -9.9398 | -43.5542 | 2026-10-08 12:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| af154eec-8ffc-3b29-9264-f566eb8ead1e | -10.9766 | -45.3865 | 2026-10-08 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 8d44d9dd-0c25-3a28-bde6-7b6aacd2fa07 | -11.2482 | -46.2604 | 2026-10-08 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| ac0df41f-bb63-31c9-b189-d165a12a1452 | -11.6186 | -43.6433 | 2026-10-08 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| cea25d9d-cc23-357f-9e80-07548d9ff5b6 | -11.8485 | -48.0373 | 2026-10-08 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 5f0e8c70-4998-3a3e-95da-0b6bfb316fb7 | -11.6369 | -43.6876 | 2026-10-08 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| cda5a393-72a1-30fb-8b78-db4f058ada3c | -11.6365 | -43.7113 | 2026-10-08 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 9720da34-6017-313c-a500-86ef59d81688 | -8.6107 | -67.0301 | 2026-10-08 12:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9aca54ef-fd8a-3633-bb6e-43442f003c58 | -11.3176 | -46.6798 | 2026-10-08 12:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5b3afabd-4d7f-37a2-bd1e-24778896a685 | -11.8485 | -48.0373 | 2026-10-08 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 3829f1b5-7c22-325e-ab4a-660539a00a8e | -9.1543 | -49.8142 | 2026-10-08 12:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 764ad3f1-ef39-33f5-98e0-e0d60ad55f0c | -10.4337 | -47.2824 | 2026-10-08 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 3493000a-69a7-3142-aeb3-2500007a2d1d | -9.9014 | -44.8147 | 2026-10-08 12:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e13acab0-9378-3875-88a6-a2184f150fe5 | -8.6291 | -67.0296 | 2026-10-08 12:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| da0bdf6b-2517-312a-ad9b-6c984d1d3026 | -9.9589 | -43.5516 | 2026-10-08 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 28260c59-801f-38eb-b575-0c0d294eb19d | -10.9766 | -45.3865 | 2026-10-08 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7c8737b9-a5ce-3a1b-92cf-42ed0e611a9b | -11.6186 | -43.6433 | 2026-10-08 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 48c65924-5025-302b-aa7c-3b7fa9526438 | -9.9398 | -43.5542 | 2026-10-08 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 896d0e08-a356-3036-ad84-e888273e82c9 | -11.6369 | -43.6876 | 2026-10-08 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| f2cb1cb6-9166-3ee1-8e82-abf9ca4074a8 | -11.6365 | -43.7113 | 2026-10-08 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| cc80165e-1476-3951-b4fc-bd2a29796f56 | -8.6107 | -67.0301 | 2026-10-08 12:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 527ef54f-8640-3db5-9e33-86574d7d86c8 | 1.74065 | -55.59069 | 2026-10-08 12:17:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| a82a5ced-3aab-3d2e-b01a-6a8887908e7e | 1.62724 | -55.77311 | 2026-10-08 12:17:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b5ad6b96-b9e6-357a-871a-498bf67fc1e6 | 1.34259 | -50.82789 | 2026-10-08 12:17:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0715d857-1686-33a9-b36b-05e31f78d61a | 1.6599 | -55.79905 | 2026-10-08 12:17:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 83232c00-a5ba-3b87-a8a2-92de7372a52f | 3.23535 | -51.3035 | 2026-10-08 12:17:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 06e6e332-37cf-348a-86e5-de599bf0ae3a | 1.76971 | -55.5415 | 2026-10-08 12:17:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0c97af7d-762a-3898-8596-826ac6cb4d05 | 1.74824 | -55.5806 | 2026-10-08 12:17:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5d13c053-9921-3aad-b7d3-13e9c16b2949 | 1.69156 | -55.6401 | 2026-10-08 12:17:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fbff035e-bceb-348f-a7c8-569fffe766a2 | 1.73939 | -55.58182 | 2026-10-08 12:17:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 16b16440-aa4b-3608-941b-3b943aa0cfe6 | 3.51535 | -51.25644 | 2026-10-08 12:17:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 529d5ae9-82c2-3df4-bc1d-2bb681d2d7fa | 3.54837 | -51.27484 | 2026-10-08 12:17:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8a3ebd55-0ffd-31eb-90c0-b32de0267b8d | 1.66117 | -55.80802 | 2026-10-08 12:17:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b4152e3b-e270-33ef-93f7-8ec747b6ff11 | 3.55001 | -51.28612 | 2026-10-08 12:17:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 56beec7a-dfce-384f-96b4-aa628381119e | 3.74282 | -51.61611 | 2026-10-08 12:17:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8566efac-4f34-3f1c-a072-a2a00985579b | 4.27105 | -60.0354 | 2026-10-08 12:17:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2d5503e4-43f1-3504-93e6-793f6bf703cb | 1.77855 | -55.54029 | 2026-10-08 12:17:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7994035d-b0dd-3865-af6e-6fda4fc1aa8e | 1.6966 | -55.61225 | 2026-10-08 12:17:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e5767ec8-5302-3a1d-b418-26885c971154 | -5.95506 | -55.3448 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| bbe2b44b-a688-3301-be76-91823d377005 | -6.0472 | -53.21724 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 21659b93-42b9-303e-b29a-a9edfc23cf5c | -3.05252 | -53.94653 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d1fa6749-35a8-3be0-9548-3794973c096e | -3.09065 | -53.94189 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| db6b6a36-be71-3a4a-a80e-6bfe2f61be3f | -3.96246 | -56.12568 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 326e71a2-6c6f-3ee6-819b-feb55f1fadf5 | -3.18026 | -54.61411 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b2bc8971-ea8b-3db5-87b1-b54a35c9da17 | -4.26871 | -54.87508 | 2026-10-08 12:19:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d26d392c-56f1-3f9f-bf79-b775abcdda70 | -3.58494 | -54.68506 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 95d9da68-e86c-34a6-9594-42a150a0d5b8 | -3.0893 | -53.95148 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 9f56afe5-0aa8-3a52-ae23-fbe8a51470e6 | -5.81806 | -53.82911 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ad9b8678-268c-3609-a755-5f151e38b68f | -3.04397 | -54.27311 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 804a1ed4-1b8d-35f6-8de5-6bd8861993df | -3.58556 | -55.59629 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| be313cdb-c878-34f8-be8e-0ebf74776602 | -4.57101 | -54.96009 | 2026-10-08 12:19:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f1534329-b1e1-3564-a731-38e86658f294 | -3.31595 | -54.04044 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 70b5db1a-cc8f-3757-854d-7c4ca3063916 | -4.77588 | -55.72522 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6d00f340-2889-3f0c-b291-20346ed92180 | -6.09496 | -55.72374 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e451aa2a-7511-345e-906b-a0ffdebbc27b | -2.3922 | -56.13266 | 2026-10-08 12:19:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b39726a3-c305-3a28-ac75-562ff4e390b2 | -3.56523 | -59.47898 | 2026-10-08 12:19:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 4c853065-2c64-3ee7-8bf6-3d9c4fa51c7a | -2.94419 | -54.06197 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README206.md)
