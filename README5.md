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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a98446fc-5d54-3036-ad45-0dd7b729405c | 2.66626 | -60.15618 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22d3874c-685d-3266-8c8e-addb1a1db391 | 2.66762 | -60.16481 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25ab0f45-20bf-3650-ab27-451ea7f69eae | 2.66186 | -60.1569 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 022b0791-60aa-3e76-aa84-660c002afad8 | 2.66336 | -60.16684 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73899ac9-38a8-3126-ab9a-14eba2a8c931 | 3.86946 | -60.07621 | 2026-02-17 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62d8e3bb-9677-329e-a9b4-dc8636953d94 | 3.70906 | -60.63481 | 2026-02-17 05:54:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 477fd20b-b533-33da-b361-aea54e11c50f | 2.66122 | -60.15392 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c0b5573-8979-3560-af5f-81daa182c371 | 3.1846 | -60.50589 | 2026-02-17 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd1756fd-8a7a-3385-ad37-31a4fefe8582 | 3.68392 | -60.92663 | 2026-02-17 05:54:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5589f27-3630-324c-99e6-12a078b503b6 | 3.69153 | -60.9216 | 2026-02-17 05:54:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 151246c0-efae-3e19-83df-48fa0a7f76e7 | 2.66118 | -60.15258 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8ec56f1-66ee-342c-9dad-61d2f5f1dac8 | 1.91658 | -60.71744 | 2026-02-17 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12e78d4b-9bd5-3a05-9a2b-be96940498a9 | 2.86462 | -61.02418 | 2026-02-17 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffc2f745-7f87-37e7-9145-3cce3fb7ec5f | 3.69386 | -60.65902 | 2026-02-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff23911e-ce15-3fb3-b0d8-418f42616048 | 3.69848 | -60.64741 | 2026-02-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98d11a80-e3b7-33a0-bb86-e3c8c42ee22f | 3.8668 | -60.08358 | 2026-02-17 06:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32433f77-9a00-323f-b489-c6e4feacba0d | 3.86578 | -60.07777 | 2026-02-17 06:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 17344e75-fa4c-335e-9f5a-fe182e7bdd34 | 3.69595 | -60.66301 | 2026-02-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 812e0d54-d279-390b-a3be-752af2901f9e | 3.70027 | -60.65791 | 2026-02-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af9f3474-41d4-32aa-a94e-660576b9ad3c | 3.69476 | -60.66428 | 2026-02-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b68e6f3-c17b-31b6-9944-a295a4693e32 | 3.69937 | -60.65263 | 2026-02-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a9203a9-a434-3165-a40c-eaf570de0407 | 3.69501 | -60.65773 | 2026-02-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b6f722c-19c8-3fa4-8948-d46a502ed63a | 2.66222 | -60.15687 | 2026-02-17 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c21667bf-a673-3fd0-ad22-fa80e6a58ee3 | 2.65551 | -60.15796 | 2026-02-17 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e4f3266-1c07-3e96-86c7-208b211d003b | 3.70162 | -60.64925 | 2026-02-17 07:26:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dc8c8fda-dc37-317c-9d22-645c47283177 | 2.94756 | -60.74711 | 2026-02-17 07:26:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5a36a555-e580-354a-935f-6119efaf80b4 | -20.2079 | -50.4608 | 2026-02-17 08:10:00 | GOES-19 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| f0b9c746-f24b-3620-a3ac-d1c91228b746 | -20.2079 | -50.4608 | 2026-02-17 08:30:00 | GOES-19 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.4 |
| 50503d5c-6de5-3cee-ac02-061c9ac29061 | -8.47956 | -36.81404 | 2026-02-17 11:12:00 | TERRA_M-M | ALAGOINHA | PERNAMBUCO | Brasil | 2600609 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 731dd3a8-3ef7-3323-b3ef-d360fed92165 | -9.36068 | -36.95629 | 2026-02-17 11:14:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 50e8174a-3763-3441-bb80-d70cca630236 | -15.31631 | -53.42024 | 2026-02-17 12:53:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e1cfed23-f09b-3095-9708-a41508df07b8 | -23.10735 | -55.22318 | 2026-02-17 12:55:00 | TERRA_M-T | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 394b2a01-6c0f-3b17-b857-fa8e912d1edf | -20.23164 | -56.37923 | 2026-02-17 12:55:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c682c37b-ac4e-3cd4-820e-5d3d9561dde2 | -21.42133 | -56.46875 | 2026-02-17 12:55:00 | TERRA_M-T | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a125161f-828b-340d-a67c-9fa02f118795 | -22.5994 | -53.66312 | 2026-02-17 12:55:00 | TERRA_M-T | NOVO HORIZONTE DO SUL | MATO GROSSO DO SUL | Brasil | 5006259 | 50 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| 47e00f88-6f8d-30c4-9869-8896ea44646a | -21.42311 | -56.46236 | 2026-02-17 12:55:00 | TERRA_M-T | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6b653444-b828-335c-878b-41287fe608c5 | -22.36983 | -55.46486 | 2026-02-17 12:55:00 | TERRA_M-T | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 22.1 |


