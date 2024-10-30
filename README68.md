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
| 88e98b78-c241-3014-b0e1-1b5d346592b7 | -3.13299 | -54.26402 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f37c238-6aeb-3eda-bd1d-4951b1f349c2 | -3.13226 | -54.26859 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8e024b1-08da-311b-a091-0a7651979246 | -3.12918 | -54.26338 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65b0fb69-012c-359d-ab72-7ca760dae77e | -3.12846 | -54.26795 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69c72ddb-95a2-3cf0-8a62-8e9b2c04313c | -3.12773 | -54.27253 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a017d8f-0ae4-383c-81dd-e6b0887dcc6c | -3.12699 | -54.27717 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 029399b2-9897-306d-84af-643667506c14 | -3.12626 | -54.28182 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9176eff6-7c29-395e-9a68-6e6cf4fdcdeb | -3.12538 | -54.26271 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4f0466a4-3851-37b5-8f7c-e3710e431110 | -3.12465 | -54.2673 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f3836909-4a9b-3265-95c1-3f71b5a635fd | -3.12392 | -54.2719 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 53cd3989-1ffe-321b-9bbc-ec86a231ff9d | -3.12318 | -54.27655 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 26fc4e87-813f-3592-9fcf-05222ce0c019 | -3.12244 | -54.28119 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b6df7f1-5b4c-390a-913b-847a340bbf97 | -3.12158 | -54.26204 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 19bda016-b43a-35eb-bb31-3c2239dda106 | -3.12084 | -54.26665 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d235c8e-2c55-311a-8860-d7c939d35be9 | -3.12011 | -54.27127 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b23e901-1279-3221-8499-7ad0868142aa | -3.11937 | -54.27592 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 62d63e8a-b8c1-34b2-86e5-16ccd97bc24b | -3.11863 | -54.28058 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53ed5659-ba3e-3198-995f-ca96681a273d | -3.11703 | -54.26603 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0053af58-8333-3e26-90bb-8ae999fc47eb | -3.11629 | -54.27065 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef5aaf9c-8082-3c8f-b4fd-b95715bf0ba6 | -3.11481 | -54.27997 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d0b81b7-19fe-39db-99e5-d1e6f47c64ec | -3.11407 | -54.28464 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2affbddb-90a3-32b8-bffc-af51a7db7fa7 | -3.111 | -54.27935 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cd5e55b-f252-35b0-8e95-5536a0e88070 | -3.11025 | -54.28402 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7bd95c4-203b-34df-bbdc-9b897abb7a6f | -3.10792 | -54.27408 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9750a49b-5f78-3646-938f-e3557215f62e | -3.10718 | -54.27874 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fadaaaed-891f-3182-a83c-08eda75ead49 | -3.10643 | -54.28341 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0d4ee42f-dfe5-3ea8-893d-f4c437ca3e40 | -3.10411 | -54.27346 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 63d6c201-a95c-3225-9478-af2a7482a64b | -3.10393 | -53.71759 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09ac5cf2-daf0-3f4d-8c75-3c0ed043be8b | -3.10336 | -54.27813 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3f0a44b2-f3f0-3a1d-9186-73863a5f99d4 | -3.10262 | -54.2828 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1d672843-3482-3024-b9fd-0b03bced3e6a | -3.10187 | -54.28747 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9703610f-6a6f-3580-ac2c-3ca960e5c946 | -3.10029 | -54.27288 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8140df31-4302-30a2-aa8b-9bc34851923f | -3.10023 | -53.717 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 499248d2-7a5d-3dc2-97a8-478634ccd803 | -3.09955 | -54.27754 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 526edda9-9c65-3be2-80b7-fe4266f4e3d5 | -3.09954 | -53.72135 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3af63d68-2283-386b-8eef-8051103f0066 | -3.0988 | -54.2822 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ac4efc90-fcb2-3823-a2b4-cad58e670311 | -3.09805 | -54.28686 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7ef010b-f580-3988-bf47-20ea7c477dcb | -3.09673 | -53.81114 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 535ed61a-9444-3dc9-935a-2e15826dbe7e | -3.09654 | -53.7164 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04d8d1cd-8dff-3afa-81fc-223d1d78883b | -3.09585 | -53.72076 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09ba370d-3502-32e3-a53d-526ffabee63b | -3.09498 | -54.28159 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7e6c3167-0dbf-38f4-aae2-9d8327a9f8df | -3.09424 | -54.28624 | 2024-10-30 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a134efe0-e5ca-3247-bcff-bfc04a5c25e9 | -3.09373 | -53.80605 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a321549c-6715-3bcb-9ad8-2ed6bb9eba29 | -3.09302 | -53.81054 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 102630d6-cf66-3953-a37e-df96fcf6c251 | -3.09284 | -53.71581 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6773f6ce-df47-38a3-a534-55881bca4840 | -3.09231 | -53.81501 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7fad42f0-9a1e-37df-b83c-03eecda706bf | -3.08859 | -53.81442 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72e9cd28-6d67-302d-8a94-510abf7d5c89 | -3.46023 | -54.07547 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a581496c-7765-3112-99d0-28d7067677ba | -3.45951 | -54.08001 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47b55a2c-a056-3fc1-9dd3-47e236ddc0c2 | -3.45648 | -54.07488 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99ed2b8c-bf11-3746-9d38-da58cbba4076 | -3.45576 | -54.07939 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5331c582-9a78-3631-b22e-7888b204f549 | -3.45503 | -54.08394 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe83db29-08e6-39c5-b12a-e002fae5e4ee | -3.45272 | -54.0743 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 241a03a2-18fd-3b9a-befa-e3323039ad98 | -3.452 | -54.0788 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c31ec0fb-a455-3fdc-9384-0590fb8d48ee | -3.45127 | -54.08332 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8583f9fd-6387-3b59-878b-9a8ed3e8290e | -3.42527 | -54.14894 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ff51752-f746-3d17-87ba-c804eb7dcab5 | -3.42453 | -54.15352 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f53fccce-6de9-3b18-8a2a-bfff78b25575 | -3.42076 | -54.15287 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 363c97e9-186f-33eb-947f-860248d678f7 | -3.27141 | -54.17146 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80a5a270-d24c-32bf-86c9-7c1cf3148eac | -3.27031 | -54.17337 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62556541-a3d5-3f38-856f-b951ffea6f61 | -3.26578 | -54.17728 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79efbf7a-5556-32e9-a487-5fbfbc836c1d | -3.25863 | -54.17865 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35dbe200-92da-317b-82b9-92f83ccdd546 | -3.25822 | -54.17603 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fef5586e-e5e1-3fde-abb7-87424a2b165e | -3.20931 | -53.85383 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9705c673-9ffe-3190-a3fa-92eac078d420 | -3.2073 | -53.85243 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 556a1bf1-bffe-3869-88ab-fc8e0dbbba27 | -3.72614 | -54.6428 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cb9305b-076d-320f-84da-1116466f701c | -3.69691 | -54.06767 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a809c04-9210-3bcd-bae0-daed3642b965 | -3.68453 | -54.21833 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88592263-6a01-3749-8ac8-9eb1c7aadd30 | -3.68435 | -54.21663 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e19f71b3-145e-353c-a974-5f7bf47f76d4 | -3.68076 | -54.21769 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ff7767e-81c8-3c77-9078-e289f7216c30 | -3.67302 | -54.31544 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9217eb64-39bc-32cd-8412-d60704421e88 | -3.66687 | -54.30515 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b85cfed-e8d4-3db9-817f-3cbea6b3d07d | -3.66615 | -54.30968 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef0051fa-4632-361f-b520-974309816e74 | -3.66307 | -54.30459 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46539def-3ac2-3b06-a87f-f6f05d89eb07 | -4.14702 | -55.33254 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 79a5e9b1-9014-30ba-a3df-f4d61a87388e | -4.14646 | -55.33606 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35666407-ce48-3f4a-95f9-9be202cb98ed | -4.14301 | -55.33188 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 743bc3c6-1971-38e0-ae07-d72f45f344dd | -4.10649 | -53.94971 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a46cf96-c141-3707-a0ec-b331c7fc1970 | -4.10578 | -53.95408 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fc551ba-2350-362d-9f69-9aa359febc37 | -4.1042 | -53.9404 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5ec7f15-c9c1-37fc-b268-f276ff3ea96e | -4.10351 | -53.94466 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc6883d9-a521-32f5-bd33-aa479268638b | -4.10281 | -53.94902 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0379089-66b4-3679-ae7f-0557304ae6e4 | -4.1021 | -53.9534 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f421ffa-7bd9-3bb9-92a3-596c7fe89b68 | -4.09983 | -53.94401 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d703b1cb-3e81-3d73-8794-14e789e508d8 | -4.09823 | -53.93056 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f43366b5-94be-3f1a-894e-bf67ebf9d6b7 | -4.09314 | -53.93852 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dd2630b-15c9-3fe0-952b-c30f2fb0e094 | -3.96998 | -54.14685 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6feb5de-0a9b-3865-8642-dc126d1ecc44 | -3.96924 | -54.15144 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dae2f80d-5326-376f-ae66-0f33bca71d75 | -3.96624 | -54.14624 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6595a658-15d8-349b-8880-75de081b63e6 | -3.96551 | -54.15076 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9f59318-fc24-33e2-bcd3-5be18228b3ae | -3.95579 | -53.99919 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa93cbe-0af6-3cf2-a5bc-a88b5a54b2e1 | -3.95515 | -54.75893 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 954ae979-a202-3fde-87c1-eb9e4f38ed7e | -3.95127 | -54.75829 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cbe7292-4caa-3e5c-86bf-9528f29aeb02 | -3.73001 | -54.64342 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6f4e573-f315-3f4d-9b1d-6a9fb5982c98 | -3.66917 | -54.30841 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e8c6d9b-2232-3bd6-bf4d-cb6222974b26 | -3.66235 | -54.30909 | 2024-10-30 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb218c06-410a-30a8-aaf5-b6798b4b74fa | -4.50899 | -55.45858 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52cf3a73-bbc2-3229-82fc-4871de8d7722 | -4.50554 | -55.45444 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1ca93ce-1f27-3abd-9900-e2ad449604e7 | -4.50497 | -55.45789 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14faa03b-1ab2-3bd3-b401-dbc4b2e115d2 | -4.40705 | -55.10809 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README69.md)
