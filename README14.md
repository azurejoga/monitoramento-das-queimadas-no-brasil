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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01f4a340-7b7e-3c8e-a2b1-8be97bf54964 | -12.1351 | -46.983299 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| babfaa68-6010-3350-8387-2e5a636f9554 | -6.5908 | -44.154701 | 2026-09-19 00:41:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71b3c0f0-4397-3cbd-bf0d-967cb1a96b42 | 1.2575 | -50.967999 | 2026-09-19 00:41:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bd57a8b8-fd49-3e77-b447-aa63a47854bd | -11.4348 | -51.458199 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be4684d9-f316-35ae-8a52-934367aed4d0 | -2.8246 | -50.462799 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d89715be-9227-32a6-84f9-4b00fa76c944 | -11.3243 | -47.6763 | 2026-09-19 00:41:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab7dcbb0-5c74-32c4-bbca-76720be33c01 | -14.6639 | -46.6698 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d225e847-0d51-341d-b139-1654a44cf4d5 | -7.633 | -46.1012 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a643f451-1f53-3710-bea7-868cb3da7956 | -9.5692 | -46.561199 | 2026-09-19 00:41:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba848b5c-a00a-34de-9e6e-ebd911b8b4f5 | -13.7392 | -48.7911 | 2026-09-19 00:41:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e56a53b-3bce-3174-b8fd-2d2d918caec8 | -9.8013 | -46.098 | 2026-09-19 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec8f5cca-ebd6-3d21-9493-1e8b1c2fdacb | -12.5927 | -49.0966 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57c0cac9-f6c7-3301-bba0-21b349fe592c | -12.8455 | -44.381802 | 2026-09-19 00:41:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 001d0cee-1e16-37d8-9e9d-865b344bf00e | -4.2755 | -46.526699 | 2026-09-19 00:41:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bd417b1d-df5c-3401-9f8f-4b59219c66f2 | -13.6087 | -48.296299 | 2026-09-19 00:41:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4b112042-949b-3dd9-8fcf-53c852626b0d | -9.0291 | -48.7351 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3858286f-0ce8-319d-81fa-8e5cbbfb9e10 | -5.8876 | -53.535099 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e07fc50-0112-3c8a-abf0-4be53a4b620c | -13.0081 | -46.964699 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8be3d59e-a3e3-3255-9e20-fbfda8d7083e | -9.7443 | -45.073601 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b6d564d-31df-3ae8-8110-68835b903263 | -6.6621 | -50.93 | 2026-09-19 00:41:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c5a7fa3-8821-3bba-8476-731717cdfec2 | -15.9907 | -46.743099 | 2026-09-19 00:41:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| df7f501d-ef08-372f-b6dd-32f2b2cb58bd | -11.4007 | -47.289501 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1645dcea-ab83-3325-8ebe-cdc5b8aaf2a3 | -6.6556 | -50.901001 | 2026-09-19 00:41:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59b01c37-40c3-33b0-9f3f-67ed6c0a2fd7 | -14.1352 | -45.194199 | 2026-09-19 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6946ea6f-fd69-33a2-a0e5-66ab537a30bb | -14.102 | -44.835499 | 2026-09-19 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05d74f91-89ae-3d00-a93c-f098db905ef6 | -9.0339 | -48.755798 | 2026-09-19 00:41:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bc3f02ed-9a1a-34ce-bb78-ec353c6a346f | -11.3033 | -46.7794 | 2026-09-19 00:41:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42623c3a-7ac5-3ed0-9d33-cd3235481f28 | -5.3326 | -48.9879 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ec08fb0-77cc-3ab0-8539-0c466e2aafda | -10.9972 | -48.322102 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4e424da-288b-3103-a3a9-bed28859eb43 | -14.6803 | -46.650902 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b52050de-8d71-3c8d-a518-84ed4290207d | -0.5194 | -49.141602 | 2026-09-19 00:41:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 029d96ec-6a03-3346-b7f9-0b87ce175c27 | -16.7978 | -46.985401 | 2026-09-19 00:41:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 12d8e176-c20c-3af7-bb1c-3e087dba55ea | -6.9484 | -46.966499 | 2026-09-19 00:41:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45a7f6e2-5592-3014-bc4d-6e7c0ce2502c | -1.5926 | -54.4478 | 2026-09-19 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0456cf59-62ae-30e7-a4af-f60b5970daf1 | -6.9932 | -42.164299 | 2026-09-19 00:41:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95d9285d-7dfd-305a-8c30-57d3d4355f6c | -11.3017 | -46.772099 | 2026-09-19 00:41:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 166d53c4-f83a-3b74-a9a2-59d9c1ba6c95 | -12.9918 | -46.983398 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc9ca069-3736-3aa9-b8cb-2c376c676854 | -14.1807 | -47.8601 | 2026-09-19 00:41:00 | METOP-C | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aba6c8ac-dfe1-3d0b-aca7-032eb6d1bc35 | -14.6851 | -46.672199 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a4f23174-20c9-3705-8232-ff6d09d6fe57 | -8.7801 | -48.683102 | 2026-09-19 00:41:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 69686070-6dc3-3a9b-ac11-9b3a3b0b92b2 | -9.1981 | -45.774799 | 2026-09-19 00:41:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 76c3cb50-6a4c-3feb-b20e-9578d353d19e | -8.777 | -48.6693 | 2026-09-19 00:41:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| da9b536c-7093-37a6-8081-6b01187abecd | -9.7423 | -45.065102 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f5ec5dac-b747-3d96-9684-b2e411d4cef5 | -6.6718 | -43.635502 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10aa1438-c740-3f89-91fe-1d77d3ad28fe | -10.7015 | -50.2649 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6157ad03-a713-3044-be6f-77a2df4ca351 | -8.8649 | -45.938301 | 2026-09-19 00:41:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bb907f95-6a95-3f01-8568-045830d442ad | -12.1433 | -46.9739 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a65f1247-ca73-3030-a3d7-83a81955f3de | -8.7679 | -44.2351 | 2026-09-19 00:41:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eea670e8-bf2d-38e6-933e-71017c97b139 | -11.0545 | -49.769001 | 2026-09-19 00:41:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57e26890-df9b-379a-b927-458bfa6cc9bb | -11.9368 | -50.132401 | 2026-09-19 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1116a2cb-4b58-37a7-a582-fb0103919c5c | -12.3237 | -47.3997 | 2026-09-19 00:41:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3919746b-e166-344d-9e98-e448299d30ff | -12.3414 | -48.2038 | 2026-09-19 00:41:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b556ba2a-3581-3beb-afa6-f6fb67a99b7c | -14.1505 | -45.215 | 2026-09-19 00:41:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1fad9a6c-5155-340a-9342-cfd75259c78e | -5.8616 | -52.037601 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72985a78-c1c4-3018-b792-04396d7f4573 | -8.7786 | -48.676201 | 2026-09-19 00:41:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6eea38e9-c553-3f28-8432-a77ed12acb4a | -10.3973 | -48.313801 | 2026-09-19 00:41:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2de6edd5-28a4-3b55-bef1-bb80bb21ab46 | -10.9246 | -53.968601 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb5c50cb-567b-3909-ba4f-f2cad3ad3464 | -5.8897 | -53.544498 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2840d8b3-f875-379e-9a44-abfb04a4bacd | -4.593 | -42.963001 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc0d5ac9-6f81-3abb-a02f-28459b306908 | -10.1272 | -45.5536 | 2026-09-19 00:41:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c940682d-6e90-3b82-bfe9-4fb0e222679a | -11.1145 | -49.437698 | 2026-09-19 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d4e3395-6d40-387d-8947-8648bbeb4b22 | -10.1674 | -48.5266 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6a65a81-d50f-3f30-b7b6-13466611e9d4 | -11.2477 | -54.099499 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29ebcf46-d760-3161-89fd-87e72bdae06f | -7.1924 | -48.238201 | 2026-09-19 00:41:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cda707d2-3298-3daa-a05d-02f2c88971f7 | -12.1172 | -46.994999 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d481eba-0575-3b40-8472-ff14c320262c | -6.6507 | -50.924999 | 2026-09-19 00:41:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61fda7dd-2ba4-3e26-9b1f-78bc26822c6e | -5.8489 | -52.0732 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84571fae-cf25-37ed-be97-93b215658e97 | -9.9529 | -46.612202 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5e8068f-1a8f-3446-9b1b-57808b7eb99e | -11.0447 | -48.304001 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92f603cd-710e-3746-ab15-44b2c645e373 | -3.4564 | -50.609501 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27b32a32-56c4-37fb-9b37-6334475b5776 | -11.1398 | -54.022099 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e78c09b4-c554-3dcb-be63-212d690a1366 | -1.4106 | -49.428398 | 2026-09-19 00:41:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd21243-d72c-387f-9609-a18a930716fd | -8.6661 | -45.4482 | 2026-09-19 00:41:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79b561dd-cffb-3323-a864-2f6643933d9f | -9.0046 | -44.9184 | 2026-09-19 00:41:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 13ab30bd-caa7-3b18-8a73-482ba478f913 | -10.1728 | -48.459801 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6330b8b9-8abe-3924-ad64-be4b37a208ca | -11.557 | -46.893799 | 2026-09-19 00:41:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b4058fc-c163-32df-8fc4-9d45e9ad9724 | -3.445 | -50.604698 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94887223-b1e7-3c08-af90-0f8cbf29fda2 | -12.1433 | -47.018799 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bfc71cc-ad89-33b9-8241-5b178a027df0 | -5.2525 | -49.402 | 2026-09-19 00:41:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 710b26f6-a7f3-3329-bc4c-ee29fa606cc9 | -12.9804 | -46.978699 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98d2fcc0-522b-3ea3-8222-eba2e1d3fdd4 | -8.3732 | -45.650501 | 2026-09-19 00:41:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc0f4fc7-6b7d-3427-90a8-7fbb1ccfbbe6 | -10.1756 | -48.517399 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82cd74a5-e6e0-3eb2-9cb7-488f1b541b4c | -11.1187 | -45.290001 | 2026-09-19 00:41:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9f5466-d09b-3d10-9e7a-2568993caa70 | -11.0725 | -48.290199 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d820b0a4-7783-307b-b4d7-d4621ab00361 | -7.7778 | -44.8853 | 2026-09-19 00:41:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d3c00ca5-49dc-329e-abd7-5489cf282b8f | -10.4005 | -48.327702 | 2026-09-19 00:41:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 847f9bbd-792a-365d-b471-dc9f5f2bcebb | -2.0246 | -48.780998 | 2026-09-19 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c6bad99-4109-3813-8322-3953ba8ef925 | -9.7834 | -45.064201 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1baa4b-7c3b-3b74-9ff1-5905e5290c18 | -5.9103 | -52.1175 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f091b36-0e3d-3441-bc7a-a07215549a8a | -10.2381 | -48.8382 | 2026-09-19 00:41:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 155f4915-dbdf-3ce6-ae5b-173cacd3796e | -3.7259 | -54.656601 | 2026-09-19 00:41:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 869bc2f5-3534-33cd-8dbb-19b9059618e5 | -7.6526 | -46.0966 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6843971-f6a6-3b85-9166-7f49c5d36620 | -8.4769 | -57.5984 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53671250-77fa-3fcd-91ad-0d2d4669d8ff | -7.6056 | -45.4189 | 2026-09-19 00:41:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8016da0a-a41e-3b98-ae76-1ed5d605535b | -10.7955 | -50.8787 | 2026-09-19 00:41:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e8f3de6-65bb-3796-8cf9-54c4cd65be78 | -14.1377 | -45.160702 | 2026-09-19 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ee71f69-01b5-3262-8461-f22999ba9aee | -5.3228 | -48.990101 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dbd7ce9-2c2e-3c59-ace0-104f30876a8b | -10.6067 | -50.2547 | 2026-09-19 00:41:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23dd1612-1a99-32c7-bc64-254e84bcb2e9 | -4.2587 | -48.537201 | 2026-09-19 00:41:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45ba7fef-680c-32ec-9b59-b942ff12f4f4 | -7.1867 | -50.836498 | 2026-09-19 00:41:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
