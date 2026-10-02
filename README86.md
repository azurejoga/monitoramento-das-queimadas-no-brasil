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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0087789-fa00-37c3-a0ac-27a1be4c7cab | -11.7375 | -43.4356 | 2026-10-02 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| b0728a53-308a-36b4-9d6d-709fdcf9a212 | -11.7563 | -43.4563 | 2026-10-02 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 245.8 |
| 00aa5873-22a6-3d6b-a665-8f17bcba5644 | -12.5329 | -43.091 | 2026-10-02 13:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 274.3 |
| 0ae54036-9e6d-3f81-829d-626a260a3b4f | -15.6741 | -41.3151 | 2026-10-02 13:00:00 | GOES-19 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 97.7 |
| 51c396ce-2e5c-33c9-9610-e9149bed4084 | -11.7187 | -43.4148 | 2026-10-02 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| c403af25-bf53-3241-a838-0568d474f7a3 | -13.3481 | -43.8538 | 2026-10-02 13:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 513.5 |
| b3f97eb4-1d1e-35ee-a7b5-3cf123a7bfc1 | -11.1615 | -44.6002 | 2026-10-02 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 229.6 |
| 4472ed96-e842-3d8a-a51d-415c874f4cd5 | -10.3034 | -44.6249 | 2026-10-02 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 8c916d2c-c998-3c0b-a134-be08a739e691 | -13.7843 | -45.2321 | 2026-10-02 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 102ae44b-1234-3d04-b2b2-28367774aec0 | -12.5522 | -43.0877 | 2026-10-02 13:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 188.6 |
| c0b3616d-8876-3db2-a69c-bd2ab4279403 | -12.7808 | -45.1897 | 2026-10-02 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 434bb40d-e76c-3761-83b1-a4b919ec2aa2 | -11.7182 | -43.4386 | 2026-10-02 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| b838a344-72df-3517-b2a4-a4916fb2a5d1 | -13.3287 | -43.8573 | 2026-10-02 13:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 480.5 |
| 21b0789d-987e-3fdc-a318-f293325375c8 | -11.7567 | -43.4325 | 2026-10-02 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 304.7 |
| 789be200-bd36-3c78-a99a-530961505b95 | -11.1424 | -44.6029 | 2026-10-02 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 169.5 |
| dc7acad5-c6f8-3ad1-a63a-5e29b001adc8 | -12.9036 | -44.8217 | 2026-10-02 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 57a27d28-22d7-36fd-905a-43b06005cbbb | -11.1427 | -44.5796 | 2026-10-02 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| bf5b81e8-3c99-3909-8b40-d8c6c861572a | -12.7812 | -45.1665 | 2026-10-02 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 32d9e41d-0491-38b1-ae98-11f22f2ca9bc | -11.2753 | -43.5539 | 2026-10-02 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 54ac854c-538b-3e45-8c66-e2819c7161db | -12.5334 | -43.067 | 2026-10-02 13:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 196.6 |
| b5a81e55-83e8-3d2d-80d9-4708eaa59c50 | -11.7169 | -43.5098 | 2026-10-02 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| e766afe3-46eb-3738-9ff7-0b239ca20f9c | -12.5334 | -43.067 | 2026-10-02 13:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 217.6 |
| a7041a11-1cd6-35c7-bbe4-cd4b02edb11a | -11.7375 | -43.4356 | 2026-10-02 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.8 |
| fab189a0-4363-3856-81b0-d0447319aaf3 | -11.7187 | -43.4148 | 2026-10-02 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 02967509-b33a-37ce-8233-43f38df4e13f | -11.1424 | -44.6029 | 2026-10-02 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| e82c2902-dd0b-31e1-99aa-fa0bae4b4db8 | -11.142 | -44.6261 | 2026-10-02 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| fbdeceb0-2008-3566-8550-372bf5822946 | -11.7169 | -43.5098 | 2026-10-02 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 8bc0b105-8c6b-3616-9586-d416e9644b4b | -11.1615 | -44.6002 | 2026-10-02 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 350.5 |
| a80a7cb6-294e-3f68-b85e-86ac224f909e | -11.2438 | -44.2626 | 2026-10-02 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 1be664e2-2ca8-36da-83ce-b1b34ef131cb | -11.2434 | -44.286 | 2026-10-02 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 620.6 |
| 2aebc3ad-4b17-38e1-a22b-f19215f46bc5 | -11.1611 | -44.6234 | 2026-10-02 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 501.0 |
| 9b62ae8e-007d-39d7-a3e9-17365b788773 | -13.3481 | -43.8538 | 2026-10-02 13:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1173.2 |
| c429d6c4-3cf4-33f8-bad4-c87095452d49 | -13.3486 | -43.8301 | 2026-10-02 13:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 300.2 |
| c550f4df-ad64-357e-9972-c2aa119477f7 | -10.303 | -44.648 | 2026-10-02 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 233.2 |
| 5df6f45a-eec5-3701-86b1-126270b4feba | -11.2753 | -43.5539 | 2026-10-02 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 86ade662-6fd7-3f97-9589-d1f777ecba09 | -13.3292 | -43.8335 | 2026-10-02 13:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 1d942ce3-69ae-3785-8348-7f21eea7e57a | -12.5329 | -43.091 | 2026-10-02 13:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 291.9 |
| 6a8fb2c7-a81e-3481-a340-e28bf664ae1a | -10.3034 | -44.6249 | 2026-10-02 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 37493224-651e-3aca-a3de-5e625565d6b1 | -13.3287 | -43.8573 | 2026-10-02 13:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 468.9 |
| 586f3f20-5e02-3e2b-a6a4-5047e377ce5b | -11.7379 | -43.4118 | 2026-10-02 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 4aa9f8b4-a6c8-366f-9f6f-50d6271bbf32 | -11.2629 | -44.2598 | 2026-10-02 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 393.5 |
| 7e34622c-8453-3a4d-98e4-f16108048aa1 | -12.5522 | -43.0877 | 2026-10-02 13:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 309.9 |
| f8a6dc26-eaa1-3f5e-91c1-9ee3c2235436 | -11.7567 | -43.4325 | 2026-10-02 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 214.3 |
| baefa9d1-5414-31c0-a8e2-4e0f6d97530f | -11.1427 | -44.5796 | 2026-10-02 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 7f3648be-cf37-30e6-9ada-faa93838ee42 | -11.2633 | -44.2364 | 2026-10-02 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 233.9 |
| 6f7caea2-d0f5-3439-bfa0-4b0053f63c91 | -11.69 | -43.64 | 2026-10-02 13:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f39dee30-d150-3996-8043-57f0caa0e163 | -12.47 | -44.16 | 2026-10-02 13:15:00 | MSG-03 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c811dba-fd1f-3ed1-8b0b-42a73ce189d0 | 4.17606 | -60.66537 | 2026-10-02 13:16:00 | TERRA_M-T | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| bf0aec4e-036b-3080-a627-1d9d31ab6a87 | 4.17996 | -60.67157 | 2026-10-02 13:16:00 | TERRA_M-T | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 63fbc998-bc8f-3d9e-b475-5f1793e06ab9 | -12.4732 | -44.167 | 2026-10-02 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| c276424f-f0b5-3bf7-8d74-f88d52579213 | -11.257 | -43.5095 | 2026-10-02 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 4689a34b-3ddd-31b6-8703-e96778df5f9f | -12.886 | -44.7314 | 2026-10-02 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 2214b32b-3d1a-3861-9279-93fa49cdfa8b | 1.7399 | -50.8235 | 2026-10-02 13:20:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 124.3 |
| f30e514c-34f3-34b3-ada9-032a03381a30 | -12.4544 | -44.1466 | 2026-10-02 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 0009fc88-40a2-3e27-b7c0-c56fb6034408 | -11.7169 | -43.5098 | 2026-10-02 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 049a592a-c1df-300a-aa06-cc3228ce1e0d | -11.1611 | -44.6234 | 2026-10-02 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 392.7 |
| 8ccc37b6-6f3c-37ee-b2db-ff074d323c5d | -12.4737 | -44.1435 | 2026-10-02 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 437.1 |
| 302d7121-8567-3f4b-a9d0-d5eb4251de0f | -12.5334 | -43.067 | 2026-10-02 13:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 349.8 |
| 6e074255-5ae8-3b0b-a1b4-24ceedabf7c0 | -10.3034 | -44.6249 | 2026-10-02 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 422.0 |
| 36edd62d-cfd3-383d-8500-04622a56deb7 | -11.142 | -44.6261 | 2026-10-02 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| deea75a9-4375-3d6c-9e94-53f2e016cdb4 | -10.9262 | -43.8406 | 2026-10-02 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 692e0901-2f35-36e3-bbd4-1633d7269b00 | -12.5329 | -43.091 | 2026-10-02 13:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 369.2 |
| 367c9e4a-d116-3ec3-824e-baff36c8abe5 | -13.3287 | -43.8573 | 2026-10-02 13:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 361.5 |
| 18c7b4e8-934f-3148-8d9f-203283e127a3 | -10.303 | -44.648 | 2026-10-02 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 385.2 |
| c5ba6757-a122-3972-b059-ab76a8c2d8bb | -12.5522 | -43.0877 | 2026-10-02 13:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 402.0 |
| 92e29915-dbec-37ef-aa59-64dbfdbce61a | -11.7187 | -43.4148 | 2026-10-02 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| fa5fb1fb-85b6-3d13-bf30-addb8187445c | -11.2434 | -44.286 | 2026-10-02 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 332.2 |
| 28b904fd-886c-3004-80f5-e881e286fc5a | -10.907 | -43.8433 | 2026-10-02 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 3c7f0c3d-7d8e-3465-8f46-df76dece1b8b | -11.7379 | -43.4118 | 2026-10-02 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 42cdbc35-479f-34af-9bb7-5028a83e242b | -12.8667 | -44.7346 | 2026-10-02 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 83a939ad-417e-32c5-8585-47b24815436a | -11.1615 | -44.6002 | 2026-10-02 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 360.7 |
| abeeb3c4-fec7-35ad-b250-eb80d15aa580 | -11.1424 | -44.6029 | 2026-10-02 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 188.9 |
| f9946af8-0909-313c-8ded-0e97f692d320 | -11.2753 | -43.5539 | 2026-10-02 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 28a1fd1d-df31-34c5-936b-ee720b5f6aa0 | -11.2242 | -44.2888 | 2026-10-02 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 21bde56e-d54b-3c27-8d31-867af5a59c41 | -10.43108 | -62.46903 | 2026-10-02 13:23:00 | TERRA_M-T | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 8dcb9eb4-ce12-39bc-bec4-bfd41a633d08 | -12.6129 | -63.08875 | 2026-10-02 13:23:00 | TERRA_M-T | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.4 |
| d4428a28-c3fd-3791-84dc-d0ed3c5d92a8 | -12.7804 | -45.2129 | 2026-10-02 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 653bcb2c-675f-341c-89ff-def72ac629bd | -10.907 | -43.8433 | 2026-10-02 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 29b447b9-b557-3602-af35-6da70cd4ac7b | -9.844 | -44.8449 | 2026-10-02 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 137.1 |
| e562b255-1bfd-3858-a454-584aa5c1734b | -12.5334 | -43.067 | 2026-10-02 13:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 281.2 |
| 455161de-b2fa-3ab9-8f76-4926be24dd78 | -10.2473 | -44.5628 | 2026-10-02 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| d361e0c6-5cf7-3e0f-8684-94b9c4132ecb | -12.7812 | -45.1665 | 2026-10-02 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 534.2 |
| e409d15c-6240-39e0-924f-5bff14eeb4a9 | 1.7399 | -50.8235 | 2026-10-02 13:30:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 41c9a631-529d-3ee9-9e34-2daedb212a01 | -10.303 | -44.648 | 2026-10-02 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 281.3 |
| 71544a1b-3e97-3544-91ee-a6d470c33892 | -10.9262 | -43.8406 | 2026-10-02 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| ff530756-676d-3409-a127-587ed7c47db4 | -12.4544 | -44.1466 | 2026-10-02 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 181.7 |
| e3460066-9982-36ab-a466-6e4fe5ea7eec | -11.2242 | -44.2888 | 2026-10-02 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| ff222187-9ca1-31e7-b34a-d716fba2e29c | -11.2282 | -45.1682 | 2026-10-02 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 55ea4eb1-b5eb-30b8-b330-0e665bf46290 | -11.257 | -43.5095 | 2026-10-02 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| e744477e-d2b8-31ac-93b4-6a312fe2f57d | -12.9229 | -44.8186 | 2026-10-02 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 1040038e-71e0-30e9-b28e-8a2376e398c4 | -11.7169 | -43.5098 | 2026-10-02 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 16b1f5be-834c-3528-9acb-3ab1bb0bcb60 | -10.3034 | -44.6249 | 2026-10-02 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 332.6 |
| 52dde8b8-f7da-38db-8319-5d37a7083c8a | -12.4732 | -44.167 | 2026-10-02 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| f4923e29-46ec-395b-a499-1e763215b6ce | -11.2629 | -44.2598 | 2026-10-02 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 459.5 |
| 9472e0d9-5a09-36e4-b5b0-c3ec2b63fa7c | -12.886 | -44.7314 | 2026-10-02 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 8107c5c3-8c4e-367e-960e-1a9a78276e5b | -12.2441 | -42.1048 | 2026-10-02 13:30:00 | GOES-19 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 124.4 |
| 99944229-5823-322e-897d-12d6cf64dcc6 | -11.142 | -44.6261 | 2026-10-02 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 45d1587d-2b3c-3261-892c-45e2d6f184b4 | -12.5329 | -43.091 | 2026-10-02 13:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 342.7 |
| 29362ea5-ac75-3fed-bcfe-b569cc0613b0 | -13.3287 | -43.8573 | 2026-10-02 13:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 194.1 |
| f4cb573f-85cf-31e4-a640-84cbb9f8fd58 | -12.8667 | -44.7346 | 2026-10-02 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |


[Clique aqui para ver as próximas entradas](README87.md)
