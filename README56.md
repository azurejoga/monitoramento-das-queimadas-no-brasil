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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bd898e4-93dd-3c12-918e-88e7d989fd4c | -20.52713 | -46.4798 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bc387ca-e613-3eae-a0c3-edefe6bbc586 | -12.93217 | -48.03638 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a46997a-2e9c-3311-9b4f-b90345b6b3b2 | -13.76518 | -52.76707 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8bc7a8a5-d5f3-3aba-b820-8fd8dc116c8e | -19.88877 | -41.42815 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d9cde469-c4a2-3a8e-b2fb-776fb8ec2562 | -18.03697 | -47.09372 | 2025-09-07 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 324746d4-80a1-3707-9949-c1089d538ac9 | -12.62061 | -56.99045 | 2025-09-07 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65936441-8bff-363c-91c6-0bb091ab10e4 | -19.47927 | -47.76784 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd51ff91-f2cf-3035-88e4-f3b3379f036f | -17.63231 | -44.79083 | 2025-09-07 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e60f3392-86d2-38f7-b8e3-8ea20e0b65ec | -13.85846 | -46.24822 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8780c981-ed3b-36c7-bad7-e5883ed6e8b0 | -17.68606 | -43.55104 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf251770-1d5d-3161-809e-c454b3305d2c | -15.10232 | -50.10257 | 2025-09-07 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cdefda1-b6a6-39d1-a87d-4becc2365f3b | -14.54148 | -53.15256 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53d92129-b9c8-3f66-b7a5-01d86c794cb3 | -19.47812 | -47.77515 | 2025-09-07 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 983e4039-7cf8-3e1a-b1d5-2422e9709cb0 | -13.82921 | -46.2616 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 790519df-abeb-3b0e-bc7f-894548aab378 | -13.04013 | -48.0621 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 815769c0-0991-3495-80e9-6357e8689fe2 | -14.58816 | -48.09934 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dbfa312-8aa1-31e2-b424-0c94cb0466b9 | -13.83363 | -46.25505 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c335efa0-8c48-3ae2-89d7-a7f67ca719a1 | -15.15257 | -48.17255 | 2025-09-07 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b3f73f9-c808-31bd-8624-16860627c28d | -12.93361 | -54.77 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 93aad5dd-4498-321d-99bc-7e228b82e426 | -13.36534 | -46.83205 | 2025-09-07 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f31521f1-32e9-368a-b704-aee1872daa70 | -12.60979 | -56.98386 | 2025-09-07 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bfb9ff6-6345-3a8d-a7c5-efa32db233d6 | -18.35774 | -43.92431 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a0a7983-cebc-3cc2-a588-9da2b4ab325b | -14.59392 | -48.08532 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed03493d-db8f-36ee-950a-edb52311ea03 | -14.58807 | -52.14315 | 2025-09-07 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f160ece-e694-3eb6-90d4-e5ecc80f3143 | -13.72702 | -46.90627 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1a0cdb3-855b-3189-ab2e-429470fc0e1c | -13.55246 | -48.10583 | 2025-09-07 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c6da48f-2d47-30eb-901a-6d05d622cba2 | -12.94972 | -54.79518 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed8bd142-a8ee-366e-9eff-40bdd7f19e9f | -14.59791 | -48.08216 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 23498932-b5de-3c9e-92f3-bd56d28696b2 | -21.20534 | -44.33203 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d1f7fdaf-7b50-3012-87e5-1f039208b309 | -13.29148 | -51.74891 | 2025-09-07 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccfab285-ea6b-34d1-8fe5-96bab97158a3 | -14.45228 | -48.4577 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0755eccd-00b0-3359-a171-870b945ba46b | -18.00712 | -43.48466 | 2025-09-07 04:21:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51c99033-2d47-3857-ad4a-6c3622726727 | -20.54576 | -46.44756 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b37f6b2a-cc85-3710-aa52-2d847cc3baad | -17.87578 | -44.3261 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc908cd2-a040-38e7-ab4c-e9fb944a6649 | -15.67591 | -43.23198 | 2025-09-07 04:21:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 56349196-ec32-39cb-8b9d-09b941c9f02d | -18.38366 | -43.89392 | 2025-09-07 04:21:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb7271bc-c15b-3257-a4d4-16134bf49ae3 | -13.30037 | -51.74657 | 2025-09-07 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e80a5a0-6ee9-383f-b537-6d252f66cbed | -13.06113 | -48.06229 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8c8489c-d7e4-3e24-a336-5b682814d2cf | -13.04478 | -48.05515 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4da2a752-6028-3a13-8cd9-8a6587b32d93 | -18.07209 | -47.98838 | 2025-09-07 04:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0329f587-100e-35e1-911b-98b9eaa9121e | -18.72928 | -49.629 | 2025-09-07 04:21:00 | NOAA-20 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bab8b7c3-76b2-3521-8587-4fec8a55509b | -12.95258 | -54.78009 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5e53ab82-375e-39e9-917a-94834274a796 | -15.12755 | -52.35583 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17d8eeb7-70a4-3cd2-b34b-cf9391b33d65 | -13.01013 | -54.82797 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e51967cc-ee75-3a1a-9fbe-e9ba1f04e702 | -15.37284 | -46.41953 | 2025-09-07 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e21de69c-5f23-3ad8-80cb-0ea6ff7a61af | -16.82279 | -49.18795 | 2025-09-07 04:21:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80d7aa7b-3931-3024-996a-e8f8f4c941f3 | -13.28681 | -51.77519 | 2025-09-07 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0210149-f4cd-335a-b624-ac57d6693a8b | -13.71215 | -46.8928 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 965ebe3e-e204-33b0-9867-63984d2edbc3 | -20.07443 | -43.74901 | 2025-09-07 04:21:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d358b28a-5b8a-39d0-905a-61a3c97e28de | -15.83356 | -52.27265 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d62cd85d-2a39-3282-bdcf-d2fc3121c3e5 | -12.92877 | -48.03576 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e78474b3-1ba2-300b-91f4-55a4c6798606 | -15.83548 | -52.28546 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fada4052-df64-3e43-b6b6-ff568ed4d766 | -13.91318 | -48.02371 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 171fd769-f37e-3942-b019-8830ddd27805 | -12.92856 | -54.76909 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 5c509357-0a13-3fec-816b-cebec94c9517 | -15.7076 | -53.5612 | 2025-09-07 04:21:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f36071f-c9d9-3663-8f5e-cf2b70ea9e61 | -13.27822 | -46.39606 | 2025-09-07 04:21:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71a2fb89-b379-3bc4-849e-5d8b91db0688 | -12.63395 | -56.98434 | 2025-09-07 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b60043f0-1a74-303e-a990-531c678b37d1 | -15.84173 | -52.27394 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54a912e4-7df5-3f06-89a3-e225a3c794b4 | -14.6579 | -46.82023 | 2025-09-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2c6af15-682c-3aa0-b318-f43f5aac02b7 | -13.02433 | -48.05169 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe150f46-cb8b-3988-86a9-b53074d17509 | -19.47437 | -47.75572 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e0d132b4-00d0-3ace-b017-51ce45b17939 | -15.22092 | -52.34739 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe4a3225-5588-323f-88e3-0900b50ba796 | -15.00717 | -48.00691 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6f9dcb3-f474-3f4c-90fd-6f20b95e59df | -15.02034 | -45.45248 | 2025-09-07 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4531ea11-a235-3227-8a11-1447140dd605 | -13.83474 | -46.24797 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05f45a7f-e8ba-3b9e-8fb5-91319812ee17 | -13.71658 | -46.88637 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7ba22cf-bf33-3611-b905-668fee0748b8 | -14.4948 | -48.76913 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79e2c042-a374-37f4-b656-b5be60500611 | -13.90872 | -54.002 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a2e7789-8f76-3177-b81f-79f4bfa5d54f | -13.29797 | -49.57354 | 2025-09-07 04:21:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28921d57-db17-3907-aad7-394507136f32 | -13.29626 | -51.7458 | 2025-09-07 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3189d1a2-c4fd-3660-9d87-6b54eaa75323 | -17.67859 | -43.5503 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81565cd2-a75a-39df-85e2-c43a8dfbaf01 | -14.49394 | -48.75322 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3a3f173-644c-3f72-88ec-7b46fd5bb093 | -19.66689 | -44.88243 | 2025-09-07 04:21:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 16671be3-42a4-361e-866f-c7d5d81623ea | -17.22681 | -46.71691 | 2025-09-07 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dd8e067-09aa-387d-85d7-cc74d0cb8c49 | -13.91062 | -53.99208 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00f89fe8-fca5-38df-9e17-2a0859e8e47f | -20.35331 | -43.88116 | 2025-09-07 04:21:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 915f2f9d-22f3-3e5b-aabc-7d1941d3aede | -13.05711 | -48.06544 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f0a23a83-1b0e-3317-be4f-cd52011c78ef | -17.22017 | -46.71579 | 2025-09-07 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4135389f-a1c1-385e-8479-1fde95c58691 | -17.68352 | -43.51384 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 315b6ae1-65d8-350e-bf91-7618ca70eb70 | -13.93493 | -54.018 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89906288-2a88-342b-b8c2-b52e7957b3a9 | -14.68666 | -47.15059 | 2025-09-07 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9078b89-4128-315e-9fc5-258e06ffc4b9 | -14.21041 | -53.30396 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 45fc70b5-d83e-3f28-9b7e-c1db7d692383 | -14.97201 | -47.59636 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d3b810f-6f38-38dd-ae1b-c5179bd88702 | -14.97475 | -47.60056 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dcff594-e283-3afb-87bb-1a41275cb902 | -16.34656 | -52.94858 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d872b1c-6557-3e3e-b4ca-ac4ff4d37b4b | -14.74231 | -47.50233 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27205fe6-7cdd-36a7-a9d1-30321b90f2f9 | -15.67702 | -48.20813 | 2025-09-07 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd6fde73-890e-348a-b3d1-791705ecad81 | -13.04322 | -47.12265 | 2025-09-07 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f982b1d1-467b-366a-837a-02b643efce1e | -14.58104 | -48.07919 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86a06a88-3737-322a-80c9-97feb50bd27b | -18.02816 | -47.08471 | 2025-09-07 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd1bd6d0-468e-3193-bbe9-2cd333724f28 | -18.3547 | -43.91928 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2725533-9648-395a-bb72-eb2281e2be51 | -12.63975 | -56.98565 | 2025-09-07 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4d7e4f1-5898-3e7b-9c47-a41e9fe91f42 | -14.50235 | -48.76644 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a62fd557-2166-3de7-ab40-56c83accd0ca | -12.78104 | -52.95605 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 927f4963-1ea6-3340-b788-bb256cbdf5c2 | -12.77959 | -52.92515 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d287ade8-e86f-3dee-9f02-85148319f4b8 | -14.82891 | -48.17747 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7571fd7-2d87-3773-b23a-829212c7a703 | -18.01837 | -44.91082 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e7510b9-945f-325c-a05c-0fff21095b9d | -13.66835 | -46.95496 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4816feb0-8e2c-3cd5-b004-e0417cb542f4 | -18.03147 | -47.08527 | 2025-09-07 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00a77937-f265-3f1b-9d3a-954ee0c3112c | -14.44612 | -48.45256 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README57.md)
