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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d57fd715-31e1-315c-8da1-ee45485e0ed0 | -6.3198 | -59.9572 | 2026-09-13 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 768b5a00-580f-31e2-b5ca-520e28da1d43 | -6.0314 | -52.736 | 2026-09-13 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a5b42b40-a798-33bc-9191-d723809562e1 | -6.8445 | -55.581 | 2026-09-13 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| cf8d6c70-fa0e-3795-a3e6-b01226b83a2b | -3.8461 | -58.9178 | 2026-09-13 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b7322a8a-a5fe-38c3-9361-c620365a7ce9 | -10.1639 | -50.3787 | 2026-09-13 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| ba849a20-bcd6-378a-b0c6-34e3579f304e | -10.6431 | -45.9999 | 2026-09-13 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 7181669e-1984-37c1-8f06-946c848f6501 | -7.9645 | -43.9971 | 2026-09-13 15:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 9257433f-628f-3363-b908-87823960f20d | -15.057 | -48.4765 | 2026-09-13 15:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| e56325c9-175e-3c2f-8f66-a5e80bb71002 | -13.47 | -48.4772 | 2026-09-13 15:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| bfaaa25c-77a6-3419-8ff6-7bf6eee3c625 | -12.4533 | -47.3322 | 2026-09-13 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 92135e23-3ae5-3811-8f4e-cf24d23b4f5d | -9.3951 | -50.1121 | 2026-09-13 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 470a5257-a03d-33e3-bfc4-87dbcad81471 | -3.4058 | -59.2347 | 2026-09-13 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 87aa302e-4f96-34b7-a615-6db2354cef75 | -11.4905 | -50.2581 | 2026-09-13 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 0c764d9d-1748-308f-98e9-dccecb7a5558 | -10.5667 | -51.3349 | 2026-09-13 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 237.2 |
| 43cc33cf-9d56-3bd8-aa89-150a69e36153 | -3.1696 | -58.6629 | 2026-09-13 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 29238714-f027-351c-9a35-eaacd832cb57 | -3.6077 | -59.0577 | 2026-09-13 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 48f84854-fe38-3667-92aa-baa3d6ea7732 | -9.1711 | -49.9835 | 2026-09-13 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 6792bb1e-df30-3733-b047-54dc049a2e09 | -8.1124 | -54.8073 | 2026-09-13 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9d8e5940-8c52-3618-8fd6-006635cd8872 | -3.8774 | -51.1825 | 2026-09-13 15:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2d99c9af-2208-3a83-9642-cd2926cd4dd9 | -3.314 | -59.3706 | 2026-09-13 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 35577193-2449-330d-ae49-bf7178ac7b4d | -10.5664 | -51.356 | 2026-09-13 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| bc734d8b-8964-3355-b540-11b68068dff9 | -6.1634 | -47.7239 | 2026-09-13 15:10:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| b527b519-fd45-3604-88a5-a401651461ee | -9.3763 | -50.1139 | 2026-09-13 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 4ec0ba65-cf0d-3a2e-bea8-1bbc673b007d | -6.0255 | -59.9484 | 2026-09-13 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 722a7919-0207-3f7e-8338-6f117fc445e6 | -2.6602 | -57.5119 | 2026-09-13 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 7cc2f8a0-9133-3da5-be16-d1f2a13af744 | -1.3007 | -49.1464 | 2026-09-13 15:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 2bd54a58-6ae9-3231-aebd-78f141275770 | -9.98 | -46.04 | 2026-09-13 15:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 363b3311-9666-3dad-bd05-af9a32b5f44a | -2.91 | -50.35 | 2026-09-13 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96556816-8823-3cab-bbdb-c92984e6f7f2 | -2.88 | -50.45 | 2026-09-13 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3755c14-8d72-3c72-b730-fbf482b9dbeb | -2.91 | -50.4 | 2026-09-13 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79a12419-67ed-3f38-a70d-b8d9f2c64846 | -2.88 | -50.4 | 2026-09-13 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d627623-a400-3fe3-8a4c-bd686eb88423 | -9.69 | -46.07 | 2026-09-13 15:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a5b8ed4-5a62-3258-8648-ec6511bf5c19 | -2.6785 | -57.5115 | 2026-09-13 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 58c02e63-f149-3959-8959-1d4da6220681 | -9.9621 | -45.8351 | 2026-09-13 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 158.0 |
| baefd4e2-bb02-371d-a17f-cc85edb5c4d6 | -8.1124 | -54.8073 | 2026-09-13 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 95c56cfa-d88b-34ca-b587-59eff8273d39 | -13.3555 | -51.7855 | 2026-09-13 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 891988bd-e16a-3899-b2ff-2ff30bc69333 | -6.0255 | -59.9484 | 2026-09-13 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 150.8 |
| a0b218a9-53c1-39a7-9b2a-0ff652c9922c | -3.3688 | -59.4079 | 2026-09-13 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bd3f787a-54c2-310b-8934-29c2c323ea96 | -8.0934 | -54.8488 | 2026-09-13 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e99772aa-6f04-3cb7-8edb-90f2a2881f02 | -9.7041 | -54.3303 | 2026-09-13 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 9d064ea9-b838-3578-875c-81bbe220fb1a | -10.7018 | -54.1458 | 2026-09-13 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| defcd251-02eb-3e40-8c05-88ec223b9a22 | -3.6077 | -59.0577 | 2026-09-13 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| bb424507-629c-3763-8eee-dd547eadf157 | -2.6602 | -57.5119 | 2026-09-13 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| eac24fb5-b5ae-3def-bf4c-e5db00635798 | -11.5095 | -50.2559 | 2026-09-13 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ae59344e-42a4-3235-b9d0-bdcf70141370 | -11.0376 | -51.4559 | 2026-09-13 15:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f51442c6-fb6c-3731-a319-7bad6d002f5d | -6.2648 | -59.9209 | 2026-09-13 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 31f6db00-c1a9-396d-82d0-fdb1ee9534f9 | -4.1223 | -54.0158 | 2026-09-13 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| f2fa3e4e-24b0-3687-86dd-5723cd5c03c5 | -5.1255 | -55.955 | 2026-09-13 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 176.3 |
| c7b73e53-5af7-3a95-b168-0c0db9c0c233 | -13.3552 | -51.8068 | 2026-09-13 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d946d9f6-be2b-3882-994f-102d0cff1e43 | -13.4507 | -48.48 | 2026-09-13 15:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 959f0e5a-51a3-3230-846a-6eff066d2fc3 | -7.8715 | -54.7016 | 2026-09-13 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 0511b062-8403-3a55-aa81-2f100beccaef | -11.4905 | -50.2581 | 2026-09-13 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 233.2 |
| f30665d0-cf9b-3c09-b687-54b764985f9a | -2.9723 | -57.214 | 2026-09-13 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 027b32cd-7de6-31c9-85c6-a455edbe7b0b | -5.6803 | -45.2931 | 2026-09-13 15:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 5808c0de-b9b8-34c9-98e3-725f9a74995a | -2.6602 | -57.5313 | 2026-09-13 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0721f9d2-c2d3-34b9-8c22-f6e95475c158 | -5.2723 | -56.0483 | 2026-09-13 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| bd718807-2271-328b-9711-c589ba8409a2 | -3.6076 | -59.0769 | 2026-09-13 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 306.6 |
| 8df98006-198e-3226-a3a0-1559c55e83a2 | -7.9645 | -43.9971 | 2026-09-13 15:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| f8ef772c-43c5-3570-acf0-b56324d56813 | -10.7532 | -46.2573 | 2026-09-13 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 237ffbf6-aba1-3d20-98c0-62f614a6af3b | -13.4503 | -48.5022 | 2026-09-13 15:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a1f3d7fb-6978-3602-8b83-ba15143ffe2c | -1.2268 | -49.1899 | 2026-09-13 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 36d10db4-ef6a-3903-98d6-c48b5b98077e | -6.9474 | -59.7607 | 2026-09-13 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| cd179fc7-d8b1-3292-89b9-ac10751d0f1e | -6.0314 | -52.736 | 2026-09-13 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 87ccdd67-a3bd-3575-8f04-e84783647717 | -2.7149 | -57.608 | 2026-09-13 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 50a304cc-68f0-3cfb-8ee9-8b45e5895b9d | -3.1697 | -58.6437 | 2026-09-13 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 0bcee3e6-9073-3d4e-8ff0-4d2b9783959e | -11.9911 | -48.6576 | 2026-09-13 15:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| c3be6cb1-1661-319c-a7e0-06050775791f | -6.1046 | -55.6367 | 2026-09-13 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| fc704781-bf12-3124-825b-0ec814db4298 | -6.7172 | -50.4733 | 2026-09-13 15:20:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d413e372-c554-3a1e-8b98-436ea3eeb7d2 | -4.6651 | -56.011 | 2026-09-13 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 49a8cb2f-50f4-32fe-bae3-d1aa88bd87c4 | -8.1126 | -54.7871 | 2026-09-13 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 5a2b53dc-8517-3c77-8f35-170813da20f2 | -3.4058 | -59.2347 | 2026-09-13 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7662d119-b33e-38e2-ac07-5e0be6b925c1 | -11.3532 | -46.8324 | 2026-09-13 15:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| b5ce10b9-656f-36b3-984e-a243f69bdb28 | -6.8632 | -55.5601 | 2026-09-13 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e6d7515a-60ca-316c-bff6-8ba1babd830b | -3.8461 | -58.9178 | 2026-09-13 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f79108e8-b3bd-3cf5-810f-ce9135a44462 | -3.5893 | -59.0773 | 2026-09-13 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 169.4 |
| aec1be5d-b8db-3872-a6e1-e6514273f94e | -2.7149 | -57.5886 | 2026-09-13 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 5305ade0-fba4-31b8-b7df-c4b80a945e20 | -9.1711 | -49.9835 | 2026-09-13 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b53b16c8-7ef5-365f-b26f-8667c7a130f9 | -1.3007 | -49.1464 | 2026-09-13 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| b924e3c9-decf-3897-ad2e-297176e7117d | -6.8445 | -55.581 | 2026-09-13 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 182.2 |
| ece29f24-e6a2-39cf-b9f5-62a28bb44b6b | -6.0312 | -52.7565 | 2026-09-13 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 9f54501f-8be3-3a30-aded-829bcb630d35 | -13.3363 | -51.7879 | 2026-09-13 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 22fa55b7-bc53-3dde-8248-2876bf3c6793 | -11.8189 | -46.386 | 2026-09-13 15:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 259.4 |
| 1590ae6a-a73d-3190-a197-69202d358a85 | -11.8362 | -50.0244 | 2026-09-13 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 7e9db7c7-0c4b-36d4-82cb-5a6b58dbe06c | -6.0256 | -59.9293 | 2026-09-13 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7a3978e2-84cc-3e3d-b9a7-d5f8b0ff6b11 | -9.01 | -50.9312 | 2026-09-13 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| bed11dd0-ac51-316e-ac7c-c1fd1924fe74 | -7.8713 | -54.7217 | 2026-09-13 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| cde9d1ac-9daa-37f0-b33f-ea44071277c2 | -3.4058 | -59.2538 | 2026-09-13 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4799cd05-f9fb-3a00-b37c-5f5a76067dd6 | 0.1747 | -51.4805 | 2026-09-13 15:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ae23edf5-d0e1-31d3-bd1e-f704982d3e88 | -10.5481 | -51.3156 | 2026-09-13 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 96b414b4-1d63-374b-a925-613a9e3e80b0 | -9.7038 | -54.3507 | 2026-09-13 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9a9a0f72-ea8d-3fc9-a3ca-473f3158ee95 | -3.1696 | -58.6629 | 2026-09-13 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0713c5ef-17f1-39f1-8446-4a91c9ac2ff8 | -8.9868 | -49.6797 | 2026-09-13 15:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 51c358d4-9ffa-3b43-821a-3db5068feb93 | -13.3247 | -51.3211 | 2026-09-13 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| bcfb723a-e565-3f64-bc96-c48480402293 | -10.8028 | -50.6326 | 2026-09-13 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| f7666b4c-ebc8-3798-98e6-dc8b10afc425 | -3.8096 | -58.8994 | 2026-09-13 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a5e62f76-432c-3c35-a411-72b43fa111fa | -10.6335 | -50.5651 | 2026-09-13 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| fd8261c7-7a9a-327c-a001-70f42c3e5150 | -7.12 | -42.107 | 2026-09-13 15:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 128.5 |
| 19d65265-d7f9-3798-91f2-aba6f9d27b55 | -11.4902 | -50.2796 | 2026-09-13 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 53f5e9d0-3d90-307f-9cfd-4bbecbf7a5e3 | -10.5664 | -51.356 | 2026-09-13 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| b9ecad18-4a7c-3c2a-bee6-39df21feb7f2 | -3.7181 | -58.863 | 2026-09-13 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |


[Clique aqui para ver as próximas entradas](README69.md)
