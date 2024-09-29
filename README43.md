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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fe444b1-963c-318f-ab49-7823e292cac4 | -7.02764 | -45.33961 | 2024-09-29 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69969e69-9b46-33ed-b156-2411ba6df111 | -7.00273 | -45.34629 | 2024-09-29 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a7c27c6-3d59-3f90-9a87-8c22ae197bec | -6.99802 | -45.34577 | 2024-09-29 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b09c1b1e-0acf-3464-aff8-d140d4fb74b9 | -6.95058 | -45.68456 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fb45951-40c9-30fe-873f-5bb7ab4b24c8 | -6.58249 | -45.70418 | 2024-09-29 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f482e93-e51b-3346-b47f-a7f3cb0b8e9a | -7.19187 | -45.89386 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90519a15-894f-3f8b-bde5-a997fb8e5101 | -7.18732 | -45.89334 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68c815ce-ba06-331b-a794-c8ed3d546b79 | -7.05635 | -46.14767 | 2024-09-29 04:49:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c6b8c0a-fff4-336d-90cb-57ffc4806b16 | -7.05126 | -46.15147 | 2024-09-29 04:49:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 78d274c1-1fac-3627-ade7-2d04291399df | -6.94071 | -45.85337 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08846282-810d-3699-9ccf-594d594b09f0 | -6.94006 | -45.85793 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a34ee236-2a81-332b-8666-6c6398c17699 | -6.93617 | -45.85282 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21dc6a37-5766-3968-bb09-77fdb1ff06c8 | -6.93553 | -45.85735 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e5e4e54-85b4-3c79-a9f1-a69dae1c9f5c | -6.90463 | -45.97846 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 335c729a-4fae-39a0-b7e3-c959711ceabf | -6.90013 | -45.97788 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d307cb6d-58d2-3b07-b593-f2b769f4b38c | -6.89502 | -45.98167 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bc556ae-f566-3083-9cf4-28f75811f267 | -8.80385 | -46.76516 | 2024-09-29 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 752ad079-98d3-3d46-ad6b-93570d27bb27 | -8.80326 | -46.76933 | 2024-09-29 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e20c48aa-783b-3e70-88d8-dc5fc456ea90 | -8.42268 | -46.35414 | 2024-09-29 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6dc59ef2-b417-3a50-b120-9ddaecbd969c | -8.41818 | -46.35366 | 2024-09-29 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 175c7e42-5bf6-3556-800f-481e3b4d39c2 | -8.41756 | -46.35803 | 2024-09-29 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 286e66f1-e799-3886-a900-a03973fffcfb | -8.41371 | -46.35302 | 2024-09-29 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6531f9f-eed6-3dd2-834b-c4bee8a3dda8 | -8.41179 | -46.36652 | 2024-09-29 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e10370d-2d67-3809-bcae-517f70452915 | -7.8841 | -46.73428 | 2024-09-29 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb0f29a7-1580-395b-a822-afc3ecf31f05 | -8.91152 | -45.66574 | 2024-09-29 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f7a5d144-2084-3875-bf4e-6fe4241a32da | -8.90892 | -45.64952 | 2024-09-29 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a6a0980e-0560-3b1d-8742-845175061996 | -8.9082 | -45.65473 | 2024-09-29 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 0958b2ac-83cb-376b-a128-f747ed97e495 | -8.9075 | -45.65992 | 2024-09-29 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.1 |
| eded4579-4bf4-3182-8456-ca44a5dd3fbe | -8.90679 | -45.66509 | 2024-09-29 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 225a4a60-5f9b-39d1-83c0-7ffe1424715a | -8.90419 | -45.6488 | 2024-09-29 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 592d57ee-f1a0-36a0-bdc7-b8680c4c7475 | -8.90277 | -45.65927 | 2024-09-29 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f3b7653a-0861-35c1-8f69-ff6d9c8d844f | -10.7794 | -46.56221 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2657eb9d-7bc5-3bbc-8144-119cf37921fb | -10.77937 | -46.56 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3587ec79-0d6e-323c-9532-9d265eaa8e03 | -10.77876 | -46.56441 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14129707-f0e1-3e34-869b-37a2dbc49fb9 | -10.7749 | -46.56111 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31390f93-b9d7-392c-91b3-56208c5a9649 | -10.55991 | -46.38873 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e265e79-a4ab-32de-a44a-fa8269d9433c | -10.55589 | -46.02887 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 071e72bb-3e74-3f1c-b6a2-e4c32d004672 | -10.55117 | -46.02822 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0ea97f3-9180-33f7-9e4f-2028c7c0aa58 | -10.55052 | -46.03318 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b03d1e9-2837-3600-93b4-72ffde558a45 | -10.5352 | -46.07686 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb5e76af-336a-3902-acd1-49f00629c8b5 | -10.53361 | -46.03861 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97542ff5-62f0-3bc9-8488-0c1fec766f7e | -10.5282 | -46.04298 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 413d7de5-5274-38af-bc43-e724ae99a4c2 | -10.49019 | -46.31846 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3a012e3-c18e-3532-b695-b014b7f92336 | -10.48908 | -46.32087 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f47804b9-b0c7-3068-b106-2e997ac4c2e2 | -10.48846 | -46.32565 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9baab20f-320a-3619-9fc0-f2ce51f36fef | -10.48489 | -46.32267 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49f7a52e-2ccc-3e19-a208-929d03c0f9ff | -10.36922 | -46.17675 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e541a86d-ce70-3bf5-a60a-889c71615441 | -10.36856 | -46.18159 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81502d72-d35d-3248-82aa-1bb3114ccc62 | -10.36522 | -46.17127 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b3cb87b-35c8-3bcb-a5d8-b61653eeb58b | -10.36055 | -46.1707 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 179685bf-7617-3918-9a66-0ce034ae4f64 | -11.31363 | -46.30256 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e024df5-084b-36f3-902a-08a5ea2ea882 | -11.30331 | -46.16307 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bd92e1f-344a-3d6e-a1ad-0175771d8cb0 | -11.7915 | -47.6066 | 2024-09-29 04:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71c648a2-152d-3790-8711-fb53a95ba44e | -11.78718 | -47.60608 | 2024-09-29 04:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 584ba2e4-cf61-3a97-918f-1dd0b0fa1611 | -11.69796 | -46.35282 | 2024-09-29 04:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c70bb5f5-0d8f-3cb6-a1d3-e4a27e7e9e92 | -11.69326 | -46.35218 | 2024-09-29 04:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6aa09d34-1244-3395-8af1-9bf0456cbe45 | -11.69263 | -46.35709 | 2024-09-29 04:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e98dcb5-737d-30f4-8466-6c37f4882d39 | -11.45863 | -46.95903 | 2024-09-29 04:49:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1675b572-55e5-3653-9a1b-19dcf5527841 | -11.45411 | -46.95861 | 2024-09-29 04:49:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa7608da-6a73-3b10-b24d-fd0f009b1ac9 | -11.41172 | -47.23626 | 2024-09-29 04:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a538b27-5de4-35ea-8fbf-e0460fe9eb81 | -10.92028 | -46.38506 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b262f0a-5fd8-3eca-ba81-e3425cb961bb | -10.91962 | -46.38982 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ac14fc8-bb7d-3471-a2a6-891082b64cf8 | -10.9196 | -46.38284 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0586e88-ca59-3051-9c13-806640a358f3 | -10.91898 | -46.38758 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4bd029c1-8079-386c-aa4a-c24ef440d4de | -10.91565 | -46.38444 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03f32f10-500f-30ee-8e94-2a284a5206cb | -10.91499 | -46.38923 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 195d0974-50d7-3c18-840d-24b640749c28 | -10.91497 | -46.38218 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a28428c-fc94-3e71-b03e-9cadbe9f1c03 | -10.91435 | -46.38697 | 2024-09-29 04:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a38dd9af-080d-3c8e-8800-8f0ded80e654 | -4.58519 | -47.09772 | 2024-09-29 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67165fb3-4a72-3d2a-8c79-e55af0e24b2a | -4.487 | -47.75804 | 2024-09-29 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53a0e299-80db-3d9d-8efb-adf1ed605f38 | -5.76422 | -47.44193 | 2024-09-29 04:49:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43b9c69c-628c-34b4-9319-6c4862742569 | -5.76372 | -47.4453 | 2024-09-29 04:49:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2453c60-9b4c-3979-b606-a1e8611fdfed | -5.76022 | -47.44134 | 2024-09-29 04:49:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abefaa71-1104-3f8d-b776-f2fba524181f | -5.39969 | -46.58187 | 2024-09-29 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb029610-0dfa-392b-b507-d60ac0a38d25 | -5.39913 | -46.58575 | 2024-09-29 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8cdc0cb7-d48e-3a82-be8a-b6388ac8feec | -5.38123 | -47.50901 | 2024-09-29 04:49:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbcaeebd-ca27-3a07-a4c0-c2d54f046337 | -5.32584 | -47.69545 | 2024-09-29 04:49:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb44e19d-b728-3123-9bdd-86d27504d4cd | -5.32512 | -47.6979 | 2024-09-29 04:49:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4b9e77b-490c-382f-8074-0ac50e2e9add | -5.24399 | -47.38708 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea02f23c-e25d-3924-86a0-26394f62386b | -6.16066 | -47.71146 | 2024-09-29 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e436a10-daa0-33b2-aa61-7c9c4009e6d7 | -6.1599 | -47.71653 | 2024-09-29 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ce36732-a9d5-389c-9c4e-192be7b7b6ed | -6.15672 | -47.71075 | 2024-09-29 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76d37d08-44d7-3dbc-bdbf-c5df8cac18fa | -6.15596 | -47.71585 | 2024-09-29 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bad81b6e-6249-3806-9103-e25c6e721cd4 | -6.15278 | -47.71009 | 2024-09-29 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b106ab7-8b52-3093-9d13-5379c1c398df | -6.14997 | -47.64716 | 2024-09-29 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce8ec1d0-1af8-3df3-8818-2335cfc4b5c9 | -6.12281 | -47.26811 | 2024-09-29 04:49:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08188d6f-17d0-3854-a08d-0cd450f0c34f | -6.07797 | -47.65015 | 2024-09-29 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3d9ec8ea-c87a-3601-8c96-0652dd982214 | -6.07719 | -47.65528 | 2024-09-29 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f021a8ab-5c8a-3fd3-80d1-bee059eb4a39 | -6.02762 | -47.43866 | 2024-09-29 04:49:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0678b998-a6d6-3a14-8fc5-68fbd9356557 | -6.02711 | -47.44216 | 2024-09-29 04:49:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1a27645-e8a0-3316-aebd-eda1612ef535 | -7.52997 | -47.95811 | 2024-09-29 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97c30879-3c95-3e07-95d2-19d783f575a1 | -7.10342 | -48.05329 | 2024-09-29 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e3cb4ea-4997-3bd1-b5db-937eeb47e63c | -8.35663 | -47.56089 | 2024-09-29 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 09750b9a-5799-3ae1-8a6f-cefce664d0db | -8.31698 | -47.5442 | 2024-09-29 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3c9eb71d-6474-389b-9472-0df83411c559 | -8.10529 | -47.68932 | 2024-09-29 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e13f57d9-7218-3624-87fd-2e69a8277ba6 | -9.89272 | -47.41209 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5f88775-21c3-358c-b4a5-0027d41717fb | -9.88846 | -47.41155 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6fa351ec-2a8d-3add-b0a2-c5420fb41682 | -9.88788 | -47.41562 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d930ddd-65c5-32ab-9e1c-167ae47d6ac7 | -9.88363 | -47.41503 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2622917c-a362-3994-87d6-d3d92e8dc3e6 | -9.88306 | -47.41905 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README44.md)
