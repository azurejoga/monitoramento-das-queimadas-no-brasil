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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ee3775c-797e-38f7-8ab7-1e05810ae61e | -16.41213 | -45.68456 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b87e0a29-31f1-3915-8e2a-32b755cacae3 | -18.59455 | -47.19112 | 2025-09-12 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7a5f8ba7-d866-385a-9c87-8b9845064f67 | -23.14204 | -48.25502 | 2025-09-12 03:40:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 0a96eb7c-d044-3ce7-901a-9120109bc435 | -15.53568 | -48.552 | 2025-09-12 03:40:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 186c48f7-b771-30e0-a194-0ec3516dd04b | -20.35402 | -48.41039 | 2025-09-12 03:40:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3a1312e-62d1-37f9-8e5d-6afc8d364ba6 | -21.26998 | -43.86456 | 2025-09-12 03:40:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 55fa62d0-cabf-3b7d-90f9-7ae19fb11ca0 | -23.49039 | -47.26552 | 2025-09-12 03:40:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec338694-0283-3b95-b18c-16d2f8035b5f | -17.94091 | -46.92962 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b72db45-9f13-39aa-9b90-768b3c507ca5 | -19.99376 | -47.63941 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 930c54d5-aa82-3fcc-a580-f4bbf84ce3a3 | -15.5283 | -48.55754 | 2025-09-12 03:40:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 13dce122-20c6-34ca-a259-55201ae2f601 | -17.13636 | -48.49796 | 2025-09-12 03:40:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 99e02524-35d2-3bd4-9d4f-69d3b942f5c3 | -18.77819 | -48.54223 | 2025-09-12 03:40:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6669681-0114-33f2-9750-668f1d84b245 | -19.88265 | -42.04844 | 2025-09-12 03:40:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bee837b7-0d4f-3147-b38f-4818ca4337d2 | -19.97578 | -47.59963 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9624c695-8c9f-3d4c-a389-db4b246e792d | -21.18734 | -44.95308 | 2025-09-12 03:40:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a0e3428a-6aa9-3a8a-be97-c2b057879451 | -17.58672 | -42.17048 | 2025-09-12 03:40:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 39521808-d32b-3c31-921d-ce822981766d | -17.43715 | -49.23057 | 2025-09-12 03:40:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bb36bc4-0141-3dd5-ae28-d07481b55e12 | -23.53889 | -47.14186 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 235b11f5-7ff4-320d-8d5d-43f3a71401e6 | -22.78704 | -47.81326 | 2025-09-12 03:40:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25ceb4f5-90a0-30a3-8481-4414e3ec4c85 | -18.75464 | -47.62345 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3812091-aac7-31ce-939d-14f9532fe93c | -21.94382 | -47.55709 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2d601f4b-2b94-3927-bb58-99b292f2e3b6 | -19.56609 | -44.24409 | 2025-09-12 03:40:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67315aa9-9975-36e1-a8a6-268034159a10 | -21.33934 | -43.5073 | 2025-09-12 03:40:00 | NOAA-21 | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8bb79eb7-2035-326d-a30a-5d18d689259f | -21.36836 | -45.16404 | 2025-09-12 03:40:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bc8c1194-b24f-39f4-a964-deecb78c793a | -18.05849 | -45.44138 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bce2be48-115d-3026-b2f4-1eb67c834adb | -17.4304 | -49.2308 | 2025-09-12 03:40:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57c46d22-db6f-3039-bb8d-f09a00c45479 | -21.29087 | -45.95378 | 2025-09-12 03:40:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| f02119cc-87e3-3ad3-af0e-88a5f8653a03 | -20.27046 | -42.1142 | 2025-09-12 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| f3d1b98d-a792-391e-aadc-567e353a1efb | -18.74896 | -47.62191 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c1ccb84-cd87-34fe-8e9a-2af97442afb6 | -18.77222 | -48.54052 | 2025-09-12 03:40:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7e5e40ce-e164-39ec-b74e-6ff155b49c27 | -20.11593 | -42.35644 | 2025-09-12 03:40:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a73f748-9304-3648-9f75-d75e609172a7 | -22.70016 | -48.69639 | 2025-09-12 03:40:00 | NOAA-21 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f797dc36-ef49-3096-824a-5db70f254010 | -23.49551 | -47.26668 | 2025-09-12 03:40:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 92b777d1-335a-3b0a-b57c-97ef33525f4a | -19.06007 | -48.73899 | 2025-09-12 03:40:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dc55ed3-6e97-3b1a-a859-ac563f50af7c | -21.95123 | -47.55867 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4cf7ad3b-cfc9-35fd-b0df-272c0bce339e | -21.38929 | -45.18943 | 2025-09-12 03:40:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d97d1364-419d-3118-9aa1-bcd68df8d4b1 | -17.34633 | -46.68014 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f2fd58f-941b-3c8b-b6c5-fc9594ce823d | -21.32802 | -45.00337 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cfffa17b-1233-3a8b-9612-7b05097d01b0 | -18.53733 | -48.41563 | 2025-09-12 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 469808f2-4acf-3ec2-a6c8-8f6c0b3ba2f4 | -20.12072 | -42.35316 | 2025-09-12 03:40:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1bd6db0d-109c-301e-b24f-3c4b2a22821e | -19.84097 | -44.58397 | 2025-09-12 03:40:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b7cca69d-a536-342f-aa84-11da3f54821b | -22.1911 | -49.59953 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 593a3ecc-bea9-304d-9d2b-dc723acf7938 | -20.03866 | -41.74843 | 2025-09-12 03:40:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8b1d0ec6-a79f-3e3d-a741-48f0a4d80f0e | -20.00517 | -47.64107 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88a21d3f-c352-3610-9908-7405e3dccf67 | -18.44655 | -47.18161 | 2025-09-12 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f693515d-e541-3fbb-b579-3bcec49d4c39 | -20.26453 | -42.12401 | 2025-09-12 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 946246ef-0571-3374-8ceb-8440b16ccc90 | -19.98046 | -47.60516 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98e328f1-239b-30c1-b27d-553e17ebc9d5 | -21.18715 | -47.51997 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 7553aafc-a5b5-3fe8-a7fe-ce1980869957 | -21.95376 | -47.56317 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e600b131-25fc-310c-a0ea-f2291c61f719 | -18.81658 | -46.87868 | 2025-09-12 03:40:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 844ad8b5-a9d7-3dc4-9fa0-292d7ef1df93 | -19.64 | -41.58296 | 2025-09-12 03:40:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2efe5340-cec5-320a-b520-1301c9cbd9ea | -22.39552 | -47.38916 | 2025-09-12 03:40:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 524f543c-f35b-3483-94c0-bee21c65e8b1 | -19.63906 | -41.58814 | 2025-09-12 03:40:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 665cda4e-29a4-3284-be98-0a9adec20dbc | -20.56489 | -43.74542 | 2025-09-12 03:40:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 22717c9b-16f9-36e8-b7b0-5491211b72d8 | -19.60939 | -43.57685 | 2025-09-12 03:40:00 | NOAA-21 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c203f8b-ac02-379a-927a-87e4a8079bf5 | -21.94414 | -47.56507 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bffe8f53-a602-37bc-bf17-6c33c3731d44 | -20.66932 | -44.25928 | 2025-09-12 03:40:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 707400f2-bd07-3f1e-ac2a-d3e5bc4a3588 | -23.10461 | -47.49858 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c2a3c39f-30d5-3adb-8384-273557f2f47d | -17.34993 | -46.68233 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 099fe9aa-4aef-3773-9b44-84d74dda0e7e | -21.19334 | -47.51776 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 57.4 |
| bbe2658d-4101-314c-b244-2b800b6a04fb | -20.23618 | -49.25605 | 2025-09-12 03:40:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 38.7 |
| cd9424d4-36ce-3290-a114-b273d28b4872 | -18.65492 | -47.6659 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af69d7d5-7204-3729-9fed-8c6dd7931d4a | -19.99274 | -47.644 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57cd8097-7bc5-3017-a738-ec14825594ca | -17.82222 | -46.72799 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a9fef5a-2c4e-3275-aa15-e1e8a2bd3f99 | -21.96276 | -47.55756 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2a8f2cd-75e2-30df-9ba5-37b43183ad08 | -22.86086 | -46.56234 | 2025-09-12 03:40:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| daf8ec26-3043-30a4-98a9-863ede2bc1af | -16.41745 | -45.68568 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbbac9b5-5564-3126-aa48-03281271b555 | -17.35547 | -46.68364 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 979fe48b-0d84-37cc-ae63-d67376e604b4 | -23.10237 | -46.67587 | 2025-09-12 03:40:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| c2fe37f7-4a04-3bb8-b89d-dd1e3a798394 | -19.86631 | -44.93185 | 2025-09-12 03:40:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c2b12179-4750-393a-ae63-77445f7ca97c | -23.10172 | -46.67891 | 2025-09-12 03:40:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 79fea37e-fc4b-36d5-8a92-27d49a7cb6dc | -22.84966 | -47.33916 | 2025-09-12 03:40:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c348d232-6e1d-3907-900f-debb77d50764 | -17.95448 | -46.93756 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea23a059-e4d4-35c8-bf44-c1cac76091b8 | -21.38459 | -45.18843 | 2025-09-12 03:40:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7fd13150-35c8-30a4-97ff-13c1c1e0ae3f | -16.43895 | -49.0295 | 2025-09-12 03:40:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee3e020c-053f-30b2-932d-b65fdb33f0e2 | -21.95204 | -47.55508 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d5b58f0d-eeb7-3155-9b8f-1f94361b951f | -20.27895 | -42.88629 | 2025-09-12 03:40:00 | NOAA-21 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6bcf1604-8b56-376e-941b-60fb434adc1c | -20.35028 | -48.39995 | 2025-09-12 03:40:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3bf8e4c-8652-33ad-ac27-4bfa078897a7 | -21.70665 | -46.25602 | 2025-09-12 03:40:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 34ca7455-c46f-372d-b759-ca84b76a8862 | -19.97364 | -47.59777 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cc9b9f6-4b40-372b-830e-4ac7b5c7db5f | -21.18593 | -47.52947 | 2025-09-12 03:40:00 | NOAA-21 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 26.6 |
| fc604c86-cf4d-3ffc-9d3f-a6a092b413e6 | -20.26775 | -42.12881 | 2025-09-12 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 8f3fe3a8-6237-38ac-8b91-86f4fe50b19a | -22.61522 | -46.41819 | 2025-09-12 03:40:00 | NOAA-21 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 39a99b5e-66e6-382a-8728-7d6300d9f342 | -23.28649 | -46.47889 | 2025-09-12 03:40:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8c5f32d5-02ea-3959-8588-d065c7948b28 | -16.42589 | -45.69878 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20e2dc9d-fc84-3896-a1e0-093b57711584 | -19.19694 | -48.00859 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11c7c9e4-4c70-3385-afa5-ee0cd4310753 | -15.86857 | -48.34023 | 2025-09-12 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a26522a2-c105-3161-b8f2-67b458e81053 | -20.29848 | -46.57113 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b64b3a8-9184-3e64-82e4-b5f80565bd3c | -22.18383 | -49.60337 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c23338c0-3b54-36d6-b4b7-87209c61f145 | -17.35755 | -46.70113 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 696ff52b-1b4e-3b25-b254-cb0226ee5e9f | -21.32108 | -45.01353 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 77f60764-4bf3-3377-8b2f-6a54d2ed7184 | -19.24344 | -48.04153 | 2025-09-12 03:40:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0c084203-712a-3889-abdc-e1187e3b74cc | -22.71362 | -43.73119 | 2025-09-12 03:40:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6e0b849-13b3-38c4-a8a7-a73d9eccfedd | -21.97348 | -47.56011 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 40c79c07-4643-3a3a-a33c-4108146e939d | -20.00184 | -46.92712 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b08a09e-b70a-30a1-9486-841b8de54c3a | -20.00795 | -46.92494 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a714052-b776-31ec-891b-cedf74ccade9 | -18.54442 | -48.41223 | 2025-09-12 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| d39a0561-7b11-3b9d-aacf-36301611c8a6 | -19.84312 | -44.58677 | 2025-09-12 03:40:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 97a9144d-1508-397b-8751-33ec61ded71f | -19.88391 | -41.4194 | 2025-09-12 03:40:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4fee5c27-f66f-3f42-91df-74ba9c51b007 | -20.91274 | -44.61457 | 2025-09-12 03:40:00 | NOAA-21 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README28.md)
