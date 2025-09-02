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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48f570f3-85d1-3dbd-a081-83313bda6b05 | -6.53071 | -56.20937 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4afc9610-7a81-3818-864e-55ab111ad81c | -6.84386 | -52.80956 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b52c5d0-25c1-38ea-8a01-01a12ef83c72 | -6.82514 | -52.81841 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f25f5d77-2d47-30b1-a974-a5da93176ff6 | -9.26423 | -59.75631 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4353b1bf-bded-33fc-acbf-cf78981d064a | -11.67189 | -52.20411 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a1c5cd7d-5686-3c74-94bc-207b9512cfb2 | -6.9259 | -63.13407 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51b767dd-a256-3423-8b0e-08212d4272f6 | -6.82475 | -52.82787 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41f96467-0207-3515-abf5-2318738069ee | -8.97718 | -65.97437 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e054c305-d3c2-3a16-838d-cb0f57bebdc5 | -11.64948 | -52.1721 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b3b3ad48-3a1b-3a78-9bf9-aada5292bec4 | -8.76543 | -61.42546 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa624826-e3d1-305e-927e-d8aed63beeb0 | -7.06338 | -62.99336 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1568d668-adb2-3789-ac3d-1f1595e6a4ba | -11.67084 | -52.19821 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7360627f-ccf6-3478-af8c-2a9bc0275ed9 | -7.28114 | -60.64697 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43c0931a-4679-32ac-9e8f-e20fdef15669 | -7.54144 | -63.84381 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0757855e-4015-3d2f-b31f-95cffa2556f2 | -7.69977 | -61.09998 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed8cbbed-f1aa-3610-bfef-3017346891e5 | -8.50613 | -63.90825 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e76831d-bdab-3672-9652-47140197b53b | -6.22102 | -53.5754 | 2025-09-02 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7abd1b87-0333-3661-8c81-0f2a7eb8fc12 | -11.66097 | -52.17861 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 30a16304-e43a-35ab-995a-f470bac28ec2 | -11.6681 | -52.22042 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c4633076-571a-3c5c-b012-479a0267cc82 | -6.2767 | -62.53786 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e8d09c9-7a45-3663-98e3-bc30ffd7f1b4 | -6.82017 | -52.81442 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aabdda7f-3562-32e5-a05d-b88fb526698e | -8.75758 | -61.43156 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7c8184e-4388-31c2-a8bd-741ad47c2749 | -6.47938 | -56.00785 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ea6835d-d531-3969-b224-fd9de7f3c6a2 | -9.8368 | -48.60968 | 2025-09-02 05:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 766e62de-18ac-3b0b-9cda-80c9d994218e | -11.65535 | -52.18802 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 52c7e955-18f4-3a93-b94e-d1a3fd18454d | -7.09611 | -63.13244 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f221f3de-b665-3ea2-900d-d1e8db05d538 | -6.34289 | -53.42831 | 2025-09-02 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1816eb20-c276-37b0-b503-59a42f14fc66 | -8.84857 | -50.58404 | 2025-09-02 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f426691f-5149-3fe9-b469-28daa759a054 | -6.84197 | -52.8234 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2fcbfa1-6ba4-3ad7-b2e4-044ad9d452d4 | -11.42411 | -55.19041 | 2025-09-02 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d4a5043-7c66-3abb-98ad-b1fc2eb966b3 | -10.7622 | -59.83618 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a38536f8-2394-3e44-898f-cc50db2042c0 | -8.51289 | -63.90936 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1735fad-4bd2-329d-ada1-148643094041 | -6.04244 | -52.17566 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aa170bd-27d1-3cac-90c3-f5fca83b35af | -7.78632 | -61.56837 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5958dcfb-2ec1-3da2-bf10-e900b30c774a | -7.55972 | -63.83877 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78e46dfc-b1db-39e3-8c10-b923cf541f68 | -6.8088 | -52.81641 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09859502-8cc4-3d22-8868-541a793e0219 | -5.1465 | -60.37143 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d0bbfae-c903-3570-b37b-723ae518e333 | -6.79893 | -52.80788 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1c1b57c-1bed-3e01-a1d0-ad840dd314f1 | -6.78165 | -52.81251 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0900d92a-2e95-3357-b5ae-645900e2e333 | -8.42687 | -62.29389 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ee145fe-6379-33d7-8fc9-8b50a9425aeb | -8.76657 | -61.44031 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 008fc635-7b9e-3e63-a28b-5166765be809 | -6.81724 | -52.83498 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb5aa44b-1439-3b23-a3c4-38821c4443af | -6.85422 | -52.81488 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8df75137-46d1-3167-9d2d-5458a2017103 | -9.54415 | -62.38895 | 2025-09-02 05:31:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 350dee5b-09a5-383c-bcb6-982b44c81257 | -6.15348 | -62.52555 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1200c827-8dc5-37c6-92b1-7d81e51cddc8 | -6.79749 | -52.81807 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 604b7d97-9414-3de3-a1a6-90e92ce89924 | -8.75607 | -62.43214 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db21c33d-e97b-3139-acf1-d18bcf1b3efd | -7.53347 | -63.85 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5996c9c-25da-3563-8b9d-26d0fa6d0ae7 | -6.82115 | -52.81358 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b8ede43-5b34-35ee-92d5-36ec269443de | -9.28212 | -61.01683 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa41b0f9-84ab-3a99-8896-6ba0999edd74 | -11.64892 | -52.17667 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3401edd-6e50-38b6-9849-8f3841d57d21 | -7.34808 | -57.62482 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ebacdad-5aca-30a3-9517-c60559d61629 | -8.72102 | -50.44967 | 2025-09-02 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eceb776-84d6-3fc7-a07e-a73522146b1c | -9.31238 | -59.20671 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7604df92-a3e2-3a39-8372-5fda22942caa | -6.92141 | -63.14062 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3c3243e-0f67-34c1-b349-5b8adec8d492 | -9.27744 | -59.74142 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab18a584-8a2b-3792-9312-00625ab8a8cf | -8.65105 | -62.6051 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e243242-8923-3b2b-8b42-755227134e06 | -9.27263 | -59.74911 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb30fbc7-809e-3b24-9a56-d0b1f44022ad | -6.81772 | -52.83163 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f67eb41-5c41-31e3-883c-ff315d8c420a | -9.4397 | -60.57921 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a58e2d8-6f85-3796-b065-61a8eb57d209 | -6.34802 | -55.5593 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b8b8a55b-aa6e-3881-a989-23fb96f4f272 | -7.11129 | -63.01547 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec59ce19-4f24-37b5-8716-24af20961f0e | -8.75384 | -62.42462 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e4e8f1e-4934-3166-8099-2c7ab9d04908 | -6.77575 | -52.81512 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd6b6029-cc6b-38cc-9f7c-ae947af365c8 | -11.31536 | -55.20923 | 2025-09-02 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21095be4-daa4-35c4-98f1-d08a551cd3bf | -6.77416 | -56.29906 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89ed007e-3ce6-3fb8-ba33-edc236c41605 | -6.80243 | -52.82234 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e336827-686f-3f9f-9ee6-deda6ffabff3 | -6.82661 | -52.81416 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b35d69c-37d5-35b9-94af-2482966e7276 | -6.84786 | -52.82084 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 016212e5-bc70-3ab4-9440-53e06f0d19d3 | -9.73211 | -48.97616 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7288a13f-6f4c-3007-9ab2-6f32be4ee5b6 | -9.25706 | -56.89943 | 2025-09-02 05:31:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52c1a6bc-4587-3aa0-864a-199708a402c8 | -10.39048 | -59.41196 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e68b8f6-881c-34ca-a83c-83eaba3a5963 | -7.69866 | -61.10716 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6724d021-b5ec-3caf-a4ab-94a6286b903b | -11.65494 | -52.17767 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b8fc6430-1e4d-3e07-aa4c-54d76c41598d | -10.75816 | -59.83794 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a572d5f2-c942-3a36-a50c-30e0e06ef853 | -7.69922 | -61.10358 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c23993b-54af-38a2-89a2-ed8c57723cc1 | -8.5518 | -63.01554 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa6a0ed0-6290-329c-bba5-8c3ea33914ab | -8.69905 | -62.40883 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fcef535-3306-3313-9f5c-2e553b8cfa02 | -9.7577 | -54.76661 | 2025-09-02 05:31:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9db6733-4ae1-3fc3-b171-730eebc123ed | -6.8474 | -52.82421 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44658bc9-d22c-3c86-ac94-1b368031123d | -8.73508 | -62.41814 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d23c90d9-2540-3454-a378-373399b98d06 | -9.25761 | -56.89542 | 2025-09-02 05:31:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30ff81d5-6bfa-318a-8fc4-d4a5f27ea927 | -7.11298 | -62.98333 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ef27956-b269-395d-b512-19464ef76cbe | -8.5007 | -63.91512 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b3e771a-aeab-309b-b4f5-8790a2f55dae | -8.66429 | -62.9259 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3a22fd0-3a16-3c40-8a83-df910baf9ec4 | -6.1507 | -62.52153 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35d97e6d-d2c5-3ac6-b764-8c4116a5f340 | -7.69602 | -50.27563 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9227431b-3fa0-39c5-974e-39e7e2aa1abd | -6.85279 | -52.82528 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f174253-15b1-3a3c-a491-2103d1cb56b1 | -7.54119 | -61.33488 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5af8388c-7297-3993-b8cd-bfd9955837d5 | -7.59013 | -63.45201 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 928720b9-481b-3a53-874c-3a0f894bd4f7 | -7.58698 | -61.62746 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 555d4ba8-6a7e-30d3-9133-044a7188201b | -6.83065 | -52.82518 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 141bf342-1958-386d-a474-9e3ec62e981c | -6.82319 | -52.83208 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4337b2d2-8f44-3efc-b8fe-bfabdaa0ef2a | -8.69239 | -62.40777 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3d8600c-3496-33a1-bf0d-4ff465d110d2 | -6.33827 | -58.18127 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c7e0134-7a09-38f2-979c-80b2178a4a7b | -11.84198 | -51.46824 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5a5d34c-daf7-34e7-a886-79549f97c53d | -11.67859 | -52.1852 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e568997f-9adf-3f33-8a5b-90fa91c5920d | -8.67003 | -62.85153 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9341d384-5d62-3722-98ba-add3cc5e4424 | -6.8606 | -52.80876 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed421cb2-a735-37ed-aa70-2f4053a492be | -11.67584 | -52.22279 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |


[Clique aqui para ver as próximas entradas](README75.md)
