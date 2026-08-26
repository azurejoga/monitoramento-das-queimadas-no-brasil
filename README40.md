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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c366c64f-2097-33a2-9979-d9ff7b8eb876 | -5.34541 | -45.16046 | 2026-08-26 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cb871304-737b-31a9-9bcb-ee8e5e6a3eef | -6.14284 | -59.92487 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e0a3462d-b251-39ac-aaba-b8c54dcdda4b | -5.95342 | -53.5848 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21b0c0a4-f763-3505-9ca0-b73b657448f1 | -7.00046 | -59.30584 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 19e2d05c-f558-3910-bdb4-a7ce125b6b8d | -6.26559 | -53.37291 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 534c4fe3-b4a2-3756-a7e2-98e46ae66f23 | -6.1503 | -57.93819 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1139ed9a-be26-303f-9ca4-12430f3a7dd7 | -8.51621 | -55.35181 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb73395c-700d-3a2b-836e-0f787518d1db | -6.14833 | -59.92074 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23b71df5-4888-32c8-9d0c-8edf4cd47610 | -8.62709 | -54.72382 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83d86f61-a848-3750-8f5c-3ea0c8978561 | -3.78352 | -59.28235 | 2026-08-26 04:51:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22aeb3f5-b819-3fcc-8a96-b732db895811 | -6.16183 | -53.68677 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02c675d1-7a39-3f7f-a6f3-971379476e9f | -6.12801 | -57.81987 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 131aa99f-19b9-3553-a859-8ed3f9ea7ecb | -6.64768 | -58.50749 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6a147b76-ba18-374b-9d09-4844ac560dfa | -8.15335 | -54.98658 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e483716b-e944-3a01-acd8-e1e80a96303f | -6.98642 | -59.25477 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb2d89f1-bbe9-3097-b2fd-9906ded8d505 | -9.03065 | -50.78186 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 37a935c6-0618-32b4-9a4c-9755ea5bdaed | -7.32131 | -42.98176 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0f563af2-22a0-35d1-938f-ade6e0dc9818 | -9.9016 | -46.48966 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 87692e23-0e87-3510-a888-3a0ede9a0cf2 | -9.4375 | -51.6811 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ba65c53b-1a1b-3cc8-b2c8-ecb702113efc | -4.94975 | -43.19923 | 2026-08-26 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1309d268-d3b2-3388-b780-1cd374400d7b | -7.75526 | -44.75577 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8da31f4e-0c22-315f-b131-e1cebb09e2dd | -8.86047 | -49.71817 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ba706f9-d93f-38c8-843d-be74459f74d4 | -5.7786 | -57.5538 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb4eca47-c054-301d-b93f-90e3fef9b343 | -9.03005 | -50.78586 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df73a9c8-a671-3e12-96a3-26d5e16a87ed | -6.3592 | -54.78758 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f4e74d6-b554-37bc-978b-91a69e5b7b9e | -7.47395 | -61.36752 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88e79aa6-f736-31fc-bb24-6c891fc40d53 | -6.50425 | -53.26132 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2bc6961-f0d4-33c4-93b3-f0c087319d4c | -7.38157 | -55.17604 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25cc4181-fc01-34c5-b806-7cb776bf6a9a | -8.5849 | -54.83626 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8bf8c6a0-ae57-3639-b7e8-af5eb18229ed | -8.30961 | -45.71516 | 2026-08-26 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10e81e23-66b4-3101-bef9-ba9aabb87c0b | -7.02663 | -59.23053 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f261f58c-3902-305f-967b-598e0ee25091 | -6.84325 | -52.50634 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79897d74-a443-368a-8079-c734b420a9ed | -6.26394 | -53.38337 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2fd14667-fa88-36de-bff7-1080766b8407 | -10.37501 | -45.06231 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| caf5e8e4-6421-3229-82c2-2321a15b5668 | -6.13148 | -57.82403 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9de14d14-f70f-30e2-a34d-8d56ed235d10 | -5.17501 | -44.61345 | 2026-08-26 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e5a11cb-a414-3a4a-af37-4b1c4a4c6051 | -8.08119 | -47.5043 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91f99d78-38af-3f86-b1ff-b3cad0c18008 | -3.10393 | -61.22681 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 420e42b4-b7fa-3778-975e-53db643dfdc4 | -8.55521 | -55.28458 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb9200d6-0704-3277-86ce-79c3a92a7852 | -6.10882 | -53.84872 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90f7722f-c1e3-3250-9148-9c9ff0bdaf9a | -7.51323 | -55.58677 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07a7b965-a42c-3f0b-8a59-4f27bc933966 | -12.72977 | -48.3768 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2403538-55cf-313a-ad5d-de1af54988f7 | -12.74611 | -46.45724 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e172e376-b3c8-3cae-9698-ff001fde4a10 | -11.74896 | -54.53504 | 2026-08-26 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ea0bd9f6-f7ae-3b4e-aa18-76568aba5eb0 | -14.80301 | -48.7977 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9fc8cc0a-6f5e-3210-974d-949d0e1b4a8a | -12.02734 | -46.01598 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 14f0114b-9294-3078-8c81-28b4b180e6f3 | -13.2322 | -51.52399 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e423c1ff-da76-3bdd-b1d9-2b8737212554 | -12.77015 | -44.26963 | 2026-08-26 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5658224d-0a5c-3760-b417-3ac4efed93c2 | -10.5104 | -50.781 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fae2ece-d18b-39bd-81c5-27898d287fbc | -9.09588 | -59.4112 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c06668c-8615-35cf-b25f-b1e235e8cc2a | -12.75385 | -46.47304 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26279404-3c12-37bf-afed-8db2be1aa40d | -13.35639 | -48.2344 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b408ffe8-47f6-3ec3-889d-a4ad71807e6f | -13.36698 | -48.22056 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8125987-9fde-371a-afac-1437cf61c5f4 | -12.76557 | -46.45597 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b3bc1922-d984-38aa-a882-ddf9a78e2c2b | -11.49408 | -45.11029 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24c1ec13-88e3-39d5-b0d0-5668f17f12e4 | -13.16511 | -51.33937 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b6fadb1-0bd1-3fdb-bae5-fdec7182f29b | -11.68978 | -54.58715 | 2026-08-26 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bc739c6-9532-36a4-9f7b-1db4d29e2154 | -10.7614 | -54.02502 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5f63fb20-4d23-3305-aef2-aee0ea84f6e4 | -11.1622 | -54.00711 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fa46098-1289-3e29-a173-c8e13c773f95 | -11.01385 | -45.06804 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| df15b4f2-1334-3164-b450-1caaa0edc07b | -10.7859 | -50.92276 | 2026-08-26 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06d5ad91-5b75-3f98-9524-7d72c44e906b | -10.76968 | -54.03711 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 505e5a0f-4ad5-39c8-81ce-f2e3b8fea99e | -13.37129 | -48.22113 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06b19176-2d28-3b98-b675-a40e0a84793b | -11.42542 | -44.53934 | 2026-08-26 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a4dec37-7e2e-3ce4-adef-6efc6f258e8e | -13.24115 | -51.38719 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 749d1000-9eb7-343c-9366-c15791df5fbb | -8.67529 | -62.94939 | 2026-08-26 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e498a067-f23e-3ec1-bee9-a3f379a01b60 | -13.37183 | -48.21705 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2557ffde-291a-32ac-b8aa-543c46db6443 | -10.76416 | -54.02905 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 76667b94-ae95-3330-b727-18b8e4946264 | -10.99431 | -51.15358 | 2026-08-26 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75a42c8a-f9b2-3bf8-9126-180db7c53623 | -13.28756 | -51.46414 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2040ab65-8449-313e-9230-c4b0ac556b64 | -15.60097 | -53.12506 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9a7de7e8-bba6-3a65-a866-007d575b18e2 | -10.76361 | -54.03256 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fb567542-0432-3b5c-af7e-735fe3bc65ce | -9.60489 | -55.11357 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| a8110954-7ffb-3374-b305-3ad8708c7913 | -13.22572 | -51.36798 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 954de664-f26a-397d-97b2-7eebf8f86b7f | -13.29582 | -51.45702 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e38eab68-3305-3e35-ae91-ac92ddeeaa9b | -11.79965 | -47.24371 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d065d6a-19ce-3a54-8d94-78bbb025e25a | -10.75864 | -54.02099 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b1453c39-b0d2-3de5-b32e-1ae34c21227d | -11.42417 | -44.54968 | 2026-08-26 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 282e6770-3694-3813-9459-94db274dc847 | -12.72498 | -48.38041 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 696a1a27-e6ee-3b31-a3c5-21d72afc98ff | -10.74926 | -54.01591 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ba38465-f12b-3443-aa4e-d76092a14f60 | -13.1758 | -51.34099 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6f056838-3b7c-3fa1-95fe-558ae46a15aa | -11.16661 | -54.00063 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ce4310f-5726-39a3-85c3-682396268c8c | -13.19069 | -51.35843 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04203ecc-33b1-3676-b101-45c3fc9ceecf | -9.13054 | -57.56285 | 2026-08-26 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa749d66-ea35-3396-8da4-5f378d72e477 | -9.47224 | -56.9048 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c15f343-a220-3d1c-9691-ab25bb5a7e4c | -9.46378 | -60.53681 | 2026-08-26 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6ae0ed7-584c-3d9d-88e9-d5550e51d78b | -11.49609 | -45.09419 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aeafd0fc-1a78-3696-927d-00e56c230c57 | -9.13817 | -57.5641 | 2026-08-26 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea3a48ed-6846-308e-90e4-6f13c22ce30b | -12.21841 | -54.23219 | 2026-08-26 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e6d322c-ed9d-3b7c-9a09-02eed45ef7ea | -12.72078 | -48.3797 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfbb9351-4649-3be7-a6c5-28bab152bdf8 | -13.19006 | -51.34315 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 34d8f1a5-b2f3-3ca9-9959-6b6d26780e4b | -11.289 | -47.06974 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 976ae38d-d8e0-3fb1-b46e-6523e67bb52c | -10.76306 | -54.03606 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| eea7d091-7946-3827-936c-7e4abe5a3682 | -14.32244 | -51.73156 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c6612c6-8e0d-3ff7-a4d0-a02a361450f5 | -12.76015 | -46.46023 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d65aa87-2986-3069-9c78-13030f387a26 | -15.36382 | -53.79893 | 2026-08-26 04:53:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9512d2af-20a3-3bbd-88c6-a7a321a4ba0b | -13.25775 | -51.39814 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea06cfcf-0215-31c3-8f6b-9654fa7814f0 | -9.67572 | -55.08358 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77d8c94b-e11a-3b3c-8412-079912f2680b | -11.27339 | -47.07037 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc264c51-ca82-33a7-aef4-5d4bb3262700 | -13.18531 | -51.34494 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README41.md)
