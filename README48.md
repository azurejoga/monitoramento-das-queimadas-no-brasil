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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2001f95-38e8-3b36-8c5e-881287051c03 | -8.46656 | -54.68 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db2efb05-f760-3c99-aeea-6c693201640b | -8.41877 | -67.77876 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35e03ded-9789-3c1d-91d3-c259ce808ea4 | -8.45687 | -54.6587 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dab2ce5b-087a-3be8-8cd2-92ad80cca7e4 | -7.53372 | -60.72236 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 151ba94b-4355-372f-a8bb-9ca26c7d57f9 | -7.53774 | -60.72296 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 055496c5-01a6-3609-a748-22b5aeade1c6 | -9.05042 | -65.73699 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e90bb0b5-a16f-3d0e-94b2-1da1146777b6 | -9.02556 | -65.72239 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faae1817-072e-3018-bc9c-ddc2b57969b3 | -7.45401 | -61.37466 | 2026-09-03 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68d82b39-914b-3baa-b79a-e3899160f263 | -6.88278 | -59.39988 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a92175f4-4bc7-3e97-afd8-21e3fe89a448 | -7.29765 | -60.71703 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c059b67b-6521-3d66-8801-773af580e86b | -8.05997 | -70.50263 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 490e3918-107c-3d75-90fb-5071da9a2c0a | -9.04272 | -65.74291 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bd3cebe-4824-3361-9f84-a32f0b41669c | -9.02278 | -65.45388 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87917fbc-9c07-3d05-8b32-a44abff0b94b | -9.09988 | -65.50529 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e7e82e5-3280-3c8d-bf79-167e9c36ede9 | -6.96103 | -59.78068 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aad0a8d4-3fb5-389a-9e6c-48ad0e39fa5e | -7.5021 | -60.77122 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20a74e83-7e42-348a-990d-2b5f41da2f3a | -9.03995 | -65.73891 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6287d80f-aa77-3e67-adf1-f26c827e924a | -8.46297 | -54.6596 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b980e77f-ef85-333a-a433-8088a87208aa | -8.98552 | -65.3871 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d881125f-0cbb-3bcf-8ca5-776b83de3798 | -7.8018 | -61.11118 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63ce6a1f-fa19-3a08-98e5-30ac8a38cbca | -8.06473 | -70.49827 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7da0183-ddf0-3c65-93a0-49e918d5239f | -9.09056 | -65.36747 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c92c1ad-3c00-333d-84aa-7305154ad8b4 | -8.87396 | -66.66901 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eff1a7bc-d050-351d-b198-cdc16dce32ec | -9.7127 | -65.01109 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 725e00e6-c462-314f-836a-1bcd4d7c16d4 | -9.0884 | -65.38152 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec24915d-9b8c-383b-828a-3b459ffdfd14 | -8.45987 | -54.68371 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bba2c8ee-664d-33ea-84e9-30ed78895665 | -8.81852 | -68.6771 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0cc8916-6303-35ca-81f9-c3d1aeff7d2f | -7.29415 | -60.71295 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 573ca192-ef02-3d5f-b6e1-2481f0972646 | -9.73986 | -58.40483 | 2026-09-03 05:44:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39060985-2af2-3466-baf7-4bd961b45c30 | -9.88086 | -60.29703 | 2026-09-03 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63b4953f-18bf-30fa-b26f-523780f605b8 | -8.87617 | -66.67654 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b04090f-5d29-3e4f-9304-f126a1f84a86 | -8.8502 | -70.61966 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a25d2fb7-2fd8-38f6-8531-d1b3b8e6e350 | -10.28322 | -60.53655 | 2026-09-03 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a093109f-7371-341a-8143-96f30623bc3a | -7.79585 | -70.05804 | 2026-09-03 05:44:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f42d8e24-17de-328c-ae92-b5db978a15dc | -9.04657 | -65.73996 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 058dddfc-da61-3590-a5a5-2c0ee616b16d | -9.02225 | -65.72187 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1aa44a37-a8ad-325b-94c7-62cbae69131c | -8.85326 | -70.62527 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a49fbb95-ffc0-392f-8ab9-e22556653acf | -9.71434 | -65.00036 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7762178b-ca56-3fb8-949f-2c4585b210cf | -7.80893 | -61.11737 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf05e00a-9823-3fc0-b3ce-6f065be96da3 | -9.02441 | -65.44339 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3ac8231-82fe-3497-825b-ba9e724f96cd | -9.71939 | -65.01216 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17bf1fb7-e629-35aa-85b8-a29dc225a40f | -6.87845 | -59.39919 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8afb8aee-6068-3e5c-993c-d0464565b93b | -12.01138 | -60.53088 | 2026-09-03 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 480173b8-92db-36f4-88e9-768f1c679710 | -8.61072 | -62.55028 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b33f09f-5f6f-3ea9-8102-f90500a09cac | -10.82674 | -68.31209 | 2026-09-03 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fae9a9c0-3957-34f5-995a-f9ab2abd3ee7 | -9.08894 | -65.37801 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33e93eb2-cdf0-3765-ac7a-428bf0a6cedc | -8.89714 | -68.90782 | 2026-09-03 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f53ac991-55b4-39ed-97ba-f5061281d93f | -10.28672 | -68.84473 | 2026-09-03 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51f4d21b-0e75-3676-83c4-802325d41862 | -7.50859 | -60.78285 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26ef1258-9931-3a0f-9020-ab0d05677bcc | -8.87672 | -66.67304 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebd939c5-5440-32f2-a3aa-bbdac3988c72 | -9.13768 | -61.60212 | 2026-09-03 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01a31a63-282c-346d-81b2-1b4c012f074a | -7.29072 | -60.62271 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd0d353d-9f02-36d4-b736-430a9c19fc54 | -9.64959 | -68.61419 | 2026-09-03 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 165be60e-0dcb-3e0c-867f-f97e8c8fc1c3 | -7.26149 | -61.10366 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9935f7f6-0431-3a7f-8a70-c3ce099159ab | -9.13108 | -68.17708 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dc5f33f-c7a5-348d-a0ab-050cbf33de79 | -8.77085 | -62.82868 | 2026-09-03 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ad15a9b-b818-300c-a3b8-053d91bd399f | -7.202 | -60.65941 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61bd1be4-9e5a-35d6-bb1d-2d1a5cc0554c | -10.25377 | -68.24953 | 2026-09-03 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b5318ee-9838-32ff-97fc-8424997aa464 | -8.81317 | -69.58085 | 2026-09-03 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a52aecb0-8049-31f0-bc07-dbcae062cc6c | -6.9148 | -63.09298 | 2026-09-03 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2e1e7c3-bda4-368a-a515-4a33eae1e8c4 | -8.65885 | -70.91946 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 580ab8ae-c6f1-316f-8157-e6f598605ed9 | -8.86513 | -69.03707 | 2026-09-03 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b1fa3ce-4c4a-3999-8334-6e5a82ee85e7 | -7.02521 | -62.98454 | 2026-09-03 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92a2b920-f3fa-3417-8b20-24e8d1ed44a2 | -7.26004 | -61.11359 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae36b8cf-225d-3906-b242-65c0cf23d18f | -8.43884 | -54.75104 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6ab1f9f5-34bb-304b-ada7-6163a79a47ab | -9.09002 | -65.37098 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85ba7868-2118-3702-aa4d-6cb96820881a | -7.29315 | -60.71992 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2188395a-cf78-3197-91b1-f9b5f0f3c23a | -9.02502 | -65.72588 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 903dc83f-5aa4-34be-9d96-9bb2b1482e19 | -8.59354 | -67.17135 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed241fef-79c8-37ce-9949-2ee092855305 | -8.44613 | -54.74242 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41d4c2e7-f43b-38c6-8a1e-e50f6360de25 | -8.48335 | -70.62041 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a716ee4b-697f-31f5-b611-b22d621e791d | -9.09281 | -65.37502 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04239d60-f1af-3238-a3a7-76b59ab844ed | -9.04765 | -65.73299 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90ee3b27-f7c1-353b-b312-8c5a5d6b8078 | -7.50459 | -60.78226 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c426fd6b-6146-35f4-acfd-e5f2489da273 | -9.71659 | -65.00805 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99b0d39c-1eb6-328d-8582-e9772ace8aca | -8.62408 | -62.56104 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38c96115-2024-3568-8949-03588f18b8d3 | -8.99293 | -65.44922 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3fcdb82a-3e44-39f3-92cd-bbfa7c1f59a5 | -9.13452 | -68.17764 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f331c185-0af4-3454-ac83-83a947a45123 | -7.35824 | -60.61115 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82c5dcb1-eea8-3b0a-8995-169824e7c8e5 | -6.84485 | -59.90053 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 771119fe-5086-3c0a-ad5e-880d84580989 | -7.26959 | -60.62679 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a98b7a9-299d-3fe8-9789-f23399b4d37a | -8.43944 | -54.74636 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad90322d-3fd4-3eed-ba4a-1d2cbb284d21 | -7.19698 | -60.66574 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3c6515b-dd87-3897-9db9-2611abd356b2 | -8.43396 | -54.74089 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43db70b6-ae3f-34a4-a5b8-b8229e0daec8 | -10.29178 | -68.85766 | 2026-09-03 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3639f389-726d-3239-b823-1375d3c529ad | -7.19299 | -60.66507 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a31ea3d-e356-3292-9ad0-7dc986b62317 | -9.88512 | -60.29768 | 2026-09-03 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1794e9e3-4bb9-3e70-9fea-082074cd92e9 | -9.04326 | -65.73943 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4aaed42-0d82-3e39-89eb-17d7d52e1b1f | -7.21045 | -60.68577 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54a3cf45-8f0f-3de2-a359-fc312fc68520 | -7.35524 | -60.60354 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f81d530-2dec-3062-9870-1c6e976231cd | -9.01215 | -65.41279 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f79fb5ee-3a4d-3aaf-9087-8fcd4a7f8f26 | -9.07351 | -65.71922 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e64ca98-16a2-330d-accd-7a74df6de817 | -8.62284 | -62.56962 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75aa7f7c-45b4-3886-b057-4303eb99d46a | -9.07682 | -65.71973 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae1ba4b8-65e7-313a-b6d8-ab8902f1011d | -9.08948 | -65.3745 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55c720f0-14d9-3dc0-9005-c4b9b3fbe0f6 | -9.71099 | -64.99983 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 425e82f7-b1dd-37e3-b85c-f95f0ccb9c38 | -6.96526 | -59.78131 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a2616ba-b71b-3f9f-b543-b7d2da972e4e | -7.20148 | -60.66299 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75e0ec78-960b-3146-884a-5e1e59488c2a | -9.06578 | -65.39594 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4dc0dd4-3792-35f2-931d-52bed6c63240 | -9.03718 | -65.73491 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README49.md)
