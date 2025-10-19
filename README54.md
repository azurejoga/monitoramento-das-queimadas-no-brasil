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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee2c6aa9-2278-3c6d-abc0-d2a48c661ac1 | -16.77668 | -42.7652 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f5c58a4-8d6f-3737-9879-5a08d9d7716a | -15.90348 | -41.57338 | 2025-10-19 04:34:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 730a0c53-553a-3312-92f4-3d8634b4ac71 | -16.80936 | -41.00539 | 2025-10-19 04:34:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d0823de1-1531-3b0d-b0ed-e09462fa59ed | -15.79064 | -43.25455 | 2025-10-19 04:34:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65e2cecb-6713-3389-b751-8712200352ec | -15.52435 | -45.34424 | 2025-10-19 04:34:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 56c2e0bf-a969-3f6e-bd59-59af8bdfe50b | -13.61241 | -43.96018 | 2025-10-19 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd87e36-052f-319f-9956-1cbe6fa369a3 | -13.01626 | -46.94992 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecd23e4f-b5d0-3be0-8653-0405c77c086b | -16.14904 | -41.15718 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 082aced6-b584-3387-9e99-2e78cab33bb6 | -12.98824 | -47.28118 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e2d7e32-d90a-37ca-b310-df378edc2428 | -14.03147 | -47.0871 | 2025-10-19 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34f2cd1a-9b0b-3f14-b874-592c42149100 | -16.80902 | -41.00829 | 2025-10-19 04:34:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2cce7c47-dc67-36b3-8027-4ba474cb13e9 | -14.13088 | -46.97969 | 2025-10-19 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72819daa-618c-3110-8672-fda03c0241f9 | -22.30408 | -51.50806 | 2025-10-19 04:36:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5cab1f9b-80e3-30ba-b790-ed3e20f2f33b | -22.30077 | -51.50746 | 2025-10-19 04:36:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 09276fab-0f5c-3ef0-be71-effe20b9b0fc | -29.9525 | -51.61567 | 2025-10-19 04:38:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| fd101f8a-08ec-3421-bd1d-624d5786ee0b | -10.8891 | -46.0814 | 2025-10-19 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f5d42a8f-e08f-3017-958d-a214bd6f0e8b | -16.7834 | -42.7668 | 2025-10-19 04:40:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8173ef8d-9db0-3ee6-b329-fa3f7b91272f | -16.7635 | -42.7714 | 2025-10-19 04:40:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 144.3 |
| e56d9ccc-b02a-3d92-9fe0-6e42ea61e0ef | -12.4686 | -45.4232 | 2025-10-19 04:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ace53300-1b4a-3931-b220-0de6cb28c4d0 | -8.6032 | -40.1834 | 2025-10-19 04:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 66.6 |
| fc04461a-14b0-3d1e-8273-0ced9b1365f6 | -10.8891 | -46.0814 | 2025-10-19 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 42b8fbfd-ae39-3b09-9980-73170c8f9a64 | -8.2104 | -43.9479 | 2025-10-19 05:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 210dde4f-de26-30dc-bb6c-67add1d0ca81 | -0.35382 | -50.36743 | 2025-10-19 05:21:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0bc20f2-0467-308c-93a2-3f0f66688ed0 | 1.6712 | -55.9752 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fc1d510-847f-3d82-8d8a-a4b6381f8765 | 1.74544 | -55.94328 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de0193d8-7467-3fe3-9084-020728b71183 | 1.78932 | -56.01711 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d6cb8cc-e14c-32fb-8ed6-e0444609fc73 | 3.17005 | -60.28784 | 2025-10-19 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 758efeb7-912c-342a-b87f-151f214b72dd | 1.75292 | -55.92192 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ff47cc2-945e-3357-9b13-b40f7b163b86 | 1.78992 | -56.01416 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91042493-bfe7-3fc2-b4b9-58f6d427c444 | 1.7825 | -55.71802 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c56ff0a-3a19-3d8a-a20c-de9916191203 | 1.48419 | -56.05531 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4af6b9d0-360e-3b4d-9819-b43c6fdc0d97 | 1.75063 | -55.93035 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5404af8d-d986-34cc-b7d5-f1de517e6d80 | 1.80192 | -55.70257 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 519955ee-92fa-3b75-8e43-b0e4bb86a35d | 1.78314 | -55.72203 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d41abb5-c2b6-30eb-9821-7698cfe7e891 | 1.78472 | -56.0337 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e8389e-617e-3d8c-9fca-e1942bf2f4b9 | 1.78961 | -55.71692 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63a00aff-6ea1-3a35-adbd-8901ed07729a | 1.74378 | -55.95568 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35ebad37-d4eb-3650-b35a-0c8a3d94fb23 | -0.99143 | -47.07795 | 2025-10-19 05:21:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fa108fb-d134-3d46-9947-7db2a78c051e | 1.74254 | -55.94778 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad30bd45-082d-3aba-a26f-b5e2170530d5 | 1.72217 | -55.77145 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d99ed311-16b6-32ae-ab43-c2fa9aaf3a61 | 1.78898 | -55.71292 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20e47c5b-55cc-3c8a-a50f-3a5c3a713ff9 | 1.799 | -55.70718 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f431facd-eedf-3d57-9759-bd1781e5d8eb | -5.35042 | -47.20749 | 2025-10-19 05:21:00 | AQUA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| a2de783b-1bac-3d49-80bd-4df07fc00482 | -5.35531 | -47.21309 | 2025-10-19 05:21:00 | AQUA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 27fd5ce5-99a5-3463-883a-d4cce90960c6 | 1.77895 | -55.71858 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3daaf73-c814-300f-9792-0baef597729d | 1.78642 | -56.02153 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b241f86c-e725-36cc-bb4b-7c30e629326e | 1.79836 | -55.70313 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee3969b0-73b3-3446-90bc-29f80cd36016 | 1.79253 | -55.71236 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09d6209d-ea97-34bf-a086-1ca6f325e5d5 | 2.06024 | -55.72984 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad3dfb8f-402f-3c9e-86e5-d44a2f34e0c7 | 1.78766 | -56.02249 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1c70d15-656e-3cf4-bf42-28d6e52fabc2 | 2.05962 | -55.72586 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0cd69e9-2824-3bbb-9eac-b2aa824373e9 | 1.74026 | -55.95624 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc3d689a-0529-32d4-a9c6-bf8c32099155 | 1.6738 | -55.97411 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 373875f9-6973-3271-9bde-fc57f7835475 | 1.79652 | -55.92031 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d3f118c-e4b5-3ffa-a56c-4e7bfff0ba07 | 1.74316 | -55.95174 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13fcf2e8-edfe-383e-a952-945d759fb3b1 | 1.77539 | -55.71915 | 2025-10-19 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4c0189f-8565-3036-8b07-97ad3f36ada7 | -0.9914 | -47.07958 | 2025-10-19 05:21:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1a0922a-464f-35f6-ba08-f7301a47d14d | 1.73798 | -55.96468 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fbd337b-5728-3ea6-9b06-4f5a93a81448 | 1.78704 | -56.01862 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d017c08-6664-3d8c-9717-da3dc5b7f4c3 | 1.78762 | -56.02925 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b82a5703-41f3-35e8-b988-e89266affd4b | 1.7386 | -55.96862 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2463bb6-f019-3b9c-854a-07c116e758c0 | -4.83756 | -42.74216 | 2025-10-19 05:21:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 9e54fb55-de63-3b11-ae55-dc93b6864a7e | 1.74711 | -55.93091 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91c17c92-c82a-3f7f-8dee-a4cd922ec508 | -0.39748 | -51.94957 | 2025-10-19 05:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f975046-bd02-388a-a0b4-7487ef3c5398 | -0.43332 | -51.9649 | 2025-10-19 05:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cf1aac3-c5bf-3d47-a1a6-36c94ba8c796 | 1.75001 | -55.92641 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bad512d4-3a3b-36fa-a931-d396eb1dbe25 | 1.74088 | -55.96018 | 2025-10-19 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc717131-6e76-346c-80b3-2189920b0c0c | -4.82554 | -42.74018 | 2025-10-19 05:21:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 23602661-4c5f-3834-abdf-1127225ec453 | -9.11765 | -65.362 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 151f4231-e129-367a-a2ca-903ac87cd89d | -3.3969 | -54.06003 | 2025-10-19 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60589b87-2bb6-36de-bafe-907fc6f2c15d | -12.45009 | -45.44066 | 2025-10-19 05:23:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| cd8790a1-2071-33ba-9b5f-8419175546fb | -12.45364 | -45.42014 | 2025-10-19 05:23:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0ed51ede-25b5-3307-8245-456531095544 | -10.01617 | -65.05918 | 2025-10-19 05:23:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e911576-c1fe-3690-9b03-a5d78b6cf7ac | -2.86843 | -50.74078 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3de3d7bb-f43c-3420-a5eb-9fd6e7164400 | -2.64864 | -49.52405 | 2025-10-19 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd37405e-a36f-301d-8882-d3a8c6dbb347 | -8.71974 | -67.0537 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3c7e176-684f-3b6a-ac7a-9d7587833231 | -6.52524 | -60.03193 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bca608c-74fc-3287-b52e-e2efbba2ad67 | -11.37934 | -61.21526 | 2025-10-19 05:23:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd109d5e-3fc8-36ca-8ed4-10f5d922ba31 | -4.30559 | -49.66335 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af56f687-a04a-3c00-b2e3-ee4d9012726c | -2.87467 | -50.73506 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a06a0c0-2448-3ed7-96c1-c5b9aace4056 | -9.55943 | -66.64288 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c5fbe87-3a82-30f0-b025-e2318eadab8b | -2.69476 | -49.54139 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fdcb9660-9b8c-33e3-ba76-b56b782a9c51 | -5.36065 | -47.21587 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5f968d22-f381-325a-813f-46a1ead7bfbd | -2.51922 | -51.93002 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b45d416-5f30-3370-94a8-d1006a30f2ff | -7.01049 | -59.62197 | 2025-10-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7060e0ae-b9fc-34fb-922f-152e44606c82 | -10.18279 | -62.92962 | 2025-10-19 05:23:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38bf2436-32d8-3ca6-8ab1-53dcf99044d5 | -9.64548 | -67.48966 | 2025-10-19 05:23:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b53f51a0-b2bb-39a3-9047-ae13739f6a8d | -9.73945 | -65.88779 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0b5e165-8737-399e-aa73-b344c60127e4 | -7.17943 | -39.66807 | 2025-10-19 05:23:00 | AQUA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 52a4c57a-fbb3-35d3-b713-89d0229df9d1 | -9.91588 | -64.08868 | 2025-10-19 05:23:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c4fda95-e5dd-3a5a-924f-a2a8c31ec7e8 | -3.09183 | -49.22422 | 2025-10-19 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e9ab2cd1-786d-39ed-96ea-c83283167257 | -8.94498 | -65.93282 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ddb2007-b2d2-3e2d-b5b5-13a9eae647d2 | -4.48756 | -50.56152 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abdaf322-ca87-3019-bded-6ee34ff8bce6 | -9.55533 | -66.64217 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f470af7-adf8-3c03-a3d5-2ac45aa20ac5 | -3.53046 | -55.47248 | 2025-10-19 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16ab52d7-14a1-3c80-8de4-e5f694861d98 | -4.22303 | -50.62798 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 499f6570-c45a-3fe7-9030-21d08d6aa0f2 | -2.87038 | -50.72768 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61139c48-3427-37ee-a0b2-5d65834a84e0 | -6.91534 | -55.45464 | 2025-10-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fcf05dd-adb1-3ef1-8a85-cfd5b306f1bb | -2.25689 | -51.91834 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e039c616-ed27-3684-bca0-de3e75ff6fd0 | -9.74243 | -66.33502 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README55.md)
