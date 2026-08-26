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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03f6d89c-1f36-3672-8277-a05cee948685 | -6.71907 | -59.44931 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dcf0378-6874-37fb-b117-be5dcb360b7a | -7.11299 | -56.5657 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78b42e6b-b541-3220-8a54-be22b80f4466 | -8.14727 | -47.50841 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe68af95-a474-3c6b-8328-bf4cbc425bec | -8.14635 | -54.98937 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c685fbfb-4d84-3f2c-91f3-83b42fe8ef3f | -7.39307 | -55.17262 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b780af98-0a57-312c-8758-801a562d3656 | -7.02156 | -59.23042 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c96e8b2-33d8-3628-8563-31dc58cc135e | -6.86142 | -59.408 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cde767be-ccb8-3645-a50e-a7ea25038bcb | -6.13751 | -57.77159 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30d3a4ba-c4fc-3ba8-918f-dad988ff0f09 | -7.09065 | -56.54597 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7045e1a8-18c0-3272-bf2e-75adb30ba349 | -6.42243 | -54.93888 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adb318a5-c3d9-3357-bf58-9ecf20bcadbe | -6.84654 | -58.98939 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 589729a8-7ba0-38d2-a707-5b6957b88e25 | -6.25832 | -53.36752 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c5c75f6-a0f9-3634-82d2-6445421004e9 | -7.47339 | -61.37238 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55269641-b880-375d-9dc6-b7fba81bf523 | -3.25836 | -52.23417 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17613b2a-07ee-3279-9952-d640a8746f14 | -6.26084 | -53.37983 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffd605f5-1947-3fa1-940d-52e6d8febf91 | -7.01714 | -59.23684 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3c37984-960f-3b98-9931-cb98278277dd | -3.49907 | -57.02517 | 2026-08-26 05:27:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 261ea301-885b-38d7-86b5-bd2008893751 | -6.63401 | -58.50983 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13ba5826-e064-3816-aadd-52b1531cc169 | -6.64067 | -58.51088 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f85006f5-7abe-316f-a164-bc752a485cef | -6.89858 | -58.91582 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e168abb4-3eaa-3c94-b044-c1d9694d67a1 | -8.5714 | -54.81207 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be0156a0-db65-3e3b-98a7-08768941e92f | -3.10584 | -61.23067 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4fd5dc8-8600-31a2-bdc9-e6298ac7e205 | -6.84262 | -59.46192 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca3dc252-70b5-32f3-a2d9-1ce6d916602a | -8.14085 | -47.5075 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b694a877-b943-39d6-9825-be663a8b4dc0 | -8.01017 | -51.8138 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27f0313b-421c-3d3d-a7d6-057b0558593b | -8.6266 | -54.72681 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15af01bf-1008-3abc-8db9-5de22aa061bc | -7.54263 | -61.36049 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3abc343-a876-3a63-b0c0-80985d85a9c9 | -6.13201 | -57.85102 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ec126e0-efb2-3a82-9ec4-11b7d0798be3 | -6.63734 | -58.51035 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea2cb5f6-dcbc-33f3-a945-49aa7167e0cd | -6.64565 | -58.50093 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4e6f4ff-d315-3853-ac2c-04004e565715 | -6.63457 | -58.49215 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78b6f8fd-0ac6-3830-a3b5-95fb132ad7cc | -8.57083 | -54.84335 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb81af93-f494-345a-beab-cae89382e287 | -3.49963 | -57.02159 | 2026-08-26 05:27:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 971aca7e-7a3d-35a9-beb7-877593424439 | -7.38089 | -55.1758 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 841361b7-035d-3b9e-9ec7-397a474b9056 | -6.12509 | -57.71832 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e47e20e5-d842-3968-ae80-07b4a03c8d6e | -6.99061 | -59.27531 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9b1de04-0de8-3abf-98bd-5a4c2870497a | -6.17065 | -53.49314 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c031746-8f47-3825-b968-6dcfc75ed501 | -6.98285 | -59.25985 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b9baf21-7e10-31b0-b23a-f5fa60ff3386 | -7.43197 | -59.77728 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a67d5e1c-ea5a-3e14-b192-c31099aa2f48 | -7.51613 | -55.58694 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e69168e9-1ab3-350b-95a2-723e13dc1db2 | -7.02985 | -59.22107 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0e95568-e8f4-3bca-816f-cca1925216b2 | -6.5149 | -55.22475 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08a318dc-ffcc-3063-a144-742df89f7919 | -5.34239 | -45.15989 | 2026-08-26 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9657e926-4d72-3505-8c9c-943878bb7fe6 | -7.56104 | -61.42173 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06545053-da29-3fc5-8a9e-91c791bba20c | -6.94081 | -52.79841 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d28300aa-795f-37ee-b6f6-30098864a2da | -6.62959 | -58.50209 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9017735d-c5a9-37a9-8352-675b3275de62 | -3.1065 | -61.22662 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3aedc816-952a-3807-b4f0-7fff26b0f116 | -6.65176 | -58.50547 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 47efc12f-e7bd-3370-b251-f4723db69a1d | -8.63486 | -54.75451 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f6200dc-df04-376c-9b3b-6d0e8c2902f6 | -6.97731 | -59.25185 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4375cba-28cd-34c2-9fb7-d48de77dbafb | -6.1359 | -57.82612 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd83adcf-d21f-3104-83fa-dadcaae46d00 | -6.54526 | -58.51747 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75a96151-90c2-3296-a4ce-7d6573dcc19a | -6.81601 | -59.58606 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcf5c213-7544-3570-be68-eadc72e85bd9 | -8.1464 | -54.98739 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b603101-d764-358c-9ec4-12463af8f410 | -7.07361 | -59.22155 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c882407c-96b4-3c8a-a02c-01bc1d6bf955 | -8.07127 | -47.52919 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76200020-bb96-32ad-899a-9a0909f22e8e | -7.03042 | -59.23895 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 010d24af-bd66-33b7-ad76-57c44f8b96d9 | -6.22433 | -53.01257 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 382be906-5a7a-33a0-9507-d111fe18d70c | -6.29946 | -53.58108 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 928b92f6-9f65-39b5-bf22-c4b7db0a7a49 | -6.98617 | -59.26038 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4a789d2-365e-393c-bbb1-14470b9e74f5 | -5.98062 | -55.71265 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3851fc9b-92ff-3b51-9ecf-4beda0e041d9 | -6.51423 | -55.22929 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4445474-92cf-3210-b2f4-e587e20435f4 | -6.80817 | -58.61288 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4de33e9-7297-3e19-bc96-15a826910be0 | -6.2541 | -53.3669 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b6ab3c9-50fa-3202-a20a-e79965987dfe | -8.22367 | -55.00625 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e951a5aa-03fc-3a88-b258-11e44888abf5 | -7.25832 | -49.86479 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b65d05d-1342-322e-836e-ec927040cb51 | -6.40917 | -60.05255 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e57ba86-ca79-32df-b555-9bafc6b0b8e1 | -8.08044 | -47.50912 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0def8d7d-8cd4-366e-9d6e-84b850093560 | -7.02378 | -59.23789 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 295d8025-5e85-3801-ac9e-d92d0f2e23f4 | -6.82664 | -58.66199 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4798cba6-cef6-3a71-969f-b6cb83b6a4f3 | -6.8166 | -59.45422 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9304a47e-1818-3a73-a101-a71c47db67a7 | -6.98564 | -59.28519 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c265591-4bcb-3661-93d4-ad91c0f4eb3b | -8.57063 | -54.81727 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77c55f4e-6a2e-3319-8a89-24fe5ec4a40b | -6.12134 | -57.83112 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c6eff5f-febf-310d-80fc-019b9a0e94aa | -7.54607 | -61.36106 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 738ebf32-4207-3fb0-9560-f5521990b845 | -6.25889 | -53.3636 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b19e62b-37dc-3e83-8840-d2c2d29a58a9 | -8.85735 | -49.71827 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 278a5286-4dc4-3aec-828d-f5db551d9ec4 | -8.58414 | -54.8355 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3de4cf71-5640-3194-ac19-1e071d27e427 | -6.84013 | -52.50459 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67934695-6d6f-3fc7-864a-eba84c6e4064 | -6.79937 | -59.60485 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b1362bf-5c7e-3cb8-bd10-f8b43ff8b674 | -6.62366 | -53.1912 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2679de5a-a3ee-3833-ab8c-f2f4e507f1d4 | -6.62794 | -58.51256 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 835cd59b-1558-36cb-9624-b107cf4e9d93 | -7.52514 | -61.38087 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d5534e4c-8f22-39ad-acfb-aa7f0c03b729 | -6.80985 | -59.68869 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3986ff9c-7519-3e51-91f5-b9626b6b5f0e | -6.70014 | -56.15163 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 287cf23c-7e5e-3926-8713-a46bcf4f7bf2 | -6.88047 | -56.50721 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e60d336e-214d-3d1f-ba70-8ce21c2afd32 | -6.68547 | -56.34501 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae4407d7-a6b2-38e4-9db4-22a718f5d010 | -5.97377 | -57.63297 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42bfeb53-8f6f-3e6b-bb3b-3076abea6906 | -7.07084 | -59.21755 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1396c43b-8629-3cf9-b971-80e9cd04f0bf | -7.20573 | -60.61542 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3670a019-6886-35cf-8291-6fa4936bf832 | -3.2169 | -61.2346 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f50d80d-439e-36f4-b957-461d473b8b7a | -6.9346 | -58.94645 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7faeea1-d43b-303a-9bcf-b4aea42f3833 | -3.21333 | -61.23402 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61839dd5-7319-34f9-b784-b8821dd815ea | -3.07312 | -61.07779 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d06cbb6b-2c7d-3590-b5c3-adc4509b130a | -6.30108 | -53.57623 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01065f48-28f8-36b1-9b74-ccaaf202dc54 | -6.62516 | -58.50854 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c33c02df-0663-3edc-8186-395feb080e33 | -7.25515 | -49.8479 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61989d81-2094-3385-82d1-cf988029d37d | -8.09411 | -51.67596 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d9b96e4-bb3d-3747-b1ab-7934e6f303ab | -6.26449 | -53.38432 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e8372a8-9fbf-3b6f-b81d-54e968b96bac | -6.16334 | -53.68359 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README55.md)
