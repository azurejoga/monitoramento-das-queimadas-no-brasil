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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a3d70c0-1296-3703-b032-3cab40f0d954 | -12.76214 | -61.45786 | 2025-11-08 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb0a9997-ff46-33e7-a882-d5459c4f556b | -11.84877 | -63.67739 | 2025-11-08 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c65622b3-ba5d-300a-8e60-af98c5157605 | -14.97767 | -52.97898 | 2025-11-08 04:59:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aafbd2ba-c2fd-3b62-88f9-e2c43152af7a | -18.02264 | -54.13668 | 2025-11-08 04:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2855d82-8fca-3dac-95ab-d2f652bfcfec | -11.73188 | -59.31113 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa592c8d-09f4-3747-bce7-9b440a542708 | -13.41117 | -61.26564 | 2025-11-08 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef969bde-933d-32c7-8450-af6afd81743a | -14.67435 | -51.8964 | 2025-11-08 04:59:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55d5e7ac-b958-3c0c-a910-50b1cb63a7e2 | -18.33357 | -54.28547 | 2025-11-08 04:59:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b92314-18ad-32b1-af45-17d9871b3bc1 | -14.67346 | -51.89761 | 2025-11-08 04:59:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8da300ca-e7df-3042-9ae5-305c36d2ce1b | -11.85312 | -63.67718 | 2025-11-08 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48983214-1907-3be3-ad01-89c80853c997 | -11.90908 | -58.93062 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2d6f37c-0877-3b6e-8a90-3fb2dae5d058 | -15.10687 | -48.77757 | 2025-11-08 04:59:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ee0a72c-00f0-3b58-85d7-f4d7cef2f136 | -10.28217 | -67.28221 | 2025-11-08 04:59:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf74a7e3-1848-3ca4-a574-904c26032dc4 | -12.58739 | -62.98512 | 2025-11-08 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53ed2b17-9906-3e78-8a33-091ee1a1efed | -14.67055 | -51.89585 | 2025-11-08 04:59:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26adf60e-2120-3625-b2f0-f3b357aaadf5 | -18.33415 | -54.28137 | 2025-11-08 04:59:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbf0825a-1acd-3357-be14-e2efcbbbdce3 | -18.33342 | -54.28226 | 2025-11-08 04:59:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4e6b7f8-d23c-35db-ba33-80b2e8170c15 | -12.13956 | -63.05765 | 2025-11-08 04:59:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a1ce5b5-16cc-38e0-ace3-a938910fbc85 | -15.18993 | -49.52026 | 2025-11-08 04:59:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dc4bdbf-2d37-36e8-acf7-be3d8efbf43c | -12.45275 | -63.15091 | 2025-11-08 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 538ca4c1-07a1-35e7-b23d-a477dc8830fd | -15.79908 | -50.1077 | 2025-11-08 04:59:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12f7eb45-1e8e-32ff-98e3-80580f2b6efc | -11.70741 | -61.42407 | 2025-11-08 04:59:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ca62e64-c2e3-3039-a639-b3fddd0d31ff | -15.63611 | -58.08305 | 2025-11-08 04:59:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 923b23ee-7a72-3e87-b556-a8449efc272c | -10.28115 | -67.28075 | 2025-11-08 04:59:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 970b4216-6f2b-3a28-952f-780ae37893f8 | -11.55971 | -61.69611 | 2025-11-08 04:59:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b71f00c5-4577-32e2-9268-9cd1e6f41ec9 | -16.08934 | -49.3886 | 2025-11-08 04:59:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa1ea861-a27e-3e3f-8b08-2bb4b9ed09a0 | -11.73563 | -59.31176 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fdbf5f1a-74d8-30fa-8e94-4a90221ccd36 | -16.09333 | -49.39389 | 2025-11-08 04:59:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3899e1ee-2f6f-3346-bc39-ba08772e2239 | -15.48363 | -58.19718 | 2025-11-08 04:59:00 | NOAA-20 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a377dc6a-6c9c-30a5-ad5f-ddf105e1a827 | -11.73032 | -59.32025 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 525c6099-5295-3ce4-a300-c7902b560cab | -14.48856 | -52.1441 | 2025-11-08 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e900006e-5545-3de6-899e-3a201042fe8d | -15.92409 | -56.12831 | 2025-11-08 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4f84106f-0db4-33e8-b7a1-642d523916f3 | -19.911 | -57.31805 | 2025-11-08 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5e8e46bd-2c21-3f45-a182-5cd94f2b0bcb | -20.25278 | -58.13247 | 2025-11-08 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.1 |
| e4d3a252-d24c-3935-bdce-cbebd6eb3419 | -19.4806 | -53.94273 | 2025-11-08 05:01:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe842f27-1076-3f5d-be0c-a30b5345e7e1 | -20.24946 | -58.13186 | 2025-11-08 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1673ae08-cc5c-3b7a-be09-44453da6ec4c | -19.91158 | -57.3144 | 2025-11-08 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6cd735bf-7c93-33e6-879b-be0a7874d982 | -20.2555 | -58.13677 | 2025-11-08 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6e7ab596-40fd-3664-bb41-8a8cb38a55ab | -20.25006 | -58.12817 | 2025-11-08 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 121c973a-5298-3ce5-9c90-350d412902ae | -10.07596 | -36.13418 | 2025-11-08 05:10:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 44.4 |
| 594bed90-c729-3004-b06a-f99b5dd2327a | -10.08538 | -36.1357 | 2025-11-08 05:10:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 610ece8c-53b9-3cd8-ba42-add5b22c4559 | -3.6634 | -45.9463 | 2025-11-08 05:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f8993b86-2251-37e2-bc9f-a877d9d40d69 | -3.3526 | -53.22655 | 2025-11-08 05:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c24619b-16dc-3639-bd18-559f5a101a6c | -4.49495 | -55.79882 | 2025-11-08 05:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 779b476c-8a68-3463-974b-eb34f4752885 | -3.32542 | -53.36597 | 2025-11-08 05:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f46a144-dd7e-363a-a965-768be48894f2 | -3.35347 | -53.22058 | 2025-11-08 05:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bce6af1-b657-3f81-89d9-49c108a966c9 | -3.32626 | -53.36023 | 2025-11-08 05:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b33afe36-97bc-3e07-8aa9-9ee064b97404 | -3.13421 | -59.19278 | 2025-11-08 05:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2dbd042-11e4-3f9a-aee0-ccfa1b9cb5e1 | -4.48855 | -55.80207 | 2025-11-08 05:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b107975a-d157-3ea5-ba62-c6e693a27200 | -3.04872 | -58.73084 | 2025-11-08 05:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4abe394-210b-30e0-8603-726b2c431b38 | -1.70319 | -54.67057 | 2025-11-08 05:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfbca286-3073-31cf-b0d0-21f359bf3c19 | -3.27976 | -64.86653 | 2025-11-08 05:46:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53c7e6ff-7229-34aa-92da-14b0e5aa83e0 | -4.28239 | -55.54377 | 2025-11-08 05:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4983dba0-7464-3bc6-90ae-ff184b782e96 | -5.14749 | -60.3723 | 2025-11-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac19b40e-a8eb-3c38-875c-0c57d7c4cd1f | -9.22116 | -62.5884 | 2025-11-08 05:48:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79d11396-3df6-33b5-9dda-3d45689df0ac | -8.56246 | -67.00904 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33fa051b-d286-3148-a59c-4a9862404e04 | -9.95271 | -63.19389 | 2025-11-08 05:48:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79640343-e9bd-34d2-bec8-e6258395e019 | -8.62129 | -66.76212 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccec868d-4d9e-39f9-adbe-a0ea460c237b | -9.76181 | -55.62189 | 2025-11-08 05:48:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d4203c6-b128-322b-b99c-959a8eda6f7e | -9.28682 | -64.3814 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed7191ef-b7e0-347a-b3f2-4e9ae338c46e | -9.82788 | -62.331 | 2025-11-08 05:48:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5d19398-8619-3172-ada8-f5876c939626 | -8.60935 | -63.52365 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7497483-1eb7-3d71-aaa3-09c4d1adfa05 | -10.99242 | -53.98734 | 2025-11-08 05:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 768c911e-a7f9-340c-b9ad-5553cf7f730b | -9.42623 | -64.36218 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67b4b30f-d921-3a9b-913c-0b2bd144e7fc | -9.94446 | -55.54782 | 2025-11-08 05:48:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d470563-0f74-32ec-98cd-b8fea4c8898c | -8.61306 | -63.5242 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c986675e-7fdc-34eb-a350-26512685cae4 | -7.81164 | -61.56926 | 2025-11-08 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eac51917-7872-3e56-abef-85986dc1a69f | -8.64764 | -67.03023 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5c01237-43a4-3e9a-b3f1-40a6b3c02137 | -9.77861 | -62.50189 | 2025-11-08 05:48:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8d5dff5-42bd-3526-a9e6-649898cd1671 | -10.00301 | -63.65403 | 2025-11-08 05:48:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c654042-16d1-3c28-81dd-a90e737c13e5 | -9.76246 | -55.61673 | 2025-11-08 05:48:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bf95384-f257-38ec-b01b-a757d140115b | -8.25678 | -71.11803 | 2025-11-08 05:48:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 573307b5-0c5b-3cf1-95dc-3a54a545b021 | -9.18772 | -63.73399 | 2025-11-08 05:48:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fafbc3c-a783-3a7b-8239-3c437524c3df | -9.54312 | -66.73969 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5893f8a-35aa-3e3a-b585-4188fded0411 | -9.9381 | -55.54694 | 2025-11-08 05:48:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b2fb667-6efc-34c0-a80b-000c5dc136d5 | -9.50787 | -66.77007 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5611e3e-ccf1-3b96-b74e-48df4e24db2d | -8.62721 | -66.81357 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f721b0-b5ac-384d-a1f2-fbcb0d84c78c | -8.47407 | -63.93445 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd259d5d-c9f3-3c16-bcc1-a32d1c981e2e | -9.34513 | -65.92525 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dd1614c-56cf-34ad-9922-8fb91d67d706 | -9.79862 | -64.13889 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12d95713-40ad-3c4c-b88d-5081d7294a9b | -9.99926 | -63.6535 | 2025-11-08 05:48:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77f2918e-8d4d-3f1d-a937-d06bfa743792 | -9.86688 | -64.88332 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 334d0c72-0cdd-3d4b-a605-740a515b624c | -9.44254 | -59.20579 | 2025-11-08 05:48:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| d5879249-a7c6-374a-bc25-312d12bab484 | -9.55307 | -66.74126 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1a5f0a5-4494-324a-912d-fa27b0183e35 | -9.55639 | -66.74178 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ced1422-a7f8-3b21-99d1-6f3b08475ee3 | -8.6471 | -67.0337 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cc7a8e6-1dff-3da0-8ca5-2cb284549956 | -9.41319 | -68.06992 | 2025-11-08 05:48:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf7a2995-2ae3-3412-943d-a1d6b118fce1 | -9.24456 | -67.60612 | 2025-11-08 05:48:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edd8551a-a4ad-3977-9570-2f3016aad08f | -9.55585 | -66.74529 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82c95633-7bfe-38b2-9692-d5e86cf7305c | -9.07776 | -61.69334 | 2025-11-08 05:48:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c73792a-9f17-3e87-a4d9-fbe1437ec425 | -8.63611 | -67.03907 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18bf07ad-1c2e-3ade-aeeb-02a465be542d | -9.82865 | -62.33004 | 2025-11-08 05:48:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 430148b9-1abf-3a86-8d68-8ab9fd7b3e4f | -9.56025 | -66.73879 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7959db9b-7833-365f-8bf5-544b7cc6aa8d | -9.56363 | -66.76087 | 2025-11-08 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e78b2dd6-ad42-34b9-bf8a-a763e7023f9b | -9.86979 | -64.88784 | 2025-11-08 05:48:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1e42a1c-749a-39fc-a46c-c7bc53c22e9f | -9.44752 | -59.20652 | 2025-11-08 05:48:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b41f3de-dd34-3ef7-8226-9fa02a885297 | -6.62143 | -55.01622 | 2025-11-08 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfe77680-c060-3146-a8c2-eb375d5636c4 | -9.08194 | -61.69394 | 2025-11-08 05:48:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04a838a9-aa02-34b1-9fd7-a23e949038ca | -10.99521 | -53.9865 | 2025-11-08 05:48:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 12e26c95-58ee-3ca8-a869-9c839fd56975 | -9.07829 | -61.6895 | 2025-11-08 05:48:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README38.md)
