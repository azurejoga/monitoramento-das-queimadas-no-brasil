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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f110c6c2-2179-3cf0-976f-b24956c77d5f | -3.66375 | -52.17794 | 2026-08-31 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 415a4c46-01cf-3b1e-a2bd-6d4d48f0fc79 | -7.37283 | -45.0706 | 2026-08-31 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 965663ee-5295-3b29-bb12-edfc3cdd0b68 | -6.8943 | -55.70754 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5140d4d9-bfd4-3fe1-b3e0-3700099b02cc | -4.89513 | -55.90984 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d5d3456-43ff-36da-92cc-9c4ba9fae5ec | -6.6392 | -53.1815 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 114ca231-dcae-3ff9-b179-f49dbb357416 | -7.91817 | -44.25243 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 04a84a6d-8f37-3d85-9010-a6a45bfda31b | -8.21252 | -54.94365 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 432f135a-103c-3f28-b9e1-7ed9c5bb7b4a | -6.99942 | -55.88193 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b654a4a6-9886-385e-9aae-4f8922c26f1b | -7.21574 | -60.66843 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcaaf0e7-b9f2-3fb0-b571-db7e8c9c4515 | -7.00335 | -55.8789 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b614a291-ffeb-32c4-923f-1eedc0b34a2b | -4.85868 | -55.82831 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 997ac5fa-877c-3fad-96cd-b61561502ab0 | -5.63721 | -51.78718 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35c1ef0d-f5ca-34f7-ac13-1ec115d758c9 | -6.76893 | -52.92966 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ff5f905-2583-3351-9266-a23bb6debf76 | -4.96833 | -55.84567 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a5ec55f-5bdf-3dbc-8beb-940663b576c8 | -7.33733 | -60.59081 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4f6d791-0293-3a3b-87fc-a29a57f6ac05 | -3.62739 | -60.56579 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b33a0815-8c41-310c-aacb-6d4bb00919ce | -5.88576 | -57.76244 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b8da1a3-fbfb-30fd-a3bf-745163269e14 | -5.25444 | -55.90175 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 30936aba-0e08-3c59-8fa3-0b0cb826bcd8 | -6.59782 | -59.11438 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82635b53-ce09-31ba-a725-3c1b09287eb4 | -3.80157 | -59.61256 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c94fbc8-35b4-3c22-b71b-abef014067f2 | -8.09523 | -45.47495 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6992f8b8-0c22-3238-bde9-8c2b30f6344a | -7.34163 | -60.5915 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a2bd1e7c-387c-39fc-b3a2-f7f7bff39507 | -7.5219 | -55.33307 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27b6d31e-9201-3d6a-b795-1988100282f6 | -3.61237 | -59.07635 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22a95d6c-20bc-344d-9cb3-f713f8e3131b | -5.59154 | -42.32116 | 2026-08-31 04:57:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b28fb4c7-07f3-3fc8-bda1-ba423d8501d8 | -4.94184 | -55.79253 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d245265f-4abd-35dd-8cc6-5f87352d5fc2 | -2.49388 | -54.84096 | 2026-08-31 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c319cae-122d-3a3f-b4bb-3e2942a87f57 | -7.31446 | -60.59539 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 491471be-f9bb-37f6-87ea-6ee57e3d78f1 | -2.91361 | -54.11659 | 2026-08-31 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41106f90-8771-3ffb-a4e1-4f5b028e2b06 | -6.15284 | -57.77913 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a855cb5-fb77-3d97-9e85-fc6ec8a66fb7 | -7.32805 | -60.59343 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b8dc1db0-5713-3f7a-aa95-6833443f21e1 | -4.85127 | -55.83097 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 73141fd9-b335-3290-9b67-6718d003ca50 | -6.97728 | -59.59751 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c0c6bce-35f3-3095-8fc1-b39d07163ca2 | -5.95783 | -53.61215 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dacb7cd-71cd-368e-82aa-d5b7199e8011 | -8.16695 | -54.92928 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f2e0522-b890-36a0-a350-b22460745d03 | -7.30657 | -60.58981 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dd60424-7d2e-389e-9b9e-403608db6a13 | -6.92227 | -55.70464 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f7d963e-30ee-3286-b34e-ffb1cffbe316 | -6.93402 | -55.69555 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d5b2795-cbfd-33bc-b73e-fe28c3a8632c | -4.96317 | -55.85616 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 551faba1-66ae-3c6f-9dd9-4ce8523f26a3 | -5.24869 | -55.91592 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d0671aa9-e71c-3384-9d29-8744df8d8867 | -5.85899 | -57.55576 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 35999c67-7181-3cdf-991b-21460da327e5 | -6.25119 | -55.4335 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d539fa83-6eaf-395b-95e8-75712175ab30 | -5.24763 | -55.90067 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b581241d-bc48-3f45-a522-ff1f8b2e8856 | -6.17756 | -55.44379 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6caee0a5-8526-3496-a7e0-004320ba1a44 | -5.87739 | -52.14999 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 388fa3c7-cf3e-384b-b9ca-cb8fec3f2957 | -6.72592 | -56.34048 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4923200e-afaa-3bb3-a4f7-0ac7ceba0923 | -5.24552 | -59.72852 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47b739d6-63e6-371d-80a4-b77766fcd787 | -4.96891 | -55.84198 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78814141-6c60-3c86-ba40-fd6f21c2c6e5 | -3.48385 | -54.66587 | 2026-08-31 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33b54c2a-109d-348b-8e83-04c90a5fdb53 | -5.88207 | -57.76192 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 178069cf-221e-353c-b307-c3c87660640b | -5.87261 | -57.77389 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92ab96c5-b307-340e-a475-35fe9438878c | -6.86908 | -59.46916 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c66b8421-9d94-3a40-9331-08811753154b | -2.60145 | -54.41651 | 2026-08-31 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b3e8244-0d23-38e9-b4a1-0f0b84e81d0b | -6.11639 | -57.6808 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a900e823-d546-392c-b88c-1c3161f190dc | -7.62003 | -57.61458 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4d3ff99-779e-3895-a9cc-60bdd902074b | -4.85185 | -55.82727 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 450ba3f5-e1ea-3a46-99af-b161ef3fc2dc | -5.61081 | -44.00135 | 2026-08-31 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 756bcc21-e728-3ebd-8a4e-5d34f4fcd48a | -7.52577 | -55.33011 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5219e620-da80-3450-82b0-e3ea6a0b9a5d | -6.86329 | -59.47918 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de8ae539-1cd8-3346-8d81-7ec01bfae93f | -6.80476 | -59.45869 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28349b00-9a9a-3180-9865-cca4bf1c3c55 | -6.25063 | -55.43703 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bad75d64-92d7-3b33-9265-0a889054826d | -4.15319 | -60.68962 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd9ea615-58e1-39af-8a7b-c9c64d45299e | -7.92505 | -44.24488 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 113b7700-6d41-34d7-9dd2-bcb325a4c9f1 | -3.46249 | -51.89126 | 2026-08-31 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d091eb39-a852-32d6-b237-17e19c10ee31 | -6.98191 | -59.59465 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08ddbf39-f612-328a-a624-047b6c032861 | -6.177 | -55.44734 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50a9ed32-4eeb-36d8-89d6-653f025e9fdb | -8.75134 | -46.45209 | 2026-08-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 73931991-55ba-3347-9cb0-f3e5a2e5fea4 | -6.26546 | -55.42529 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75df4fe3-0363-3e83-b392-bed33e8aa21d | -5.35272 | -56.67028 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d9a7c9b-411f-37d8-a60e-6c79c1e446aa | -7.97391 | -52.08478 | 2026-08-31 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54ec78a6-ed5a-3fd7-a7b8-7fcbd628edbd | -3.53684 | -49.47113 | 2026-08-31 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d6790992-3533-32fb-9da6-e757fb9f3c63 | -6.75786 | -56.33806 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a621e42f-be91-3ae6-9a75-4864dd8e186e | -5.85967 | -57.55158 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64eed3e3-de30-3d9f-aac5-50877baf1ee0 | -7.93662 | -44.2468 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b6157afd-4cea-325c-b4cc-770840803ac8 | -6.37533 | -54.9469 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdbb1fd4-da4b-36d5-9573-1f7092765f8a | -7.28652 | -52.54142 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0a5b27c2-e3d9-3aa3-bcee-1ad6f132d3b6 | -5.89084 | -57.75428 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d91eaea-0ef6-3713-9ba3-08ac70d1a4f2 | -5.40474 | -45.88474 | 2026-08-31 04:57:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6ac160d-2b67-3af1-9e5c-7a2a6588ea63 | -6.12158 | -57.69478 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3f19c3a-00c0-3c5c-892e-b55ce3ffb1a2 | -5.9728 | -57.68701 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc2d3671-3e3d-39d2-b329-51543502f5ba | -5.97119 | -57.67369 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d2a0fd4-b804-355c-a850-058b8221d3b2 | -3.61031 | -59.07134 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7148569a-6c72-3e97-b94a-b554ea68cd9b | -7.30586 | -60.59396 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5df15ac-02b4-3682-a113-226d5e6d6554 | -6.9093 | -59.48402 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 548cf6a1-7046-340b-b624-d43ec08ca56d | -5.2521 | -55.91646 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 345f532d-6269-3d07-8541-e38a9884650f | 0.1958 | -60.50274 | 2026-08-31 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a306e34-4594-3f0e-aa85-ba35435aa57e | -6.25899 | -55.42745 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 092c8877-4506-3610-975b-8f786791962c | -4.95928 | -55.83664 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4379a34-b234-3ef3-8624-c7b2c121ffb1 | -9.43293 | -45.66506 | 2026-08-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| add53cdf-a749-3bf5-8b1f-4c632bec9f72 | -4.85527 | -55.82779 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16f63f06-d418-3081-9077-3554f0a66ce8 | -6.18663 | -44.93657 | 2026-08-31 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b01cb5c-4bf8-31da-beb6-b3a5d903d1dd | -3.11037 | -61.22507 | 2026-08-31 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd7443ef-dadc-3754-89be-2b14af896db3 | -5.95447 | -57.68419 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8d79419e-1602-3a41-b499-729929834ef8 | -8.38245 | -45.00275 | 2026-08-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d35ed8c5-d811-3651-90c9-a77512b3a29e | -5.48582 | -57.14986 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af38dd92-11a8-36c4-9cc7-559cc93fc79a | -7.97762 | -44.29668 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11b9de9a-8288-39be-8ff4-c2d989c35258 | -2.02213 | -52.1098 | 2026-08-31 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd007857-6ac6-3211-b8cf-c45493b992ba | -3.86484 | -49.10645 | 2026-08-31 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 04167c41-5f3e-384a-afc7-33b6a1d5c293 | -7.34593 | -55.17632 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d310247-f11a-3a98-9374-659c4065d039 | -5.96685 | -57.67731 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README40.md)
