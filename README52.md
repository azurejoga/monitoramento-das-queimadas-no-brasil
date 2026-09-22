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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 777e1a1c-c6d9-31d1-95c6-418efd879f87 | -5.99413 | -44.72859 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 45738c6c-c6cb-39c4-a138-82c850d45ea9 | -7.41425 | -44.73067 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4bca210d-25aa-3b41-a5e8-26682103510f | -6.44209 | -55.64119 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 876c3d91-eb4b-3123-97d4-3a512abbecd3 | -6.58374 | -44.14366 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 722841db-89bc-360c-89fe-c66bb74e17e7 | -5.80994 | -52.09308 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55f88cd4-f6de-3a02-9342-2105ad1580cf | -8.61867 | -54.62272 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b566e43c-dfaf-3ae2-b18c-3e928a35bcde | -5.72923 | -52.23613 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d84bea32-3588-33a9-bcb8-7f1d84cbacbe | -4.30792 | -55.59583 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86f4e8be-9d9b-3a03-8089-896ba699a3a4 | -5.39456 | -42.94947 | 2026-09-22 04:46:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| da66edca-5b75-398d-9802-56903194ba78 | -3.0489 | -54.40638 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 028b74f5-4193-3d1b-92ac-c113a5be8cad | -4.05669 | -56.33075 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a093442c-1fd3-3ce2-9765-4b1408f6fc93 | -3.92782 | -56.05381 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7395de2-d011-3cc5-aada-d2029b000253 | -6.10074 | -57.67864 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9cd2c3df-a4c7-3253-987c-f4f8b81008e2 | -9.15575 | -50.00965 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bc36e87-e059-3a7a-bf35-567cc1107bc3 | -6.67721 | -50.94493 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f8cddca-447a-3191-b916-19b5089b9882 | -8.14475 | -54.81085 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4edd0514-3766-3e96-8a77-bae1351ec031 | -5.75713 | -45.08974 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 45cecb61-48b2-34f2-8499-479146bfc1ce | -6.77971 | -48.66761 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57b476a7-94c5-37ac-97bb-2a0117a18063 | -11.14835 | -42.8427 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ff5b8441-4181-3a92-8915-a17ad2ca24fe | -6.30589 | -57.74157 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3ddb2f8-c1ec-3c94-aebf-4f6a0e30a6ff | -5.89229 | -53.64066 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 003333c6-44d8-33fd-94d8-12bca8462831 | -5.93849 | -57.69928 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b6fa89c-2f84-35bf-944e-0f1c3b9e6d14 | -5.38881 | -42.95439 | 2026-09-22 04:46:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ec496059-f071-329a-be06-80430e0d7f16 | -8.264 | -55.26849 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc2777d6-4358-3dea-9216-c9a2a2fc0765 | -5.88128 | -52.05016 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 950615a8-dc9d-321b-9d00-c234bea3adc4 | -8.78181 | -44.28826 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a8ded62-6ad9-3f5d-a59a-83423606fbf4 | -5.80428 | -47.7699 | 2026-09-22 04:46:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b2ae7958-5123-3ca8-9988-1e35124122f0 | -7.24687 | -55.58353 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e9ccb98-d923-395a-aa5d-6fb2f73c734e | -6.28764 | -57.77634 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc12bf33-9fac-3644-a7a7-e21e6da151a5 | -6.74793 | -55.09336 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 556caddb-52b8-3f7d-85f6-dc5287e30dd4 | -4.2695 | -55.43925 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c8c355a6-03c1-320d-a145-8db6557ffba1 | -5.89738 | -52.09951 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12370411-ff19-39cf-9d50-fbdaf72b71aa | -5.86793 | -51.94054 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 722056c0-69c7-3b7e-b8d9-73d1efe2d5c6 | -3.05644 | -54.40747 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e20d96ca-5384-3113-9210-6a3cea2815fb | -3.36372 | -50.76908 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4060734-ec1e-32ca-ba6a-d93b362aa866 | -5.46684 | -60.21476 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef21404b-41fb-3cf1-97fd-b7d7f6d4a6ff | -3.82174 | -48.9977 | 2026-09-22 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f17322d-3541-314e-95bd-ad8ff8f9cce6 | -10.74907 | -46.31468 | 2026-09-22 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 41e67c22-6167-311c-b356-fa3dbd11946f | -5.19888 | -56.07377 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 31615b9a-2758-304d-b134-5741c73a6104 | -10.46308 | -51.30749 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e3a69de-92a0-31cf-a202-2cca8d870074 | -6.34309 | -59.94944 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0830e45-4801-35a2-baef-87b925ef9950 | -6.83614 | -55.52995 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b01be21-0db5-3b04-ae38-be63b2678cae | -5.8278 | -53.50736 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d971f1f9-0e8c-3643-86a7-f78f1ac59b7e | -5.88905 | -52.04414 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3485db02-f3cb-30b4-b958-3530825b6991 | -3.05784 | -54.39854 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eac07537-61e0-3130-a8be-0ac81ab3204d | -2.86431 | -57.79827 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c33c512a-80a9-350e-82f9-e41b0278b527 | -5.61303 | -44.84035 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ca5c47f-aba7-3b17-a0bc-1f9bb0d8fd50 | -4.17984 | -51.24992 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae1dfce7-1308-39e8-9ece-4c0a1c3d8653 | -6.98508 | -52.86034 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffb78fcc-76d2-3ceb-8e89-341c21df9311 | -3.4688 | -59.55204 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a7e127f-0ba9-3009-bb17-bee1e5639c12 | -4.29814 | -56.26275 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da87f5df-d039-3ac9-8bd3-6c54415fed12 | -4.58032 | -42.93989 | 2026-09-22 04:46:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d77f9da9-67cc-395c-a25a-9a59c8b2a652 | -5.78746 | -43.77134 | 2026-09-22 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba8375ee-dd88-3b8b-85bc-2314262cf263 | -9.7317 | -54.81024 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 172010b4-ddf4-36a8-92cc-a96f27a1ddf9 | -3.07503 | -51.20047 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae7cdd6b-4f5c-3e54-a0b4-11e1d127c050 | -5.90429 | -51.77489 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 56e663c6-6d9f-32ab-a95a-881cfa54d26d | -3.40943 | -61.29785 | 2026-09-22 04:46:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33943403-c4fa-3e61-bfca-a749b8d65a7e | -8.60089 | -54.61984 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9a9828f-4a45-339e-84e3-2f9327cb0d81 | -7.19457 | -50.83061 | 2026-09-22 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f61eb73-f7af-35aa-a2ce-fcee97f0bc5b | -4.78731 | -56.00939 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 765dbe78-79cb-3391-b5b2-141a44bc98a5 | -6.14525 | -59.93596 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2006189-e138-3e67-95bd-f9c5a6c44cc3 | -6.59763 | -39.13514 | 2026-09-22 04:46:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a0406b9c-ea67-3c18-bdb5-16fa299ded07 | -6.61964 | -59.91809 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| c6744e84-e87e-3d60-9b3b-8d789dc51a51 | -3.45294 | -50.61404 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5cc3f4c2-8357-392a-a225-1e74865ff32e | -6.46304 | -59.98269 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1b4948ed-b6ee-3b32-b825-d9b451959645 | -6.97715 | -47.50117 | 2026-09-22 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac5b4402-f7e4-3997-a187-a26bf3f5a3a6 | -3.2063 | -53.95331 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69550785-205e-3301-bb2a-8b3a38984f34 | -10.01893 | -45.20372 | 2026-09-22 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df19134d-1ef8-37c1-8801-8346337d6241 | -7.05601 | -49.91718 | 2026-09-22 04:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8cdae47-e462-3ee3-bedf-4fec4e2cd61f | -3.47339 | -59.58974 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f945c866-cc05-39c3-befc-06b5e08a3343 | -5.42512 | -60.16979 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1999f6b3-fac6-3108-92c0-cc4d3d9d8433 | -8.79748 | -44.27977 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d756db21-2a17-3bc9-ac41-c6c6d4948db4 | -4.05991 | -56.31146 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a490aec-133e-30f2-8b13-62ea6c6a6fef | -9.61974 | -43.92845 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d7a106e3-38ba-3cea-a4c4-78aaefd35f46 | -9.62261 | -43.92855 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f48ab610-956e-35a7-86d7-589e71f7d0ed | -2.96252 | -57.62794 | 2026-09-22 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 219ffb20-35f4-3f12-8323-c89a343b0ce2 | -5.72655 | -53.45976 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93fcb0c1-2fb4-3793-981c-c44fa748756e | -5.69614 | -50.01047 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5aa1babb-2b45-3d49-a954-3da9e31ad464 | -3.72079 | -51.27003 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f1c5a6d-0931-3de9-a4ba-6c3c72864ee9 | -6.19915 | -57.78402 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87fc29e3-7d7c-33be-a5b0-c28fd26602a4 | -2.96133 | -52.14426 | 2026-09-22 04:46:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99638d70-9d35-31d2-a1a4-805e10b28405 | -6.35295 | -55.84409 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7271ee9-85f9-310c-8714-9d287e87114d | -7.59357 | -57.67257 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8664f094-b557-33bc-965e-053f92a32e2d | -9.60918 | -43.93269 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a6bf4ed2-be44-36c9-972b-86c39baac72e | -4.22772 | -48.61314 | 2026-09-22 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78d5555a-95ca-3d77-bfbe-9d85cb464e40 | -4.41671 | -55.49741 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bbcac07-2c1c-30f6-97e2-48a25cbc33c1 | -9.89776 | -48.4184 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80820e5d-e973-3cd9-b7ef-8cc4c26a38f2 | -5.89794 | -52.09597 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15140883-ab64-3e73-867f-4fe20f7462e7 | -5.9863 | -55.69778 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a12fb12-f2c5-38ea-bb76-e41f68e1ae93 | -3.77593 | -51.35316 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e10131b-c2da-340f-9824-c089c7ba627f | -5.86848 | -51.93707 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4d72ccb-8400-3173-81c0-544dbf2a1be4 | -3.06198 | -54.40184 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d5c5beb-b1b7-3b1d-a592-0f019952813c | -5.89298 | -52.27961 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7bab929-a5f0-3298-b2ea-e56fade91ab5 | -5.75052 | -51.92939 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91c611ec-e0d5-33b4-9b30-2d5ca610d061 | -8.3727 | -45.61795 | 2026-09-22 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 011dfd25-22b4-3e9b-ada5-319e2d0aa3bd | -6.74536 | -50.9201 | 2026-09-22 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee674da0-805c-3139-928c-e24cfce85b9d | -9.23907 | -46.15388 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36d372ab-23a7-388b-8a91-2b468958b4fb | -3.92411 | -60.55367 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5464eec-2bf3-3a71-a1a4-1890ab435cdd | -8.90404 | -62.3729 | 2026-09-22 04:46:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed3a5d0a-b30d-30ef-ad1a-8ca63b69390d | -6.30984 | -60.01845 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README53.md)
