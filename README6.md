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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 703e2536-3f96-32d9-a39b-659743c331dc | -14.3191 | -51.478001 | 2024-11-20 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aaa18207-a8d5-3896-9f36-9c67b40703b8 | -2.623 | -47.1147 | 2024-11-20 00:09:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb215d5-030b-3bf4-b352-5dafda6d8e17 | -3.7612 | -44.064098 | 2024-11-20 00:09:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f62a4e2-6398-363d-84a4-dc967d0ac426 | -1.6695 | -46.031898 | 2024-11-20 00:09:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e1930e7-b01d-3f79-b27d-565f262374c5 | -2.8215 | -46.667702 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7adae7dc-a123-36f2-acf7-a687880f39f6 | -5.0022 | -41.948101 | 2024-11-20 00:09:00 | METOP-B | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0865814d-771f-3715-8fe2-6c15031f407d | -4.6453 | -49.010601 | 2024-11-20 00:09:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a33b6af-96e9-3996-a52b-5c29e649624f | -2.6528 | -46.604 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5e140340-f4bd-31ad-943a-778b9ddca418 | -3.165 | -45.214401 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 02decfb6-adb6-372b-9924-c2e432c812bb | -3.3795 | -44.4282 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d93efb2c-d837-3a18-bd85-e0724e6f4a1c | -6.5184 | -44.1828 | 2024-11-20 00:09:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0dee53e-bf03-3e55-b8f2-14d7525cce42 | -5.135 | -44.124001 | 2024-11-20 00:09:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04b87e67-8539-3c64-86a6-1ce77d17c72c | -2.6438 | -46.150501 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bfd353d4-e299-3739-ba18-b1a686686c2c | -2.7227 | -51.812302 | 2024-11-20 00:09:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d165795-7b66-36b8-9907-043d88660627 | -5.2322 | -42.640202 | 2024-11-20 00:09:00 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9f294c36-9ec6-3655-bb26-40221d43f6f7 | -1.9838 | -46.6054 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b23d5a5-1e26-3278-8e07-210220b31372 | -2.0167 | -46.522099 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9f12460-afa0-3599-8b66-2f41a6d003b0 | -2.9085 | -44.167599 | 2024-11-20 00:09:00 | METOP-B | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 352886aa-b005-3a13-8ddb-9302996fa653 | -6.2702 | -44.7309 | 2024-11-20 00:09:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23a1db0e-4430-349a-8d97-9b804a0f9247 | -10.8075 | -44.405399 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36c49921-3fc1-32c6-8be6-64ed653f9bf2 | -1.4388 | -52.653198 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34deeb5c-f056-3d72-af30-e232ba8cb1eb | -3.8583 | -47.0723 | 2024-11-20 00:09:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e99be9a5-cd16-3365-99bb-7c3b53263faa | -5.7194 | -46.189701 | 2024-11-20 00:09:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 264d567c-f4c1-3ce5-ae78-91bd831fcbcb | -10.4399 | -44.888802 | 2024-11-20 00:09:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18badf4a-0a76-398b-97a2-7dc40771360a | -5.3692 | -45.445999 | 2024-11-20 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f27b2ea2-abeb-3e84-a53e-54a4bad0664f | -2.7414 | -45.3008 | 2024-11-20 00:09:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca3b69d3-ff04-3349-ad5c-4726b9e73674 | -3.3014 | -45.408798 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76d7a144-7049-3465-9eff-5250ede78227 | -5.4949 | -46.430099 | 2024-11-20 00:09:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 475ab0be-7fa3-37a2-ab74-9bbd98342556 | -3.2351 | -48.431599 | 2024-11-20 00:09:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f063ba-5e50-3756-a721-db2750b11a55 | -5.1448 | -44.121799 | 2024-11-20 00:09:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e884bb7e-4843-39bc-be4d-ac032ab64416 | -2.1998 | -46.466599 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a16b263-618d-39e3-9089-89e806da0768 | -3.1143 | -48.582001 | 2024-11-20 00:09:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d71b339f-8383-38f3-8ce8-3fdb2d1b965c | -2.6778 | -46.2104 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ca5ab63-76a3-3b66-b31d-966e9f1e672e | -3.2998 | -45.401901 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e1fd377e-9351-3065-9b24-832fdf5639ed | -4.2309 | -46.1115 | 2024-11-20 00:09:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff04f729-e002-3788-9a41-a8308cfd62c2 | -1.2382 | -53.3522 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2923eb0-092c-3e42-a2e0-476616002263 | -9.6317 | -36.3503 | 2024-11-20 00:09:00 | METOP-B | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e3786032-1177-3c86-984d-731dae3e6810 | -9.9207 | -44.487499 | 2024-11-20 00:09:00 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 865b5a66-3313-3e65-b98a-d07b44306541 | -1.6921 | -46.3153 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c514941-7df0-3587-a9cc-78016d156b40 | -2.643 | -46.606201 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a531119-c13c-3178-94e1-eda4624e09ae | -4.149 | -45.514599 | 2024-11-20 00:09:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e22de87-00ec-3766-aa19-868669260dbd | -3.3057 | -43.827301 | 2024-11-20 00:09:00 | METOP-B | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| affbf85c-0677-3e0f-bf07-6f7b67512417 | -10.0549 | -44.724899 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eb2d58e8-4884-3f78-894d-d3571243c0f1 | -1.0256 | -51.722801 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2f98ed8b-71e2-30cd-b7e5-89c452f67014 | -2.9893 | -45.441399 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ecce1c6e-cc88-34ae-89e5-aa4cccd8e497 | -4.4267 | -46.5755 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34eb0feb-838b-3fda-95a8-8b9ef2dcb3d8 | -4.3704 | -47.7603 | 2024-11-20 00:09:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 970146ae-941f-3e10-8cf6-0ef4dea5b01f | -2.4251 | -46.966499 | 2024-11-20 00:09:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e18551-a6ee-3cad-b009-32f1ef9f2681 | -3.2557 | -50.612598 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19316423-d358-3f42-9689-4461c6e6efc6 | -2.8198 | -46.660301 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 011992c6-ca8a-3138-98a7-b6fb9257743a | -4.4365 | -46.573299 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 694f8bbf-77a8-3e89-a313-c26774473b3a | -4.1424 | -43.972 | 2024-11-20 00:09:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8ef5cfc-e848-30ab-9ced-2e49a2acc667 | -2.6696 | -46.219799 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b3abc76a-2d4e-3eb4-ad34-7d6372ed1ebc | -5.4356 | -44.8209 | 2024-11-20 00:09:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 071ccecd-c90a-3d02-8a62-73fa1ab4de26 | -3.3103 | -45.494202 | 2024-11-20 00:09:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 33baa624-fb3f-3964-b3f6-754d3709a72c | -3.2582 | -44.4837 | 2024-11-20 00:09:00 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| acea36e4-1266-3e1e-8d15-ef488837a266 | -2.6413 | -46.552601 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f90130d-08df-312a-89a1-dc4893086791 | -2.65 | -46.224098 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 119f72a8-0e9a-3a76-8673-9d1b52dbc245 | -0.8889 | -51.752899 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e3d18d6e-17a7-319f-a462-ea005a0725e5 | -1.1268 | -51.672199 | 2024-11-20 00:09:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 075d236b-9e3a-3375-a762-0cb25702a63b | -2.8139 | -45.119202 | 2024-11-20 00:09:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a0cadb3f-2650-3b9a-b3b1-570e08558596 | -3.9981 | -43.243401 | 2024-11-20 00:09:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 615a424f-a929-3ce3-93bd-64d5549b9d3c | -5.3676 | -45.4389 | 2024-11-20 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbc7c4d1-09ef-38c3-8fdf-6d3d1f0c4001 | -1.6823 | -46.317501 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c912466-d74f-3fe3-811c-df8d3c0164b5 | -14.3153 | -51.457001 | 2024-11-20 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9568c98f-d176-3d5f-b32b-5e6b59c3f041 | -9.4884 | -43.185501 | 2024-11-20 00:09:00 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ed962de0-e3e4-3a63-b6a6-fc9be6cf1ba4 | -2.7385 | -45.700699 | 2024-11-20 00:09:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9893afba-851b-30be-9a60-dc424fb9b491 | -5.3638 | -44.960602 | 2024-11-20 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efdf29d7-9090-34f4-9ecd-56d9c59e24f6 | -5.434 | -44.813999 | 2024-11-20 00:09:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb601dd7-b6ae-3959-bc30-5c06f8e20530 | -2.6511 | -46.5966 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01d2244a-3c32-33c7-ab20-84dac9684327 | -2.961 | -49.279099 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb99a3b7-ffd6-312f-ab5e-cc67699ff275 | -2.6247 | -47.122398 | 2024-11-20 00:09:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1674196-53b5-3f73-8687-c85a193f6407 | -4.131 | -43.9674 | 2024-11-20 00:09:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32d66059-1d2f-3df1-b2fb-997c609cdc4e | -2.673 | -46.1889 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2aad1f46-798a-337c-9242-d7f9b87f7a72 | -2.6827 | -46.231899 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45f0218a-3970-30a1-830f-56b056e44354 | -3.0288 | -49.445801 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a0291f3-4c4f-3484-90da-80cd2200e28d | -2.1429 | -47.406898 | 2024-11-20 00:09:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48ab13bd-ee12-3534-b873-976650eff85d | -9.635 | -36.3638 | 2024-11-20 00:09:00 | METOP-B | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f0d5e7a-93c0-39bf-8cb5-755f9b3e8aa2 | -2.2112 | -46.4716 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 229e302e-d4c1-367d-a2ef-76912e7fc5be | -1.2978 | -52.388699 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66ae2856-5c4f-3209-a90e-a5b216b95e3a | -11.0525 | -41.618 | 2024-11-20 00:09:00 | METOP-B | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 59f8dfb4-8c4a-3ee3-966d-c3741df96dc1 | -2.6418 | -46.233398 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 641692fe-90cb-3688-a9e2-7875c1fbed3b | -1.136 | -53.487701 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 883394ae-e9c3-3564-a1fc-16651fa3ece8 | -3.3026 | -43.813599 | 2024-11-20 00:09:00 | METOP-B | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6067ff53-4377-36d3-ae9b-a6bfbc93ca97 | -10.2207 | -44.3078 | 2024-11-20 00:09:00 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cccd1cc4-57d6-3f3f-abea-c37e303714bb | -10.3877 | -44.460098 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0fd1a414-c6a2-3b5f-ac48-722d1cd28523 | -1.4908 | -47.4361 | 2024-11-20 00:09:00 | METOP-B | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1f06ff1-5a2b-33e4-95fb-e7977d732e86 | -7.9902 | -44.364399 | 2024-11-20 00:09:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03342eae-0af3-3182-961a-e873fa08b03f | -3.3697 | -44.064999 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4da3828b-aaca-32d1-8d80-6a11410cc4cd | -3.6112 | -42.403 | 2024-11-20 00:09:00 | METOP-B | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dbe51ad6-6e7b-3ae4-a6be-92c1903c2b8e | -2.6762 | -46.203201 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 081633e7-b0d8-375a-a225-0abd12df7226 | -10.3893 | -44.4674 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c4e6433-ccec-3a9e-b24b-0cfc9fb41bfd | -2.4015 | -45.622002 | 2024-11-20 00:09:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ef0a022-3991-3f67-b0cb-9bbcbcdb4ece | -2.6212 | -45.133099 | 2024-11-20 00:09:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb6c280-16ff-3389-a028-4ae3fba8f2f3 | -2.9097 | -49.417801 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39785778-2677-3c71-86bb-b770bc9900c7 | -1.992 | -46.596001 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4f20851-9052-3299-8b09-15556f6b8274 | -1.4065 | -46.786098 | 2024-11-20 00:09:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be526009-4f4e-35a5-b5be-7652ebcc1824 | -3.771 | -44.061901 | 2024-11-20 00:09:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cffd7478-8ee6-332e-8674-64fded714239 | -2.2604 | -53.595001 | 2024-11-20 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13bdaea0-29f9-33de-870f-0a7e0c0f7c68 | -5.4288 | -45.575298 | 2024-11-20 00:09:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
