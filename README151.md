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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d241d3f-171b-3295-ac82-a7bfba35ec4e | -2.85157 | -50.74733 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4858b6f8-76ba-3d2c-a128-5afd62578aec | -2.84802 | -50.70952 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4b190cfc-d7f1-3b4b-b5bf-d5bb4b715104 | -2.84666 | -50.71866 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 17f9a945-8ea8-339e-9cf0-b51d954c8085 | -2.8453 | -50.72778 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 7f72668d-419d-3cb7-b391-0a12ecb32001 | -2.68131 | -51.70575 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c39cf967-09ca-3724-ac01-414bbb204d4c | -4.64293 | -50.98935 | 2024-10-01 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 96478249-d2d0-3651-aa21-0758e49796d7 | -4.089 | -51.11503 | 2024-10-01 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a380c8d4-4417-37a0-a4c2-6473ac7bffd3 | -4.08765 | -51.12412 | 2024-10-01 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c92b40e1-eda4-3b3c-a858-15bb891ac38a | -3.07766 | -53.06113 | 2024-10-01 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 57870602-87d1-3a94-aede-fbc6f4e3cc06 | -2.85496 | -53.31639 | 2024-10-01 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c226325d-d0d0-39a5-ae33-d92edcb775a8 | -2.84589 | -53.31507 | 2024-10-01 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f55aa67d-e39d-35e8-8c89-660c92eb5f01 | -16.62066 | -52.58077 | 2024-10-01 05:46:00 | AQUA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 59048d37-a22d-3acd-a0df-02f7a092734d | -10.90041 | -46.34581 | 2024-10-01 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 04da7fc6-4e9b-3ee9-a369-c06843bdc961 | -11.00931 | -46.48945 | 2024-10-01 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 9d6d2f39-e25b-348a-86ff-22f55f07a6f2 | -11.00401 | -46.46227 | 2024-10-01 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| cd9b3d3b-a1ad-3597-a243-4bc44be9e69b | -11.00134 | -46.48305 | 2024-10-01 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 294.4 |
| 33351049-cab8-3fed-9e37-84b74ac5c97c | -10.99857 | -46.50454 | 2024-10-01 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 82047eea-272f-3660-9ec9-94d27c18de2d | -10.99827 | -46.46653 | 2024-10-01 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 210.6 |
| a0a4670b-3ffb-3082-a33f-5abca9a2248e | -10.99579 | -46.487 | 2024-10-01 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 9712e256-cb5e-3fb2-bff5-9944bf3fb0f1 | -10.99562 | -46.52737 | 2024-10-01 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| cea28289-fbdd-358a-a031-407627960053 | -10.99311 | -46.50917 | 2024-10-01 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| ecd6f1e3-db9b-3a8c-a59e-a67551d0626e | -10.99034 | -46.53201 | 2024-10-01 05:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 157f325f-2752-3aac-a4d2-ca24e8c90919 | -14.77735 | -48.06894 | 2024-10-01 05:46:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| afd078c9-4f87-3b0f-be60-2688c16eab6d | -10.76965 | -48.74991 | 2024-10-01 05:46:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4d6bafb7-af60-3c91-bb72-80f6242bb70f | -10.56647 | -48.0265 | 2024-10-01 05:46:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8af3a3a2-72c3-3897-b153-6eff29fe2f59 | -10.56437 | -48.04253 | 2024-10-01 05:46:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c9faf415-bcef-31ef-a068-2d0b4a51b55a | -13.50344 | -48.57584 | 2024-10-01 05:46:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| fc764ca6-981a-3b77-adad-c582fa059a91 | -13.50141 | -48.5921 | 2024-10-01 05:46:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 2294fd11-4eb6-3581-a3f9-983acd4460df | -13.46702 | -48.6165 | 2024-10-01 05:46:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 057f35c2-e284-30f5-af31-e05c3fc0505a | -13.46147 | -48.62088 | 2024-10-01 05:46:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5d4ca734-b3be-365f-901f-fd2c61f88c01 | -13.21903 | -48.55594 | 2024-10-01 05:46:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4c9c9cd0-de34-3b7f-b54d-0f99eca2372b | -13.21708 | -48.57164 | 2024-10-01 05:46:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 522e1734-1e05-3c3c-a526-f511888c1e67 | -13.2119 | -48.56425 | 2024-10-01 05:46:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5eccba64-d4e4-3f82-97e6-e40e283dfdaa | -14.74111 | -48.76236 | 2024-10-01 05:46:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 28219f9e-b3b0-3174-9cde-6fd55b09b05e | -14.73473 | -48.76635 | 2024-10-01 05:46:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| b9e78e1c-de46-3fe2-92d4-56384fbcebfe | -14.72924 | -48.75957 | 2024-10-01 05:46:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| f1587d79-649e-3400-8ec0-44e0d06f7094 | -14.72272 | -48.76462 | 2024-10-01 05:46:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 2b2568a4-fda2-302d-afaa-2b5bbe715201 | -12.2091 | -50.47127 | 2024-10-01 05:46:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0b0d5032-1770-3a62-8796-ef0035e87366 | -12.20743 | -50.48327 | 2024-10-01 05:46:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e413875a-2fad-3439-9f6a-af68730ede81 | -12.15126 | -50.06716 | 2024-10-01 05:46:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4da16c0c-138f-3d75-90fa-b94a45d8ba4f | -12.14953 | -50.07991 | 2024-10-01 05:46:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 053daaf6-eb39-3ce3-a380-5faa01e305e9 | -12.14255 | -50.05298 | 2024-10-01 05:46:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| a45b6258-b4ac-3012-8ffa-b43514b96662 | -12.14082 | -50.06573 | 2024-10-01 05:46:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 8463846d-71f1-3cc8-805e-0e569678c41f | -12.1321 | -50.05156 | 2024-10-01 05:46:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 911efa3f-1264-3281-9846-d3e4f9efe5ec | -10.98381 | -50.16107 | 2024-10-01 05:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0d3f6398-55ad-3534-a54d-e81ad421e262 | -10.97653 | -50.1535 | 2024-10-01 05:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 2d18c144-c1ae-3375-8296-8df4b0f3d0ae | -10.97484 | -50.16553 | 2024-10-01 05:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0624a64e-6cd9-310b-9ab6-fc217d140624 | -13.63444 | -51.16874 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 3b239a9c-8054-3e63-8e56-7a30d2656934 | -13.6292 | -51.13298 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 400e6904-5d86-3978-ae6c-39177d223a98 | -13.62765 | -51.14445 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 26ed3372-c55f-3653-8f71-40c577716b17 | -13.62455 | -51.16735 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 278c9db1-08f1-3b55-b53c-1c64e3e04bde | -13.59799 | -51.06321 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6d3e2985-6bff-31a6-99e3-b60aaf0a933f | -13.59639 | -51.07478 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7006f5f4-8e69-3100-b3ec-a0baa9de04f2 | -13.58523 | -51.15518 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 58b4df82-2ee5-3c5c-9551-36f73b8db78b | -13.57534 | -51.1538 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c1d11605-1d6f-3e22-8eaf-6f3781c2fe9b | -13.57376 | -51.16521 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ee0b0b2f-33da-39f1-aaaf-5607e3b19b82 | -13.56026 | -51.1167 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8af24680-5a95-35d6-a420-f0610c11de70 | -13.06312 | -51.16695 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 89a79830-b2a8-3b65-8b3c-dd0e0148e020 | -13.06159 | -51.17817 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 312.6 |
| fe8c0888-8dee-358b-ac37-388381cbdb2b | -13.05178 | -51.1768 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0d93dc42-2aab-3067-9f55-1518a3fd275e | -12.39526 | -50.9665 | 2024-10-01 05:46:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cdd32586-50ae-3f56-82bc-38e220512b59 | -12.3937 | -50.97777 | 2024-10-01 05:46:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0aabfb7a-ece1-3154-a457-2f431b23ea14 | -13.93037 | -50.86962 | 2024-10-01 05:46:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b565bd76-3271-395d-abd7-254706254c26 | -16.65862 | -50.58364 | 2024-10-01 05:46:00 | AQUA_M-M | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e10672cc-3d3b-3644-8fce-98b2984f3589 | -16.65682 | -50.5977 | 2024-10-01 05:46:00 | AQUA_M-M | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 88e1da5a-b5e3-3471-94c2-3cc417e2ddd9 | -16.09746 | -50.32798 | 2024-10-01 05:46:00 | AQUA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b300cc3e-4818-386d-9fc6-d73dc95e634f | -16.09396 | -50.33558 | 2024-10-01 05:46:00 | AQUA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3ebbc488-a2fb-36a6-bb4a-1347d70fe4f6 | -10.50423 | -51.11866 | 2024-10-01 05:46:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5588c42-52fe-32f8-9cfc-5150ca677571 | -12.26721 | -51.53492 | 2024-10-01 05:46:00 | AQUA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 33fe4112-2704-3ca6-ae5d-08ca064f72df | -13.22898 | -51.22551 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2656cfe2-143b-3890-b61f-7e9c66a24267 | -13.21864 | -51.21724 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| d4e19763-228a-3c49-956e-6afb6a74ef6b | -13.20884 | -51.21586 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| cc4d8501-f7d4-3161-a7e5-66ea00b35aa8 | -13.19903 | -51.21448 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 15c824bb-5ac2-3dfb-acca-2be4dfd0b8de | -13.06007 | -51.18937 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 239.2 |
| c016c6c0-df1d-3080-af4d-0ae522c18418 | -13.05855 | -51.20055 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| f1bd9a8e-7a08-3856-91c4-90a9206a7ffa | -13.05703 | -51.21172 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 88445511-72f2-3c33-b549-cca009c253a6 | -13.05027 | -51.188 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 74163539-cfca-3d55-9520-db655b2a0c8e | -13.04875 | -51.19918 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 181.5 |
| a951e0e4-e76d-33c3-a805-43e97b2f6fa7 | -13.04724 | -51.21034 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7a2efd20-e573-3db0-b206-e19010493b81 | -13.04573 | -51.22148 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4883541e-81c8-3942-92c5-70fde559026b | -13.04422 | -51.23261 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| af363a70-c04b-3aae-a576-93b31d1098e0 | -13.04046 | -51.18662 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 3146cb89-1414-3f19-9cba-803817cd1585 | -13.03896 | -51.1978 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b63a984b-47f4-302c-bc2f-d9fd04bb6000 | -13.03837 | -51.19093 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 137c524f-55c3-32db-addc-94e363a7bbdf | -13.03745 | -51.20896 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| a96472f1-1d4c-393f-b7d9-3b5abc3c46bd | -13.0368 | -51.20208 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| d2fa17ba-c131-3c5f-add1-1b05fc5dd315 | -13.03595 | -51.2201 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| b2344083-e4f0-39e5-93d3-6e7089047a8b | -13.03524 | -51.21322 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| a15c4a8b-6994-3278-988b-05eac0a6c319 | -13.03521 | -51.29904 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| df8e61e9-188b-303b-a341-88d107993bd5 | -13.03445 | -51.23123 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| caaa1737-7271-3492-929f-b1505e471ce9 | -13.03371 | -51.31005 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 45405e8a-ce95-3f6c-b29f-c5a4639cff99 | -13.03367 | -51.22433 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 583eb231-a86f-3f9c-81f7-8e2c324f328d | -13.03295 | -51.24235 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 45282587-b7df-37e3-99d1-25d4d9b5814b | -13.03211 | -51.23544 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 1d9b8082-2b62-33b4-9877-a0f9f105738a | -13.03055 | -51.24653 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3c5bfb94-2d1f-39fa-8c94-b4465e827597 | -13.02857 | -51.18956 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 99c3d334-e85b-37f7-9de1-48277af17f40 | -13.02701 | -51.20071 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7e0e7f92-63f2-3fec-9da8-24c2e5233d0c | -13.02545 | -51.21185 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f9cd1ed2-5526-3d8d-ab44-3df7938b5940 | -13.0239 | -51.22297 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 03cfa975-d233-32fa-9ab2-f3147bc35965 | -13.02249 | -51.31968 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README152.md)
