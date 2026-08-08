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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 502e803e-6406-37e8-a0c7-0837f9fc16bf | -15.38006 | -53.80012 | 2026-08-08 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b1e9448-fb82-3a01-9b6f-e48633500bea | -11.15904 | -54.85295 | 2026-08-08 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fb0d135-8fcb-35b7-8666-22882c6edd08 | -9.84432 | -56.07383 | 2026-08-08 05:31:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b941c78-f917-3793-901f-d4209311ad71 | -11.6171 | -54.57647 | 2026-08-08 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00f209bc-caaf-3b5e-a680-5952a86d296b | -8.78437 | -64.2147 | 2026-08-08 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b0fa21d-1a9c-3d12-9faf-78efc028f532 | -14.37329 | -54.97342 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 509bc264-eecd-36ad-b7b5-76b713de8c1c | -11.27152 | -55.86058 | 2026-08-08 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| bcfc2b2a-d8d7-3144-843c-00dbecd80b7b | -14.32311 | -54.99358 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fe8863d-28b8-347d-9416-38aa0321aff5 | -15.16495 | -52.74289 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 207526c5-e9a9-3b30-b0aa-3ef177f78573 | -14.33395 | -54.99163 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd68f772-6789-3f1e-97ab-2eb46d5aeb67 | -9.84368 | -56.07849 | 2026-08-08 05:31:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b3bc892-8db0-322d-a473-9a0d86603f5c | -14.37408 | -54.96687 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b7879be-1c57-340e-a3db-02129275b537 | -11.27309 | -55.86165 | 2026-08-08 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| acb44079-7373-34c0-a526-16bbfd726fb5 | -10.77555 | -62.93637 | 2026-08-08 05:31:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76580e7f-1b8f-3174-9528-cf243595f6e9 | -15.37884 | -53.79459 | 2026-08-08 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bea2bee-7a7d-349b-ab4d-44632c0c2ebd | -11.19635 | -54.84295 | 2026-08-08 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3f0fa85-5ef6-357c-b804-6455e84521fe | -14.16261 | -54.00321 | 2026-08-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa4f7792-65c1-36ac-b9f4-7b1bd758ae82 | -11.27623 | -55.86132 | 2026-08-08 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7653e4de-67a8-3fbe-845d-55c48c6ab6f1 | -14.32957 | -54.93812 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce9075bd-d725-3f8d-9052-9a8be7336e81 | -11.84316 | -56.94344 | 2026-08-08 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1be55a8-39b1-36dc-8e91-2e9805b8b152 | -15.16447 | -52.7473 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c819f75-fb9b-3b8a-a09c-522935c8d877 | -14.31787 | -54.99295 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3ada9026-99d8-3d2d-8d16-dfe87734dba7 | -12.32958 | -53.15756 | 2026-08-08 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 166e7eec-e949-3019-98a0-16a999de91a9 | -14.32908 | -54.98785 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4123409-4255-39f0-b769-0c81c8cabf70 | -14.15657 | -54.00659 | 2026-08-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 337b0762-68a9-35e7-8002-256bf4dd72be | -11.26839 | -55.86084 | 2026-08-08 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 335e1434-dadc-323a-89c8-d58d927d2821 | -14.31824 | -54.98978 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d3e9366e-ef81-3edb-8a32-6807770d8b36 | -15.70275 | -54.85672 | 2026-08-08 05:31:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 30199138-0ac9-3d96-ba51-5b7ba205a852 | -14.36806 | -54.97276 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2198eea1-de1a-3600-9c52-740192b6d9e8 | -8.5735 | -63.8562 | 2026-08-08 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 411d99dd-91cb-3476-abd4-595a4ec617ff | -15.14759 | -52.73572 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c3ea03e-2e2d-36c6-b7ef-1321b69876b1 | -11.27083 | -55.86576 | 2026-08-08 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3e1d09f3-6cb3-368e-9272-c0d649f5bdc3 | -14.31264 | -54.99233 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| acd6d66c-12af-34b3-b005-4f864890a9a2 | -11.24795 | -54.0241 | 2026-08-08 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67c205cc-cbf6-35db-8203-e4bb59557bd2 | -13.42987 | -57.04264 | 2026-08-08 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 910133a8-10fb-3ed1-89b2-f3670773abb3 | -18.36755 | -50.69314 | 2026-08-08 05:33:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3679c615-f43e-3a4b-a95c-18d0811ebe30 | -18.37467 | -50.69393 | 2026-08-08 05:33:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 553a51fa-c47d-3141-9cb7-2991964f5508 | -18.3663 | -50.70832 | 2026-08-08 05:33:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 93373f49-d9c0-31f7-abbe-d9e92098f006 | -18.3712 | -50.69685 | 2026-08-08 05:33:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 7dbf1fb1-e5e7-3ff6-a617-2d1427775402 | -4.2634 | -48.2016 | 2026-08-08 05:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 63817797-6b52-3e92-9785-3a9b67d2ce30 | -4.2634 | -48.2016 | 2026-08-08 05:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 4dcb6877-6452-31f0-98dc-7f3584c864d2 | -10.2662 | -45.7979 | 2026-08-08 06:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 3e5c8ff4-fc0b-36d0-8e89-1d271a2b923c | -4.2635 | -48.1799 | 2026-08-08 06:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a9935877-16c9-3475-ac0d-a72f4a9dd05a | -4.2634 | -48.2016 | 2026-08-08 06:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e78a7e2f-e765-344c-a252-6a10b575f69e | -6.89267 | -59.89569 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c7d8e95-128d-33af-951f-f9e0948fd0e2 | -6.9603 | -60.14208 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b72edc0-405a-3822-97f1-eeebe9c6019b | -6.70942 | -58.95166 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ae05770-e7c4-38e9-8a76-29c53eeb5644 | -6.84049 | -58.97635 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23319ca4-9120-36e0-8422-4ce1dfbc85a0 | -7.54973 | -61.15578 | 2026-08-08 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e22d8312-c80b-3faa-b87a-475614c138be | -8.16617 | -55.41813 | 2026-08-08 06:05:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6b01d83-3ba0-35cf-95eb-79e2c90725c0 | -5.88425 | -57.64922 | 2026-08-08 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7fbd186-bfd6-3035-a878-3b522ef014ce | -6.28851 | -64.15427 | 2026-08-08 06:05:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 49f64c0f-cdd3-348b-9740-da006495e528 | -8.68564 | -62.8662 | 2026-08-08 06:05:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b48da4d0-1d47-31c2-b7f1-158842f4c4ac | -8.14761 | -55.41674 | 2026-08-08 06:05:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| aba652bd-d9b2-31bf-9fab-791022204554 | -6.88698 | -59.89805 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88f3fc1d-26b2-3e42-b272-b474cfa3b9a7 | -6.8471 | -58.96978 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcb3f77c-6240-3edc-ab14-30034ba96946 | -6.70839 | -58.95911 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79caebaa-fd36-3d42-a5dd-570918af5957 | -8.76129 | -64.07182 | 2026-08-08 06:05:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6daaf5f-4bd9-3dea-8a70-a7a4190d4add | -6.88654 | -59.90121 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a479f76d-7939-33fe-86ad-ed342758f015 | -6.70891 | -58.95539 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 899a8b08-b4da-34c7-bada-e115e0a663b8 | -7.55658 | -61.15915 | 2026-08-08 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f64fca94-c31f-36fa-959e-d7ea9d3607a9 | -6.7346 | -58.58708 | 2026-08-08 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3369d62a-dfa0-377c-9f04-43dc8fbecb86 | -6.89222 | -59.89887 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e394eb0e-e755-3a32-bca9-81be43d297a8 | -6.73066 | -58.5851 | 2026-08-08 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 770d586c-2246-3947-9067-3571ada6931c | -8.6851 | -62.86963 | 2026-08-08 06:05:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d876c845-3ffd-3f6d-9729-41ea71a16722 | -5.88364 | -57.6537 | 2026-08-08 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b57619cf-7481-3f06-99c5-ab6a99beb82a | -6.72883 | -58.58661 | 2026-08-08 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a4f0ba7-1323-3ca1-bbc8-3aac07d1e4c3 | -8.85356 | -63.54402 | 2026-08-08 06:05:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98307d0d-28b2-3ff0-9e1c-4f5a0c1a6320 | -6.84659 | -58.97348 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6060cd1b-90b6-308d-887d-763796e9f96a | -7.55171 | -61.15849 | 2026-08-08 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae17b753-1ed4-3a03-abaf-5f4a1adc50ef | -8.68502 | -62.87047 | 2026-08-08 06:05:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8998999-f215-367c-a91a-60f8fec8653c | -6.88786 | -59.89165 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76e76931-36ad-3c86-846f-7ecadba36096 | -8.68063 | -62.86983 | 2026-08-08 06:05:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e01814c3-e2c3-3a3c-b38c-f0c125fc191a | -8.6895 | -62.87026 | 2026-08-08 06:05:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41e4a817-db78-3ba8-9c70-553eb4f6bfa2 | -6.2846 | -64.15368 | 2026-08-08 06:05:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1a9afcf9-a48c-3110-840c-ba01e8d8f63a | -6.28534 | -64.14877 | 2026-08-08 06:05:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1292b6f6-cb60-322e-833b-75797d257edc | -8.84936 | -63.54338 | 2026-08-08 06:05:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c2c4324-00b3-3961-b439-9ca3aba723ee | -7.54896 | -61.16101 | 2026-08-08 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 309fd4de-6836-3c7b-8ee0-ea5506577fb4 | -8.6807 | -62.86897 | 2026-08-08 06:05:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f79adfd5-b1ba-3dc9-8a17-926011d20f5b | -6.83997 | -58.98006 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11f3812f-fb1e-3451-8e61-459cda43af79 | -6.70994 | -58.94791 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf9afc7b-d908-3d55-9d80-5bffa37025ed | -8.14674 | -55.4236 | 2026-08-08 06:05:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 20181f25-2530-3136-8744-9cfc30da28e4 | -8.78619 | -64.21346 | 2026-08-08 06:05:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c93f40fd-c7cd-31f4-8311-65fcbfcbe616 | -6.89311 | -59.89247 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd78d125-6cf0-3c6a-ae0e-c7f72d6bef68 | -8.78216 | -64.21288 | 2026-08-08 06:05:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5dd5f6ee-4b2b-33e6-a017-c64bffb01fc4 | -3.8392 | -59.29862 | 2026-08-08 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b07d3299-a76b-3910-a266-e31532fa3830 | -5.88244 | -57.65219 | 2026-08-08 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c9282bc3-6bfb-384b-bb8b-1ad46ea37de2 | -3.83958 | -59.29871 | 2026-08-08 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84357a49-c8e4-38fc-ac53-ef39ecb539e6 | -6.88742 | -59.89485 | 2026-08-08 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 589ec962-ea35-396d-bf54-ebad4b29a2c3 | -7.55099 | -61.16375 | 2026-08-08 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a436ca5-ade3-3ce8-8f4a-3d2ef174d917 | -3.83913 | -59.30185 | 2026-08-08 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 707a54c6-9897-37b4-a3ce-9310ca7b13c3 | -3.83873 | -59.30175 | 2026-08-08 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d8db09d-8a53-34bc-9835-46b8697fa99a | -10.94398 | -68.74762 | 2026-08-08 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d10b5c5a-6d85-3aa6-a50c-91e4944a78ab | -11.27788 | -55.85075 | 2026-08-08 06:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 490cf9b3-93be-3014-84a1-4344054bb343 | -11.27249 | -55.85929 | 2026-08-08 06:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e4bda3a8-51ff-378a-92eb-33de93b53920 | -10.9459 | -68.74726 | 2026-08-08 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f8e96a6-4ca5-3f3a-8e6f-aeb8308d5499 | -11.26992 | -55.85678 | 2026-08-08 06:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8b9ce5c2-4b86-3c36-9354-489dfb9d3f33 | -11.2708 | -55.84914 | 2026-08-08 06:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6729ae4f-d246-38dd-b834-68409d482018 | -11.27331 | -55.85178 | 2026-08-08 06:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5b6bcc25-220e-3d01-a613-cfb6069d5780 | -4.2634 | -48.2016 | 2026-08-08 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |


[Clique aqui para ver as próximas entradas](README23.md)
