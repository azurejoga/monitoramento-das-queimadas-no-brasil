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
| 86db70c9-1a95-312b-bae5-68b8c253365c | -4.83199 | -55.77285 | 2025-08-22 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 735898bc-9539-349e-9ef7-83003cd53dd4 | -6.9269 | -44.39238 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c04b9cd-5adb-30d6-af25-50672c6d8607 | -5.88885 | -53.63395 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a766169-6d93-36f3-aeba-3dabb1bc55b2 | -10.87121 | -50.84858 | 2025-08-22 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90fbee5f-b770-3aa0-b257-6904297cc6c4 | -7.61164 | -44.37844 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e62febb-f1c3-378a-ba06-92e619976f60 | -6.11313 | -44.385 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31597774-2bf8-394b-a844-0bd3cd13a510 | -6.74236 | -50.95546 | 2025-08-22 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da625475-0c98-30a3-a1aa-5984f709c067 | -6.57939 | -44.72421 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01cc564c-80bf-3b6a-bebd-176de41541f7 | -6.57445 | -44.73406 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87a9d58c-80a3-34c3-83ea-e993415da48a | -9.63133 | -48.33386 | 2025-08-22 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b697bc0-d6fd-38bb-8b08-6d27fbd6c8eb | -6.11205 | -44.39192 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3ca3d54-68d0-34ba-88c1-d3784c017388 | -9.63774 | -48.33921 | 2025-08-22 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d736696-8057-37f7-b62a-108b16de6844 | -6.17685 | -44.73491 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2038ff2-f545-32a3-bf3a-9c005832938c | -5.52663 | -46.42038 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49293c6d-ebfe-360d-8b3f-d3e81773ee82 | -7.63588 | -45.23965 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cc4c3545-78c3-3c9f-9b8f-4519edb047e9 | -12.91987 | -41.57067 | 2025-08-22 04:19:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a0f4941f-a59f-3d4b-8045-aa64ea1c3cb1 | -7.09352 | -44.56412 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6151ca81-dd82-37fd-a1c5-a501f096accb | -5.56283 | -45.56348 | 2025-08-22 04:19:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cf972e1-7ad4-320d-92fc-352c945d187d | -10.27108 | -46.75916 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4d4126d-1aab-3c76-9621-d055ad4adf42 | -11.28105 | -48.90037 | 2025-08-22 04:19:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b90dd49a-74fb-3e56-9896-46ed82d8caed | -9.15123 | -59.60575 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8578be9e-8242-3391-ab7c-c6a0d6fb5fa8 | -6.63583 | -47.90479 | 2025-08-22 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| fff2b182-4fdd-3e09-a6ce-2b72de8f1d9e | -6.9855 | -44.1477 | 2025-08-22 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30b3759c-ab46-3ff6-b057-14cfb72d2bc5 | -11.99744 | -44.67132 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fa6eed2-119f-315c-a303-8795e8a8e438 | -5.7938 | -45.07423 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8f2ac9a5-d3c8-3c4a-92e9-e3a61673613c | -11.81545 | -44.25174 | 2025-08-22 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0506ee7-6754-38a0-a77b-814f65550176 | -11.30236 | -48.15665 | 2025-08-22 04:19:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11f03913-9183-33fa-a10c-32ac9fe48559 | -11.998 | -44.66768 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c45046d4-c71f-31dd-b68e-bd84ac75e38a | -7.03793 | -44.61576 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b450a43c-7a42-3c82-97d2-2b8cdbf0b723 | -11.05955 | -46.07949 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 804cc4d5-3fb5-3c13-b4e6-e0a3fdff4ef9 | -5.88167 | -50.15414 | 2025-08-22 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c501449-6a20-3412-95ee-d5c02fd8e34a | -11.43565 | -47.31686 | 2025-08-22 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dc5fa55-7e67-3f29-b140-ba83db9e8112 | -12.52365 | -45.59901 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10ced0c1-7731-337b-ac34-cc4641477e28 | -5.52992 | -46.50822 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f62ec9d-0919-3245-8295-12ddd90b424a | -10.98171 | -45.60373 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c7901e9-3c04-3541-a567-d99d93d7c9a6 | -7.63919 | -45.24017 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 63bddad9-0b43-36d4-9d36-d7458244bd59 | -7.24147 | -44.79015 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57ccb61d-1c25-357e-a70d-946e5bddf09a | -6.2519 | -53.68507 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 690573e6-587d-3b05-a0ea-6145ef54e29a | -6.10874 | -44.39141 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d01f382-c09f-3b52-8e3b-82396cd7bb4f | -10.27167 | -46.75551 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 577d9685-b9c3-3b95-999a-e70b4b86f39e | -8.12356 | -47.1473 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3684ee96-2f20-32d4-aac7-156b7cadf9ca | -10.97001 | -45.61325 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fd0d6ba-3107-3f91-a174-7698c3eb7a2f | -6.51116 | -44.57534 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6263fefd-9042-3e72-b088-37896bbdc7d9 | -6.00138 | -42.80547 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9472b8a-2b43-3c66-bc22-ea370042d0ff | -6.58215 | -44.72819 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4e0d9ad-9706-3452-a511-cd0551257506 | -6.65694 | -44.40316 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d3ac09a-3502-30bc-86b8-769bd07504f4 | -6.03459 | -44.36525 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3077aab5-fd00-31af-a3ce-487595d90e4f | -6.49074 | -43.44561 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e671ac01-79f9-3e62-9b04-b91cdd1589f3 | -11.28501 | -44.94412 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6af9144b-ab7d-33a6-995a-c3ea2e8fb1c4 | -5.56226 | -45.567 | 2025-08-22 04:19:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65a696bd-ce42-3fdd-b01c-384691b85faf | -7.1586 | -43.22756 | 2025-08-22 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bcbc8309-7bc6-3d2a-b8d3-9b93309aeb55 | -6.53226 | -45.45165 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d1f0a6c-6823-3edc-b8d6-7e92a0a2bd37 | -10.72444 | -48.23423 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f8a670a-2552-3320-8f24-457aeaee4050 | -8.27314 | -47.53783 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4332b283-8bf6-39de-9987-ebb0463b1f4b | -12.0081 | -44.66928 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11faffcd-7244-35ca-9a4d-9ed77a0d8e7c | -6.42826 | -41.85337 | 2025-08-22 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd165dea-ccbc-3043-a378-d18719adc60b | -7.26823 | -44.05569 | 2025-08-22 04:19:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fe8b69b-c0b8-322a-89a6-81aba3ca6f15 | -11.92175 | -50.52082 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3f7fd46-ec4a-3f58-ab95-1b269d1c5700 | -11.31479 | -44.94501 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0fb8828-c833-31ae-8d5a-6ecd7242bca1 | -7.16614 | -44.6647 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 272cfed3-6b1b-3dbe-bceb-ebe4136ad70d | -7.15622 | -44.66314 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f3c950a-324f-3901-83bc-1f5c9d417cca | -6.52136 | -45.88211 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22903ebb-9226-325d-a6de-37a0b61fb2c5 | -6.26387 | -53.67919 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0abccf0-f3aa-3388-93b1-be87e259ef4c | -6.55254 | -45.51594 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 005ee3cd-ac8e-38ff-9ab9-5ffea26477b6 | -6.5707 | -42.99685 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dda4abda-f2e3-380d-b1f3-c65c14491a46 | -6.00081 | -42.8092 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 48a24341-ead6-3830-9dc9-fb487424a493 | -6.04805 | -43.9977 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2ee8919-835d-3e96-acfb-a06e5b8dd302 | -5.88472 | -53.62653 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66ab15d8-664a-3577-a73d-5b5d376ec335 | -6.44601 | -53.38084 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 844afc14-4f4f-3aa0-aaf5-b04efc894ac6 | -7.60831 | -44.37793 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8b27d9f-2804-37f9-96f2-26d391c5aa94 | -8.47502 | -48.24904 | 2025-08-22 04:19:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b28fc2e-ef29-323e-a3c6-b12066ba1976 | -10.72857 | -48.23096 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78e9f50c-32c0-3806-b8c1-b6c4f5489eec | -6.29417 | -43.70255 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6231d52c-7027-3189-80fb-884eaebc2791 | -5.63207 | -45.83179 | 2025-08-22 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfe03879-d2aa-3ccd-be7c-68f1d27db0e0 | -9.18497 | -59.6341 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 316f1ef1-6017-3fcd-9f6f-ef39c28aeb8f | -10.8644 | -50.84002 | 2025-08-22 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1057351f-70f2-3710-9991-1da6e174d96c | -7.72135 | -44.09002 | 2025-08-22 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb32750a-db71-3eeb-a9b9-baf5f8454a23 | -5.87991 | -42.41123 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e03e4575-8569-332a-aebb-f2d28ea748a5 | -6.50234 | -44.84661 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ba6fa58-02eb-3c89-a310-eea121c0d09b | -7.09732 | -43.69163 | 2025-08-22 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a2b95c0-0313-384d-90d1-551d68340c08 | -7.16175 | -44.6711 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52b0faa3-f941-3f90-8d12-cc25024b733f | -11.28668 | -44.95536 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f89be9b-8665-38d4-8d42-91786fb9f050 | -5.75168 | -52.32111 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| df6c590c-8f7e-3e85-b760-37a11a0f6da3 | -10.28826 | -46.78031 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e71c21cf-6ebf-318b-bd37-8638baeb3695 | -7.56866 | -44.3929 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8af44f54-028b-320c-bb62-79ec56be79f5 | -7.63864 | -45.24364 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e36ae0fa-ed28-367e-bebb-8de5dfc3fb84 | -6.50622 | -44.5852 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a04d7ca9-b8d3-3767-8ef9-53f103718311 | -8.83603 | -52.03326 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1b0f7e7e-0f2f-3490-bb63-cce5c4b5a57b | -6.04507 | -44.36334 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad9bb843-68ad-3c60-842b-016ce2556eea | -6.11368 | -44.38153 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c6bb2b0-3ebd-31ed-9bf9-299f5c2706fb | -9.87046 | -44.69653 | 2025-08-22 04:19:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c111bf53-3d3d-376c-b2c1-7131cadb7b5e | -11.312 | -44.94092 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eadc3d7c-985e-33d8-997c-d345e4794a3e | -6.16103 | -53.77153 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d111590-e386-3a77-b7a9-0728432c2724 | -6.03097 | -42.84029 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e6b36987-98fe-345a-a069-0158cf141e12 | -6.03845 | -44.36231 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78fec9d9-899c-3981-8629-0111dfbf832e | -9.82244 | -45.95492 | 2025-08-22 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3483b4e-b6b6-3e34-ab5f-9057423a0291 | -7.8597 | -47.0024 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1690fe40-b7b8-3a87-97e6-4f915a573154 | -0.74993 | -47.75059 | 2025-08-22 04:19:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f48b807-7861-35f0-a98b-ed5aa14e4770 | -6.01918 | -44.377 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b81b5082-9c70-319e-9d10-9a909f68ee51 | -6.56445 | -42.99212 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
