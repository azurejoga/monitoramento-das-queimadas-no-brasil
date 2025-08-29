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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50810b62-5ab7-3174-8a75-712771d35618 | -13.00865 | -56.9187 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc5c2278-6e5c-3431-97b2-d22f42487522 | -12.43996 | -63.91463 | 2025-08-29 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d11313a6-b9d3-3682-b8bd-c3a98ab96f50 | -14.31345 | -51.89536 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea2a0a35-8aa9-3a0d-81da-eb4dbb0f0463 | -13.58543 | -46.86845 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca11a70c-58ec-3fc8-9a9c-c05b59f1f9bc | -17.75362 | -44.49763 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64ecdf7b-edfe-32d0-83d0-503a57e3e576 | -14.60194 | -54.5018 | 2025-08-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e29135f2-a7cc-32a7-9663-0e23398d9dc3 | -13.41566 | -46.84505 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d37c1e99-f1bd-37a2-bedc-fe15552982d1 | -13.37573 | -46.87918 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5b6242a0-3b68-3308-88a7-842e6bbbc1b6 | -13.53725 | -46.94505 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f8e1684-2959-37fd-bff1-d52d082230b8 | -13.40843 | -46.98193 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| af7e052f-92dd-3466-a134-9d89a33f1c79 | -13.52892 | -46.94875 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c7627e2-3c0f-3e93-989b-0413452ea644 | -13.56004 | -46.92191 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61563c86-6bd7-35ad-9f8c-66280df3ceac | -13.47635 | -46.84669 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f3684fdd-4e56-3c49-aeb3-0bcd8013ce14 | -19.40212 | -41.44595 | 2025-08-29 04:42:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 92193bfd-ff99-309d-89cb-fbdaceaa6fdb | -13.00587 | -56.91012 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d514b0b-245f-32d1-babc-a2ccb1a8aa2f | -13.68425 | -46.90741 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76d71484-ffc2-3655-ae78-91e9be1610f7 | -14.77305 | -59.73974 | 2025-08-29 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24abea86-38bb-34c9-9fae-84b7162c86a6 | -17.04258 | -46.50517 | 2025-08-29 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0c2f82c-92fd-3d00-86d3-ca0d6a926e99 | -19.00021 | -46.97086 | 2025-08-29 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7dc94444-8ffe-311d-b398-5fd48461b276 | -12.43218 | -63.91899 | 2025-08-29 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 152a1132-36c9-3e9a-a4bb-2cd23415b95f | -13.55347 | -46.94086 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d1191e9-01aa-37bc-a278-893ed5f4f6c7 | -12.99537 | -56.92038 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d76ca706-8bb5-3365-97ab-9a11e84556d2 | -12.99118 | -56.91967 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d191da26-ab0e-3c3d-88a0-475986e03154 | -13.41349 | -46.97358 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 595234df-182d-3aa5-a36f-1cd525e3f942 | -15.5357 | -54.26973 | 2025-08-29 04:42:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e8ba0071-d895-3ed8-9948-72977cb42050 | -15.06179 | -48.61899 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a9c16b3-df03-3d1c-a326-7676fee4d95e | -11.73091 | -61.75808 | 2025-08-29 04:42:00 | NOAA-21 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 03ccae62-deeb-3268-8f75-2b05ae3b5ee3 | -12.6323 | -60.24213 | 2025-08-29 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2021eb2d-8c71-3ba6-a522-60f6e47e0db3 | -13.62593 | -48.24835 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b798edf-8e7a-3920-a9a7-a362c28bebfd | -13.96981 | -46.33789 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6b8dc32-4ae0-325f-9e8e-90d80d7bf355 | -13.43203 | -46.95252 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c17c71a9-d1ba-3e83-8ef2-3285bc424e75 | -11.38087 | -63.26799 | 2025-08-29 04:42:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a51aaa0c-e2bd-3a89-b376-631dfd1c7168 | -14.3453 | -53.26619 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ae22af-ba59-3eed-9df7-8d302c26c040 | -13.67983 | -46.91102 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc3c8dd4-4c9e-3f30-9718-42a5aac6ba3c | -13.34433 | -51.78526 | 2025-08-29 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88bee8fe-d1c9-3652-84cf-ee63fa466c68 | -17.0467 | -46.50576 | 2025-08-29 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b06fa10-666b-331b-b615-26c6b0f0704b | -13.41183 | -46.84439 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d83c2e58-0540-3a5c-a6ef-5d5432ceb341 | -18.56458 | -44.00158 | 2025-08-29 04:42:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 214a6e0e-7028-3eec-ab7c-aadd7b4494bc | -13.63245 | -48.25381 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e92bcc7-7f9b-39f6-b185-7d8ea0b4c0d4 | -12.43339 | -63.91319 | 2025-08-29 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1ae51ff6-e585-3608-a843-cf60ec908367 | -13.39885 | -46.99485 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5c09e83-f680-30bf-87bd-95c31fd06752 | -13.45794 | -46.95444 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 306538d0-e2fb-351c-8136-646cc50681ae | -10.93636 | -63.63029 | 2025-08-29 04:42:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b4a5996-a7c2-3c58-8cf4-6be8116e7d7d | -14.2559 | -48.0675 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3321e262-f868-36d0-93b3-0bc25dceacd5 | -18.22051 | -45.57531 | 2025-08-29 04:42:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a17a40a-384f-3478-96d5-a5357b958b91 | -13.40346 | -46.8482 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8b47e65-fad6-3e03-bb3a-3ed10fd3ee7d | -13.63135 | -48.13227 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b811910c-3bbf-3d2c-9d0f-1c287cfa4bfd | -14.52384 | -52.99623 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd001db0-430c-3b71-b272-773b5d75cdf6 | -14.40404 | -50.4129 | 2025-08-29 04:42:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 503516d6-4269-3685-9301-2dc74dbd8357 | -15.12593 | -48.1216 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 43f0ad9d-4e71-39ee-b711-b6a403c013a4 | -13.97924 | -46.32866 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1289f0b3-16af-3464-92a3-6e663aee6778 | -17.54169 | -46.61722 | 2025-08-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c111361-f71b-3921-b4d7-1d7207fb1fe7 | -18.08785 | -44.71941 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92eca7e8-90d4-32da-8edf-247f7056e84a | -13.01702 | -56.92025 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e616bcf0-0768-3031-91c7-2751b3dc26bf | -13.4802 | -46.84726 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7764c67-6b58-363d-b879-a7d22797331d | -17.35093 | -42.64421 | 2025-08-29 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b21db2eb-96bf-3230-9138-5ee062081635 | -12.98256 | -54.75785 | 2025-08-29 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24cbd6c6-0752-32e0-b9f6-e3bcccd46139 | -14.52047 | -52.99568 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 005886a6-cb50-3213-a8a2-46dd8a4af549 | -13.56588 | -46.90828 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41a32ddd-cb98-3913-af00-ff0b66bc9279 | -13.58928 | -46.86901 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c47ae560-2520-3821-b445-c0e413969d84 | -15.71962 | -49.31474 | 2025-08-29 04:42:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b90f915e-2c06-3204-a916-978855758cbe | -15.09768 | -48.39615 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac8c1365-4769-3b6a-90e4-bd7fa351da03 | -13.5603 | -46.89223 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34ea1199-b5a2-3429-9c2d-4f9db3b1acb2 | -14.58489 | -54.52167 | 2025-08-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74fa1ded-3255-32a4-9350-5aa725074de8 | -13.41278 | -47.00652 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92a093f8-e232-356e-a3ff-c4745c4b26c6 | -16.50396 | -47.77709 | 2025-08-29 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ebfd020-7fdd-399d-9ee6-6c2cd8066cd0 | -13.01427 | -56.8875 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5998390-14de-3e22-b213-05dd14ace650 | -14.24204 | -48.06067 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ca522dc-a0f1-31de-8a86-440fab7b33c8 | -14.04143 | -44.48435 | 2025-08-29 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f7dc1ce-6fa4-3292-a848-c2cb952350b5 | -13.50015 | -46.84488 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80713228-92a8-3cdf-ba74-bcbaea641120 | -13.58159 | -46.86786 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe94591d-16c9-3694-b48b-ef5b3bc0895b | -13.36815 | -51.7637 | 2025-08-29 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4b4f361-67e8-3788-9de9-4433f0cad620 | -12.99817 | -56.92887 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c1c215b-e196-32bb-a58e-059aea45c83a | -12.92907 | -56.97293 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f993b9db-eebd-3603-8d74-33dae179fb4e | -13.97335 | -46.34181 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bdeb96d-8c51-3f03-a961-192d130f5390 | -13.67348 | -46.91297 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16e2cab0-8e26-3143-ae59-b491c4869854 | -13.98324 | -46.32921 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d74f4ef-7029-3ac5-8b0c-aec749c413a4 | -13.54943 | -46.88585 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a142e841-5cd7-37eb-9c75-c466a5014ea6 | -13.40898 | -47.00592 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1735931a-e352-3d85-89aa-ad22c97916ea | -15.07349 | -48.12303 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80db2ef2-1dd1-37a3-ba5e-2845a078f8ed | -13.01214 | -56.92336 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a868011d-00e1-3a1b-9239-553c92f97708 | -15.07429 | -48.62788 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 776b7168-8b10-3887-a023-0ee607f80030 | -13.41729 | -46.97426 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| bc6a89f8-1415-3186-bd8e-6ceee0cbbda9 | -13.36427 | -51.76669 | 2025-08-29 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f89bdd67-60d0-3885-a1fc-ff8de8aabd3f | -15.32066 | -48.22312 | 2025-08-29 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dcde870-f31c-3cc8-8aa7-abd3d495c7a7 | -14.58695 | -54.52499 | 2025-08-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd0dfaa7-3cf1-30cc-bc67-a1b02e770526 | -13.45669 | -46.96361 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dfc0c65-37ae-3156-bdd9-9d345df659cf | -13.41987 | -46.98365 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 56abbd73-c303-3425-a654-979ff5c85e98 | -13.53603 | -46.86938 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f489bbc3-fd0d-3bc1-991f-c82226e6876e | -13.59136 | -46.86681 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e67aa075-0ac2-3bb8-ad75-9dbb8647963c | -17.04865 | -45.88761 | 2025-08-29 04:42:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bc21935-b8e4-3679-973b-4ad6c11cab11 | -13.45173 | -46.95107 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1daa0fb3-ca3e-3e92-91ac-3f9a05762152 | -13.40731 | -46.84877 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19793ddc-fc0e-3b2e-afe1-8715dc8f47b4 | -13.40267 | -46.99538 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cb6c2698-f277-354c-836a-3544e33d63e7 | -14.7864 | -59.72311 | 2025-08-29 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f626d09d-6240-37c0-a7d8-315373f82263 | -13.55536 | -46.87147 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 51f2e261-39a7-3976-971d-76d784510851 | -13.55486 | -46.9309 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b5677cb-5d96-3839-83eb-d426fec705a8 | -13.48858 | -46.84334 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a26517dd-69b7-39ad-84cb-06c49ec27d2c | -13.5875 | -46.86631 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96d4c24b-e451-33ff-8503-6da5c85c59b9 | -16.28227 | -53.61201 | 2025-08-29 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README56.md)
