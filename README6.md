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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8c26f46-a6c5-3ec9-9c11-f790466e00bf | -15.1559 | -41.5566 | 2026-08-14 01:20:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 186.3 |
| ffde52b2-9e5f-3c15-9819-d3ce42662ceb | -16.8994 | -54.1509 | 2026-08-14 01:20:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 30df8fa1-31e6-3fc9-acdc-66f5588f4d12 | -6.6194 | -59.0609 | 2026-08-14 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d78e4e42-ccf6-3e86-ad4b-60b9015a300b | -6.6195 | -59.0416 | 2026-08-14 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.4 |
| e29bba7b-771d-3456-986c-e6113c98e068 | -4.4869 | -42.5336 | 2026-08-14 01:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| c3c62f3e-141a-3233-8f97-b0a285ed8245 | -13.2415 | -54.2476 | 2026-08-14 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 6b799d8b-dca0-3690-9479-7965b0e08361 | -6.6195 | -59.0416 | 2026-08-14 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 8ebca0b0-9e59-38fb-bccf-a6f4a513f622 | -16.9191 | -54.1481 | 2026-08-14 01:30:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 249.0 |
| 5d1ab4d0-b1b7-3f1f-afb9-372b85344c04 | -14.4734 | -45.6914 | 2026-08-14 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| d18b73e4-6cd4-3236-8f59-239fed43499c | -4.4868 | -42.5572 | 2026-08-14 01:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 02216aab-7ad2-3950-89d9-cd78465cd90c | -6.6194 | -59.0609 | 2026-08-14 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 31249671-397b-30b1-90aa-a895d4f2b821 | -13.5701 | -46.2584 | 2026-08-14 01:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| af7fba88-44a6-3593-bedc-417e65f8020f | -13.2413 | -54.2683 | 2026-08-14 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 08d5f7bf-c547-37ba-a405-d61212205bd7 | -6.9145 | -43.6351 | 2026-08-14 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| adaede8a-9c1f-3349-887d-7c3058ba1e4d | -16.9195 | -54.127 | 2026-08-14 01:30:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 7901a939-a6ed-37c6-97c5-cf7059ae1d98 | -11.4885 | -54.6273 | 2026-08-14 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| b5ab95bf-ec4f-34e0-a246-474e754bf9b4 | -4.5057 | -42.5325 | 2026-08-14 01:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 124.2 |
| 3d318930-dbd4-366b-9068-10aefd70d3af | -21.9049 | -55.3755 | 2026-08-14 01:30:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 98.9 |
| ab5d905e-672c-3720-a5a5-9eb4a9b20607 | -4.5055 | -42.5561 | 2026-08-14 01:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 138.0 |
| 9605b599-60a0-37e1-bdd0-3298a8661506 | -21.9054 | -55.3538 | 2026-08-14 01:30:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 03a0f31c-7840-3cf0-9ffb-7f6222633f6f | -14.4734 | -45.6914 | 2026-08-14 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 80c67bad-f48c-3a7c-bf9e-ac47b8857dad | -11.5074 | -54.6256 | 2026-08-14 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 660b70f4-dbc8-3ee0-acb7-2f3465c70f2d | -11.4885 | -54.6273 | 2026-08-14 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 577a22ff-7f4a-379d-a6e7-d869020a134a | -6.9145 | -43.6351 | 2026-08-14 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| fe58973d-0121-360d-99e3-482013f2f0de | -21.9054 | -55.3538 | 2026-08-14 01:40:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a019ad18-86c8-31af-9c0b-688c6f560171 | -16.9191 | -54.1481 | 2026-08-14 01:40:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 83f04f51-71e8-3c7b-b1c1-b10e37a07a03 | -6.6195 | -59.0416 | 2026-08-14 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 23b5c766-ba56-3c56-9e66-1b5bebdf0975 | -13.2415 | -54.2476 | 2026-08-14 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| a3ba8cf5-d706-3803-ba28-32d8b49ad8b8 | -13.2413 | -54.2683 | 2026-08-14 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 608b78c8-6c15-3ee0-aad0-52a22d10af9f | -4.5055 | -42.5561 | 2026-08-14 01:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| b561f08d-91fa-311c-8d1b-86ad67507136 | -4.5057 | -42.5325 | 2026-08-14 01:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 154.2 |
| 8dac56c3-76fb-38c6-b91d-0c9a30cc1f0c | -6.6194 | -59.0609 | 2026-08-14 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d58b402b-60ac-3872-a10f-fc4d2f95fa12 | -21.9049 | -55.3755 | 2026-08-14 01:40:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 30679a47-ff85-3ea8-ad49-679af8f51084 | -13.2415 | -54.2476 | 2026-08-14 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 63caba8f-833b-3db6-a12a-0c7a683e0207 | -21.9049 | -55.3755 | 2026-08-14 01:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d9f56ecf-e351-3097-94a5-a47a0af67ec6 | -6.6195 | -59.0416 | 2026-08-14 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| ad8f35e6-0364-32bf-8002-5b64f54bac62 | -21.9054 | -55.3538 | 2026-08-14 01:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 76caec66-52c2-37e9-8a79-55d48c4efefa | -16.9191 | -54.1481 | 2026-08-14 01:50:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 00f79b98-a409-373f-8ee4-79c596d299fb | -13.2413 | -54.2683 | 2026-08-14 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3340c620-9af4-3646-a144-0134c6e6e019 | -13.5701 | -46.2584 | 2026-08-14 01:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 139d1cfd-8e1a-3cf8-9157-46834ec44592 | -6.6194 | -59.0609 | 2026-08-14 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| d95b8ae6-1189-3480-8641-243bd954325f | -11.4885 | -54.6273 | 2026-08-14 01:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| cc673e75-54e7-32d7-b4f4-abddf1c213db | -4.5057 | -42.5325 | 2026-08-14 01:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 88d4c7a1-dc7f-37a6-9b51-bc67410a2f89 | -4.5055 | -42.5561 | 2026-08-14 01:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| ae5c2eea-0894-3a18-9c35-5d0714980d18 | -6.9145 | -43.6351 | 2026-08-14 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4f46c589-f429-3970-a4c0-d43847b6a02c | -16.9191 | -54.1481 | 2026-08-14 02:00:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1848c281-ee94-3830-931b-1de86b22a0c0 | -6.6194 | -59.0609 | 2026-08-14 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| eca40eef-7348-3b10-a630-5639f5ea29b5 | -14.4734 | -45.6914 | 2026-08-14 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 7ee23144-8537-31b8-8ec6-09bdafd04308 | -13.2413 | -54.2683 | 2026-08-14 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 3d3af647-080a-32ef-b5d3-6bc67830b7ae | -4.5057 | -42.5325 | 2026-08-14 02:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 0453aea8-cce7-34bb-9f10-e09a5133e0ce | -13.2415 | -54.2476 | 2026-08-14 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 3bbadb5e-8afa-3db8-85b7-9bc6ea3b0407 | -4.5055 | -42.5561 | 2026-08-14 02:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 3e0827f9-8354-3919-af54-d554961afd25 | -13.3988 | -42.3817 | 2026-08-14 02:00:00 | GOES-19 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 80858218-5873-37a5-b224-a26c0056ebe4 | -11.5074 | -54.6256 | 2026-08-14 02:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 772ca9d0-93bd-3223-99e5-39e17ad468d4 | -21.9054 | -55.3538 | 2026-08-14 02:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 386c2c9f-6297-32a8-82e9-385dc1381e14 | -11.4885 | -54.6273 | 2026-08-14 02:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 8d8666c4-6de6-3186-9f2d-5832fe4d0464 | -4.4868 | -42.5572 | 2026-08-14 02:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 059a522e-7fdc-3376-b04e-32874261cf31 | -6.6195 | -59.0416 | 2026-08-14 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| b50beabf-d071-34a0-b6a6-14b0e3a6662c | -21.9049 | -55.3755 | 2026-08-14 02:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 74a99361-26a6-3677-b220-5bb95035edfe | -4.5055 | -42.5561 | 2026-08-14 02:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 79253b2a-5fa4-3ca9-a2d2-2950f160a7ba | -6.9145 | -43.6351 | 2026-08-14 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 2d48283e-d188-3c40-875e-506349173c37 | -14.4734 | -45.6914 | 2026-08-14 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 0022ba0e-4e64-3bf8-bc12-966a8cb916f8 | -21.9049 | -55.3755 | 2026-08-14 02:10:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7f4e5364-d28e-3a3f-8078-207fd2a06ee7 | -16.9191 | -54.1481 | 2026-08-14 02:10:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 50cf38d7-f44e-358b-8a41-d45ea93c9dab | -13.2415 | -54.2476 | 2026-08-14 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6b6cbd6e-3ff5-3a14-b249-f12528453df3 | -6.6195 | -59.0416 | 2026-08-14 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| f4d61e89-f230-3b2f-acac-c0b7428be3a6 | -4.5057 | -42.5325 | 2026-08-14 02:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| c80c6cc4-6c01-3179-b7ad-e88632899b0d | -11.4885 | -54.6273 | 2026-08-14 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ff665bd0-51e1-3bd4-bf70-435590fe4950 | -13.3988 | -42.3817 | 2026-08-14 02:10:00 | GOES-19 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 886f8f24-80fd-35b4-ab19-6749a6357373 | -11.5074 | -54.6256 | 2026-08-14 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 97f45a90-b836-30c7-bc63-522dbd590178 | -13.2413 | -54.2683 | 2026-08-14 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c9e2281a-e92b-3f76-a75b-cf25320772a3 | -21.9054 | -55.3538 | 2026-08-14 02:10:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 53a9836e-12ee-376a-80a6-66045f51c5ad | -6.6194 | -59.0609 | 2026-08-14 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b8d4adea-5fe3-3d5f-a012-2e2423f8d2f5 | -4.5055 | -42.5561 | 2026-08-14 02:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 0c52ff4d-4a17-3308-99f3-c7f62842f826 | -6.6195 | -59.0416 | 2026-08-14 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 48ff91ec-8041-34ca-86ba-14c11acd143d | -11.5074 | -54.6256 | 2026-08-14 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 99b8ee12-6120-367b-a468-d11adbf8247a | -16.9191 | -54.1481 | 2026-08-14 02:20:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 4c45b7fb-811b-3586-a2fa-a8feaf264552 | -6.9145 | -43.6351 | 2026-08-14 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d0fd331f-b291-3f56-8ecd-8f8a736cfb10 | -11.4885 | -54.6273 | 2026-08-14 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| df3c7041-3b60-3d37-8860-6dec71b6b405 | -4.5057 | -42.5325 | 2026-08-14 02:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 0f309bdd-1860-3bf0-9512-2e03b4f63465 | -16.8994 | -54.1509 | 2026-08-14 02:20:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| aa4ff988-a738-326c-b86a-f690b422eb94 | -13.2415 | -54.2476 | 2026-08-14 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 38e03411-4a2d-37a2-b091-38d6f980a276 | -21.9049 | -55.3755 | 2026-08-14 02:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3ef1a2d0-2d55-3ca3-ba51-a5b09872d4bb | -13.2413 | -54.2683 | 2026-08-14 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 3959c618-355e-3e64-9fde-37933ccd1cf7 | -13.3988 | -42.3817 | 2026-08-14 02:20:00 | GOES-19 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 59.4 |
| c8c99c1e-82ed-308c-8536-4868c673c475 | -21.9054 | -55.3538 | 2026-08-14 02:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 51d6e0f5-f692-3976-ba41-057fe93527b0 | -6.6195 | -59.0416 | 2026-08-14 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| c027493a-ab0d-3797-99ca-273a919cd2ea | -13.3794 | -42.3854 | 2026-08-14 02:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 62.1 |
| a156f42c-3b40-307d-9377-615aea7f48f0 | -4.5057 | -42.5325 | 2026-08-14 02:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| d9049365-3256-366b-b46d-9284572f5887 | -21.9049 | -55.3755 | 2026-08-14 02:30:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 59.5 |
| e5ebd6ad-776c-3f17-92c4-78d59f3a34a2 | -13.2415 | -54.2476 | 2026-08-14 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| fa32fc40-7926-38a3-be45-31609fe717e8 | -16.9191 | -54.1481 | 2026-08-14 02:30:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 41f149f1-5b00-3cd4-b0c4-ff5f520083ac | -11.4885 | -54.6273 | 2026-08-14 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 6b47fc26-f796-32ea-b5fa-a25f9cca6c16 | -13.3988 | -42.3817 | 2026-08-14 02:30:00 | GOES-19 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 59cf908e-662e-32bc-8ddb-8c82d5cd525c | -6.6194 | -59.0609 | 2026-08-14 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 0c8fa4a0-1ccb-36f8-b47d-6fdc06643fb8 | -13.2413 | -54.2683 | 2026-08-14 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9c28274b-dbad-355e-8cb3-f0bc91d6b141 | -13.2801 | -54.2228 | 2026-08-14 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 156696f3-8add-3f05-b731-aee3c6061085 | -4.5055 | -42.5561 | 2026-08-14 02:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 9ffbde59-9e14-3ba5-a894-8cdd8e53f9c4 | -15.1362 | -41.561 | 2026-08-14 02:40:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| c21bf26f-8616-34ca-83b1-676ccc6ef3d1 | -13.2413 | -54.2683 | 2026-08-14 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |


[Clique aqui para ver as próximas entradas](README7.md)
