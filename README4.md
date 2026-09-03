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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39dcd7b4-0718-3ced-8e7c-99297d9c978b | -6.63311 | -52.95342 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 40149502-049d-3386-8554-97d2a14c871b | -2.48093 | -49.4088 | 2026-09-03 00:07:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fc89f9f8-4821-3483-ad19-5973c967e2cb | -6.64398 | -52.96247 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ccf16e36-08f2-3815-9a9a-e3f7274eb6f6 | -7.40642 | -49.74264 | 2026-09-03 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| dac97ecc-3cfb-34d6-a431-c3752974e4b5 | -8.1695 | -45.80405 | 2026-09-03 00:07:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 85453392-19d9-3a62-a0d7-2f2f81a95565 | -2.44277 | -50.26224 | 2026-09-03 00:07:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 91c47ee8-024e-3260-8035-62d72e6d5b6e | -6.41693 | -58.31457 | 2026-09-03 00:07:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 716d7467-0e0a-3b63-90c2-bcd35f54b65c | -8.07119 | -49.623 | 2026-09-03 00:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0553f2c2-8479-3c2a-b7b1-427d669b2410 | -3.38086 | -52.79625 | 2026-09-03 00:07:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e5fa21e1-470c-3557-94e8-5c2be560c33c | -5.41866 | -44.79985 | 2026-09-03 00:07:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| c896d22e-17f1-3a49-ab16-633038267665 | -5.75801 | -53.39638 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b7566ca6-a340-3d11-9b50-6a5fa5c84764 | -5.75946 | -53.40704 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 31dddb52-3740-3e29-8131-23982ff18f89 | -7.82972 | -47.66883 | 2026-09-03 00:07:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 443b3308-1295-3a3f-a06f-38c7b7c75611 | -6.07222 | -53.66432 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 23e5470b-3653-31e0-9943-500ed8e8f409 | -5.92585 | -52.1982 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 230f40b1-95d2-3263-9e87-677545a36ba5 | -2.45169 | -50.26099 | 2026-09-03 00:07:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e5b45430-4d49-343c-a7c1-5860961f8809 | -5.23742 | -49.6037 | 2026-09-03 00:07:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 708b7655-b2bb-37dd-9f56-3203652bab4b | -6.76205 | -44.55943 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9855c87d-aabb-34e4-8ce2-61e005a1422f | -4.11525 | -51.02255 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8418b655-f60a-32ba-ae00-b74574671d0d | -8.45613 | -54.65073 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a29a809e-7777-3ae1-afcd-745c498ba86c | -6.62982 | -55.25277 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| af4ac9e9-cda2-33f4-a947-a82b8de13d29 | -5.3058 | -49.16687 | 2026-09-03 00:07:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5ca79f5f-3162-3c83-8f07-157ad8a3efd3 | -7.40765 | -49.75152 | 2026-09-03 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 033dfa90-28de-347f-898d-423dbada2941 | -8.43026 | -54.71233 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4cf48758-7924-362e-b934-0abd6a33a1ed | -7.82589 | -47.67572 | 2026-09-03 00:07:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 849dfcd4-4ef8-310e-aba4-24c327a9ef3d | -7.56122 | -48.35985 | 2026-09-03 00:07:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 369509ec-9791-3a0a-9c83-9d374376066d | -6.65282 | -46.14001 | 2026-09-03 00:07:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 135be047-aa9c-3376-88ce-8009c998cc92 | -3.80338 | -49.10963 | 2026-09-03 00:07:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 5618f9e3-6e76-37ed-9712-943735238618 | -5.50988 | -47.43937 | 2026-09-03 00:07:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ababf11e-ae96-3916-9ba4-c2fd6c0d5df1 | -8.07988 | -50.9626 | 2026-09-03 00:07:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 19819519-567f-3768-b704-637709c21dc9 | -6.76473 | -44.57703 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| b178cb57-360d-3a92-9e6d-8972b003b3c5 | -5.47154 | -60.07241 | 2026-09-03 00:07:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 52f4ff45-53f8-3bd7-9407-af7fa77d70b9 | -8.13731 | -54.93751 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 793fd3c2-8236-3953-b485-5242f2ff59fb | -4.09132 | -51.04374 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a451c99b-48f8-3ffc-a18c-0fe34ac0c0cc | -6.62785 | -55.23788 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 167ed378-4137-344e-b449-2f37f010e249 | -6.68009 | -43.42502 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 8f2c39c8-66b7-38c2-a521-740d41efc9f2 | -4.10768 | -51.03253 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 63481f2b-1393-3263-a633-388ed1bff9a6 | -6.63447 | -52.96377 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 0da93c10-1088-3c4d-bfae-a8b17e2d7346 | -6.49274 | -53.60606 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 658d4b1b-2f6a-3282-a4fb-33eeff5f530c | -6.4354 | -48.54412 | 2026-09-03 00:07:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b27d112d-cfa4-371b-a640-62b075305c48 | -3.62487 | -54.03031 | 2026-09-03 00:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f8e143b5-494b-30b9-8666-53ab648a00c1 | -6.6259 | -55.22305 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 947b6ada-ab06-3659-99ed-ea0e273f40ee | -6.83529 | -58.96641 | 2026-09-03 00:07:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| decc4967-de35-3e72-b938-06e326781dbb | -6.3736 | -58.28857 | 2026-09-03 00:07:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| aee7f5ef-be52-3eb9-bf92-f2219166a0ff | -6.65213 | -52.95087 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 29e77f25-59b2-3d87-a01f-a5838064b260 | -4.10648 | -51.02378 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b461e687-4454-36a5-b425-bd8e941ef8e9 | -6.04854 | -53.80069 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| eb6d17ac-a9a5-33b9-8d5c-2e5329e1dc6b | -6.14832 | -57.76635 | 2026-09-03 00:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| b04d7ebb-2c3f-347e-8782-1afe55a8c03c | -8.44496 | -54.7398 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 392ce67e-a312-3394-b7f0-10e1fa37b8a5 | -8.08998 | -50.97034 | 2026-09-03 00:07:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 23622cf9-e4fc-3d9c-b01f-0233e6ba717f | -3.81466 | -50.11487 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 89373699-861a-386e-b527-d994863aae04 | -8.44678 | -54.75423 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a393e47e-09fe-36c1-b249-9b5723f3a619 | -1.47357 | -54.82613 | 2026-09-03 00:09:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7675eed8-7f22-3e43-920e-1f15d179f925 | 0.46402 | -50.90989 | 2026-09-03 00:09:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0f545e19-4b40-33d1-a44a-63cd9b36a713 | -1.02845 | -53.72637 | 2026-09-03 00:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 44ed5eff-3b06-34e5-b598-6cdd8c931677 | -1.472 | -54.81454 | 2026-09-03 00:09:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a924296a-db60-30c0-a452-9239d6e32798 | -1.01912 | -53.72734 | 2026-09-03 00:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 215f7023-78f3-32ae-9d44-fa5f1de917e1 | -1.51279 | -54.96317 | 2026-09-03 00:09:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 403d238b-d982-3e99-bb20-bb3ca57645cb | -10.9819 | -45.0643 | 2026-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| a3756e7f-44bd-378f-aebb-37ee374f8a84 | -6.6882 | -59.9628 | 2026-09-03 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 47cc4062-14d3-3837-9a30-651fc7b417e7 | -8.0737 | -50.9656 | 2026-09-03 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 9b43be9d-af29-3f5c-8499-0b4ba8a1eefa | -11.0003 | -45.1078 | 2026-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| ba3111a6-df6e-3b7f-b362-94b4b0a3a554 | -13.4157 | -42.4999 | 2026-09-03 00:10:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 7c4ddb21-8a59-3290-bd26-56f2e185e640 | -6.3237 | -56.0434 | 2026-09-03 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 59b3cb2a-a783-3db5-ac51-d2e3c9ca5397 | -10.9013 | -45.3279 | 2026-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| bfb0a5a4-955d-35d3-9db1-a945813551d0 | -11.7725 | -50.4614 | 2026-09-03 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 188854f1-45fc-317f-8ff0-45f9f68468a2 | -18.7766 | -48.8999 | 2026-09-03 00:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8056a179-b4fc-3602-8e3a-ecc56b8ef6ba | -10.9017 | -45.3049 | 2026-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 9b2f4126-b2ec-3064-abfd-6d7eaa69a018 | -6.8412 | -58.9746 | 2026-09-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 44818115-e1a3-3d6e-a109-704eeb58cc4e | -11.7722 | -50.4829 | 2026-09-03 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 6fbb69f2-d20e-3071-87f3-e205ebf296f6 | -18.15 | -51.8156 | 2026-09-03 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 52d89f66-0603-3f1f-adca-2467c3fec8d5 | -12.4033 | -44.8089 | 2026-09-03 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| ddd907a5-1c6f-32f3-bae3-92868b2b324b | -8.7104 | -70.9695 | 2026-09-03 00:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 67.1 |
| c2edc568-b639-3a7f-b035-a6b6b9d81096 | -6.4209 | -58.2943 | 2026-09-03 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| fcb05113-12e0-35b2-a2b7-a359e90a5769 | -6.6725 | -43.4239 | 2026-09-03 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 03dd3c29-6b53-31ba-bcdf-13a99052bd54 | -9.713 | -65.02 | 2026-09-03 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 45d48e08-58b5-3e37-8b5a-cb3c7598710b | -6.3052 | -56.0442 | 2026-09-03 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 26fbbc3d-3da4-3a82-b194-a76cb65d7a94 | -12.4225 | -44.8059 | 2026-09-03 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 76ac0270-818a-313e-880d-303556c313db | -18.1704 | -51.7904 | 2026-09-03 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 747d4ccc-9c08-3e33-a4ce-d1bf50544529 | -6.6248 | -55.2331 | 2026-09-03 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 510808ab-4d56-3cec-87dd-9457e4c28f59 | -6.6247 | -55.2531 | 2026-09-03 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| be66cb2c-dd4a-32b2-ac68-225c591dc9f9 | -9.7131 | -65.0013 | 2026-09-03 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| e4530c84-896f-35c1-b492-3d0a4628af29 | -10.8822 | -45.3305 | 2026-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 00fb27ac-7e76-3208-a82a-90f9f2421998 | -6.6698 | -59.9443 | 2026-09-03 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 0277890a-7942-3eec-b42b-ab0402ef47e7 | -18.7559 | -48.9267 | 2026-09-03 00:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 4474ec9b-85e2-3b1a-b354-8be2a5c1a74b | -6.6913 | -43.4222 | 2026-09-03 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 565068f5-14cd-3584-bf2c-ae4247974f5e | -8.4296 | -54.7262 | 2026-09-03 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b594973f-8b69-32de-b7e7-6381311358ea | -7.0428 | -59.2173 | 2026-09-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| b6495939-ccf7-3c6d-8e4d-08936f434f2c | -8.8709 | -66.6707 | 2026-09-03 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 0cea9923-57ca-39e6-9cf3-d45b7ca68575 | -10.8826 | -45.3075 | 2026-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 202e916b-266e-3d73-ad45-1697bb084021 | -18.1505 | -51.7937 | 2026-09-03 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 115476df-f53a-32df-a461-1d2aafd1c7f1 | -8.5916 | -67.1788 | 2026-09-03 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b1e803de-63d0-368f-8958-b359f2dfc8d3 | -11.7535 | -50.4636 | 2026-09-03 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 95948cbf-ae98-34b9-aea9-d99cfd1698e3 | -11.001 | -45.0617 | 2026-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 7e9250b0-9837-356a-8dd8-c398d7d901c6 | -16.7741 | -49.6333 | 2026-09-03 00:10:00 | GOES-19 | CAMPESTRE DE GOIÁS | GOIÁS | Brasil | 5204607 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| a0dd02da-3a59-3ee7-82c7-91362498b639 | -8.7104 | -70.9879 | 2026-09-03 00:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 185ff4fb-0283-3170-a386-ad171b67a64f | -6.7648 | -59.4408 | 2026-09-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 86000056-6398-3d84-ac8a-c329e03a861e | -7.4954 | -60.7736 | 2026-09-03 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| b0bd8411-c746-32a4-83bf-de491ddc979c | -18.8407 | -46.4417 | 2026-09-03 00:10:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 1225ea52-2108-3abb-9c0f-6d7f202a7b8b | -11.7532 | -50.4851 | 2026-09-03 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |


[Clique aqui para ver as próximas entradas](README5.md)
