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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| def5d08a-d14e-3fff-9c1a-b959d020c818 | -8.8548 | -62.4503 | 2025-08-26 09:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 63d17050-db67-3382-b339-de9b75d7fb0c | -6.8229 | -58.956 | 2025-08-26 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 06cb8b8f-35f3-33ac-aaed-eddcd15f9b30 | -8.855 | -62.4313 | 2025-08-26 09:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2a3895ce-0990-3cf1-a2a7-e9d9cd5d3952 | -8.9874 | -65.4192 | 2025-08-26 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 7beb8fdc-aae9-30e9-841b-12c283eac69f | -7.8895 | -63.0171 | 2025-08-26 09:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 11688148-3d31-336e-b069-08a5a4f90fc9 | -8.8548 | -62.4503 | 2025-08-26 09:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| c0dbcbc1-25bf-3a44-9c12-e8e9f62e887b | -8.9874 | -65.4192 | 2025-08-26 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 10d9ff7d-c4a3-3e29-ba01-cba2d61987d1 | -17.0779 | -49.2682 | 2025-08-26 10:50:00 | GOES-19 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 6b7d06fc-5aa8-364c-82ed-44e2e386cebc | -6.2459 | -60.0174 | 2025-08-26 10:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 0f69d9e8-0939-35cd-8200-7d4796ebff30 | -7.54686 | -36.7396 | 2025-08-26 11:17:00 | TERRA_M-M | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 1001ad28-f710-334c-b6d9-ff2b83941615 | -7.54258 | -36.73297 | 2025-08-26 11:17:00 | TERRA_M-M | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 13.8 |
| af60fccb-e081-31d8-bfe2-cfebfa79e378 | -6.2459 | -60.0174 | 2025-08-26 11:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 33ed3ae8-c60e-3f1f-ab03-afa7ccd0ae46 | -10.76 | -47.0424 | 2025-08-26 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| be3e0fb9-7c9a-365c-b241-576e0b0e6378 | -6.2459 | -60.0174 | 2025-08-26 11:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 4aefb8e3-28e6-3407-bbc9-591db498d5bf | -6.2459 | -60.0174 | 2025-08-26 11:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 02842d86-5661-3dfc-aa17-43ad91ec46fa | -6.2459 | -60.0174 | 2025-08-26 11:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| d82d78c1-8a71-3f45-949b-0160e4ccbccf | -10.6822 | -47.1635 | 2025-08-26 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f2ded5af-67e8-3afe-b1ae-ba299a5586d7 | -7.8854 | -45.8779 | 2025-08-26 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a01e120d-162f-3676-80d6-755d73c88fbc | -11.0767 | -50.0042 | 2025-08-26 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 2e4215c6-5a34-3cda-8cdc-51cdbe860a0a | -6.2459 | -60.0174 | 2025-08-26 12:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| c7482bfc-4ec9-3736-a974-d8b576860713 | -11.521 | -52.1209 | 2025-08-26 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| db984b41-23c1-34ae-a446-78e2d77f108c | -6.2459 | -60.0174 | 2025-08-26 12:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 3e6c642c-b614-3c12-aa7c-5d553259cdb1 | -6.8062 | -45.0019 | 2025-08-26 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 8161adae-c7b1-3256-8ca4-c8f6d505b8a3 | -12.7455 | -48.1597 | 2025-08-26 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f0a0703f-86a0-38f3-b4ad-3673753cb745 | -11.6086 | -46.3926 | 2025-08-26 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 630ca4c1-2450-38f7-839a-3cafc1144bf5 | -6.8229 | -58.956 | 2025-08-26 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 11302a3e-5abf-3244-9edf-53b13fc9a0bb | -6.2459 | -60.0174 | 2025-08-26 12:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 2b04e2cd-b7a2-34d2-86fe-ec1fa6d24263 | -10.7787 | -47.0624 | 2025-08-26 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| b90ba55e-c362-39e8-b5c7-27524ece0613 | -10.76 | -47.0424 | 2025-08-26 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| e7da36a6-3c3e-3cdf-a8d8-2de4152115ee | -14.8508 | -47.161 | 2025-08-26 12:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 123.5 |
| b1dfc40f-7abe-31ba-8253-40a6944b2dc2 | -6.8228 | -58.9753 | 2025-08-26 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 87ce570b-8ce6-3f12-8cdb-73568ef8f638 | -6.8229 | -58.956 | 2025-08-26 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 068a9370-ab4a-306c-9e5b-279b481884b2 | -6.8062 | -45.0019 | 2025-08-26 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 2cdefa99-f213-31b7-912f-b03727e4db4b | -11.6086 | -46.3926 | 2025-08-26 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 841e8b73-23d2-3738-8e92-546e13b1b710 | -11.0767 | -50.0042 | 2025-08-26 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ecda1bbb-4a47-338d-84d1-e25b3b0cfea0 | -12.6741 | -47.8589 | 2025-08-26 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| bc25b89d-0771-344a-9e8a-05ad289f100b | -6.2459 | -60.0174 | 2025-08-26 12:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 178.6 |
| 579acea5-da0a-338b-954b-43252dbcccfa | -12.7455 | -48.1597 | 2025-08-26 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| fd830bd5-1146-308f-b646-a657663f8e62 | -14.8512 | -47.1382 | 2025-08-26 12:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5d0dcfff-c343-31a0-ba3c-1b9785770d0d | -9.1375 | -45.2493 | 2025-08-26 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 135.9 |
| b905c2ba-d541-3994-bcbb-9679f3e62df7 | -11.6273 | -46.4126 | 2025-08-26 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f4a06222-9cd7-375e-a398-5178ac6ec9aa | -12.6737 | -47.8812 | 2025-08-26 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e349bd9d-87aa-3f21-b0ee-6e95ee3d5f6b | -6.8062 | -45.0019 | 2025-08-26 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5a941ae9-51bd-3d71-9d67-114cf9260408 | -12.6741 | -47.8589 | 2025-08-26 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| fe5c4e3d-d295-3c9a-ad3a-9029934468d2 | -6.8229 | -58.956 | 2025-08-26 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 2490eb42-8f28-317e-bcb6-a55a19471df9 | -6.2275 | -60.018 | 2025-08-26 12:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 8c443d49-a03e-31f3-aa48-28d10974b72a | -6.8228 | -58.9753 | 2025-08-26 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 562f86a8-cb18-36d0-b37b-aa8e608890a7 | -6.2459 | -60.0174 | 2025-08-26 12:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 232.4 |
| 7fc01d4c-4be9-3aec-b0b0-3971129a437d | -9.1717 | -59.5405 | 2025-08-26 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| aa80684b-aefd-30ff-b3d6-ade2c7964990 | -11.6086 | -46.3926 | 2025-08-26 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| a5b3c17c-c16f-326c-b339-c43468c09144 | -8.8548 | -62.4503 | 2025-08-26 12:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 2c28f642-8efb-3d7b-9d1b-99b251cf1da0 | -8.2524 | -45.094 | 2025-08-26 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 006c057b-5950-3e33-a2f7-91ab9efbad1c | -10.6822 | -47.1635 | 2025-08-26 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 12a8f700-4d6a-3785-9ecd-d0a06bf67094 | -11.0767 | -50.0042 | 2025-08-26 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4abb2d3e-c841-3402-b197-214021851774 | -8.2522 | -45.1168 | 2025-08-26 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 9115aa03-c93b-3a66-9b5f-70473dda9317 | -9.1375 | -45.2493 | 2025-08-26 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 187.6 |
| fbe4d1d4-d64e-3b8f-bbf4-072c6d033861 | -9.1717 | -59.5405 | 2025-08-26 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 7b722cc3-bb3b-30dd-8c3f-54f10d7c5afe | -11.6273 | -46.4126 | 2025-08-26 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d6ea8f76-9b90-3aef-9ac2-3c6b7c7296a0 | -11.2014 | -50.5685 | 2025-08-26 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 3ae4a1b2-e630-3d0b-a672-1321650c651a | -6.2458 | -60.0365 | 2025-08-26 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 6ac3d87b-44db-3e17-b125-bdef3277d06b | -11.6086 | -46.3926 | 2025-08-26 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 192.5 |
| f9516a0f-20cd-3cca-8de4-5807d708b88c | -6.2459 | -60.0174 | 2025-08-26 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 221.6 |
| a6007a83-a67c-3eca-9d35-ce93b474c0e1 | -6.0662 | -44.0085 | 2025-08-26 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 720b44d6-122d-3e6d-a1cd-f506ece4a8d1 | -6.7819 | -59.6711 | 2025-08-26 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e452a228-fc39-3c61-aed0-da433d46cc42 | -6.8228 | -58.9753 | 2025-08-26 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| b98a152f-5f2c-3516-a252-038bc57bd39c | -7.4816 | -45.0328 | 2025-08-26 12:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 479f415a-8978-39c5-bbc8-be0a9630545a | -6.246 | -59.9982 | 2025-08-26 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ec17911d-8aa6-3e61-b158-19953f9439d6 | -6.8229 | -58.956 | 2025-08-26 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 6cf03707-7be3-3cbe-a169-7c7652387556 | -6.8062 | -45.0019 | 2025-08-26 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 2f42a56d-8647-39e6-8965-b99787c674c0 | -6.2275 | -60.018 | 2025-08-26 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| fc12f59d-1611-3755-8928-3e4d9092f176 | -11.6089 | -46.3699 | 2025-08-26 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| daa96d98-c9a3-3d5c-8076-9ba283b248f0 | -0.75863 | -47.74813 | 2025-08-26 12:51:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 1ab44561-a025-302c-b007-5945046fd94b | -2.45116 | -47.32128 | 2025-08-26 12:51:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| af8dca52-fd2f-3907-b0f9-2d53df92041a | -6.23646 | -60.01064 | 2025-08-26 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 5f701e32-f94c-356e-9069-0e31bf268afd | -6.23385 | -60.01902 | 2025-08-26 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c51400bf-0ee1-348e-a46a-c80215af417f | -9.63064 | -49.75472 | 2025-08-26 12:53:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 221.1 |
| 21f0bb3a-62f0-3817-81d4-48061c46f128 | -9.41331 | -48.25344 | 2025-08-26 12:53:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| aaeb7995-b8ba-3bdc-8c13-f59cea15da49 | -9.62825 | -49.77429 | 2025-08-26 12:53:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 126bcb85-d44b-3c1b-b7b3-6cde53e674df | -6.9123 | -59.36401 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 7c046655-30d7-30c8-ba34-64c22c5fd643 | -6.54277 | -53.90693 | 2025-08-26 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 10f711d0-5677-399d-9441-f758e4031734 | -6.77297 | -59.66923 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7a0d784d-de27-3686-9806-bd1985f28b96 | -6.24495 | -60.02076 | 2025-08-26 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 257.5 |
| e1188c47-5620-33ed-8ac5-e51fe127b5d0 | -5.79975 | -59.22138 | 2025-08-26 12:53:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 116c7b4e-d75e-3f7b-8a4a-5925e2a71c1a | -6.91425 | -59.3514 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a3f91bc0-2865-3dcb-8f46-676800cd4907 | -4.96146 | -55.80688 | 2025-08-26 12:53:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 9eea4e2e-c7c4-303b-82b6-d688827e9c42 | -6.24528 | -60.02685 | 2025-08-26 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 5481b478-3c85-3144-9c3f-d4da22bc6141 | -4.96775 | -55.826 | 2025-08-26 12:53:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3dce8a84-caae-3e20-91f9-3d4bd370e10d | -10.30933 | -46.76823 | 2025-08-26 12:53:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3c35c598-9ff9-3b05-80ef-e3aa8c40a217 | -6.8308 | -58.96334 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 8cc1b3be-7243-308d-b46f-bda32af963a8 | -10.54523 | -46.79455 | 2025-08-26 12:53:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| b7e340fe-69f0-30bf-9414-fd0735982216 | -6.69778 | -58.55193 | 2025-08-26 12:53:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 8e900979-a709-3c98-8f70-387ce738920b | -8.29448 | -46.31964 | 2025-08-26 12:53:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 7644ab9e-afb4-3721-bae3-52caae19db98 | -4.96905 | -55.81707 | 2025-08-26 12:53:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5cb8fc41-d5d9-387e-8d42-7d17eb47d572 | -9.00495 | -51.27911 | 2025-08-26 12:53:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| c4373ff1-51db-379e-86d5-3adae7afddd6 | -10.31864 | -46.7613 | 2025-08-26 12:53:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| b4b814e3-0834-3382-8c82-6653eaad1ed2 | -6.68957 | -58.53926 | 2025-08-26 12:53:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 98d889bb-6753-3b09-8a73-db442e1c1dd7 | -6.84273 | -58.95293 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 51fac5d1-8e5b-3efe-9583-3065eb81c2c2 | -8.08745 | -47.31614 | 2025-08-26 12:53:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 17d05bff-29b4-3768-b768-0a79704868e4 | -9.63056 | -49.74794 | 2025-08-26 12:53:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 96798a31-4353-397d-ace8-896eeff1d5be | -6.24754 | -60.01236 | 2025-08-26 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 177.7 |


[Clique aqui para ver as próximas entradas](README103.md)
