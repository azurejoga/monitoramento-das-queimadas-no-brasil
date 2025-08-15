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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d61b35f2-7d5c-37ef-bf33-5a4cb8a06d7f | -17.68153 | -44.44101 | 2025-08-15 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a5ce1675-288b-361c-a547-f0d88cd4f078 | -11.54381 | -47.26382 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a955dc58-e63a-3b45-93f5-1e53e5180283 | -14.02166 | -52.03712 | 2025-08-15 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e73edc3-1713-32ae-8997-22b4968cf970 | -13.61319 | -46.91837 | 2025-08-15 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 695762e3-bcb8-3e24-b70a-70fffe7a0fcc | -13.15709 | -46.86871 | 2025-08-15 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d059a9a-6d0f-3d32-8594-c288a78a9ca8 | -12.35621 | -49.91131 | 2025-08-15 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8a91880-3f13-3e52-9376-984b9c725bd7 | -13.32283 | -45.23656 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15a0387e-b896-34fc-ac63-3df34bf56442 | -15.57899 | -47.32267 | 2025-08-15 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e9faa0e-e4e5-3b4d-9f5d-2958c080d9e5 | -15.39195 | -46.58762 | 2025-08-15 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7eb053e-a82f-36a5-a472-210bab147afd | -17.64497 | -44.49362 | 2025-08-15 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa0400d4-0a83-3875-9f6d-c1a0a4b09d56 | -11.3536 | -55.4067 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 251253a0-9f59-3fa5-a2d2-6d781fa16537 | -11.3548 | -55.41841 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ae8f69fb-e433-3329-b08b-626b7953d92f | -11.34497 | -55.41242 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 13402ec9-b18d-341c-b1b1-5109a28cd40c | -12.58476 | -46.95169 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f3618681-3457-3087-9e96-002052ee095f | -16.47922 | -51.98345 | 2025-08-15 04:04:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f8d9aba-25c7-3a7c-9244-6abe72468f0b | -12.50174 | -47.01983 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90dbd9ef-e01e-39f4-8129-fcea8f32eeb3 | -13.3251 | -45.22339 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5dc4357-66bd-3720-8eef-bf325e12a056 | -16.30075 | -52.92461 | 2025-08-15 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d9d8b5ed-0ff6-3cf9-a15b-912e75dd3355 | -14.79312 | -42.72469 | 2025-08-15 04:04:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 787174b2-6830-305a-b1b2-2febbf37f7d1 | -20.32511 | -45.2299 | 2025-08-15 04:06:00 | NOAA-21 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dc7dde67-ecd3-335b-8137-10fb7b4e7e46 | -20.46473 | -47.40791 | 2025-08-15 04:06:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1e873ff-92e0-3f4e-a69c-278d6b5b49a1 | -21.08421 | -44.98301 | 2025-08-15 04:06:00 | NOAA-21 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8073ee33-9d07-3528-aadb-0738222b831f | -19.91057 | -47.47282 | 2025-08-15 04:06:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03ce615a-8fdb-357a-b01e-4cfe4d06f2e7 | -22.18953 | -45.35209 | 2025-08-15 04:06:00 | NOAA-21 | CRISTINA | MINAS GERAIS | Brasil | 3120508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e450998a-08d1-3901-854c-30634a8c7755 | -19.6466 | -46.09553 | 2025-08-15 04:06:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 641f6a5b-8854-3e52-82c2-34780c37cf54 | -23.46138 | -47.38129 | 2025-08-15 04:06:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 34de8609-c1be-3e13-8bbb-8166668bacea | -22.95903 | -47.15348 | 2025-08-15 04:06:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 98f78e9e-2a56-344b-a6fd-dfb262120c2d | -20.85565 | -46.38128 | 2025-08-15 04:06:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eba9baa3-652d-33a4-9689-c098a2eceea3 | -18.9705 | -49.50084 | 2025-08-15 04:06:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5af3f190-6fec-333e-acc9-d75d1ece8e91 | -20.57018 | -47.0971 | 2025-08-15 04:06:00 | NOAA-21 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8220beb1-17ee-3dd0-ac98-d2c8e3d35b48 | -21.22449 | -48.74525 | 2025-08-15 04:06:00 | NOAA-21 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| e26b31c6-78ba-3002-a451-b127300df790 | -21.57996 | -47.0072 | 2025-08-15 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f027035-eb4d-3559-8456-027b4ffbc658 | -23.08504 | -46.70055 | 2025-08-15 04:06:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f5ab7cbd-1e6b-36b3-9e9e-0019b6e1337e | -22.89626 | -43.65654 | 2025-08-15 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 43d90ef7-c654-32d3-afb7-22a4d680e253 | -22.95985 | -48.82338 | 2025-08-15 04:06:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5dde659-2955-30eb-9f4b-a94b5fd10bb4 | -23.41013 | -47.1145 | 2025-08-15 04:06:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bffdd811-72d2-3c03-9ec8-f47e5eefd362 | -18.96712 | -49.50318 | 2025-08-15 04:06:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08a97fd0-5efc-3488-9048-7b47445d99c3 | -21.99742 | -44.88021 | 2025-08-15 04:06:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e1762316-523c-3c92-acbd-58a7849876bc | -22.58819 | -45.83221 | 2025-08-15 04:06:00 | NOAA-21 | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f6613b1-5c6c-3aaf-898a-4845bc89e592 | -18.96796 | -49.49889 | 2025-08-15 04:06:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45402be8-c471-3e1e-aa8f-42ca4f19db58 | -18.87181 | -51.99821 | 2025-08-15 04:06:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bc70382-9e9a-3fed-9928-e68d3b3a3127 | -23.20489 | -46.74862 | 2025-08-15 04:06:00 | NOAA-21 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 34a76130-6046-31f6-833e-371db1eecad8 | -20.40049 | -45.40886 | 2025-08-15 04:06:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2ccb7979-97f4-350d-ab51-f85f0a16731f | -20.40116 | -45.4049 | 2025-08-15 04:06:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8fdb2b79-fd00-3522-9278-c08bbe90beec | -20.40183 | -45.40092 | 2025-08-15 04:06:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 11c96854-c406-3e83-b081-fc7bfe52056d | -23.92233 | -53.4881 | 2025-08-15 04:06:00 | NOAA-21 | PEROBAL | PARANÁ | Brasil | 4118857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f95bc384-fb05-3c1c-8bd8-497bff339133 | -20.32916 | -45.22664 | 2025-08-15 04:06:00 | NOAA-21 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b57bb583-5069-3d5d-aa84-795ef1a9f789 | -20.59752 | -47.85407 | 2025-08-15 04:06:00 | NOAA-21 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9993b085-d460-33fd-9b69-c9ff7e9fa39f | -20.6482 | -48.69594 | 2025-08-15 04:06:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1d300c7-f7db-35af-936c-b1852ab2bf4c | -24.17142 | -50.3516 | 2025-08-15 04:06:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7ffa3d02-c901-3716-abd8-de4378f1092f | -19.90683 | -47.47195 | 2025-08-15 04:06:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5ea345c-448a-320d-a41c-a8c5afdfc398 | -20.56653 | -47.09636 | 2025-08-15 04:06:00 | NOAA-21 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4792acce-da8d-36cf-bd85-fe9c5e92ffbe | -20.46548 | -46.21939 | 2025-08-15 04:06:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e38743d5-b7b6-3da1-b403-0ff8138399ad | -22.36987 | -47.56564 | 2025-08-15 04:06:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 5930d782-ec30-3567-9170-0844c816e23c | -21.99679 | -44.88401 | 2025-08-15 04:06:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a8556568-6168-34b0-9bb6-04fb99b2a57c | -20.97976 | -47.42128 | 2025-08-15 04:06:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f764dad-08fb-3399-900e-6357bae1f789 | -23.27179 | -51.20837 | 2025-08-15 04:06:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| e7b58bc6-5e51-3269-83cb-baadb76edfc0 | -23.35714 | -46.9175 | 2025-08-15 04:06:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1da0b1b5-6f9d-3ea1-ba6f-cde6237c61e0 | -21.42841 | -45.96821 | 2025-08-15 04:06:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c8121885-c997-3881-8671-0bd20e14f94a | -21.2829 | -44.03553 | 2025-08-15 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bd44d9ba-b682-3064-a9f5-bdb684342ab4 | -21.36449 | -45.04643 | 2025-08-15 04:06:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ff35bb05-0650-3590-9b1c-2fe58222bbdb | -21.22052 | -48.7445 | 2025-08-15 04:06:00 | NOAA-21 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| ef357189-60e7-32c4-b397-30ed6124c4b4 | -21.20567 | -46.69287 | 2025-08-15 04:06:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 60c0ad00-e255-3985-a04b-cc195064abe3 | -20.97607 | -47.42049 | 2025-08-15 04:06:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02d9b42f-531b-39c7-acea-f822dc584819 | -21.58431 | -47.00359 | 2025-08-15 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d24b8ce-d799-3a8c-a5be-77bdb3409f00 | -23.98351 | -51.27643 | 2025-08-15 04:06:00 | NOAA-21 | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1255cac-60b9-3b7e-a4db-b8dd9e4d1eea | -22.0496 | -48.3414 | 2025-08-15 04:06:00 | NOAA-21 | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56aa1221-a671-3e18-88c3-edd8fcc7040e | -23.33909 | -46.89621 | 2025-08-15 04:06:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 23f9121b-7ff2-38cd-8446-e0565d811e9e | -22.71371 | -47.32635 | 2025-08-15 04:06:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46359538-689d-39f2-9298-55c9ca19c119 | -21.26548 | -43.7593 | 2025-08-15 04:06:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 71941773-37ab-3b59-84e8-854b33fffbbf | -22.39761 | -45.4752 | 2025-08-15 04:06:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| af5b9f39-e9a6-319e-b7b8-c58695cc2607 | -22.40034 | -45.47975 | 2025-08-15 04:06:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 888be1e5-9e42-33af-b220-47796303d283 | -23.34258 | -46.89695 | 2025-08-15 04:06:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 298e4106-f6b2-3ab6-851d-ce13e3eda8f8 | -23.25807 | -47.0881 | 2025-08-15 04:06:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 09f21922-f950-3f9a-8e11-b01dffde1172 | -22.39826 | -45.47128 | 2025-08-15 04:06:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a6927b5d-2b57-3706-bd83-d781829dacc8 | -22.83858 | -46.42601 | 2025-08-15 04:06:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4f6d3840-4f3f-3055-ae21-0cf62845f498 | -21.63458 | -49.84342 | 2025-08-15 04:06:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3e933a22-d776-35cd-98a4-77e4c041f171 | -19.64587 | -46.09978 | 2025-08-15 04:06:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eb91a03-87c0-3963-8d43-daf2ac9f8399 | -22.27635 | -49.05338 | 2025-08-15 04:06:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b4ea63c-1bb6-36da-bf07-e5db1f71306f | -20.32576 | -45.22602 | 2025-08-15 04:06:00 | NOAA-21 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f772941f-64d4-3d0c-bc3b-8de3de04dffc | -21.21948 | -48.74999 | 2025-08-15 04:06:00 | NOAA-21 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 7ced4791-ffce-3195-841e-7f98796492c8 | -23.18222 | -46.60274 | 2025-08-15 04:06:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 24d7a2ba-8928-3af7-9f63-f0aa2ca617ea | -22.5703 | -47.02614 | 2025-08-15 04:06:00 | NOAA-21 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db93d175-98a5-32df-be14-26d66dbb5577 | -22.98586 | -49.17677 | 2025-08-15 04:06:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 254a7ee3-b301-35fa-b458-e3cb03cbf107 | -21.84343 | -46.68604 | 2025-08-15 04:06:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0786a960-9881-3bc0-81ab-d70b756a8f00 | -22.71731 | -47.32705 | 2025-08-15 04:06:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8415089-84a6-3c0e-b646-1fde8a774453 | -21.19391 | -45.68879 | 2025-08-15 04:06:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f8c309fe-b52a-35e6-90ed-a52fc1a86ebc | -21.84694 | -46.68683 | 2025-08-15 04:06:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d09f9bd5-1c65-3571-9e22-abd79664471f | -22.40098 | -45.47585 | 2025-08-15 04:06:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 588eb3d8-018a-365e-be39-27abc042871f | -22.68418 | -50.47492 | 2025-08-15 04:06:00 | NOAA-21 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 729eb9d5-f288-36d9-af25-13ba07679b2c | -20.65825 | -45.67262 | 2025-08-15 04:06:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d8d63ee-9146-3148-8189-5caa6e42d6f8 | -23.08618 | -46.70008 | 2025-08-15 04:06:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 19896430-c98a-38ad-865d-e9ef7b6c7d4d | -21.05477 | -48.61593 | 2025-08-15 04:06:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ef5917c5-4808-345a-8551-85b8644da175 | -23.3433 | -46.89283 | 2025-08-15 04:06:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 743c0cd4-725c-3c4b-ae85-96d00bcb0061 | -21.04527 | -44.9998 | 2025-08-15 04:06:00 | NOAA-21 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3d172004-8f34-34f8-8d11-87a919914d80 | -20.47156 | -44.06617 | 2025-08-15 04:06:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1cd6203c-ebf1-3d9d-ba05-aa9531d6a5fd | -18.96969 | -49.50516 | 2025-08-15 04:06:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d96bbc8e-20c6-3c60-84b7-fcf1137e5e58 | -20.39842 | -45.40028 | 2025-08-15 04:06:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8d24c229-8e11-3687-bde0-b8529a3a530b | -21.26606 | -43.75561 | 2025-08-15 04:06:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1da8c1a9-a8b3-3e12-aa9a-970c0fce35f0 | -28.60417 | -50.63655 | 2025-08-15 04:08:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |


[Clique aqui para ver as próximas entradas](README26.md)
