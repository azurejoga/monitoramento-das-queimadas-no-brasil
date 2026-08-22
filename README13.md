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
| 8f6e6946-3234-345a-9d13-7d2e1b7cd0db | -7.68374 | -46.17097 | 2026-08-22 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d5048c5-efd0-3f13-a8e1-67bd857c834d | -5.59233 | -43.99849 | 2026-08-22 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47bfa015-503e-32e6-8d3a-fa8bd4bfd865 | -5.55409 | -43.43542 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9aa3a154-d67f-3148-802a-490f863e4882 | -9.26602 | -45.64371 | 2026-08-22 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d07820cd-254d-39ff-862e-b0245fa0a3ab | -6.88134 | -43.74644 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8275d8a9-ddff-3bd1-a78e-9036c846b774 | -5.82029 | -43.49614 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3902425-e278-31df-89c0-7084fce78adf | -6.34257 | -44.07791 | 2026-08-22 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 130b88c3-1e0f-38b8-8ac6-c565d199666b | -6.89177 | -43.7523 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 290f7b80-832a-3c73-afc8-d5c7ebffd6d9 | -6.91688 | -44.97242 | 2026-08-22 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3cc4c75c-d31d-3fa4-a846-c0cb95a23c02 | -7.21619 | -34.95757 | 2026-08-22 03:42:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 628955cb-c09a-308a-8572-8200dec31731 | -9.27011 | -45.6475 | 2026-08-22 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 256b0742-9444-3ec3-80d8-3dcc5f49333b | -7.48715 | -43.81489 | 2026-08-22 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c20c34dd-6829-3741-bdac-ec652eaba52d | -9.27104 | -45.64992 | 2026-08-22 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9d7adf8-9bc6-3d81-8b56-ddd4cb3217ed | -5.82587 | -43.49703 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77cd809c-9b9f-35e9-a389-32fefccf35fe | -5.64549 | -37.25598 | 2026-08-22 03:42:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 475283ff-d4fb-3747-ade2-300bdabd8df3 | -5.71282 | -46.19144 | 2026-08-22 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef6fa7ed-3cc3-3809-a858-bdc5c3f5b69b | -9.02891 | -45.88362 | 2026-08-22 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0388ec1d-dc03-364b-ae76-cb38f0219360 | -9.02991 | -45.88198 | 2026-08-22 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5bf588d-e5f6-3dcc-bb1f-12d2b9090ea3 | -6.87644 | -43.74181 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 348c992a-68cf-34a9-9b51-2e6d487f5771 | -4.93289 | -41.9822 | 2026-08-22 03:42:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 330f6de9-77ad-3b7f-9d13-529be5840076 | -6.87578 | -43.74547 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43a23042-81cd-359e-b14c-afebfdd2449c | -6.34893 | -44.07535 | 2026-08-22 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e2e62a6d-c6c3-3f4c-a542-6828a975fd82 | -5.59164 | -44.00245 | 2026-08-22 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4e15998-41d3-3617-aee3-240b680913ac | -7.72087 | -46.14938 | 2026-08-22 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f69fe82-2a93-31ae-be13-fbd4518e0487 | -5.82092 | -43.46803 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e0e74dc-0009-3be2-8730-5366f40c728c | -9.02899 | -45.88692 | 2026-08-22 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8cad311e-639f-39f8-aff9-6ccfcd16e6fe | -5.82097 | -43.49236 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7db9ed0c-c9cb-30d4-8aba-4603ff91ec15 | -6.87155 | -43.73713 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b61228a-c8db-37e3-a8b9-a6c0e5929a11 | -6.64908 | -43.90425 | 2026-08-22 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9550b7ff-41aa-3010-bd54-dde04cfcb4be | -6.87998 | -43.75402 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 834aa4b7-b280-374e-973e-315db97aef46 | -8.28477 | -39.97443 | 2026-08-22 03:42:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b1d56e1e-0be7-3647-8d8b-a6cbccae2a8d | -6.8702 | -43.74455 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d45199b-f39f-35a4-aefb-a6d8b808192f | -6.21271 | -39.81592 | 2026-08-22 03:42:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 31c0d704-7c59-3295-9cf4-2a8ee9663da8 | -8.1609 | -46.72298 | 2026-08-22 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5779bc0f-128f-3a75-a5f0-c75ec8d9970c | -5.8279 | -43.48565 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e1ce55c-58e8-3a5c-9445-4260b60aa10f | -6.88689 | -43.74747 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b8a82e7d-85e1-30cc-970b-098a4f44c1ae | -7.01745 | -48.03204 | 2026-08-22 03:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a945f38e-9a58-3978-a3ac-75c366cc5bb0 | -6.88066 | -43.75024 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c275bc9-1bc0-3f19-a4d3-4bc5960256bc | -6.34752 | -44.0834 | 2026-08-22 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fa9f6588-3074-3bf8-be8e-550967f04d3e | -4.71992 | -44.34237 | 2026-08-22 03:42:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdf005ce-2c1d-3efd-b97d-bb0ae4c5080a | -8.15334 | -46.72701 | 2026-08-22 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 37e88bdf-90dd-3457-b151-e41f49886c36 | -7.53657 | -46.02446 | 2026-08-22 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e29680b6-d3fa-39bc-b32e-bafa7c7e5f5f | -5.82165 | -43.48854 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5519a95b-8d9c-3537-85dd-dac32e9b7ee9 | -7.01032 | -48.03043 | 2026-08-22 03:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7269c85-2217-3e20-b30f-11a68ce9d7a2 | -5.64919 | -37.25658 | 2026-08-22 03:42:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 63e8e1b1-5635-3011-a184-ed41262036ca | -6.34871 | -44.08227 | 2026-08-22 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 393a69f6-5136-3124-94bb-bdb9966cf081 | -10.47005 | -45.09196 | 2026-08-22 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 244655ae-c08f-3dde-9b57-4a5b0099eb50 | -6.34379 | -44.07682 | 2026-08-22 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb14036f-3ca6-3b84-a457-f8ec08511de3 | -7.17847 | -42.75232 | 2026-08-22 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5dddb0bf-4c78-3e5c-ac47-75389e783191 | -5.27029 | -44.03273 | 2026-08-22 03:42:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85aacc0c-57e1-31f8-b9f5-bf8413acf83b | -5.58588 | -44.00134 | 2026-08-22 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6333889-2bc2-3260-acae-735a49a798cc | -7.69012 | -46.17215 | 2026-08-22 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b30d7b49-ca83-3ca6-815a-d60c052c9242 | -8.15439 | -46.72156 | 2026-08-22 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aeebe5e3-f87b-3193-be7d-afd133ef5729 | -5.55475 | -43.43167 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d11d6b34-31e9-3f39-acba-faddcc06342a | -15.91961 | -43.52317 | 2026-08-22 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be378bcb-573f-30ba-8964-0fbb7ccc1c81 | -15.51519 | -45.86187 | 2026-08-22 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61f7ac64-4ca7-3b09-8046-8d27f3557a9a | -17.95491 | -42.73028 | 2026-08-22 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7281889c-7d35-398b-ab88-2a780bb2b6dd | -11.95233 | -45.49544 | 2026-08-22 03:45:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79178a77-3d6c-30f6-aaaa-2e8d835acf66 | -11.44223 | -44.55366 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcf1275f-adaa-35ec-86b8-722faf3d5138 | -17.97417 | -44.37334 | 2026-08-22 03:45:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8adb4faa-0e16-39c3-84cc-050461d8dce9 | -18.72427 | -42.22816 | 2026-08-22 03:45:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5df15817-68fa-39f3-b792-b1c078b6c69c | -12.2565 | -43.17487 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1e285c1c-350f-3e5e-8770-b9f5a2b574c1 | -15.80881 | -38.90967 | 2026-08-22 03:45:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 917bcbe4-43be-3c20-bcb7-15c44ebd1107 | -11.43984 | -44.55903 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc71d13d-6db1-3b70-9c89-eafacab62e2a | -12.25313 | -43.1793 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 66c774bf-1454-3268-93fd-7b81adc757dc | -13.15658 | -42.41505 | 2026-08-22 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bf825141-d755-3bfe-af5f-633dfc84c4ea | -18.65607 | -43.17675 | 2026-08-22 03:45:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 45f5d745-e80b-3488-9a93-fc7fd845bc9a | -18.65562 | -43.17529 | 2026-08-22 03:45:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b3ec094b-3392-3321-927e-f800c79de8b1 | -17.97401 | -44.37317 | 2026-08-22 03:45:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a162dd2-18c9-3fbf-b6d2-98e93748be0c | -12.832 | -48.46991 | 2026-08-22 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 145d8ab9-37a0-32ca-9eba-bd0810a9576a | -11.44568 | -44.53602 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3140739f-506c-367d-ab45-e901b46d43cb | -15.80028 | -38.91671 | 2026-08-22 03:45:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e09ac541-ecc2-3b18-906a-696c2bc5d025 | -11.59626 | -46.55129 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b85b84da-3b18-351a-9598-434b06dc2d4f | -11.12897 | -49.04602 | 2026-08-22 03:45:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a062f72b-ae4c-3436-8de5-7a1a5f843c9d | -13.37817 | -41.34645 | 2026-08-22 03:45:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c9cc2991-129f-3309-badb-4c57191a8e81 | -16.41191 | -43.05971 | 2026-08-22 03:45:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2c0444c-89ac-3580-b183-919d0d7daf5b | -17.84641 | -44.4678 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56deebc0-7599-31dd-b12e-d8870319859e | -17.91914 | -44.40043 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35606ffc-03d8-36c9-bf3a-180c2cd192b9 | -17.97297 | -44.37845 | 2026-08-22 03:45:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f647f72-05ad-32bc-8427-ee8aa9b94e78 | -17.97034 | -44.36677 | 2026-08-22 03:45:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb59cc15-04f0-3bbb-8c4b-e369c9037ced | -12.26016 | -43.18216 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 170b2174-3a66-3b35-aad2-10b714caeb5a | -12.76897 | -48.39216 | 2026-08-22 03:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 50e575da-3c88-3654-8b40-d63fe8ebbcb1 | -15.79672 | -38.91605 | 2026-08-22 03:45:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f00060e-07c2-335a-8c85-9561f37fdc68 | -10.9889 | -43.70406 | 2026-08-22 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e206f9a2-5150-3b3c-9343-49dadc9dbf62 | -10.29924 | -48.22609 | 2026-08-22 03:45:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b1f56d3-36e0-3c8f-a877-2e70bff06abd | -16.48351 | -47.95212 | 2026-08-22 03:45:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 23207faf-f144-3c58-a2e6-37794ade3f0a | -11.11461 | -46.19667 | 2026-08-22 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75fda042-df54-335a-8075-fb6c46152c82 | -14.39996 | -43.79766 | 2026-08-22 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 931c02c7-1924-3897-8c57-c2bd56750b31 | -17.91573 | -44.41747 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c7407ae-15d6-37e3-890a-ece6d463f7d4 | -12.75538 | -47.11537 | 2026-08-22 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92dbd39c-3872-3968-b0ff-0db45a3882bf | -18.33584 | -42.46702 | 2026-08-22 03:45:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a594a67-7d10-3bf9-b2fd-2f26738a4b50 | -17.96826 | -44.37728 | 2026-08-22 03:45:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c28d5594-60b1-35bc-8c3f-7294941c9dc3 | -16.485 | -47.94544 | 2026-08-22 03:45:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e5732554-fa67-381e-acec-cc2d42eb239d | -17.95827 | -42.736 | 2026-08-22 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fb0c88f9-8e50-3119-88c8-61c352f215ee | -14.40279 | -43.79356 | 2026-08-22 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 06a3f478-74ac-35d0-9d74-4106481d39f2 | -18.33659 | -42.46301 | 2026-08-22 03:45:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 379b87b7-adfa-35e6-828c-6c0c08cbb50a | -18.33993 | -42.4683 | 2026-08-22 03:45:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5ca4d3ea-49e8-3a28-873a-d7cd3def2898 | -12.82314 | -48.46665 | 2026-08-22 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47f547d1-ec4d-3afc-943d-d8c3e892147e | -11.59008 | -46.58061 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 722332b3-5998-3dee-89c3-6cfe2dfe69d7 | -15.81237 | -38.91033 | 2026-08-22 03:45:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README14.md)
