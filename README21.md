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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1b7812a-ac4e-36be-8f69-9230bece7db5 | -22.37062 | -50.01921 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d019682b-4451-3ef1-b533-bf5fb60d4174 | -23.38688 | -45.38895 | 2025-10-06 03:40:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 82756c82-293c-39d9-8dee-37af4b9da322 | -23.38871 | -45.39263 | 2025-10-06 03:40:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2b832d42-6203-3eb5-b39f-08e8fc3555e0 | -22.38333 | -50.02128 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 05da117b-90a0-32ad-8cd5-cc952db514eb | -22.37563 | -50.02578 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c28d9d32-d735-367a-8ecd-93faae3b6a58 | -23.83818 | -48.5305 | 2025-10-06 03:40:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1408d07b-cd14-3707-87e4-975a7d443cfb | -22.35701 | -44.21411 | 2025-10-06 03:40:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9dbebd2b-2344-35b9-9ffe-308f74dcfd90 | -22.37854 | -49.97125 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d5f4f979-6d74-38b6-9fe6-eccae75032b1 | -22.57958 | -44.86567 | 2025-10-06 03:40:00 | NOAA-20 | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c940b732-6f74-3af2-a940-598ef2b4dfcd | -21.6106 | -45.2983 | 2025-10-06 03:40:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 085b2580-8c8b-366b-b413-5015c2ecc42e | -23.58904 | -50.27293 | 2025-10-06 03:40:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 135064e3-2c3e-3893-8dd7-5ea9f16239c4 | -22.3618 | -50.02822 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ba2d2658-4cae-3609-b368-80fd91461e03 | -22.3764 | -49.96849 | 2025-10-06 03:40:00 | NOAA-20 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 03a0eb2d-43ff-35ba-b08e-f4287683ad2b | -22.51559 | -44.22037 | 2025-10-06 03:40:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 27eb461a-e56f-3a31-b7da-ed4f14318366 | -22.81701 | -45.53854 | 2025-10-06 03:40:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 918d32ec-777f-3b42-a364-e1d43a8a9d9c | -21.60823 | -45.28568 | 2025-10-06 03:40:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 30662275-5614-324a-bb30-79bf8b10a70a | -22.9487 | -46.13132 | 2025-10-06 03:40:00 | NOAA-20 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 746af2a0-8b6d-3e49-a28c-a5df742fc788 | -23.38984 | -45.38715 | 2025-10-06 03:40:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a870d6fb-a5cd-3223-8705-f6fb00373526 | -22.1186 | -45.00437 | 2025-10-06 03:40:00 | NOAA-20 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f2e668b1-c2f3-3eb8-a57f-2ca975a47238 | -22.358 | -44.20922 | 2025-10-06 03:40:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 58e42a06-4e25-39c8-a0ba-d7e47a136de6 | -23.39809 | -45.39435 | 2025-10-06 03:40:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| b2bdbd88-1027-3bc3-8cc5-6547dc44de1a | -22.97339 | -48.34543 | 2025-10-06 03:40:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f0f6b9ff-8aff-392b-9aa5-d0cf8844a179 | -22.63256 | -43.63083 | 2025-10-06 03:40:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 142fe917-57de-33b9-8946-6d35d8f20e06 | -23.23464 | -51.28843 | 2025-10-06 03:40:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 248aa7c1-da1d-357b-b2ec-8092e8a8a37b | -21.60498 | -50.9567 | 2025-10-06 03:40:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4d7a68a0-23f1-337c-94fe-6647c56e12fa | -22.98483 | -46.1551 | 2025-10-06 03:40:00 | NOAA-20 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ebef5938-a7a9-3746-aa72-3a969cead07e | -22.03182 | -45.30264 | 2025-10-06 03:40:00 | NOAA-20 | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 530795d6-b9ef-38fd-80aa-1f8c735a8583 | -22.36311 | -50.02288 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b863f33e-4f20-3e7a-b121-a4eab1eeb77b | -22.44949 | -46.86459 | 2025-10-06 03:40:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1436ad51-6301-3c8e-8a12-1ca2f77a5070 | -23.39625 | -45.39075 | 2025-10-06 03:40:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 77ff009d-adce-3c65-9af7-d22917ef3837 | -22.99117 | -46.14955 | 2025-10-06 03:40:00 | NOAA-20 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f86c26b3-2f3f-3237-accc-27b0669cf6ee | -22.36418 | -50.03178 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 003511a8-28f6-3234-b314-65ace69255bb | -22.37508 | -49.9739 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6b228e12-1a58-3bb6-937c-8a257bf0968c | -22.62847 | -43.62915 | 2025-10-06 03:40:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 87c73496-aba7-33ea-bc7b-2e34d2bcea07 | -23.43617 | -45.47901 | 2025-10-06 03:40:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7ca0bfa9-cf53-37b5-9f41-c67c8cde4054 | -18.0008 | -57.5444 | 2025-10-06 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 242a382b-68b3-3507-81f1-e25dd89d5e63 | -10.3162 | -50.278 | 2025-10-06 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b5573839-b37e-34b4-b063-9ecd6db65104 | -12.4853 | -45.5587 | 2025-10-06 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 93841eeb-c8ff-3241-9175-1d04927d4f34 | -8.633 | -46.2984 | 2025-10-06 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 211c50a6-0b43-3ca3-8036-e9eb012c7c80 | -8.6139 | -46.3227 | 2025-10-06 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 62197773-579d-3db2-b434-c0193468d2b9 | -17.8621 | -57.5818 | 2025-10-06 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 1e03f8cf-f442-3166-9f61-ff684d1d7f07 | -10.4285 | -50.3518 | 2025-10-06 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| efde1ae6-0d5f-3b67-9990-2c3a1664bd87 | -11.7017 | -45.4226 | 2025-10-06 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 40bec109-c876-34ee-a93e-0261ea848ab7 | -17.981 | -57.5468 | 2025-10-06 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| a6437491-77dd-302c-9720-9302c7783edb | -17.9813 | -57.5262 | 2025-10-06 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 3cf93fb7-4667-3169-9bdf-6415417f74c3 | -18.1366 | -53.3946 | 2025-10-06 03:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 454cd3bf-924c-322a-9609-424d84d7e4c4 | -18.1167 | -53.3977 | 2025-10-06 03:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 701880be-e13e-3756-9947-06d42c9d469c | -12.9142 | -47.3105 | 2025-10-06 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 00c37253-13b3-3446-a259-b3e8700331db | -14.3538 | -47.7175 | 2025-10-06 03:50:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| da353f44-e35a-3166-a1d4-3a869a8e6bc7 | -17.8617 | -57.6024 | 2025-10-06 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 3a9d5351-df80-3462-87ca-4b2c9db24468 | -10.3165 | -50.2566 | 2025-10-06 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| d8affc1d-b4bb-305f-a561-4cbac15fbd1c | -17.8818 | -57.5794 | 2025-10-06 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 6e409807-fc9f-3b82-a8a7-bab9d29f7a57 | -12.9146 | -47.288 | 2025-10-06 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 5964d058-e02b-3646-929a-2a15cc77fcc2 | -18.1362 | -53.4161 | 2025-10-06 03:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c0ec2ce3-4e1d-34ec-b5f0-d472933433db | -8.6327 | -46.3208 | 2025-10-06 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 4b0d7998-92bc-3b87-9dee-24c2feefec72 | -18.1167 | -53.3977 | 2025-10-06 04:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 135be00b-0a1f-352b-8cdf-344e34e413f9 | -12.4853 | -45.5587 | 2025-10-06 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 025b2dd4-5ff3-3fda-b762-4e65e091a32b | -8.6139 | -46.3227 | 2025-10-06 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 027c93ab-c4a3-3929-a399-c9df9a4600d7 | -18.1366 | -53.3946 | 2025-10-06 04:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 0dfb96ac-c927-3da6-b679-262ced69f40b | -8.633 | -46.2984 | 2025-10-06 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7a1fa0fa-9850-3ec9-9add-76bc05704811 | -12.4857 | -45.5356 | 2025-10-06 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 7cc4f230-041c-33ce-a2f8-efa98cb25289 | -17.8617 | -57.6024 | 2025-10-06 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.6 |
| e0492c56-2d74-3679-a47b-e516dc021a1e | -17.8621 | -57.5818 | 2025-10-06 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 4823fcc7-6898-3960-ad59-12dac3a7807a | -18.0008 | -57.5444 | 2025-10-06 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 173065f8-1dd8-39d1-a4d4-bea11acdbdf4 | -17.9813 | -57.5262 | 2025-10-06 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| ee694a52-aefb-340a-86b3-e0da69a434ea | -17.981 | -57.5468 | 2025-10-06 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| a7b6aff1-7f64-3072-be4d-e66ce55d3f0e | -18.1362 | -53.4161 | 2025-10-06 04:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 56.8 |
| bf91a10e-e843-35b9-9040-da4a17c04f2d | -23.7362 | -51.9193 | 2025-10-06 04:00:00 | GOES-19 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 94.9 |
| 05060edb-53ab-3c16-a0b1-3676963c2276 | -12.9146 | -47.288 | 2025-10-06 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 9547dfc7-d595-3436-9793-04321fc7a2a7 | -14.3538 | -47.7175 | 2025-10-06 04:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 302288aa-7d83-390d-9665-4bf098a0a31e | -8.6327 | -46.3208 | 2025-10-06 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| c903ddfd-a38a-3886-9624-4daf90ce6c60 | -8.1687 | -44.2534 | 2025-10-06 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 0e0ef948-e857-3bf4-9d31-a83999c8a791 | -12.9146 | -47.288 | 2025-10-06 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 4cd42b43-b913-3721-b8b5-ef6623152edf | -12.4853 | -45.5587 | 2025-10-06 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 943c7553-301a-3397-ba08-86a4c9e818e7 | -17.8617 | -57.6024 | 2025-10-06 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 3b82671e-6a5a-3e50-83a0-f57e0457eeba | -11.0151 | -46.5393 | 2025-10-06 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 13461153-8377-38b1-a3d7-a32f2f838963 | -17.981 | -57.5468 | 2025-10-06 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.7 |
| cd3c4d03-7ece-3494-8ba1-97a2760c7a4e | -9.6793 | -49.9569 | 2025-10-06 04:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 54a86a66-bc06-3caf-8e48-646bbd8f7c33 | -17.9813 | -57.5262 | 2025-10-06 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| ff8c9049-6f15-37b0-80c5-22a66ec04951 | -8.6327 | -46.3208 | 2025-10-06 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a3a4bd89-0a10-3daa-a79b-c569eb8be129 | -18.1167 | -53.3977 | 2025-10-06 04:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0c122f7f-c553-3e36-ab66-99ad28daa843 | -12.4857 | -45.5356 | 2025-10-06 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| f344f5bd-6b16-3028-bd0e-3e328f456909 | -11.8029 | -45.1087 | 2025-10-06 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| ace500a4-e48b-3254-ba6c-6c7147025fe3 | -18.0008 | -57.5444 | 2025-10-06 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 90d3f05b-1407-33a0-8896-fa8c773f9212 | -18.1366 | -53.3946 | 2025-10-06 04:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 66242f2c-5da6-3c53-adce-e5c89e3ca48a | -15.335 | -47.3042 | 2025-10-06 04:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| c1f306a0-016e-3386-9740-4bbc0fd3b3cf | -17.8621 | -57.5818 | 2025-10-06 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 79329304-256f-39ee-8722-80a173cc1a20 | -18.1167 | -53.3977 | 2025-10-06 04:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 23f7f0db-25bc-3b07-b467-178f08622bdd | -12.4857 | -45.5356 | 2025-10-06 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| d0735ac0-f05f-3261-9ef5-74a32a0545bb | -11.0342 | -46.5369 | 2025-10-06 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 0de2ed4a-593c-3a2e-8a80-8c40fc83f292 | -17.8621 | -57.5818 | 2025-10-06 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| b83fa619-4fba-35cc-a768-8334fcce4c5d | -9.6795 | -49.9355 | 2025-10-06 04:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 8c1bc694-27b8-302d-80aa-470855a79764 | -12.4853 | -45.5587 | 2025-10-06 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e0faf48c-19de-3826-8924-08df93009673 | -18.1366 | -53.3946 | 2025-10-06 04:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 262c18c3-6f09-3b65-a42d-1db6d183528c | -11.0151 | -46.5393 | 2025-10-06 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| c694843e-cd7c-317a-a037-fe37d8853d24 | -11.0154 | -46.5168 | 2025-10-06 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| c3d175ea-9e2e-3a6b-bd3f-36764a6bd52c | -17.9813 | -57.5262 | 2025-10-06 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| bf1f0496-4d18-3458-8f3e-8ecd78bc6ba3 | -17.981 | -57.5468 | 2025-10-06 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| ffe130f9-61b9-33b1-8512-2f3873bbb24b | 0.56413 | -50.85116 | 2025-10-06 04:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f55f0d-6775-3762-b703-8fbb5a308d54 | 0.56351 | -50.84704 | 2025-10-06 04:23:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README22.md)
