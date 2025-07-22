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
| 2d530632-057b-3124-a296-aa17bb1dafd7 | -8.96364 | -62.24105 | 2025-07-22 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f75d77d2-2a68-3a5b-af7b-60364f684464 | -11.31157 | -55.11679 | 2025-07-22 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8bf4cd6-dc2d-3492-b27f-742306fb75a6 | -7.29626 | -60.16427 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f8b30f4-ba3e-3515-a87f-a7b1b776d2de | -7.95412 | -71.46316 | 2025-07-22 05:42:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e0289a1-f5e7-3331-92e7-14d26f2b49a8 | -11.30455 | -55.11783 | 2025-07-22 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b687dc50-46b7-3012-a92c-75ca1deb6f41 | -7.96971 | -55.30096 | 2025-07-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bf2b38b-fdf5-310b-a7fa-f907007c2ea2 | -10.10069 | -58.22117 | 2025-07-22 05:42:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8d97a74-c0cd-3172-b9cd-76733ce0c366 | -7.26918 | -60.17569 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7904ab2f-29bf-35ea-b82e-75abe2dbe45c | -11.31071 | -55.11862 | 2025-07-22 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3fabded-cb23-3ef7-866a-ea3b9a0c3d39 | -10.05036 | -59.0942 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 322f17e9-51cb-347f-bbf6-27160d0681e3 | -10.04805 | -59.10139 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5df7e4f-54e4-397c-bbcf-ca5608286511 | -7.28217 | -60.17369 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 064d3167-07ad-3091-bfa3-fe56f0331875 | -9.0017 | -69.53627 | 2025-07-22 05:42:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55d540c4-8951-3e35-941d-292503cb34ca | -10.2984 | -60.54138 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aedd141c-c513-3a85-81e7-1160fb0a35da | -10.04968 | -59.09908 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e8cd265-2bcb-343e-a921-d098c9a53883 | -5.13462 | -60.36462 | 2025-07-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2a5ea60-fea0-3f50-92e2-82b046f0c0d0 | -7.26449 | -60.17884 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60e05923-a6f6-3694-84e4-8c95fa904c3b | -10.03575 | -59.09706 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6052f05c-d0c2-3a05-a85e-40299d141e03 | -10.09799 | -60.49451 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b65c956e-ad56-384e-80d8-b61b8100446e | -10.10381 | -67.74857 | 2025-07-22 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c4d253d-5b1f-32cf-ba0c-f792e7aeefba | -9.00244 | -69.53192 | 2025-07-22 05:42:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26da4511-5cac-357f-8772-47efe66f61a0 | -9.55556 | -65.98843 | 2025-07-22 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98a64b67-a527-3aa9-8e51-d903837dda0a | -9.62154 | -67.282 | 2025-07-22 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f67b882a-4831-3117-873c-2849acf087fc | -7.2957 | -60.16806 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aabcfd2b-d8ae-32fe-b124-b3288732cb76 | -10.09994 | -58.22681 | 2025-07-22 05:42:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1caa585b-fb5b-30f3-8ad4-7cf130f7b40d | -7.23695 | -60.19384 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6007eb28-9d58-3576-be17-569926acadb7 | -8.74614 | -63.93141 | 2025-07-22 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 890142cc-6d84-3df1-8bed-d8e73fd876e0 | -7.27802 | -60.17309 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b9a9dfd-9aac-389b-8767-3961c9349e49 | -7.97457 | -55.30737 | 2025-07-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9cfe833-8dcc-34f9-877c-34a99ece2cc6 | -7.27748 | -60.17683 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11f42b26-fe04-309b-a7da-993f31758b7d | -6.2167 | -57.77213 | 2025-07-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a65849c-4044-38da-b1ac-4a0bcdfba3f4 | -8.49471 | -64.04293 | 2025-07-22 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97024813-2721-3399-8a94-0b106e1cb900 | -7.29155 | -60.16746 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6f64e81-a5ff-3ee4-b318-e9d2d54594dd | -10.05501 | -59.09487 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0d23669-3a3f-3d06-aee8-60a0f70de563 | -7.27277 | -60.18005 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00c2c048-70a7-36da-a6c7-024c970f3610 | -8.95992 | -62.24049 | 2025-07-22 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2d6a94b-45f0-3344-b405-fda6f2a1ddb7 | -9.00274 | -69.53378 | 2025-07-22 05:42:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 470cac17-cc98-3f4d-8549-23e3c9536f8f | -7.24576 | -60.19138 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cbc8cd0-b2aa-3555-bf4f-9c7f2ed668e8 | -9.38425 | -66.57867 | 2025-07-22 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e54d203-899b-3b7b-b6b1-0bf352588051 | -9.79094 | -64.88717 | 2025-07-22 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1c106d7-fc7a-3c55-a77b-5e4e18fca3fe | -7.95479 | -71.45926 | 2025-07-22 05:42:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98109199-40af-38db-901f-0ba7aeb8e261 | -8.94422 | -64.12536 | 2025-07-22 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca7d31d5-fc8e-3f62-a242-31965e9bd738 | -10.05432 | -59.09975 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bad45d7b-d7d6-3f55-8e8f-cc3139b83956 | -10.03941 | -59.09512 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a19c2e1d-3376-35c1-943d-5c15784a3b20 | -9.69092 | -62.30886 | 2025-07-22 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26327670-8ab0-3a13-8123-a300a059ef8e | -7.23283 | -60.19316 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14de779d-16eb-3371-9796-c6ac80857649 | -10.04504 | -59.09841 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e8ee9e5-8962-3bda-98af-0af57f6e661a | -12.4945 | -57.76946 | 2025-07-22 05:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 482c8a62-0880-3443-898b-ab9dc925e625 | -11.94228 | -63.8502 | 2025-07-22 05:44:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1b1baeb-94bb-3c11-a4cd-7f3c3e2ed72f | -12.26048 | -63.82317 | 2025-07-22 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b730b39b-1508-3a8d-9c56-418b63775b34 | -12.49327 | -57.77949 | 2025-07-22 05:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ff9888e-2564-3339-bd90-666c2f7a6732 | -12.49935 | -57.7735 | 2025-07-22 05:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ded3e150-7307-39e6-802e-cce51bbf023c | -11.94802 | -63.17914 | 2025-07-22 05:44:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9458e572-4078-347b-9ef3-c7fb3e0da5e6 | -12.49895 | -57.77684 | 2025-07-22 05:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 554ae720-74ae-31a0-936c-2435dd082f8a | -12.49977 | -57.77012 | 2025-07-22 05:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 00945248-c0a0-3aca-997d-f309cca91b4a | -12.50019 | -57.76667 | 2025-07-22 05:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 76129ae2-fb1b-34b5-b50e-8cb897c650b2 | -12.49368 | -57.77617 | 2025-07-22 05:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08ca03e9-df4d-3fa0-889c-9a8f02468542 | -8.5211 | -43.3063 | 2025-07-22 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c3fac6a4-d32b-34fb-89be-c24518fdfeed | -11.7317 | -48.1849 | 2025-07-22 05:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 23cd850d-af0e-3580-92cc-ad5b4c0c8ebc | -7.95404 | -71.46349 | 2025-07-22 06:33:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9ce1f6a-f02d-3fb1-8eb3-44426769790e | -7.95374 | -71.46111 | 2025-07-22 06:33:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2150d308-7d19-3181-8142-b8351efc4d62 | -3.1833 | -49.4429 | 2025-07-22 06:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 807bbbfa-40df-3596-bb46-21ef1ebdd19a | -3.1833 | -49.4429 | 2025-07-22 06:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3c99124b-3cab-3009-aa52-4ec7d625b143 | -7.27554 | -60.17518 | 2025-07-22 06:54:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 62087b30-caf1-3006-8a07-423865d91968 | -7.24208 | -60.18628 | 2025-07-22 06:54:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f716b8cb-5e95-3013-80cb-5cdca7b39305 | -12.49198 | -57.76628 | 2025-07-22 06:57:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c0ecbe07-0a41-3352-b9ad-a0990250ec15 | -6.5631 | -51.1126 | 2025-07-22 07:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2922e91e-d1c0-3607-9f66-ae5f93bd6cf0 | -4.3693 | -43.2907 | 2025-07-22 07:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 2f3b2211-56cb-34f6-b6cb-9f0e8f8f6fa0 | -4.388 | -43.2896 | 2025-07-22 07:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 6b0c819c-3af6-3efe-9f15-8c4461334881 | -4.3879 | -43.3129 | 2025-07-22 08:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 05f4749b-1ed9-3042-a1ec-145928c7fadf | -4.388 | -43.2896 | 2025-07-22 08:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 0a6e49a0-4f4b-3e08-b852-37f17516a145 | -4.3692 | -43.314 | 2025-07-22 08:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 665d85f8-9b09-3823-b929-40f990ec8f24 | -4.3693 | -43.2907 | 2025-07-22 08:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 191.0 |
| a9469be1-256c-30b9-b593-e6ff2f3a09a7 | -4.3695 | -43.2674 | 2025-07-22 08:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| e2e53dda-3bfd-3538-94c1-14b36e8a17ab | -4.388 | -43.2896 | 2025-07-22 08:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5885a40d-0f12-367b-b8d8-ef04ea5f66a7 | -4.3693 | -43.2907 | 2025-07-22 08:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 34021e94-760a-308b-aac3-946cb9d3b1eb | -4.388 | -43.2896 | 2025-07-22 08:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f90d9f42-8f63-3bea-b75c-47e2e83828c3 | -4.3693 | -43.2907 | 2025-07-22 08:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b55bf34b-98d5-3655-8959-54b2908fd32c | -4.388 | -43.2896 | 2025-07-22 10:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 67a556d3-b26b-388d-b825-9441339ef725 | -4.388 | -43.2896 | 2025-07-22 10:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 1c1c4ce0-5c2b-364b-9264-8c767cbd6014 | -4.388 | -43.2896 | 2025-07-22 10:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 42f906cd-c152-3558-92dc-5eb103dde8d6 | -4.388 | -43.2896 | 2025-07-22 11:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| ec8930c4-9496-3d6e-a214-c0a3864cacdd | -4.388 | -43.2896 | 2025-07-22 11:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| f784b2fb-66e4-3f21-b3f5-4e700a92529a | -4.3693 | -43.2907 | 2025-07-22 11:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 8abb2764-4c17-3e06-820c-eb82737476c2 | -6.9801 | -42.809 | 2025-07-22 11:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| b14f9891-23f8-31e6-8f21-3021aef0fc62 | -6.9804 | -42.7854 | 2025-07-22 11:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| f5e4c5fc-8b89-36a0-92f3-971c2d7c28ad | -4.388 | -43.2896 | 2025-07-22 11:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 199.0 |
| b21c4d3d-e295-3436-a3df-3f5ba41060fa | -4.388 | -43.2896 | 2025-07-22 11:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 240.9 |
| d8765078-17fc-35d9-95d7-6ba67cdb8d5d | -4.3693 | -43.2907 | 2025-07-22 11:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| b3eccf95-0db5-3c92-a941-3611f60f2de5 | -6.5752 | -45.6096 | 2025-07-22 11:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| ac0adf11-0f7b-39de-9636-0b15386dce4c | -6.575 | -45.6322 | 2025-07-22 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d6fe9ea5-c99b-3df6-b07e-a59cd5561c83 | -6.9804 | -42.7854 | 2025-07-22 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| f53ab6c6-c468-3929-afd7-84a43bac8007 | -6.5752 | -45.6096 | 2025-07-22 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| c20aa868-c384-39ff-ab86-6d27042c1ce9 | -6.9804 | -42.7854 | 2025-07-22 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 3a838089-cbf1-32c9-93bc-e28497efd1b2 | -6.5752 | -45.6096 | 2025-07-22 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 81891391-3906-36d2-a06f-6fe86d250fb8 | -6.575 | -45.6322 | 2025-07-22 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 4ecb984a-8794-3be2-aa66-10a44f106c71 | -6.9801 | -42.809 | 2025-07-22 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 1f3c2203-9884-3fcd-95d1-e48b6a17b6b2 | -6.9804 | -42.7854 | 2025-07-22 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| ce0e1bc8-f863-3183-bf94-9214b9e788a0 | -6.9801 | -42.809 | 2025-07-22 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 129.5 |
| 87ef5705-6a39-3407-a002-36bc5444b9e7 | -6.9804 | -42.7854 | 2025-07-22 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 117.4 |


[Clique aqui para ver as próximas entradas](README21.md)
