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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 172c9d33-41a9-3bc9-9fad-c29fdaf35543 | -5.59412 | -44.19657 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2d97c11-049f-32d9-9e89-3e7eb42f4fa8 | -4.30969 | -48.09365 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 105150af-6468-3161-ae58-ef850601241d | -5.78045 | -45.74475 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9451e870-f7c0-3ac5-8d54-410860e0403a | -6.65797 | -42.82191 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 863e388f-1fdf-3447-8910-177d433cab1a | -7.23371 | -42.98406 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8d2e8c8d-eb4f-3c59-8dd6-2f84ec924833 | -4.31093 | -48.086 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef6838e0-2e4f-3b85-a6de-0de4f8178b9d | -6.0461 | -44.61747 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fe3b3c8-9329-39b8-b992-8c32e918bfb7 | -5.31576 | -45.30204 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 552377db-c924-363c-b388-226b3e4fe608 | -3.09194 | -47.01312 | 2025-10-04 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d505995d-78cc-34c0-86ee-9477531924e4 | -6.26798 | -42.79576 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 681a0d24-10cc-32a7-a1f6-9878b765bacd | -6.60423 | -44.31263 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87761f06-7be0-32fa-9c88-d4df006a3395 | -6.39402 | -43.61047 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e02bfdb-2a35-30f8-9f76-4a7dd4f1ac2a | -6.48298 | -45.65823 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3743d6e2-f6b5-3213-a970-e3acf4a8db4d | -6.46088 | -44.57024 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff4ae370-6e39-3497-8998-9236e079e25d | -6.87632 | -47.23541 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 0dba17f5-98a0-3bfd-8914-f465b451b62a | -7.34578 | -44.35027 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3f47c70f-0175-3bb3-9e11-9998a9a66c6a | -6.65298 | -42.8105 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2acd67dd-ac12-3a40-995f-df6676d025c2 | -5.69376 | -43.03409 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b0bb5bcd-2023-3d9d-95da-133b6289bc08 | -6.52195 | -42.49838 | 2025-10-04 04:12:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 038d0b3e-aae5-3d08-a99c-48e31a2990fb | -7.74675 | -42.5695 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7ce5062e-276e-3ce8-8e9a-50296f9358f2 | -6.24514 | -44.24762 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30a0083f-227e-36ee-90f7-d17a94a81f43 | -5.20091 | -45.07283 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f07cf882-a41e-3325-b811-eeae5dbe9f0f | -5.79231 | -44.36038 | 2025-10-04 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8997adca-cb4f-3609-afba-fa6a45c8ada2 | -4.50242 | -46.38042 | 2025-10-04 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19a3bbf9-90a9-382c-955a-ab4bb690facb | -6.37102 | -43.88279 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcba775d-42ea-3a90-b89c-9ed3ec06854b | -6.27988 | -45.08023 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64daf848-ee78-3333-881e-baab28324d9d | -6.772 | -44.81404 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1c24bd0-e290-3cc1-8ee4-a68108f9a4eb | -4.48237 | -43.89644 | 2025-10-04 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f32934d-ed75-385a-9feb-ec4db88834f9 | -5.83997 | -42.86243 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 48fdcb0b-2578-3e14-a131-2d79b1f9d54c | -6.24337 | -45.34847 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 069f7ecb-4cff-3c11-a474-fc0c00abad24 | -6.29545 | -42.49169 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5bfbd82a-cc9f-3fb7-8398-dce085a2f7bd | -3.8325 | -44.55396 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0455bc9-8f81-3ca1-9aa0-1bf2a62cd265 | -6.63257 | -43.7132 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6249e46-142c-3afc-bd70-a2b1df784931 | -5.4822 | -44.10911 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cf9d663e-c090-3e36-aee6-3bccb3a4cae9 | -7.80203 | -42.52071 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6fa72ae7-88b3-3fb1-8540-7817aa018e23 | -6.4625 | -44.58169 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 203c0ec4-b19a-3bce-9db9-f794fdcae341 | -7.5263 | -38.00087 | 2025-10-04 04:12:00 | NOAA-20 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34284f50-89ae-3f5b-8375-51764ca3f94a | -5.8819 | -42.52959 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a3a25f3d-c0cd-3f1d-92d5-3dd32fc590e8 | -5.63337 | -43.22291 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 24393fca-8e76-31a3-8218-4554e95a6700 | -6.27744 | -44.04479 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d99ce459-16bd-38ec-a50b-58118d1bc365 | -6.87408 | -44.50223 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 56356d37-bd61-35f5-ad5b-d0afe074eddf | -6.71709 | -42.16093 | 2025-10-04 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1de1453d-ea29-35ce-a418-b5fa880aa637 | -6.74985 | -42.16969 | 2025-10-04 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fdcf408f-1671-37e9-ba43-a3b1e0af4d78 | -5.46156 | -43.17054 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8ea254c-a500-3739-be99-d5f2e239dd95 | -6.67173 | -42.82057 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cdd03952-c4fc-3f98-88bb-79f8cb86fb8e | -5.50771 | -51.01708 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eab4ad9c-a61d-3efb-8609-e4ce8d61cba1 | -6.6048 | -44.30906 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9628e109-cdf8-3cd5-a46c-e4a7a5bea2bb | -7.7045 | -42.58079 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bf2693bb-7e61-3c6f-843a-04b0bdc58c3d | -5.98198 | -43.48804 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac0d40cf-fe68-3965-90c5-dff26aeeb314 | -6.23331 | -44.65389 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8ae046f-f09c-37b1-b30d-2d865653b96f | -6.05702 | -42.5178 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ebcc1888-d450-3a80-9ecd-ae1fe31feb7e | -7.35306 | -44.34774 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e54f383-4473-3924-88e2-2803aaf94580 | -4.89583 | -49.96595 | 2025-10-04 04:12:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27670123-5bf5-3ed3-9dc8-5ec1540acc48 | -6.71969 | -45.96215 | 2025-10-04 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a278b75-e549-3ecc-90f3-9ae28ba88529 | -7.04497 | -42.78003 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 429d82f4-ef40-365a-9555-0027a6d9b70d | -6.27547 | -42.44593 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1dbb4740-22f1-3c6e-bd07-834efa747e99 | -5.77211 | -43.61166 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbd88b17-49fb-3024-a391-2efcab9047fa | -4.95881 | -45.07048 | 2025-10-04 04:12:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| f103873f-9ac5-3f68-9c31-cac5ee867a0c | -4.60151 | -43.15171 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ece1b01f-278b-3566-8b16-a36209e4a529 | -5.97581 | -42.94753 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aa8b3c81-5b49-3f56-a7d1-084ada8cc5f5 | -2.73729 | -47.14654 | 2025-10-04 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1de16982-8d92-3819-9f5b-ee1fe7ee0ff3 | -5.48296 | -42.79893 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 28f757bd-5536-3b4e-b6be-073d3cb3efe5 | -5.32533 | -43.34415 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efdb2a4b-a71b-3e13-9a4e-c8f62ca77a03 | -6.24407 | -44.23267 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23629071-f0be-3462-afed-fd9e49e9e4d2 | -6.72837 | -45.97629 | 2025-10-04 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed4da430-da6d-3637-aaea-d47377f5c0fc | -7.74131 | -42.60445 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0cfb579a-84a5-3671-b594-8b0465447317 | -3.68342 | -49.0509 | 2025-10-04 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e12f46d5-5a18-34c0-9452-f14e264ecd3b | -6.03811 | -44.18236 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f998438e-6e61-3fa6-a09c-bb7ae0b5ef8a | -7.71838 | -42.60085 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d436e333-4a28-3a07-b949-9bc1d41777b3 | -6.22319 | -44.27714 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e74ce81-383a-3966-8a2b-c76f5d10d270 | -4.44648 | -43.2515 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e513aafc-7fc5-31a6-ab2a-1e584c8f3bbb | -5.85463 | -42.20557 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dc1da120-09ef-3be6-a500-b8ed76cd7b92 | -5.9582 | -43.48785 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22b75f95-944a-35b0-8b39-7757cb678ffe | -6.2854 | -42.44752 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e991afba-47d8-38f9-a3ed-6a23f3eaeaff | -7.75008 | -42.57001 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 50c9d063-f3a7-36c1-b538-d6d9d0534d20 | -3.69532 | -49.57243 | 2025-10-04 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cca0c105-e4f4-38ac-8f34-28f79c77bf62 | -7.34913 | -44.35081 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9969500-7cf4-3aed-8502-7604a9519705 | -5.94432 | -43.29673 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf7e359a-5603-360f-8f4a-054af48ec312 | -5.90703 | -42.78102 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9bcf4d22-c2b6-35ba-b6b0-df0d0a07645e | -7.37028 | -39.20513 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| e42b5cfb-4243-3df0-b95d-aa1ae4b5b952 | -5.96641 | -45.89329 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 950ad9b5-f801-3e58-ad7a-123973db5129 | -4.6087 | -43.14928 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 089df23a-c7c1-3e97-b63c-d4b97e7530a2 | -6.76298 | -44.80513 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 838d911e-949f-322c-8210-0db0552b7f7d | -4.95818 | -45.07433 | 2025-10-04 04:12:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 66c77657-e726-32a1-8884-02e30970296c | -6.67368 | -42.37633 | 2025-10-04 04:12:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10909a8b-edb7-3aed-8b3d-d7dcec8d1346 | -7.04693 | -43.22023 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cfc8ea64-fed4-3d50-b00c-4d892284bf4a | -6.77117 | -43.61025 | 2025-10-04 04:12:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de8cc315-43f0-3d55-b16d-369b1f29995c | -5.7411 | -42.92842 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 42ceb380-fd03-39fc-b06c-946f6545f4db | -4.61091 | -43.15674 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1be3d4f0-2a24-31e3-89e3-47feabf28735 | -5.90535 | -42.53303 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 44474cf4-fa98-34cd-85f4-94c59a5ab0b9 | -4.44978 | -43.23063 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f0dc948-bde4-30d1-bc32-a7ffde38aac0 | -5.45603 | -43.16259 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b55c48eb-affe-36b4-8f70-18e6aa10b134 | -6.6602 | -43.47504 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 875a2f96-40b2-3d97-8f8b-1df50987a81d | -6.07412 | -42.51693 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 0ae969bc-1811-3445-aa56-844e3e313d0e | -5.85777 | -44.13545 | 2025-10-04 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aef76771-52c4-34df-832b-411cfc4ec101 | -4.42012 | -46.41339 | 2025-10-04 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04fcd2dc-51c6-3c28-ba11-1fad91bab659 | -7.7708 | -44.16098 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4171ac5a-7721-3c99-b163-1576ebd9f25e | -6.55977 | -43.89163 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecd09f39-0914-3254-b741-9578d2e8cc41 | -6.44456 | -44.80058 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 596651d4-1b8e-3dd8-ae91-af246fb7c650 | -7.16228 | -46.21876 | 2025-10-04 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README55.md)
