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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bdd3397-38cf-38e8-b920-8941f4ace643 | -12.75996 | -62.84586 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08e3fe4a-8ed0-393c-b1d5-178dd9de3306 | -12.75183 | -62.84932 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbf29721-30ed-38d9-812c-cf070279150b | -12.74745 | -62.85333 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb8d37f2-4f00-3f7d-8b13-57120a7b49cf | -12.65807 | -63.11094 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c123c730-216d-3a81-94a6-ef62b4c82c7c | -12.38226 | -63.00326 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53f6ea5b-26d0-350e-be4d-cd98f754372e | -12.33015 | -63.71851 | 2024-09-29 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| daca5936-67ae-3bee-9438-6bc86699d917 | -12.32954 | -63.72262 | 2024-09-29 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3ecfb709-ae02-3f57-8a50-80b13647e265 | -11.7517 | -64.28238 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46ad0956-e0df-3e52-b198-31c954ea4d15 | -11.74273 | -63.80079 | 2024-09-29 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8655ac22-38fa-390b-b1f2-f04d9a8e9262 | -11.73479 | -64.09442 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e54041da-f3b5-3b6f-ac20-e65413605aed | -11.72839 | -64.11339 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e595e073-4be9-36bd-9692-9ce4d5763e90 | -11.71218 | -64.12682 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5134175f-dd8f-37ba-99cc-0f9f679f968b | -11.70873 | -64.03064 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be94dbf5-52d6-3ee5-bc8c-878a95007431 | -11.70525 | -64.03012 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09c648da-826d-3dbb-86f5-13d69069ccb4 | -11.69019 | -64.05972 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 472dfb71-e9ba-34f2-afd1-34cd80f233dd | -11.68727 | -64.05538 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 859366f0-1e64-3de1-a50b-7c921e72257d | -11.67974 | -64.05823 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c800e267-f1f0-39d5-a77e-625e62cfde44 | -11.67626 | -64.05774 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f6d1cf6-1603-33be-b91f-28bba4ed092d | -11.67118 | -64.18806 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4074cf3-7045-339f-a79a-d567e7e2d2a7 | -11.6706 | -64.19193 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67f756de-ddd0-3553-9bd8-3c98dcc7b869 | -11.66743 | -63.99668 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bff9f8d7-9e02-32a2-9660-dd7c820e2630 | -11.66685 | -64.00063 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d4d9516-eb8c-3342-b48f-90a4adf86001 | -11.66641 | -64.07638 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5220133f-0f04-38b9-bd2e-0b3d134f105d | -11.666 | -64.19911 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dbdda83-ffa0-35a0-bbb1-61507d0ae113 | -11.66455 | -63.99193 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e900f82-0a1d-34f1-851a-3f539eb71d03 | -11.66349 | -64.07211 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2af7582a-e385-39f3-a578-3d569c22d138 | -11.66109 | -63.99122 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f19e6be4-c7d1-3ce6-8dd3-e1d83e2c7539 | -11.6582 | -63.98656 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 241375fb-68a1-32b0-a6d8-8bac7086c72e | -11.65818 | -64.01117 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b559b0a7-edc2-39ce-804a-50150cbf74e0 | -11.65761 | -64.01511 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e446bdc8-b9d3-33dd-83c1-ca94b90b435f | -11.65761 | -63.99058 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b529bc0-993b-3c82-bd5a-2416a5d736dd | -11.65472 | -64.01047 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a60114e-05fc-398f-84f6-08a6fef30b2c | -11.65125 | -64.0098 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e29e27e-bc17-3aa6-b954-d648af49d834 | -11.64604 | -64.00982 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26234d37-4978-305b-a3b0-a6aa25ba9e9a | -11.64197 | -64.01319 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6b17601-5d9c-3b4f-893b-8871f40298e8 | -11.63638 | -64.0873 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5acebc29-9d56-3907-a659-f6f3d78cd39d | -11.6343 | -64.08793 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f2e9654-a51d-3a16-8b13-6817f3fddbb3 | -11.63141 | -64.08353 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab880672-8629-3e55-bae0-d0c0fec25e15 | -11.61995 | -63.99371 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09347b20-49bc-30ca-b154-13987a824ba4 | -11.61936 | -63.99765 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d79a719f-11ce-3d39-bf97-2f3fe1b17678 | -11.60894 | -63.89935 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7e5acaa4-b3ef-373e-84dc-89bcd361619a | -11.60836 | -63.90331 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4ea16307-b9ef-35e9-bbee-62f1e53eeb6c | -11.60778 | -63.90725 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e272636-871d-301d-ac83-6c40564b5091 | -11.60602 | -63.89489 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b579a2e1-0aa1-3e8e-8570-fa31eeb9ad9d | -11.60544 | -63.89884 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d19f30d2-1bf8-3a46-8062-9b2da052140d | -11.60486 | -63.90279 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9a018597-b552-3ea5-aef7-5a2e68789b44 | -11.60428 | -63.90673 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0263430-3668-38d0-ba28-5bafd6e0bc80 | -11.60311 | -63.89041 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| aeb92d24-5445-347b-b7c1-41e131a6247f | -11.60252 | -63.89437 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bece3c78-aca1-3cd4-8138-744a976f9e82 | -11.59961 | -63.88986 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a8264ce4-d136-37b0-9d8a-25cf768c7c2a | -11.59669 | -63.88538 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 306fef12-415f-359a-b535-fb59aa818502 | -11.59611 | -63.88932 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d14b3180-0c8f-39a1-90f3-80187b29fa69 | -11.59319 | -63.88485 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f4eb3440-3b55-30ac-b8a8-d5bba4d5f4a8 | -11.59027 | -63.88036 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6be567b-470c-31a1-867d-e9709a7f247c | -11.58969 | -63.88432 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c07b621-c208-38e3-a90d-24a68ab9a435 | -11.58677 | -63.87981 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78f7fef5-d5f3-3bfa-aea7-a00c5e0e6984 | -11.58327 | -63.87926 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79cb2232-cd40-3b9c-8430-cf54f7461ffc | -11.57977 | -63.8787 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dc994fa-82ab-38dc-bd9b-dd8727a91b31 | -11.57627 | -63.87814 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1497b25e-5c83-3507-a607-14832f3b465f | -11.57278 | -63.87758 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4dbc7016-0e91-30d4-bb96-ec8a9f3c440b | -11.5722 | -63.88155 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd6d54df-ef46-3b76-9604-1ddf10b50ce4 | -11.5687 | -63.88099 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee2d88f3-853b-3158-8f52-b2778759374d | -11.56812 | -63.88496 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b037fd9f-68d5-3c89-9533-acfd34a2ba3b | -11.60008 | -63.66488 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d325971b-7e45-37cf-861f-71d601ebd9a9 | -11.60002 | -63.71515 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b433a5b9-51f6-3822-84a3-ebf77d76d752 | -11.59943 | -63.71926 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb550078-79fb-375d-b3aa-ee517f358fc6 | -11.59885 | -63.72326 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f42c31e-6d4b-3a8b-bf14-3017b0f16adc | -11.59532 | -63.72277 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7ffe356-ade4-3c2b-a8d9-8901f4c72e61 | -11.59418 | -63.70569 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0796048-cc8a-3eab-a649-071408eaadc9 | -11.59178 | -63.72231 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5dbf40d-b421-3930-b848-d9351bdf20d2 | -11.59122 | -63.70125 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d85b873e-20a7-3eb6-a723-1c6e32a676d0 | -11.59063 | -63.70535 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dcf8a0b-af7b-32d3-a9a8-a3c1339f5397 | -11.58654 | -63.73357 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd25668e-7aad-3a40-adf4-5b5e52944ca2 | -11.58596 | -63.73761 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 926cdf3e-bd99-35eb-928c-f418d7fb2acc | -11.58477 | -63.74585 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0c6219c-ec69-3516-a0ee-b322b353a038 | -11.58419 | -63.74987 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb0d3a50-8ae7-331a-bef6-25484649e596 | -11.58125 | -63.74535 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| be8e73a5-3e8d-3c97-87d8-794a73bf6982 | -11.58067 | -63.74933 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 04bda90e-1c81-3d58-a332-7a2b260f885e | -11.58051 | -63.74606 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f1bb7532-f37b-3608-b71b-683fb3ff448e | -11.5801 | -63.75325 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 26.9 |
| fdcf084b-cafb-38f5-b61c-0826be5b3c09 | -11.57992 | -63.74999 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 247b0d2a-97bb-3439-8737-9af4e3dfef05 | -11.56182 | -63.72654 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa4b6966-624a-3560-8f70-55da4b9a7217 | -11.56125 | -63.73038 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b97901e-456c-3067-8ca5-4584610ab9e4 | -11.55658 | -63.71331 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4febcc0f-6617-3552-82d5-e79b9e38cd67 | -11.55308 | -63.71258 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0aa52ae-e422-338b-a494-4e1b6e5c5ad0 | -11.55078 | -63.70382 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| beb4d874-ecfe-3eec-a15d-de13c8c38440 | -11.55018 | -63.70784 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec2dbefe-84a6-3913-a7d2-2be6272c1202 | -11.47952 | -63.40215 | 2024-09-29 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b75d7f88-c75a-35c0-8d3d-64b75b6e218c | -11.47891 | -63.4063 | 2024-09-29 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f935eca-efc0-3bab-be7a-cbfb0e696f51 | -10.97145 | -63.58636 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e48deb75-a160-3099-9b8f-8fc2aa6393bc | -10.95274 | -63.59116 | 2024-09-29 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00ffddf2-b798-3f94-b46a-f36a49aa73e4 | -10.95212 | -63.59552 | 2024-09-29 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ccccbe38-d2bb-36da-9311-37d869b762d9 | -10.95188 | -63.59256 | 2024-09-29 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 204fff1e-b392-31f9-aa18-9235db2590ee | -10.95124 | -63.59683 | 2024-09-29 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2b5b4e8c-9d08-37fa-82df-c6773ae25e0b | -10.94864 | -63.59459 | 2024-09-29 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| edb4a356-a2b9-3a22-b573-28a3cefdd8b7 | -10.00514 | -65.25196 | 2024-09-29 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f648a5b5-6833-320e-910a-2f7d680e1e5d | -11.92911 | -64.94307 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 65ca05b2-f6d9-373a-a1b6-05e0ccd7dfa2 | -11.64212 | -65.01483 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f5a8b12-4a52-39c5-a260-34ec34de8c97 | -11.6393 | -65.01065 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a3a5c17-7739-3497-8912-683e84b83b35 | -11.63875 | -65.0143 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README68.md)
