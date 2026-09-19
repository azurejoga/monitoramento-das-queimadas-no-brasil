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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f0125c6-b0bb-3b5b-bfc0-1d91b1f030b5 | -10.68944 | -60.73988 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59d0e90c-bc01-3011-a36e-ecdc20a701c6 | -10.69914 | -60.72671 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75744227-5886-3c8a-9930-3e75b16bc426 | -8.42617 | -54.73103 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9884f9f4-b889-33cb-93b5-64b626d80e7d | -10.71308 | -60.72331 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef3092bd-f5d0-38b1-a2ce-ed06e1031a29 | -10.71149 | -60.73516 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a7f66b0-b306-3967-89f6-7031835fff4e | -10.92721 | -53.9716 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| def084be-9e37-3f55-a8d4-78c298ba3a78 | -7.83505 | -55.4145 | 2026-09-19 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c077df51-8162-3af3-8022-1080a82989b1 | -11.67842 | -54.45079 | 2026-09-19 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ec61890-6d5c-38a2-ac4b-6f1b9375b425 | -10.22939 | -57.83116 | 2026-09-19 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 800680a2-5060-325b-86ee-64b7a77a17de | -10.8836 | -54.06339 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 90d22f3d-3661-34d3-b8f0-512c22d23b2b | -10.71623 | -60.73181 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 045113fa-3f6e-3b8f-8fc6-04d1a3f570bd | -11.02109 | -54.13403 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef948155-b477-3948-a259-267db54623b9 | -7.55555 | -61.32351 | 2026-09-19 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ebb37436-e54f-354d-8c4b-8ebe52a2eee1 | -10.69384 | -60.73391 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5045c0a-b9ef-3627-b60b-aec8ad35e581 | -8.50077 | -57.62971 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a910564f-52e8-3830-9a82-3c3b03e0075d | -10.91403 | -53.98165 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2167dbb8-18eb-369d-994e-bfef347a0387 | -10.92925 | -53.96614 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11a3e1cc-208a-3990-a75c-b3e8d3fd0c7f | -6.7682 | -59.42615 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4da6046-404c-380c-a06d-70c87a1f643a | -7.57015 | -57.67299 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 709a6c1e-f94f-3bb5-80fc-f3c477acd12d | -10.88295 | -54.06917 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f9c156dd-a3a9-3a09-8352-5567f787d2d1 | -10.6952 | -60.72876 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 680e68b6-e2fb-3d98-899d-e506ef2a923d | -10.72097 | -60.72844 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5bd1d65-bc83-3047-9a52-628ad1af8228 | -12.27002 | -57.18105 | 2026-09-19 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cd90e23-1bf2-339e-86ee-f8a95023c72a | -10.92787 | -53.96578 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c503d317-ff24-3298-929e-17130d9dfc98 | -8.61071 | -54.60475 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28bf37bb-0850-3428-91fe-97860dc51f54 | -8.27052 | -62.7382 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e095666-a4de-316e-b9b8-83437305cc5e | -7.57779 | -57.69134 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a10aaaa0-66d5-37c8-a306-20dd27255351 | -7.98334 | -71.34151 | 2026-09-19 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c97b2c59-c90d-32fe-b736-18ca54f6f911 | -9.93574 | -53.98611 | 2026-09-19 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 997c1127-6ca5-3353-848d-4b8c5f85f157 | -6.80222 | -59.16195 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dee43d04-0587-3a59-8582-eb820a66e074 | -10.69859 | -60.73062 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cef5f4c9-99f5-3ca5-b591-a2d9a3a3c5e9 | -10.69993 | -60.72546 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2a21e23-c250-37e6-9c05-5b2b3cd25fd4 | -10.87709 | -54.06845 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1f60c35-3450-3c70-833f-ca0dc393b82f | -8.6125 | -54.59015 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70ba5a0e-0e16-388f-8587-867f2546b87e | -10.86786 | -54.09044 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d724f40-e5bd-3969-8a8e-76e8e4c253b1 | -6.77009 | -59.42459 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4a44ffe-88ff-39c0-8e02-91d8248234e3 | -10.86593 | -54.10688 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16b34481-f269-352d-8b8e-c157d57b3dfa | -10.8843 | -54.06364 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e6ba7a15-68a8-3121-89d2-b306a6b083ac | -10.85938 | -54.10626 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed16a793-3296-31f9-8697-bfd40834acb0 | -8.71043 | -62.54149 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a6c73ea-b55a-3121-ae5a-f1546c874d37 | -12.02386 | -55.54647 | 2026-09-19 05:44:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30a0413e-b502-3a3f-9a29-5dd7adf3041e | -10.86491 | -54.11221 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52bc859e-a1c1-3578-ba72-eeb066147b4d | -9.88286 | -58.3032 | 2026-09-19 05:44:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4329b754-846d-3cd7-bd97-0e7c538ca596 | -9.88778 | -58.30379 | 2026-09-19 05:44:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e645b24-e932-3080-a1b4-d50182822d38 | -8.00924 | -61.37385 | 2026-09-19 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cea10360-7b74-3e89-b344-17b3df086f35 | -9.10852 | -60.95029 | 2026-09-19 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dcd2c2c-4ff0-3c6e-b593-8db6dd0bf6c7 | -10.87375 | -54.09673 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a79066d-117d-3752-ad7e-bdf9415dd1b1 | -10.87642 | -54.06821 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c60beb80-f0ec-3c41-86d9-cd7f31a2a6df | -10.69468 | -60.73268 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abcf624c-4953-327d-bb9e-21ee28b43041 | -9.54645 | -63.77694 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a94a7767-a136-3153-8137-6989ebd32076 | -10.72043 | -60.73239 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79ffc4ab-edfb-320e-afbb-ec90c40026c6 | -10.69836 | -60.73724 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92dd8adb-f04d-3d6d-a9ba-4f17ae7c9837 | -18.68166 | -54.84884 | 2026-09-19 05:46:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b8fa5b87-cdca-3e57-b760-f93ee2abe049 | -18.68021 | -54.84479 | 2026-09-19 05:46:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c7e011b1-6a88-39d3-841d-4e8b041aa96c | -18.67968 | -54.85098 | 2026-09-19 05:46:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a71af378-e0e6-36f4-825e-790a775f4659 | -16.31028 | -53.85738 | 2026-09-19 05:46:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 19c3df99-6349-3443-bc5a-d7bc12b7d35e | -16.31732 | -53.85803 | 2026-09-19 05:46:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c178e17b-f184-3fad-9c75-0c15b2a8d441 | -10.6928 | -60.7322 | 2026-09-19 05:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| da7edd8d-e664-3a71-b246-5a6dbb644e28 | -10.7115 | -60.7312 | 2026-09-19 05:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| aa8f1b12-1c32-3f49-8499-50dc9c78d082 | -18.0274 | -51.0709 | 2026-09-19 06:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 44a521d5-aa0a-3abe-bd7d-eecef18d9984 | -10.6928 | -60.7322 | 2026-09-19 06:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 46cd3144-8d1f-3856-a9d5-346ae3e8f4f0 | -18.0303 | -50.9385 | 2026-09-19 06:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 9203622c-ec88-3bad-936b-bf073ed975c8 | -10.7115 | -60.7312 | 2026-09-19 06:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 4b7cda19-8fca-337b-9cd9-e01a7bf46599 | -10.7114 | -60.7505 | 2026-09-19 06:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 42eda4f0-9fbc-3376-bc57-a6dfb9773e84 | -10.7115 | -60.7312 | 2026-09-19 06:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 607511e4-7538-3159-bcd0-0debe8302c25 | -10.7117 | -60.7118 | 2026-09-19 06:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 61e1ea92-a12b-3aea-bfa7-ceca00d528ec | -18.0274 | -51.0709 | 2026-09-19 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 4f3b4022-a4f2-3f87-b36f-2c20f4b9104f | -10.6928 | -60.7322 | 2026-09-19 06:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 4baf7b1a-2420-3c0d-bacb-a3085efc59dc | 4.07713 | -60.0174 | 2026-09-19 06:16:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 887ab6a5-c6e6-3380-a593-2874fa06d2b8 | 4.07767 | -60.02055 | 2026-09-19 06:16:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5cb7b1c-bea2-3be9-a4ec-7d3692543452 | -3.35003 | -59.85931 | 2026-09-19 06:18:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ecfd72c-656c-3e05-848f-cd94e3dc78ce | -2.89144 | -57.80646 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| f5b62671-46a9-397f-b48d-1818318f8c91 | -3.33865 | -59.81018 | 2026-09-19 06:18:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14c46346-1346-30fb-9cb2-de3b8ce9b56f | -3.33045 | -59.82308 | 2026-09-19 06:18:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 23ec205f-67b1-3375-b3c7-a1b15fb3ee8a | -3.38234 | -61.30105 | 2026-09-19 06:18:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1f6d9e9-5125-37d5-be9d-060af44852e1 | -3.14335 | -61.4 | 2026-09-19 06:18:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6acc054b-2151-3322-8f7f-740ae6272f97 | -2.89942 | -57.80137 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 360f87b9-5669-336c-abab-a6ccdc3c751a | -3.14283 | -61.40358 | 2026-09-19 06:18:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56009514-e481-35cd-ba9e-6363cda4415b | -2.90615 | -57.80222 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 618d4be4-a4b0-3004-8c8f-97711debffe3 | -2.89428 | -57.78755 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 13942867-636a-3005-85a3-41bf580066dc | -3.6957 | -60.61271 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe2d3c99-ab4e-3c93-a723-4891298144a1 | -3.69379 | -60.59768 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4a81966-6951-3583-b994-91cd6a99f59a | -3.33795 | -59.81482 | 2026-09-19 06:18:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d929ed28-5d9b-32c1-a011-abbe5cae9a88 | -3.69065 | -60.61831 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 860cc772-1c18-3485-8836-b0ea8bd9407a | -2.90425 | -57.8148 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7160c79e-4e02-3e90-93aa-5a0181141b7b | -3.35614 | -59.86021 | 2026-09-19 06:18:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68c0e3d5-337a-321b-83a9-3680ece1a0ad | -2.89238 | -57.80015 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 4812cfd9-dc37-39ee-a818-dc349257c806 | -2.90033 | -57.79505 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d1cde858-c672-3e03-94de-27caac0ff00d | -2.90721 | -57.79612 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7a07b98a-0346-3da4-820d-e0a9f30d176e | -3.37624 | -61.30386 | 2026-09-19 06:18:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5b1563e-aaa0-3044-a628-699f53ced9d5 | 1.32657 | -60.71103 | 2026-09-19 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df735e92-cc51-3d5d-828c-53d88354ba6a | -2.9063 | -57.80242 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 30172592-99af-3a19-b1cb-3cf69b46bdc1 | 1.31143 | -60.40731 | 2026-09-19 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2124579-b538-3361-9b12-97c1b500a589 | 1.31164 | -60.40766 | 2026-09-19 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0afe6c5f-c9fa-3d6e-ae56-4ff55e556e8d | 1.32712 | -60.71439 | 2026-09-19 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3a00e97-9a0b-3459-badd-89309427ad65 | -2.90022 | -57.79489 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 16063f9d-9404-3c3c-a869-8aa811330200 | -2.90449 | -57.81503 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 32a1104f-c1d6-3f6e-949d-ba0ba2c89710 | -2.89333 | -57.79385 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 3cd9ad04-8d83-3506-bfdd-fd1169478d6c | -3.6919 | -60.61007 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bafd81c3-4419-35c2-9304-e9dbc69c70a8 | -2.8976 | -57.81399 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |


[Clique aqui para ver as próximas entradas](README99.md)
