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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a95f32f1-9c31-3bad-a043-6f91f3964d8c | -8.4506 | -47.3614 | 2025-09-01 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1eeb468b-ed8e-3589-8516-cb1c26801b1d | -8.8437 | -47.5217 | 2025-09-01 14:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 5bf386ac-bc10-3221-b91a-8c45ec15dff8 | -8.8936 | -45.1168 | 2025-09-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 187.4 |
| da316ee7-165a-3d45-8f59-9b0cbebbd33f | -10.6284 | -48.2314 | 2025-09-01 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 0a79d1af-d196-3d30-961e-8799e3517b61 | -10.9873 | -49.6267 | 2025-09-01 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| bf8db612-8d15-358d-b4b1-367d39c91206 | -8.7068 | -62.3995 | 2025-09-01 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 711134c9-a832-32e2-897b-30b612ec73b8 | -11.9623 | -45.8428 | 2025-09-01 14:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 0e450a15-760b-3d3d-ba3f-0bee8c080739 | -6.9327 | -42.006 | 2025-09-01 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 463b3805-6f97-3d73-b98a-34113cebed36 | -8.6883 | -62.4002 | 2025-09-01 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.7 |
| fd60d122-9267-33a2-8718-7ca07fa25fa6 | -9.4987 | -46.4749 | 2025-09-01 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 0dea9f4e-0358-3a0f-bd2b-283234c27102 | -11.3901 | -43.5602 | 2025-09-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 278a1a22-7558-3c45-bb83-4a0313475a14 | -7.9536 | -46.4765 | 2025-09-01 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 275.6 |
| 750db5ba-a26e-3798-853b-f00c341389ae | -11.7985 | -46.4567 | 2025-09-01 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| b07c61d7-4e64-3c90-a483-40ff97cd386f | -6.8095 | -52.8154 | 2025-09-01 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 07d93f54-07df-3f44-a1ba-2964d6b9ad03 | -8.9664 | -65.961 | 2025-09-01 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c7702a8c-6b40-366d-96c0-533ef1650023 | -7.6946 | -61.4712 | 2025-09-01 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 48bec551-8a11-37d9-be3c-5c78576df6c7 | -9.6607 | -47.0597 | 2025-09-01 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 95f2069f-bbaf-3c9e-98d3-9debbc01f58d | -6.8237 | -43.3402 | 2025-09-01 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 31026ab1-1129-3a41-8ddf-19d62f964e76 | -9.2633 | -47.1249 | 2025-09-01 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ce579d79-d817-3863-b2d2-86c7f6aeac0f | -6.8279 | -52.8348 | 2025-09-01 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e4da082b-e42c-3ea2-8d33-330841f12ab8 | -6.471 | -44.7792 | 2025-09-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 613173f6-a5bd-3a21-bda4-50918d9f90a4 | -11.3701 | -43.6104 | 2025-09-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 22ff90a2-cbbe-3e35-833e-f1ad41e4e1ae | -11.3709 | -43.5631 | 2025-09-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 0f6c311c-1529-3a4f-a094-055d94ef8c46 | -8.8744 | -45.1418 | 2025-09-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| bba704f7-9603-3a23-88a9-9e82f81315b7 | -7.7839 | -50.0585 | 2025-09-01 14:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 93e7d171-63b1-371a-acae-301c2cdfd1bd | -6.8281 | -52.8143 | 2025-09-01 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 82412644-24b0-34da-96ac-7bde899bbece | -8.9125 | -45.1147 | 2025-09-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 9f2ee529-8cd1-3848-adc9-46591389bd3e | -14.7427 | -46.7472 | 2025-09-01 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| b26ce8b1-a131-3bea-9ea3-9c5bef4db25a | -8.8625 | -47.5198 | 2025-09-01 14:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 4e024c15-a08b-3350-8336-e10e4f5da5a4 | -8.6882 | -62.4192 | 2025-09-01 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d8882e60-a164-34b5-bc6b-60c362c8efa5 | -6.8466 | -52.8132 | 2025-09-01 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 29f96aac-fe7f-3bac-a5e9-843f3c508ea2 | -8.8454 | -64.15 | 2025-09-01 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 1807ac36-38cb-39ac-9ccf-71a0688c10f3 | -6.824 | -43.3168 | 2025-09-01 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.5 |
| e5e7b4c3-7419-3bf8-bf47-2b1d3785edd4 | -9.6127 | -47.8169 | 2025-09-01 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a04c0755-713b-363f-806c-3fdcf3a90e39 | -8.6316 | -62.5921 | 2025-09-01 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5f51d744-41e5-3a5d-a51b-72adf2d8bafa | -14.0502 | -44.5779 | 2025-09-01 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 1a73e881-b2e9-35df-ae1b-63970ac0f10e | -6.9129 | -45.5593 | 2025-09-01 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| b442ba6b-e608-35b3-b658-fc92f48bf6a8 | -7.1089 | -44.7703 | 2025-09-01 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 8e127e5d-6b3e-3939-971f-cd662a3007b8 | -13.5171 | -46.994 | 2025-09-01 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3288b30e-1b64-39c8-84e5-6888ee01da91 | -7.0572 | -44.3393 | 2025-09-01 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 4cc913f8-f0d2-3b58-8710-209484155571 | -5.6573 | -43.6465 | 2025-09-01 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e3e9070d-d719-3f36-bb89-5bf9e040a860 | -8.6315 | -62.6111 | 2025-09-01 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 72226fbb-4065-3698-a7df-0ffc59d9eb88 | -9.1567 | -45.2243 | 2025-09-01 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 4fe13e82-3dc0-3a7d-b50f-3dc4d45dcf89 | -9.4 | -48.2119 | 2025-09-01 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 3011f2b2-b598-3656-baeb-20fc59436262 | -8.0676 | -48.0112 | 2025-09-01 14:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| fccf68a1-da53-360d-a5d5-0767a4639ff9 | -11.6183 | -51.9427 | 2025-09-01 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 776d7ef0-1e9a-34e4-89cc-f0a4c142753f | -11.3888 | -43.6312 | 2025-09-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 72be604d-692b-33fa-8469-4873f272e00e | -8.1943 | -46.788 | 2025-09-01 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 8d4a9392-c480-3b08-aa6a-1154d8105350 | -7.7131 | -61.4705 | 2025-09-01 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 640a34e2-9dad-3ebf-90e5-e65f989e5f06 | -12.3287 | -45.7201 | 2025-09-01 14:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 36b385d7-60bd-361f-91a0-24bd510956fb | -13.3271 | -46.8426 | 2025-09-01 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 14d29070-432e-396b-922e-4c8e1240aa20 | -8.8662 | -45.7561 | 2025-09-01 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c94fae4c-50a2-3def-b826-434ad2dc0f34 | -6.8426 | -43.3385 | 2025-09-01 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 0df3af20-11b6-39d0-994f-753ce5efdb3c | -11.3513 | -43.5897 | 2025-09-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| fed8e448-c158-32f8-ab64-03640910d27e | -11.7993 | -46.4114 | 2025-09-01 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 84a82ead-b419-3d11-8c2a-a45f98f32272 | -6.7909 | -52.8165 | 2025-09-01 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 961eb974-e798-3bbd-9b38-58fc48daeff2 | -11.0849 | -44.611 | 2025-09-01 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| eb96a2ee-2ff9-358d-8b30-27412a48f9a9 | -6.9516 | -42.0042 | 2025-09-01 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 3528e3dc-3094-3295-b88e-614349981cf5 | -11.815 | -51.4572 | 2025-09-01 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 4bd1016f-a4c4-348f-999d-cf33f682b0df | -6.9314 | -45.5803 | 2025-09-01 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 35dc02a4-8b16-3fb9-a669-3b2ed92628bf | -6.8428 | -43.3151 | 2025-09-01 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 075f7a7b-b5d7-332d-8232-1c83bc1b8ef8 | -7.0948 | -44.3358 | 2025-09-01 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| dced2009-b29e-35d1-aba0-9bd1ebdf5a67 | -8.6673 | -62.8369 | 2025-09-01 14:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 102.3 |
| e34f7a2d-7ec7-3162-ba11-0ddbffedd1ab | -11.4683 | -46.7947 | 2025-09-01 14:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a78e7cea-ccf8-3186-82ea-850e357f140f | -8.9671 | -48.1896 | 2025-09-01 14:20:00 | GOES-19 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 06db9a6e-9902-3d66-bc06-53c2ed00a778 | -7.9348 | -46.4783 | 2025-09-01 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 162.7 |
| fb03bec4-5045-3c88-b788-0e8545dd0f53 | -7.3992 | -47.4333 | 2025-09-01 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3b57d6ed-e84a-3745-81a4-eeaa5c0fcd96 | -5.8696 | -42.9768 | 2025-09-01 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 068dded0-5cd7-3e84-a44b-5b77d5306de4 | -11.0841 | -44.6575 | 2025-09-01 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| f0fdabf0-b734-31fb-9ea5-45749936fe2e | -9.4003 | -48.19 | 2025-09-01 14:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 7e9bc903-9a17-3b4c-8e94-5fc7e8647500 | -7.9539 | -46.4542 | 2025-09-01 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| de1ac510-1f6c-34f6-a39d-a8353ed1a3df | -11.9685 | -51.3554 | 2025-09-01 14:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 5cdb9434-221f-37d3-af55-ae063f07ee4f | -7.9348 | -46.4783 | 2025-09-01 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 1a018b18-fa84-31aa-a7d7-e47942f04b28 | -11.0845 | -44.6343 | 2025-09-01 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| fbf35dae-b3b6-3480-a670-d80aeebf3ef3 | -9.6505 | -47.8128 | 2025-09-01 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 3473ce7e-3cf2-3bce-9fba-f2a5b1fbbd00 | -9.6127 | -47.8169 | 2025-09-01 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 29e16a17-afb0-393e-94cc-920f330b4f30 | -8.4506 | -47.3614 | 2025-09-01 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| de11dc63-8205-3172-92c2-e8008580d041 | -10.8935 | -45.8084 | 2025-09-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 68571d00-c7cd-3c7f-9b6e-91eaa0775295 | -13.5171 | -46.994 | 2025-09-01 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 9e94f699-bdf4-3a3e-8310-7c4693cb5b49 | -6.9314 | -45.5803 | 2025-09-01 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 152.8 |
| cb894d77-0804-3798-970d-044534114772 | -12.3287 | -45.7201 | 2025-09-01 14:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6596d45c-5e33-32f2-8609-0ff401b14374 | -8.6674 | -62.8179 | 2025-09-01 14:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 891def20-42bd-3e4f-b576-5d8719947454 | -7.9265 | -63.0158 | 2025-09-01 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 7ec18410-568e-33ef-adf6-3fec067029b7 | -7.1089 | -44.7703 | 2025-09-01 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 0776c606-31bc-3816-bbe4-37757110ad9f | -7.6946 | -61.4712 | 2025-09-01 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f727c355-64b1-3775-a0d1-b8bb48a1ecfb | -6.8237 | -43.3402 | 2025-09-01 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| f095ac0e-a67f-3276-a910-cbd30f3e6abf | -7.6784 | -61.0717 | 2025-09-01 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| db474bab-0810-3d95-92f6-11daffa9f848 | -6.8426 | -43.3385 | 2025-09-01 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| ed47e44b-7ef6-3d6d-a66b-ec1ce21bcddd | -6.704 | -42.2427 | 2025-09-01 14:30:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 0512a98d-c58c-36a4-b5ea-96fc941e01c8 | -12.5769 | -44.7814 | 2025-09-01 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 28e89b92-a83a-3c4f-af1c-b830319548ed | -6.9324 | -42.0299 | 2025-09-01 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 68aa27d9-92d9-3cd5-a794-75c3e2923d33 | -7.9539 | -46.4542 | 2025-09-01 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| dc005fa6-ee24-3f58-a230-d9f861eb5fa4 | -4.9122 | -43.2103 | 2025-09-01 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 8e6e6eeb-964b-37d5-b734-a42ac99dfc75 | -7.1111 | -44.5641 | 2025-09-01 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 99228b56-5cc6-3183-9199-0f9ea8b26f8b | -11.3709 | -43.5631 | 2025-09-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 5a656c2e-b5e3-32e0-8a3e-1bd18ffe369f | -11.3696 | -43.6341 | 2025-09-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 5c5e868c-2d6b-3993-ba95-383078508e11 | -12.392 | -46.4626 | 2025-09-01 14:30:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 78bffb99-c51f-3751-bf56-fbe22b4409d1 | -7.6252 | -44.0083 | 2025-09-01 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 224.0 |
| 39682da8-cf51-3c6f-b269-2310d21fab2a | -8.8437 | -47.5217 | 2025-09-01 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 29a49c53-ad20-3c75-8fc8-c34dbe537d67 | -6.7226 | -42.2648 | 2025-09-01 14:30:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |


[Clique aqui para ver as próximas entradas](README112.md)
