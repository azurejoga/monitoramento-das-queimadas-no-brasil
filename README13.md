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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2f5d807-366d-3c7f-b88f-d22c494a06ec | -10.83912 | -56.95503 | 2025-11-21 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a32740a7-8bc3-3222-8029-e6c80083da79 | -10.84289 | -56.95981 | 2025-11-21 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e7b80cbd-7b6b-3edf-a18b-158ad1b95bd7 | -11.51162 | -58.45289 | 2025-11-21 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36d16766-b9bf-3655-b215-95863b2e6687 | -8.9612 | -63.66485 | 2025-11-21 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bea08d78-a49d-3138-81ef-f6532428b0ad | -8.85279 | -62.94407 | 2025-11-21 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5daa143-b419-3029-9170-3177b474eae6 | -11.67104 | -62.61777 | 2025-11-21 05:33:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc731178-84b4-3e92-b18f-704475c67560 | -12.87466 | -54.7435 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e469c38a-6a1f-3b98-b54a-46b8c49124a9 | -9.63903 | -67.48063 | 2025-11-21 05:33:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60e18649-54a7-3b4e-ad91-f8a3f9521dbb | -9.02925 | -63.6573 | 2025-11-21 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86a79c01-dd1c-3999-a187-751fe062d3fc | -12.5539 | -54.80453 | 2025-11-21 05:33:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b519b60-6a63-383f-9a6c-96cf5f27c43b | -8.86814 | -63.67547 | 2025-11-21 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1046a685-841c-3929-8267-d4c385385115 | -12.86907 | -54.7459 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fa12073-0801-340d-bb93-79d52d40bcd8 | -9.78227 | -62.76035 | 2025-11-21 05:33:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89e1f755-67c6-319e-a213-b2954e0f8290 | -9.63817 | -67.48568 | 2025-11-21 05:33:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63bed188-ab97-332c-9686-f298d25859a7 | -10.84347 | -56.95566 | 2025-11-21 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8dcc056-5c77-3746-a674-bb7afd11dcfe | -12.54012 | -62.02107 | 2025-11-21 05:33:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d162fff5-2b73-3ad3-a8f9-5cb1a3d952e1 | -8.86164 | -62.95265 | 2025-11-21 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 905770fa-6eab-33bd-a451-52a77061ec5e | -12.88838 | -54.76142 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee10aeea-a7dc-372b-ab10-403a2cc9d724 | -9.63425 | -67.48499 | 2025-11-21 05:33:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5b38b3e-ffa9-3d24-a3bf-60c3ad04f9b7 | -12.8699 | -54.74007 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14845ad9-7336-32d3-b8cb-132b385a1716 | -9.00897 | -62.72635 | 2025-11-21 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b38d071f-6879-3f39-844f-b64e691220c0 | -11.96072 | -62.84206 | 2025-11-21 05:33:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed2bc65a-c34b-3482-aed9-ced2954462c3 | -12.86945 | -54.74275 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7f72425-eaac-3cb0-b60b-23c0b075e2c3 | -12.86869 | -54.74907 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 065f026a-ae6b-30e5-b85d-2151c5d3cf00 | -12.8687 | -54.74951 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8dfdb76-a2b5-3653-a7d6-2195033cf02e | -10.32701 | -63.69363 | 2025-11-21 05:33:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66a2555f-d416-3240-bc4a-7a3df23bfb91 | -9.60731 | -65.2458 | 2025-11-21 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de64d586-b01a-32bc-aeb7-1a8a7e680657 | -9.94384 | -67.24573 | 2025-11-21 05:33:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d79a5be0-1291-3bc5-9685-f343b8bd5e11 | -12.87512 | -54.7408 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f556bb0-4e01-3ced-822d-ce8163bc1ea2 | -9.73237 | -63.64746 | 2025-11-21 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64eb2cd2-33fa-3c7c-82b1-7e7ec631e8a2 | -11.95406 | -62.84098 | 2025-11-21 05:33:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 762289e4-d1dd-3a00-b12f-87ccc3bfb602 | -12.54721 | -54.80359 | 2025-11-21 05:33:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 150fe9c0-4459-3f5f-ac32-981194bda297 | -9.98945 | -65.18736 | 2025-11-21 05:33:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b68a85cf-d2e0-300a-90b7-76c886c1c44f | -9.99704 | -65.18463 | 2025-11-21 05:33:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3afc3ccc-1484-3c2c-be81-9f29f72def1c | -11.51357 | -58.45013 | 2025-11-21 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42e595a8-82a1-3b6e-8dbb-e2398e21a959 | -10.32644 | -63.69717 | 2025-11-21 05:33:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f84affe-0c51-39d5-b86a-71e6e0e59b3d | -12.87552 | -54.73764 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 912df7ff-a505-3d0f-8aa2-0efade30b535 | -12.8739 | -54.75026 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 598157d3-b086-3d10-ba7b-8a63cfa8b3d1 | -12.87542 | -54.73718 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1290c434-8fac-397f-b6b3-7ef0f71bbc65 | -12.20173 | -63.44234 | 2025-11-21 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c6d9242-dedc-3ea0-a8a4-ecb844fa2aae | -9.38305 | -67.83511 | 2025-11-21 05:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3136fccb-5184-3d21-be67-c6664fb60ca0 | -9.60799 | -65.2448 | 2025-11-21 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2045a0f2-972b-3c63-b546-85579a3450a2 | -12.54872 | -54.8039 | 2025-11-21 05:33:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff6425b4-2691-3cca-a579-7bb78ba0ced5 | -10.84783 | -56.95628 | 2025-11-21 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b0ec0193-e5ab-3ffb-a138-34927ec0bc7a | -8.85334 | -62.94057 | 2025-11-21 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bff2243-233e-34d3-9e00-24cc3c671d43 | -12.54762 | -54.80046 | 2025-11-21 05:33:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0ee69b8-23a6-30a5-8f13-2f6c286297c9 | -10.84725 | -56.9604 | 2025-11-21 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8493f68d-42e8-3528-a6d5-5b5f94ae65d0 | -12.87389 | -54.74984 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e915fea2-551e-39b6-b8da-e0f6d68faf1d | -12.8691 | -54.74634 | 2025-11-21 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 427fed6a-c1a3-304b-b1c3-d24deb80c5f2 | -8.86497 | -62.95319 | 2025-11-21 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f97e286c-ff98-33a5-bf37-cd39a6c723c0 | -18.11107 | -54.52459 | 2025-11-21 05:35:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 57cf2a14-e482-3c53-b9bf-d1243b3d4a56 | -18.10621 | -54.51604 | 2025-11-21 05:35:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e5d5d35-5dd3-3a71-ab19-854ec5fec1e3 | -14.96076 | -58.8837 | 2025-11-21 05:35:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6f591b1-cccd-347e-a1d7-b181263d9a83 | -14.41173 | -56.86568 | 2025-11-21 05:35:00 | NPP-375D | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a9d7c65-9605-310f-ad70-8cbd0b7d9ff9 | -15.48207 | -58.71583 | 2025-11-21 05:35:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 434321aa-b9c8-3db9-a5c7-a2705435cb37 | -18.11147 | -54.52074 | 2025-11-21 05:35:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a319339-8a44-3b43-9ecf-c2ba7bb76615 | -17.61681 | -54.19522 | 2025-11-21 05:35:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b80aa67b-a22a-364c-9742-da23e2fd04bd | -16.26477 | -60.14869 | 2025-11-21 05:35:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc4d218a-741f-3edd-986d-23fbf574bbd6 | -18.10541 | -54.52388 | 2025-11-21 05:35:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f35f99ba-672a-32fe-8933-fa5ccee536ae | -15.52869 | -58.83916 | 2025-11-21 05:35:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca41f0b3-9dd5-3a31-9266-604c1ceccb3c | -18.10581 | -54.51998 | 2025-11-21 05:35:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8652054e-92a2-3d1f-8972-80a006935ad2 | -15.50302 | -58.84317 | 2025-11-21 05:35:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2bc3dad-c0cd-3221-acee-f54eb3ef02ec | -14.57257 | -59.70565 | 2025-11-21 05:35:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7204be2-01be-373e-af6e-72e15c9d87bc | -17.61763 | -54.18726 | 2025-11-21 05:35:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c85abab-86cd-321d-8a55-ecb520064e8a | -15.30597 | -53.00178 | 2025-11-21 05:35:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a2b2017d-aee9-3db2-a28a-8d4a74379851 | -15.31199 | -53.00262 | 2025-11-21 05:35:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0a99fff8-309f-3f55-8f69-1fd578505c20 | -17.62294 | -54.19225 | 2025-11-21 05:35:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 368b1b42-1567-3d45-ad9d-0344606ab073 | -12.76551 | -61.4546 | 2025-11-21 05:35:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a693bd7f-47e7-3370-bb78-7d6ba42a9a8e | -19.4992 | -55.35081 | 2025-11-21 05:35:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f4938256-5b27-3242-a470-1c5de0d2716f | -17.62253 | -54.19622 | 2025-11-21 05:35:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9bf1dd87-032a-35de-ab52-d8b5ad838068 | -18.10016 | -54.51917 | 2025-11-21 05:35:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c587d3a-b519-3ff5-9a3d-10e65ae76e27 | -14.76333 | -60.17126 | 2025-11-21 05:35:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02e9e6af-c195-3344-bb0e-b185ce189c65 | -17.61722 | -54.19125 | 2025-11-21 05:35:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d06e4bda-3ab5-3225-aeb9-a3473fb96328 | -15.50352 | -58.83944 | 2025-11-21 05:35:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d815b40-c6a4-3980-afbb-bce7cafbdcdd | -18.11186 | -54.5169 | 2025-11-21 05:35:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7550b82e-709b-3f15-9ad3-e82976b72333 | -15.42875 | -60.2753 | 2025-11-21 05:35:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a029f043-7316-30b6-94d7-ecb530cb899d | -17.62213 | -54.20013 | 2025-11-21 05:35:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7028a7a3-e280-3e9a-95fe-47368f46effe | -20.88731 | -52.35049 | 2025-11-21 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 886449d1-7a22-36eb-a678-01e71cba5349 | -20.88779 | -52.34475 | 2025-11-21 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 382122fb-501e-3c29-98ac-21690cedf402 | -20.8841 | -52.34378 | 2025-11-21 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37b2b4f8-2a2d-3529-a554-d6ce11c7182a | -20.89034 | -52.3499 | 2025-11-21 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76319a78-7796-34b5-ac49-6941c9d957ac | -20.89079 | -52.34411 | 2025-11-21 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f05de1cc-8090-3a5a-b9e4-459ab87f5891 | -20.88366 | -52.34953 | 2025-11-21 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8455a36-7bf4-331d-8a84-18a973063cd3 | -10.8455 | -56.95977 | 2025-11-21 05:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ebe50ae8-1255-378e-9841-e9e8c97e62d9 | -11.95891 | -62.844 | 2025-11-21 05:57:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 041506dd-55ba-340b-8144-19b0a70e47bd | -9.38072 | -67.83504 | 2025-11-21 05:57:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 47e6a7cb-730c-3432-8d49-347d3c25c050 | -8.7094 | -66.65887 | 2025-11-21 05:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d7769be-e667-3bfa-82b3-adbab100db7b | -9.94376 | -67.24767 | 2025-11-21 05:57:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2a4cd43-94db-3449-a9d0-3652783c595c | -9.03008 | -63.65712 | 2025-11-21 05:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73543a73-3708-381c-b257-f0d9e972d71d | -9.99557 | -65.18426 | 2025-11-21 05:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 543aecf2-b8fc-350f-a5e5-195f84c788cb | -10.25337 | -67.14902 | 2025-11-21 05:57:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ecb9691-7025-3357-abd8-30d7a22308a1 | -11.67082 | -62.61844 | 2025-11-21 05:57:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c637aa4-559e-3293-96cc-2a996cfcdb2e | -9.57232 | -65.17696 | 2025-11-21 05:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6b6ae2f-7908-3c10-95bb-c6c77a5b8009 | -9.99226 | -65.18631 | 2025-11-21 05:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e45cf69c-c3d5-37d3-9110-317fc4243a65 | -10.32625 | -63.69787 | 2025-11-21 05:57:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c2f1ebd-f66f-3fd5-9c1c-0bcfc0f3db16 | -10.32553 | -63.69823 | 2025-11-21 05:57:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 993bb237-2caa-317a-849d-a4350c0e44f7 | -10.84696 | -56.96501 | 2025-11-21 05:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5c5d97e2-365f-3d2a-a9d4-f7dee9160203 | -9.60458 | -65.24584 | 2025-11-21 05:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03f52c84-8f7f-3b9b-b3d4-ee3164709241 | -10.3261 | -63.69432 | 2025-11-21 05:57:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4411d6cc-2b86-3140-bdc9-d02b9d004165 | -9.49489 | -63.50648 | 2025-11-21 05:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
