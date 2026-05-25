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
| 0f9fd8e7-a713-32c3-9018-36924f9b8830 | -12.8857 | -58.209 | 2026-05-25 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 52dd0637-f52a-3386-9300-966465320818 | -12.9049 | -58.1875 | 2026-05-25 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 54ff6d40-977a-3d52-84e6-d4e59dcf94b6 | -12.8861 | -58.1692 | 2026-05-25 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 0d47269b-4f4b-30f3-bf1c-5ab47ffc0cf3 | -11.5561 | -56.9232 | 2026-05-25 15:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 191d2b44-cd06-36cd-a51a-c924aed39de3 | -12.8859 | -58.1891 | 2026-05-25 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 310.9 |
| c4c0c311-77d5-3179-98f7-e4d041223b63 | -11.3773 | -52.9496 | 2026-05-25 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| d40a4e91-6ac3-34f9-ad88-41051260ba74 | -7.8381 | -42.0552 | 2026-05-25 15:00:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 305.0 |
| 1595e560-84b0-3b86-8ec8-3384ea7be16b | -3.9594 | -43.1271 | 2026-05-25 15:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 58964add-f9e0-3ad1-a5b6-c8f4d778e137 | -11.3584 | -52.9514 | 2026-05-25 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| be4db1ea-2e3c-3f0a-82d5-1617740e9b85 | -8.6118 | -45.0105 | 2026-05-25 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 6d36516d-a653-3db8-a7a1-4ec867a9210b | -12.8857 | -58.209 | 2026-05-25 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 135.7 |
| da68d269-1693-3de8-a994-957c1ce44241 | -7.8381 | -42.0552 | 2026-05-25 15:10:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 308.9 |
| ee8d5a82-0307-3511-978d-9e5953beca24 | -12.9049 | -58.1875 | 2026-05-25 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 421c32cb-2651-3f73-8bd5-662c514915c3 | -11.5561 | -56.9232 | 2026-05-25 15:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 9fd31122-1288-3928-b915-4f13f02ab4a1 | -6.1081 | -45.533 | 2026-05-25 15:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 6aad54c2-98cb-3100-a73f-21dfb96de990 | -7.8191 | -42.0573 | 2026-05-25 15:10:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 406.7 |
| be0bf055-d9cd-3236-919d-d612dcae20b2 | -12.8859 | -58.1891 | 2026-05-25 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 319.6 |
| d2aa5c5e-b667-38b2-98f8-3a003276ccc1 | -8.6307 | -45.0085 | 2026-05-25 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 156.2 |
| b7f8949e-f665-38a7-8850-4fe7df063354 | -11.3773 | -52.9496 | 2026-05-25 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b64205f6-2cd5-3f3a-9156-526cc1cb1648 | -11.3584 | -52.9514 | 2026-05-25 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 191.2 |
| 730fc3d1-63d7-32ce-ae6f-d8d5b0146aaa | -3.9594 | -43.1271 | 2026-05-25 15:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 99580e5f-8c07-340d-906f-0b5998046d3c | -12.8859 | -58.1891 | 2026-05-25 15:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 212.4 |
| 33df13ca-5ea4-3a86-b803-332af31ae8e9 | -11.537 | -56.9447 | 2026-05-25 15:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a0310530-2d2f-3628-a511-4597cf94b9d5 | -8.6307 | -45.0085 | 2026-05-25 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 91fb37e5-173f-3929-bd8f-edad197def9e | -12.8857 | -58.209 | 2026-05-25 15:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| e06a3607-b50c-386d-85aa-4f78dd361308 | -7.8191 | -42.0573 | 2026-05-25 15:20:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 421.0 |
| e688dec9-3488-3d38-a799-280d7578e9ca | -12.9049 | -58.1875 | 2026-05-25 15:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 48281e85-faf6-38eb-8e63-3c783c64a3b8 | -11.5561 | -56.9232 | 2026-05-25 15:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 916bb25f-c7c3-3770-8d83-5c506c790e42 | -11.3584 | -52.9514 | 2026-05-25 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 4282aaf1-c15c-36b3-9f74-f4c607a15a03 | -8.6118 | -45.0105 | 2026-05-25 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 182.6 |
| c4a0187a-9cbf-3953-a27f-38fd3045fa21 | -11.537 | -56.9447 | 2026-05-25 15:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 56b7a835-64e7-32d6-8cf8-6fae32912a22 | -8.6307 | -45.0085 | 2026-05-25 15:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| a6bfe634-3fe0-3b8b-992f-81faeeacd09e | -8.6118 | -45.0105 | 2026-05-25 15:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 3ea2060a-d9c4-3b80-8ff3-1811642b44af | -12.9049 | -58.1875 | 2026-05-25 15:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| e3f5360d-d5b5-3da1-befb-362082ac6550 | -11.5561 | -56.9232 | 2026-05-25 15:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| e55d7405-aa06-3ad7-b708-b3c0f7271dda | -10.8725 | -49.7041 | 2026-05-25 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 7a3c96ce-4627-32bb-baa2-6f2a35f4b757 | -11.3773 | -52.9496 | 2026-05-25 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d2f20279-836f-33c2-8851-1b4349fff66a | -12.8859 | -58.1891 | 2026-05-25 15:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 230.8 |
| 3e2a5214-39d5-3469-ac70-16e4e764c4d7 | -7.8191 | -42.0573 | 2026-05-25 15:30:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 290.5 |
| d961d58a-f943-38bd-93a3-19acc07210af | -11.3584 | -52.9514 | 2026-05-25 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 182.1 |
| 467b9535-399d-312b-80ae-b7d44e0ad96b | -7.8191 | -42.0573 | 2026-05-25 15:40:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 319.9 |
| 5ac72bcb-4801-37df-b83a-b2ed16f17a1f | -11.3584 | -52.9514 | 2026-05-25 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 133.3 |
| ee4ad700-9699-3a07-b0e9-4832a10ebbb5 | -8.6307 | -45.0085 | 2026-05-25 15:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 27d28c9b-c7cc-3f81-814f-60677926322b | -11.5561 | -56.9232 | 2026-05-25 15:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 478e88d8-f24f-388d-8fdb-58c8bfe1dbc3 | -11.537 | -56.9447 | 2026-05-25 15:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d12d64b2-d171-3c08-87b2-34b504d5cc90 | -8.6118 | -45.0105 | 2026-05-25 15:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 4e491475-8df3-38d8-9879-6163fc55617c | -11.5748 | -56.9417 | 2026-05-25 15:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |


