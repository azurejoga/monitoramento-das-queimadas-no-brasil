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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8c81659-5e6e-3fb9-b093-aac872e78317 | -1.04361 | -53.35791 | 2024-09-26 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b62f842a-58ce-3212-a103-753973ff9651 | -6.54389 | -43.01608 | 2024-09-26 05:40:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| f2d1cd82-1d89-32ce-9177-b61097629b1c | -7.08798 | -46.44109 | 2024-09-26 05:40:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2a769ddd-d09e-38b3-961c-a4161eed97fb | -6.78616 | -44.7239 | 2024-09-26 05:40:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 8ca633be-25b1-341d-a1bc-675db00ceab2 | -6.77267 | -44.72218 | 2024-09-26 05:40:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 88a0e665-29e6-365e-a7c6-9ab858f6a662 | -6.0891 | -47.66826 | 2024-09-26 05:40:00 | AQUA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| d511049f-8c34-3cf2-b24c-ee60b7806e7b | -6.08731 | -47.68085 | 2024-09-26 05:40:00 | AQUA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e4061c4d-59c0-35a1-8273-020b38ec027a | -5.94599 | -50.00036 | 2024-09-26 05:40:00 | AQUA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f8844289-8924-3843-a06b-e31157a70197 | -5.87616 | -48.08949 | 2024-09-26 05:40:00 | AQUA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9bf901ee-da06-3cad-9a6e-6244ff9709f4 | -5.87441 | -48.10153 | 2024-09-26 05:40:00 | AQUA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 395722a0-c7c4-3405-8e9b-9fb9298c17f7 | -4.66088 | -48.14522 | 2024-09-26 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a0cb122e-8625-3567-901a-319260c706d9 | -4.65923 | -48.1565 | 2024-09-26 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| aeb35347-e967-35cc-aab1-71790fc97a88 | -4.62705 | -48.52862 | 2024-09-26 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ac4def47-1466-3e91-9d61-703efc85649d | -4.62393 | -48.53234 | 2024-09-26 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| de1ba395-4b15-3392-abe8-69a4466ac93a | -3.9192 | -46.45113 | 2024-09-26 05:40:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 30.3 |
| cf0352dc-1da2-3662-a85d-1d347f4d48f0 | -3.91848 | -46.44564 | 2024-09-26 05:40:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 33e3db68-a74d-35b9-baa7-537dc0ec4bc5 | -3.91636 | -46.46003 | 2024-09-26 05:40:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 24b45c83-0a7c-3aa4-9287-6b85600e928d | -3.90807 | -46.44948 | 2024-09-26 05:40:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 9cf8431e-84ea-3f37-8be3-c149417a3091 | -3.90735 | -46.44401 | 2024-09-26 05:40:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5719ce6f-b0f2-3634-b343-11c44cbbe096 | -3.90523 | -46.45849 | 2024-09-26 05:40:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 14c70910-715f-3d68-9f2f-62be600fb55e | -3.56454 | -50.5671 | 2024-09-26 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f8f1c14b-09e7-366d-a6df-183dc1bdd09b | -3.56322 | -50.57595 | 2024-09-26 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 603b675d-2852-330f-956d-a26840467e26 | -3.55678 | -50.37567 | 2024-09-26 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 51a04118-d0bf-3c62-8258-0a20678cb707 | -3.55546 | -50.38457 | 2024-09-26 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e33c851e-85ae-3b80-b308-47273888aad1 | -3.39137 | -53.71871 | 2024-09-26 05:40:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 386e3096-9b2e-391b-9af4-fe063fbff84a | -3.34959 | -53.77247 | 2024-09-26 05:40:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 67068077-0d5d-3c00-831c-9e7c591323fe | -3.34793 | -53.78337 | 2024-09-26 05:40:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3d9f7be8-90f5-3d6e-ae8d-8c54e4378bee | -3.32393 | -53.20979 | 2024-09-26 05:40:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a3d1fb17-c56d-39ea-9732-55938c56abb2 | -3.32239 | -53.21989 | 2024-09-26 05:40:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 3b182bb6-2154-358d-874c-12bd23a5eca5 | -3.31452 | -53.2084 | 2024-09-26 05:40:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c63f1c51-077d-3811-86b4-bba030b85ede | -3.24633 | -50.47551 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 636e42f3-2848-3a37-b7fd-60ca02e66c51 | -3.22972 | -50.4576 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 66dbafd2-c544-30ff-9644-74c5308f0537 | -3.22429 | -50.31182 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ba82afcf-078d-3942-a3bd-c05f5eca6642 | -13.9572 | -56.14853 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 337a30a3-2d5f-3dd2-bbfe-793b252bd524 | -13.29302 | -51.32993 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2b0fcdbb-637b-3112-9f3f-95f9adc29a02 | -13.29162 | -51.33981 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 56f86f5f-548e-31dd-ae60-ec8890e14762 | -13.13173 | -48.54571 | 2024-09-26 05:42:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e64da9c3-8ab5-324e-bbb3-ebe242b550e7 | -13.03077 | -57.29547 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| db600a3a-d148-3033-a2e2-12783089fd6e | -12.89293 | -51.24044 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1b7c0553-dc47-331b-ad03-4edaf6767b88 | -12.89151 | -51.25028 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 368.2 |
| 41bcf1f0-82f8-313d-b597-f8eb735f88e1 | -12.89009 | -51.26012 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 294.9 |
| ca895eaa-b9e1-3964-a955-6b18f7d29777 | -12.88511 | -51.22925 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 48b74896-8372-3db2-9f28-3aa5c277ed96 | -12.88369 | -51.2391 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 3bc3d688-d309-3e4d-82d3-52b2cbed24c5 | -12.88228 | -51.24894 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 391.5 |
| 468fd956-d4b2-3491-9b7a-43cf23436201 | -12.88087 | -51.25878 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 394.1 |
| c4145069-94d7-3af0-8757-fe8af9852896 | -12.8787 | -51.20816 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b246848-e4c4-3608-ac49-c0abfa46131b | -12.87728 | -51.21804 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e847b707-02c4-39cc-a4be-bd5ab12dc51f | -12.87587 | -51.2279 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 7607fe5d-e1fe-306a-ae1e-e2f150f54357 | -12.87446 | -51.23776 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d4d36551-0eb1-36a0-903b-405b768527f1 | -12.87305 | -51.24761 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 0c4cf31d-6938-30a7-822d-f805dbf0f96d | -12.87164 | -51.25745 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 256.3 |
| 8b7a572e-19e1-362f-bcb1-afd723cb0dbb | -12.87086 | -51.19693 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| ab5aebfc-c499-3988-97b4-d736b4fa871b | -12.87023 | -51.26728 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 03910978-4b5a-3acb-ae68-5a62b35d62df | -12.86945 | -51.20682 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| d2ae2ff9-49f4-37e2-8a01-705338501d33 | -12.86882 | -51.2771 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 743d5480-5f63-30b4-8bb6-a2703ac563df | -12.86804 | -51.21669 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a89e28c9-ebf3-3c73-8fc1-473f0b37c349 | -12.86663 | -51.22656 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 29192ea1-ff27-3bfa-9cfa-9fca9934b29b | -12.86583 | -51.16587 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1ecd05fc-1a97-3a90-b6bc-143b6f528773 | -12.86522 | -51.23642 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 265f7568-2f14-32e2-a6ce-c245c3e8111c | -12.86442 | -51.17579 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0007b237-939a-3537-89f7-79b46f98e5a5 | -12.86381 | -51.24627 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4fe723d9-1e4e-38a8-89c9-0b044d92e86c | -12.86301 | -51.1857 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8d8913bb-2765-3253-a0d5-eba2cf66b413 | -12.86241 | -51.25611 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 705a2bab-5162-311a-a0be-2dcc7ca713f9 | -12.86161 | -51.19559 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9b4a848e-04bc-310e-adab-596ada9dcb87 | -12.861 | -51.26595 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 5a0a07cf-b5f4-396f-a523-135cdbc886ac | -12.8602 | -51.20548 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9cd9271a-f095-3b5f-ae31-c9f0e6d1d493 | -12.8596 | -51.27576 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 84221f69-537e-3142-a556-dc2910cf4ffa | -12.85819 | -51.28558 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 269.8 |
| c8a2e7c3-1a40-341b-a7a2-f305e237b15e | -12.85739 | -51.22522 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| cd237959-85bd-3537-a9b1-e560bcdf58cc | -12.85679 | -51.29538 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e5e1fa2c-2964-3a40-bc5c-1ea00ce016eb | -12.85657 | -51.16454 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 6e14655e-7024-307b-9956-891e4934d2c0 | -12.85598 | -51.23508 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4123d985-ba1d-316e-8a39-9b41ca0ce70e | -12.85516 | -51.17445 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 450712ff-065a-3f27-8180-4aadee0297ad | -12.85318 | -51.25478 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 52ef720c-dbc0-3b52-82c9-4ffa34b2a953 | -12.85235 | -51.19426 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d082bc94-e332-3045-9d4c-fdadb3245634 | -12.85178 | -51.26461 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 4ada6aa4-b869-3492-891c-9fa513f7c274 | -12.85038 | -51.27443 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e2208038-21bd-3089-94e6-d65fdd85e93d | -12.84898 | -51.28424 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0a082ed1-a69f-33c6-8bf6-d4f971106405 | -12.84815 | -51.22389 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 1823424f-784e-3b7f-bbe6-42e48217089e | -12.84758 | -51.29405 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 892defcb-520d-3f9f-a122-8976c0ba13da | -12.8473 | -51.16319 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 77dea84b-bfff-393a-9aa8-e0af6bb1f592 | -12.8459 | -51.17311 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 738ff7e7-3f69-3839-b190-4426c46d98ef | -12.8431 | -51.19292 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 694cf583-85fe-3429-844f-a0d7b3a31712 | -12.83837 | -51.29271 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 24745314-51a3-3919-a02d-ad8ad0ec5e27 | -12.83803 | -51.16186 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 0b1644c5-553c-3044-bfae-521589830960 | -12.82915 | -51.29137 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7b51be78-768d-39ab-bfa1-5d21b19afb19 | -12.82877 | -51.16051 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d589b6bd-77f7-3cea-b260-825a629e1af3 | -12.82776 | -51.30117 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 606e2f08-6adc-3b2b-aae0-645aef15dfe4 | -12.82025 | -62.68331 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| b7f2dda8-5f33-35da-a1b4-2f9f6ba21240 | -12.8195 | -51.15917 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 73b2ea77-4dbe-3a8b-9ea7-9708b9956e3c | -12.80935 | -51.2985 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ceb8c71c-2374-33dd-880e-1a972726a2df | -12.80797 | -51.30828 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d81f58f5-0788-3ead-aed3-786d26284f7a | -12.77378 | -54.03769 | 2024-09-26 05:42:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7fd597e7-9e01-3f37-a14f-03a78fb931c5 | -12.77235 | -54.04696 | 2024-09-26 05:42:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a2f8314a-1f34-32f0-90aa-7cdc6587025f | -12.76482 | -54.03628 | 2024-09-26 05:42:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ba474cc6-f877-3971-b413-8e468abdb48f | -12.76339 | -54.04555 | 2024-09-26 05:42:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 35ed0d86-ea0c-32de-bf5d-733364d64bed | -12.75984 | -51.32547 | 2024-09-26 05:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f82b6a17-95ab-30aa-9aa5-6af9dd5cb3ce | -12.7541 | -54.03825 | 2024-09-26 05:42:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67cefc04-5c3d-34a5-a14b-3e0c5e21b3f3 | -12.75269 | -54.04752 | 2024-09-26 05:42:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| bc28b0f5-57b0-3501-8782-23a6da524c55 | -12.7036 | -54.06827 | 2024-09-26 05:42:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README151.md)
