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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24bfdb4d-c350-32ce-8a1a-509392d469b7 | 3.1275 | -60.8026 | 2026-03-15 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 238.3 |
| 655ef2aa-b7ab-39aa-904b-46353c2ab9ec | 3.1093 | -60.784 | 2026-03-15 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e340e711-19c5-34cc-a30c-47edd28e6fe6 | -11.9512 | -41.3251 | 2026-03-15 00:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 89.5 |
| da543970-d5d3-3513-b3b3-c7fccb053934 | 3.1093 | -60.8029 | 2026-03-15 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 68ff5b26-c990-3aea-89fd-25b245f131bd | -11.9517 | -41.3005 | 2026-03-15 00:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 56.7 |
| d5267d59-fde1-311f-b8df-2d95ef269f66 | 3.1276 | -60.7836 | 2026-03-15 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 51c6c72d-4cc4-32c4-a0c9-0e087959f4d5 | -11.9517 | -41.3005 | 2026-03-15 00:10:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 53.7 |
| 1302be3c-691f-346f-b173-0d338e15ee4c | 3.1276 | -60.7836 | 2026-03-15 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 8d297b9a-3c98-3d8c-850c-f3a5e0493737 | 3.1093 | -60.784 | 2026-03-15 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| ccc7ba4e-9eef-32c3-8815-e4e7a592037c | -11.9512 | -41.3251 | 2026-03-15 00:10:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 024d1fb0-739f-34c3-9aeb-f15dd7f7e892 | 3.1093 | -60.8029 | 2026-03-15 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e3b7eea5-b33b-36c2-a47e-6428d6aaa5d5 | 3.1275 | -60.8026 | 2026-03-15 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 184.4 |
| e6ceeb08-4ad1-3cc8-8b81-759de146541b | 3.1276 | -60.7836 | 2026-03-15 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 111.5 |
| f494c850-d276-3a40-9256-9e5bf94a6254 | 3.1093 | -60.784 | 2026-03-15 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 53cd4188-3aa0-3511-801f-d0cc17864f98 | 3.1275 | -60.8026 | 2026-03-15 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 116.2 |
| d4ab824c-8c38-3776-b2c1-db84f8d100ff | -11.9512 | -41.3251 | 2026-03-15 00:20:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 15cf2d3e-dcc9-32c7-8409-9e8256eb24bb | 3.1093 | -60.8029 | 2026-03-15 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.5 |
| b46a71b4-a589-3956-aa2e-0b2576925b97 | -10.0651 | -36.29 | 2026-03-15 00:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 99.4 |
| f519302e-7342-3047-94ba-c0eaa64256c3 | -10.0458 | -36.2935 | 2026-03-15 00:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 138.8 |
| 42041011-3816-3d11-8e1d-10b775fb6fef | 3.1276 | -60.7836 | 2026-03-15 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 90.8 |
| e42a08d1-8960-325d-9e99-0eeeb3b002ac | 3.1275 | -60.8026 | 2026-03-15 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 9e044578-e61c-3ed0-a2fa-21131d548a13 | -10.0453 | -36.3205 | 2026-03-15 00:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 54.5 |
| 68fc3388-f619-3b7c-b015-634b48eecaad | -11.9512 | -41.3251 | 2026-03-15 00:30:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 763bec38-f1f4-3901-b608-761f5d1e9203 | 3.1093 | -60.8029 | 2026-03-15 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b688846c-ac37-3c3c-a172-717347773a4d | 3.1093 | -60.784 | 2026-03-15 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6cf488f8-324b-31b9-8d0a-f4f973894c83 | -10.0578 | -36.294201 | 2026-03-15 00:34:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 329e9062-3667-3e8b-ac92-f394056ee7f6 | -10.0482 | -36.2967 | 2026-03-15 00:34:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 89297700-cdb4-38c9-b703-5a4646604551 | -10.0523 | -36.272999 | 2026-03-15 00:34:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 86967dab-376c-32ae-a10d-8e247d883f05 | -10.0633 | -36.315201 | 2026-03-15 00:34:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 1063f4a8-810c-37e9-ae1f-cd3f46ad07d9 | -11.9537 | -41.3312 | 2026-03-15 00:34:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b386148e-10a7-3b67-bfb5-d99c072e2a6d | -11.9492 | -41.3125 | 2026-03-15 00:34:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bf719bfd-af9c-3bd5-a0f0-571feb46e8d4 | -11.9394 | -41.314899 | 2026-03-15 00:34:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 25964947-5f14-39e0-84ac-9d0b48b187a2 | -11.9514 | -41.321899 | 2026-03-15 00:34:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 35e44b1a-6dd7-33ca-bbbd-f586d83d2ab4 | -11.7867 | -47.091599 | 2026-03-15 00:34:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f446ad9-6cef-38cd-8b92-8adc5a7d07ca | -11.9439 | -41.333599 | 2026-03-15 00:34:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 52f07db7-8b4b-33a7-b642-59ec39ca07f6 | -11.9416 | -41.324299 | 2026-03-15 00:34:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 58ee100a-3537-360d-9ff8-dc6e68713cb1 | -12.6601 | -47.090302 | 2026-03-15 00:34:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9022189b-265a-3cda-8396-ab9454243cf3 | -8.7976 | -44.808201 | 2026-03-15 00:34:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2cb7aaf-281f-3d3e-99f5-46da90c06c12 | -8.8074 | -44.805901 | 2026-03-15 00:34:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 01d82c05-34b0-3370-a11d-bd0d01c27d89 | -8.7959 | -44.800999 | 2026-03-15 00:34:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 606546a5-5dbf-3d98-8c54-4fafab06233a | 3.1275 | -60.8026 | 2026-03-15 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c9fcfdad-289f-3f99-b6f6-c8e4552ba367 | 3.1276 | -60.7836 | 2026-03-15 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 548e792f-83c2-35ad-bcc3-fde81d85d13d | -11.9512 | -41.3251 | 2026-03-15 00:40:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 04aea1e2-c16e-3121-8b39-7242bed18092 | -11.9517 | -41.3005 | 2026-03-15 00:40:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 52.2 |
| e9e53cc6-e606-376e-9bd1-dd298e276471 | 3.1093 | -60.784 | 2026-03-15 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ff442d3d-055e-3c6a-9b62-96f838377ae5 | 3.1093 | -60.8029 | 2026-03-15 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 650c5aa5-139b-356a-be22-132d0ee1ec24 | -10.0662 | -36.2359 | 2026-03-15 00:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| e27678ff-3aef-3fb0-9b9b-83311cef5a5f | 3.1276 | -60.7836 | 2026-03-15 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7886ce06-0366-3995-a552-a99039048c7d | 3.1093 | -60.8029 | 2026-03-15 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 4d34dfdd-3544-3f26-9ac0-7fc985dd6def | 3.1275 | -60.8026 | 2026-03-15 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 8f4f8525-355a-33b3-98c3-4904058250df | -11.9517 | -41.3005 | 2026-03-15 00:50:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 43.1 |
| 07ff0869-3feb-319b-8e7f-113fe21431a6 | 3.1093 | -60.784 | 2026-03-15 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 4fc053ae-f9a3-3656-a89e-ba84c0b68120 | -11.9512 | -41.3251 | 2026-03-15 00:50:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 66ce3c83-df47-3ca2-85e0-1e192132e055 | 3.1276 | -60.7836 | 2026-03-15 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 8946917b-6818-3a30-9b75-b7356b5da5de | -10.0855 | -36.2324 | 2026-03-15 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| b700c7bb-58db-37bb-8f20-7608999e153b | -10.0662 | -36.2359 | 2026-03-15 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 198.2 |
| 70b91906-031a-38fd-a151-8a9499446e4c | -11.9512 | -41.3251 | 2026-03-15 01:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 2472d21d-8f45-3083-a13d-d9188fa454b8 | -9.9884 | -36.2768 | 2026-03-15 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 51.9 |
| 8403d29e-9c99-30fd-946a-9ecd68e1c305 | 3.1275 | -60.8026 | 2026-03-15 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 89.2 |
| f9b41fa6-1607-3c65-b2ab-a0f985d76d3a | -10.0667 | -36.2088 | 2026-03-15 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 115.5 |
| 056bfaa0-df71-3a71-a855-50699cc1bf49 | -19.87639 | -55.55214 | 2026-03-15 01:00:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3a670228-4c09-3aee-b398-fd8fe9a034da | 1.09618 | -59.58129 | 2026-03-15 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf115533-f0d6-3ae6-8c3e-887bf7067648 | 0.94583 | -60.39951 | 2026-03-15 01:05:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3edadc17-009d-3077-801b-1bd6b86885cd | 0.90579 | -60.29135 | 2026-03-15 01:05:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 5c2eb8ee-62d5-3c7a-a7c4-62bdead4be6b | 1.65113 | -60.29788 | 2026-03-15 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a039a5d1-d54d-3255-ab2f-410f327785a7 | 1.11312 | -60.38685 | 2026-03-15 01:05:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 81076568-b50d-3019-a763-4378d203a84a | 0.90448 | -60.30083 | 2026-03-15 01:05:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 92a19c77-28b7-33c4-8d5f-0b2bd0fa1875 | 0.91363 | -60.30213 | 2026-03-15 01:05:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e5cc003d-b136-37c8-9b3f-5e1c61c4ed5b | 1.17461 | -60.00314 | 2026-03-15 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 660dfc85-c369-38d5-b8c0-a89accc6374b | 3.12897 | -60.80157 | 2026-03-15 01:07:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 16.6 |
| e1044693-0d34-3a18-8101-fdf5308657a2 | 3.18588 | -60.24489 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d85e3b64-00d9-375f-8a3b-c35a05aab130 | 1.88033 | -60.43635 | 2026-03-15 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 54c997d5-bbb4-3aa7-856e-3fb513aa5040 | 2.5427 | -60.91244 | 2026-03-15 01:07:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f252bb55-cd24-38ae-aa49-ff000c390b9b | 1.93553 | -60.37571 | 2026-03-15 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 829aa849-3ade-3743-a86a-306b722c5092 | 3.13026 | -60.79211 | 2026-03-15 01:07:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 32294370-b7ac-3bc9-aa81-ce26c49af62e | 2.10708 | -60.19423 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 60ab7d4d-8faf-3652-a062-bcf5dd2acc64 | 3.53596 | -60.37855 | 2026-03-15 01:07:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0e42516c-67ba-325a-9dca-21a09e2ef3df | 2.9488 | -60.37539 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b81f9bef-53c7-3f60-97a7-6e608c754123 | 3.12242 | -60.78136 | 2026-03-15 01:07:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 64121d82-0620-3eef-b55a-78cc6adb7ee6 | 3.00043 | -61.33339 | 2026-03-15 01:07:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a2402b8-9abc-3282-8037-e273fa8e7525 | 3.12113 | -60.79084 | 2026-03-15 01:07:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 620ca797-e2b1-3424-b4d2-ebace31f173f | 3.13652 | -60.46977 | 2026-03-15 01:07:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a558d412-c5f6-34c3-98d8-d50889b6a7a5 | 2.07645 | -60.68755 | 2026-03-15 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8ab932e4-da7d-3464-920c-5c125330b678 | 3.11984 | -60.8003 | 2026-03-15 01:07:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 241b06e3-1cd3-35c1-926e-8d370bbed88c | 3.15714 | -60.13174 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a1e84012-3555-315e-b067-79538b8be6b9 | 1.87115 | -60.43506 | 2026-03-15 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2ae3e964-c103-3668-99ca-67eda50c40b6 | 1.88163 | -60.42682 | 2026-03-15 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 15608d0b-a794-3a5f-91e8-83cfac6ce546 | 1.98368 | -60.89215 | 2026-03-15 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 10ec14ad-39ce-37c2-b592-66484fafb921 | 3.1477 | -60.13043 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 539818fe-6491-3497-bc54-1fcda917cdde | 3.17649 | -60.24358 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 27.4 |
| ab74adab-7f8f-30bd-a469-027d97ac9b73 | 3.19905 | -60.3582 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 4299ec05-2a4c-315d-87cb-04bb6542ab46 | 2.94744 | -60.38519 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 74c2ef47-4092-34df-802a-009a1c2629ce | 1.95822 | -60.60745 | 2026-03-15 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| db8aba96-b259-3c05-a556-32089fce5d7f | 3.17784 | -60.23357 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5d8baa67-ab66-3b9e-8aa2-d3317ec12a8e | 3.14351 | -60.16088 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0b1c177a-f3c1-325a-a580-edb4eafc3854 | 3.14491 | -60.15073 | 2026-03-15 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| dc59de10-3849-3cca-aede-5d08f52f44fc | 3.4145 | -60.66461 | 2026-03-15 01:07:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e5c87665-6558-3174-a25d-1f8e95247c09 | -11.9512 | -41.3251 | 2026-03-15 01:10:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 892aa9b4-7433-310c-bcdb-9fdeab994465 | 3.1276 | -60.7836 | 2026-03-15 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| cb20e8d5-eaf3-378c-8f47-39438dcf748e | 3.1093 | -60.784 | 2026-03-15 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |


[Clique aqui para ver as próximas entradas](README2.md)
