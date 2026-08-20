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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 916e01b8-30c9-316c-ab3c-d76153997d1e | -6.24018 | -55.42319 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1073326d-0a69-3069-a666-3ed747034ade | -3.09971 | -61.2092 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 999a967b-1166-33a1-9be6-e1975e4642ce | -3.09585 | -61.21214 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43f4b344-5957-3f70-b3d6-fb337d8f7a96 | -6.87022 | -51.86418 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14248fd0-2e27-33f9-b986-d4b90070ac8e | -6.01884 | -57.87306 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 599de51d-f0df-3692-9fe3-053386ebcce8 | -3.01104 | -51.06126 | 2026-08-20 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddf2bbb4-fcee-3f8e-9304-8e9afc81529c | -4.39516 | -55.47172 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 584f7721-f91b-35f1-8dc4-3f60ca2fda51 | -2.64357 | -47.98807 | 2026-08-20 05:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45b44045-bdf9-3187-b84a-cef762b91344 | -5.79587 | -55.7177 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcb51453-6021-3f51-92bf-f53491605721 | -4.5071 | -55.44976 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68e44ec6-e90b-366f-871a-eb74d200f6f5 | -6.00481 | -57.86118 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df407d0d-e1dd-3b1f-9afb-0b85d1e7adf1 | -6.14891 | -57.85516 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76c6bda4-5c76-38be-b894-1900a97cf59f | -6.38706 | -54.94282 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59a9a893-db1e-381d-9d34-34f31a0db42f | -6.95287 | -52.81266 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acb998d2-3e7b-316a-850b-980509b29fa6 | -5.7965 | -55.71338 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 289134bd-f446-3d25-854b-6440b201e7a4 | -6.38121 | -54.94065 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62e97b4e-f2de-32c1-8f88-594c1d060bb8 | -6.25199 | -55.40582 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56285f6a-08fc-3e39-8764-440160ebff28 | -6.43282 | -52.76185 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4f91750-0ed3-3fe1-8edd-68c48153c654 | -3.91602 | -59.58598 | 2026-08-20 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3810c4cf-75ac-3dac-a658-2504081991a1 | -2.83206 | -48.65225 | 2026-08-20 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0c3ed2b-1abb-338e-8a48-8b3216776df2 | -6.39068 | -54.94195 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 817f9eb0-3f92-3faf-bd3a-2ba451e369d5 | -5.49518 | -60.13902 | 2026-08-20 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a432a6d-c98c-32ba-b200-8e202acf092e | -5.79714 | -55.70905 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba22d589-620c-3cb0-be12-194b534b867b | -6.00653 | -57.87611 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb85f963-b53d-323d-a731-4bc7a633b968 | -6.24674 | -55.40994 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5cb95fac-1929-36d6-b1d3-d65e27185105 | -4.46082 | -55.45607 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5afaaa83-5235-3a48-9c9c-c8809af37fac | -6.64361 | -56.41575 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11bb51ea-a3d9-33f7-a4af-118fbad21a24 | -6.38994 | -54.94695 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a09abb0d-a67a-36f4-9fa0-94f30dc99556 | -3.10085 | -61.22353 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af115de0-7b68-30bd-9455-c8808ddc1130 | -3.90159 | -55.88239 | 2026-08-20 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41e9b5bb-b10d-3b90-9c6f-299146920ba8 | -6.42611 | -56.18877 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdffa0e8-b5af-3adc-b314-b0b4a4bf7f77 | -3.0184 | -51.06269 | 2026-08-20 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1cd1525-55af-3147-9357-fd22da669830 | -6.30803 | -55.92116 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 726a6110-80ba-3d76-a20e-1e639bbb6279 | -6.00024 | -57.86537 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bc35ade-790b-31da-a70e-61d5dba5af46 | -4.45641 | -55.45527 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7e851f7-bbb9-3bb1-ac81-e3c34a03f9e8 | -6.43833 | -52.76252 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f7c0e12-1fcf-327e-9d07-1e7018898bd3 | -5.80412 | -55.7233 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3413acb-f394-35fc-8f45-57e43bd5f6fd | -6.43184 | -52.72868 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ca5caa5-fb14-3566-924f-ccea97a96ed7 | -3.10967 | -61.21076 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01f8eddd-bb83-33aa-9a14-00f5f90d3a84 | -6.42682 | -52.76473 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61e95c43-7261-30b1-8edc-8fb71cd974c4 | -4.50932 | -55.45462 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f62ef4f9-e32c-36c4-a30e-727b6ecebfc2 | -3.12985 | -60.69861 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 566f45c5-1c64-388b-81e7-0d8faa06188f | -6.44984 | -52.76044 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa1ffb5c-8834-34ed-81e4-d74b3378d658 | -6.1066 | -57.73918 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d0ad9e3-a23a-3134-bdea-a32f3ec5187f | -6.89628 | -55.72276 | 2026-08-20 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c1065145-d7f7-3a9b-9db4-f67f47b4938e | -6.24474 | -55.42391 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 132ed640-7875-3dda-a7b6-9f99191abdb6 | -4.44084 | -55.3772 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c7024aa-7547-3f24-bb9b-61e4eecffa93 | -5.80285 | -55.73193 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f938164d-c24e-3091-ae1e-710bd2c8b18f | -6.43785 | -52.72584 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e108d24-8fff-3160-ba97-e9a5a26ac8a3 | -4.39073 | -55.47108 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eca60aed-71cc-386e-889e-41e0dbe1b78a | -6.44084 | -52.74465 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ed714ed-f6c8-32b2-aff2-338bdd051199 | -2.74524 | -60.23893 | 2026-08-20 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79ccadb3-a616-33b3-8921-5d3ce55466fa | -6.37647 | -54.94006 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7abf8a02-9991-37f4-81e0-87b0516bf6fa | -6.00797 | -57.86647 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c0a3946-f8ed-30bd-8694-fe5372e8c7a7 | -6.62408 | -56.32329 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16392fa7-6db8-311c-ab5c-381f3b1ebcb7 | -6.44134 | -52.74105 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6f05428-1e66-3a99-983f-b66e77e30329 | -6.31244 | -55.92183 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fbcb670-4f00-37a0-892f-438375159c58 | -5.80031 | -55.71835 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01406d9e-a918-381b-9a51-ccbac4a76f0a | -3.01689 | -51.06216 | 2026-08-20 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b6fd2e6-f76b-3844-afc4-159ef76f737d | -6.38636 | -54.94783 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d2ac3f8-d084-34e9-84d3-792074e4c365 | -6.43233 | -52.7654 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 913513a0-2f7c-3b5d-beea-24627e423570 | -5.49175 | -60.13848 | 2026-08-20 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfdc255d-b181-3777-96cf-b4e205883fac | -6.86969 | -51.86803 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f786d412-de4f-3940-bebc-f7bd8c393fbb | -3.10303 | -61.20972 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5e273c0-cb26-3cee-932c-78749223e02e | -3.84078 | -59.37563 | 2026-08-20 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a297884d-1535-37c5-89b7-be2b0f1ac724 | -4.39108 | -55.47315 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6dabaf40-64e2-3e43-b078-396f2f33d12e | -6.25132 | -55.41051 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7619232a-43d7-3c56-a435-efe9e177d1e4 | -6.08928 | -57.91013 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0f8f9a8-4642-3b72-8671-63e0df3e02ff | -6.35318 | -54.90079 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 907bf9aa-a078-37dd-a47e-b37563f03946 | -5.4946 | -60.14273 | 2026-08-20 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c579307-399a-3e74-a32c-08a5f3054954 | -6.62199 | -56.32143 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee2696b9-de80-3069-a825-b51759ff57fc | -3.2554 | -61.16626 | 2026-08-20 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaf23e13-b620-3a42-9969-14c1ed8acbe6 | -6.34772 | -54.90508 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 213188fa-64e1-3adb-a56c-da480c3ce691 | -5.79905 | -55.72696 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d3badb8-3b68-38bd-ba99-ea889728935c | -3.09858 | -61.19487 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab42666a-18fe-3076-a6ed-2864384a39d4 | -3.09808 | -61.21955 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed44ce1d-7bf9-30e1-8ba2-ae802fa979c5 | -6.39179 | -54.94349 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b302dbf4-69c2-3173-af8a-a81a038393f7 | -6.0041 | -57.86592 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a164746-48ab-32a2-9af7-3bfca6fbff87 | -6.09172 | -57.9203 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 92b36293-8933-39da-b8f3-33d9c0be9465 | -6.44034 | -52.74821 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54a4d4d7-a962-32c7-9885-6b05925e4043 | -3.10026 | -61.20575 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ee84e84-a9c8-31e3-a440-c1235850b085 | -4.78757 | -62.9198 | 2026-08-20 05:40:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4931f39d-85b6-38d5-b304-1247e12252b9 | -6.44437 | -52.7194 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d09d959-bbe5-33e4-8148-68c4e565fd5a | -2.87623 | -59.22501 | 2026-08-20 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a451f3b0-0153-35fe-b57a-f49a3a7ab862 | -4.39012 | -55.4753 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71c19708-ceb3-30d7-92ec-5d47a3c27da9 | -4.95762 | -56.27035 | 2026-08-20 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46d4d0fe-c0d7-3f11-9409-1f7c0768deb7 | -3.01256 | -51.06181 | 2026-08-20 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02df4d89-0592-3a84-8bb3-37d7100616de | -6.43684 | -52.73306 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b6fde42-c304-363d-bab4-2ddaec4bcc28 | -7.75563 | -49.20317 | 2026-08-20 05:40:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e78b6d42-4518-3ed4-9488-a0c5d4274bfe | -3.1058 | -61.21369 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a80a8eba-ee8e-363a-91bb-bea0e835e58a | -5.99782 | -57.85507 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5e79a94-dfaa-39e2-9f60-812fea60567c | -6.42089 | -54.94254 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4df51919-1fe1-3918-b869-802f752de3e6 | -5.80159 | -55.70967 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0c915c8-a59f-32ca-aaf7-44d15553fc8e | -3.10189 | -61.19539 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f51f48fb-0149-3f0f-be32-8cc0accfc71b | -6.61978 | -56.3226 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa830100-2f48-3672-abef-d457ff40f281 | -6.44336 | -52.72662 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 723f54d1-a928-3c73-8c26-8138696df212 | -3.91229 | -56.12151 | 2026-08-20 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5683894a-2051-3015-877a-e50517001562 | -5.79968 | -55.72266 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 334dfda6-1a1a-3b68-88db-30844d9ca756 | -6.62141 | -56.32557 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1bd5e2c-5a24-3e44-93ed-8a24abea655e | -6.24084 | -55.41855 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README59.md)
