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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea6c174c-1a25-368e-8ef7-cb387bbd0a44 | -3.6033 | -60.5474 | 2026-08-28 20:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 2a4d1d08-c6a8-3dad-9634-ff4215d8244e | -15.5773 | -56.271 | 2026-08-28 20:10:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a54799e9-a316-3206-9e5f-3421a23f8e86 | -14.9011 | -52.6267 | 2026-08-28 20:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 138.3 |
| a0e7b9be-c9e2-3f6d-97c1-900043776128 | -7.529 | -61.3635 | 2026-08-28 20:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 194a7d4f-40bb-3ca4-a1ac-ab0b9d745f58 | -10.5523 | -59.6161 | 2026-08-28 20:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 20e4d695-9b31-32a5-983b-27ac57e2c02d | -21.5152 | -55.3985 | 2026-08-28 20:10:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 434.0 |
| 1b30c337-0dc9-30b5-af45-2945d8a9179e | -6.8358 | -59.9379 | 2026-08-28 20:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 59ff9fb6-1b54-371c-bb67-ed797893a859 | -8.6012 | -70.2192 | 2026-08-28 20:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 141.7 |
| f6971067-554c-3f05-afbb-cc1c2df3e9e1 | -6.3465 | -44.1013 | 2026-08-28 20:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 6acc4f9b-cb80-344d-9bf2-6d790f5e9836 | -17.9681 | -50.1762 | 2026-08-28 20:10:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 153.9 |
| c95a8104-4ab8-3af4-9ca3-100bc9ea9638 | -5.9079 | -57.7506 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 3d25f1ad-9b47-3a7b-894f-88ce1f28b5e3 | -5.8711 | -57.752 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 468f872b-b2b7-3ad6-9694-9cf491b8a099 | -11.4968 | -45.1071 | 2026-08-28 20:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 2aece2d5-a898-3de9-9822-ad0a5f11e7b8 | -10.5149 | -59.6184 | 2026-08-28 20:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| a1297919-221a-376c-aeb2-aff7ca86b108 | -14.622 | -50.9117 | 2026-08-28 20:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 119.7 |
| af0155e6-a4c8-31e2-8770-fb6bd9087195 | -6.7652 | -63.054 | 2026-08-28 20:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 22edfbc8-9159-3de2-be6c-0dde8d6c11af | -17.988 | -50.1725 | 2026-08-28 20:10:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 77b3dc8e-e78b-37c1-ad2b-76016b3f3445 | -6.9272 | -70.0046 | 2026-08-28 20:10:00 | GOES-19 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 8e807cd6-a029-3960-b9e8-8a2df4b142b6 | -14.9389 | -56.3011 | 2026-08-28 20:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b7c0c89b-7670-3d14-a024-a7a1c0d701c9 | -11.0441 | -57.2421 | 2026-08-28 20:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 194.7 |
| 12649435-a517-3b02-9e39-203c5a67c1e1 | -6.7647 | -59.4601 | 2026-08-28 20:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| bd1a386c-e5c8-3c7a-aa53-7794b6646b5e | -5.2711 | -45.0946 | 2026-08-28 20:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 0cc5dd2e-6d7d-3d2c-b5cb-ab1ddd5de1fe | -12.3803 | -50.5823 | 2026-08-28 20:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 271.6 |
| 66c06fc3-b552-3773-b76f-117148a87542 | -8.0113 | -48.0161 | 2026-08-28 20:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 7e1a0671-bda7-3e4d-9550-5adb4d1b94a2 | -6.0004 | -57.6884 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 793c03ca-c200-3ac3-8316-d432d875fcb9 | -6.7833 | -59.4208 | 2026-08-28 20:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b7270d24-60ed-383c-b55c-3cfed8d6df09 | -9.9708 | -53.9419 | 2026-08-28 20:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| dd7802ee-0133-36ea-9231-e9b1a46fc159 | -7.5516 | -69.9963 | 2026-08-28 20:10:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 145.3 |
| fbea5141-795d-3a57-b868-4238469fd305 | -2.5516 | -45.3162 | 2026-08-28 20:10:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| c3966bd6-bf89-3933-a63d-99c5718f43f8 | -11.2493 | -45.0501 | 2026-08-28 20:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 8da7c6c7-e892-3e72-b864-bc95b8a2b677 | -14.8817 | -52.6293 | 2026-08-28 20:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e81b938d-6e6e-35d4-8709-f599335d3ca8 | -6.3467 | -44.0782 | 2026-08-28 20:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| efd84d8d-8373-3645-81dd-5dabef410cdb | -7.2903 | -72.845 | 2026-08-28 20:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5555fc55-49e6-330b-b921-6436cd2e3788 | -6.1472 | -57.7995 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7f7c6030-4c17-3459-8084-cb58b410a65d | -11.6215 | -54.5742 | 2026-08-28 20:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1cda7d33-5b4b-37f2-93e2-aa3b6cb6a2f9 | -11.0252 | -57.2436 | 2026-08-28 20:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 229.3 |
| fa5baf29-88c0-3788-b7e3-b6ab653d2252 | -14.9193 | -56.3237 | 2026-08-28 20:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 175.2 |
| db83a81a-ccc9-31bb-b54e-829436ba7327 | -7.4953 | -55.2862 | 2026-08-28 20:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| e6f2bb27-6165-35b2-8c6e-b854a282cee0 | -9.1711 | -49.9835 | 2026-08-28 20:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 41a56515-0831-3794-983f-50506fc17bbf | -6.857 | -59.4371 | 2026-08-28 20:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 7be1e2d9-942d-30e6-8524-dac9b85764ae | -3.1815 | -61.1613 | 2026-08-28 20:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 889d0ed8-f664-3d5a-9178-aa7b5a069ed8 | -6.949 | -59.4719 | 2026-08-28 20:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 215ea5e3-a678-33aa-b18a-7e4e6b9f7db4 | 0.1367 | -60.412 | 2026-08-28 20:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| f1145241-45e4-3d7f-b095-7b790ac2a43a | -5.4179 | -43.1752 | 2026-08-28 20:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 642.2 |
| 49adac86-b8e0-31a7-80ca-ad076ee4e0e0 | -5.4177 | -43.1986 | 2026-08-28 20:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 540.7 |
| 406a7438-134a-383a-9ab9-ee7db622a29e | -4.175 | -54.5761 | 2026-08-28 20:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 95a69fa8-314f-3280-8412-cf4d472dfd39 | -8.5366 | -55.2625 | 2026-08-28 20:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| e0b0c5f5-5d44-3733-8052-d50883dde35a | -15.577 | -56.2916 | 2026-08-28 20:10:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 2d6e3806-b2fb-350a-b989-c4150a72c979 | -6.7832 | -59.4401 | 2026-08-28 20:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 6479b60f-6924-3ac1-bb97-2efb04d28f34 | -7.5516 | -70.0146 | 2026-08-28 20:10:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 503ecd11-de7d-3040-8932-4112bbf14da0 | -9.1425 | -61.0069 | 2026-08-28 20:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 179.8 |
| b693e627-2ad8-3177-ac54-9ad210049966 | -14.4061 | -50.0319 | 2026-08-28 20:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e59b17f5-7d7e-3b7b-bcd7-4b48a3524935 | -6.4062 | -43.7494 | 2026-08-28 20:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e1539932-5842-326d-8490-41ed59f3e521 | -14.4057 | -50.0537 | 2026-08-28 20:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 1d103a04-f41d-333a-8157-e6418ece7d02 | -10.7598 | -54.0179 | 2026-08-28 20:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f0805d86-a0fa-30f5-b21b-469024594deb | -8.1617 | -64.0047 | 2026-08-28 20:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 01f6388f-9797-3ba8-a999-71d9d9f915e5 | -11.0244 | -49.6872 | 2026-08-28 20:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a0a1e9be-9849-3ffa-b453-254a19fcc7ec | -6.9336 | -58.9514 | 2026-08-28 20:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.6 |
| bc1fce06-1286-3c05-95ef-5e971612f425 | -14.1784 | -48.7703 | 2026-08-28 20:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| cdeaa79d-385c-352a-8f55-34a3c440111f | -13.8752 | -54.1153 | 2026-08-28 20:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b7cccbe2-6462-342f-b2e6-294325ac8299 | -14.603 | -50.8928 | 2026-08-28 20:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 229.4 |
| 0dcace5c-b738-379d-9ce6-3c0707ebc637 | -9.4329 | -51.6926 | 2026-08-28 20:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3df5d059-57fc-3be9-a75e-1fe700d4d093 | -12.3799 | -50.6038 | 2026-08-28 20:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 217.8 |
| 612839f1-f582-3d77-93d2-7b9de31ef9d9 | -3.6216 | -60.528 | 2026-08-28 20:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 97a0d661-536c-3d60-8751-ce5a8d7c10e7 | -5.251 | -45.2768 | 2026-08-28 20:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 9a73e961-9553-38a7-af41-bc8133eef310 | -6.8569 | -59.4564 | 2026-08-28 20:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 1449d2ea-79e5-34c1-afb8-9c8c7963e7a1 | -8.0303 | -47.9926 | 2026-08-28 20:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 31a66e87-6b26-3a36-8138-3ff72dd67985 | -13.471 | -57.0373 | 2026-08-28 20:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 361b5814-e7b8-3340-9614-db4666c281e4 | -17.9875 | -50.1948 | 2026-08-28 20:10:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 47ea539c-f4a4-382d-8a7f-2848d58845e7 | -8.8219 | -70.638 | 2026-08-28 20:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 87.9 |
| f839f19b-7443-32de-ac84-28f98cc38a01 | -6.894 | -59.4164 | 2026-08-28 20:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 38e94eaf-6742-36ed-bbae-3f51e3b2c665 | -11.0256 | -57.2038 | 2026-08-28 20:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 303.3 |
| fc1e15f4-7083-3dc2-89a7-5a194dcd5a6a | -6.1473 | -57.78 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b230c33c-b4de-334b-9ea8-01fd665b594e | -3.6216 | -60.547 | 2026-08-28 20:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| b6a5fe94-d66b-3001-b360-39842eac4eed | -7.5478 | -61.3056 | 2026-08-28 20:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 374.4 |
| a69bf2b9-fd36-3ee0-8253-4138720b4249 | 0.1549 | -60.393 | 2026-08-28 20:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 9107a35b-b015-3a1e-9b2f-02799e444e96 | -6.7653 | -63.0352 | 2026-08-28 20:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| b94ac6f0-cd51-326e-8e10-834dcf046ed1 | -14.1597 | -53.1219 | 2026-08-28 20:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 244.8 |
| 121ca0f0-6072-31fd-aa59-81a2016d4c5d | 0.1367 | -60.393 | 2026-08-28 20:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 507767b6-310f-353d-acc9-585362910db6 | -9.0012 | -57.5585 | 2026-08-28 20:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 340280cf-1a82-36a9-89ac-3ca9e3174513 | -3.3639 | -61.2527 | 2026-08-28 20:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| bb4dca0a-959f-3992-a0de-31d0ea36e07d | -9.1523 | -49.9853 | 2026-08-28 20:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 0784e5b9-4a0b-327b-a40d-07e740432f6a | -9.1976 | -61.1 | 2026-08-28 20:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 5eeb0472-385d-3f94-9284-df04e5426aef | -5.871 | -57.7715 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 93e1c9d2-dbc2-359e-b890-ec71a2aeb927 | -9.7838 | -46.3752 | 2026-08-28 20:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| ff25368b-8604-373a-84db-f74c558dd75e | -14.4856 | -58.5074 | 2026-08-28 20:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 299cb6e4-4c51-31e3-863d-56348dc6d44c | -7.5477 | -61.3247 | 2026-08-28 20:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 155.2 |
| bd80c00e-833f-35e1-8422-dd3731fb259c | -10.9589 | -50.2958 | 2026-08-28 20:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 5e2fd088-5579-3cfa-af3d-1cb6f0fae753 | -11.6212 | -54.5947 | 2026-08-28 20:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ab777b34-4bb8-3e6c-a305-4945ec747d69 | 1.2055 | -51.0389 | 2026-08-28 20:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 92.5 |
| f46c2d8c-91a5-3103-a5e8-ec10948be033 | -4.1934 | -54.5755 | 2026-08-28 20:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 6b5f71c3-72b4-3f3f-8577-99c0b78b5e8a | -6.8019 | -59.4008 | 2026-08-28 20:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 9cdad92a-d1c4-3c5a-875d-0e4bfd050ec5 | -8.0115 | -47.9943 | 2026-08-28 20:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| a30b78f2-8488-395c-92ea-cb9762cf7ed3 | -8.1432 | -64.0053 | 2026-08-28 20:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| de1d7484-1290-31b5-9db7-d9f667dad70f | -14.1594 | -53.1429 | 2026-08-28 20:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 27000306-cd29-34cd-b518-c4d23d49ebc7 | -3.913 | -60.9395 | 2026-08-28 20:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| f666cf5e-53b7-3266-87a1-1fe6fbf621dc | -14.1978 | -48.7673 | 2026-08-28 20:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 565983d4-ab69-3a48-944f-4bd0d76b126a | -3.913 | -60.9584 | 2026-08-28 20:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1df02f65-5bf5-323c-8b7f-d506e3bda44d | -5.3992 | -43.1766 | 2026-08-28 20:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 334.6 |
| a1668701-2f26-3942-a910-4e5e7fc909f5 | -11.2128 | -53.9976 | 2026-08-28 20:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |


[Clique aqui para ver as próximas entradas](README179.md)
