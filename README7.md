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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d959876b-4cb0-356d-893a-0f733122a311 | -9.2012 | -59.6367 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6790b095-6a07-333e-875f-2b8edb5e1b36 | -12.5412 | -46.969101 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cd1d089-8eda-3c97-b35a-5beb12c4b907 | -7.2572 | -60.608501 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1430ff-ee86-3faa-805d-81974fc443be | -9.0556 | -60.6427 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f67baf20-043c-35c3-91b1-405baa62852d | -5.8925 | -57.728901 | 2025-08-13 01:01:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3032ef3-01ca-3b58-b075-b91a925ca83b | -11.9153 | -52.5354 | 2025-08-13 01:01:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e8b5c04-8217-397e-88de-0c01a7400f1d | -12.144 | -48.006699 | 2025-08-13 01:01:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96b3089e-8dbb-37d6-b67c-7bc359a2f1d9 | -6.6039 | -43.871601 | 2025-08-13 01:01:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6a86f4b-c7c1-3755-b06f-0f226392be24 | -6.8904 | -59.097401 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f898881-c15b-35aa-b7f4-29b39c95f468 | -23.2999 | -50.3158 | 2025-08-13 01:01:00 | METOP-C | ABATIÁ | PARANÁ | Brasil | 4100103 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f6d9d09-5895-35ad-a54b-6d919a71466c | -12.5795 | -47.040501 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 565c7a47-0087-3b46-83a2-e6a65b1dc4d3 | -6.8758 | -59.124298 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27cbd6ff-a1c2-354d-a355-ba05cd41e286 | -11.9911 | -45.152401 | 2025-08-13 01:01:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b8e1b0b-994a-360c-b921-0a29751b6d88 | -22.381001 | -45.451199 | 2025-08-13 01:01:00 | METOP-C | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2cdb1597-b097-39a6-94de-4bc1590d0294 | -7.1332 | -60.125401 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06964ce9-1b6c-3acf-bc7b-f0ddda0344db | -9.7166 | -49.475201 | 2025-08-13 01:01:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f35a4011-2ef7-32a8-98fa-bce0aa602b24 | -12.3124 | -46.0527 | 2025-08-13 01:01:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8318d219-93bb-3db7-b224-d467101395e8 | -21.1441 | -49.097801 | 2025-08-13 01:01:00 | METOP-C | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8cb774d8-1cd2-36e6-886d-b558e62ac49f | -11.9138 | -52.5284 | 2025-08-13 01:01:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd0abf7-b487-31c2-a089-94ddeb9c1c8d | -7.1372 | -60.096699 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a03b279e-db1e-3147-a622-1cd929ab8fca | -12.6856 | -46.967201 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e94bc2aa-eb3b-384c-9f51-21bd49958930 | -15.1015 | -51.3508 | 2025-08-13 01:01:00 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0844b5d8-e2ab-3597-9c45-d7d2c211176a | -6.888 | -59.133598 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf188bf4-7b16-3676-9dd1-6fd77c5b533c | -12.5385 | -46.958099 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4e1dab7-074c-3712-88d9-9c0219315595 | -6.9051 | -59.118 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 014540cf-0d4d-3af0-839b-df0f8e3d0dbe | -9.7145 | -49.466599 | 2025-08-13 01:01:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d247141-55a6-3172-89eb-c02f5e029538 | -12.5162 | -46.952099 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3858b8fd-8c26-3db1-8fbf-031ffd815e48 | -7.147 | -60.094601 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 52e1d41a-185d-3c89-8d38-31622902a50b | -9.7068 | -49.477501 | 2025-08-13 01:01:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c334f8f-5817-3a04-afac-e58a7d90937e | -7.095 | -59.995201 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64254a43-25a2-3a31-aa0a-2f2548bb7e8d | -7.1303 | -60.112 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 200343b3-0776-3c72-82f2-999098af0acb | -10.97 | -49.5741 | 2025-08-13 01:01:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c8c987d-eb0a-33b8-9327-8ba5baab9c2f | -8.1104 | -55.545399 | 2025-08-13 01:01:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca6eddc-1635-35b5-80fc-d7f4389e6608 | -23.7808 | -51.682201 | 2025-08-13 01:01:00 | METOP-C | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6e620071-3039-36f5-991d-87cfcb36bfc5 | -15.0918 | -51.353199 | 2025-08-13 01:01:00 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93cf4a43-5b13-3a55-885f-6c36f7f20496 | -12.306 | -46.027401 | 2025-08-13 01:01:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f79c4a38-38be-37e0-a04e-d88aef18393b | -6.9149 | -59.115898 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2549b28f-dc2b-3afb-a826-722a5d6b3876 | -23.3015 | -50.3232 | 2025-08-13 01:01:00 | METOP-C | ABATIÁ | PARANÁ | Brasil | 4100103 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9cc18b81-9c9f-39fd-aade-82d1d15e6334 | -15.0901 | -51.3461 | 2025-08-13 01:01:00 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b3dc9059-27ab-3a52-a122-f45d3dee5ba7 | -6.2779 | -53.635601 | 2025-08-13 01:01:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6e3fcb0-e0e0-341e-9c59-7a4cd8f116fc | -11.7627 | -48.1828 | 2025-08-13 01:01:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3320fbdd-13cb-3eef-af18-f9ab243fac3a | -21.142401 | -49.090401 | 2025-08-13 01:01:00 | METOP-C | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfb12491-ae9f-3789-8626-1ad80b15b1e5 | -7.2603 | -60.6231 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a77da5c8-c9f3-3575-860a-5d9156dc24bb | -11.904 | -52.530701 | 2025-08-13 01:01:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c447f3fd-8dd0-30f1-8751-f1f296c1305c | -23.303101 | -50.3307 | 2025-08-13 01:01:00 | METOP-C | ABATIÁ | PARANÁ | Brasil | 4100103 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9724e23b-41f6-3418-bf01-e6b3fbed10e6 | -7.1429 | -60.123402 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2bb08478-d1a5-3bb0-b7c8-44f1c5441dbc | -12.5856 | -46.981098 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4646de87-aaee-3f91-b32e-c0c0d14041c4 | -5.8848 | -57.740101 | 2025-08-13 01:01:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfe2bf0d-06a3-3ca5-8778-73c71f9c0043 | -7.0978 | -60.008301 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d78c79c5-25dd-3561-9e28-53fab61b39f8 | -7.267 | -60.606499 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8457b777-7816-3f45-a62f-b0a0ff1d0d80 | -10.1869 | -49.497501 | 2025-08-13 01:01:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da17118e-856e-31a8-84ce-83eb6f789c84 | -8.3744 | -49.349499 | 2025-08-13 01:01:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2a641d-6128-3881-a628-02c38f180bcd | -7.2672 | -57.6334 | 2025-08-13 01:01:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48a6fa7f-3bf5-30e2-a4f5-023db57410a9 | -16.3144 | -52.921501 | 2025-08-13 01:01:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed966530-4778-3deb-ac78-d47d6144879e | -12.5731 | -46.972599 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad87da0e-a26a-3c92-acc1-0d764ad1a069 | -11.765 | -48.192299 | 2025-08-13 01:01:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21752e6d-54df-3366-a3e7-53a1c6c1ceb7 | -9.1887 | -59.625401 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d3e3603-98cb-34ad-8e97-ad04a8729d7c | -11.7604 | -48.173302 | 2025-08-13 01:01:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ec8ab93-5d6c-3977-97aa-ee57805049b4 | -7.0852 | -59.997299 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfa9fefd-f1f6-332f-b5a7-5a753636c502 | -12.5509 | -46.966599 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b46f151-705b-3fd1-946a-f63a671ce502 | -12.5828 | -46.9701 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e55d6c2b-1087-3e4f-a2a6-2cfc8c6e7922 | -9.1943 | -59.6521 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 261489aa-8038-38a3-ac10-7188721c5a69 | -13.1112 | -46.8466 | 2025-08-13 01:01:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a99cb409-d5d3-390c-9eba-bd75d664a57d | -10.8885 | -50.542099 | 2025-08-13 01:01:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e4f4e06-99d5-3280-86b8-f57767400069 | -6.9076 | -59.129398 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21654a73-9468-39e4-9194-136195e29dbc | -18.540501 | -46.045101 | 2025-08-13 01:01:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 00c564f0-2e81-347f-b3a7-bd6139660056 | -6.8734 | -59.112999 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aac4f018-742b-3340-8c8a-4143da052ca3 | -11.0846 | -54.486599 | 2025-08-13 01:01:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 369cd187-9dfa-33a3-a622-57a95c2afb06 | -12.5287 | -46.960602 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 834f2019-dd89-31bf-a82e-2dfa0d961f02 | -7.0908 | -60.023499 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 505f6158-6cd3-3523-bfbc-85c0b5d7a741 | -22.3859 | -45.4711 | 2025-08-13 01:01:00 | METOP-C | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c42970d-4508-3985-ba8d-b86e035fc152 | -16.5965 | -47.0322 | 2025-08-13 01:01:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 60c955b4-6981-3f80-9784-44b9bb620075 | -15.5475 | -43.1427 | 2025-08-13 01:01:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 6734b219-8eeb-3c84-a470-d64c0e4d946d | -20.924 | -45.2365 | 2025-08-13 01:01:00 | METOP-C | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53ce0291-8850-39bf-bd84-ba076bb20624 | -21.1458 | -49.105301 | 2025-08-13 01:01:00 | METOP-C | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87e54ef9-5219-314a-a918-81fd7cfc8e7e | -5.8484 | -59.901001 | 2025-08-13 01:01:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f45b99f-492c-3b72-8cbf-8a9b7bcc74a0 | -8.1155 | -55.568199 | 2025-08-13 01:01:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b504220b-6e4f-3463-843f-054522f2f366 | -16.5942 | -47.022598 | 2025-08-13 01:01:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7f79cfac-933b-347c-931b-d4a868c1576b | -23.7824 | -51.6903 | 2025-08-13 01:01:00 | METOP-C | KALORÉ | PARANÁ | Brasil | 4113106 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97070dd5-4ca5-36e0-ae5c-1bd350d95f0b | -6.2763 | -53.628799 | 2025-08-13 01:01:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96fee2db-37c1-30df-b4c3-87b2da98627d | -8.1121 | -55.553001 | 2025-08-13 01:01:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c16da73-0474-38a6-8d04-c42b00fdcae3 | -6.8978 | -59.1315 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bbec49ce-cd64-3784-8b27-8b5e5dda5281 | -7.1401 | -60.110001 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5680a033-4d29-3610-9810-b252dcbd96e3 | -12.3221 | -46.050098 | 2025-08-13 01:01:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 63e9a865-fc13-3b21-8a67-b7398e9710ad | -6.8905 | -59.145 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8250a1b1-20cf-36de-9e99-18274bfda8a5 | -12.519 | -46.9631 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31a0153a-1f5a-351b-af72-c39f74ba77d1 | -12.5314 | -46.9716 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 780af3b2-e264-367a-a312-e8b630ed7129 | -9.1845 | -59.654099 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbeb16e4-892d-39a6-b6b3-5f731272b769 | -12.5822 | -47.0513 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0d9d847-663d-382e-ba44-584cb0727aab | -12.3092 | -46.040001 | 2025-08-13 01:01:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eebf6cba-51ad-31f6-85fb-11772cba3e29 | -18.538 | -46.034801 | 2025-08-13 01:01:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b0adb84b-de9d-3e5d-ba90-2b42cfb0e1b8 | -6.9027 | -59.106701 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84599390-c5a9-36d9-ab93-2ebe4fc6e5e1 | -7.1499 | -60.107899 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff9fbf3-9345-3b45-b8a3-d83218539b45 | -9.0653 | -60.640701 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7f7ccd-786c-35e8-87df-dbf51ece0510 | -6.8831 | -59.110901 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 342e0dee-a49f-39c8-acd6-879705b4641a | -18.057199 | -51.2939 | 2025-08-13 01:01:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 343c9c20-c7b6-39cc-81d9-a00e246d1e96 | -11.7725 | -48.180401 | 2025-08-13 01:01:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8f0eca2-68e5-3d16-8343-177e008bc0ce | -6.8929 | -59.108799 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 52d7459b-d5ca-31e4-a137-d708b3f20b8b | -9.1915 | -59.638699 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 066ea58b-3d0e-3fb1-8a28-fff81b71b336 | -8.1253 | -55.566101 | 2025-08-13 01:01:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
