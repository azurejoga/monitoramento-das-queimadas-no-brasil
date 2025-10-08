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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a701da01-bd30-3493-b90d-a6654618b593 | -16.33062 | -47.07696 | 2025-10-08 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 730f3f71-033b-3b4c-9324-d4c2563718b7 | -15.26156 | -46.33511 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efbaf0c7-0991-34ed-be48-36945e1d75a7 | -11.11113 | -54.04491 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 390a76a7-0e59-3730-910d-6379055972e4 | -18.40866 | -45.21469 | 2025-10-08 04:40:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 6b993266-d384-3e73-9516-b45585e9f185 | -18.65102 | -43.90799 | 2025-10-08 04:40:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 308437ba-8703-3b9b-b9af-e4a5fb366d3e | -13.39756 | -46.70442 | 2025-10-08 04:40:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7241fe5d-55c9-33e8-9dba-b5de6be97c98 | -15.99783 | -50.82488 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83511304-a11d-37b5-b1ac-1e44886828de | -14.77118 | -46.01065 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ceb6e353-730c-3127-b61c-e41b4e3d2655 | -12.31801 | -55.10971 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35d5df60-d669-3143-b1d4-b2b108e4ac73 | -18.04934 | -44.44819 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43410598-6efe-3fd1-92ce-5cd7439417a8 | -16.33336 | -47.05685 | 2025-10-08 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68d87ebf-22b3-30da-a2b9-0172b66708d8 | -12.99061 | -46.77565 | 2025-10-08 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2f660c02-f2d9-368f-b4ac-09a5c56ff969 | -11.14085 | -54.8774 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d72e52f-b3f6-3d28-b3f5-b1d56876a063 | -12.32829 | -55.14196 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1e89a67-ceef-31f6-b972-17c3d7362963 | -15.38489 | -48.0053 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec0ca137-d93d-3d8e-a63f-fc31b5e79f62 | -11.69872 | -50.95493 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 971e6b9b-abe8-39ca-b360-57c9192ca305 | -16.71787 | -47.5963 | 2025-10-08 04:40:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dae75bff-c0c6-377c-9252-d7e3152f3c2d | -13.7336 | -45.71704 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d85e9c9-df39-34d6-8053-b9aecb143516 | -13.00128 | -46.7819 | 2025-10-08 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f8b533ab-0653-3490-97c3-f1dcb28ab90b | -12.52151 | -54.72507 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4112f8e-c355-3e0b-9390-f8f3638f0916 | -18.11878 | -53.35521 | 2025-10-08 04:40:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b170a0a-10c3-3c35-bb85-b36374988b25 | -14.52444 | -46.64145 | 2025-10-08 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7d3e1ac-0f4a-3fbf-ab0d-1b04cbc03698 | -17.14937 | -43.44015 | 2025-10-08 04:40:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85e1747d-d780-35be-91ac-0eaad35c7a7b | -15.38821 | -47.31354 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1b5f74c-ab0d-3b92-a26a-ced86d90658c | -16.18177 | -51.75263 | 2025-10-08 04:40:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32f32fce-fb09-3b34-bec1-a140dd2a1e9a | -19.71698 | -43.91151 | 2025-10-08 04:40:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1209c815-1791-3063-abbd-02aaaae57c55 | -11.5139 | -51.49253 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa6ef956-e36e-3056-8cda-8f25bc371bee | -15.63569 | -52.57215 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15b1a9f5-3fc4-3879-ba5e-da082b1d5acf | -13.06653 | -47.83652 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 195c0dd1-d011-37ae-a86f-5eef987edd8b | -14.91218 | -46.81785 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dfe557a-7a58-31b3-a36d-7fff61158491 | -16.28964 | -45.24681 | 2025-10-08 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 023716f3-2f41-3e95-be76-90c07c6fdf1b | -12.29871 | -55.10624 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5558af60-aca1-3af7-b54a-1add26ef2ed1 | -12.25386 | -47.86581 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf2f0754-5cb6-3502-9ff1-1290f0de52bc | -15.15896 | -52.7637 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1e1d1e5-0d71-326b-9cbe-f745bf723625 | -18.40133 | -45.19999 | 2025-10-08 04:40:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dc6fbc3-33b3-355a-bca7-446a3df759ee | -13.3283 | -48.02076 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09b904d5-d745-37c3-b307-11f5fd27bb7f | -11.13206 | -54.88765 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2108320b-712e-3110-aacd-5d05c139beb3 | -13.2253 | -47.17946 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bfd944e-f9a9-3826-8286-b4827ee60b3c | -11.99597 | -46.77064 | 2025-10-08 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8ea8cb8a-3f96-3d8f-84b6-35ab0ba4e2ec | -19.4702 | -43.89657 | 2025-10-08 04:40:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0043e51-022b-3360-a801-2cab7b5b3c1c | -15.63472 | -52.55696 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 476e6a93-21b7-314a-9306-fc985fb42bd4 | -11.15188 | -54.86581 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1148a3f9-a3ee-3fe3-b9c5-cfc339e8bed3 | -13.06712 | -47.83251 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51dc2e9a-9eee-35d3-8c81-6309bed6589c | -12.39067 | -51.13313 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bc76d1d-3772-3ded-9ce2-3486ce8e6666 | -12.45241 | -54.71946 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc210aef-addc-3bb8-abb3-4431ec0f6387 | -13.22402 | -47.18827 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 00a2bb36-641d-39d1-b39e-5c45b72599be | -11.14543 | -54.8798 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53d4fe30-a41f-3997-aca5-0d6d90b76bf1 | -11.13508 | -54.89323 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4107dd2e-4d41-3131-9116-12e9fa967a61 | -13.80846 | -45.80519 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c612d970-1ee8-33cf-ab44-7618b26eae7f | -11.7363 | -50.95387 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfa7ea55-3052-348a-ac5b-0237092c2026 | -12.41545 | -45.62418 | 2025-10-08 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0cf5b00a-0a43-3f6b-9b7c-05bd0ca995e4 | -11.17815 | -54.87534 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 93c849fa-45ee-3313-af03-d2ef00ff1071 | -15.19356 | -43.73604 | 2025-10-08 04:40:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 190755db-a625-3d8f-a729-03fbd19ec1aa | -11.29259 | -54.88816 | 2025-10-08 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a56f75c-b511-3f4a-9b86-93b9ec095b33 | -12.98262 | -47.94409 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3030b087-1d8e-352f-afbb-22543a907b7f | -12.29485 | -55.10555 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8424ce7e-0937-3f74-a013-7c6e3a8b3ea0 | -15.37497 | -47.32288 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 14d6f215-6937-3981-bb77-7a71c5efc721 | -19.71204 | -43.91057 | 2025-10-08 04:40:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f561cea6-9a78-3760-96ad-7e45fa0d21db | -17.56273 | -46.06812 | 2025-10-08 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8629718e-817f-3406-b81b-1a5396f995e7 | -12.77907 | -50.5029 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19296c55-f07a-39e5-bc40-6238a915544b | -11.42453 | -56.2919 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07c25ff2-be81-388a-8a27-eb7b677fdb68 | -13.29007 | -48.03729 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 64a0f22a-9144-3c94-bb79-456cfa2a82d2 | -12.91591 | -46.83917 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30391bfe-4460-3cf0-a718-c8509591954f | -15.99266 | -50.96812 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1192a9cd-0bef-3ee0-bac0-e72718262a5a | -12.49638 | -54.41583 | 2025-10-08 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8dad7af-4afe-36df-a87a-76b2abbcc220 | -15.06396 | -49.48671 | 2025-10-08 04:40:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67e40ba3-bacf-3e82-aa6d-e26fcb5ca0cf | -11.11928 | -54.04174 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c82e3ca1-675c-3275-be47-8182fb8dd843 | -11.72142 | -50.94058 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| b1f1c29b-11d5-3f19-bdbb-d6d989718bc5 | -14.44022 | -48.7865 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25a8bdf4-a420-3776-bf56-bdacc5ada18a | -18.02578 | -44.31345 | 2025-10-08 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db48922c-cfd0-3886-92f7-98432647b3ea | -11.16008 | -54.88742 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c2e07970-fa8b-3a38-9b3f-90575fbb2eae | -16.13476 | -48.2424 | 2025-10-08 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aaf16f3a-91db-3dca-bd19-6259685190f8 | -11.71524 | -50.97933 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af4137c6-b329-312a-b287-4023edacfd20 | -11.38582 | -54.34694 | 2025-10-08 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4a5f1fa6-e1cb-3c5c-88dd-ccdcaa6ac3e4 | -17.27444 | -58.1166 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 76bf0e1b-409f-3f8f-ac66-ac27a95775a4 | -12.44743 | -50.17081 | 2025-10-08 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b70b1f4-3b8d-31ea-be6b-3d549e22c902 | -11.16482 | -54.88316 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e4e14d62-e53e-3665-aa99-be245f8a86c3 | -11.1562 | -54.88675 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20b5cf98-1528-301c-b990-38465a6a3556 | -15.61321 | -52.58341 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0edd9666-36d6-3270-b662-9cb77697e77f | -11.74467 | -50.92272 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8c7aa14f-1414-3d60-aacf-86d2e9097d2a | -12.443 | -50.17735 | 2025-10-08 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6b5a0a7-0c53-3e61-aa05-d1cc30c47fea | -11.13835 | -54.89216 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ccbe740-58cc-38e6-819d-738a908b9d28 | -11.38208 | -54.34626 | 2025-10-08 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a3072f2-131f-3974-959b-7734349a034d | -15.24132 | -46.36431 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1cd8d5d0-48d2-322b-820f-c1831c6e7128 | -14.62413 | -52.47601 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83ca3b47-5f90-3085-8fbc-499c3e356af5 | -15.36329 | -47.2968 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43c9754d-8df8-3abb-a646-58aec5208735 | -12.74113 | -44.71894 | 2025-10-08 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12f8fdf9-5fa3-33bb-9a94-94d40acc3645 | -18.00736 | -44.30662 | 2025-10-08 04:40:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d334cb44-6f9e-3f7c-a0ce-4e6074580df8 | -11.9916 | -46.77463 | 2025-10-08 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c6dd09e-0cee-3c83-96eb-5613a3ba7eb9 | -12.43536 | -54.22382 | 2025-10-08 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05b1c2e0-bba3-3189-8588-57751f1b7ad5 | -15.6284 | -52.57468 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23f09f1e-f4b2-3939-b34a-41d9267cb4bc | -18.49676 | -42.90251 | 2025-10-08 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 339316b9-f280-385c-b7c3-eba2d2573aeb | -11.17343 | -54.87957 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d7bd4198-2321-3dbb-bd2b-0f5b3065ce06 | -16.71411 | -47.59567 | 2025-10-08 04:40:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 829401fa-cb4d-3337-948a-4a20109ecea3 | -13.28784 | -47.15552 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2efeafa9-48e6-3c42-ab7d-8937d852524a | -13.32091 | -48.02507 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3433d277-9ac1-309f-8887-529a1dce5ca8 | -14.72186 | -46.0401 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34f8cfb3-9b56-370d-b946-c57f30485b33 | -12.93137 | -46.86496 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c1e3c73-f221-3749-a159-803f2da0e080 | -13.01985 | -47.90761 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 114698a2-e093-308f-9a95-e0f632c050c5 | -13.06697 | -47.88359 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README80.md)
