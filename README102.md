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
| ebf91f31-2230-338a-ae61-9008730a8bda | -6.44873 | -59.97688 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41ef2915-2b22-34c0-bf9c-3639d725a275 | -3.33911 | -57.86131 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0c13492-e708-30cb-8cc9-e993d513f6c6 | -3.40097 | -61.30384 | 2026-09-20 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67401659-f3eb-3f38-8e0e-56353ade5a5c | -3.69219 | -60.62192 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c56e8dc1-ac76-3579-bf5d-d700c864fa34 | -2.6603 | -59.7606 | 2026-09-20 05:59:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 450c11bc-4aa0-3df8-b089-6c24a8f83160 | -6.44941 | -59.9722 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30a80f00-37bd-3fb2-8ba0-0edfff3c9d75 | -2.51694 | -57.73852 | 2026-09-20 05:59:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b76f852f-cda9-31b4-b3b6-aca3e159e143 | -6.64484 | -62.88104 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b7c83de-b109-345e-acfe-9a27d1707cd2 | -3.6988 | -60.5791 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f0f6959-0430-3747-88d2-60304f5d5f97 | -6.35717 | -58.30846 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4a5e8ee-009f-35a7-8706-27d2d7a67ec2 | -3.01076 | -54.16608 | 2026-09-20 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1b6cf6f-196a-367b-9c60-3cb18efa8609 | -2.88076 | -57.82138 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee5fcc39-c629-34f0-a9a0-ab351dfb993b | -3.48312 | -59.58682 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e64aefb-a85d-3cf9-8f55-38f700ba4feb | -5.81531 | -57.54001 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80b6f378-fe01-369e-bfa3-d5b329adb960 | -2.50111 | -56.60094 | 2026-09-20 05:59:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd6030b3-68bc-3d56-94fe-cf01d0f081f6 | -3.69036 | -60.60575 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b3c7c0f-1655-37c4-844e-a6cdf3a3296d | -7.59648 | -55.70753 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93d35343-7fa5-3ff4-a575-dbd34833493b | -5.75331 | -57.57673 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bd2e72c-23fd-3ca5-9c8b-62423ac63814 | -5.85581 | -53.53404 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9efa5ef-bb56-33f2-99a0-6ada42d59eb9 | -2.96954 | -54.77082 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f997fc99-8909-364a-89d7-db89ed9d89ac | -6.89073 | -63.04169 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4baadc67-2b0d-3a0e-837f-52364424f745 | -3.69697 | -60.56277 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 594eda6e-1117-332f-bcad-1103f1acfa77 | -5.85674 | -53.52723 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d47f57e7-ea6d-3374-afcb-111c66d4e2d2 | -8.07429 | -55.34171 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a685c13-a941-3c49-b82d-d346ad306a0a | -2.98261 | -54.76818 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 975f87e7-a961-3cae-aff1-902b2d36cc48 | -7.04918 | -62.95583 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4b292d6-27f4-3081-86cf-490d3df9dca0 | -2.64012 | -54.68911 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aabd9bfa-37e2-3bc6-9a4d-589383f6edfc | -3.30638 | -57.87153 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a14b9df2-aaa4-376a-8de4-4301055388ac | -3.35195 | -59.86222 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 912e1f88-232e-3f00-b723-e4c684572671 | -3.68493 | -60.61288 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38df6357-7239-3882-8cd6-924f7995e00e | -5.8471 | -53.54597 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03a3758b-0224-3088-976a-b0cbb97af668 | -3.00437 | -54.16475 | 2026-09-20 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb10bfdb-dc61-3b9d-9268-32832a553389 | -5.84018 | -53.54478 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c8cf8dc-c6dc-38cc-9ff7-75845beec870 | -5.8444 | -53.56577 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 30a8eb58-6e04-3ba7-9675-0c27d24da60f | -2.88538 | -57.82506 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b15dc4d-e7a5-355e-84b9-451667d34edb | -3.45885 | -59.53212 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83f37995-8a0d-3c5c-9324-3e177e61b5b1 | -8.18079 | -54.74078 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b88e3b0d-52e0-3147-acb9-43d7c65b2cb1 | -3.6994 | -60.57519 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a1344dc-984a-3c53-89da-242c86a8c8d9 | -3.20018 | -60.42831 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a70fa759-5eba-3017-aa84-b11102a13b4a | -3.86714 | -59.00739 | 2026-09-20 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9016249-8a1d-3720-976c-262694f5524c | -6.34728 | -58.30388 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9bd1ad6-bf17-38ca-b4fa-ff926f3fbaa1 | -3.16101 | -60.57782 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c05463b5-b6b2-35c9-ac72-fd8f740df201 | -3.6904 | -60.63355 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2a6b88d-61b3-37a4-b5ba-6cf0f5d16974 | -6.10379 | -57.6861 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e21503a3-2dfd-3586-bc40-d58c348b3a9c | -3.29157 | -57.86632 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf6d2d42-92cd-3835-a712-a9c6eb1f1831 | -3.73239 | -60.61209 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06b93d18-41e9-3cbe-8936-0d7f79299c21 | -6.36233 | -58.30922 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e5a3bdf-00eb-3aa3-8c0f-a8dd32f071cb | -8.07551 | -55.34281 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a27a842-6e4d-3769-9724-663af2f7c1e1 | -3.0716 | -61.17897 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14e702d2-2a3f-376d-81cd-ec032d29b36b | -7.57115 | -57.68937 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aedf2b1a-c9b2-3ea8-a5c0-c9cd2a2e940d | -3.85966 | -58.8964 | 2026-09-20 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c874ccbc-80d5-342e-b2d0-83d2abaaafc9 | -5.8549 | -53.54069 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b12c949c-5d6f-3dbd-bd40-9c9188290aa7 | -2.71592 | -57.96509 | 2026-09-20 05:59:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| da8ead99-fd7e-3f8a-a5bf-5ea217583998 | -3.68374 | -60.62063 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f0bf776f-4ba6-3784-b7a9-ae5cb87a5d58 | -6.44413 | -59.97617 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e02027e-4533-3b93-beff-26e23463ec73 | -3.35884 | -59.8764 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ea3b3d9-03ce-351b-846b-b48d8e7f26ac | -2.88582 | -57.82214 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c5c6545-9178-3645-b08c-b13ffe978c47 | -1.30228 | -61.37418 | 2026-09-20 05:59:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cb6c81d-a105-37f7-b792-644fe903a570 | -3.15054 | -60.42105 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdebc990-6c46-3039-b6f6-afe2807f0bad | -5.84195 | -53.53171 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fbcf030b-d41d-3853-8c4f-bc754dab1bc0 | -4.48833 | -55.48726 | 2026-09-20 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80994004-cf40-3202-9c8d-46b604b0ea3c | -3.04946 | -61.26809 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44b41030-132b-3520-bf22-1cc64915147b | -2.68049 | -57.62479 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40dba198-80c1-3374-936a-3254ad761b8e | -5.74402 | -57.60296 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc8b6914-11ce-346e-886b-6d6b3d6df57e | -3.69637 | -60.56671 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8edf697-2298-39cc-bbaf-6f8e6ba09b6f | -6.64554 | -62.87637 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b901a007-8367-3dfd-8c71-e85c173e5312 | -3.44704 | -58.22759 | 2026-09-20 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 88e282f5-84dc-3772-bf97-349fda315e2d | -2.61141 | -54.75347 | 2026-09-20 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5821013b-07f9-3be0-8125-81caaf21c19f | -7.04536 | -62.95526 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5b60554-8bb0-3651-9fc0-a5dc025d755d | -6.49564 | -58.38342 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38584488-c16b-3ec4-94cc-2bd31c392622 | -6.92541 | -63.11466 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dee96ff6-cd51-31a1-83c8-8776ee51c128 | -2.81635 | -54.7164 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9decb0e8-ce94-3bf2-ad26-015098bc4566 | -3.691 | -60.62966 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27a204fc-4324-328e-b5d4-cbd9a62f20cb | -3.88484 | -58.9532 | 2026-09-20 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c33fa0d7-09f8-3f52-a5da-bfac629cf467 | -2.8812 | -57.81845 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07c957b8-d592-3a44-af7b-b859f8f3eba7 | -3.38045 | -61.29737 | 2026-09-20 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab51cce2-c931-33a4-9247-96052eeeede8 | -3.53948 | -58.69128 | 2026-09-20 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b066cfc7-bd72-389f-b036-59414412ce09 | -3.79784 | -60.72092 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66627db5-10fe-3c51-a230-a4e3b1864ebd | -7.57663 | -57.69016 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d670c9e0-226b-3073-a8a2-f711c7e63307 | -6.20255 | -57.77824 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 250971a9-4235-3dbc-baad-164d30e29de2 | -3.72757 | -60.61537 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db2d3a45-4f18-3121-9f72-c334ba0c107a | -4.48697 | -55.48719 | 2026-09-20 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 630d0a15-e42c-3e95-b81b-c5fc43d89cea | -3.39102 | -59.57523 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0756d23a-8d31-3a15-b2f6-2e34c5d8289f | -3.68797 | -60.62127 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 962460c2-d8e5-383e-926c-35b2c16bf209 | -2.88732 | -58.28857 | 2026-09-20 05:59:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3de4209a-cb44-3a59-9bfc-46435bcc8995 | -6.1936 | -55.45266 | 2026-09-20 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 815555bb-9827-31ab-848f-d2b712a59326 | -3.37642 | -61.29677 | 2026-09-20 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7a5d8e2-fdee-3fc9-8888-08ccd41b491f | -5.74744 | -57.57936 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d410180-b99b-3449-bbef-879caa909ea7 | -6.45333 | -59.9776 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f252f43-7240-3071-92a9-cfbdbac04830 | -2.89045 | -57.82582 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f9a9f31-6ba3-371b-a04a-1501f6578426 | -5.88917 | -53.64336 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df5ae0a4-51bc-3324-8141-952707aab4c5 | -3.37186 | -61.29962 | 2026-09-20 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73285286-bdd3-3b60-afba-aa1df514c95b | -6.72526 | -55.07854 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb58ba52-a7f2-37ab-9d5a-eee4a7c41f0e | -6.73219 | -55.0806 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee8741c5-8e90-3bd1-af02-286ea97f4b82 | -2.97188 | -54.77036 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7654004-5e0a-344c-970a-8e724c088a80 | -7.04606 | -62.95058 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86367daf-e53f-3280-9464-f758f7829e72 | -2.89596 | -57.82366 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd2dfabb-226a-36a5-8fdd-e34c033b5dee | -2.97714 | -54.76215 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d806c8b2-70a5-3355-975a-f74495cbdcb5 | -5.78022 | -57.58056 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7f3b3ec-e01e-3d6b-8cd5-7cbdc9cad26f | -5.84621 | -53.55249 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README103.md)
