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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5af683f1-5cf7-3035-9904-7543e54c0278 | -16.62591 | -40.53043 | 2026-08-28 16:05:00 | NOAA-20 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 414f3c18-3f76-3475-b607-0ad95541ebe8 | -5.96153 | -44.80077 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| aee0d14d-d29c-3427-bd48-bc6853e3d1cd | 0.41731 | -51.11509 | 2026-08-28 16:07:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ea6677e-bb4a-34a1-bbc1-7eeee08f0728 | -0.71496 | -49.04696 | 2026-08-28 16:07:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09704487-37a4-3d2a-8e0b-9c0d5b03fa1b | -10.92312 | -46.62563 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a6dc471f-f9c0-38b7-98ee-6769b0b58f92 | -10.07195 | -46.95081 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e57ca24-2614-3f4e-83ef-0dac6612205b | -11.83884 | -47.22618 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 51d82850-e144-3fb6-a47d-229a8759df1a | -10.55929 | -46.41912 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2f168a04-db39-31b7-980c-e5ca1ed82138 | -9.87092 | -46.34314 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c4349916-ea36-3e36-9d7d-8defbc544ab3 | -11.84272 | -47.2091 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9567f74c-0f54-3c37-a0b6-f425a6d0c185 | -11.15674 | -45.57952 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 64853767-de13-3b33-ae46-45f6c7b873f5 | -9.50525 | -45.64933 | 2026-08-28 16:07:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 83f87e39-b6ef-34f4-a539-b22e0160fc30 | -9.87314 | -45.85861 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| abce94f1-03a5-361a-a519-5c9ed4774642 | -11.07419 | -47.11538 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 38c3623f-98dd-3123-b110-3dfbe88ed49d | -1.57911 | -47.74204 | 2026-08-28 16:07:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| b3b34feb-51a0-3f3e-91a5-a7cfe2db2240 | -10.07149 | -46.94715 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 257963b9-e6b6-3f18-812c-0f849e221645 | -11.34932 | -48.38655 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 81214983-9837-37d5-acb8-b0b7fe11bd22 | -1.69072 | -47.42392 | 2026-08-28 16:07:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| db19299e-f055-37de-a8c3-56b465a3200e | -9.79319 | -43.56372 | 2026-08-28 16:07:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| d3e094ae-9ea7-3234-abfb-f79858ebe905 | -10.90264 | -46.64608 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4fdcc57e-683a-3693-bd80-87cf5b0a92e3 | -10.08177 | -46.98344 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5184c8aa-7750-3187-8599-d066d0d31139 | -9.61706 | -39.31616 | 2026-08-28 16:07:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 6017cad9-47cd-37c4-8605-d94888c081a3 | -10.55398 | -50.42621 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f956744f-8807-3a24-adaf-5655e84b7f05 | -10.08367 | -48.6938 | 2026-08-28 16:07:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 93a826ed-1a87-3b9b-811a-255a86c9e4cf | -12.05162 | -47.18018 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7bc1ed18-91b4-3c15-841e-c79d743cc37e | -11.79389 | -47.65465 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1b5a1fab-14fc-3a89-ad5c-f2cb65cf708c | -11.67469 | -46.73048 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f0c76428-f1ed-3f82-b6e5-bc5026dc5b09 | -11.26473 | -50.70348 | 2026-08-28 16:07:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f9a8f384-a385-3247-b8de-bfc6562541d7 | -11.67096 | -46.73468 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de09baa1-6a31-3c5d-8240-71e41cbe448d | -10.90291 | -46.64297 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4ffada25-84bb-3da6-b0ba-e82e76f8c839 | -11.77557 | -47.65238 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 513e4589-06df-3d81-a7da-9a3f42aab256 | -3.96431 | -40.70502 | 2026-08-28 16:07:00 | NOAA-20 | PACUJÁ | CEARÁ | Brasil | 2309904 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9cc2f250-3c26-36c1-addb-8e687793f861 | -11.35611 | -48.3908 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 61ba50ec-ea7c-3254-874c-db5578e7d989 | -11.24312 | -45.05957 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 282df806-65ff-36d5-854e-78d442115d1d | -10.88537 | -50.51072 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fe9e766e-ffb9-352e-b6bc-caeb7f579806 | -2.7287 | -47.04315 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| fb66e5f0-1ad2-317b-ab20-e630d23aa9cd | -10.34691 | -50.39178 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e00c02a5-99dc-369f-bec0-b5fea387c8c8 | -2.72457 | -47.04966 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5583a62e-4fd7-3dc9-9c99-a8bfc25c6a95 | -3.43736 | -40.6431 | 2026-08-28 16:07:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4b288720-1720-34fe-8a94-b1d05648a0c6 | -2.95524 | -43.24788 | 2026-08-28 16:07:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| fa8d3e04-8bb0-38eb-ad26-d01189626b70 | -10.55632 | -46.41912 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7d910023-e8b9-3b25-b0df-09d6db2cebc7 | -1.96605 | -48.37681 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6d4faa33-32c8-3c7f-a997-fb7198d3f910 | -9.88343 | -45.85738 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 08054777-ae62-368e-8dc1-3f5a62710c23 | -3.45697 | -43.36097 | 2026-08-28 16:07:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 09448cc2-104d-300f-ac47-ba47d54c49da | -11.23102 | -45.04414 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| caab4857-54ae-3791-a31e-47eb0c1d93d1 | -2.72543 | -47.0567 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 05f46fce-6b4f-3d28-a0c9-20c89c306617 | -9.86681 | -45.84991 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c68703c-b1d3-3906-81dd-2e05892a349d | -10.03283 | -45.82116 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 007f3001-b020-353e-9c10-a4583df4782d | -11.24745 | -45.04588 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4eeeedf4-136e-335c-9528-789fd786f10a | -9.88777 | -45.85052 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 17d70f34-decc-3da0-a59f-f3d151a17565 | -11.56429 | -50.6615 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 565d6d73-2531-3a9c-986f-ac136185ebd2 | -11.79832 | -47.67035 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9c07bdbd-1fff-34b8-9329-ce055f15be4c | -3.92859 | -44.91133 | 2026-08-28 16:07:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 51caa37d-d5c6-3c18-9b59-f91e8cac8ffb | -9.87234 | -45.8523 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| acf61d10-511b-33be-9c98-ca7410e761bd | -10.17876 | -46.86343 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| befd3201-447e-392a-a918-f2c617aac522 | -12.22616 | -50.54514 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8da948ae-2079-3514-a310-3e629d21b3d2 | -11.83778 | -47.2243 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2fb133fc-2cf9-35cc-94ba-7114f2829c2a | -10.56127 | -46.41485 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e63fdd1a-cfbe-3517-9fe8-987368a76697 | -11.78113 | -47.62818 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b7673667-2aba-3f7e-9db4-5b52eecc3a63 | -11.07092 | -47.11627 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5878dd04-f5b7-3ba4-905d-38a33a2bdb57 | -12.08483 | -47.16344 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 42569c5d-8295-37fb-bc50-4ffb55ad26cc | -12.31259 | -50.57269 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| ca298b0f-4b29-3265-b580-5bccc20bfc3f | -9.79642 | -43.55458 | 2026-08-28 16:07:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 49d709ef-d752-3e13-b117-880c16eb8dd9 | -10.07242 | -46.95448 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a3c755f-3dc8-380d-9893-0e45ff72a5bb | -9.79901 | -46.32855 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53558138-c3e3-324d-8618-b1d816307076 | -12.03474 | -47.1863 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e7d56040-cde7-3f7f-ae99-d6254da63736 | -11.22608 | -45.04482 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 080b0065-0f15-3d18-983b-cd3a3162f24f | -12.31151 | -50.59735 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 4ee78a2a-af84-3a16-8642-72f05b9ee67a | -12.26685 | -50.54918 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.7 |
| c2223fe8-90ac-3791-a61d-3f608b64ae81 | -11.41006 | -42.30677 | 2026-08-28 16:07:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 9b0af057-dc3b-3dff-9a9f-4eff2858db9c | -11.84319 | -47.21316 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5963df0c-39c0-300d-b74b-6c17e855a5a7 | -11.23743 | -45.05465 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 09a2b85b-a2c5-3d31-a4c8-4ca60eb14697 | -12.32048 | -50.57898 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 60ee2e4f-682a-3de2-9846-fae02e2916eb | -3.59695 | -44.86147 | 2026-08-28 16:07:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 58bee990-42fc-3b76-9acb-d31bebeae712 | -9.85788 | -45.84005 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 84e72739-0a91-38ed-9afd-361adc84a580 | -3.53913 | -48.17705 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 766cfcd0-76dd-37c5-8af0-18e69c6a7f51 | -9.88197 | -46.34507 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e8562546-9ed8-3909-a160-9ee507bac0e2 | 0.18275 | -51.43925 | 2026-08-28 16:07:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a567ca90-a2e5-3dfe-a960-3bceb031b079 | -11.65848 | -46.7254 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 72ac15dd-8176-3030-a5d6-65505f9d84c2 | -2.72919 | -47.04731 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8b7b0d00-9d06-3b5e-a6c3-8be3bf05d512 | -10.01873 | -45.63489 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e955f79f-01a5-35c4-807f-8ccad30aca7c | -9.01595 | -37.57742 | 2026-08-28 16:07:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f7b94950-2c08-3069-8110-395dda28d148 | -11.35534 | -48.38948 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b361e773-f5ea-3aea-9d4b-8a466288303b | -12.05786 | -47.18347 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 57b11981-d0bf-37e6-ad9a-632dc4c7f4c9 | -11.08038 | -47.11877 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b6dfca3c-9af8-3dff-9aa2-4b42ba97378a | -9.87631 | -45.84252 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c328b3cd-67fc-3b32-8048-4219e3835119 | -2.72793 | -47.03859 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6396770e-4d2d-397d-a75f-7d141892acf4 | -9.87788 | -45.85483 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 534dfb76-a36e-360e-b336-6d1dfccdca8c | -2.72961 | -47.0502 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 10179a6f-c739-3bbb-8b9a-71908a1ba57e | -9.38212 | -38.27323 | 2026-08-28 16:07:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e068ae9f-ec66-31e4-a5ef-05cc55074959 | -10.17737 | -46.85264 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17a3493a-c1d6-3c57-853b-394471f71dec | -4.05062 | -38.30849 | 2026-08-28 16:07:00 | NOAA-20 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9c34b781-751b-30fc-b72e-1be1a972dbca | -12.21195 | -50.54667 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bd9483df-4830-37c0-980d-c5f930357728 | -9.85975 | -45.8353 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51f536b0-8527-3398-b83a-70036aed6478 | -1.58474 | -47.74442 | 2026-08-28 16:07:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| d4e1e18a-d40c-3a3b-9afb-758469f52249 | -10.76676 | -50.6404 | 2026-08-28 16:07:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6c8523a9-e0ed-30db-86f2-230307a283c3 | -0.94617 | -47.17493 | 2026-08-28 16:07:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dc0ae319-eed2-38ca-bbbc-ce56975e7f78 | -2.72293 | -47.03932 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b8a199f9-7e51-31b8-aa85-5e3a6361259a | -3.43393 | -40.6436 | 2026-08-28 16:07:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 9e39b0c5-a040-3d48-aaf6-f8cd76d61ca3 | -11.66355 | -46.73212 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README95.md)
