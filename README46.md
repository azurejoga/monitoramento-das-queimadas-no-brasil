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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87471f89-77cb-32fa-98ae-89fde7966c6b | -20.32977 | -51.70624 | 2025-08-19 04:57:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c6d7827-6efb-30e0-9375-486189f0ba94 | -21.87931 | -48.19426 | 2025-08-19 04:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2356c97d-adae-3cef-ae08-1449db755f6e | -21.23599 | -49.08275 | 2025-08-19 04:57:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8f21f38a-f661-3c06-bc5e-8f21293ea5cb | -21.8736 | -48.20897 | 2025-08-19 04:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38941515-8c84-391b-a2c1-df026b7aad07 | -21.8734 | -48.20419 | 2025-08-19 04:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fe9d3ad-d162-3895-ab63-f03f94c9ae62 | -21.40484 | -45.00836 | 2025-08-19 04:57:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 19858c25-c141-37a8-8dd0-147ba99dc187 | -21.39858 | -45.01228 | 2025-08-19 04:57:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 33a85b27-528e-3fd8-8f5e-55f6d38db48f | -20.86394 | -56.91478 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 514f4053-9828-3145-8a3f-4fd6923e1442 | -21.13083 | -47.03893 | 2025-08-19 04:57:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57aea881-cb97-3710-a1a6-fff2037c0dde | -21.87486 | -48.19792 | 2025-08-19 04:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dde0aaf-6688-3e46-a5a9-7ef6a09e8e33 | -20.87066 | -56.91595 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27e2fac0-481a-313c-ba1a-f304310a14f3 | -20.8719 | -56.90832 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2ef1682-6a5e-36a0-af7f-4c8d3f5a0614 | -20.91729 | -57.60636 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e54e9d9f-9a46-331b-9cad-b277ad707286 | -23.20457 | -55.44938 | 2025-08-19 04:57:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ead3919a-6c70-3273-a0f6-be0d26765dd9 | -20.85899 | -56.94508 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5153046-dbd0-39b6-8a53-fefa8fd3378b | -21.23792 | -49.08526 | 2025-08-19 04:57:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d0cccbe3-f95e-3c7c-9d66-eab150d3e645 | -21.87872 | -48.19981 | 2025-08-19 04:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe158f85-9e28-36d2-aa1c-c01d67e16e00 | -24.24061 | -54.03108 | 2025-08-19 04:57:00 | NPP-375D | TERRA ROXA | PARANÁ | Brasil | 4127403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a8fc4a8c-17c6-37c3-9e08-f101e5a1a442 | -21.2385 | -49.08046 | 2025-08-19 04:57:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 00f58541-c691-3cd8-b12a-9df482bb2231 | -21.02953 | -56.88963 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0be790a4-6e32-30f8-9033-f121da9d4852 | -20.8663 | -54.97765 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f51f7afb-8a31-3f6d-8fd8-7a5698ca82bb | -21.19076 | -45.11089 | 2025-08-19 04:57:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aafd2682-6d33-3f3f-bc59-0ea8458e4f8f | -20.54761 | -57.39186 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e042013c-3f16-3be8-abc6-e6fc2989957b | -21.88943 | -48.19039 | 2025-08-19 04:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f195b082-30c5-3a00-bb2d-328cafcb8ab8 | -20.85686 | -56.93689 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7665592d-c0c5-35e7-b1a8-fb5841fd27fd | -23.57395 | -51.6378 | 2025-08-19 04:57:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 53.4 |
| 74212d94-2642-3e56-be25-b3f2a58383d7 | -21.13392 | -47.03954 | 2025-08-19 04:57:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 614b2dd6-d0f1-3e60-84b4-50cd992bf4ba | -20.6316 | -57.3271 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a450fac-ad10-3038-92b3-f53fb1255ac6 | -20.8802 | -54.98783 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbf9c0b0-53bc-39fd-8de8-555ee8c743f7 | -20.83251 | -57.73651 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ce75b7d5-a909-3987-9f53-269c36f8261d | -20.84379 | -56.91109 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fcd8657-9199-3708-bb06-ca729c294c97 | -20.84838 | -56.90416 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82030b1d-0b97-34c5-a800-5aa0d659740f | -20.8703 | -56.93933 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef589aa7-9ed7-3b3e-a4bd-333451440089 | -20.86688 | -54.97389 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa7af575-e8ef-3d5f-842a-a94386c406d3 | -21.31932 | -48.67199 | 2025-08-19 04:57:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c7311391-0551-3201-ad7a-28ba6e5a7b9c | -20.33353 | -51.70684 | 2025-08-19 04:57:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| da96fed3-2cc2-3e9a-9317-44eda4dc31cc | -20.55131 | -54.57838 | 2025-08-19 04:57:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57a05c03-65d2-30a8-a7fa-4a840cbda6c5 | -20.87964 | -54.99156 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bac4600-fd76-3655-b676-e17c49cc7ea2 | -21.39312 | -45.00768 | 2025-08-19 04:57:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 80d6f068-7227-3db7-bd4a-2fb24f9148ad | -20.86366 | -56.89527 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 91c5512a-ae46-3d22-aece-f836531f62bb | -20.88191 | -54.97659 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21ee9a7d-95d8-30fa-9ee8-c9f2a93e9865 | -23.06401 | -55.17735 | 2025-08-19 04:57:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 73e86762-cdb9-32aa-818f-9161f80c9db6 | -20.87128 | -56.91213 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aad4fbe-df53-302a-b805-1c0c69be3cd4 | -20.86794 | -54.978 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8b551db-96bc-3227-85a9-1c89339476de | -20.87072 | -54.98238 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fa42dc0-63b7-3f9e-87ae-dc969f25836b | -20.86792 | -56.91154 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 641c7f9d-ca87-3f93-83e4-f2569f041a33 | -20.86518 | -56.90717 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbdf9d25-1559-3449-bb3d-7e1c8b1d7c8b | -20.85798 | -54.96464 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0db8ce27-ae04-31c0-b3fa-f87222b190e5 | -20.91882 | -56.8814 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0fed97d-6b53-3679-a3bc-d84fa5d4f097 | -20.86358 | -56.93811 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e67045b-a691-3f48-b059-d1a58f291648 | -20.86737 | -54.98176 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d89be536-d337-3572-847f-d3d31e6deae7 | -21.39938 | -45.00366 | 2025-08-19 04:57:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| a7cbcf32-ac93-3d2a-883d-5365bfda3bab | -21.38306 | -45.76756 | 2025-08-19 04:57:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 39896ccb-d793-3ace-b591-23ddd7bedbc9 | -20.29765 | -50.95892 | 2025-08-19 04:57:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f20333f8-313b-38b9-aee9-64ee2794c0fd | -20.86132 | -54.96524 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31149ca0-cf93-301c-b28d-26815899256e | -23.57788 | -51.6384 | 2025-08-19 04:57:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 53.4 |
| aa0cdceb-a3cd-360b-9b4a-1d990b4a2cc7 | -24.29124 | -50.82662 | 2025-08-19 04:57:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e39463b6-788d-3657-8874-2dced621acb7 | -20.8673 | -56.91536 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7c66323-b323-359b-8910-4c6fa1deb9ee | -20.87691 | -54.96424 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7560a29-b356-336c-9246-8be79149c3b2 | -20.8535 | -56.93628 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 550bcb7d-d10b-3933-8082-7326c8149bb7 | -23.5786 | -51.63282 | 2025-08-19 04:57:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fa43b2de-5e0e-3d12-b9d5-92a749324708 | -21.24046 | -49.08348 | 2025-08-19 04:57:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f2472273-2eec-3e2b-90d8-5a36029fcb86 | -21.39899 | -45.00794 | 2025-08-19 04:57:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a4337366-b0e7-3783-9177-2282d09a1bc0 | -21.37747 | -45.76723 | 2025-08-19 04:57:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 46a40b79-4516-338b-b73c-56686e78712e | -21.87424 | -48.20336 | 2025-08-19 04:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 708842b5-cb00-372f-8a55-fd9e50e95080 | -20.98738 | -56.90577 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 439c10e2-0414-3cdb-a991-38347029bf6f | -21.23404 | -49.07973 | 2025-08-19 04:57:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ffff7551-ccb3-37c2-8600-a2bc8f5b754f | -20.87685 | -54.98727 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 881e1127-6f64-3379-b96e-0683bd3895dc | -24.29075 | -50.83072 | 2025-08-19 04:57:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 27852e58-dfd5-3b16-9657-750800e1d5c2 | -20.85386 | -56.91296 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 546c6824-743d-3ba5-8f49-379db9eaa628 | -20.88078 | -54.98408 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 732b54c8-4fb7-393e-ade6-5e3047d2b4fb | -20.84318 | -56.91486 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebe6bb57-92fd-3acf-92be-4596dcc6d266 | -21.38219 | -45.7659 | 2025-08-19 04:57:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 55fd8e39-d558-38f7-a8ad-d895032d14bd | -6.9715 | -43.5833 | 2025-08-19 05:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 5bbb1ae2-f70a-39cf-942d-4f9f97cbeaf3 | -6.9339 | -43.5868 | 2025-08-19 05:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 088db7b1-a6aa-31ff-a0fd-f8fe0705aebe | -6.9527 | -43.585 | 2025-08-19 05:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e229fa0e-b517-370a-9c87-aaf97211d18c | -6.9715 | -43.5833 | 2025-08-19 05:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 48eabec7-bbe4-3303-8ada-8da6d0a85c85 | -6.9527 | -43.585 | 2025-08-19 05:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 1c501de8-e89f-33d7-b412-155fb5b2b987 | -6.9339 | -43.5868 | 2025-08-19 05:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 746c4d73-a950-3cd9-a4f6-b9ea2139963c | -5.7887 | -43.6134 | 2025-08-19 05:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b0c2bb7c-5a25-3823-afa8-70ddbc3eb578 | -13.1555 | -54.9357 | 2025-08-19 05:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 367e8bfb-b983-34b0-9ca9-d880021eae04 | -2.90241 | -48.29286 | 2025-08-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad825342-98a2-30c5-9598-ec3dead599fd | -2.54457 | -47.72047 | 2025-08-19 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa0e0f99-41ef-30fa-9fc2-d79fb5d510fd | -3.13099 | -48.98487 | 2025-08-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9549ed8-409b-3782-973c-26eea7a2146e | 2.46472 | -51.24283 | 2025-08-19 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe6c6534-debb-3696-8c37-02c92efe8393 | -2.53806 | -47.724 | 2025-08-19 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2937aa05-43a8-37ab-b01b-8b66f8fba6cd | -2.90688 | -48.30137 | 2025-08-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c64e439-d89e-3f24-8c68-bdb0c25b0a7d | -2.9047 | -48.29911 | 2025-08-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5fc661a-d00d-3e57-9d7e-b2e1a0c104b6 | -3.08232 | -48.85351 | 2025-08-19 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f91ea36-65ff-3f34-a0b7-c0cffb9a33de | -2.5387 | -47.71984 | 2025-08-19 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bed1c8f-5232-308f-a340-62ffa546ccaf | -2.90182 | -48.2967 | 2025-08-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2be283ae-21ae-3e2e-8cd0-2023e3fc93e0 | 0.96737 | -60.41198 | 2025-08-19 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 733d69e2-8b9a-3ec3-a422-11a7ff8a0e98 | -2.90527 | -48.29527 | 2025-08-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6633e382-ff9a-30ae-b086-4451bcfaa35a | -2.90747 | -48.29751 | 2025-08-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90f10278-f70b-3fdb-b7af-71e9a4d573b7 | -3.13047 | -48.98838 | 2025-08-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8580346a-8a64-3d00-80a4-4aed599c329b | -2.54394 | -47.72456 | 2025-08-19 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ff68fe1-364f-371c-817f-8a9b5c481ee9 | -3.08777 | -48.85434 | 2025-08-19 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40bf91bb-f957-3fa6-a54c-8730b588bff4 | -2.90806 | -48.29367 | 2025-08-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76edd58b-ee74-3286-ad1e-926d1632860e | -6.19043 | -53.51664 | 2025-08-19 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4823d9d4-9409-378f-a5b7-692a6197c182 | -3.48769 | -48.4398 | 2025-08-19 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README47.md)
