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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f94ce14c-5d02-38ed-84c9-8c2ed4747da3 | -12.27151 | -44.60823 | 2025-06-14 03:51:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8dc4adc2-67af-3097-843b-f3cc547b0483 | -10.65393 | -44.49268 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 35c83835-9798-3418-8da2-b6c85c5f1a89 | -9.71492 | -48.62059 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4792f81-c43a-37a3-a725-13e1a37c0e07 | -8.92801 | -49.85396 | 2025-06-14 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cf48e6b-c93b-3aef-82ed-98615e3773b2 | -10.65103 | -44.48283 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71fe41ed-8621-315e-a30d-eaf816e380a5 | -10.65497 | -44.49532 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| def0b94e-e019-3278-99b6-6370a2ec0a8f | -9.39924 | -48.42562 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 909177b4-6ae8-30de-8995-226518708941 | -10.41168 | -46.68327 | 2025-06-14 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4476e8c-6314-35b3-b757-d10c77384759 | -9.52954 | -46.29973 | 2025-06-14 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bea88410-e413-3819-b29b-f6e90e926aac | -12.68167 | -52.40088 | 2025-06-14 03:51:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 083e7c49-a00b-34c4-999c-58aa8a3f9c7f | -10.52384 | -47.58784 | 2025-06-14 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4f33b5a-6941-3ba1-92dc-067f2941af12 | -9.40092 | -48.41695 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b6a79afa-3667-36b9-9840-b688238c813c | -14.5381 | -46.03107 | 2025-06-14 03:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f58946a-de87-3f55-ac6d-7ebe1cc606c5 | -10.20547 | -47.62201 | 2025-06-14 03:51:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02f8aef2-0b37-3255-b5fa-434703ad8a6c | -11.89768 | -47.4611 | 2025-06-14 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4163df9-eb1f-3305-bcf7-8a9e8075404f | -15.38787 | -47.86168 | 2025-06-14 03:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f75bc034-95c9-30eb-ae38-2e0ec9288c6a | -16.19278 | -46.46643 | 2025-06-14 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 027e899f-5dff-3fbb-bef3-1d63a558a26d | -15.37564 | -47.86919 | 2025-06-14 03:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17415b01-56d1-3145-a0dd-0bd51968a758 | -12.68582 | -52.40368 | 2025-06-14 03:51:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef2fb25f-a509-3317-92a3-a8a6162d8029 | -9.40174 | -48.4127 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18f13340-f463-3684-a77e-d805454a1255 | -12.10794 | -48.87421 | 2025-06-14 03:51:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0e67501b-c58c-3fed-8709-a140fce5e023 | -11.89234 | -47.45996 | 2025-06-14 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d543f0d2-93c6-351e-855e-9143b91b896c | -15.99612 | -49.82288 | 2025-06-14 03:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee32896c-eaeb-3d18-9beb-fcae05e33eb0 | -13.03422 | -44.11575 | 2025-06-14 03:51:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cf3ab5a-df54-3955-a89b-eb368b67a3f5 | -12.59849 | -47.07119 | 2025-06-14 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27c02787-ab79-34a9-8e92-ff185e9684ab | -10.65473 | -44.48816 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 37ae0c5d-d3c1-34a5-b3d7-41af71c5c067 | -10.20473 | -47.62585 | 2025-06-14 03:51:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12ba5ffe-15c5-3a2b-a80e-d56cc02f4180 | -9.40519 | -48.42673 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d3429d0-eaf6-3c42-b7be-dcf3b294eb1a | -9.40417 | -48.42068 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0217e53-e6a4-30e2-ae79-bbc54c016512 | -15.91298 | -42.65662 | 2025-06-14 03:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6ae5e932-e842-303b-8ac4-8fbb31f0dc0b | -9.4093 | -48.42627 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0cfd787-bca4-3756-b43a-de3a89322575 | -15.38145 | -47.86699 | 2025-06-14 03:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05125d5b-f5ac-3145-b5c1-a41a23610641 | -10.64944 | -44.49185 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc124ffb-a9db-3fbc-adfc-0ee8ef8d62df | -8.92065 | -49.84645 | 2025-06-14 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a4efa16-7fd0-3275-8895-b4b0654bc991 | -12.11248 | -48.87255 | 2025-06-14 03:51:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1094409-7be4-3f60-94e7-354a3367b5f0 | -11.04247 | -41.09056 | 2025-06-14 03:51:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0697d335-c2c9-3fc1-b4f2-2e56925b3351 | -10.56043 | -52.01644 | 2025-06-14 03:51:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dfef6c4c-f949-3bb8-b8c5-350163d74b79 | -11.02324 | -45.23627 | 2025-06-14 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03382d8a-fb8d-3fca-8318-2a1c5927a016 | -9.39838 | -48.43005 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58d87ea1-d70e-37cc-9b25-e13c2b60718e | -16.19645 | -46.47241 | 2025-06-14 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4a07bbd7-6705-37b3-8b61-52c5d4ba8266 | -15.39223 | -47.89387 | 2025-06-14 03:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58d6e392-0ad3-3f52-8543-01c1e8e2a579 | -12.68726 | -52.39687 | 2025-06-14 03:51:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f64dd4f4-5a1f-390e-b737-4037c9f52a43 | -9.40848 | -48.43064 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9f08b41-bd68-3c93-b1ed-c89d1bfdab82 | -9.5347 | -46.30075 | 2025-06-14 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4e283fd-6195-3a25-8376-51c6f71def55 | -14.67122 | -53.38674 | 2025-06-14 03:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ae2a7d87-06c7-3e33-82e8-d30059dbe576 | -10.81207 | -44.35255 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 554ee0e0-7cec-3850-aff9-3a4ed57b4582 | -12.68018 | -52.39529 | 2025-06-14 03:51:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0de689e-f33a-352f-8e5e-368fa76b18a7 | -15.99136 | -49.81964 | 2025-06-14 03:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b22a4ad-8f41-3be9-bcdb-b6bda02de8d6 | -10.64653 | -44.48203 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4201f9c-f839-3242-afbb-6cae0bd59b85 | -10.64574 | -44.48652 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7663891-ef14-3b7b-874e-ac2438e69877 | -9.39982 | -48.41103 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 839bdfc1-5edd-3557-b070-5abbd0e0dc8d | -12.59975 | -47.06465 | 2025-06-14 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f660cd6c-d3be-3acf-82e1-b0eb5fe44210 | -12.10665 | -48.87138 | 2025-06-14 03:51:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a66e9ec-56e0-3ce7-b39b-8a8df98f19f4 | -11.89835 | -47.45762 | 2025-06-14 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a28e5206-ef7b-39a5-9ea0-fd75dd5f93bb | -14.68189 | -53.37336 | 2025-06-14 03:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 293c010b-f220-359e-ae5f-3054390991ae | -10.65214 | -44.4855 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aaa27ca7-e8d2-3af0-a55c-77fdcef4567f | -9.40694 | -50.41651 | 2025-06-14 03:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e6b625a-8210-3a80-99c3-2ab88ca335e4 | -9.53526 | -46.29771 | 2025-06-14 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa3c584d-5556-3881-b214-24e6a3d19c9e | -8.91957 | -49.85195 | 2025-06-14 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8ae6a5c-a9a3-3e75-a5eb-351772f57029 | -9.53009 | -46.2967 | 2025-06-14 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a2b3bd7-b283-3963-a8fe-a5097dedcb20 | -10.85565 | -46.7018 | 2025-06-14 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16506d44-4d5b-3f5d-a123-e9429798b2f8 | -14.68775 | -53.37589 | 2025-06-14 03:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec79ee8e-e01b-3a04-b187-5576c0c11a37 | -8.92152 | -49.85244 | 2025-06-14 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4916f364-b18b-3891-aacf-32f21a38b7a0 | -10.84866 | -46.71045 | 2025-06-14 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2896f79-6345-3392-8720-dd9cce9763ba | -15.3976 | -47.86672 | 2025-06-14 03:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91ccd000-82ac-3202-9fed-d67c238c206a | -10.65131 | -44.49 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0433a327-f6d8-3acb-801b-eb80c7e1ba4f | -14.99352 | -41.91914 | 2025-06-14 03:51:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3af57189-fd14-3e1b-870c-9199baa3ef8f | -14.99712 | -41.9198 | 2025-06-14 03:51:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f832044-3148-3b0f-8274-79d44d2ec79a | -15.39243 | -47.86571 | 2025-06-14 03:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b9f8a54-8af6-3d60-8080-60fbabdb19ac | -14.67685 | -53.39526 | 2025-06-14 03:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed429d1d-03e5-3414-93a1-7f3af17ae1d8 | -14.6773 | -53.38869 | 2025-06-14 03:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 025619db-7655-3281-b5c2-bc2184ffdad7 | -9.71581 | -48.61602 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3107ae4-052a-3d3c-9bd3-666e1474de96 | -9.40336 | -48.42505 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b738798-67bf-3de6-82a1-2522a3f5f819 | -10.41228 | -46.68005 | 2025-06-14 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff308eb0-e05e-3494-8f60-4ecd4171b416 | -9.40497 | -48.41643 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0249050-ec44-3c7a-8a7f-fb1f33e6e702 | -12.76762 | -44.41343 | 2025-06-14 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b97c3c3-c638-334f-8c40-886743b6db4a | -16.25084 | -43.74284 | 2025-06-14 03:51:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25347a7c-dad8-31c9-99a6-b75d34bbacdd | -9.40009 | -48.42122 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3ed8adc6-d73d-37c6-97b4-1ac370311a71 | -10.52458 | -47.58405 | 2025-06-14 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26de95f5-15be-3b34-a298-05f3211109ae | -10.52476 | -47.5887 | 2025-06-14 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4e9a8c0-b1d1-3ab2-935b-daf8185834f7 | -15.99714 | -49.82083 | 2025-06-14 03:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f69b8ce9-6523-30e7-a35e-c7d5f4ac7cee | -10.52546 | -47.5849 | 2025-06-14 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4585a76-b990-303e-b3f7-61c6f07abc56 | -12.10581 | -48.87554 | 2025-06-14 03:51:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5651b4ab-d600-3358-828a-097c44a15ebd | -11.79749 | -43.78941 | 2025-06-14 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98535405-4daa-3247-9d89-ecfa895e9058 | -14.66998 | -53.3875 | 2025-06-14 03:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59f24d4b-9bb1-3655-9bc9-4f015bbd67a9 | -11.83885 | -43.80118 | 2025-06-14 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 789b363c-0353-3da9-be0d-a5d5c0b40af3 | -12.68316 | -52.39403 | 2025-06-14 03:51:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 25ef44e8-9199-38e7-8444-863b9e68dbfb | -10.6558 | -44.49082 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1311f073-ac80-3edd-9792-e0d09643b792 | -9.39658 | -48.42838 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f22f2241-3c80-3c74-8d4f-9b4a5dd00efe | -13.22673 | -49.83158 | 2025-06-14 03:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6028b4c-17be-344b-971a-4652eaa573d2 | -14.67562 | -53.39621 | 2025-06-14 03:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ead44da8-d00f-315a-bf25-c0d72e9a0f6d | -10.56751 | -52.01842 | 2025-06-14 03:51:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba644d80-fd4d-3b59-9d8d-f901d5305ed6 | -15.99626 | -49.82506 | 2025-06-14 03:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37ad437f-2481-3c6a-8e9d-8a4a8c269a4b | -13.00677 | -42.67266 | 2025-06-14 03:51:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9ad74fc9-081d-3539-8110-a9fe5884244c | -15.39292 | -47.89035 | 2025-06-14 03:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec63f6a2-56de-36c3-8248-5a27e4e0e7c4 | -14.66953 | -53.39407 | 2025-06-14 03:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ef382cc-24f0-39e6-924c-06ca78fdb9e9 | -9.40434 | -48.43112 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1a79138-66b8-3159-b598-b29e41a490b7 | -15.38725 | -47.86477 | 2025-06-14 03:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7e7f93a-2696-350b-9de4-099b9a8ec8be | -8.92605 | -49.85346 | 2025-06-14 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9890aaaf-253c-3cb6-91be-a36dcfb7dd8b | -9.40768 | -48.41385 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README11.md)
