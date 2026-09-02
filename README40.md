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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52937f59-8e89-3a59-a909-c4cd2c1ae891 | -9.95085 | -53.99433 | 2026-09-02 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edd1f9d9-d8ff-34ad-9e3b-fc9b40d70233 | -10.40824 | -50.00386 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53d18386-e6db-3340-92e2-0b295def5a84 | -11.53774 | -45.48522 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbd05792-e562-3c2c-b116-84c83631b5c6 | -8.50311 | -55.30232 | 2026-09-02 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 303cff9d-a51f-3685-9036-2efeef891b79 | -8.4546 | -54.69701 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e2523ea-20e8-353b-ab6f-05adcdf3663d | -7.54881 | -54.99752 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5d2feeeb-5f27-3de5-919b-75353540872c | -6.80999 | -59.56256 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dc55d7e-b291-361e-8be4-6b4cf8ff601c | -8.56535 | -63.1822 | 2026-09-02 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96dd94cb-f99b-3748-9287-265cf7dc7508 | -8.46344 | -54.73292 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 864d1e45-f8f1-3b14-a2cd-b4ac345b6ba5 | -6.75894 | -59.44023 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2cd8eaff-7952-3bc3-9b52-c13c730d3831 | -11.81583 | -46.03147 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9a3385e3-ac6c-3a36-a9a8-4f328d61de99 | -8.43009 | -54.71015 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0a9784ab-0149-3f25-9558-58411c788d8c | -11.47971 | -45.08379 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 750c99f9-6aae-33cd-ab12-9ebc7b961d03 | -10.51187 | -57.44372 | 2026-09-02 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2813bfb7-6e64-3c3f-9738-a90f9d08a7af | -6.85415 | -59.48223 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30019488-2ac3-33d3-8707-2e6c4c9f8de1 | -6.59722 | -59.11249 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cde295e-54d4-35e3-bfd2-fd89caa0525a | -10.49349 | -59.60806 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71147add-9f92-3f20-9c86-ce965c994eab | -10.70712 | -46.20175 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50222240-4e34-373e-9391-402ed2083b12 | -10.32132 | -49.9562 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57c2dc2e-5bf8-325b-8816-f727d88c8fae | -10.05248 | -46.67737 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8f5fd42-d845-3fca-8a07-c830a80901d6 | -7.20864 | -60.67354 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af5cbc37-c564-3956-8fcf-0ab956e885af | -8.4272 | -54.7053 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 97ff4bfe-9634-3f80-934c-d6cf38e5c55e | -10.49245 | -64.33131 | 2026-09-02 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9ea8b46-bfb4-3501-93be-bd6ae0d491ec | -8.45821 | -54.69763 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7cef8ca-feb2-33b3-a4f0-2b9e3bbfed68 | -9.46633 | -56.74199 | 2026-09-02 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1718eb4a-ad73-3078-b590-e5f11b9dbaec | -8.49133 | -54.58823 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4e988b3-a074-3cbb-a9ec-dfcdb46c27a2 | -8.46403 | -54.7072 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39d1e200-48fa-32ba-8477-e24c1fd3e54e | -12.14928 | -47.12365 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0fe8ff4-dee9-37b3-81e6-cfbed821678c | -11.30393 | -45.17653 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35e33a3e-a2f5-311d-bfff-9fd77058ea44 | -6.08954 | -53.80643 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dc40fe7-8bec-314c-a1f7-979ce5f23478 | -6.64685 | -59.43733 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5c5f61a7-c236-30ac-b960-08dfbd9e3cb6 | -9.70799 | -54.33457 | 2026-09-02 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e253a08-d44a-3304-a616-5a74ac1666e7 | -7.36122 | -60.61004 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6269fa9a-f75a-35ba-8cd2-ed132f7f9850 | -6.81451 | -59.56657 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65a90c4e-f09c-36fe-825c-0dbc7e5f3eda | -10.31209 | -50.04007 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab208200-8fdf-3d91-b55d-50e9b3103a89 | -8.9092 | -50.56653 | 2026-09-02 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4887529e-6d7e-37c3-b218-584011f78959 | -12.14621 | -47.11565 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c14075a4-67ae-32c7-9a09-f2ed9765aa10 | -5.9091 | -53.56653 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4923537f-ebab-3297-af71-1f1af756d051 | -5.87083 | -57.77926 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a77dfd4d-2d31-3e51-80dc-1a67015eaa64 | -11.30718 | -45.15197 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 881c86cf-7b35-3c9a-9617-dbcfe26a5f7b | -12.15132 | -47.13905 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb625eba-1ac3-3b23-8795-67c1eca27bda | -11.95548 | -45.03807 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e145d9f6-c9ec-347a-8212-209840d84b68 | -6.18294 | -57.73471 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d52eb1a3-de99-3c86-acf3-d2d81fcd567e | -7.29427 | -49.8195 | 2026-09-02 04:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baeb8564-2eb2-3710-8c2a-1b5c55a88f48 | -10.79653 | -44.74812 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11d407f6-13eb-3d68-b8ac-51dcf96fd4c1 | -11.67694 | -50.47528 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99f29391-6fa9-3410-b6fc-488c50795f56 | -11.35563 | -50.61884 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5b6477c-8f4f-33d5-9794-7c48ce59570e | -10.75051 | -54.03096 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a384adb6-e3bf-3b1f-b8d2-f794c2f08484 | -8.44384 | -54.71675 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19229c75-01a1-38ca-891a-3bad8201f62a | -6.14703 | -55.679 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 123f9567-8f5e-36f0-abea-25d1fcb397d9 | -11.29733 | -45.19085 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99588c05-2793-3b12-b5fd-2614fb598126 | -9.15366 | -49.97797 | 2026-09-02 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efa499aa-b856-3e4e-a9d1-763a0e03ea41 | -8.4337 | -54.71077 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30ff77c4-27a9-301d-947b-62d50ca66672 | -11.29929 | -45.17598 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 13677f42-f007-32bd-bf84-6bfd132c9b81 | -5.33497 | -60.15014 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75a5b132-b9fd-331c-92dc-14a4f49c1e12 | -10.32939 | -49.94965 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e85dd211-8c3f-31ea-863d-dfd46d1b2beb | -11.82646 | -46.05592 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4da19a85-ab18-3afe-80a9-4b7e23190889 | -5.8754 | -57.77989 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3f4d719-b8aa-39e3-8f05-d8947f7fd636 | -6.79821 | -59.39379 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9f7939e-d9a5-3f07-ac30-f63360ad69fa | -8.26709 | -62.75988 | 2026-09-02 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93d7137f-a224-39ce-9314-224d7eb0b7d1 | -14.11516 | -45.50555 | 2026-09-02 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3f9d1be-ae4b-3a89-94d9-ab83c88fa9fa | -12.14418 | -47.06988 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f8bdf69-5f4a-3846-8f47-20da609a5434 | -9.39676 | -51.60071 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 560dda4e-5785-35d5-ab4f-ff919e8727dd | -6.93029 | -59.64063 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04e4061e-29d3-3507-b494-6233f2cf4ff8 | -9.69797 | -47.20686 | 2026-09-02 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5ed9fbc-83ec-3d41-a50e-99689058a749 | -7.64782 | -45.87417 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b7fc993-6461-3afe-8fcc-244fbd9c5b3d | -12.13336 | -47.05689 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 053a4114-5147-3ac2-bd64-0efd7cf18d7c | -7.29046 | -52.35878 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9b3bedc-9491-3054-9c94-ca375706d83f | -9.83727 | -59.47173 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a98d4ce-c3e3-3fba-b520-be35e0149e67 | -11.35693 | -45.40676 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59af2735-0d8e-382b-aaee-8633a5139807 | -8.42725 | -54.70263 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e5d76ea-c7b6-3df6-894b-188122b9e233 | -8.12148 | -51.6644 | 2026-09-02 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e079bee6-9cdf-3ec9-b261-6cec4e2cbebd | -8.44455 | -54.71257 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7ad520e-8612-3f43-98b8-a0dd7fa92931 | -8.76265 | -62.58809 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f655bf2-bb81-33a0-9ef7-583d5cc375f9 | -12.06131 | -45.00185 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf3229fe-68c3-3f65-b523-bdd139d6f5e6 | -6.26055 | -55.42907 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5d7c10b-2e10-36a8-a591-d735bb409f32 | -9.00528 | -50.77858 | 2026-09-02 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 29d0ef93-9306-384f-8d5d-cf1b9266110e | -11.03936 | -49.66771 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59189a0a-09c7-3c64-b204-2c60de9773b1 | -6.769 | -59.44184 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b8e758bf-dbc9-3527-a4df-f3a9e4ef10b7 | -12.64516 | -47.08941 | 2026-09-02 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66947db3-61fb-3a3c-b7a2-8f740ec9635c | -9.09096 | -65.38154 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3cd5f02-d96c-3dcc-996d-19fc7d8d5f95 | -12.13338 | -47.14767 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 35effbf3-7d52-323a-ad27-c2257d621fa6 | -10.04517 | -48.69379 | 2026-09-02 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 93a8da7b-0f79-313f-b427-edd8a61eba53 | -6.93311 | -59.64018 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64254ea0-95ac-30ec-ac01-45fc1dc28e1a | -11.36083 | -45.41212 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 633c56cf-1a9a-3702-b05d-8959327a7776 | -8.44967 | -54.72634 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96775a10-5dd4-3637-8d6e-e122da1d54e9 | -12.05664 | -45.0007 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d08a0fc-790c-3ac0-95e7-d81d1c73b848 | -11.26841 | -45.13451 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f17cc7ef-42cb-3272-a686-5a6aa21968df | -6.14787 | -55.67399 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa0cee02-2dc5-3e96-a7e6-3228fa80d814 | -8.74932 | -62.57655 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 01b852fb-e278-303b-8d6c-0f2fa94ef92c | -7.20009 | -60.68982 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed501a0a-bac7-3255-b99c-e12de7abaef7 | -12.00838 | -60.53625 | 2026-09-02 04:57:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a07d037d-69f2-3df4-bc21-9f83bb3975e4 | -10.67965 | -54.03946 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f6be8d0e-b98a-3501-a89a-01a3dce511a9 | -9.41005 | -51.60282 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c3f0e713-c186-3415-828b-0a61da7f8d73 | -6.80828 | -59.10088 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 38159b1f-b6ab-3d53-9740-cfcc3faffa83 | -11.84255 | -46.03606 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7953a14e-91be-38a2-8521-f63773369488 | -11.65576 | -50.19588 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb2034aa-b0e7-389a-abbd-4dffe5d1066d | -12.37096 | -53.19022 | 2026-09-02 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 948592fd-0d66-3d30-b492-06f5d002aa19 | -7.76875 | -61.1994 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7c55e8d-4743-3739-bf7d-09c7a9a1bb0f | -6.72492 | -50.46479 | 2026-09-02 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README41.md)
