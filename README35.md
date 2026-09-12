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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b35e61b-1290-3e8a-b121-f66a227b80e7 | -6.06765 | -53.49462 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72e06743-1718-3139-b689-e92d2f99a2d0 | -6.60548 | -58.84003 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b29481e6-5f94-390e-93fa-3358f0ec535a | -11.53367 | -44.8946 | 2026-09-12 05:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76040eb6-f097-3580-86a6-c12f662cdba4 | -7.95865 | -44.00605 | 2026-09-12 05:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bd4258d-0fb2-3641-8579-90d67de97351 | -9.46723 | -54.93135 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 230330b6-87f7-30b7-b9dc-4a522e244251 | -4.92802 | -47.54171 | 2026-09-12 05:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfbc1946-0634-3847-bcde-92e910746259 | -3.89495 | -55.81797 | 2026-09-12 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1778ea38-87a4-31ea-b9e8-511081aa156e | -8.08563 | -54.87062 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcfb4246-c768-35d7-b7a7-df9f36f13808 | -6.06487 | -53.4906 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca9148cb-042d-35ff-8696-81a30843737f | -11.09569 | -50.82933 | 2026-09-12 05:10:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72a0f7b3-4bdc-3e2e-9a81-581c50e4598d | -4.86448 | -56.00327 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74379081-ce6b-3837-871f-d4958e9fbd81 | -5.78716 | -53.81411 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 385d199a-3acc-31cc-bf05-09f6c1ec4ab7 | -6.43261 | -56.10656 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8fe7f6-9c88-3282-a22e-00bb30dff539 | -6.12395 | -55.64013 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54988654-9c34-374e-a7ce-5243ebc389ab | -11.36352 | -46.797 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38641894-0c13-316f-b6c1-8e1558c63833 | -5.82813 | -53.79211 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45cb1039-5038-3c3f-be92-d55a3a91a689 | -8.22147 | -55.25507 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8098ea3e-40d5-34b9-ad92-f440135cda58 | -8.11724 | -54.80062 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bef7158d-bed3-3b41-8794-9368fce32343 | -10.224 | -45.19172 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c2fdddd-1005-3f31-9966-3d9fe23aa26a | -9.70417 | -54.34673 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0681996-5415-3a3c-899d-225b27c64b24 | -4.35983 | -47.77927 | 2026-09-12 05:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 35aaa8f9-ee92-3aee-b165-2e3613c4f45c | -8.06784 | -54.86079 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b15b833-c7c7-33a1-a220-ed8f12a7ce1e | -8.25745 | -55.47006 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7faf31f4-f617-3c1f-aca9-974b4718121e | -11.81699 | -46.37079 | 2026-09-12 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b201dfcb-e835-39d6-9756-443a31587f7d | -5.78771 | -53.81065 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0656ed44-8246-3819-afc3-a5d4ea704c2d | -2.73831 | -57.64002 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 580b9c48-dd63-3095-9c8f-852f602380a3 | -6.18435 | -57.72407 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f3afba7-b7e3-34c8-87cb-ac64ac782de3 | -4.74076 | -55.89919 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f16ea5b-3aff-3028-8141-23debee8c82c | -6.39179 | -53.18059 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1f8a571-53ed-383f-9fd5-5b772f189090 | -10.54834 | -45.2103 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 284b6d45-f02a-3298-be25-65443f6609c3 | -10.54975 | -45.22609 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2089f391-738d-38c3-b3b4-2ebc8d92aaaa | -10.53121 | -54.38358 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3df8b8a7-0276-3a8e-b02a-fa0c53cbcf4b | -9.54957 | -45.4738 | 2026-09-12 05:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e31ad95d-f294-3521-abcc-d74c75ea2da5 | -2.72134 | -57.62265 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff1d0e09-aa74-3a11-acaa-cad6043ae8b9 | -9.70638 | -54.33262 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e1a289c-082f-3007-904f-0cba316ec5d5 | -9.90882 | -46.23933 | 2026-09-12 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fed0dbd-dbc7-3cdd-8f5d-479f928fed37 | -5.7666 | -45.09529 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 60e751f2-7a25-35f3-9f04-dcf3d2e8636d | -3.37183 | -57.70775 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c71ed0c8-fea5-357e-8291-23ba4f202e6b | -8.12389 | -54.80169 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60bda40c-aec6-3a4d-b4cd-bdc761231440 | -6.61165 | -58.85132 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 57d03684-9481-34d6-b6e3-fdf7e80e3dee | -5.12635 | -55.97376 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 515519d9-b8e2-30f3-97ef-f1146ec1150f | -3.74412 | -61.75632 | 2026-09-12 05:10:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d536701a-a5a3-3492-9fbd-b233ab5f6087 | -4.39709 | -55.77618 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bf36cdc-2bc6-30c5-b884-057fa428c229 | -6.31536 | -56.05431 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9946e065-2e0e-3505-823b-e36b69cc0b42 | -4.30122 | -49.11723 | 2026-09-12 05:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f7faf9f-b1aa-38b9-8763-cc99d2d4423f | -7.41881 | -46.15358 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9c92c81-7efc-3076-868d-a259a8104f35 | -5.79381 | -53.81516 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2813dda-8702-30f3-a608-d071c8964b2b | -5.60888 | -44.84362 | 2026-09-12 05:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 33648baa-4983-3f38-a478-4bc9b529bd7b | -4.36115 | -54.78232 | 2026-09-12 05:10:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0154ceb2-c245-32d2-844b-178edd4b2b58 | -11.3749 | -46.8297 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51aa8ff0-c723-34af-830d-5f903536e0ce | -10.53902 | -51.36325 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3ee3f04-c2f7-3999-8bc4-53fdbb40cb8f | -5.61427 | -44.84449 | 2026-09-12 05:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 339b9be1-db95-345c-ad54-7576d157cec2 | -9.23762 | -51.73275 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b8c24df-a855-313f-936e-364f6c3d69cb | -6.88667 | -55.65483 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b498d572-d6f4-3001-a55d-266ab5e17438 | -8.50379 | -50.14961 | 2026-09-12 05:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3bee3df0-4312-34e3-a362-22806d529456 | -5.81486 | -53.81136 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6333feb1-badd-368e-bb68-b56572ffc026 | -6.96057 | -44.54876 | 2026-09-12 05:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 77fbdf8b-894b-317c-8682-db9f922d40af | -11.03837 | -47.97144 | 2026-09-12 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 286137cb-943c-3ae5-9c4f-1145891c2538 | -10.63246 | -46.12337 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64a3e7f1-ae0b-3ec4-8b61-ff38ed21aac3 | -10.55444 | -45.20742 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b65c07e3-11de-3abc-bfa9-e96e8eeb4d17 | -8.09839 | -54.83334 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b7d86d4-fcdf-393b-88b4-ccfa8ab40839 | -10.23657 | -56.25898 | 2026-09-12 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebfeda05-647d-36ee-a95a-432915579f54 | -4.81792 | -55.76534 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f94c88c7-8d9b-39f7-b523-26ab9ec9c257 | -10.5281 | -46.34639 | 2026-09-12 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1dc9e015-b3cb-31db-a57c-75f550261e65 | -9.69896 | -58.16253 | 2026-09-12 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b87cea7a-7a5b-39b8-85e1-a287ece42377 | -4.87236 | -56.00765 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75c83322-c3e9-37d6-a0e4-194c7af38f73 | -10.56013 | -51.34969 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f08bf3f-723b-38a4-b794-23c1b4542462 | -8.58375 | -54.56781 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd0d203f-9394-3b31-bc88-33937c2c14e6 | -5.76469 | -45.09793 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 362599fb-1ba4-35bc-80f6-e675bf26b8a7 | -4.27346 | -46.53447 | 2026-09-12 05:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6dd13c3-3656-36d9-a589-9a947503ed1b | -9.46444 | -50.31351 | 2026-09-12 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 487e1aa9-b99c-3305-acd9-4247e602d9d3 | -6.31132 | -55.15063 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b84b9fe1-0155-3f57-b8a0-4b7a5f49de16 | -5.93413 | -46.3556 | 2026-09-12 05:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 524cee63-da6b-358d-a000-74d81c53d0af | -6.11519 | -52.24574 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 450b3fc6-61de-3460-99c6-bd231261d6a3 | -8.82458 | -46.02039 | 2026-09-12 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02abbe15-6766-38fc-a6f6-deb3b1fa6d9b | -5.81099 | -53.8143 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d2eaf57-f68b-3f2e-876b-3dd1c368c32c | -6.96108 | -44.54498 | 2026-09-12 05:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f855bb6c-0fd7-3009-9c0d-6a3beb60f82b | -10.68851 | -54.16699 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 118d4b23-5233-367e-b0ee-71016f2c9b3a | -9.53794 | -45.47219 | 2026-09-12 05:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 235ed7a3-6b1e-3715-a01e-7a7de8c299d1 | -11.79867 | -46.38763 | 2026-09-12 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fde21b9b-7ab3-3461-975e-dbbe0e7ea591 | -5.80598 | -53.80286 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17db6fd2-f4ed-3c71-835c-3ad7ffe1efc2 | -9.72867 | -54.8158 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff5ba42a-f917-3a5b-8956-7f53d4dffc03 | -6.11128 | -55.64969 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92f24e27-bec9-3871-bc90-1822b2732759 | -6.10451 | -55.64851 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 872d4724-c01c-3973-8854-2a5c7df98565 | -11.37531 | -46.82662 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f93e1ed-27a8-360a-9575-69886acff8fb | -6.61081 | -58.85633 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 798442b8-50cd-3f26-9b6f-64d796583cb5 | -10.22182 | -50.36959 | 2026-09-12 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21619883-8ed9-3f64-95f6-2d28334a742a | -5.10178 | -56.12516 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5a7ad63-f9ab-30cc-a9af-069d99497232 | -8.57268 | -54.57319 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d74d5a67-c829-3c22-99ff-bbb866fbe9db | -10.47466 | -48.63988 | 2026-09-12 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbaf3ed0-064a-3295-87c6-02b3adbd99b2 | -9.57524 | -55.16364 | 2026-09-12 05:10:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 412db136-1359-30dc-b1e1-f8a0d1a7a713 | -2.72599 | -57.64289 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 026f9098-1e37-39e9-871e-cf7843c8a8fa | -10.55056 | -51.33724 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0e15c110-ed1f-39ff-9ee3-5ec9cda2b710 | -9.90492 | -46.22839 | 2026-09-12 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 682107f3-ba81-3821-91d7-6aec7af52d08 | -6.92215 | -55.64953 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a76c446-5c40-3fe9-87d9-6d58ee99844b | -9.15666 | -49.98421 | 2026-09-12 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65458713-a5ba-3948-89de-f3b9c6f41310 | -6.84791 | -55.80775 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6172aa57-4202-3942-a9ca-18f1bd90e3cc | -6.79387 | -58.79344 | 2026-09-12 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 92021461-a700-3847-9620-804815f4f386 | -8.08114 | -54.84146 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28ed6fab-b76b-3e31-addd-fec7ce340043 | -4.86606 | -56.00275 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README36.md)
