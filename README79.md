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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99ef4d69-4684-357f-9236-f90d43b18cb1 | -3.83691 | -44.54955 | 2025-10-05 04:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c998f994-06fb-3756-ba03-6e0f76c5036c | -5.54504 | -42.6721 | 2025-10-05 04:44:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4ccd5647-a77a-31d6-b0c7-10315defde81 | -5.24779 | -42.63654 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a338518e-87fa-3f9f-b710-d25456045619 | -3.44464 | -43.33937 | 2025-10-05 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efeae71f-89b6-3d98-955b-2b176a6fbe44 | -3.84582 | -41.58892 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3d63a4b1-add6-311f-ad09-9160baec86a4 | -6.10191 | -43.47518 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a55aed5-7ad9-3433-8270-41ad819ef0fd | -5.93202 | -43.32798 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 12e63502-3571-3ce9-8fc3-04d01f0a4141 | -5.41225 | -41.31931 | 2025-10-05 04:44:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 91c18407-2d06-35b6-8fe5-391e12bf078a | -5.83027 | -45.81112 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcfcdf49-3515-3c90-bc08-90d758a2732e | -5.79794 | -45.77415 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ee0bfd9-d013-3c87-93a4-f3d0b1bffd40 | -5.86544 | -43.5546 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6283e44f-b822-3a8f-bb10-6aac1d3889ed | -6.13787 | -44.63443 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b27e0983-2dd1-37c9-a4c5-ea5325ed5cec | -3.81433 | -51.07599 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50b5e84b-f990-393f-a12f-9fe9ff14cb7e | -6.08901 | -46.19101 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8fe6457-4f66-3825-99db-4a1b42acf6c4 | -6.30075 | -44.44124 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4afd1fd8-2998-3707-90fe-6bc354ae41c7 | -6.39625 | -44.77501 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5617ab0b-6063-3b36-9b02-f1db98a4e8e6 | -4.32754 | -50.58286 | 2025-10-05 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7a3db4f-8942-3b36-9588-c7a2cfd02ef4 | -5.91178 | -42.89638 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 90fef36e-2fdb-3619-9efe-021f13f28406 | -5.89366 | -42.91681 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 975752a0-234c-38d1-8e24-0104a03daa90 | -3.331 | -43.15504 | 2025-10-05 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 802c3830-0e39-337b-9990-a13844386aa5 | -6.00471 | -45.81234 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c466624-dd9e-3a23-8c55-e69bd52758c2 | -8.53792 | -47.68497 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e5572cf-1bf1-32f9-94eb-22370c9b8d53 | -13.49178 | -47.26743 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3073d9cc-5fc0-3998-a437-9ef89d57474b | -8.23932 | -46.8185 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46c820ce-ad4a-33b8-a8d7-49759b4b5854 | -12.12605 | -49.42567 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e35a1aa1-b1c5-3fa6-a08b-b5c236af5c77 | -9.33416 | -54.51783 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f458b37-c2af-314a-a289-65112842f1a7 | -8.91324 | -46.59491 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0c3e95a-b27f-37c5-ba85-2b7fa9b9f0ea | -13.2513 | -48.48951 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab955a65-6420-3f0a-af54-b5b8e36d8d46 | -10.22592 | -54.2849 | 2025-10-05 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52aa3b58-3ae1-3879-8e68-eb4b4e1b4769 | -8.63805 | -44.90742 | 2025-10-05 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd14e2b2-aa19-3b07-96b1-32d4283f1286 | -10.62789 | -45.00331 | 2025-10-05 04:46:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6f3e9a0-6c52-309a-aba2-3cecaf4e0e51 | -10.65283 | -58.75528 | 2025-10-05 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67cf520e-14a4-319f-8cec-9fb273fbe1f9 | -7.73025 | -46.31494 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 46e7d7fc-8b7f-3d82-acc9-89855452cc48 | -11.1108 | -49.86195 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46bd73df-342d-3c7c-a4a8-21eed60aa2f3 | -7.47871 | -42.62651 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2c127a51-3b3c-3eb8-9573-4cb33760ba1a | -9.98938 | -48.29411 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2e09537-c07a-31da-99bd-ee8ee11eddfb | -13.37846 | -47.55349 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6d4b918-d18a-3a35-b844-c7c97202eb76 | -12.89152 | -47.31361 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45b607e7-864d-339f-8588-20ffa2bb6b97 | -5.82764 | -50.1683 | 2025-10-05 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea138cad-c90c-36b0-b918-2a781bd5be34 | -12.84903 | -50.49853 | 2025-10-05 04:46:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30ca784c-5916-3980-ac73-d029be48cb84 | -13.1191 | -47.9632 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c284761a-1d56-3679-a1ae-89507c57ae91 | -12.30437 | -55.14131 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a19755d2-e2a9-3906-a6e3-9d40d407cf76 | -12.96693 | -51.02886 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6d3cc3a-1d35-3b6b-8818-79f9d676bd31 | -12.92145 | -47.30663 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38c1199a-415b-384c-98b8-415186dc948b | -9.02017 | -58.98606 | 2025-10-05 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 384b1005-4467-32f3-ba1d-49b0ea01842f | -9.57366 | -46.12243 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 937937a7-1f9b-3dfb-abab-d18d19f6719e | -8.55155 | -46.27434 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 20f186a7-afa6-3e29-84fd-6d3daabf0929 | -8.55616 | -46.27139 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 014b9396-944b-3a69-aa7f-d344d0851615 | -11.16111 | -47.76015 | 2025-10-05 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9efb0e22-871d-320c-8b18-3c109a6ed408 | -13.32109 | -47.17369 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea8afc32-af00-3255-9625-828d205cab9e | -11.88821 | -44.97825 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ecd8c0f-4ff0-3259-90ba-259ccfd67c65 | -11.67195 | -43.89956 | 2025-10-05 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e0b3937d-08d6-3692-a37e-280a002a571a | -10.68349 | -49.27354 | 2025-10-05 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7aba2ecc-57db-30af-bfa8-af199a70c44c | -12.57044 | -48.16282 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45acf402-679b-3db1-ba6f-108c895014bd | -11.16256 | -47.76356 | 2025-10-05 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5143ef5-023a-30ec-a6e5-1b7c304e2b88 | -10.41785 | -51.67343 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88b8a777-5610-3eb1-a6da-02edb25b44fe | -9.10282 | -61.52983 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55747d76-7a8f-3e0f-b7b7-877448e60fe8 | -10.01544 | -48.29106 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84241c26-771d-3ef0-846b-24213613df07 | -11.83048 | -45.07013 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 934732d4-1b0d-3de3-a44c-1d64069bff7e | -13.34218 | -48.05814 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 10bed27c-59b6-361d-9834-6338de959d13 | -7.79145 | -44.51354 | 2025-10-05 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 68edaadd-47c4-30dd-9b64-e5232a7f98e8 | -11.20823 | -54.85126 | 2025-10-05 04:46:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79f60842-dab5-346b-bfec-b95a2552b45d | -11.63709 | -45.0777 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 790c2a80-6a02-3d2e-981d-c82879d94745 | -7.51445 | -41.26885 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 838fd0e9-3ca1-34d5-be6d-d96322a2dc1d | -9.80145 | -48.27161 | 2025-10-05 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5c4a173-a76f-3f5b-b116-ba756e147087 | -9.2956 | -46.00653 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c611ab1a-d318-3490-bcfa-ec18430c97d6 | -8.5387 | -55.01907 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42618378-9735-3b5b-a1cf-97a29d57c62e | -11.43273 | -43.48566 | 2025-10-05 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5726e12-6357-3beb-9254-faed987f9f94 | -13.11256 | -47.98187 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a0a1e31-5ba4-3798-826c-411a668e697a | -7.81562 | -44.53959 | 2025-10-05 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f27c1ba8-5c40-3408-8938-0530ac31ad66 | -13.25969 | -47.81399 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fc7ec8f6-facc-3e19-a30a-817d69f07f1b | -9.29464 | -45.6662 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5646a6e6-dd06-3b48-a938-64ec692d75cd | -8.78081 | -49.89639 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fd760d6-8d97-33a1-91ab-8754cfd501aa | -13.15878 | -50.88837 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 369a4900-d5a0-3023-a358-aefbefbc48fc | -11.249 | -47.77849 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25e22be0-807b-36ff-91b3-dfd8fe3a998a | -9.30665 | -59.32132 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8ce1c8b-bb16-37f7-9c67-5957e0c83e3a | -10.8392 | -47.19027 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ea30f60-9e5d-3cb0-992f-3b7333679dd0 | -10.68289 | -49.27759 | 2025-10-05 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5ea3763-dead-3849-846c-4fa428dbb9c5 | -9.30703 | -59.32368 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c098bf4f-ba8d-34a6-92fb-dc8cc45e8990 | -7.81174 | -42.54025 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9b3bfcad-f9a0-3ced-a2b8-6de357ae2b32 | -13.30435 | -47.78252 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b02978ef-1dcd-39af-8404-824cf85eb68f | -8.63039 | -54.9888 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a9ff5c3-9f66-33f3-849e-f60c188f5a98 | -9.34056 | -54.52299 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 494957b0-b5f6-386c-8493-7e1a3b7d6d91 | -13.13039 | -47.939 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a51c19f1-3154-390a-880e-2f991ea0e6e5 | -13.52091 | -47.2944 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf287670-f757-34af-80da-2a9a19d40668 | -13.23003 | -47.82483 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57f32523-8945-3be5-a721-1b246481b192 | -7.01561 | -55.26144 | 2025-10-05 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b3ac507-ab4a-3c70-94db-b3738f977a6c | -13.85716 | -43.98977 | 2025-10-05 04:46:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d1661363-22e9-34e0-80bb-62d00e755013 | -7.05509 | -42.7765 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 54f6c6b4-2a18-32b0-a516-57ed8eeda742 | -8.48263 | -45.9154 | 2025-10-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6190954b-b108-3c1e-b575-427f7e33717d | -13.09933 | -47.87421 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7be29bf6-bd26-3e60-9c92-72429a7e0040 | -13.12114 | -43.84393 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 18f7b05e-8931-38a8-b657-e9f3544299ca | -10.40108 | -45.41533 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d1a2a769-2d90-3229-92f2-fa218bb89bd9 | -11.95961 | -51.46782 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75cf799e-93d6-38ad-a558-782e2e8068e6 | -9.56358 | -46.91658 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e424330-2e0f-3388-b437-bbe8c7e6f3dc | -8.56952 | -46.26226 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 90c077af-6337-3c6b-bb78-0e9430b8cbed | -11.81478 | -48.88042 | 2025-10-05 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbedd36d-340f-33be-a62e-22deff6b6ff0 | -11.00296 | -46.52212 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2e41197b-ca4e-362b-8ef3-42da5480ae22 | -12.06925 | -47.98973 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 916c612b-5e82-335f-bae7-d3ec1a08643c | -9.95114 | -48.11566 | 2025-10-05 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README80.md)
