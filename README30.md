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
| 00a9ad58-db12-3ffe-93f0-efbc08984ae3 | -14.48844 | -45.67234 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a3e904b-d612-3181-bf12-8308acd12f09 | -13.45434 | -51.80098 | 2026-08-19 04:21:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2e759ee-508f-3995-bedd-c1fa86345b87 | -17.95283 | -44.44483 | 2026-08-19 04:21:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74046e05-6083-3119-b9db-d99379a8541f | -14.45482 | -45.6274 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e1912f8-532c-3dd6-9254-8fbac96d7f9d | -20.58234 | -45.92193 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71d1aad1-6e1c-35c0-8915-c22e4225dc15 | -15.32183 | -56.46077 | 2026-08-19 04:21:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3c0b30b-1032-3e80-8ed5-23c3e15e696c | -15.07117 | -45.32875 | 2026-08-19 04:21:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e938c963-43b2-38a2-b3a3-9e3ea9c4281d | -20.5832 | -45.93773 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14a59af8-09d2-3b95-a15a-e4e83b724774 | -21.65765 | -45.57049 | 2026-08-19 04:21:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5b081990-8029-35b8-a1e6-f8fd26157088 | -19.6752 | -45.91343 | 2026-08-19 04:21:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36be3759-f7f4-3472-81a1-d497ac25d3e1 | -18.46386 | -47.2289 | 2026-08-19 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96d6c559-2dbc-3faa-a8c2-1aa1575ef5db | -20.65605 | -46.19485 | 2026-08-19 04:21:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4b325d1-8b94-3beb-ae17-6d7e7942a20d | -21.39602 | -45.95345 | 2026-08-19 04:21:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 19fde530-20c1-3ce2-90d7-bbe0c4eb04cc | -19.52394 | -45.3247 | 2026-08-19 04:21:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b61ecffd-e940-3149-8a51-bbe183c44fe2 | -16.71712 | -46.40459 | 2026-08-19 04:21:00 | NPP-375D | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa7b3d3c-de6c-3dea-825e-3fb8b417c2ec | -15.31665 | -56.45331 | 2026-08-19 04:21:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ae48542-e251-3389-8fd3-2df335b0fa80 | -15.88067 | -55.56781 | 2026-08-19 04:21:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3930f1af-94b2-30bb-816e-0222ee972aeb | -13.47218 | -51.78961 | 2026-08-19 04:21:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 527fc905-c819-3479-a5cb-2dbda5d04b67 | -14.48153 | -45.67112 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd0f8e8c-21aa-3604-a00c-bd047155f8d6 | -15.88684 | -55.56876 | 2026-08-19 04:21:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3561abc9-21d4-33ba-95f0-5dd61a51656a | -17.47732 | -48.86843 | 2026-08-19 04:21:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcbd8f13-d7e5-312d-955c-e44ada5c8f33 | -17.9391 | -44.42384 | 2026-08-19 04:21:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6fd89aa-ada3-3580-827a-8990e41fb987 | -20.18549 | -44.59115 | 2026-08-19 04:21:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ea79efd8-2c28-3c63-8187-6413bd101d6a | -17.91856 | -44.34258 | 2026-08-19 04:21:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be3fd537-8e57-34d2-9de6-8ae25b53dec5 | -19.66573 | -45.90792 | 2026-08-19 04:21:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f2122f3a-39d4-348b-8219-73861425a240 | -20.58294 | -45.91824 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f218f6c9-97f9-3395-874e-21f4f1773680 | -14.45547 | -45.62354 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e7e7bf7-49e4-3566-86f5-df3ba720c4a3 | -21.04423 | -48.4771 | 2026-08-19 04:21:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ea5d179-b459-366b-ac76-6b432e9cf192 | -14.45137 | -45.62679 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5a61ae4-7707-350d-8d11-0dff609ddef1 | -14.19856 | -51.81097 | 2026-08-19 04:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f729f023-7657-31e5-8ac5-51d68af9b3eb | -15.31542 | -56.45285 | 2026-08-19 04:21:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 109da2e2-c17e-3c79-bfa8-204038b648e2 | -20.28969 | -46.46477 | 2026-08-19 04:21:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb8f23d0-f407-3288-bf15-60d3779e7d2a | -16.57406 | -51.62114 | 2026-08-19 04:21:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 279b6dae-9dbb-33bf-b720-81f3160a9e94 | -19.06326 | -57.35881 | 2026-08-19 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 362449a7-58bd-367e-ba4e-2ef0b273fe34 | -15.01281 | -41.94977 | 2026-08-19 04:21:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 70cb500d-cfe9-3a56-9962-4eafda0fcf42 | -20.29367 | -46.46186 | 2026-08-19 04:21:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef1a9d0b-e8ad-31b1-a179-cb77721996f4 | -21.04504 | -48.47264 | 2026-08-19 04:21:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1e97d7d-146b-3737-b626-3bccfcafef46 | -20.8805 | -45.29134 | 2026-08-19 04:21:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e359805e-3d01-343f-84dc-50e989bcc8d2 | -15.43873 | -41.38762 | 2026-08-19 04:21:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e5bbcdcb-79c2-30c0-bffe-ed951500be78 | -20.18897 | -45.40081 | 2026-08-19 04:21:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 4b1942ca-f46c-3336-bacd-7e70952a90e7 | -20.28104 | -46.4747 | 2026-08-19 04:21:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb956077-ebd8-3829-813d-ce90867913f6 | -14.90228 | -44.80424 | 2026-08-19 04:21:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 40265507-40cc-3551-8920-0f5f7498c6dd | -15.23615 | -57.6646 | 2026-08-19 04:21:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db7ddf31-c098-3241-a7e3-c1d8291384db | -20.58111 | -45.92944 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 319f9e9d-83ba-3832-9d67-230532cfd3db | -17.50562 | -49.97111 | 2026-08-19 04:21:00 | NPP-375D | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03c40ff1-bd25-3394-a38a-4dc62c520b20 | -14.4932 | -45.66521 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14ab5e6e-3021-38b7-92d1-235fcc43c2ed | -20.41644 | -44.08708 | 2026-08-19 04:21:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 63826f06-61cc-31b7-a7e8-27211db443d8 | -15.00941 | -41.94922 | 2026-08-19 04:21:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49ef26ae-67ff-3ebc-9c1d-d0dbab1ec9e1 | -17.24306 | -46.90355 | 2026-08-19 04:21:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ef32d4c-deb7-303e-978c-f18b05dded6f | -16.50206 | -48.83701 | 2026-08-19 04:21:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cc23a33-5ef3-326e-a327-6ad5aa50bc44 | -20.28569 | -46.46777 | 2026-08-19 04:21:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 041ee60e-9b35-3b89-866b-6eeb9aebb4e8 | -17.9534 | -44.4412 | 2026-08-19 04:21:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18145e9e-e0de-3843-a129-41880a15e77a | -14.48219 | -45.66724 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7887b39-c2c6-3e31-a882-3fd66349294d | -19.81558 | -43.08007 | 2026-08-19 04:21:00 | NPP-375D | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ba1cfb20-31d7-3e50-9b12-273342de1cd7 | -19.46601 | -44.1816 | 2026-08-19 04:21:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14ef0010-cba4-36c6-af8d-c14c2e30d5e0 | -20.30003 | -46.48651 | 2026-08-19 04:21:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c640abf-3994-3edb-871d-7b576cc373f8 | -17.44071 | -47.16506 | 2026-08-19 04:21:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2537283-0dbb-31d6-bb95-75575313e1a1 | -15.31536 | -56.4593 | 2026-08-19 04:21:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c65d289f-76f5-392e-8994-f0429344ba4c | -14.48778 | -45.67621 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94f8236e-5ec2-3916-b8c9-293c3bcc96f5 | -19.67582 | -45.90968 | 2026-08-19 04:21:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 25506678-8aa0-3f0c-ab87-93f95f616a7f | -17.99154 | -48.54574 | 2026-08-19 04:21:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4d0e7312-35b5-32f8-845e-20b389ae41b0 | -21.09255 | -45.10475 | 2026-08-19 04:21:00 | NPP-375D | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7e735c48-ce03-376f-8d55-49a104aebfcd | -14.45827 | -45.62801 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f281a93c-cca6-36c7-96b7-cf5a471d5d43 | -19.6691 | -45.9085 | 2026-08-19 04:21:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 10ff8533-e0b7-355e-8307-9831aac061ba | -15.43931 | -41.3837 | 2026-08-19 04:21:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b7bfcfe1-fbc4-31e4-95ef-2bdc102043e8 | -15.22934 | -57.66246 | 2026-08-19 04:21:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50b94fbc-bc84-3def-9f77-e9dec2c85691 | -20.18837 | -45.40452 | 2026-08-19 04:21:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 40ff1927-2d57-3822-8c0a-f78236a152e9 | -18.48918 | -47.25097 | 2026-08-19 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7332f5c-673c-3618-a7dd-1bc2e500fa6a | -13.44928 | -51.80013 | 2026-08-19 04:21:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7856df7-ccea-397a-9034-c40fbafe43c1 | -19.66635 | -45.90416 | 2026-08-19 04:21:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53b41137-40fd-38c6-aeda-21f79d4bedc9 | -20.32831 | -42.40249 | 2026-08-19 04:21:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3a2ec422-1e15-3354-986a-3fde43dec146 | -20.77299 | -45.30657 | 2026-08-19 04:21:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99bd1c89-0a03-380b-81dd-3dbb7dae523d | -14.89417 | -49.30786 | 2026-08-19 04:21:00 | NPP-375D | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d8f4d3d-37a3-3512-9032-fb8fa660c04a | -19.07716 | -57.35669 | 2026-08-19 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3af4eaf6-a453-33f9-88a6-300f10393a9e | -21.20065 | -48.52562 | 2026-08-19 04:21:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b01b6de6-88bf-3299-9975-3c6dfd59b8d2 | -14.48975 | -45.6646 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 591ad232-e7c1-38aa-adb4-2972dfd33ec7 | -18.24569 | -45.58725 | 2026-08-19 04:21:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 88df55d7-2541-37c3-adc4-415c6ea84f2d | -20.8799 | -45.29504 | 2026-08-19 04:21:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2bab7815-c23a-3ee6-97f5-c7f2755e9cdd | -15.71013 | -47.8008 | 2026-08-19 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 194401fd-57f1-30b8-849f-7d3a130b98cc | -19.0759 | -57.36215 | 2026-08-19 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c52a32da-2211-3090-84a9-8dfeef1d514d | -20.29644 | -46.46618 | 2026-08-19 04:21:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 432b89d7-279c-3a79-8cb6-d4865fab741b | -19.47805 | -45.98242 | 2026-08-19 04:21:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97cedf3b-90cf-31fa-b499-26b6d11def4e | -14.49189 | -45.67295 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 46113bb9-e8cb-3c21-9c6f-eaef8c7ad9c9 | -18.81058 | -46.74821 | 2026-08-19 04:21:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d3030ad-21fe-3681-a1e5-20a6903190a6 | -21.08922 | -45.10415 | 2026-08-19 04:21:00 | NPP-375D | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5b53fcda-7526-3a7d-8891-582b3855050b | -20.57777 | -45.92879 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaa21fac-8e3c-3eef-a6c8-b81abc68097c | -16.24651 | -57.66014 | 2026-08-19 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a35238d4-07db-3e49-bada-f4e386f4aaf2 | -21.39935 | -45.95408 | 2026-08-19 04:21:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 46de70c4-3ec5-3ede-aa31-89617f89b8bc | -17.59321 | -44.59534 | 2026-08-19 04:21:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49e538a6-fd78-37c5-b430-b81b55d83f8a | -17.91913 | -44.33895 | 2026-08-19 04:21:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7004617c-f1e7-3738-9b01-c14799a50aa5 | -20.58048 | -45.93325 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e054f9ec-036b-3d0a-b0b3-3a01323327fd | -13.45377 | -51.80396 | 2026-08-19 04:21:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9fc9c54-95b5-399e-803b-c2421e203029 | -20.58963 | -45.91943 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1807f2e8-970b-36fe-b34d-afde6f757c44 | -19.73663 | -57.94514 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e1d7f60f-5994-3a63-b28e-dadf28654b24 | -19.74993 | -57.95436 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 079f23b0-f6d1-3692-9cf9-3024af974649 | -22.11809 | -46.65881 | 2026-08-19 04:23:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ec8e114a-e526-30dd-95c9-58b844c355ac | -22.87876 | -42.46444 | 2026-08-19 04:23:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 235db9a3-5cb2-3211-bffd-9adf01648699 | -21.76444 | -47.54564 | 2026-08-19 04:23:00 | NPP-375D | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db9e811c-ea1a-385a-a58f-cff7060e7479 | -19.74214 | -57.95838 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6af45859-b699-3743-a3a0-2317a14690d9 | -21.45017 | -48.51284 | 2026-08-19 04:23:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README31.md)
