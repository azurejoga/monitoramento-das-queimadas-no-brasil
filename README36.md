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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 647f93b8-9a07-3ba5-bcb0-fb3b952091a8 | -9.16608 | -59.69286 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4cc9d0b-9175-383c-934d-efbd671fa3f7 | -10.47324 | -61.32802 | 2025-08-15 04:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f90d5d6a-8aca-36cc-abfc-0c7b974bf8a2 | -14.02246 | -52.0404 | 2025-08-15 04:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d3b7b89-5dd5-3dfc-8ef1-af5f8283ebd5 | -11.31332 | -55.2062 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 499296cb-2538-3b81-bae1-480e9896ff12 | -14.2813 | -53.02134 | 2025-08-15 04:29:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b8c0270-5e6b-3ab5-b43c-74cd13f00f28 | -13.11788 | -57.16985 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5ff8e84-2d95-3699-8ad7-14429fed878a | -11.35856 | -55.42863 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| db0e1e81-2a6b-3105-a09a-5fc157aec558 | -11.35284 | -55.40397 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5d81c7b7-ac42-31d7-b605-312d632cf324 | -9.93521 | -60.47811 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b04225b-ad7f-3658-a96a-e1ab03bf2bdd | -12.7536 | -44.41552 | 2025-08-15 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00fafc80-e01d-3de4-a1ef-cbc10c0ac4e6 | -10.35845 | -50.81686 | 2025-08-15 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0116454f-0c3f-3f31-a895-be1bda0eef25 | -12.58526 | -46.96201 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83792b9f-48a6-3d68-949c-31e2a515468f | -12.67362 | -44.95146 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 920af12c-66d1-3ed1-902c-129cbff9643c | -12.59063 | -46.96258 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f848554-c705-3285-ae8a-3b7099db47a3 | -13.56906 | -46.95351 | 2025-08-15 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c67779ff-0dcd-3af9-ac86-4cb023c62b5b | -9.16214 | -59.65588 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0e688fe-b121-3a97-b163-081be0865096 | -9.14278 | -59.42081 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72df1ac2-b9dd-39c8-bb44-bc19bab5a38b | -14.57094 | -52.04766 | 2025-08-15 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ac9d1d9-6a8c-3bf7-84ca-dd34e0181bc5 | -10.01049 | -58.42624 | 2025-08-15 04:29:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a700941-96ce-315b-a290-fd207b877a24 | -9.16529 | -59.67503 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b31ee56-45b9-30a8-a0f1-16b63d44f350 | -11.77958 | -47.39332 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3a8f021-28e4-316e-b140-000a61cba70c | -9.50447 | -60.53332 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a94f5890-211b-3b77-9431-f3dddb1bc571 | -11.02771 | -45.0724 | 2025-08-15 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ede2b5f-c1e5-3c82-aa0a-b8a096f2133a | -9.16511 | -59.66165 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2bea69de-b0a7-3ef2-bb97-03178df7dd30 | -16.37578 | -50.90517 | 2025-08-15 04:29:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 663ea712-cdf7-36d2-b390-327bf1078cc1 | -14.24168 | -44.58281 | 2025-08-15 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b1dc6e7f-d72a-37a8-9a28-33953856dc68 | -13.31541 | -45.23061 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c282105e-e40a-34ac-8296-6701b9be5c90 | -11.35363 | -55.42761 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| db05b09e-896b-3a92-ab3d-b3e4c1c8b8d9 | -11.28395 | -49.1185 | 2025-08-15 04:29:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4f1416a-149e-3f08-b7ad-5b7f45714018 | -13.56962 | -46.9499 | 2025-08-15 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2714a3f-fc04-3c83-b4d9-9c571a519610 | -13.11462 | -57.15813 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2aeabf3-f15e-3c8a-a2c6-59ed1bd29d1d | -13.13066 | -57.16154 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 995a3c7f-9060-33ed-be77-8681076f3a6d | -11.34584 | -55.41433 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b41e22ce-d38b-3534-944e-c9e37f7e4a01 | -11.92703 | -43.43884 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05f1aa47-ccd4-31b0-ba48-3e2ac6488f3a | -9.1507 | -59.67844 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1c52fcf5-2b8c-3a1c-98bd-23c5eeb60e89 | -12.75409 | -44.41376 | 2025-08-15 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcb9c475-5e27-3375-8318-bf815e9a41f0 | -15.89231 | -50.17412 | 2025-08-15 04:29:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 100fa87b-4757-3456-96a9-e5150f037f70 | -14.23924 | -44.57938 | 2025-08-15 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| acac76af-ba78-34ab-b83e-caa55272fb81 | -12.75348 | -44.41801 | 2025-08-15 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d15b1a7-ed10-3e4d-988a-21f99e9f9b0c | -10.35548 | -50.81172 | 2025-08-15 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50d53b9c-641a-3d72-9415-3c28b1ceca35 | -11.91049 | -43.44633 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de8bfb27-1484-3c0f-8618-d750e92c90ed | -15.93084 | -48.16035 | 2025-08-15 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dfd07cce-7e50-321c-9a56-38a3b8c061d7 | -9.50884 | -60.525 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 66c9c748-1750-388d-995a-be84cf5f0d22 | -11.40648 | -58.5495 | 2025-08-15 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a9b2967-2cd2-3a4d-a8ac-eb86e2553fcd | -12.51033 | -47.00443 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9814ce39-d12c-399c-a155-e8eca05e0c3c | -14.79246 | -42.72275 | 2025-08-15 04:29:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 57d98e55-3c53-3b3b-b747-f610b5db97dc | -13.47021 | -56.66479 | 2025-08-15 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c78d3ae2-c051-3a8d-95f6-6f4bde9a68a4 | -9.19014 | -59.65474 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 981cae8d-9a76-3736-871d-7800a0c35a09 | -15.5803 | -47.32259 | 2025-08-15 04:29:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f4f5e49-9d0f-3cd9-a3ed-d3778ad3ce7d | -9.38915 | -60.54149 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 715fc734-9f12-30d7-bc3a-3a163a9d181e | -12.12393 | -45.14125 | 2025-08-15 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16ca79a8-2c73-31e7-82fc-b509e55e0880 | -11.34118 | -55.41429 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d919f829-9732-357c-bf63-38230609055a | -16.38129 | -50.89376 | 2025-08-15 04:29:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96a2cb9e-1687-33ea-a7fd-77b74e26f4d8 | -15.32692 | -51.51294 | 2025-08-15 04:29:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4734ded4-c672-3df6-992c-d8c717d3c665 | -15.40398 | -46.59973 | 2025-08-15 04:29:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25f5fcc0-786d-3740-9c30-8b4551f8fb08 | -13.12285 | -46.85007 | 2025-08-15 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03cbb1ee-d750-345d-bc08-8c435ce5ec2f | -12.49147 | -47.01594 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24dc601a-f75a-31af-bbb3-6bb548e4d0c9 | -11.36245 | -55.43535 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c33fb100-19fb-35fe-b5a7-fc10b4470f7f | -15.89166 | -50.17799 | 2025-08-15 04:29:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1aa1d413-caa1-336e-9f5f-b8a8772b5fdc | -13.3277 | -45.22029 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8446522-c2dc-3b04-adcd-9e60ff33d45c | -9.15151 | -59.69625 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adb8146c-1576-366a-a4b6-78a421478ce3 | -11.3596 | -55.4229 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cae0cbf6-2a6a-37ff-a482-208b1e0c7be9 | -15.39447 | -55.78304 | 2025-08-15 04:29:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 37f95f45-888b-31c7-98cc-a87457b70455 | -13.31249 | -45.22609 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 04175439-56ad-3a6f-90f2-ec10818e038f | -14.06164 | -46.30141 | 2025-08-15 04:29:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10f5f074-96f5-392a-911f-cae9e9c49ec6 | -11.77626 | -47.39278 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a273604f-2950-3bbd-985e-1ce38f0bcffb | -9.50033 | -60.55357 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 235dd618-42e0-3ecc-bf9a-b2520d16a0eb | -13.32185 | -45.23567 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f14deb2-8404-396a-8785-81d20c0e4776 | -14.56991 | -52.0494 | 2025-08-15 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32c7e231-0777-3e9d-9f41-1a73a870663e | -13.63644 | -46.91679 | 2025-08-15 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d5244c7-50e5-3d57-b128-372a3f2ebc90 | -14.01405 | -52.04372 | 2025-08-15 04:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 606bc822-f183-3bc7-a660-f98aac3378b5 | -13.34013 | -43.3786 | 2025-08-15 04:29:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 70baa4b2-6be7-35b1-bc3c-0315e4def03a | -13.11808 | -57.14052 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3443793-5c5e-31fc-b350-09d01e39861f | -9.19801 | -59.65002 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46a12cef-e668-34bf-a2f4-e1636f49fb83 | -15.40114 | -46.59548 | 2025-08-15 04:29:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65929b39-e2bc-3093-8f00-e705da20917c | -9.91879 | -60.48784 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6c32177-095f-300e-9abd-12a6c7d77152 | -13.11253 | -57.16873 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b584b43b-4986-305b-9d81-64ed72cbe80f | -9.15061 | -59.66486 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f373bf4f-7bd0-389f-a788-b46725d2defb | -9.15728 | -59.66628 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c079d2e-cfe3-3412-9575-263f1d467d3b | -11.35468 | -55.42187 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 796d246b-95cb-3b22-a61b-bad3cfcb0f13 | -13.88662 | -45.55522 | 2025-08-15 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51080a0d-9360-32b2-a760-56a1f0bbd382 | -9.15612 | -59.67232 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60a1e39c-bb44-3219-8079-8157e35b7124 | -13.88213 | -45.55576 | 2025-08-15 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de76e805-1580-39fd-962a-cc2467e01922 | -15.8889 | -50.17346 | 2025-08-15 04:29:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| dcaea9e2-ad1a-34b2-b70d-f7d3a4345321 | -9.17079 | -59.68237 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5db09c7-0699-3be7-96a0-aca8d129c723 | -11.3182 | -55.20708 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ba8c0ba-51ac-3a72-9e7e-76af2059d3d8 | -11.31921 | -55.2017 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfecba44-5866-341b-8e60-515a65beeb79 | -9.17985 | -59.67167 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f56fa777-cfde-3c55-ac3b-bee499bc982b | -12.50978 | -47.00798 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74cf9eb9-a6e3-3ef3-a314-022e3e319729 | -9.16764 | -59.66315 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bdb465b2-e520-335e-ba2b-5e8dad1accc6 | -9.9216 | -60.4823 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e2cb6fd-abe2-3346-a6d5-0b25ec3a04e9 | -13.11392 | -57.16167 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 181ec1ad-c32d-366d-9c36-c6de83d150fd | -9.20686 | -59.64028 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9473765-16ab-3c2a-bddb-b77f350337b5 | -12.59007 | -46.96614 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 55b2f892-df8d-3a1e-a3f6-766f17483f1e | -9.15551 | -59.65433 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4f254af-1ef9-3ecd-b5bb-da05313581a7 | -9.9203 | -60.48878 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68b7e1ab-f7a1-34a7-b208-ebc44d16e4bf | -9.16623 | -59.6558 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 84e40d14-6f4d-3ce7-9d40-3aecdf39b847 | -15.17392 | -49.74062 | 2025-08-15 04:29:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcec2563-b1d2-3b65-8384-fe91c0564fb9 | -9.15858 | -59.67377 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1a23fdf-5340-3cca-853b-0ef89372c063 | -14.3769 | -53.37143 | 2025-08-15 04:29:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README37.md)
