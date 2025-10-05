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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a86cb26-1b44-3b56-aa5f-835048fbd38d | -15.9698 | -43.32746 | 2025-10-05 03:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c0d4692-7d2c-35ee-b8e2-f750b2771bc6 | -14.29904 | -45.86223 | 2025-10-05 03:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0da9bf87-0b82-3d1a-9bfb-06f93f2f145d | -15.73339 | -46.26443 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f4efe57-387e-31cd-916a-da98393747e9 | -15.7226 | -46.25409 | 2025-10-05 03:36:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6342d1e2-94bb-3a56-872c-73fb009c76b3 | -15.52631 | -46.88008 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7ed3be5-510a-3240-8c81-fcd107b99d1d | -17.02223 | -43.45173 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6a4e2c83-89eb-337f-8991-9ac0b68375e2 | -17.02111 | -43.45719 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ebb397c7-0db1-3365-9b9e-324787bf3fae | -17.01602 | -43.45598 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 81cc0428-9537-398d-b729-1d2e11b92a93 | -15.50289 | -46.86062 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a0c7b07-dbf5-398b-aa45-2ff628b746d1 | -15.54784 | -46.84126 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9cfe1b72-0ea9-3dc0-a8cd-e7bf2985c853 | -14.64408 | -48.33155 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76e8d910-f677-3e44-933f-16fe49c087e9 | -15.91722 | -48.83397 | 2025-10-05 03:36:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ff3aea2-ff1d-3341-99b3-2e52388ea8f2 | -14.00916 | -48.2075 | 2025-10-05 03:36:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59925628-cfad-32db-b879-79092d2c024a | -14.66401 | -48.30896 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 448bae26-177c-3497-8a5d-4b8450f49c0b | -14.32524 | -47.70476 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6f93874d-baa5-3e09-8faf-46d3457f98da | -17.97254 | -45.0044 | 2025-10-05 03:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 787d6274-331a-35aa-ae32-244e00f6b0ce | -14.68965 | -45.17386 | 2025-10-05 03:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8df44f23-2c8e-33ae-82ee-9b67b210f834 | -14.66781 | -48.3592 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1207f99a-429b-345c-8295-ff57a285c852 | -15.12312 | -45.73726 | 2025-10-05 03:36:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54c78082-4895-3acb-8a11-2ea27e7daba2 | -16.29 | -45.24727 | 2025-10-05 03:36:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2779a8ce-db54-36bc-a50e-413d6af519bc | -15.39107 | -47.95375 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 11803fce-8fa3-34f6-a5c8-6779739dc5a8 | -14.67092 | -48.37901 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 38bfc6ff-2c89-3b05-85d1-de9eb5ccc46e | -14.88308 | -48.26606 | 2025-10-05 03:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a2bbba7-9fc2-3cb7-ac9b-f6af707de5fb | -14.69369 | -48.35238 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6489beaf-c213-386a-83cc-6ce5e43b5278 | -14.66927 | -48.36112 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 96ba38f4-1fe4-3655-acc7-003765102fa6 | -15.29278 | -47.33527 | 2025-10-05 03:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 842be06e-c651-33ac-bdd9-e92179e15522 | -14.68677 | -48.34094 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cc81181a-7918-32b4-b3bb-983d6d0faed2 | -15.13326 | -45.74945 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5c3c24c1-aed9-328d-be8c-b630d344bdb9 | -15.72715 | -46.26316 | 2025-10-05 03:36:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a8af168-183a-336c-9df5-0b4c89d8e0ed | -15.34176 | -47.34539 | 2025-10-05 03:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52732dcb-5dbf-341a-8970-ef389aa9f3b3 | -15.54637 | -46.8479 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efaa3ec1-7f98-37fc-a831-3f9488833c91 | -14.93285 | -46.92124 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9938e594-11a7-39a9-ae63-4d2770ea2dab | -15.39778 | -47.95605 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8f2b1dd-4275-3989-a529-ee2e26573242 | -18.33267 | -45.89238 | 2025-10-05 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 96060b5b-72c1-3a59-b746-dd525a01b5cc | -15.30363 | -47.96775 | 2025-10-05 03:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| cf2880fe-92ce-34c8-a931-2f870c4a6896 | -15.1279 | -45.74677 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20c203cc-4006-3470-8d1b-1d79dc6c0b41 | -19.94581 | -44.64258 | 2025-10-05 03:36:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0f392aef-5696-3b86-aee3-d74ae81752f8 | -15.39885 | -47.95774 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e17f0cdc-5cc7-31b2-b0b7-552fbbfe49eb | -18.00511 | -45.01461 | 2025-10-05 03:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56fbfeea-999f-3f3c-b3ef-74878944a972 | -15.20768 | -46.39046 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec623019-64b4-329c-ba2d-be80e4c0c07e | -14.88797 | -48.26351 | 2025-10-05 03:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 98636369-e53c-3d06-992d-007091b3723e | -14.67499 | -48.36053 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| eb0ce74a-efdd-3b0d-9c1c-5e6541fcf8c2 | -14.68724 | -48.305 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbab3fc7-61b6-3361-919d-dc9a6d37d0f6 | -14.89104 | -48.26368 | 2025-10-05 03:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90a213d4-e8f6-3e4e-8295-99807f1ae9e3 | -16.29199 | -45.24229 | 2025-10-05 03:36:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de52002c-3bcd-3d08-a21d-c74f5973fa62 | -15.37879 | -47.94421 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9ff14ce9-d613-38b7-a9be-c8d8eb5009fa | -14.32951 | -47.68532 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7f99a643-c3bb-3150-b7fb-1869a462a6f9 | -14.69351 | -48.27663 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 397b377a-e386-3485-8a0a-1ea69d19249c | -18.33355 | -45.88829 | 2025-10-05 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 8a5473cd-df2f-3543-9849-ae34e1b83844 | -15.54035 | -46.8149 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b749926d-db44-3179-aa6a-eb19d3c426d2 | -13.9187 | -48.19006 | 2025-10-05 03:36:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2153e24-5b2c-3758-b896-b45229f78b1b | -17.0166 | -43.4532 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c38276e-6d1e-3fbb-b863-4d041c5da71e | -14.67125 | -48.28685 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 907a8f4b-1c1a-3801-8ff4-30e862854284 | -13.9134 | -48.19127 | 2025-10-05 03:36:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5429809c-34b8-35c4-b3a9-4c173bad3444 | -15.50548 | -46.85112 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb360156-c5c3-343a-93b1-5ca4ae23ffdc | -15.30529 | -47.96019 | 2025-10-05 03:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 13cdde64-aa50-31f9-a1c1-5f8054d86579 | -15.17339 | -43.63097 | 2025-10-05 03:36:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9ff4e7be-6d3b-32fe-8379-c509e079279f | -15.87318 | -46.25386 | 2025-10-05 03:36:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 002ef724-837d-347a-842b-5940608e32a1 | -19.94553 | -44.39137 | 2025-10-05 03:36:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4251344-9cc4-3782-bf4d-6b0296b0a346 | -15.96395 | -43.32968 | 2025-10-05 03:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb8792bf-9d91-3d0f-951f-3b0f05508e72 | -15.13802 | -45.72872 | 2025-10-05 03:36:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad7141a2-ae51-323b-9728-e010f39fa2f0 | -14.65172 | -48.33079 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 125dc027-7b0a-3d48-abfb-2a437b9631d2 | -14.32191 | -47.68696 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fca204d3-8452-373f-b530-82c6d6cda7d3 | -15.35634 | -46.30111 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae862388-41ea-346d-a3f0-1cade1287773 | -14.64552 | -48.33416 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 17aec1ec-64b1-3d86-9894-427cdaf4248e | -15.30512 | -47.95644 | 2025-10-05 03:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 747d5fd3-71f9-3c40-8607-b1f6bc899dfd | -14.93633 | -46.84221 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcece2a8-2bfe-33b9-99d5-92115934e353 | -15.90914 | -48.8264 | 2025-10-05 03:36:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6653f0d8-dc14-3708-aa56-67d4a63ee45d | -17.02169 | -43.45438 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e9b7e97e-737a-35f1-aab2-ca4f5e141ac0 | -14.94273 | -46.8442 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38e95cae-ff0a-3862-b162-92309a501507 | -17.20779 | -44.44774 | 2025-10-05 03:36:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2760c2dc-6407-3359-99d9-d5d294c3bc60 | -18.55239 | -41.5783 | 2025-10-05 03:36:00 | NPP-375D | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c448ba80-cbb3-3f7e-9a21-ca47dace1cb8 | -15.5467 | -46.81591 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcbc5fc3-4b90-37a1-aafd-1551e2b95f61 | -16.29109 | -45.24661 | 2025-10-05 03:36:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e3ede58-0037-3b81-a989-776faf17c05e | -14.92604 | -46.92102 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43059ab1-6604-33ca-b41a-8778e8c1a9f4 | -15.14543 | -45.75223 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a92dca9-da3d-3e00-b81f-aa2064f8288d | -15.50405 | -46.85547 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 798075ef-fa5f-3abb-9536-58c6931e6870 | -17.97879 | -45.0023 | 2025-10-05 03:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39fb6d32-fc73-3c8b-8003-29495b4e7420 | -15.54658 | -46.8173 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3665efc9-5e62-3922-abb8-9047b389d4f8 | -15.82526 | -42.61293 | 2025-10-05 03:36:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3628fc28-ec6f-3886-9d30-24e2fb24f841 | -19.95089 | -44.64437 | 2025-10-05 03:36:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ee3b339-2c82-3e62-b27f-b48e99224597 | -14.46013 | -46.34076 | 2025-10-05 03:36:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 916533ca-fb17-3b9f-b44c-f81d2d1d87ab | -17.95238 | -47.02354 | 2025-10-05 03:36:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d93e1ab6-9482-3dba-b261-0c1bf675df99 | -15.5351 | -46.80731 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32f671d7-04bf-33c8-9a5a-959676d6ede7 | -20.73597 | -44.32755 | 2025-10-05 03:36:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eff05277-2dde-3afe-9efe-b232dc434333 | -17.5882 | -44.45696 | 2025-10-05 03:36:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4febca54-fe21-3412-b5dc-0ac539c92ce1 | -17.59365 | -44.4578 | 2025-10-05 03:36:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d39e77a-5046-3182-bcad-e49fd1954c18 | -14.68822 | -48.34349 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 470c14a1-76fd-3a91-9cde-dbd16c643e38 | -15.77289 | -46.26232 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d31f69f-b609-3d26-9418-8615a1b3bea0 | -14.68847 | -48.27668 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13c013d4-9858-3209-b6ad-49147c486edb | -19.81575 | -46.07139 | 2025-10-05 03:36:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efe39188-eef2-32b6-8625-13015600f1b8 | -15.13398 | -45.74816 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae4b6111-4bc6-371b-a554-027756126a8a | -17.97798 | -45.00602 | 2025-10-05 03:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 259ef0f8-3ebc-3fac-ad77-08ecac2a62ed | -15.91474 | -48.83475 | 2025-10-05 03:36:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e6efcdd9-b30e-34c5-a4ea-190710251ac6 | -19.94426 | -44.39048 | 2025-10-05 03:36:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9be10068-9545-3a0c-ac88-1eedcafc8780 | -19.58269 | -44.63598 | 2025-10-05 03:36:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8eeed61-567e-31f8-a8d5-04eb5565dd9c | -15.20425 | -46.38467 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36abfc4d-bc8e-352e-ae08-478b440e7959 | -15.12209 | -45.74205 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7200c8b-1525-3dc1-a128-e3e360ac7c08 | -15.12105 | -45.74684 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e50f84ad-02e0-38b8-bd25-c7234d600015 | -14.64988 | -48.33906 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README35.md)
