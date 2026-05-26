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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66328325-9d80-3022-93e8-1cda4452d4e9 | -11.1903 | -55.9101 | 2026-05-26 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 59c2f5ea-8f39-337b-9710-6754bb1a35a9 | -11.3581 | -52.9722 | 2026-05-26 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| e2535f8f-870f-3070-acbf-1ce5887224e5 | -11.3584 | -52.9514 | 2026-05-26 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 166.8 |
| bb604359-ce0e-3b4e-9f94-21017307f426 | -21.5491 | -47.0668 | 2026-05-26 00:00:00 | GOES-19 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 11ca8f71-fb7e-3020-95af-2fcba230fd77 | -5.7939 | -45.1267 | 2026-05-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9d114b09-9e7c-33d3-88c7-a07c2614df4d | -9.3045 | -45.4809 | 2026-05-26 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 7f8d31b9-7645-3a58-bc53-046686c35c17 | -21.5498 | -47.0429 | 2026-05-26 00:00:00 | GOES-19 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 102.0 |
| ced1e249-b943-39ab-9e6f-6dc59f086b43 | -11.1714 | -55.9117 | 2026-05-26 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 8bf791d9-5a51-3131-af3b-30f3907c10d3 | -7.1355 | -44.0553 | 2026-05-26 00:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| a4e0a5c9-0af0-3ece-b030-7605a75b78b0 | -11.3584 | -52.9514 | 2026-05-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 3ea740ee-e9da-306e-ae71-7d0d67d7430d | -11.1903 | -55.9101 | 2026-05-26 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 10a3f856-72c7-35f2-b96e-ed3f9c73cfa3 | -21.5498 | -47.0429 | 2026-05-26 00:10:00 | GOES-19 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6c9ce3ae-7355-39a7-b7b6-29e759ff0749 | -11.1714 | -55.9117 | 2026-05-26 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1f8d5067-6a63-35c2-9b2d-d373afb55764 | -7.1355 | -44.0553 | 2026-05-26 00:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 23b5a51f-1872-3b8c-802a-1fe7d94f1a56 | -11.1712 | -55.9319 | 2026-05-26 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| c8590130-fb04-33a9-9d68-31504f5f5590 | -11.3773 | -52.9496 | 2026-05-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 0426873a-0cde-3b02-97c1-175d854c99b8 | -5.7939 | -45.1267 | 2026-05-26 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 9b7e20cb-b2f1-38d0-92d4-44549c13defd | -11.3581 | -52.9722 | 2026-05-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| b7360d18-eff5-3c4d-be4b-d8bb05205168 | -11.19 | -55.9303 | 2026-05-26 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| b9d20d92-e50f-3141-ae8f-ac4f28c575c1 | -7.5782 | -50.170601 | 2026-05-26 00:14:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee2af79a-910f-3292-8a53-aa0642c53834 | -21.5597 | -47.0541 | 2026-05-26 00:14:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5bc840da-21dd-3d79-bf3e-fbc1c75c881c | -5.7958 | -45.120899 | 2026-05-26 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55a781f4-cdae-353d-8f3d-81886c1a62ec | -13.2793 | -48.858601 | 2026-05-26 00:14:00 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 623a94a0-d15c-3bf1-9519-95700fc2041e | -11.357 | -52.945099 | 2026-05-26 00:14:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd71d3b-0cd6-3946-9892-71fed5fdbae8 | -9.3002 | -48.5756 | 2026-05-26 00:14:00 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f90fa4c5-ad28-31dc-8a08-195bc54e5758 | -10.8503 | -53.7477 | 2026-05-26 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 606195aa-ef32-3e78-8955-91d427cd7a4b | -17.2407 | -48.294601 | 2026-05-26 00:14:00 | METOP-B | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 656059b9-99c7-3c71-a570-6099d9dce0b5 | -11.1699 | -55.900101 | 2026-05-26 00:14:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b6235c3-67c2-31a8-8aea-bf3df2873a7a | -11.1866 | -55.882099 | 2026-05-26 00:14:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff24dbde-01c7-3266-88d9-e5f6fc02c666 | -11.5432 | -56.907398 | 2026-05-26 00:14:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16e0ac26-3de6-374b-955c-ff0ea0d430dc | -6.5249 | -55.052299 | 2026-05-26 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2195355a-b347-34a5-9c97-038dab4c85d3 | -12.0373 | -47.3256 | 2026-05-26 00:14:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d936d6fc-7050-3b53-ad83-830d381a5057 | -8.553 | -45.967201 | 2026-05-26 00:14:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b922d58-5799-36f1-a6c5-c12dee555af7 | -13.2777 | -48.851601 | 2026-05-26 00:14:00 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d31921cc-3ac4-3944-b3c4-b9115c7f7a06 | -17.2488 | -48.285099 | 2026-05-26 00:14:00 | METOP-B | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| abd6e7da-9904-333d-80c5-f9345e16d863 | -8.5571 | -45.9846 | 2026-05-26 00:14:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bd7b2a2-d172-3a89-8e7d-54fe5fd0a80e | -11.1894 | -55.896099 | 2026-05-26 00:14:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 610bb0a8-2cdd-39bc-820c-3a0a71cd5cc9 | -12.4604 | -54.432899 | 2026-05-26 00:14:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46ea3161-3210-3ace-96ee-1757f71f099d | -5.7835 | -45.112598 | 2026-05-26 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64ccb76e-fc2a-3cd7-b89f-4bdabd207c08 | -9.3018 | -48.5826 | 2026-05-26 00:14:00 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73453a44-37ea-3f8e-8cb1-2cb3c1ed222e | -7.1367 | -44.043301 | 2026-05-26 00:14:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6b36bd3e-154e-3a73-93e1-5c843d9adb05 | -7.127 | -44.045601 | 2026-05-26 00:14:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 29609cec-7dbe-3635-b5c9-e77a950b052d | -9.4938 | -48.6562 | 2026-05-26 00:14:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3221655-faff-3586-b64e-43b14dd9464b | -9.2969 | -45.488602 | 2026-05-26 00:14:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d9e3a369-06fa-3598-9b57-7fec02ee00c2 | -7.0141 | -44.999001 | 2026-05-26 00:14:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74000e40-6fed-3368-a723-fbdf8b3fd759 | -13.9659 | -53.868801 | 2026-05-26 00:14:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c6ebe8c4-1e95-3459-af74-876bf2b007c7 | -10.3753 | -51.8965 | 2026-05-26 00:14:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d287e00e-ae4b-3757-bedf-cd4c37328623 | -17.9517 | -54.442799 | 2026-05-26 00:14:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 919f1a6f-d9ac-3cf9-bdc7-68778c49c3c9 | -9.2828 | -45.472698 | 2026-05-26 00:14:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae29f476-1d76-3d2b-abef-4397c404230b | -11.1825 | -55.912201 | 2026-05-26 00:14:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0245159c-7166-3a37-80ba-1a26868675d2 | -21.3055 | -48.585201 | 2026-05-26 00:14:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4cb9a0b1-bddb-3844-ae43-3c6e2c512d0c | -4.4326 | -47.7211 | 2026-05-26 00:14:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b76ceae-fc72-3a9b-97c4-954f377002e2 | -11.5529 | -56.905399 | 2026-05-26 00:14:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1353bd5c-00bd-347d-9f4f-88b53e8fdec6 | -11.3688 | -52.952301 | 2026-05-26 00:14:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf75d1f1-932a-30e0-8b25-294af1717410 | -14.2512 | -45.8246 | 2026-05-26 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3fde890f-b084-39f1-9c6a-22050f509ec9 | -10.3672 | -51.9067 | 2026-05-26 00:14:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 679a827a-9229-3917-ac27-81101534af88 | -21.323799 | -47.056999 | 2026-05-26 00:14:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 08de9296-59a7-373c-80e7-99b8154fa0ca | -7.1299 | -44.057499 | 2026-05-26 00:14:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c671bfd9-f656-3800-9ab2-f603feff2011 | -9.1994 | -48.767502 | 2026-05-26 00:14:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 44e8a7d3-9b85-3671-a890-4da052be981a | -9.5516 | -46.884201 | 2026-05-26 00:14:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d1a3a77-b66a-3e33-a339-a1f67a980bc0 | -8.555 | -45.975899 | 2026-05-26 00:14:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b0c2ace-c66d-3cff-bd1a-dbbfb5570567 | -8.9781 | -47.977402 | 2026-05-26 00:14:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db4d9c08-c533-35f0-b37a-6a28805e8311 | -11.359 | -52.9543 | 2026-05-26 00:14:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 954495dd-08a9-305f-b4d6-1b9127abf449 | -10.5976 | -44.317699 | 2026-05-26 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e809b7f-fcfb-30c7-aa06-7a49aed9e6ed | -7.1327 | -44.069302 | 2026-05-26 00:14:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18349e5d-f033-326e-99bd-a05ed2efebc7 | -14.0402 | -46.34 | 2026-05-26 00:14:00 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0a806a59-7a76-33c1-a21a-f1a6b30a1910 | -9.2948 | -45.4795 | 2026-05-26 00:14:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4c1c9691-e950-38d6-be17-01c9e709d78f | -13.6558 | -55.281502 | 2026-05-26 00:14:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbc04159-4692-3639-8a61-1ae563c12ee7 | -8.7094 | -54.9865 | 2026-05-26 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf2cfe18-ad24-3531-93d0-a7d0e27a8391 | -8.3288 | -45.366798 | 2026-05-26 00:14:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8d21d811-36ef-38a3-930f-93740ce53fa3 | -10.6343 | -48.320599 | 2026-05-26 00:14:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e5f83e0-9088-32e0-a96e-92b460a641de | -10.9238 | -54.099998 | 2026-05-26 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe5ad80-c5f2-3e7b-adce-13c6db904d0b | -10.6359 | -48.327599 | 2026-05-26 00:14:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c5e55e9-40df-3fa4-b6c9-3f08326288d3 | -11.1786 | -46.912201 | 2026-05-26 00:14:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b6d26be-4a42-3eab-8a08-8c84dc95f524 | -13.6531 | -55.267502 | 2026-05-26 00:14:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c8b2e65-683b-3fb7-980d-b1e6106d824e | -7.1396 | -44.055199 | 2026-05-26 00:14:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0b3f854d-ce1d-3ec4-9123-432c139dfc95 | -8.9798 | -47.9846 | 2026-05-26 00:14:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2806effb-c99d-34a6-aa36-d0047c23943c | -21.325399 | -47.0644 | 2026-05-26 00:14:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e512a7dc-a11e-3173-8123-1f2ff97d8eca | -11.1768 | -55.884102 | 2026-05-26 00:14:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fca9b19b-ab0b-370b-98c2-7eabf089c79a | -14.2494 | -45.816799 | 2026-05-26 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ecc339c2-ec21-3f46-bfbe-3b3abab5b9c5 | -9.285 | -45.4818 | 2026-05-26 00:14:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e62935c2-3d18-38c1-83fc-5bb5c7d1e873 | -10.8833 | -51.207298 | 2026-05-26 00:14:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9be224fe-16b2-3b87-b165-248d94d6be21 | -12.0432 | -45.2659 | 2026-05-26 00:14:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab6c1b14-1de4-35b0-a943-faf3de99778d | -21.339701 | -48.602001 | 2026-05-26 00:14:00 | METOP-B | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd073fc7-48b1-318b-af28-3fc3ef94cb26 | -12.4628 | -54.444698 | 2026-05-26 00:14:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85417899-53a1-311d-97b1-df9b144a303c | -10.5951 | -44.307499 | 2026-05-26 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a76b4a01-07a4-3053-a810-80106189fa02 | -9.4455 | -50.836399 | 2026-05-26 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40755867-c753-3f0e-bf2f-61a65bfea59d | -5.786 | -45.123199 | 2026-05-26 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1da1a405-b5e9-3924-96e5-cc270a17b6a7 | -8.331 | -45.376301 | 2026-05-26 00:14:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a6af7b91-ccd3-3f86-bd5a-148109eebbd1 | -10.3023 | -49.7332 | 2026-05-26 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a599c17-ced0-372e-b6be-7be832b6b785 | -10.8482 | -53.737598 | 2026-05-26 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df180558-0686-318e-b80f-5c6e1df0dcc9 | -12.2312 | -46.598202 | 2026-05-26 00:14:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 802df1e6-0180-3d81-8240-697cbd17ea10 | -8.9281 | -51.8522 | 2026-05-26 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3de0ac44-eb83-33fb-ab45-b597b81d88da | -9.4922 | -48.6492 | 2026-05-26 00:14:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0004237-e52e-3015-8335-5f73f118e035 | -5.7932 | -45.110298 | 2026-05-26 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a9972c6-0726-3663-9df0-beeb82a25a84 | -7.1424 | -44.067001 | 2026-05-26 00:14:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1aafef51-cf7c-352c-af49-af0711670dc6 | -21.3039 | -48.577301 | 2026-05-26 00:14:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ab7d7f44-16c9-3e46-b0ff-90e047e2a9da | -9.2926 | -45.470402 | 2026-05-26 00:14:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b2543ed-45bb-3309-987d-ba1538de8d48 | -21.556499 | -47.039398 | 2026-05-26 00:14:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9609f240-79b1-3cf2-8e7f-bf92fd4786d9 | -21.5581 | -47.046799 | 2026-05-26 00:14:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
