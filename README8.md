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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd9b9d88-da52-39b1-9afa-4b9c980263c9 | -11.73895 | -57.81938 | 2026-07-27 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 626f5bb7-ebbe-3a3d-a625-48f95f167b78 | -11.48438 | -47.55374 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8e84068-7c45-3671-9ade-dd1aa9377f70 | -12.31868 | -46.38752 | 2026-07-27 05:10:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c004bae6-d8f9-30cd-9da1-e397bf0dbda3 | -16.96148 | -51.88487 | 2026-07-27 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1e940aa-c3f9-31a2-a249-12180770a9db | -14.35069 | -54.93491 | 2026-07-27 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33a90426-35fc-33fb-b1c5-ff809dacc9f7 | -15.67343 | -56.08373 | 2026-07-27 05:12:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| faaa04e6-ea9b-30ad-8385-c94bae869dad | -14.3608 | -54.91539 | 2026-07-27 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f4768630-a431-38c4-9b95-75ff32d5b38e | -18.26408 | -50.3448 | 2026-07-27 05:12:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 68a8c7a0-dee1-3215-bf35-e10c789f1003 | -12.76673 | -59.781 | 2026-07-27 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2ca6a70-507e-37a9-93b8-809528f46901 | -14.2371 | -54.55724 | 2026-07-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02b49c9e-30eb-3688-9148-d588ca9dd9e9 | -19.10334 | -44.34448 | 2026-07-27 05:12:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d51dde4-76cb-3264-ace4-2dbeb9c61fb9 | -18.26905 | -50.34537 | 2026-07-27 05:12:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 26502d4d-d23b-3147-83dd-25ef358d4caf | -12.7687 | -59.78013 | 2026-07-27 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f53d074d-aa74-36ae-99b8-6c7380e074c1 | -16.96092 | -51.88947 | 2026-07-27 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e3f1db97-2755-3b0e-989c-ddea67f8bf30 | -14.2411 | -54.56532 | 2026-07-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94713b2b-9dd7-3f5a-b192-f81385378102 | -12.76737 | -59.78799 | 2026-07-27 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a692bb55-1c04-333f-8bc2-6d47aa10f03b | -12.32374 | -64.46909 | 2026-07-27 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c187539-df7e-31c5-ad83-ef5791de4583 | -14.36436 | -54.91592 | 2026-07-27 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a0f20d12-7083-356d-b6d1-2df8b0b7e908 | -16.96552 | -51.88686 | 2026-07-27 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 820097d4-de2d-3eb0-87f3-b212652bccc3 | -15.96429 | -52.20969 | 2026-07-27 05:12:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a54869c-e5d2-375f-a843-6ea8ad6ee1ff | -14.24171 | -54.56104 | 2026-07-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8901d90-ab82-30b1-88b5-426b4876275b | -14.23749 | -54.56482 | 2026-07-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8d2284c-61ff-3e1e-8112-0e44d1ded55c | -16.96589 | -51.88536 | 2026-07-27 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9436d608-7a18-35e7-8e83-40d090ff605d | -14.23448 | -54.56008 | 2026-07-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06175760-b936-3204-a19f-bc322649d3dc | -16.96111 | -51.88639 | 2026-07-27 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8048d7a4-864c-3197-bcac-8af9dffa88b7 | -14.38975 | -58.87477 | 2026-07-27 05:12:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 009a56f3-e8f0-3f24-9490-50fc41f0a4e3 | -14.23583 | -54.56579 | 2026-07-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bbd22a2-4fdd-3bbb-9d8d-7ce3d6794e14 | -14.35424 | -54.93542 | 2026-07-27 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42b754f2-7608-300a-9457-ccb31ab56ac5 | -15.40552 | -52.93678 | 2026-07-27 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 759a7adb-e3aa-3821-b7ad-f32e8bd1fec5 | -14.36496 | -54.91181 | 2026-07-27 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8b69b868-aab9-366d-a9bb-f8dd42851793 | -19.11064 | -44.34427 | 2026-07-27 05:12:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90511988-7b8e-38f2-ac1d-f1e8744e79ff | -20.56479 | -57.28773 | 2026-07-27 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48b940e0-69b8-3047-b022-6755af7b0e43 | -20.78742 | -57.93694 | 2026-07-27 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9db84292-82f8-337c-909c-4f3ac7d8eb2e | -20.79079 | -57.9375 | 2026-07-27 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e40590bf-551c-3508-bb93-68823079bd9d | -20.63106 | -57.26646 | 2026-07-27 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afd76e8d-6c47-3b19-ae80-db5cf3fa7bee | -20.78685 | -57.94075 | 2026-07-27 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 33d395d6-1f10-314a-b1f9-d7aeb878e4d1 | -10.94 | -43.05 | 2026-07-27 05:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31129d14-0ff7-325a-846c-c1666931162a | -10.9397 | -43.0593 | 2026-07-27 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 190.1 |
| b52dbef7-1194-3a99-980f-21bb8871540b | -10.9588 | -43.0565 | 2026-07-27 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 1dea3386-4192-3d55-aea3-c809935a3df7 | -10.9401 | -43.0355 | 2026-07-27 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 33bf3643-1526-36bc-92d9-34ef4b2141b2 | -10.9401 | -43.0355 | 2026-07-27 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 1f31c768-f6fb-36b0-ad18-dd20aadd240e | -10.9397 | -43.0593 | 2026-07-27 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 2a901313-fb37-345d-aeda-1434b3e00cb9 | -10.9588 | -43.0565 | 2026-07-27 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 5fd41444-dc37-3993-8095-120678d9ad0e | -10.9205 | -43.0622 | 2026-07-27 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| cd46a50a-6007-3ddb-ba44-e0411cfbac9a | -10.9588 | -43.0565 | 2026-07-27 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 659c5dbf-570c-3000-9f58-5a22e1002897 | -10.9401 | -43.0355 | 2026-07-27 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8f9a856f-bf7f-3ace-a8a2-ea4c68c6c861 | -10.9205 | -43.0622 | 2026-07-27 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7d968b47-69b5-3522-b257-541ec5b74354 | -10.9397 | -43.0593 | 2026-07-27 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 91ec8915-af0b-393a-b23a-11bc82c17172 | -10.9397 | -43.0593 | 2026-07-27 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| ed7477cc-9e53-3d2b-90b5-9939f4c75938 | -10.9401 | -43.0355 | 2026-07-27 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| bfbefd7c-64ac-3856-81fd-f8df696a9ae0 | -9.77453 | -63.37318 | 2026-07-27 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71e6f7d0-c4af-35cb-8e1f-60b970e8eeb8 | -8.7556 | -64.84673 | 2026-07-27 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32c38cf8-3118-3823-a351-c285584705c0 | -9.47293 | -63.37112 | 2026-07-27 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e063a31-2141-37e9-b155-72370dd2b048 | -9.91437 | -67.04485 | 2026-07-27 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c15dc877-26b5-3f54-9afa-2e9adbda379e | -9.9184 | -67.04154 | 2026-07-27 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b8a25a3-0341-34d7-9458-82c0dfa065af | -8.78922 | -63.80715 | 2026-07-27 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8db38ac0-8972-31a8-842f-9d18f5bbef07 | -9.47772 | -63.36766 | 2026-07-27 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d32ff275-d378-3517-87f0-c520edd987e3 | -8.86448 | -65.03001 | 2026-07-27 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 401f8953-85e7-3e28-a9ce-3058f2321593 | -8.71624 | -65.1942 | 2026-07-27 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7356c3ec-b389-3dea-ae3c-819e71d30967 | -9.27181 | -68.39857 | 2026-07-27 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c8d8d28-2d79-389a-a06e-6d47c43122a9 | -8.49552 | -72.7226 | 2026-07-27 05:55:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5ad6937-717d-37e2-953e-ec197bbd3e97 | -9.26849 | -68.39805 | 2026-07-27 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2022b31a-28d2-318a-8c0e-b668216f0e0f | -9.48196 | -63.36821 | 2026-07-27 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef66b475-20eb-3ff3-bee7-5690a9ad8338 | -8.71251 | -65.19364 | 2026-07-27 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85a41d0a-96b0-31c8-8647-3987936b9bb2 | -9.73247 | -63.42947 | 2026-07-27 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab8c62d0-2f16-3f1f-b7c0-6d33df4d9838 | -8.8647 | -65.02715 | 2026-07-27 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a75a2e0-c321-35f9-96e6-98e525fe63be | -9.26903 | -68.39454 | 2026-07-27 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1f17268-164f-39f5-a51d-f943e1716d20 | -9.98658 | -66.84604 | 2026-07-27 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 288eff60-85e5-3c7b-ae5f-a918ba47afca | -9.47717 | -63.37163 | 2026-07-27 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 19b32256-aad1-349f-bd5c-ffee1130e796 | -8.90491 | -65.01714 | 2026-07-27 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a924425e-7fc3-3a01-b1a6-ca1c51f89c3e | -8.7887 | -63.81079 | 2026-07-27 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 415a6232-486c-3559-b195-7de71e9cad6d | -8.75178 | -64.84616 | 2026-07-27 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 432921bd-0b28-3049-be95-6ba49de5bfd1 | -10.94144 | -43.06852 | 2026-07-27 05:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f06c7d31-c5e6-3fc5-9816-d156a9434711 | -10.93266 | -43.05029 | 2026-07-27 05:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 7e72d1f4-2e66-3393-b1f8-ecb764ae022e | -10.93546 | -43.03411 | 2026-07-27 05:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 32ea9e4e-53fb-37ab-a7ce-6ef613ca0903 | -10.93751 | -43.04404 | 2026-07-27 05:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 773b424c-ecbb-3a2e-b0f4-546b196672d9 | -10.94423 | -43.0523 | 2026-07-27 05:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 062e802b-92b7-318f-bc3b-7a80f2c0effb | -10.93483 | -43.06029 | 2026-07-27 05:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| a1a5fa7c-1bd2-3c78-b2ac-07250de44131 | -10.92984 | -43.06651 | 2026-07-27 05:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 441edc7a-0ba6-31b7-8a07-43cf0a0e4e4b | -10.9401 | -43.0355 | 2026-07-27 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 368666e1-de6f-34a5-9a51-092a3316972c | -10.9397 | -43.0593 | 2026-07-27 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 907406df-3182-32cd-8b77-d4165f96b517 | -10.9397 | -43.0593 | 2026-07-27 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 5c768972-2fef-3dd3-b7af-57133f1e8669 | -10.9401 | -43.0355 | 2026-07-27 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 318a3297-2ed2-3208-b2b6-63ac51ced08e | -10.9397 | -43.0593 | 2026-07-27 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 5f598da3-6e39-3368-8a3c-d6a16f9aaa54 | -10.9401 | -43.0355 | 2026-07-27 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| ed592e57-0fe8-3fd1-a813-a7c393c67816 | -10.9397 | -43.0593 | 2026-07-27 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 4bd72ff8-1e50-3446-97cb-59e9e0ae907f | -8.71507 | -65.19403 | 2026-07-27 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4ed7842e-925d-354c-ac19-c5e7e64dcbbd | -9.47714 | -63.36882 | 2026-07-27 06:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e2d7087-e437-3402-8809-bfa573c4749b | -8.71561 | -65.18996 | 2026-07-27 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 147c1480-7b2f-3095-bfc5-d5d35f5941fc | -10.9397 | -43.0593 | 2026-07-27 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| aa205988-b246-3b49-a53b-4f1eb2ec7478 | -10.9401 | -43.0355 | 2026-07-27 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 26dd49a8-bdcd-3ed9-b6e2-85fbc39e8e61 | -14.3624 | -54.9288 | 2026-07-27 06:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9923bb14-987d-3b60-bfff-195f96d18b14 | -14.3819 | -54.9059 | 2026-07-27 06:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 18502241-ca60-3e42-9b0f-3b74ec239f27 | -14.3816 | -54.9266 | 2026-07-27 06:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| cd0b2ce4-ad93-3760-84d7-6fb376a181cc | -10.9397 | -43.0593 | 2026-07-27 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ffc20693-7791-34f3-a903-ee571617ea26 | -14.3627 | -54.9081 | 2026-07-27 06:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 459220b7-0281-3039-b2c4-a871f37a6ab6 | -14.3819 | -54.9059 | 2026-07-27 07:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 9a4eb8e5-a4ae-38b2-8eb7-91532a705842 | -14.3627 | -54.9081 | 2026-07-27 07:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| aeed8472-f857-3ae4-8db3-a82ea89b2b5c | -10.9397 | -43.0593 | 2026-07-27 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 22397111-fcf8-3aa4-b514-57d1d7bd2a93 | -10.9397 | -43.0593 | 2026-07-27 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |


[Clique aqui para ver as próximas entradas](README9.md)
