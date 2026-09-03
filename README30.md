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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c17ec0b1-1a48-3744-ae39-925d942745f7 | -11.32318 | -50.53246 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 12f4625b-05a9-3631-aa6d-66afd58985ef | -10.87413 | -45.30988 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6db8f859-1d28-3c27-82d3-916273101a68 | -8.46341 | -54.68093 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d6d52a7e-eeb8-34e2-a92c-e1258bd37f02 | -8.45667 | -54.67913 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b7b7f14-32e6-3a77-a605-ccc307857cde | -13.37528 | -51.34689 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db95b29d-6462-379d-b7fe-a61b9cd308d6 | -16.07545 | -46.07406 | 2026-09-03 04:40:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0c2cd7f-6539-3a2e-acaa-eca922ec83c2 | -11.51631 | -46.90409 | 2026-09-03 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1131c901-d187-3f34-bc46-495652ca7c4f | -8.44994 | -54.74591 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8584985-c7e1-36f6-b836-e9d13eb9d9bd | -16.76583 | -49.62797 | 2026-09-03 04:40:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76ed6cd8-2c0f-3061-9a4a-6989a0def4db | -16.93847 | -49.3807 | 2026-09-03 04:40:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 882e3e1c-bbed-3257-a6f2-9b81f09283c7 | -8.47314 | -54.65533 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74bd4229-9a41-35c4-aea7-71ef93f64299 | -13.39416 | -43.00475 | 2026-09-03 04:40:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eb422424-d1b1-3e90-8f99-680d00700767 | -14.96191 | -48.08883 | 2026-09-03 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9442b57e-902a-32a0-a93c-a4a5398b2fc3 | -10.18635 | -50.26922 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d6e6d999-9c73-30cc-aace-5b2dd5e94343 | -13.57781 | -47.8801 | 2026-09-03 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02331808-5a2f-3f34-b857-1b145c2717dc | -10.89655 | -45.32503 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 718dcea9-f525-3060-a154-655259dd38b4 | -8.46435 | -54.66405 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e588024-a0ac-32ef-96ba-ce8c9c73cf66 | -10.31954 | -49.94584 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdfc6bd5-7532-3bb6-8a68-491ce43c74ac | -10.9988 | -45.08356 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dee8b2db-02e5-37cf-8bac-3c0f12d97ada | -11.31443 | -45.11791 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8c03ade-4b71-3008-84e8-0c18f1848d6b | -10.18358 | -50.28588 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bf6fcc1-0f21-3860-88f6-e3d680ff0944 | -11.31382 | -45.12193 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b8c016c-cb35-3b81-afae-c8c31e78b44e | -11.28647 | -45.16132 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edea0be9-9979-3e96-8446-777671153220 | -8.46059 | -54.68541 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 008ceded-3493-3428-978c-d600fc90d092 | -10.99762 | -45.09136 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 29e418c2-b1b8-3a3e-93ba-b71a71145d45 | -13.38838 | -51.3807 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b20c77f4-6000-3946-87bc-d4cb69a1d2f9 | -12.07276 | -47.06501 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 062fb6f2-2113-3770-afd1-b34552b62b6d | -10.98776 | -45.08582 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 78e8591e-901e-3f68-956c-a036ac41ac42 | -10.54612 | -49.97449 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a42759f9-1930-3c94-8955-78cac3c39ee0 | -8.46143 | -54.66433 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a44cb3ea-e9f5-3be5-8249-6380c88124e2 | -10.56665 | -47.72837 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d64778c2-5580-36a2-8d88-cab2caf52c07 | -12.40402 | -44.80579 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62d9bd2b-602e-3e28-afe9-928423a6d789 | -11.30372 | -50.5162 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 075dcb40-d242-31c2-9cc4-7d509ab5a2b4 | -12.07943 | -47.06608 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eec40fa-d334-3d59-b3d1-7683e9e9d6c7 | -10.18137 | -50.27693 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e9f60882-7956-34d1-870b-8b4386ad72e8 | -10.87297 | -45.3175 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba809832-1cbc-3791-998a-0cde961083ec | -15.33649 | -47.0454 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e2bd6b4-81e6-379a-a38c-7494d1802449 | -10.15108 | -50.25886 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d4d5579-2d46-3821-8f88-fd9399b47266 | -11.39522 | -43.92396 | 2026-09-03 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f0089c9-8837-32d6-bf52-b41e6ffb7ad5 | -16.32902 | -49.45896 | 2026-09-03 04:40:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53bca4b7-2618-3106-b77f-a33956668e28 | -11.2386 | -45.16274 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b366644a-3927-3cc0-9922-03f909703d7e | -8.46922 | -54.66493 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 024640ab-369a-3cc6-9200-53de9a666afe | -9.60635 | -48.56507 | 2026-09-03 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cf28e29-0166-34ab-8940-bf6369d8eb60 | -11.29872 | -50.52391 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ab94bab1-239b-3326-abf7-d9005ed2da60 | -14.20983 | -42.0423 | 2026-09-03 04:40:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| acc91194-495c-306d-9ff2-8e9bf7614deb | -14.95526 | -48.08773 | 2026-09-03 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 761516d0-b7b5-3598-8cb5-fdc4548a51df | -16.40499 | -48.9035 | 2026-09-03 04:40:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 197c35aa-262d-3083-ad76-0bf36e086053 | -9.62 | -54.31009 | 2026-09-03 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acc51501-f5e5-3ed8-a41a-82823a23fcfe | -12.08999 | -47.06415 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5718d478-f6de-3740-bea8-65998d72d7cc | -10.75626 | -48.97483 | 2026-09-03 04:40:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aa14c7a6-59cf-3a60-b3a4-226ed3f3cdca | -9.62699 | -54.30908 | 2026-09-03 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b915bed-7260-352a-a325-ab23e092acb1 | -10.8975 | -45.33212 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74a31684-710c-3715-913a-cc4fa9e252a9 | -11.3145 | -50.51808 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 487535fd-8a1f-30ae-b691-5e7d430b60c0 | -12.09277 | -47.06824 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 441a4c3d-c2d3-3402-b0b7-f5f2592c3b53 | -12.41178 | -44.80278 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d31d8fa1-f3a8-37a7-a952-71eb3e9d7558 | -9.70486 | -57.88807 | 2026-09-03 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| adaad044-9209-3ccc-b205-1b14fe1ab94f | -8.4623 | -54.6472 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 783aaa95-73db-36b7-b323-f1e817775536 | -12.11318 | -47.27817 | 2026-09-03 04:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3612180b-f185-3e4c-8e54-c3a4241701f2 | -13.3884 | -51.35826 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| decea118-730c-389d-833b-89a551baa0c4 | -10.18497 | -50.27754 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc7be0b3-2675-3e0a-bbe1-3472628ace1a | -11.29581 | -45.14667 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4433965-5c02-3074-9452-94faebfc9aa4 | -11.31321 | -45.12593 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acb7c09a-fc49-32e6-8897-bc4801dd5bd5 | -13.5839 | -47.88472 | 2026-09-03 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cf2d0e2-4817-3305-8975-8b9134beca06 | -15.33423 | -47.03751 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8b99a22-6f18-3621-9ccc-a03ba1f50969 | -8.4653 | -54.65868 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 452276f7-e5c0-301b-bea5-f40314013e4c | -10.27709 | -50.04658 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95bb6e93-5c42-354e-aea2-f03f15a6cd99 | -11.32748 | -50.52892 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 8d77b5e3-e87d-3eff-abc2-c78608a6ce94 | -12.41117 | -44.80692 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f214b546-a4ed-300b-a3b1-c4c505541e2c | -11.30394 | -45.1401 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16f67617-0886-3dba-adc8-074272a5a365 | -16.32961 | -49.45531 | 2026-09-03 04:40:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| ff6d0352-714e-3845-85aa-6a143cd2d379 | -12.40342 | -44.80991 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4eb61912-cb04-311e-b2e1-f30525fe6727 | -12.0961 | -47.06879 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 487d5970-c00d-3a53-8d22-a27b02a049ff | -11.32678 | -50.53309 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 0baa5d2d-d1df-3ff4-839e-c6f4a38a689b | -10.99821 | -45.08746 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a4eefc8b-5e36-3cce-be56-c8d87e07c1cb | -10.56389 | -47.72432 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64a10a0c-fe5c-343d-ac89-a45f27d10ca1 | -11.30799 | -45.13692 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4674ab3-98c4-367f-b7db-1164ce32945e | -11.28121 | -45.17265 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 92d7b628-9a1f-3014-aa26-24ec6ef55a98 | -13.38292 | -51.3826 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e3cdce8-c7db-37b5-a5b3-c1673b301487 | -10.99007 | -45.09415 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e33adaf7-82d2-3eb3-b0f9-0dc235fddd6c | -10.18206 | -50.27276 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5863bd0a-71c7-3f24-9ad8-14c65d6c9570 | -10.56169 | -47.71675 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 879c20ca-b1de-360f-9392-0819105cc5a5 | -11.28817 | -45.17377 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cf57d81-dc1e-3c4f-a2d4-76b9512a3ade | -10.8845 | -45.31145 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a12a706e-43d3-3171-a548-11d08f947dc9 | -10.92741 | -45.34455 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 169ddbd4-1662-37d6-b4b3-824d13b5f9b7 | -11.28179 | -45.16876 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cde3fc5a-80f4-3d0b-ade6-093861fcf3cc | -16.5392 | -49.5622 | 2026-09-03 04:40:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80158d6f-d96d-3ca7-8faa-68d32b5fef20 | -10.31533 | -49.94925 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a351fe69-b957-3446-820c-6ea0ebb01c4f | -11.29115 | -45.15393 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84bc5ee5-52e2-3d0d-88ad-af6e2c1e57f0 | -18.78415 | -48.91558 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1af800b5-e20b-3519-bae1-040705ab8460 | -17.08854 | -56.84701 | 2026-09-03 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f608c6d4-1128-3518-a78a-89b6a33d6324 | -18.65175 | -47.28617 | 2026-09-03 04:42:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f8065b9-e051-366a-ad8b-b9076152588f | -18.76552 | -48.91296 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5074049f-b62b-3031-b58f-b297386bf20a | -19.0898 | -57.37011 | 2026-09-03 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fc019763-588a-39de-b88d-46c56c6cea40 | -18.77551 | -48.91469 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b54ce67-bd30-3650-8998-1c15a72677e8 | -18.13777 | -51.81322 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 92ce38f5-2839-368e-858b-d1ba3f9fda1e | -18.64831 | -47.28564 | 2026-09-03 04:42:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16c77ae9-4718-3429-b305-b27b072a177c | -17.08483 | -56.84052 | 2026-09-03 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 49b61bf6-0292-382a-9dc7-bc66ea0a25f3 | -20.1464 | -54.69073 | 2026-09-03 04:42:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1dd9f22-e3c5-3e95-82f2-7af30b892482 | -17.08374 | -56.84597 | 2026-09-03 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5c3ad230-7b92-35fb-bc31-a188971cbf91 | -18.83092 | -47.60274 | 2026-09-03 04:42:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README31.md)
