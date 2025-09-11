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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e1d50e3-47b8-31c4-bfb1-2995317716da | -8.5092 | -45.6581 | 2025-09-11 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| dc9eafb4-0ff8-32b7-b672-06fab02a2672 | -8.7411 | -45.2248 | 2025-09-11 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 158cdd02-2150-391e-b138-c35d4de461dd | -19.2617 | -47.999 | 2025-09-11 12:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 105.5 |
| ffb2fc7d-3f5f-3bef-ad8e-48a22a946364 | -11.7211 | -46.5127 | 2025-09-11 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| a212cf36-83c6-3d66-b4e4-c9bca6a3da06 | -15.1367 | -52.4466 | 2025-09-11 12:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 2f4eaf6a-ceaa-3cfa-a6a1-188923ea3d86 | -6.2228 | -43.3226 | 2025-09-11 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| e78a517d-e59d-373d-a08b-25a7ca4de24a | -14.1297 | -45.4043 | 2025-09-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 82d988a5-6eef-3cfd-815d-2af4fd8d3935 | -12.6825 | -45.2977 | 2025-09-11 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| f89fd427-ee61-3aa3-b8b3-848ab6de79b8 | -9.0358 | -45.783 | 2025-09-11 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 63786c86-b770-38bb-9817-bfa813cc54c4 | -10.5671 | -47.2442 | 2025-09-11 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 69d14a70-2c67-32a7-909b-1450adba9972 | -9.1328 | -47.0054 | 2025-09-11 12:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a7491b0e-9510-3207-9cee-fa69a4cd6f55 | -13.2602 | -51.7548 | 2025-09-11 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 66df873a-3574-34b9-b293-7ffd4d1bba66 | -15.1759 | -52.4199 | 2025-09-11 12:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f65c431e-f153-3605-9003-237b1bf43edb | -6.2226 | -43.3459 | 2025-09-11 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 70b46769-5b08-3a36-a901-a8917bdc66ba | -19.9994 | -47.6271 | 2025-09-11 12:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 1f220fa8-ec98-3d5f-9f48-6eb41ed97b4d | -12.6829 | -45.2746 | 2025-09-11 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 1f9336b7-b9a5-36e0-b81f-43c78f34a170 | -9.039 | -46.9707 | 2025-09-11 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2d5589fe-f622-3f2c-89ab-01ae7daff9bc | -19.2611 | -48.0221 | 2025-09-11 12:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1dd16d54-b34b-3495-80e4-6b0e594c7e42 | -11.3931 | -45.581 | 2025-09-11 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f1814671-b846-3549-b442-99987575755e | -15.118 | -52.4066 | 2025-09-11 12:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 12bdfc3d-db1f-38b2-aa5c-af556e5006b8 | -8.7547 | -47.1107 | 2025-09-11 12:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| e2aab304-279d-3ad2-ba9b-e03bd95dc87a | -11.7786 | -46.5047 | 2025-09-11 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 2bccc46c-438f-3f88-9e22-378cb4659364 | -8.1649 | -46.0983 | 2025-09-11 12:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 15b8fc71-44af-3398-8ea4-5c8bce154f44 | -15.1176 | -52.4279 | 2025-09-11 12:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 0a6dc2f7-924b-37c6-9a58-7cb55e3f7b8a | -9.0547 | -45.7809 | 2025-09-11 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| c5b52b22-4af3-35c1-8f58-ce98956f1821 | -14.5125 | -53.9367 | 2025-09-11 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c0e3d187-5f01-3c94-8799-2bc3bbf07df4 | -14.1492 | -45.4009 | 2025-09-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 646c9c18-0671-33f5-80d5-2fd271e82e0b | -15.1565 | -52.4226 | 2025-09-11 12:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 193de589-3f46-371c-a8e1-7095008cef38 | -9.0355 | -45.8056 | 2025-09-11 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 0c90bf26-f31d-3d91-abb5-4cfbaede843b | -12.6632 | -45.3008 | 2025-09-11 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| f0181af8-ce3d-3d5b-adba-6007ef7fca6e | -15.1561 | -52.4439 | 2025-09-11 12:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 311654c4-75c6-3660-a40f-b78c86e07ef5 | -15.6737 | -47.016 | 2025-09-11 12:10:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1c7f62fa-e256-39fe-9c66-c908d71b0fef | -11.4285 | -43.5544 | 2025-09-11 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2f0dd4a5-4845-3f83-b330-69cd9474c4ff | -13.241 | -51.7571 | 2025-09-11 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| df074767-e37b-35e0-a3c1-10b84a825048 | -12.9837 | -44.6686 | 2025-09-11 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ead65567-616f-3b1d-91fb-aee8e77e865c | -19.9994 | -47.6271 | 2025-09-11 12:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 1e5e1572-79e5-3936-b3a1-8f2d573c5257 | -15.6732 | -47.0389 | 2025-09-11 12:20:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 312.2 |
| 7871df69-3aad-3a57-8d90-d3185d370cb1 | -10.1844 | -46.1927 | 2025-09-11 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ea3569de-6994-329d-979a-8b604f5586e6 | -8.1649 | -46.0983 | 2025-09-11 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| f8340802-4d94-32b5-bc7f-f13e0449820b | -9.0579 | -46.9688 | 2025-09-11 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| f44e1dea-e821-38b0-ad1a-680f4647849a | -12.6825 | -45.2977 | 2025-09-11 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 30b21e1f-0b3c-32f7-8cca-a25b2ae89976 | -11.779 | -46.4821 | 2025-09-11 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 412399ae-b5f9-3526-ac44-0e7b0cc669e9 | -15.6737 | -47.016 | 2025-09-11 12:20:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 116.9 |
| db6a64ac-a1c6-34ae-9f7e-63e094fc3a96 | -14.1492 | -45.4009 | 2025-09-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| be3f4ebf-0202-3cc8-b0a5-4973c6212a4d | -19.2611 | -48.0221 | 2025-09-11 12:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 91837179-cea5-3063-ac03-2eb5541691ed | -15.1367 | -52.4466 | 2025-09-11 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| ed8d3f67-6b98-3c65-89e1-ce2ade81e1bc | -8.7411 | -45.2248 | 2025-09-11 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| cec6b094-85cb-3933-98cf-68dbac395c0c | -15.1016 | -50.1468 | 2025-09-11 12:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| fbec60b1-e829-3fe6-babd-fe9ea31d46bf | -15.1561 | -52.4439 | 2025-09-11 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| d44abaf7-95f5-36b3-aff0-7a6bf4b14980 | -15.1759 | -52.4199 | 2025-09-11 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b5058a42-0088-3c41-9f5f-b6ae3aeba89d | -21.4328 | -48.9201 | 2025-09-11 12:20:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 111.7 |
| f002ef96-5578-35f4-99f3-0b3c35da12a1 | -8.7547 | -47.1107 | 2025-09-11 12:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 52b854fa-9f0f-3a1d-b814-a8d5dc1038b7 | -9.039 | -46.9707 | 2025-09-11 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 190f5a14-aabe-3604-9852-db1e73031667 | -6.2228 | -43.3226 | 2025-09-11 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a1308258-49c1-3ad7-821d-1f92a84dbd26 | -9.1328 | -47.0054 | 2025-09-11 12:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9257f8f1-0fb2-35be-a869-9b1ef9aec77c | -14.5128 | -53.9158 | 2025-09-11 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 576b3ac9-8487-3916-91e5-79fe61157e52 | -9.3058 | -46.7644 | 2025-09-11 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 80f0dfca-6255-349f-95cf-6da8e6a9d823 | -12.6632 | -45.3008 | 2025-09-11 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| fb5622b8-0604-3fb4-b43d-1e8e60c457dd | -19.9988 | -47.6505 | 2025-09-11 12:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e0103def-22c8-35d7-8a59-1a5f3af28ef9 | -8.8755 | -49.5613 | 2025-09-11 12:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 96d19c42-7717-3887-8ed7-0005dd472da1 | -9.1331 | -46.9831 | 2025-09-11 12:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 69c757f4-e5be-3d4c-b81c-3e44b38ae6e3 | -11.3584 | -46.5167 | 2025-09-11 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 1c274a24-da80-3761-be71-c0465cc73835 | -11.7786 | -46.5047 | 2025-09-11 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3166e320-2e9b-339b-a120-0d49c3f3954a | -11.4285 | -43.5544 | 2025-09-11 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| dc9aa530-05d2-3398-8d06-acfd3b6cd613 | -13.2602 | -51.7548 | 2025-09-11 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 4982a5da-cf0f-3caa-884c-cbc67b3f23b6 | -22.9828 | -49.7336 | 2025-09-11 12:20:00 | GOES-19 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| 35b1ac71-9653-36ab-942a-916faa0eb45a | -15.1211 | -50.1438 | 2025-09-11 12:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 6485040c-d3d6-3e11-91fa-9996d5011933 | -9.7445 | -47.8468 | 2025-09-11 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| cf3d477a-e51a-3adc-a371-0603c502faa6 | -12.6829 | -45.2746 | 2025-09-11 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| a6903880-2b06-35c0-af27-1beec2944320 | -8.5275 | -45.7014 | 2025-09-11 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2722ace7-3129-31f9-8e16-79e0c81da9cb | -15.8014 | -52.2258 | 2025-09-11 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 14cf3003-51cb-3492-bcc1-5a3dcbf595f7 | -6.2226 | -43.3459 | 2025-09-11 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| fed4ecc0-45bd-362a-9a77-3f297512f06b | -8.5667 | -45.5842 | 2025-09-11 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 3da83b86-2079-3648-808a-fe71b839128a | -7.8708 | -45.5181 | 2025-09-11 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ea8fa75c-f77b-329d-b52b-1fff30cd1a74 | -15.1557 | -52.4652 | 2025-09-11 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 4228b482-b399-3b16-97c5-f92edc04ca07 | -14.5125 | -53.9367 | 2025-09-11 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4967b24a-d9bc-330d-9e1a-f09c844ac921 | -15.118 | -52.4066 | 2025-09-11 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 133.6 |
| d9c15148-e7f2-3f4e-ad70-69f410c1daff | -15.1176 | -52.4279 | 2025-09-11 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d2488f92-67a2-3d02-8755-a258e028a928 | -19.2617 | -47.999 | 2025-09-11 12:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 079f8c9a-0dc8-35e2-809c-87034e317eb5 | -11.7211 | -46.5127 | 2025-09-11 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| b7e47cd2-7170-3119-95e7-3c4b411a13d8 | -15.1176 | -52.4279 | 2025-09-11 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 149.8 |
| d7f88909-566c-3a73-8a7f-19d64ad71bed | -15.6732 | -47.0389 | 2025-09-11 12:30:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 465.1 |
| 5d016821-7ab5-35bd-886d-860efbf7a7ac | -8.5275 | -45.7014 | 2025-09-11 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 9e312f11-5f12-3057-a168-e39c6a0461f3 | -11.7786 | -46.5047 | 2025-09-11 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a53cb538-879a-3cf7-b098-da15a35319a9 | -15.1371 | -52.4252 | 2025-09-11 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 161a73bd-fad4-3401-bebe-fd6d9a718787 | -14.5128 | -53.9158 | 2025-09-11 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ab421e51-936f-3aed-af80-9fb1c9268775 | -9.0939 | -47.0983 | 2025-09-11 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 252.1 |
| b20cb952-3bea-3423-b5a5-d25b28f02704 | -9.075 | -47.1002 | 2025-09-11 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 74c5670e-7c4e-3db1-bc41-90875422eb6f | -9.0753 | -47.078 | 2025-09-11 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| c6ae87cd-7228-31dc-867c-b9b6b64bebf5 | -15.1016 | -50.1468 | 2025-09-11 12:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 733bae91-417e-3a36-9ce0-df00dc17d386 | -15.118 | -52.4066 | 2025-09-11 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 216.1 |
| ed5fde30-b16f-35cd-9467-d98ef2b46f07 | -9.0942 | -47.076 | 2025-09-11 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 8a95646f-d87a-3fc9-a61f-8304be155939 | -8.1649 | -46.0983 | 2025-09-11 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| ab07a730-3835-3b76-9027-de82f4351e51 | -15.1367 | -52.4466 | 2025-09-11 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| d775248a-f7d6-31da-8d1d-66056765eefa | -19.9994 | -47.6271 | 2025-09-11 12:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 46d7e826-e43c-38c5-a9b4-ad40427aa62c | -10.5671 | -47.2442 | 2025-09-11 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 683d0f9c-e443-3eef-8ffc-17ad5fe21978 | -22.9828 | -49.7336 | 2025-09-11 12:30:00 | GOES-19 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.2 |
| c7bf2653-b491-3ea1-9095-23d2e2ea6513 | -12.6825 | -45.2977 | 2025-09-11 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| abe3a2b9-050f-33b8-9103-0894802ac199 | -8.8755 | -49.5613 | 2025-09-11 12:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 211.9 |
| d7be4d45-4aa8-3ee1-93c8-eb4c804cc8f6 | -9.039 | -46.9707 | 2025-09-11 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |


[Clique aqui para ver as próximas entradas](README138.md)
