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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fd92d26-1904-3a3b-92f2-2396783d0e2a | -10.05742 | -59.11811 | 2026-06-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95b18470-3bb0-376c-ab2d-03d004f3c62b | -9.0303 | -61.33298 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b19d095-1936-392c-bbba-ad11cbc0db15 | -9.76142 | -56.9334 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b19ae18f-3e6b-35ca-92e9-a7dce6f75d0c | -11.7885 | -57.35056 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1994212-4ec8-3c73-9c4b-3d76eddee746 | -11.66395 | -57.25988 | 2026-06-27 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2d400ce-728f-3f4c-8470-544d2227ea70 | -10.78768 | -54.1101 | 2026-06-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0ede271-45a9-35ca-ba04-0ceaf5f66706 | -10.38648 | -56.71952 | 2026-06-27 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a951156-5114-32e4-a0e7-d9c0a0b67cd3 | -11.91811 | -57.10249 | 2026-06-27 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3948ce7-90e7-3195-bc86-6afdc3ac5797 | -9.03772 | -61.33035 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ab89f24-5156-3cbb-a980-c68177ca65d8 | -9.5896 | -56.92462 | 2026-06-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bdfbc25f-a6fe-3058-8be7-164e04cb10b0 | -12.08009 | -54.61297 | 2026-06-27 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea87d00e-50a8-3aef-bf32-b1af3280a048 | -11.32363 | -54.46355 | 2026-06-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56847610-7a76-3c11-8822-3d4dbef07fec | -12.07959 | -54.61672 | 2026-06-27 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a87a3abc-f593-3a1f-bfc8-78a4d4ecdc10 | -12.4646 | -58.49279 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 30e19559-10c4-3cc3-a360-60d295c6d1cc | -9.47441 | -48.07106 | 2026-06-27 05:18:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36a73256-5a7d-3fbc-9590-51b971a42ae4 | -9.1938 | -58.0512 | 2026-06-27 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42f82e57-8e45-3eb2-a3b9-896fc56a8202 | -9.02869 | -59.54224 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76fc19eb-03de-382c-b861-5e467b9d8206 | -10.77982 | -54.10505 | 2026-06-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d177726b-3021-351a-9f90-5991c0fa7512 | -9.0315 | -61.32554 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a65393dd-9941-3ebc-896f-a353acd650ab | -12.45279 | -49.58174 | 2026-06-27 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9e09144-a342-391f-9b9e-5985b5ff67c4 | -10.01845 | -59.34791 | 2026-06-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7138277a-0fde-35af-a6f7-5c198921bfb3 | -11.91078 | -57.4049 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f5a3009-0956-3ec1-b012-cf31018f8bca | -11.90552 | -57.41634 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d2d789d-52c9-395e-9643-bf6eaccaa1d4 | -12.55332 | -54.58643 | 2026-06-27 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34b6602d-689c-3c53-ab58-bc6b0196739b | -12.79762 | -54.86377 | 2026-06-27 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8770c6f-e321-3a8c-bde1-cf4ad816aadd | -12.6236 | -57.8926 | 2026-06-27 05:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| bc8c66ed-7291-3f7a-9413-3d91e0804530 | -12.4654 | -58.481 | 2026-06-27 05:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 491b5532-e743-3748-9de6-e75ef2978a1c | -12.6046 | -57.8942 | 2026-06-27 05:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| f3cc9ec7-0f07-3f23-81e5-893bd3ff856a | -12.4651 | -58.5009 | 2026-06-27 05:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 025294f0-c45d-32f6-9778-d1495bdb87ee | -15.45965 | -59.23549 | 2026-06-27 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 24af89e2-2179-32d5-b78f-8bf89c04a715 | -13.25853 | -54.4058 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d6c21b9a-c462-3a1e-8b18-80561548615a | -14.87488 | -54.52962 | 2026-06-27 05:21:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f059f664-7433-36d9-813c-8ef4ab77033d | -14.87383 | -54.538 | 2026-06-27 05:21:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70cbb2d3-e49c-3a1a-bd57-f2138b11c6c2 | -13.26287 | -54.41217 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5b6c157-86ef-37f7-a0c2-2874313c1218 | -13.26654 | -54.41101 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00d2876e-57b3-313a-ba03-1b1a47aea5c3 | -13.25009 | -54.4104 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 23d216d7-ab39-386d-b380-56365d6da629 | -14.84849 | -48.14546 | 2026-06-27 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d32b632f-54c8-3ea5-9731-f37d4a4be188 | -13.64916 | -55.29329 | 2026-06-27 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9543d090-ef5e-34e1-80b9-b9d4c7cba1aa | -12.93617 | -56.64135 | 2026-06-27 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c901e33-17eb-36d5-8aa3-ddcd22626f53 | -13.67126 | -53.94262 | 2026-06-27 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3d13036d-e99a-3d45-90b0-0bb5c00fcd0d | -13.86897 | -50.40035 | 2026-06-27 05:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af0be2b2-731a-3cd7-9cfd-e64e4c802c72 | -15.37465 | -60.16214 | 2026-06-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6746d35-3c07-31b3-9d35-cdd7cca62725 | -14.87436 | -54.53381 | 2026-06-27 05:21:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7cc1a4ea-d6fb-39af-ae5a-6d0f619c6e68 | -16.1751 | -58.4761 | 2026-06-27 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0ee2652a-26ae-3853-bca4-2ff81efb5045 | -14.87815 | -54.53866 | 2026-06-27 05:21:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65abaea4-d4b4-3cac-9ca3-54a87c1b6931 | -12.93439 | -56.62742 | 2026-06-27 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ddea009-7ddc-3886-ac2c-74a8d0a2b3ff | -13.24955 | -54.41442 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc27de2a-0ee7-3c18-ab3d-0e4e329c6816 | -12.7705 | -59.00488 | 2026-06-27 05:21:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52e17607-10c0-3271-9ede-fecc7c5fe4d2 | -13.24583 | -54.40981 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8353fecf-f09a-356a-94a7-fb08a96fbe78 | -16.07276 | -60.15254 | 2026-06-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b9a00c1-c25e-32ea-a1f0-026bef8be51d | -13.60382 | -56.59778 | 2026-06-27 05:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8ef9acd-2098-32be-9a69-942314ff6147 | -15.58741 | -46.81277 | 2026-06-27 05:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 624157eb-339a-3331-8d8d-ca1538b0a18a | -13.66683 | -53.94205 | 2026-06-27 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce5a33b2-5bfa-3c8d-9c02-8a7333846472 | -15.45683 | -59.23118 | 2026-06-27 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e272a3b-0d1a-3751-997f-f27c60b5c6ef | -13.26713 | -54.41275 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1467234-1b00-33a8-a6c2-af7bb6ee01f8 | -12.93375 | -56.63188 | 2026-06-27 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3bd71e3-f2a5-3661-b1c2-cac5e6f38705 | -13.22665 | -54.42347 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ca667277-88ab-3b5e-9f30-e94e6abd3751 | -13.25915 | -54.40756 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 829d4abd-f20a-33df-8c34-b79bebd1aa85 | -12.7733 | -59.00904 | 2026-06-27 05:21:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e00fdbeb-772f-375f-ab38-4b3446afdd4c | -13.26175 | -54.41449 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13ee41a8-e3c4-3b51-b4bd-a5c6c7c2bd6c | -13.23091 | -54.42408 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9f36571-d9b9-3629-9816-b6c225c7ca57 | -12.93922 | -56.64637 | 2026-06-27 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fc44972-f8c9-311d-bb77-efde3e7b3fbc | -13.26279 | -54.40639 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3747f04f-d50c-3cda-b928-c533254523ae | -14.87867 | -54.53447 | 2026-06-27 05:21:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e3f83196-5fab-3840-b559-8d4945914ebe | -12.93744 | -56.63245 | 2026-06-27 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56a93eea-7a68-399e-a660-5bb3e80b0da3 | -12.76715 | -59.00435 | 2026-06-27 05:21:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4323e99c-b17d-35e6-ac76-e514d6f62f9c | -13.25435 | -54.41098 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e54aef8a-e3bb-3ccd-adfa-cd03f007a9f9 | -15.45571 | -59.23873 | 2026-06-27 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1a74a08-6faf-3ebc-8f72-65b2ef12f195 | -15.59114 | -46.81245 | 2026-06-27 05:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25e5171d-ed2c-3a8c-9fa7-32eb31cf278d | -13.2597 | -54.40353 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 724a0f1c-0a25-3982-8821-deb17312e70c | -13.26342 | -54.40814 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9bc85e2d-a1b2-3959-bbbd-0d658863307e | -16.08051 | -60.14638 | 2026-06-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65010db4-ca26-3362-b306-320bd9f04037 | -14.84916 | -48.1385 | 2026-06-27 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bba783a4-410d-32b0-81a8-7740c8273e12 | -13.24637 | -54.40579 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3b2bc60d-7925-36b6-a4a3-8b62a3bfd774 | -13.24211 | -54.40518 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7da73b8-1c8a-3870-b9b1-aad8381f1f95 | -12.19299 | -64.36001 | 2026-06-27 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2d18c53-3e53-31e4-baf1-79dafb0bd3bd | -13.64512 | -55.2927 | 2026-06-27 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 338239d8-2b48-3a7a-8e5f-84a51b5f2e30 | -13.26658 | -54.4168 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e2d4030-01f4-311c-84d6-b7f7f8b2cd79 | -14.87762 | -54.54287 | 2026-06-27 05:21:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99064784-0bc5-33a0-858f-8208ba1793b8 | -16.07609 | -60.15308 | 2026-06-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 073f9429-239a-3dd6-bd32-82a429334bcf | -13.8673 | -50.39738 | 2026-06-27 05:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ce06002-d367-36a2-90de-9ba2753a851f | -15.45627 | -59.23495 | 2026-06-27 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdbf0bcb-cf11-3957-a53a-da6f123f89c8 | -13.66296 | -53.93706 | 2026-06-27 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c75839d-9e7a-3dbb-9f5c-f18252c7219b | -14.84966 | -48.14319 | 2026-06-27 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7b4642e-7f47-3d20-b491-42e00dc30a4f | -12.93986 | -56.64191 | 2026-06-27 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb83e6d6-0564-3744-bf1f-1f643d45b96b | -12.9368 | -56.6369 | 2026-06-27 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbd98f33-abc2-300c-821f-cea66a0007b2 | -13.66739 | -53.93763 | 2026-06-27 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c7752bcd-cf55-3c31-a4a4-e5808e685428 | -13.25489 | -54.40697 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 451be3f8-ac90-33a3-8c98-8fa9954b6002 | -14.84318 | -48.14175 | 2026-06-27 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5d75b29-8a8c-3093-9156-012435754510 | -13.26227 | -54.41044 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8565da25-f595-3dbc-8a53-ad2eb249edd2 | -13.25801 | -54.40983 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc24b2b0-0c91-34e9-ba76-71479eb9111b | -13.25861 | -54.41159 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db1a4860-f977-3385-bdfb-72b23184eb2c | -13.6624 | -53.94146 | 2026-06-27 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a139e859-d271-3390-bf7e-583eb5ea1a0f | -13.25063 | -54.40639 | 2026-06-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e0e4955c-d16a-3280-a541-c3bc36bdf9e0 | -13.60447 | -56.59317 | 2026-06-27 05:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab3d6b19-e690-3129-b2c0-3425da5d489b | -12.94291 | -56.64694 | 2026-06-27 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99d0df3c-0b43-3de2-8644-8451bf9b7a96 | -12.9405 | -56.63744 | 2026-06-27 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 375a671f-1fe5-3ae4-9a0a-3b376e1b2473 | -21.7593 | -56.26494 | 2026-06-27 05:23:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 00869865-b01b-3668-87b6-69872eacce1a | -21.77384 | -56.28821 | 2026-06-27 05:23:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0c00014-ffd9-3f3d-9b5a-6a8b2441b91e | -21.77434 | -56.28396 | 2026-06-27 05:23:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README19.md)
