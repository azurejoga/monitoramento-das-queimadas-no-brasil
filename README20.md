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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7263d832-8a09-3220-b750-b4d88a70793b | -2.86441 | -41.75962 | 2025-11-10 11:57:00 | TERRA_M-M | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ac1ed53e-013c-348d-a136-2dbc5d2343a8 | -4.71532 | -42.94942 | 2025-11-10 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9df14be9-2250-3f48-88f4-07cb3d081a4a | -6.16743 | -38.35534 | 2025-11-10 11:57:00 | TERRA_M-M | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 4c705fd1-b51c-3a94-96d7-c2dbe35cfe6a | -5.72118 | -42.18346 | 2025-11-10 11:57:00 | TERRA_M-M | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 4fdfe8d6-cf00-3e75-b299-0c3c55da0495 | -6.59003 | -41.38639 | 2025-11-10 11:57:00 | TERRA_M-M | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| af7df8ac-79fd-3cdc-9871-025a61e4ace5 | -6.92586 | -40.8245 | 2025-11-10 11:57:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 72112789-10f4-3657-a8f1-5eb71e5a6cc9 | -5.1707 | -38.57273 | 2025-11-10 11:57:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 5cc35013-a512-3000-a522-344bcfd19fe7 | -3.08165 | -44.73718 | 2025-11-10 11:57:00 | TERRA_M-M | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1e4ae534-43f0-3e84-a8e0-eaa0bcec1fd5 | -6.35873 | -41.06312 | 2025-11-10 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 4ada26ba-f132-384f-94df-18cef5f4c6e8 | -7.52825 | -37.59024 | 2025-11-10 11:59:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 214.3 |
| b8c76745-58a5-3cca-9a4d-470d15828cdf | -11.88168 | -43.81605 | 2025-11-10 11:59:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6f24893b-b2ae-3203-8527-0e85c52730ca | -7.60692 | -38.82936 | 2025-11-10 11:59:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 16.3 |
| c36956f1-3fe9-348f-b7c0-741f333d04f4 | -11.90812 | -43.81984 | 2025-11-10 11:59:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2e5b6341-831d-3ad1-9760-b8a8bfb79702 | -10.99137 | -42.93919 | 2025-11-10 11:59:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 9dad8f93-73e6-3855-8aba-afb9f4e99faf | -15.7253 | -43.49075 | 2025-11-10 11:59:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| cef5b6d8-baf9-3b0b-8ecc-c82ed7901510 | -12.2938 | -38.22711 | 2025-11-10 11:59:00 | TERRA_M-M | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 3a85ca2f-4194-3cd6-951b-aa31dc79d1a0 | -10.40149 | -43.19783 | 2025-11-10 11:59:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| aebaa26b-f877-3345-8e32-79fab98af0c1 | -7.54029 | -37.59144 | 2025-11-10 11:59:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 49.0 |
| 733b4635-019a-36a8-bd5c-4eb0972bcfe0 | -14.24673 | -46.86801 | 2025-11-10 11:59:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 34e57436-f04b-382a-9ded-d48b52b92050 | -11.94676 | -46.26295 | 2025-11-10 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| fbf94a70-7843-3fb5-a356-d9109a84adca | -10.40022 | -43.20681 | 2025-11-10 11:59:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 88.9 |
| e097dfcf-38d9-3265-8276-52a81e5db438 | -7.52598 | -37.60809 | 2025-11-10 11:59:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 0acfb819-46d7-3de1-b4f6-5e1c8e96ad13 | -15.73568 | -43.4824 | 2025-11-10 11:59:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 23574233-0beb-3ec0-baf3-b25a55ccb74d | -10.5047 | -43.3104 | 2025-11-10 11:59:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| fbb81e75-8a4b-3b4b-b164-c9276cbc76df | -11.87286 | -43.81479 | 2025-11-10 11:59:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| a1892759-13bf-30d0-b792-d61c46727fd3 | -14.13203 | -46.91098 | 2025-11-10 11:59:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| df021eee-cb1d-3d11-afd8-c36bc537c0ab | -10.99009 | -42.94833 | 2025-11-10 11:59:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| edab7786-9476-3a18-a651-a313589bdfaa | -7.78479 | -38.01173 | 2025-11-10 11:59:00 | TERRA_M-M | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 23.0 |
| d07cde83-cb8d-39f7-b854-740b1f3e420a | -14.24831 | -46.85778 | 2025-11-10 11:59:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| fa808b23-e292-365b-87e3-fc6248d42c0c | -13.38964 | -46.55644 | 2025-11-10 11:59:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c3817371-0e20-3fa7-b5ed-f95386954024 | -10.39895 | -43.21578 | 2025-11-10 11:59:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 91.6 |
| d064c247-dc4e-3bf0-8db6-7d9ca1b398fe | -10.50255 | -44.92862 | 2025-11-10 11:59:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| fa729228-3338-33a5-ab4a-65fdbd88d387 | -10.46409 | -44.94178 | 2025-11-10 11:59:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f56d556b-e22e-3153-ad33-c7c733ee7c8e | -10.50343 | -43.31935 | 2025-11-10 11:59:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ed2d0397-5fe0-3861-86d6-9d6b0e7ca707 | -9.55105 | -42.95829 | 2025-11-10 11:59:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 03d3c75a-5834-39c7-b449-9c2c5309f091 | -9.8072 | -41.71887 | 2025-11-10 11:59:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 25.4 |
| cf716de1-8c8b-36ba-aec9-87c6f1333567 | -9.81496 | -41.7159 | 2025-11-10 11:59:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3a70d6e0-1b87-36ad-9d66-229d37623dbd | -7.91609 | -40.38892 | 2025-11-10 11:59:00 | TERRA_M-M | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 20.5 |
| a5231a23-4a69-337c-bffe-1ea20841f9df | -7.07684 | -41.66231 | 2025-11-10 11:59:00 | TERRA_M-M | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| f27b4dfa-d909-3efd-b0b5-486b7baa54f7 | -15.72662 | -43.48112 | 2025-11-10 11:59:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 27f8fe80-d882-31cd-9b64-b3be0a88c0d7 | -11.16928 | -43.57308 | 2025-11-10 11:59:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| df50b8d8-503e-38e2-b569-4ae87a5979fc | -13.39118 | -46.54634 | 2025-11-10 11:59:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c92d5eed-08c8-3d24-8526-d900a720fcf7 | -7.60502 | -38.8434 | 2025-11-10 11:59:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 54.7 |
| e112a37c-c4ef-3d0d-9112-e00867dbaba9 | -10.5012 | -44.93781 | 2025-11-10 11:59:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| c1be9ed1-d6a3-39a2-8382-e0b7002e9c3c | -8.5783 | -40.6203 | 2025-11-10 11:59:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| e9e9c70b-38da-3260-9931-f7af64e54c50 | -7.37566 | -40.83334 | 2025-11-10 11:59:00 | TERRA_M-M | PADRE MARCOS | PIAUÍ | Brasil | 2207207 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 6500f9ff-f797-3b4c-9b27-c1b64dd2e835 | -14.68859 | -46.58186 | 2025-11-10 11:59:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6c1150cd-3d0e-3ad1-97d7-14f0465bc44a | -11.90684 | -43.8288 | 2025-11-10 11:59:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ef1e1693-5217-37b7-ac3e-435385cfdc6f | -10.49226 | -44.93652 | 2025-11-10 11:59:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 61a05e4d-e1cc-36fd-8f28-e211f9c0df41 | -20.86251 | -46.97699 | 2025-11-10 12:01:00 | TERRA_M-T | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f134da79-82d1-39ea-b435-1dfbc7960825 | -22.36679 | -45.69368 | 2025-11-10 12:01:00 | TERRA_M-T | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 2f484a34-f4a4-3bd1-a829-fcfbbefc6e27 | -6.3588 | -41.0728 | 2025-11-10 12:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| a6b3ee4f-1d5d-39c4-8043-acb95439a46b | -6.3588 | -41.0728 | 2025-11-10 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 056ba0cd-bce4-3465-b003-650a12e0d3f1 | -3.9015 | -43.4328 | 2025-11-10 13:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 516566de-e7f3-3c47-951d-4ffdd89a8d82 | -3.9015 | -43.4328 | 2025-11-10 13:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 69b76e60-6096-35af-ac35-cf3efd3a4d13 | -8.6531 | -38.1517 | 2025-11-10 13:20:00 | GOES-19 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 41e20a59-414f-3a0d-b25d-fddd81cef2a9 | -6.3588 | -41.0728 | 2025-11-10 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| fbb1f549-6f91-3bd4-897a-0709dec175ab | -2.9341 | -57.7786 | 2025-11-10 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 7b73b005-0cf5-3e49-a85e-b2af207a82d5 | -8.6531 | -38.1517 | 2025-11-10 13:40:00 | GOES-19 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 131.3 |
| 8f138823-631f-33b7-8db3-d482cb985498 | -5.6059 | -41.066 | 2025-11-10 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 3138f988-deac-336a-9a4e-29f6ff90436f | -2.9341 | -57.7786 | 2025-11-10 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| e6ebd299-b09d-3dd7-b9a2-4b9a638934bd | -6.3588 | -41.0728 | 2025-11-10 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 3f1dda7a-3144-31e1-a1b7-017760cc0f40 | -6.3588 | -41.0728 | 2025-11-10 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 200.1 |
| 3a59777d-0fd6-385a-8b5f-814031655633 | -3.9219 | -43.1525 | 2025-11-10 13:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 197f40ea-c9fd-339b-9a50-74e064b9b85d | -7.9273 | -39.6212 | 2025-11-10 13:50:00 | GOES-19 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 73af21e6-c832-358d-9b31-26b11d35351a | -2.9341 | -57.7786 | 2025-11-10 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 4c7bcd54-98f1-34f5-aa36-5bcaf273a9e8 | -3.7732 | -43.0434 | 2025-11-10 14:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b0a689a0-3282-3d8d-88cd-585906f2f8ba | -3.9219 | -43.1525 | 2025-11-10 14:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d73060d1-3b63-3b7f-bb68-b35e2d2993da | -19.0319 | -57.5382 | 2025-11-10 14:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 256e3873-3adb-3b0e-8f22-da5b74b5f220 | -4.3872 | -43.406 | 2025-11-10 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 89d0aa7f-8d1e-3dcf-97b5-c29047790eaa | -3.7732 | -43.0434 | 2025-11-10 14:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 4a79b884-0999-351f-ba59-f15b7101d06a | -2.9341 | -57.7786 | 2025-11-10 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| bad40d20-0099-3770-9cfd-59a7e2bff328 | -3.9219 | -43.1525 | 2025-11-10 14:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c97cf379-c8d7-33b0-ad70-6c42c9954538 | -3.9219 | -43.1525 | 2025-11-10 14:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| fbc5ea47-5042-39ba-975c-4e45dfabc116 | -2.9341 | -57.7786 | 2025-11-10 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 39774da7-df30-3a41-ba7f-915231a92caf | -4.3872 | -43.406 | 2025-11-10 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 620fa71b-d678-3f11-8353-e3f3dd87fe85 | -4.4633 | -43.2152 | 2025-11-10 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ef97b962-6628-3c1f-8a7d-7d7e0cb1cd7f | -19.0319 | -57.5382 | 2025-11-10 14:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 97.7 |
| f106ce8c-eaac-3d0a-bf8a-a090a90cf72f | -4.3872 | -43.406 | 2025-11-10 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a06e6f87-28ba-3a19-a4ec-d6bb4adc3e7e | -5.475 | -43.0774 | 2025-11-10 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 42040686-2ee8-3009-a301-65b18f7c3df3 | -5.6248 | -41.0645 | 2025-11-10 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 93a25260-07eb-349f-a516-5d1f33d0cdf9 | -19.0319 | -57.5382 | 2025-11-10 14:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 095ce26b-81e9-321d-8e99-61fa0b985715 | -2.9341 | -57.7786 | 2025-11-10 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 7aed1762-3078-36ac-bb39-aa2c42a9978b | -4.4633 | -43.2152 | 2025-11-10 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7d71a071-3af2-332d-bf35-39983e2d5b93 | -2.9341 | -57.7786 | 2025-11-10 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 0ba1dbd4-4ab0-3e70-844b-0006de5152ca | -4.2264 | -42.3367 | 2025-11-10 14:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| f3aa3702-846b-3ca7-9f40-e39700c2973d | -4.3299 | -43.595 | 2025-11-10 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| ed599848-811c-32d2-acf3-79eaa693c6be | -4.4633 | -43.2152 | 2025-11-10 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| a0f04156-b8f5-3159-a05f-40589d4805c4 | -19.0319 | -57.5382 | 2025-11-10 14:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 104.8 |
| 3983a86c-a28c-3a88-91a6-63485176d877 | -4.3872 | -43.406 | 2025-11-10 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |


